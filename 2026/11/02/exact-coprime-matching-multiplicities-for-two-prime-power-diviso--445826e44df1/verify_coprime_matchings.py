"""Exact independent checks of coprime divisor matchings for two prime-power factors."""
from math import gcd, factorial
from itertools import product


def fall(n,k):
    return factorial(n)//factorial(n-k) if 0<=k<=n else 0

def formula(a,b,p,q,values):
    N=(a+1)*(b+1)
    if len(values)!=N or len(set(values))!=N: raise ValueError('Set size')
    T=sum(x%p==0 and x%q==0 for x in values)
    B=sum(x%p==0 and x%q!=0 for x in values)
    C=sum(x%q==0 and x%p!=0 for x in values)
    R=N-T-B-C
    if T>1: return 0
    if T==1: return fall(b,B)*fall(a,C)*factorial(R)
    return (fall(b,B)*fall(a,C)+B*fall(b,B-1)*fall(a,C)+C*fall(a,C-1)*fall(b,B))*factorial(N-B-C)

def direct(a,b,p,q,values):
    divs=[p**i*q**j for i in range(a+1) for j in range(b+1)]
    N=len(divs)
    dp={0:1}
    for x in values:
        new={}
        for mask, c in dp.items():
            for i,d in enumerate(divs):
                if mask>>i&1==0 and gcd(x,d)==1:
                    dest=mask|(1<<i)
                    new[dest]=new.get(dest,0)+c
        dp=new
    return dp.get((1<<N)-1,0)

def main():
    cases=0; blocked=0; positive=0
    for p,q in [(2,3),(2,5),(3,5),(3,7)]:
      for a in range(1,4):
       for b in range(1,4):
        N=(a+1)*(b+1)
        if N>12: continue
        for start,step in product(range(-12,15),range(1,10)):
            vals=[start+k*step for k in range(N)]
            z=formula(a,b,p,q,vals)
            d=direct(a,b,p,q,vals)
            if z!=d: raise AssertionError((a,b,p,q,start,step,z,d))
            cases+=1
            if z: positive+=1
            else: blocked+=1
    occupancy_cases=0
    for p,q in [(2,3),(3,5)]:
      for a,b in product(range(1,3),repeat=2):
        N=(a+1)*(b+1)
        for T in range(N+1):
         for B in range(N-T+1):
          for C in range(N-T-B+1):
            D=N-T-B-C
            vals=([p*q*(k+1) for k in range(T)]+
                  [p*(1+q*k) for k in range(B)]+
                  [q*(1+p*k) for k in range(C)]+
                  [1+p*q*k for k in range(D)])
            assert len(set(vals))==N
            predicted=formula(a,b,p,q,vals)
            counted=direct(a,b,p,q,vals)
            if predicted!=counted:
                raise AssertionError(('occupancy',p,q,a,b,T,B,C,D,predicted,counted))
            occupancy_cases+=1
    print(f'VERIFY_OK progression_cases={cases} occupancy_cases={occupancy_cases} positive={positive} zero={blocked} exact_permanent_dp=yes')

if __name__=='__main__': main()
