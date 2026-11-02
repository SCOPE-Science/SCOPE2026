#!/usr/bin/env python3
"""Direct finite-group multiplication and quotient-embedding checks."""

def divisors(n): return [d for d in range(1,n+1) if n%d == 0]

def make_group(m):
    n=2*m; es=[(i,s) for s in (0,1) for i in range(n)]; ix={x:k for k,x in enumerate(es)}
    mult=[[ix[((i+(-1)**s*j+m*s*t)%n,s^t)] for (j,t) in es] for i,s in es]
    inv=[next(j for j in range(len(es)) if mult[i][j]==0 and mult[j][i]==0) for i in range(len(es))]
    return es,mult,inv

def closure(gens,mult,inv):
    gg=list(set(gens+[inv[x] for x in gens])); found={0}; todo=[0]
    while todo:
        x=todo.pop()
        for y in gg:
            z=mult[x][y]
            if z not in found: found.add(z);todo.append(z)
    return frozenset(found)

def all_normal(m,es,mult,inv):
    g=len(es); a=1;b=2*m
    sub={closure([i,j],mult,inv) for i in range(g) for j in range(g)}
    normal=[]
    for h in sub:
        if all(mult[mult[inv[t]][z]][t] in h for t in [a,b] for z in h):normal.append(h)
    return sub,normal

def quotient(H,mult):
    n=len(mult); mapping={}; cosets=[]
    for x in range(n):
        if x in mapping:continue
        c={mult[x][h] for h in H}; idx=len(cosets)
        assert not (c&set(mapping))
        cosets.append(tuple(sorted(c)))
        for y in c: mapping[y]=idx
    tbl=[[mapping[mult[x[0]][y[0]]] for y in cosets] for x in cosets]
    assert mapping[0]==0
    return tbl,mapping

def elemorder(x,mult):
    y=0
    for i in range(1,len(mult)+1):
        y=mult[y][x]
        if y==0:return i
    raise RuntimeError('nonfinite')

def power(x,k,mult):
    y=0
    for _ in range(k): y=mult[y][x]
    return y

def embed(kind,d,tbl):
    n=len(tbl); out=[]
    for a in range(n):
        if elemorder(a,tbl)!=d:continue
        a_inv=power(a,d-1,tbl)
        asub={power(a,j,tbl) for j in range(d)}
        for b in range(n):
            if b in asub:continue
            if kind=='D':
                if tbl[b][b]!=0:continue
            else:
                if tbl[b][b]!=power(a,d//2,tbl):continue
            bi=next(i for i in range(n) if tbl[b][i]==0 and tbl[i][b]==0)
            if tbl[tbl[bi][a]][b]!=a_inv:continue
            # <a,b> consists of <a> and b<a>, automatically size 2*d when distinct.
            out.append((a,b))
    return bool(out)

def predicted_rel(x,y):
    if x==('T',0):return True
    if y==('T',0):return x==('T',0)
    if x==('D',1):return True
    if y==('D',1):return x==('D',1)
    if x[0]!=y[0]:return False
    return y[1]%x[1]==0

def test(m):
    es,mult,inv=make_group(m); sub,normals=all_normal(m,es,mult,inv)
    cand={closure([d%(2*m)],mult,inv) for d in divisors(2*m)}
    cand.add(frozenset(range(4*m)))
    if m%2==0:
        cand|={closure([2,2*m+r],mult,inv) for r in (0,1)}
    assert set(normals)==cand,(m,len(normals),len(cand))
    nodes={}
    for H in normals:
        tbl,mapping=quotient(H,mult)
        if len(H)==4*m: typ=('T',0)
        elif all(s==0 for i,s in (es[x] for x in H)):
            d=min(x for x in range(1,2*m+1) if x==2*m or x in H)
            typ=('D',d) if m%d==0 else ('Q',d)
        else:typ=('D',1)
        size=len(tbl)
        assert size==({'T':1,'D':2,'Q':2}[typ[0]]*typ[1] if typ[0]!='T' else 1)
        invol=sum(tbl[i][i]==0 for i in range(1,size))
        if typ[0]=='D': assert invol==typ[1]+(typ[1]%2==0) if typ[1]>1 else invol==1
        if typ[0]=='Q': assert invol==1
        if typ in nodes: assert len(tbl)==len(nodes[typ][0])
        nodes[typ]=(tbl,H)
    expected={('D',d) if m%d==0 else ('Q',d) for d in divisors(2*m)}|{('T',0)}
    assert set(nodes)==expected,(m,set(nodes)^expected)
    # A source embeds into a target if explicit generators of the presentation have images.
    actual_embed={}
    for x,(tx,Hx) in nodes.items():
      for y,(ty,Hy) in nodes.items():
        should=predicted_rel(x,y)
        if x[0]=='T': actual=True
        elif y[0]=='T':actual=False
        else:actual=embed(x[0],x[1],ty)
        assert actual==should,(m,x,y,actual,should)
        actual_embed[(x,y)]=actual
    # The actual QIso order is the reverse of quotient-group embedding.
    le=lambda x,y: actual_embed[(y,x)]
    lacks=[]
    for ii,x in enumerate(nodes):
      for y in list(nodes)[ii+1:]:
        ub=[z for z in nodes if le(x,z) and le(y,z)]
        lb=[z for z in nodes if le(z,x) and le(z,y)]
        joins=[z for z in ub if all(le(z,w) for w in ub)]
        meets=[z for z in lb if all(le(w,z) for w in lb)]
        assert len(joins)==1,(m,x,y,joins)
        assert len(meets)<=1,(m,x,y,meets)
        if not meets:lacks.append((x,y))
    u=m
    while u%2==0:u//=2
    assert len(lacks)==len(divisors(u))*(len(divisors(m))-1),(m,lacks)
    min_nodes=[x for x in nodes if not any(le(z,x) and z!=x for z in nodes)]
    assert set(min_nodes)=={('D',m),('Q',2*m)},(m,min_nodes)
    print('m=%2d |G|=%2d subgroups=%2d normal=%2d quotient_types=%2d exact-embeddings=OK' %
          (m,4*m,len(sub),len(normals),len(nodes)))
    print('        missing-meet-pairs=%d; two minimal classes=OK; all joins=OK'%len(lacks))

if __name__=='__main__':
    for m in range(2,13):test(m)
    print('VERIFY_OK')
