#!/usr/bin/env python3
"""Check singleton color classes against rational subplanes in extension fields."""
from check_plane import Field,plane,refine
from collections import Counter

def fixed_subfield(f,degree):
    def power(x,n):
        a=1
        for _ in range(n):a=f.mul(a,x)
        return a
    return {x for x in range(f.q) if power(x,f.p**degree)==x}

def test(p,e,poly,d,add_fifth):
    f=Field(p,e,poly); V,I,adj=plane(f); n=len(V)
    K=fixed_subfield(f,d)
    O=I[(0,0,1)]; X=I[(1,0,0)]; Y=I[(0,1,0)]; U=I[(1,1,1)]
    marks=[O,X,Y,U]
    if add_fifth:
      t=next(x for x in K if x not in (0,1))
      marks.append(I[f.norm((t,0,1))])
    colors,hist=refine(adj,marks)
    sizes=Counter(colors)
    singletons={i for i,c in enumerate(colors) if sizes[c]==1}
    rational={i for i,v in enumerate(V) if set(v).issubset(K)}
    rational|={n+i for i,v in enumerate(V) if set(v).issubset(K)}
    assert singletons==rational,(p,e,d,len(singletons),len(rational))
    print(f'q={f.q}, subfield_order={len(K)}, marks={len(marks)}, singleton_points={len(singletons.intersection(range(n)))}, singleton_lines={len(singletons.difference(range(n)))}, total_color_classes={len(sizes)} PASS')

if __name__=='__main__':
    test(2,2,[1,1,1],1,False)
    test(2,3,[1,1,0,1],1,False)
    test(3,2,[1,0,1],1,False)
    test(2,4,[1,1,0,0,1],1,False)
    test(2,4,[1,1,0,0,1],2,True)
