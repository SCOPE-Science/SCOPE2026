#!/usr/bin/env python3
"""Vertex-wise relational WL and distinguishing triple for the eight-point witness."""
from collections import Counter

def actions_cube():
    return [tuple(x^(1<<i) for x in range(8)) for i in range(3)]
def actions_two_k4():
    return [tuple((x//4)*4+((x%4)^mask) for x in range(8)) for mask in (1,2,3)]
def atomic(i,j,actions):
    return (i==j,tuple(z for z,f in enumerate(actions) if f[i]==j))
def rel_refinement(actions):
    n=len(actions[0]); color=(0,)*n; stages=[]
    for t in range(4):
        raw=[]
        for x in range(n):
            raw.append((color[x],tuple(sorted(Counter((atomic(x,y,actions),color[y]) for y in range(n)).items()))))
        palette={x:i for i,x in enumerate(sorted(set(raw)))}
        nxt=tuple(palette[r] for r in raw)
        stages.append(len(set(nxt)))
        if nxt==color:break
        color=nxt
    return stages,color

def check(actions):
    n=len(actions[0]); assert n==8
    for f in actions:
        assert sorted(f)==list(range(n))
        assert all(f[f[x]]==x for x in range(n))
    for f in actions:
        for g in actions:
            assert all(f[g[x]]==g[f[x]] for x in range(n))
    # Number of triples witnessing R_1(x,y) & R_2(y,z) & R_3(z,x)
    triangles=sum(actions[0][x]==y and actions[1][y]==z and actions[2][z]==x
                  for x in range(n) for y in range(n) for z in range(n))
    # A generator orbit is a connected component of the union of the matchings.
    unseen=set(range(n)); orbits=[]
    while unseen:
        x=min(unseen); reached={x}; frontier=[x]
        while frontier:
            y=frontier.pop()
            for f in actions:
                z=f[y]
                if z not in reached: reached.add(z); frontier.append(z)
        orbits.append(len(reached)); unseen-=reached
    sig=Counter(tuple(sorted(Counter(atomic(x,y,actions) for y in range(n)).items())) for x in range(n))
    return sorted(orbits),triangles,rel_refinement(actions),sig

def main():
    cube=check(actions_cube()); double=check(actions_two_k4())
    assert cube[0]==[8] and double[0]==[4,4]
    assert cube[1]==0 and double[1]==8
    assert cube[2][1]==double[2][1] and len(set(cube[2][1]))==1
    assert cube[3]==double[3]
    print('cube: orbits',cube[0],'triangles',cube[1],'WL',cube[2][0])
    print('two K4: orbits',double[0],'triangles',double[1],'WL',double[2][0])
    for k in range(3,8):
        a=actions_cube()+[tuple(range(8))]*(k-3)
        b=actions_two_k4()+[tuple(range(8))]*(k-3)
        assert check(a)[3]==check(b)[3]
        print('witness extends to',k,'involutions')
    print('VERIFY_WITNESS_OK')
if __name__=='__main__':main()
