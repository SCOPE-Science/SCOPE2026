"""Independent finite-tree test of the p-morphism/topological-minor criterion.
Standard-library only. Children are unordered tuples of subtrees.
"""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def trees(n):
    if n==1: return ((),)
    out=set()
    # Generate multisets of smaller rooted trees whose sizes total n-1.
    choices=sorted(((len(nodes(t)),str(t),t) for k in range(1,n) for t in trees(k)), key=lambda x:(x[0],x[1]))
    def rec(rest,lower,cur):
        if rest==0:
            out.add(tuple(cur));return
        for ix in range(lower,len(choices)):
            sz,_,t=choices[ix]
            if sz<=rest:rec(rest-sz,ix,cur+[t])
    rec(n-1,0,[])
    return tuple(sorted(out,key=str))

def nodes(t):
    return [()] + [(i,)+p for i,c in enumerate(t) for p in nodes(c)]

def descendants(t,p):
    return [q for q in nodes(t) if q[:len(p)]==p]

def sub(t,p):
    for i in p:t=t[i]
    return t

@lru_cache(None)
def embed_at(s,t):
    if not t:return True
    if len(s)<len(t):return False
    edges=[]
    for target_child in t:
        possible=[]
        for i,source_child in enumerate(s):
            if any(embed_at(sub(source_child,p),target_child) for p in nodes(source_child)):
                possible.append(i)
        edges.append(possible)
    def match(k,used):
        if k==len(edges):return True
        return any(match(k+1,used|{i}) for i in edges[k] if i not in used)
    return match(0,set())

def embeds(s,t):
    return any(embed_at(sub(s,p),t) for p in nodes(s))

@lru_cache(None)
def pm(s,t):
    # Existence of a p-morphism from rooted source subtree s into
    # the target cone at its root, sending source root to target root.
    if not s:return not t
    # At least one source child maps to target root (then covers target cone).
    for i,c in enumerate(s):
        if pm(c,t) and all(any(pm(z,sub(t,p)) for p in nodes(t)) for j,z in enumerate(s) if j!=i):
            return True
    # Otherwise every target child is represented by a DISTINCT source child
    # that maps directly to it; other source children may map deeper.
    if len(s)<len(t):return False
    if not t:return True
    edges=[]
    for tc in t:
        options=[]
        for i,c in enumerate(s):
            if pm(c,tc):options.append(i)
        edges.append(options)
    def match(k,used):
        if k==len(edges):return True
        return any(match(k+1,used|{i}) for i in edges[k] if i not in used)
    return match(0,set())

# This implementation purposely does NOT use pm to compute the embeddings.

def brute_p_morphism(s,t):
    ss=nodes(s);tt=nodes(t)
    if len(ss)<len(tt):return False
    Sdesc={p:set(descendants(s,p)) for p in ss}
    Tdesc={p:set(descendants(t,p)) for p in tt}
    for assn in product(tt,repeat=len(ss)-1):
        f=dict(zip(ss,((),)+assn))
        if not all(f[q] in Tdesc[f[p]] for p in ss for q in Sdesc[p]):continue
        if all({f[q] for q in Sdesc[p]}==Tdesc[f[p]] for p in ss):return True
    return False

if __name__=='__main__':
    for n in range(1,8):
        print('rooted tree types',n,len(trees(n)))
    tests=0
    for n in range(1,8):
      for s in trees(n):
       for m in range(1,n+1):
        for t in trees(m):
            actual=pm(s,t); expect=embeds(s,t); tests+=1
            if actual!=expect:raise AssertionError(('criterion collision',s,t,actual,expect))
    print('DP_VS_EMBED_OK',tests)
    brute_tests=0
    for n in range(1,6):
      for s in trees(n):
       for m in range(1,n+1):
        for t in trees(m):
            a=brute_p_morphism(s,t);b=pm(s,t); brute_tests+=1
            if a!=b:raise AssertionError(('brute collision',s,t,a,b))
    print('BRUTE_VS_DP_OK',brute_tests)
