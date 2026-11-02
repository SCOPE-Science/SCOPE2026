"""Exact finite checks for a persistent sign-walk stochastic-order theorem.

All fractions are exact. The proof of the all-length result is in RESULT.md;
finite enumeration below checks identities and support details independently.
"""
from collections import Counter
from fractions import Fraction
from math import comb

checks = 0

def confirm(statement, message):
    global checks
    assert statement, message
    checks += 1

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def signed_count_formula(n,m,s):
    if s % 2 != n % 2 or abs(s)>n: return Fraction(0)
    if m==0: return Fraction(int(s==n or s==-n),2)
    if m%2==0: a=m//2
    else: a=(m+1)//2
    j=(n+s)//2
    b=n-j
    return Fraction(choose(j-1,a-1)*choose(b-1,a-1),choose(n-1,2*a-1))

def condition_distributions(n):
    d=[Counter() for _ in range(n)]
    for mask in range(1<<(n-1)):
        turn_count=mask.bit_count()
        spin=1
        displacement=1
        for i in range(n-1):
            if mask & (1<<i): spin=-spin
            displacement+=spin
        d[turn_count][displacement]+=1
        d[turn_count][-displacement]+=1
    return [{s:Fraction(v,2*choose(n-1,m)) for s,v in row.items()}
             for m,row in enumerate(d)]

def absolute(d):
    out=Counter()
    for s,p in d.items():out[abs(s)]+=p
    return dict(out)

def upper_tail(d,h):
    return sum((v for s,v in d.items() if s>=h),Fraction(0))

for n in range(2,15):
    d=condition_distributions(n)
    abs_d=[absolute(row) for row in d]
    for m in range(n):
        confirm(sum(d[m].values())==1,('normalization',n,m))
        for s in range(-n,n+1,2):
            confirm(d[m].get(s,0)==signed_count_formula(n,m,s),('formula',n,m,s))
        for h in range(0,n+2):
            if m<n-1:
                confirm(upper_tail(abs_d[m],h)>=upper_tail(abs_d[m+1],h),('turn order',n,m,h))
    for a in range(1,(n+1)//2):
        odd=2*a-1
        even=2*a
        if even<n:
            confirm(d[odd]==d[even],('odd-even law',n,a))
        newer=2*a+1
        if newer<n:
            c=Fraction(choose(n-1,odd),a*a*choose(n-1,newer))
            for s,p in abs_d[odd].items():
                ratio=c*Fraction((n-2*a)**2-s*s,4)
                confirm(abs_d[newer].get(s,0)==p*ratio,('MLR ratio',n,a,s))
    # Direct mixtures of the enumerated conditional laws, including boundaries.
    prev=None
    for p_num in (0,1,2,3,4,5,6,7,8,9,10):
        p=Fraction(p_num,10)
        out=Counter()
        for m,row in enumerate(abs_d):
            w=comb(n-1,m)*p**(n-1-m)*(1-p)**m
            for s,v in row.items():out[s]+=w*v
        confirm(sum(out.values())==1,('mixture norm',n,p_num))
        if prev is not None:
            for h in range(n+2):
                confirm(upper_tail(out,h)>=upper_tail(prev,h),('parameter stoch order',n,p_num,h))
                if n%2<h<=n:
                    confirm(upper_tail(out,h)>upper_tail(prev,h),('strict interior',n,p_num,h))
        prev=out
print(f'PASS: {checks} exact assertions for lengths 2 through 14.')
