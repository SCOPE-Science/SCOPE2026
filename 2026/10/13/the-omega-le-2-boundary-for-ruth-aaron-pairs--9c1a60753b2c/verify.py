#!/usr/bin/env python3
LIMIT = 200000

def spf_sieve(n):
    spf=list(range(n+1))
    if n>=1: spf[1]=1
    for p in range(2,int(n**0.5)+1):
        if spf[p]==p:
            for m in range(p*p,n+1,p):
                if spf[m]==m: spf[m]=p
    return spf

def stats(n,spf):
    s=0; om=0
    while n>1:
        p=spf[n]; s+=p; om+=1; n//=p
    return s,om

def primes_upto(n):
    mark=[True]*(n+1)
    mark[0:2]=[False,False]
    for p in range(2,int(n**0.5)+1):
        if mark[p]:
            mark[p*p:n+1:p]=[False]*(((n-p*p)//p)+1)
    return [i for i,v in enumerate(mark) if v]

def main():
    spf=spf_sieve(LIMIT+1)
    hits=[]
    for n in range(2,LIMIT+1):
        s1,o1=stats(n,spf); s2,o2=stats(n+1,spf)
        if o1<=2 and o2<=2 and s1==s2:
            hits.append(n)
    assert hits == [5], hits
    assert stats(5,spf)==(5,1)
    assert stats(6,spf)==(5,2)
    ps=primes_upto(199)
    inputs=0; eqhits=0
    for a in ps:
        for b in ps:
            for c in ps:
                d=a+b-c
                if d in ps:
                    inputs += 1
                    if a*b+1 == c*d:
                        eqhits += 1
    assert eqhits == 0, eqhits
    print(f"VERIFY_OK limit={LIMIT} low_omega_pairs={len(hits)} semiprime_semiprime_inputs={inputs} equal_sum_grid_hits={eqhits}")
if __name__=='__main__': main()
