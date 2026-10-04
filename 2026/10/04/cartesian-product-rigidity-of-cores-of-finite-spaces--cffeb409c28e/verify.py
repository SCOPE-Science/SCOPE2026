from itertools import product

def labeled_posets(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for states in product((-1,0,1), repeat=len(pairs)):
        le=[1<<i for i in range(n)]
        for (i,j),s in zip(pairs,states):
            if s<0: le[j] |= 1<<i
            elif s>0: le[i] |= 1<<j
        ok=True
        for i in range(n):
            reach=le[i]
            for j in range(n):
                if (reach>>j)&1 and (le[j] & ~reach):
                    ok=False
                    break
            if not ok: break
        if ok: out.append(tuple(le))
    return out

def maxima(P):
    return {i for i,r in enumerate(P) if r==(1<<i)}

def minima(P):
    n=len(P); below=[0]*n
    for i,r in enumerate(P):
        for j in range(n):
            if (r>>j)&1: below[j] |= 1<<i
    return {j for j,c in enumerate(below) if c==(1<<j)}

def up_beat(P,i):
    strict=[j for j in range(len(P)) if j!=i and ((P[i]>>j)&1)]
    if not strict: return False
    return any(all((P[a]>>j)&1 for j in strict) for a in strict)

def down_beat(P,i):
    strict=[j for j in range(len(P)) if j!=i and ((P[j]>>i)&1)]
    if not strict: return False
    return any(all((P[j]>>a)&1 for j in strict) for a in strict)

def product_poset(P,Q):
    n,m=len(P),len(Q); R=[]
    for i in range(n):
        for j in range(m):
            mask=0
            for a in range(n):
                if (P[i]>>a)&1:
                    for b in range(m):
                        if (Q[j]>>b)&1:
                            mask |= 1<<(a*m+b)
            R.append(mask)
    return tuple(R)

families={n:labeled_posets(n) for n in range(1,5)}
assert [len(families[n]) for n in range(1,5)] == [1,3,19,219]
small=sum((families[n] for n in range(1,4)),[])
tiny=sum((families[n] for n in range(1,3)),[])
four=families[4]
pairs=[(P,Q) for P in small for Q in small]
pairs += [(P,Q) for P in four for Q in tiny]
pairs += [(P,Q) for P in tiny for Q in four]
point_checks=0
minimality_checks=0
for P,Q in pairs:
    upP={i for i in range(len(P)) if up_beat(P,i)}
    upQ={j for j in range(len(Q)) if up_beat(Q,j)}
    dnP={i for i in range(len(P)) if down_beat(P,i)}
    dnQ={j for j in range(len(Q)) if down_beat(Q,j)}
    maxP,maxQ=maxima(P),maxima(Q)
    minP,minQ=minima(P),minima(Q)
    R=product_poset(P,Q); m=len(Q)
    for i in range(len(P)):
        for j in range(len(Q)):
            got_u=up_beat(R,i*m+j)
            exp_u=((i in upP and j in maxQ) or (j in upQ and i in maxP))
            got_d=down_beat(R,i*m+j)
            exp_d=((i in dnP and j in minQ) or (j in dnQ and i in minP))
            assert got_u == exp_u
            assert got_d == exp_d
            point_checks += 2
    minP_flag=not upP and not dnP
    minQ_flag=not upQ and not dnQ
    minR_flag=all(not up_beat(R,k) and not down_beat(R,k) for k in range(len(R)))
    assert minR_flag == (minP_flag and minQ_flag)
    minimality_checks += 1
print('VERIFY_OK')
print('labeled_poset_counts=1,3,19,219')
print(f'product_pairs_checked={len(pairs)}')
print(f'beat_point_equivalence_checks={point_checks}')
print(f'minimality_equivalence_checks={minimality_checks}')
