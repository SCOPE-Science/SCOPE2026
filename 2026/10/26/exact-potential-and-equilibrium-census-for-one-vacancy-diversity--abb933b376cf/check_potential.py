"""Reproduce exact-potential and two-type equilibrium-count checks.

Uses Python standard library and independent neighborhood utilities.
Run: python check_potential.py
"""
from fractions import Fraction
from itertools import product
from math import comb


def utility(profile, vertex, a, b):
    kind = profile[vertex]
    if kind < 0:
        raise ValueError('empty vertex has no utility')
    opp = range(a, a+b) if vertex < a else range(a)
    neighbors = [profile[v] for v in opp if profile[v] >= 0]
    return Fraction(sum(t != kind for t in neighbors), len(neighbors)) if neighbors else Fraction(0)


def potential_numerator(profile, a, b, k):
    c, d = a-1, b-1
    pop = [profile.count(i) for i in range(k)]
    aa = [profile[:a].count(i) for i in range(k)]
    vacancy_b = profile.index(-1) >= a
    return (c+d)*sum(x*x for x in aa)-2*c*sum(x*r for x,r in zip(aa,pop))+(c-d)*int(vacancy_b)


def check():
    moves=0
    states=0
    by_instance=[]
    for a in range(2,5):
      for b in range(2,5):
        for k in (2,3):
          n=a+b
          stable=0
          counted=[0]*n
          for vacancy in range(n):
            vertices=[v for v in range(n) if v!=vacancy]
            for colors in product(range(k),repeat=n-1):
              p=[-1]*n
              for v,col in zip(vertices,colors):p[v]=col
              states+=1
              before=potential_numerator(p,a,b,k)
              available=False
              for v in vertices:
                utility_before=utility(p,v,a,b)
                q=p[:]
                q[v],q[vacancy]=q[vacancy],q[v]
                gain=utility(q,vacancy,a,b)-utility_before
                after=potential_numerator(q,a,b,k)
                assert Fraction(after-before,2*(a-1)*(b-1)) == gain, (a,b,k,p,v,gain,after-before)
                moves+=1
                if gain>0:available=True
              if not available:
                stable+=1
                if k==2:counted[sum(t==1 for t in p)]+=1
          if k==2:
            predicted=[a*(comb(a-1,j) if 0<=j<=a-1 else 0)+a*(comb(a-1,j-b) if 0<=j-b<=a-1 else 0)
                       +b*(comb(b-1,j) if 0<=j<=b-1 else 0)+b*(comb(b-1,j-a) if 0<=j-a<=b-1 else 0) for j in range(n)]
            assert counted==predicted,(a,b,counted,predicted)
            assert stable==a*2**a+b*2**b
          by_instance.append((a,b,k,stable))
    print('PASS: fully independent cross-edge utilities versus exact potential increments')
    print('PASS: complete equilibrium enumerator for two colors')
    print('states_checked:',states,'all_legal_jump_moves_checked:',moves)
    print('instances:',len(by_instance),'example_K_3_4_two_colors:',[x for x in by_instance if x[:3]==(3,4,2)])
    return by_instance

if __name__=='__main__':check()
