#!/usr/bin/env python3
"""Standalone exact-arithmetic verification of 2-D perfect evolution algebra automorphisms.
No third-party packages. This independently tests monomial maps against all basis products.
"""
from collections import Counter
from math import gcd

SPECS = [(2,1,None),(3,1,None),(2,2,(1,1,1)),(5,1,None),
         (7,1,None),(2,3,(1,1,0,1)),(3,2,(1,0,1)),
         (11,1,None),(13,1,None),(2,4,(1,1,0,0,1))]


def field_tables(p, m, modulus):
    q = p**m
    digs=[]
    for v in range(q):
        v0=v; row=[]
        for _ in range(m):
            row.append(v0%p); v0//=p
        digs.append(row)
    def encode(ds):
        return sum(x*(p**i) for i,x in enumerate(ds[:m]))
    plus=[[encode([(digs[x][i]+digs[y][i])%p for i in range(m)]) for y in range(q)] for x in range(q)]
    neg=[encode([(-digs[x][i])%p for i in range(m)]) for x in range(q)]
    mul=[[0]*q for _ in range(q)]
    for x in range(q):
        for y in range(q):
            c=[0]*(2*m-1)
            for i in range(m):
                for j in range(m): c[i+j]=(c[i+j]+digs[x][i]*digs[y][j])%p
            if m>1:
                for k in range(2*m-2,m-1,-1):
                    t=c[k]
                    for j in range(m): c[k-m+j]=(c[k-m+j]-t*modulus[j])%p
            mul[x][y]=encode(c)
    assert all(mul[1][x] == x for x in range(q))
    for x in range(1,q):
        assert any(mul[x][y] == 1 for y in range(1,q)), 'bad polynomial'
    return plus,neg,mul


def expected(q,p):
    h=gcd(2,q-1)
    g=gcd(3,q-1)
    s=(q-1)**2
    total=q*(q-1)**2*(q+1)
    c={2:s*(q-h)}
    if g==3:
        c[3]=2*s//3
        c[6]=s//3
    else:
        c[2]+=s
    c[1]=total-sum(c.values())
    simple_total=s*(q*q-q+1)
    simple_nontrivial=s*(q-h)
    assert (sum(c.values()) == total)
    return c,simple_total,simple_nontrivial


def compute(p,m,modulus):
    q=p**m
    plus,neg,M=field_tables(p,m,modulus)
    nonz=range(1,q)
    sq=[M[x][x] for x in range(q)]
    powers=[(u,v,sq[u],sq[v]) for u in nonz for v in nonz]
    hist=Counter(); simple=Counter()
    for a in range(q):
      for b in range(q):
       for c in range(q):
        for d in range(q):
         if M[a][d]==M[b][c]:
          continue
         count=0
         for u,v,u2,v2 in powers:
          # T(e1)=u e1, T(e2)=v e2
          if M[a][u]==M[u2][a] and M[b][v]==M[u2][b] and M[c][u]==M[v2][c] and M[d][v]==M[v2][d]:
           count+=1
          # T(e1)=u e2, T(e2)=v e1
          if M[b][v]==M[u2][c] and M[a][u]==M[u2][d] and M[d][v]==M[v2][a] and M[c][u]==M[v2][b]:
           count+=1
         hist[count]+=1
         if b and c:
          simple[count]+=1
    prediction,simple_total,simple_nontriv=expected(q,p)
    assert hist == Counter(prediction), (q,hist,prediction)
    assert sum(simple.values())==simple_total, (q,simple)
    assert sum(v for k,v in simple.items() if k>1)==simple_nontriv, (q,simple)
    # Burnside orbit census must agree with Wei-Zou's n=2 table.
    orbits=sum(k*v for k,v in hist.items())//(2*(q-1)**2)
    h=gcd(2,q-1)
    predicted_orbits=((q+1)**2-h+ (2 if (q-1)%3==0 else 0))//2
    assert orbits==predicted_orbits, (q,orbits,predicted_orbits)
    print('q=%2d |GL_2|=%5d aut=%s simple=%s classes=%d' % (q,sum(hist.values()),dict(sorted(hist.items())),dict(sorted(simple.items())),orbits))


def main():
    for spec in SPECS:
        compute(*spec)
    print('VERIFY_OK')

if __name__=='__main__':main()
