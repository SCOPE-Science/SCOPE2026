"""Independent exact checks for the bidirected K(2,6) multipath complex.

Usage: python verify.py
Run in the same folder as morse_certificate.json. Python standard library only.
"""
import itertools
import json
from collections import Counter
from pathlib import Path


def arcs(n):
    return ([(h, 2+i) for h in (0, 1) for i in range(n)]
            + [(2+i, h) for h in (0, 1) for i in range(n)])


def legal(subset, edgelist):
    sources = set()
    targets = set()
    successor = {}
    for index in subset:
        a,b = edgelist[index]
        if a in sources or b in targets:
            return False
        sources.add(a)
        targets.add(b)
        successor[a] = b
    for a in successor:
        seen = set()
        vertex = a
        while vertex in successor:
            if vertex in seen:
                return False
            seen.add(vertex)
            vertex = successor[vertex]
    return True


def all_faces(n):
    edgelist = arcs(n)
    answer = [set() for _ in range(4)]
    for size in range(1, 5):
        for subset in itertools.combinations(range(len(edgelist)),size):
            if legal(subset, edgelist):
                mask = sum(1 << index for index in subset)
                answer[size-1].add(mask)
    return answer


def is_face(f, g):
    return f != g and f & g == f


def verify_morse():
    faces = all_faces(6)
    assert [len(s) for s in faces] == [24, 192, 600, 600]
    allf = set().union(*faces)
    n = 24
    # Cover relation is deletion of one arc; 4 is maximal dimension.
    cofaces = {s:[] for s in allf}
    downs = {s:[] for s in allf}
    for f in allf:
        for bit in range(n):
            b = 1<<bit
            if f & b:
                sub = f ^ b
                if sub:
                    assert sub in allf
                    cofaces[sub].append(f)
                    downs[f].append(sub)
    data=json.loads((Path(__file__).parent/'morse_certificate.json').read_text())
    assert data['graph']=='symmetric_orientation_of_K_2_6'
    remaining=set(allf)
    paired=set()
    critical=[]
    for op in data['steps']:
        if op[0] == 'P':
            assert len(op)==3
            s,t=op[1:]
            assert s in remaining and t in remaining
            assert s in downs[t]
            assert [v for v in cofaces[s] if v in remaining]==[t]
            assert all(v not in remaining for v in cofaces[t])
            assert s not in paired and t not in paired
            paired.add(s);paired.add(t)
            remaining.remove(s);remaining.remove(t)
        elif op[0]=='C':
            assert len(op)==2
            s=op[1]
            assert s in remaining
            assert all(v not in remaining for v in cofaces[s])
            critical.append(s)
            remaining.remove(s)
        else:
            raise AssertionError('Unknown operation')
    assert not remaining
    assert len(paired)==1246
    assert len(data['steps'])==793
    c=Counter(mask.bit_count()-1 for mask in critical)
    assert c=={0:1,3:169},c
    # Independent directed Hasse-graph acyclicity test. The pair reversals
    # orient from lower to higher; all other arrows go downward.
    reverse=set()
    for op in data['steps']:
        if op[0]=='P':reverse.add((op[1],op[2]))
    out={x:[] for x in allf};indeg={x:0 for x in allf}
    for upper in allf:
        for lower in downs[upper]:
            a,b=(lower,upper) if (lower,upper) in reverse else (upper,lower)
            out[a].append(b);indeg[b]+=1
    queue=[x for x,d in indeg.items() if d==0]
    visited=0
    while queue:
        x=queue.pop();visited+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert visited==len(allf),(visited,len(allf))
    print('Morse: 24,192,600,600 faces; 623 pairs; one critical vertex; 169 critical tetrahedra; acyclic.')


def rank_mod2(columns):
    basis={}
    for a in columns:
        while a:
            p=a.bit_length()-1
            if p in basis:a ^= basis[p]
            else:
                basis[p]=a
                break
    return len(basis)


def reduced_betti(n):
    groups=[sorted(q) for q in all_faces(n)]
    positions=[{f:i for i,f in enumerate(q)} for q in groups]
    ranks=[1]
    for dim in range(1,4):
        cols=[]
        for face in groups[dim]:
            c=0
            bit=1
            while bit<=face:
                if face&bit:c ^= (1<<positions[dim-1][face^bit])
                bit <<= 1
            cols.append(c)
        ranks.append(rank_mod2(cols))
    return [len(groups[i])-ranks[i]- (ranks[i+1] if i<3 else 0) for i in range(4)]


def check_smaller():
    expected={1:(1,0,0,0),2:(0,3,2,0),3:(0,1,6,0),4:(0,0,8,1),5:(0,0,1,32),6:(0,0,0,169)}
    for n, betti in expected.items():
        actual=tuple(reduced_betti(n))
        assert actual==betti,(n,actual,betti)
    print('Exact independent mod-two reduced Betti vectors n=1..6:',expected)

if __name__=='__main__':
    verify_morse()
    check_smaller()
    print('ALL TESTS PASS')
