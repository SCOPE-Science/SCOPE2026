from math import gcd

def p(n):
    # Binary-polynomial representation of the Dickson recurrence.
    assert n>=0
    a,b=0,2
    for k in range(n): a,b=b,((b<<1)^a)
    return a

def divmod2(a,b):
    q=0
    while a and a.bit_length()>=b.bit_length():
        k=a.bit_length()-b.bit_length();q^=1<<k;a^=b<<k
    return q,a

def gcd2(a,b):
    while b: a,b=b,divmod2(a,b)[1]
    return a

def mult(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c

def rank(rows):
    piv={}
    for v in rows:
        while v:
            k=v.bit_length()-1
            if k not in piv: piv[k]=v;break
            v^=piv[k]
    return len(piv)

def row(r,t):
    # Independently construct Rule 90 spacetime Laurent forms.
    arr={r:1}
    for j in range(t):
        d={}
        for i,v in arr.items():
            d[i-1]=d.get(i-1,0)^v
            d[i+1]=d.get(i+1,0)^v
        arr=d
    return [i for i,v in arr.items() if v]

def rank_triple(s,t,n):
    B=3*n; off=n*2+t+2
    rows=[]
    for i in (0,s,t):
        for j in range(n):
            bits=0
            for k in row(i,j):bits ^= 1<<(k+off)
            rows.append(bits)
    return rank(rows)

for s in range(1,15):
 for t in range(s+1,17):
  g=gcd(s,t); ps=p(s);pt=p(t);pd=p(t-s)
  assert gcd2(ps,pt)==p(g),(s,t,ps,pt,p(g),gcd2(ps,pt))
  assert divmod2(ps,p(g))[1]==0
  assert divmod2(pt,p(g))[1]==0
  assert divmod2(pd,p(g))[1]==0
  assert max(x.bit_length()-1 for x in (divmod2(ps,p(g))[0],divmod2(pt,p(g))[0],divmod2(pd,p(g))[0]))==t-g
  for n in range(1,12):
   q=rank_triple(s,t,n)
   expect=3*n-max(0,n-(t-g))
   assert q==expect,(s,t,n,q,expect)
print('OK: all 119 spacing pairs, 1309 independently ranked finite sensor configurations, GF2 gcd identities')
