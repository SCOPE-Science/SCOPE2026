#!/usr/bin/env python3
"""Independent second-implementation verification + detailed invariants for best reps."""
import numpy as np
import csv, hashlib, json

n=7; N=128; G=20
def rot(v): return ((v>>1)|((v&1)<<6))&0x7F
# orbits sorted by min
visited=[False]*N
orbs=[]
for v in range(N):
    if not visited[v]:
        cur=v; orb=[]
        for _ in range(n):
            if not visited[cur]:
                visited[cur]=True; orb.append(cur)
            cur=rot(cur)
            if cur==v: break
        orbs.append(sorted(orb))
orbs=sorted(orbs,key=lambda o:min(o))
omin=[min(o) for o in orbs]
owt=[bin(m).count('1') for m in omin]
oid=[-1]*N
for i,o in enumerate(orbs):
    for v in o: oid[v]=i
print("omin:",omin)
print("owt:",owt)

def truth_from_mask(mask):
    return np.array([(mask>>oid[v])&1 for v in range(N)],dtype=np.uint8)
def anf_from_truth(T):
    A=T.copy()
    # Mobius, second implementation style (numpy-free loop, different order)
    step=1
    while step<N:
        for i in range(0,N,2*step):
            for j in range(step):
                A[i+j+step]^=A[i+j]
        step*=2
    return A
def fwht_numpy(P):
    # P: int array length N, iterative with numpy vectorization (different code path from C)
    a=P.astype(np.int64).copy()
    h=1
    while h<N:
        a=a.reshape(-1,2*h)
        # need copy for butterfly
        u=a[:,:h].copy(); v=a[:,h:].copy()
        a[:,:h]=u+v; a[:,h:]=u-v
        a=a.reshape(N)
        h*=2
    return a
def walsh_of_mask(mask):
    T=truth_from_mask(mask)
    P=np.where(T==0,1,-1).astype(np.int64)
    W=fwht_numpy(P)
    return T,W
def nl_from_W(W):
    return 64-int(np.max(np.abs(W)))//2
def autocorr(T):
    S=np.where(T==0,1.0,-1.0)
    R=np.zeros(N,dtype=int)
    for s in range(N):
        # (x xor s)
        R[s]=int(np.sum(S*np.roll(S,0))) if s==0 else int(sum(S[x]*S[x^s] for x in range(N)))
    return R
def pack_hex(V):
    # V length 128 bits, byte j = bits 8j..8j+7 LSB first
    b=bytearray(16)
    for j in range(16):
        byte=0
        for i in range(8):
            if V[8*j+i]: byte|=(1<<i)
        b[j]=byte
    return b.hex()
def anf_orbit_mask(A):
    m=0
    for j,rep in enumerate(omin):
        if A[rep]: m|=(1<<j)
    return m
def degree_from_A(A):
    idx=np.where(A==1)[0]
    if len(idx)==0: return -1
    return max(bin(i).count('1') for i in idx)

# load best
rows=list(csv.DictReader(open("output/artifacts/best_per_nl.csv")))
print(f"{len(rows)} nl values")
for r in rows:
    nl=int(r['nl']); tm=int(r['best_truth_mask'])
    T,W=walsh_of_mask(tm)
    nl2=nl_from_W(W)
    A=anf_from_truth(T)
    am=anf_orbit_mask(A)
    deg=degree_from_A(A)
    assert nl2==nl, (nl,nl2,tm)
    assert am==int(r['best_anf_mask']), (nl,am,r['best_anf_mask'])
    assert deg==int(r['degree']), (nl,deg,r['degree'])
    print(f"nl={nl:2d} tm={tm:7d} (0x{tm:05x}) am=0x{am:05x} deg={deg} max|W|={np.max(np.abs(W))} wt={int(T.sum())} OK")

# detailed for extremal: nl=56 and 55
for nl in [56,55]:
    r=[x for x in rows if int(x['nl'])==nl][0]
    tm=int(r['best_truth_mask'])
    T,W=walsh_of_mask(tm)
    A=anf_from_truth(T)
    R=autocorr(T)
    print(f"\n=== nl={nl} mask={tm} ===")
    print("truth_hex:",pack_hex(T))
    print("anf_hex:",pack_hex(A))
    print("anf_orbits_set:",[j for j in range(G) if (anf_orbit_mask(A)>>j)&1])
    print("degree:",degree_from_A(A),"weight:",int(T.sum()))
    # Walsh multiset
    vals,counts=np.unique(np.abs(W),return_counts=True)
    print("Walsh |W| multiset:",dict(zip(vals.tolist(),counts.tolist())))
    print("Walsh signed multiset:",dict(zip(*np.unique(W,return_counts=True))))
    print("W[0..15]:",W[:16].tolist())
    print("full W:",W.tolist())
    vals2,counts2=np.unique(np.abs(R),return_counts=True)
    print("Autocorr |r| multiset:",dict(zip(vals2.tolist(),counts2.tolist())))
    print("max|r| (s!=0):",max(abs(int(x)) for x in R[1:]), "r(0)=128")
    # balanced? weight 64?
    # resiliency: W(0)= N-2wt
    print("W(0)=",int(W[0]))

# naive O(N^2) Walsh spot check for extremal + few random (deterministic list)
import random
random.seed(0)
test_masks=[int(r['best_truth_mask']) for r in rows[:5]]+[int(r['best_truth_mask']) for r in rows[-5:]]+[random.randrange(1<<20) for _ in range(20)]
print("\nNaive spot checks:")
for tm in test_masks:
    T=truth_from_mask(tm)
    # naive
    maxabs=0
    for a in range(N):
        s=0
        for x in range(N):
            # parity(a&x)
            s+= 1 if ((bin(a&x).count('1')+int(T[x]))%2==0) else -1
        if abs(s)>maxabs: maxabs=abs(s)
    nl_naive=64-maxabs//2
    _,W=walsh_of_mask(tm)
    nl_fast=nl_from_W(W)
    assert nl_naive==nl_fast
    print(f"mask {tm}: nl={nl_fast} naive OK (max|W|={maxabs})")
print("ALL SECOND-IMPLEMENTATION CHECKS PASSED")
