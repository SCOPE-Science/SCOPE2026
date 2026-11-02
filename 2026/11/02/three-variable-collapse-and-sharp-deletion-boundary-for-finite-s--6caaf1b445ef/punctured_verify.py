#!/usr/bin/env python3
"""Finite cross-checks for punctures of Steiner triple systems in ternary block language."""
from collections import Counter
from itertools import product,combinations
from hashlib import sha256


def blocks_fano():
    p=range(1,8)
    return 7,{frozenset((a-1,b-1,(a^b)-1)) for a,b in combinations(p,2)}

def blocks_affine9():
    def a(i): return (i//3,i%3)
    def put(x,y): return (x%3)*3+(y%3)
    return 9,{frozenset((u,v,put((-a(u)[0]-a(v)[0])%3,(-a(u)[1]-a(v)[1])%3))) for u,v in combinations(range(9),2)}

def blocks_cyclic13():
    b=set()
    for base in [(0,1,4),(0,2,7)]:
        for shift in range(13):
            b.add(frozenset((x+shift)%13 for x in base))
    return 13,b

def blocks_projective15():
    return 15,{frozenset((a-1,b-1,(a^b)-1)) for a,b in combinations(range(1,16),2)}

def check_sts(n,blocks):
    assert len(blocks)==n*(n-1)//6, (n,len(blocks))
    co=Counter(tuple(sorted(pair)) for block in blocks for pair in combinations(block,2))
    assert len(co)==n*(n-1)//2 and set(co.values())=={1}

def puncture(n,blocks,deleted=0):
    return n-1,{frozenset({x-(x>deleted) for x in b}) for b in blocks if deleted not in b}

def classify_extensions(N,blocks):
    R={tuple(sorted(b)) for b in blocks}
    def rel(a,b,c): return tuple(sorted((a,b,c))) in R and len({a,b,c})==3
    def M(a,b):return a!=b and not any(rel(a,b,c) for c in range(N))
    for a in range(N):
        assert sum(M(a,c) for c in range(N))==1
    counts=Counter()
    for a in range(N):
      for b in range(N):
        state='equal' if a==b else 'matched' if M(a,b) else 'completed'
        classes=Counter()
        for z in range(N):
            if z==a: tag='equal_a'
            elif z==b: tag='equal_b'
            elif M(a,z): tag='mate_a'
            elif M(b,z): tag='mate_b'
            elif rel(a,b,z): tag='block_completion'
            else: tag='generic'
            if state=='completed':
                # Direct semantics of the displayed four-variable formula F_{a,b}(z).
                F=(z!=a and z!=b and not rel(a,b,z)
                   and any(rel(a,z,w) for w in range(N))
                   and any(rel(b,z,w) for w in range(N)))
                assert F==(tag=='generic'),(N,a,b,z,tag,F)
            classes[tag]+=1
        expected=({'equal_a':1,'mate_a':1,'generic':N-2} if state=='equal' else
                  {'equal_a':1,'equal_b':1,'generic':N-2} if state=='matched' else
                  {'equal_a':1,'equal_b':1,'mate_a':1,'mate_b':1,'block_completion':1,'generic':N-5})
        assert classes==Counter(expected),(N,a,b,state,classes,expected)
        counts[(state,tuple(sorted(classes.items())))]+=1
    return counts

def fo3_refine(systems,maxrounds=70):
    """Exact depth iteration for 3-variable FO, including empty-pebble state.
    A tuple coordinate None corresponds to an unassigned variable. Replacing a coordinate
    ranges over *all* vertices; set-valued support implements quantifiers without counting.
    Colors are shared globally across structures, never separately renamed.
    """
    stores=[]
    for name,N,blocks in systems:
        vertices=[None]+list(range(N))
        tuples=list(product(vertices,repeat=3))
        index={t:j for j,t in enumerate(tuples)}
        R={tuple(sorted(b)) for b in blocks}
        def initial(t):
            m=tuple(v is None for v in t)
            eq=tuple(t[i] is not None and t[i]==t[j] for i,j in [(0,1),(0,2),(1,2)])
            block=len(set(t))==3 and None not in t and tuple(sorted(t)) in R
            return (m,eq,block)
        neigh=[]
        for t in tuples:
            neigh.append(tuple(tuple(index[t[:i]+(v,)+t[i+1:]] for v in range(N)) for i in range(3)))
        stores.append((name,N,tuples,index,neigh,[initial(t) for t in tuples]))
    def renumber(signatures):
        D={}
        out=[]
        for s in signatures:
            if s not in D: D[s]=len(D)
            out.append(D[s])
        return out,len(D)
    flat=[col for store in stores for col in store[5]]
    color,ncolors=renumber(flat)
    offsets=[];offset=0
    for store in stores:
        offsets.append(offset);offset+=len(store[2])
    reports=[]
    for depth in range(maxrounds+1):
        nonecolors=[color[o+st[3][(None,None,None)]] for o,st in zip(offsets,stores)]
        reports.append((depth,ncolors,tuple(nonecolors)))
        if depth==maxrounds: break
        sig=[]
        for o,st in zip(offsets,stores):
            for j,row in enumerate(st[4]):
                sig.append((color[o+j],tuple(frozenset(color[o+k] for k in inds) for inds in row)))
        newcolor,newn=renumber(sig)
        if newn==ncolors:
            assert newcolor==color
            break
        color,ncolors=newcolor,newn
    return reports


def run():
    original=[('Fano',blocks_fano()),('Affine9',blocks_affine9()),('Cyclic13',blocks_cyclic13()),('Projective15',blocks_projective15())]
    punctured=[]
    complete=[]
    for name,(n,blocks) in original:
        check_sts(n,blocks)
        complete.append((name+' complete',n,blocks))
        N,remaining=puncture(n,blocks)
        print('SYSTEM',name,'parent',n,'puncture',N,'blocks',len(remaining))
        cases=classify_extensions(N,remaining)
        for (state,patterns),multiplicity in sorted(cases.items()):
            print('EXT',name,state,'anchor_pairs',multiplicity,'patterns',dict(patterns))
        assert sum(m for (_,p),m in cases.items())==N*N
        # 4-var separator: for at least one completed pair two generic distinct vertices
        has_two_generic=any(state=='completed' and dict(p).get('generic',0)>=2 for (state,p) in cases)
        assert has_two_generic==(n>=9)
        print('FO4_TWO_GENERIC',name,has_two_generic)
        punctured.append((name,N,remaining))
    print('FO3_STABLE_REFINEMENT')
    reports=fo3_refine(punctured)
    for depth,ncolors,types in reports: print('DEPTH',depth,'COLORS',ncolors,'EMPTY_TYPES',types)
    assert len(set(reports[-1][2]))==1,'punctures not FO3 equivalent'
    print('RESULT_PASS',len(punctured),'punctured Steiner triple systems, all empty states equivalent at fixed point')
    print('FULL_VS_PUNCTURED')
    reports2=fo3_refine(complete+punctured)
    for depth,ncolors,types in reports2: print('FULL_PUNCTURE_DEPTH',depth,'COLORS',ncolors,'EMPTY_TYPES',types)
    final=reports2[-1][2]
    assert len(set(final[:4]))==1 and len(set(final[4:]))==1 and final[0]!=final[4]
    print('TWO_FO3_CLASSES_PASS','4 complete / 4 punctured structures')

if __name__=='__main__':run()
