"""Finite-state certificate for two-summand binary digit-weight classes.

Run: python3 certify_mod3_sums.py
No third-party packages are needed.
"""
from collections import deque

# All nonnegative integers whose binary Hamming weight is c modulo 3.
# Claimed exceptional sets: listed small values and two geometric families.
EXTRAS = {
    0: (2,4,5,6,8,9,10,12,16,17),
    1: (0,13,14,21,22,26),
    2: (0,1,2,4),
}


def reference_nfa(c):
    edges=[]; accept=set()
    def node():
        edges.append([0,0]);return len(edges)-1
    def add(i,b,j):edges[i][b] |= 1<<j
    start=node()
    # A positive repunit has j one-bits. States label j mod 3.
    r1=node();r2=node();r0=node()
    add(start,1,r1); add(r1,1,r2);add(r2,1,r0);add(r0,1,r1)
    if c==0: accept.update((r1,r2))
    else: accept.add(r0)
    if c in (0,1):
        after0=node();done=node();accept.add(done)
        # Binary 3*2**j-1 is 10 followed by j ones, MSB first.
        # Thus from the least significant end its word is 1**j 01.
        add(r0 if c==0 else r2,0,after0)
        add(after0,1,done)
    for n in EXTRAS[c]:
        word = bin(n)[2:][::-1]
        pos=start
        for bit in word:
            nxt=node();add(pos,int(bit),nxt);pos=nxt
        accept.add(pos)
    return edges,accept


def source_transitions():
    states=[(carry,u,v) for carry in (0,1) for u in range(3) for v in range(3)]
    idx={state:i for i,state in enumerate(states)}
    edges=[]
    for carry,u,v in states:
        e=[0,0]
        for x in (0,1):
            for a in (0,1):
                for b in (0,1):
                    z=a+b+carry
                    if z%2==x:
                        e[x] |= 1<<idx[(z//2,(u+a)%3,(v+b)%3)]
        edges.append(e)
    return edges,idx[(0,0,0)]


def apply(mask,edges,bit):
    nxt=0
    while mask:
        flag=mask&-mask;mask-=flag
        nxt|=edges[flag.bit_length()-1][bit]
    return nxt


def certify(c):
    source,initial=source_transitions()
    target,accept=reference_nfa(c)
    S=1<<initial
    U=1  # Reference initial state.
    start=(S,0,U)
    todo=deque([start]);seen={start}
    examined=0
    def missing(pair):
        mask,ones,_=pair
        return not (ones==c or (mask & (1<<((0*3+(c))*3+c))))
    def expected(pair):
        mask=pair[2]
        return any(mask&(1<<t) for t in accept)
    # Empty word need not be canonical; zero has canonical word '0'.
    while todo:
        st=todo.popleft();examined+=1
        for bit in (0,1):
            src=apply(st[0],source,bit)
            dest=(src,(st[1]+bit)%3,apply(st[2],target,bit))
            if bit==1:
                assert missing(dest)==expected(dest), ('mismatch',c,st,bit,dest)
            if dest not in seen:
                seen.add(dest);todo.append(dest)
    src0=(apply(S,source,0),0,apply(U,target,0))
    assert missing(src0)==expected(src0), ('zero mismatch',c)
    # Independent finite brute-force for human inspection.
    B=10000
    admissible={m for m in range(B+1) if m.bit_count()%3==c}
    pair={u+v for u in admissible for v in admissible if u+v<=B}
    for n in range(B+1):
        predicted=(n in EXTRAS[c] or
                   (n>0 and ((n+1)&n)==0 and ((n+1).bit_length()-1)%3 in
                    ((1,2) if c==0 else (0,)) and (c==0 or n>0)) or
                   (c==0 and any(n==3*(1<<(3*j))-1 for j in range(1,8))) or
                   (c==1 and any(n==3*(1<<(3*j-1))-1 for j in range(1,8))))
        assert predicted == (n not in admissible and n not in pair),(c,n)
    return examined,len(target)

if __name__=='__main__':
    for residue in range(3):
        n,states=certify(residue)
        print(f'residue {residue}: PASS; {n} reachable paired states; reference NFA {states} states')
    print('PASS: all three infinite classifications; direct check n <= 10000')
