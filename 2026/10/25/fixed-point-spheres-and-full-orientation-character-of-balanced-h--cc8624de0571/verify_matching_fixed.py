"""Independent finite checks for transposition-fixed higher matching spheres.
Run: python verify_matching_fixed.py (standard library only).
"""
from itertools import combinations

def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def rank_mod2(columns):
    piv={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k in piv: x^=piv[k]
            else:
                piv[k]=x
                break
    return len(piv)

def fixed_face_homology(n):
    verts=[(i,j) for i in range(n) for j in range(i,n)]
    faces={-1:[()]}
    for mask in range(1,1<<len(verts)):
        hits=[0]*n; face=[]
        for k,(i,j) in enumerate(verts):
            if mask>>k&1:
                hits[i]+=1
                if i!=j:hits[j]+=1
                face.append(k)
        if max(hits)<n:
            faces.setdefault(len(face)-1,[]).append(tuple(face))
    ranks={}
    for d in sorted(faces):
        if d<=0:continue
        prev={f:i for i,f in enumerate(faces[d-1])}
        cols=[]
        for f in faces[d]:
            z=0
            for k in range(len(f)): z ^=1<<prev[f[:k]+f[k+1:]]
            cols.append(z)
        ranks[d]=rank_mod2(cols)
    betti={}
    for d in sorted(faces):
        if d<0:continue
        b=len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0: b-=1
        if b:betti[d]=b
    wanted={n*(n-1)//2-1:1}
    assert betti==wanted,(n,betti,wanted)
    return len(verts),sum(len(v) for d,v in faces.items() if d>=0),betti

def ch(n,p,q,sw):
    P=[]
    for i in range(n):
        for j in range(n):
            ii,jj=(j,i) if sw else (i,j)
            P.append(p[ii]*n+q[jj])
    L=0
    N=n*n
    for mask in range(1,1<<N):
        rr=[0]*n;cc=[0]*n;vv=[]
        for k in range(N):
            if mask>>k&1:
                i,j=divmod(k,n)
                rr[i]+=1;cc[j]+=1;vv.append(k)
        if max(rr)==n or max(cc)==n:continue
        w=[P[k] for k in vv]
        if sum(1<<v for v in w)!=mask: continue
        L+=(-1)**(len(vv)-1)*parity(w)
    d=(n-1)**2-1
    observed=(L-1)*((-1)**d)
    expected=parity(p)**(n+1)*parity(q)**(n+1)*(-1)**(sw*(n*(n-1)//2+n-1))
    assert observed==expected,(n,p,q,sw,observed,expected)
    return expected

if __name__=='__main__':
    for n in (2,3,4):
        print('fixed',n,fixed_face_homology(n))
        p=list(range(n));t=p.copy();t[0],t[1]=t[1],t[0]
        print('character',n,[ch(n,a,b,s) for a,b,s in [(p,p,False),(t,p,False),(p,t,False),(p,p,True),(t,p,True)]])
    print('MATCHING_FIXED_SPHERES_AND_CHARACTERS_VERIFIED')
