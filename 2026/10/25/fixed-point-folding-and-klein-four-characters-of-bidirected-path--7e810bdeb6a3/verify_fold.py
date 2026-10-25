#!/usr/bin/env python3
"""Finite independent checks for reversal fixed sets of bidirected-path multipath complexes.

Requires only Python 3 standard library. The infinite theorem is established separately.
"""
from itertools import combinations

def arc(n, i):
    k=i//2
    return (k,k+1) if i%2==0 else (k+1,k)

def is_multipath(n, mask):
    incoming=[0]*(n+1)
    outgoing=[0]*(n+1)
    for i in range(2*n):
        if (mask>>i)&1:
            a,b=arc(n,i)
            outgoing[a]+=1; incoming[b]+=1
            if outgoing[a]>1 or incoming[b]>1:
                return False
            if (mask>>(i^1))&1:
                return False
    return True # an undirected path admits no directed cycles longer than 2

def conflicts(n):
    out=[]
    for i in range(2*n):
        for j in range(i+1,2*n):
            if not is_multipath(n,(1<<i)|(1<<j)):
                out.append((i,j))
    return set(out)

def rowcol(i):
    col=i//2
    return (col, (i%2)^(col%2))

def relabel(i):
    col,row=rowcol(i)
    return 2*col+row

def ladder_conflicts(n):
    return {(i,j) for i in range(2*n) for j in range(i+1,2*n)
            if (rowcol(i)[0]==rowcol(j)[0]) or
            (abs(rowcol(i)[0]-rowcol(j)[0])==1 and rowcol(i)[1]==rowcol(j)[1])}

def reverse_arc(n,i):
    return 2*(n-1-i//2)+(1-(i%2))

def reverse_all_arc(n,i):
    return i^1

def symmetry(n,i,kind):
    if kind=='R':return reverse_arc(n,i)
    if kind=='T':return reverse_all_arc(n,i)
    if kind=='RT':return reverse_arc(n,i)^1
    raise ValueError(kind)

def fixed_orbits(n,kind='R'):
    seen=set(); allorbit=[]
    for i in range(2*n):
        if i not in seen:
            j=symmetry(n,i,kind)
            o=tuple(sorted((i,j))) if i!=j else (i,)
            seen.update(o)
            allorbit.append(o)
    cf=conflicts(n)
    allowed=[]
    for orbit in allorbit:
        if not any((min(i,j),max(i,j)) in cf for i,j in combinations(orbit,2)):
            allowed.append(orbit)
    ef=set()
    for a,b in combinations(range(len(allowed)),2):
        if any((min(i,j),max(i,j)) in cf for i in allowed[a] for j in allowed[b]):
            ef.add((a,b))
    return allowed,ef

def expected_width(n,kind):
    m=n//2
    if kind=='R': return m-1 if n%2==0 else m
    if kind=='RT': return m if n%2==0 else m+1
    if kind=='T':return 0
    raise ValueError(kind)

def is_ladder_isomorphic(n,kind):
    orbit, edges=fixed_orbits(n,kind)
    k=expected_width(n,kind)
    assert len(orbit)==2*k,(n,len(orbit),k)
    # Each non-central orbit has a unique edge in the left half.
    left=range(k)
    labels=[]
    for o in orbit:
        v=next((v for v in o if v//2 in left),None)
        assert v is not None,(n,o)
        labels.append(relabel(v))
    assert len(set(labels))==2*k
    new={(min(labels[a],labels[b]),max(labels[a],labels[b])) for a,b in edges}
    ref={(min(relabel(i),relabel(j)),max(relabel(i),relabel(j))) for i,j in ladder_conflicts(k)}
    assert new==ref,(n,kind,new^ref)

def betti_mod2(n):
    faces_by_dim={}
    for mask in range(1,1<<(2*n)):
        if is_multipath(n,mask):
            dim=mask.bit_count()-1
            faces_by_dim.setdefault(dim,[]).append(mask)
    maxdim=max(faces_by_dim)
    ranks={}
    for d in range(1,maxdim+1):
        lower={f:j for j,f in enumerate(faces_by_dim[d-1])}
        pivots={}
        for face in faces_by_dim[d]:
            col=0
            x=face
            while x:
                b=x&-x
                col^=1<<lower[face^b]
                x-=b
            while col:
                p=col.bit_length()-1
                if p not in pivots:
                    pivots[p]=col
                    break
                col^=pivots[p]
        ranks[d]=len(pivots)
    ranks[0]=1 # augmentation rank for nonempty complexes
    betti={d:len(faces_by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in faces_by_dim}
    assert all(v>=0 for v in betti.values())
    return sum(map(len,faces_by_dim.values())), {k:v for k,v in betti.items() if v}

def lefschetz_brute(n,kind):
    # signed augmented chain trace, calculated independently on actual arc faces
    value=0
    count=0
    for mask in range(1<<(2*n)):
        if not is_multipath(n,mask):continue
        rev=0
        for i in range(2*n):
            if (mask>>i)&1:rev|=1<<symmetry(n,i,kind)
        if rev!=mask: continue
        count+=1
        # Number of 2-orbits in the face gives the orientation sign.
        pairs=sum(i<symmetry(n,i,kind) and ((mask>>i)&1) for i in range(2*n))
        value+=(-1)**(mask.bit_count()+pairs)
    return -value,count  # reduced Lefschetz is minus augmented sign polynomial

def signed_partition_ladder(k):
    a,t=1,0
    for _ in range(k):
        a,t=a+2*t,-(a+t)
    return a+2*t

def main():
    totalfaces=0;totalinv=0
    for n in range(2,11):
        cf=conflicts(n)
        assert cf==ladder_conflicts(n),('conflict',n)
        d=(n-1)//2
        R=(-1)**((n+3)//4)
        T=(-1)**(d+1)
        RT=R*T
        expected={'R':R,'T':T,'RT':RT}
        for kind in ('R','T','RT'):
            is_ladder_isomorphic(n,kind)
            width=expected_width(n,kind)
            z=signed_partition_ladder(width)
            assert (-z)==(-1)**d*expected[kind],('predicted lefschetz',n,kind)
            if n<=9:
                actual,num=lefschetz_brute(n,kind)
                assert actual==(-1)**d*expected[kind],('lefschetz',n,kind,actual)
                totalinv+=num
        if n<=9:
            for mask in range(1<<(2*n)):
                b=True
                for i,j in cf:
                    if (mask>>i)&1 and (mask>>j)&1:
                        b=False;break
                assert b==is_multipath(n,mask),('face',n,mask)
        if n<=7:
            faces,bd=betti_mod2(n)
            assert bd=={d:1},('homology',n,bd)
            totalfaces+=faces
        print('n=%d fixed_widths=%s characters=%s PASS'%
              (n, [expected_width(n,x) for x in ('R','T','RT')],(R,T,RT)))
    print('Total direct Betti faces:',totalfaces)
    print('Total invariant-face checks including empty, three actions:',totalinv)
    print('VERIFY_OK')
if __name__=='__main__':main()
