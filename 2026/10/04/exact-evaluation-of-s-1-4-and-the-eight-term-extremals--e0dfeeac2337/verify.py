from itertools import combinations_with_replacement, combinations
A=tuple(x for x in range(16) if x%4)
TARGET={4,8,12}
def witness_index(t):
    for I in combinations(range(len(t)),4):
        if sum(t[i] for i in I)%16 in TARGET: return I
    return None
def witness_dp(t):
    reach=[0]*5; reach[0]=1
    for x in t:
        for k in range(3,-1,-1):
            bits=reach[k]; shifted=0
            for r in range(16):
                if (bits>>r)&1: shifted |= 1<<((r+x)%16)
            reach[k+1] |= shifted
    return bool(reach[4] & sum(1<<r for r in TARGET))
bad8=[]; n8=0
for t in combinations_with_replacement(A,8):
    n8+=1; a=witness_index(t) is not None; b=witness_dp(t); assert a==b
    if not a: bad8.append(t)
n9=0
for t in combinations_with_replacement(A,9):
    n9+=1; a=witness_index(t) is not None; b=witness_dp(t); assert a==b
    if not a: raise AssertionError(("bad9",t))
trans=[(u,4*c) for u in range(1,16,2) for c in range(4)]
def aff(t,u,b): return tuple(sorted((u*x+b)%16 for x in t))
bad=set(bad8); seen=set(); reps=[]; sizes=[]
for t in sorted(bad):
    if t in seen: continue
    orb={aff(t,u,b) for u,b in trans}; assert orb<=bad; seen|=orb; reps.append(min(orb)); sizes.append(len(orb))
assert seen==bad and len(bad8)==160 and len(reps)==7
assert sizes==[32,32,16,8,32,32,8]
assert reps==[(1,1,1,2,2,2,10,13),(1,1,1,2,2,6,6,13),(1,1,1,2,6,7,7,7),(1,1,1,2,6,10,13,14),(1,1,2,2,2,5,9,10),(1,1,2,2,5,6,6,9),(1,1,2,5,6,9,10,14)]
print("VERIFY_OK",f"length8_multisets={n8}",f"bad8={len(bad8)}",f"length9_multisets={n9}","bad9=0",f"orbits={len(reps)}",f"orbit_sizes={sizes}")
