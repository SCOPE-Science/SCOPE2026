#!/usr/bin/env python3
"""Reproduce exhaustive-history breakpoints of generalized Cantor words."""

def by_substitution(q,k):
    s='1'
    for _ in range(k):
        s=''.join('1'+'0'*(q-2)+'1' if a=='1' else '0'*q for a in s)
    return s

def by_digits(q,n):
    out=[]
    for i in range(n):
        t=i
        ok=True
        while t:
            a=t%q
            if a not in (0,q-1):
                ok=False; break
            t//=q
        out.append('1' if ok else '0')
    return ''.join(out)

def exhaustive_starts(s):
    n=len(s); i=0; starts=[]
    while i<n:
        starts.append(i)
        ell=1
        # occurrence may overlap current phrase, but must start before i
        while i+ell<=n and s[:i+ell-1].find(s[i:i+ell])>=0:
            ell+=1
        i+=min(ell,n-i)
    return starts

def predicted(q,n):
    if q>=4:
        starts=[0,1,2]
        m=0
        while (q-1)*q**m+1<n:
            a=(q-1)*q**m+1; b=2*(q-1)*q**m+1
            starts.append(a)
            if b<n: starts.append(b)
            m+=1
    else:
        starts=[0,1,2,5,9]
        m=1
        while 2*3**(m+1)+1<n or 4*3**m+1<n:
            a=4*3**m+1
            b=2*3**(m+1)+1
            if a<n: starts.append(a)
            if b<n: starts.append(b)
            m+=1
    return sorted(set(starts))

def main():
    specs={3:10,4:8,5:7,6:6,7:5,8:5,9:5,10:5,11:4,12:4}
    for q,k in specs.items():
        n=q**k
        s=by_substitution(q,k)
        assert s==by_digits(q,n)
        got=exhaustive_starts(s)
        want=predicted(q,n)
        assert got==want,(q,k,got,want)
        print(f'q={q} k={k} n={n} starts={len(got)} MATCH')
    print('VERIFY_OK')

if __name__=='__main__':main()
