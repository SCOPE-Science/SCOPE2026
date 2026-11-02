#!/usr/bin/env python3
"""Standalone finite checks for the power semigroup of a rectangular band.
Run: python3 check_rect_power.py (Python standard library only).
"""
from itertools import permutations, product
from collections import Counter
from math import comb, factorial

def masks(a,b): return list(range(1,1<<(a*b)))
def row_col(x,a,b):
    r=0;c=0
    for i in range(a):
        for j in range(b):
            if (x>>(i*b+j))&1: r|=1<<i;c|=1<<j
    return r,c

def rect(r,c,a,b):
    return sum(1<<(i*b+j) for i in range(a) for j in range(b)
               if (r>>i)&1 and (c>>j)&1)

def mul(x,y,a,b): return rect(row_col(x,a,b)[0],row_col(y,a,b)[1],a,b)

def t_closed(u,v):
    return sum((-1)**(i+j)*comb(u,i)*comb(v,j)*(1<<((u-i)*(v-j)))
               for i in range(u+1) for j in range(v+1))-1

def all_fibers(a,b):
    f={}
    for x in masks(a,b): f.setdefault(row_col(x,a,b),[]).append(x)
    return f

def verify(a,b):
    f=all_fibers(a,b)
    if a==1:
        assert all(mul(x,y,a,b)==y for x,y in product(masks(a,b),repeat=2))
    if b==1:
        assert all(mul(x,y,a,b)==x for x,y in product(masks(a,b),repeat=2))
    for (r,c),xs in f.items():
        u=r.bit_count();v=c.bit_count()
        assert len(xs)==t_closed(u,v)+1,(a,b,u,v)
        assert rect(r,c,a,b) in xs
    for x,y in product(masks(a,b), repeat=2):
        z=mul(x,y,a,b)
        assert z==rect(row_col(x,a,b)[0],row_col(y,a,b)[1],a,b)
        assert mul(z,z,a,b)==z
    return f

def verify_automorphisms_2_2():
    a=b=2;f=verify(a,b)
    rr=[1,2,3]; cc=[1,2,3]
    total=0;images=set()
    for rperm in permutations([1,2]):
      alpha={1:rperm[0],2:rperm[1],3:3}
      for cperm in permutations([1,2]):
       beta={1:cperm[0],2:cperm[1],3:3}
       for six in permutations([x for x in f[3,3] if x!=rect(3,3,a,b)]):
        by_fiber={}
        for (r,c),members in f.items():
            target=f[alpha[r], beta[c]]
            if (r,c)==(3,3):
                nonrect=[x for x in members if x!=rect(r,c,a,b)]
                # six permutes the six nonrectangular subsets of full support.
                by_fiber.update(dict(zip(nonrect,six)))
            else:
                assert len(members)==1 and len(target)==1
            by_fiber[rect(r,c,a,b)]=rect(alpha[r],beta[c],a,b)
        assert len(by_fiber)==15 and len(set(by_fiber.values()))==15
        for x,y in product(masks(a,b), repeat=2):
            assert by_fiber[mul(x,y,a,b)]==mul(by_fiber[x],by_fiber[y],a,b)
        total+=1
        images.add(tuple(by_fiber[x] for x in masks(a,b)))
    assert total==2880 and len(images)==2880
    return total

def verify_random_generator_2_3():
    a,b=2,3; f=verify(a,b)
    row_maps=[{1:1,2:2,3:3},{1:2,2:1,3:3}]
    col_maps=[{1:1,2:2,4:4,3:3,5:5,6:6,7:7},
              {1:2,2:4,4:1,3:6,5:3,6:5,7:7}]
    count=0
    for al,be in product(row_maps,col_maps):
        m={}
        for (r,c),members in f.items():
            tar=f[al[r],be[c]]
            sr=rect(r,c,a,b);tr=rect(al[r],be[c],a,b)
            old=sorted(set(members)-{sr})
            new=sorted(set(tar)-{tr})
            assert len(old)==len(new)
            m[sr]=tr
            m.update(zip(old,new[::-1]))
        assert len(m)==63 and len(set(m.values()))==63
        for x,y in product(masks(a,b),repeat=2):
            assert m[mul(x,y,a,b)]==mul(m[x],m[y],a,b)
        count+=1
    return count

if __name__=='__main__':
  for dims in [(1,1),(1,3),(2,2),(2,3),(3,2),(3,3)]:
    f=verify(*dims)
    print('fibers',dims,len(f),'largest size',max(map(len,f.values())))
  print('automorphisms_exact_2x2',verify_automorphisms_2_2())
  print('automorphisms_constructed_2x3',verify_random_generator_2_3())
  print('t22,t23,t33',*(t_closed(u,v) for u,v in [(2,2),(2,3),(3,3)]))
  print('VERIFY_OK')
