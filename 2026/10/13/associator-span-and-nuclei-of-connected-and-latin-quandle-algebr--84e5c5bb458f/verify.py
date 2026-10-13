#!/usr/bin/env python3
"""Finite-table checks for associator span and three nuclei of Latin quandle algebras."""

def affine(n,a):
    return [[(a*x+(1-a)*y)%n for y in range(n)] for x in range(n)]

def tetrahedral():
    # q(x,y)=phi(x)+(I-phi)(y) over F2^2, phi(s,t)=(t,s+t).
    def phi(v): return ((v>>1)&1) | ((((v&1)^((v>>1)&1))&1)<<1)
    return [[phi(x) ^ (y ^ phi(y)) for y in range(4)] for x in range(4)]

def galkin5():
    table=[]
    for x in range(3):
      for a in range(5):
        row=[]
        for y in range(3):
          for b in range(5):
            mu=2 if (x-y)%3==0 else -1
            row.append(((2*y-x)%3)*5+((-a+mu*b)%5))
        table.append(row)
    return table

def transpositions_s4():
    ps=[]
    for i in range(4):
        for j in range(i+1,4):
            perm=list(range(4)); perm[i],perm[j]=perm[j],perm[i]
            ps.append(tuple(perm))
    idx={x:i for i,x in enumerate(ps)}
    def compose(x,y):return tuple(x[y[k]] for k in range(4))
    return [[idx[compose(compose(y,x),y)] for y in ps] for x in ps]

def rank_mod(rows,p,n):
    pivots={}
    for row in rows:
        v=[x%p for x in row]
        while True:
            lead=next((i for i,t in enumerate(v) if t),None)
            if lead is None:break
            if lead not in pivots:
                inv=pow(v[lead],-1,p)
                pivots[lead]=[(inv*t)%p for t in v]
                break
            pivot=pivots[lead]
            c=v[lead]
            for j in range(lead,n):v[j]=(v[j]-c*pivot[j])%p
        if len(pivots)==n: return n
    return len(pivots)

def verify(table,name):
    n=len(table)
    assert all(len(row)==n for row in table)
    assert all(table[x][x]==x for x in range(n))
    assert all(len({table[x][y] for x in range(n)})==n for y in range(n)), 'rack'
    latin=all(len(set(table[x]))==n for x in range(n))
    if name != 'transposition6':assert latin, 'latin'
    for x in range(n):
        for y in range(n):
            for z in range(n):
                assert table[table[x][y]][z] == table[table[x][z]][table[y][z]], 'self-dist'
    reached={0}; changed=True
    while changed:
        old=len(reached)
        reached.update(table[x][y] for x in list(reached) for y in range(n))
        changed=(len(reached)!=old)
    assert len(reached)==n, 'connected by right translations'
    if name=='transposition6':assert not latin, 'nonlatin control'
    if name=='galkin15':
        witness=next(((x,y,z,w) for x in range(n) for y in range(n) for z in range(n) for w in range(n) if table[table[x][y]][table[z][w]]!=table[table[x][z]][table[y][w]]),None)
        assert witness,'nonmedial witness'
        print('NONMEDIAL',witness)
    # Coefficient vectors for associator with variable in chosen position.
    for p in (2,3):
        assoc=[]; equations=[[],[],[]]
        for x in range(n):
          for y in range(n):
            for z in range(n):
              l=table[table[x][y]][z]
              r=table[x][table[y][z]]
              v=[0]*n; v[l]+=1;v[r]-=1
              assoc.append(v)
              for i in range(n):
                # Associator for variable at first place.
                ll=table[table[i][y]][z]; rr=table[i][table[y][z]]
                a=[0]*n;a[ll]+=1;a[rr]-=1
                equations[0].append(a)
                # middle place
                ll=table[table[x][i]][z]; rr=table[x][table[i][z]]
                b=[0]*n;b[ll]+=1;b[rr]-=1
                equations[1].append(b)
                # right place
                ll=table[table[x][y]][i]; rr=table[x][table[y][i]]
                c=[0]*n;c[ll]+=1;c[rr]-=1
                equations[2].append(c)
        ra=rank_mod(assoc,p,n)
        nullities=[n-rank_mod(eq,p,n) for eq in equations]
        assert ra==n-1,(name,p,ra)
        assert nullities[0]==1 and (not latin or nullities==[1,1,1]),(name,p,nullities)
        print('VERIFIED',name,'p',p,'n',n,'assoc_rank',ra,'nuclei_dim',nullities)

if __name__=='__main__':
    for name,table in [('dihedral3',affine(3,2)),('dihedral5',affine(5,4)),('tetrahedral4',tetrahedral()),('galkin15',galkin5()),('transposition6',transpositions_s4())]:
        verify(table,name)
    print('VERIFY_OK')
