#!/usr/bin/env python3
"""Independent direct face enumeration and F2 boundary-rank check."""
from collections import defaultdict

def check(n):
    edges = []
    for i in range(n):
        edges += [(i,(i+1)%n),(n+i,n+(i+1)%n),(i,n+i)]
    assert len(edges)==3*n
    F=defaultdict(list)
    def walk(edge,used,mask,num):
        if edge==len(edges):
            if num:F[num-1].append(mask)
            return
        walk(edge+1,used,mask,num)
        a,b=edges[edge]
        if not used&(1<<a|1<<b):
            walk(edge+1,used|(1<<a)|(1<<b),mask|(1<<edge),num+1)
    walk(0,0,0,0)
    rank={}
    for q in range(1,max(F)+1):
        ix={m:j for j,m in enumerate(F[q-1])}
        leading={}
        for mask in F[q]:
            v=0;m=mask
            while m:
                bit=m&-m;m^=bit
                v^=1<<ix[mask^bit]
            while v:
                j=v.bit_length()
                if j not in leading:
                    leading[j]=v;break
                v^=leading[j]
        rank[q]=len(leading)
    homology={q:len(fs)-rank.get(q,0)-rank.get(q+1,0)-(q==0) for q,fs in F.items()}
    print('n=%d faces=%d f_vector=%s reduced_F2_Betti=%s'%(n,sum(map(len,F.values())), [len(F[q]) for q in range(max(F)+1)], [homology[q] for q in range(max(F)+1)]))
    expected={3:[0,6],4:[0,0,4],5:[0,0,2,2],6:[0,0,0,12],7:[0,0,0,0,14],8:[0,0,0,0,3,7]}[n]
    assert all(homology.get(q,0)==expected[q] if q<len(expected) else homology.get(q,0)==0 for q in F)
if __name__=='__main__':
    for n in range(3,9):check(n)
    print('INDEPENDENT_F2_CHECK_OK')
