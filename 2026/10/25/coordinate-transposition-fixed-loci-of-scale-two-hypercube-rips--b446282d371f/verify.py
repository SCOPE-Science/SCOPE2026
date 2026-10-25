#!/usr/bin/env python3
"""Finite independent checks for geometric coordinate-swap fixed loci in scale-two binary Rips complexes."""
from collections import defaultdict

def hamming(a,b):return (a^b).bit_count()

def actual_orbits(m):
    result=[]
    for tag,bits in [('A',(0,)),('B',(3,)),('C',(1,2))]:
        for z in range(1<<m):
            result.append(((tag,z), tuple((a<<m)|z for a in bits)))
    return result

def formula_adj(x,y):
    a,z=x;b,w=y;h=hamming(z,w)
    if a==b:return a!='C' and h<=2
    if {a,b}=={'A','B'}:return h==0
    return h<=1

def graph_cliques(vertices, neighbours):
    out=defaultdict(list)
    def rec(face,candidates):
        if face:out[len(face)-1].append(tuple(face))
        for j,v in enumerate(candidates):
            rec(face+[v],[u for u in candidates[j+1:] if u in neighbours[v]])
    rec([],list(range(len(vertices))))
    return out

def gf2rank(rows):
    piv={}
    for mask in rows:
        while mask:
            high=mask.bit_length()-1
            if high in piv:mask^=piv[high]
            else:piv[high]=mask;break
    return len(piv)

def reduced_betti(faces):
    rank={}
    for k in range(1,max(faces)+1):
        idx={t:j for j,t in enumerate(faces[k-1])}
        boundary=[]
        for t in faces[k]:
            row=0
            for j in range(len(t)):
                row^=1<<idx[t[:j]+t[j+1:]]
            boundary.append(row)
        rank[k]=gf2rank(boundary)
    b={k:len(faces[k])-rank.get(k,0)-rank.get(k+1,0) for k in faces}
    b[0]-=1
    return {k:v for k,v in b.items() if v}

def adams_adamaszek_c(m):
    return sum((j+1)*((1<<(m-2))-(1<<(i-1)))
               for i in range(1,m) for j in range(i)) if m>=3 else 0

def original_lefschetz(m):
    n=m+2; verts=list(range(1<<n))
    neigh=[{w for w in verts if w!=v and hamming(v,w)<=2} for v in verts]
    faces=graph_cliques(verts,neigh)
    def swap(v):return ((v>>(m+1)&1)<<m)|((v>>m&1)<<(m+1))|(v&((1<<m)-1))
    total=0;fixed_faces=0
    for k,fs in faces.items():
        for f in fs:
            if {swap(v) for v in f} != set(f):continue
            fixed_faces+=1
            swaps=sum(1 for v in f if v<swap(v) and swap(v) in f)
            total += (-1)**(k+swaps)
    return sum(len(x) for x in faces.values()),fixed_faces,total

def main():
    total_orbit_faces=0
    for m in range(1,5):
        orbits=actual_orbits(m); V=[x for x,o in orbits]
        adj=[set() for _ in V]; tested=0
        for i,(x,orb) in enumerate(orbits):
            assert max(hamming(u,v) for u in orb for v in orb)<=2
            for j in range(i+1,len(orbits)):
                y,orb2=orbits[j]
                brute=all(hamming(u,v)<=2 for u in orb for v in orb2)
                assert brute==formula_adj(x,y),(m,x,y)
                tested+=1
                if brute:adj[i].add(j);adj[j].add(i)
        faces=graph_cliques(V,adj)
        total=sum(len(fs) for fs in faces.values());total_orbit_faces+=total
        betti=reduced_betti(faces)
        expected={2:(m-1)*(1<<m)+1}
        if adams_adamaszek_c(m): expected[3]=2*adams_adamaszek_c(m)
        assert betti==expected,(m,betti,expected)
        predicted_chi=1+sum((-1)**k*v for k,v in expected.items())
        printed='m=%d orbits=%d pairs=%d faces=%d betti=%s chi=%d' %(m,len(V),tested,total,betti,predicted_chi)
        if m<=3:
            original_count,fix_count,lf=original_lefschetz(m)
            assert lf==predicted_chi,(m,lf,predicted_chi)
            printed+=' ambient_faces=%d invariant_faces=%d Lefschetz=%d'%(original_count,fix_count,lf)
        print(printed)
    print('TOTAL_ORBIT_FACES=%d'%total_orbit_faces)
    print('VERIFY_OK')

if __name__=='__main__':main()
