#!/usr/bin/env python3
"""Independent finite-case chain-trace check of cross-polytope theta actions."""
import itertools, math

def parity(seq):
    return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1

def generate(n,k):
    vertices=2*n
    faces=[]
    for mask in range(1<<vertices):
        missing=((1<<vertices)-1)^mask
        occupied=sum(bool((missing>>(2*i))&3) for i in range(n))
        if occupied>=k+1: faces.append(mask)
    return faces

def char_standard_wedge(p,k):
    n=len(p);seen=set();e=[1]+[0]*n
    for i in range(n):
        if i in seen:continue
        cur=i;l=0
        while cur not in seen:
            seen.add(cur);cur=p[cur];l+=1
        for j in range(n-l,-1,-1):
            e[j+l]+=(-1)**(l-1)*e[j]
    q_prev=0
    for j in range(k+1):
        q=e[j]-q_prev
        q_prev=q
    return q

def character_from_faces(faces,perm,d):
    s=-1 # reduced empty-face trace in degree -1
    for mask in faces:
        if mask==0:continue
        vs=[a for a in range(len(perm)) if (mask>>a)&1]
        ims=[perm[a] for a in vs]
        if sum(1<<a for a in ims)!=mask:continue
        s+=(-1)**(len(vs)-1)*parity(ims)
    return (-1)**d*s

def run(n,k):
    fs=generate(n,k)
    dimension=2*n-k-2
    maxdim=max(mask.bit_count()-1 for mask in fs)
    assert maxdim==dimension
    checks=0
    vals={}
    for p in itertools.permutations(range(n)):
        theory=char_standard_wedge(p,k)
        for flipbits in range(1<<n):
            perm=[2*p[i]+(a^((flipbits>>i)&1)) for i in range(n) for a in range(2)]
            calc=character_from_faces(fs,perm,dimension)
            pred=(-1)**flipbits.bit_count()*theory
            if calc!=pred:raise AssertionError((n,k,p,flipbits,calc,pred))
            checks+=1
            vals[(p,flipbits)]=calc
    ident=vals[(tuple(range(n)),0)]
    assert ident==math.comb(n-1,k)
    print('CHAR_OK',n,k,'faces',len(fs),'group_elements',checks,'rank',ident,'dimension',dimension)

for n,k in [(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,2)]:
    run(n,k)
print('VERIFY_OK')
