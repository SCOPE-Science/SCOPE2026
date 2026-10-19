"""Finite exact tests of the trajectory gauge for freely acting alphabets."""
from itertools import permutations, product


def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def check_group(group, alphabet, action, lengths=(1,2,3,4)):
    e=tuple(range(len(group[0]))) if isinstance(group[0],tuple) else 0
    # List element identities by action, verify freeness on all alphabet points.
    for a in alphabet:
        assert len({action(h,a) for h in group})==len(group)
    if len(group)>2:
        pairs=list(product(group,repeat=2))
        assert any(compose(h,k)!=compose(k,h) for h,k in pairs)
    tested=0
    for n in lengths:
        cardinal=(len(group)*len(alphabet))**n
        # Exhaustively reconstruct periodic codes at moderate sizes; group-size 6 uses shorter n.
        seen=set()
        for ab in product(product(alphabet,group),repeat=n):
            ys=[b[0] for b in ab]
            hs=[b[1] for b in ab]
            def prefix(j):
                # Action composition h[j-1] ... h[0] on a value.
                out=[]
                for t in range(j):out.append(hs[t%n])
                return out
            def original(j):
                y=ys[j%n]
                # Invert product h_(j-1) ... h_0 by applying inverses from left to right in time-reversed multiplication:
                # h_0^-1 ... h_(j-1)^-1 means act with h_(j-1)^-1 first, then ... h_0^-1.
                for h in reversed(prefix(j)):
                    # inverse by brute force on alphabet
                    y=next(v for v in alphabet if action(h,v)==y)
                return y
            x=[original(j) for j in range(2*n+4)]
            # Coordinate equivariance y'_j = y_(j+1), where T(x,h)=(h0 sigma x,sigma h).
            for j in range(n+2):
                xp=action(hs[0],x[j+1])
                yg=xp
                for t in range(1,j+1):yg=action(hs[t%n],yg)
                assert yg==ys[(j+1)%n],(n,ab,j,yg)
            # Identify trajectory by initial x and first n choices, which are unique due freeness.
            signature=(tuple(x[:2*n+3]),tuple(hs))
            assert signature not in seen
            seen.add(signature)
            tested+=1
        assert len(seen)==cardinal,(n,len(seen),cardinal)
    return tested

if __name__=='__main__':
    # Z/2 acts freely on two symbols by addition mod 2.
    cases2=check_group([0,1],[0,1],lambda h,a:(h+a)%2,(1,2,3,4,5))
    # S3 left-regular action on its six elements (noncommutative stress test).
    G=list(permutations(range(3)))
    cases6=check_group(G,G,compose,(1,2))
    print('PASS: exact gauge inverse, shift identity, free coding and periodic counts')
    print('Z2 cases:',cases2,'S3 cases:',cases6)
