"""Exhaustive small-frame replay for rooted finite modal diagrams.

Usage: python3 verify.py
Only standard library is required.
"""
from itertools import product

def frames(n):
    for mask in range(1 << (n*n)):
        yield tuple(frozenset(j for j in range(n) if mask & (1 << (i*n+j))) for i in range(n))

def reachable(R, w):
    seen={w}; stack=[w]
    while stack:
        for v in R[stack.pop()]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return seen

def radius_ok(R, h):
    for w in range(len(R)):
        layer={w}; covered={w}
        for _ in range(h):
            layer=set().union(*(R[u] for u in layer)) if layer else set()
            covered |= layer
        if reachable(R,w) != covered: return False
    return True

def p_morphism(R, F, g, w):
    X=sorted(reachable(R,g)); Y=reachable(F,w)
    for vals in product(sorted(Y), repeat=len(X)):
        z=dict(zip(X,vals))
        if z[g]!=w or set(vals)!=Y: continue
        if all({z[y] for y in R[x]}==F[z[x]] for x in X):
            return True
    return False

def diagram_satisfiable(R, F, g, w, h):
    X=sorted(reachable(R,g)); full=range(len(F))
    # Assign one and only one labelled target to each accessible state.
    for vals in product(full, repeat=len(X)):
        z=dict(zip(X,vals))
        if z[g] != w: continue
        reached_h={g}; layer={g}
        for _ in range(h):
            layer=set().union(*(R[x] for x in layer)) if layer else set()
            reached_h |= layer
        if all({z[y] for y in R[x]} == F[z[x]] for x in reached_h):
            return True
    return False

def run():
    checks=0
    for h in (0,1,2):
        for n in (1,2):
            for F in frames(n):
                if not radius_ok(F,h): continue
                for w in range(n):
                    for m in (1,2):
                        for R in frames(m):
                            if not radius_ok(R,h): continue
                            for g in range(m):
                                a=p_morphism(R,F,g,w)
                                b=diagram_satisfiable(R,F,g,w,h)
                                assert a==b,(h,F,w,R,g,a,b)
                                checks+=1
        # Saturation at an end point cannot be seen before depth h+1.
        if h<=2:
            loop=tuple((frozenset({i+1}) if i<h else frozenset({h})) for i in range(h+1))
            dead=tuple((frozenset({i+1}) if i<h else frozenset()) for i in range(h+1))
            assert radius_ok(loop,h) and radius_ok(dead,h)
            assert not p_morphism(dead,loop,0,0)
    print('BOUNDED_MODAL_VERIFY_OK', checks)
if __name__=='__main__': run()
