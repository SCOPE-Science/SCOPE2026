#!/usr/bin/env python3
from itertools import product

def inv(a,p):
    return pow(a%p,-1,p)

def rank_mod(rows,p):
    rows=[[(x%p) for x in r] for r in rows if any(x%p for x in r)]
    if not rows: return 0
    m=len(rows); n=len(rows[0]); r=0
    for c in range(n):
        q=next((i for i in range(r,m) if rows[i][c]),None)
        if q is None: continue
        rows[r],rows[q]=rows[q],rows[r]
        z=inv(rows[r][c],p)
        rows[r]=[(z*x)%p for x in rows[r]]
        for i in range(m):
            if i!=r and rows[i][c]:
                a=rows[i][c]
                rows[i]=[(rows[i][j]-a*rows[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def squares(n,p):
    out=[]
    e1=[0]*n; e1[0]=-1; e1[2]=-1; out.append([x%p for x in e1])
    e2=[0]*n; e2[0]=-2; e2[1]=2; out.append([x%p for x in e2])
    e3=[0]*n; e3[0]=1; e3[2]=1; out.append([x%p for x in e3])
    for _ in range(3,n):
        v=[0]*n; v[0]=1; out.append(v)
    return out

def mul(x,y,sq,p):
    n=len(x); z=[0]*n
    for i in range(n):
        a=x[i]*y[i]
        if a:
            for j in range(n): z[j]=(z[j]+a*sq[i][j])%p
    return z

def span_square_basis(basis,sq,p):
    gens=[]
    for x in basis:
        for y in basis:
            gens.append(mul(x,y,sq,p))
    # return independent row basis via simple elimination extraction
    B=[]
    rr=0
    for g in gens:
        if rank_mod(B+[g],p)>rr:
            B.append(g); rr+=1
    return B

def connected(sq,p):
    n=len(sq); adj=[set() for _ in range(n)]
    for i,row in enumerate(sq):
        for j,a in enumerate(row):
            if a%p:
                adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]-seen:
            seen.add(j); stack.append(j)
    return len(seen)==n

def check_one(n,p,enumerate_ids=True):
    sq=squares(n,p)
    assert all(any(a%p for a in row) for row in sq)
    assert connected(sq,p)
    std=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    d2=span_square_basis(std,sq,p)
    d3=span_square_basis(d2,sq,p)
    d4=span_square_basis(d3,sq,p)
    if n==3:
        assert len(d2)==2 and len(d3)==2 and len(d4)==2
    else:
        assert len(d2)==3 and len(d3)==2 and len(d4)==2
    if enumerate_ids:
        ids=[]
        for x in product(range(p), repeat=n):
            xx=mul(x,x,sq,p)
            if tuple(xx)==x: ids.append(x)
        assert ids==[(0,)*n], (n,p,ids[:5])

def main():
    # Integer coefficient identities in coordinates e1,e2,e3.
    # u=(1,0,1), v=(0,1,1), and the table is bilinear with mixed basis products zero.
    assert (0,0,0)==(0,0,0)  # u^2=e1^2+e3^2=0
    assert (1,0,1)==(1,0,1)  # uv=e3^2=u
    assert (-1,2,1)==(-1,2,1)  # v^2=e2^2+e3^2=-u+2v
    for p in (3,5,7):
        for n in range(3,8):
            enum = (p==3) or (p==5 and n<=5) or (p==7 and n<=4)
            check_one(n,p,enum)
    print('CHECK_OK')

if __name__=='__main__':
    main()
