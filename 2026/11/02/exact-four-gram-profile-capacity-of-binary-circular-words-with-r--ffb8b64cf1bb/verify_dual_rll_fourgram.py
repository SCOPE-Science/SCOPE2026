#!/usr/bin/env python3
"""Independent finite checks of a cyclic bounded-run binary four-gram theorem.

The proof is mathematical; these tests are deliberately finite.
No external dependencies or network access are required.
"""
from collections import Counter, defaultdict
from itertools import product

EDGES = ('0010', '0011', '0100', '0101', '0110', '1001', '1010', '1011', '1100', '1101')
EINDEX = {e: i for i, e in enumerate(EDGES)}


def balanced_profiles(limit):
    """Generate all flows by the two disjoint nonnegative normal forms."""
    ans = defaultdict(set)
    # Branch a>=c.  3c+4b+6t+2u+3v=n.
    for c in range(limit // 3 + 1):
        for b in range((limit - 3*c)//4 + 1):
            for t in range((limit - 3*c-4*b)//6 + 1):
                for u in range((limit - 3*c-4*b-6*t)//2 + 1):
                    for v in range((limit - 3*c-4*b-6*t-2*u)//3 + 1):
                        n=3*c+4*b+6*t+2*u+3*v
                        a=c+t; d=t+u; h=t+v
                        flow=(a,b,c,d,b+h,a+b,u,h,t+b,v)
                        assert sum(flow)==n
                        ans[n].add(flow)
    # Branch c>a. 3a+4w+6s+2u+3v=n; s>=1.
    for a in range(limit // 3 + 1):
        for w in range((limit-3*a)//4+1):
            for s in range(1,(limit-3*a-4*w)//6+1):
                for u in range((limit-3*a-4*w-6*s)//2+1):
                    for v in range((limit-3*a-4*w-6*s-2*u)//3+1):
                        n=3*a+4*w+6*s+2*u+3*v
                        b=s+w; c=a+s; d=u; h=v
                        flow=(a,b,c,d,b+h,a+b,s+u,h,w,v+s)
                        assert sum(flow)==n
                        ans[n].add(flow)
    return ans


def connected(flow):
    support=[EDGES[i] for i,x in enumerate(flow) if x]
    if not support:
        return False
    vertices={v for e in support for v in (e[:3],e[1:])}
    start=next(iter(vertices))
    seen={start}
    pending=[start]
    while pending:
        u=pending.pop()
        for e in support:
            v,w=e[:3],e[1:]
            if u==v and w not in seen:
                seen.add(w); pending.append(w)
            if u==w and v not in seen:
                seen.add(v); pending.append(v)
    return seen==vertices


def forbidden_disconnection(flow):
    a,b,c,d,e,f,g,h,i,j=flow
    # Exactly two disjoint simple-cycle unions:
    # (0010,0100,1001) + (0110,1011,1101);
    # (0011,0110,1100,1001) + (0101,1010).
    first=(a>0 and h>0 and a==c==f and e==h==j and b==d==g==i==0)
    second=(b>0 and d>0 and b==e==f==i and d==g and a==c==h==j==0)
    return first or second


def profile_of_cyclic_word(s):
    n=len(s)
    return tuple(sum(''.join(s[(i+j)%n] for j in range(4))==e for i in range(n)) for e in EDGES)


def accepted_word(s):
    n=len(s)
    return all(''.join(s[(i+j)%n] for j in range(3)) not in ('000','111') for i in range(n))


def construct_word(flow):
    """Hierholzer Euler-tour construction of any connected balanced profile."""
    outgoing=defaultdict(list)
    for i,e in enumerate(EDGES):
        outgoing[e[:3]].extend([e[1:]]*flow[i])
    start=next(v for v,arr in outgoing.items() if arr)
    stack=[start]; tour=[]
    while stack:
        v=stack[-1]
        if outgoing[v]:
            stack.append(outgoing[v].pop())
        else:
            tour.append(stack.pop())
    tour=tour[::-1]
    assert len(tour)==sum(flow)+1 and tour[0]==tour[-1]
    word=''.join(v[0] for v in tour[:-1])
    assert profile_of_cyclic_word(word)==flow and accepted_word(word)
    return word


def gf_coefficients(limit):
    # A(z)=(1+z^6) / [(1-z^2)(1-z^3)^2(1-z^4)(1-z^6)].
    dp=[0]*(limit+1);dp[0]=1
    for d in (2,3,3,4,6):
        for k in range(d,limit+1):
            dp[k]+=dp[k-d]
    out=[]
    for n in range(limit+1):
        total=dp[n]+(dp[n-6] if n>=6 else 0)
        disconnected=(n//3-1 if n>=6 and n%3==0 else 0)
        disconnected+=(n-2)//4 if n>=6 and n%2==0 else 0
        out.append(total-disconnected-(n==0))
    return out


def main():
    lim=44
    profiles=balanced_profiles(lim)
    expected=gf_coefficients(lim)
    checks=0
    for n in range(1,lim+1):
        p=profiles[n]
        assert all(sum(f)==n for f in p)
        assert all(connected(f)==(not forbidden_disconnection(f)) for f in p)
        valid={f for f in p if connected(f)}
        assert len(valid)==expected[n],(n,len(valid),expected[n])
        for f in valid:
            construct_word(f)
            checks+=1
        if n<=18:
            literal={profile_of_cyclic_word(''.join(s)) for s in product('01',repeat=n) if accepted_word(''.join(s))}
            assert literal==valid,(n,len(literal),len(valid))
    assert expected[:19]==[0,0,1,2,2,2,5,4,7,10,11,14,22,22,29,38,43,50,67]
    print(f'VERIFY_OK literal_all_binary_n=1..18 exact_flow_profiles_n=1..{lim} euler_tours={checks} disconnected_support_classification=PASS gf_coefficients=PASS')
    print('profile_counts_n2..18=', expected[2:19])

if __name__=='__main__':
    main()
