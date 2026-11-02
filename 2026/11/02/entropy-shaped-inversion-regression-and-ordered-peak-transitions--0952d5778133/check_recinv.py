from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import comb

def gen_dist(n,p):
    d={(1,):F(1)}
    for j in range(1,n):
        out=defaultdict(F)
        for perm,m in d.items():
            for at in range(j):
                x=perm[at]
                uplift=tuple(v+(v>x) for v in perm)
                for desc,prob in ((0,p),(1,1-p)):
                    newer=(x,x+1) if desc==0 else (x+1,x)
                    newperm=uplift[:at]+newer+uplift[at+1:]
                    out[newperm]+=m*prob/j
        d=out
    assert sum(d.values())==1
    return d

def W(n,k):
    H=lambda a:sum((F(1,i) for i in range(1,a+1)),F(0))
    return n*H(n-1)-k*H(k-1)-(n-k)*H(n-k-1)-1

def perm_des(p):return tuple(int(p[i]>p[i+1]) for i in range(len(p)-1))
def inv(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
checks=0
for n in range(2,8):
 for p in (F(1,2), F(2,3)):
    d=gen_dist(n,p); q=1-p
    agg=defaultdict(F); mass=defaultdict(F)
    for perm,pr in d.items():
       s=perm_des(perm);agg[s]+=inv(perm)*pr;mass[s]+=pr
    assert len(agg)==2**(n-1)
    for s in product((0,1),repeat=n-1):
       theoretical_mass=F(1)
       for bit in s:theoretical_mass*=q if bit else p
       assert mass[s]==theoretical_mass
       expected=sum(W(n,k)*s[k-1] for k in range(1,n))
       assert agg[s]==expected*mass[s],(n,p,s,agg[s],expected,mass[s])
       checks+=2
    meansI=sum(inv(perm)*pr for perm,pr in d.items())
    assert meansI==q*comb(n,2)
    assert sum(W(n,k) for k in range(1,n))==comb(n,2)
    for k in range(1,n):
      joint=sum(inv(perm)*perm_des(perm)[k-1]*pr for perm,pr in d.items())
      assert joint-meansI*q==p*q*W(n,k)
      checks+=1
    checks+=2
    for i in range(2,n):
      pexpect=p*q
      cov=sum(inv(perm)*int(perm[i-2]<perm[i-1]>perm[i])*pr for perm,pr in d.items())-meansI*pexpect
      expected=p*q*(p*W(n,i)-q*W(n,i-1))
      assert cov==expected,(n,p,i,cov,expected)
      checks+=1
    ts=[W(n,i-1)/(W(n,i-1)+W(n,i)) for i in range(2,n)]
    assert all(a<b for a,b in zip(ts,ts[1:])),(n,ts)
    assert all(ts[i]+ts[-i-1]==1 for i in range(len(ts)))
    checks+=2
    print(n,p,'perms',len(d),'patterns',len(agg),'checks',checks)
print('ALL PASSED',checks)
