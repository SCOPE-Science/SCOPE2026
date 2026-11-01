"""Exact cohort certificate for 3-color inhibitory oscillators on bridged cliques.

Only integer arithmetic is used. Each non-bridge clique cohort is indexed by
its initial color, with -1 marking an absent cohort. Thus the 441 templates
exhaust every labelled initial coloring of every pair of clique sizes >=2.
"""
from itertools import product
from math import comb

TARGET = (
 ((3,0,0),(0,0,0),(0,0,0)),
 ((8,6,0),(6,4,0),(0,0,0)),
 ((10,17,10),(17,25,15),(10,15,9)),
 ((8,6,0),(6,4,0),(0,0,0)),
 ((4,1,0),(1,0,0),(0,0,0)),
 ((12,10,3),(10,8,2),(3,2,0)),
 ((8,8,4),(8,6,2),(4,2,0)),
 ((4,5,0),(5,4,0),(0,0,0)),
 ((12,14,7),(14,12,4),(7,4,0)),
 ((12,14,3),(14,18,4),(3,4,0)),
)

def initial(u,v,p,q):
    return ((u,), (v,),
            tuple(c if p & (1 << c) else -1 for c in range(3)),
            tuple(c if q & (1 << c) else -1 for c in range(3)))

def transition(state):
    u,v,p,q = state
    # A bridge endpoint is adjacent to the B endpoint and all A interiors;
    # an A interior is adjacent to its A endpoint and every other A interior.
    inhibit_u = (v[0] == 1 or 1 in p)
    inhibit_v = (u[0] == 1 or 1 in q)
    inhibit_p = (u[0] == 1 or 1 in p)
    inhibit_q = (v[0] == 1 or 1 in q)
    def advance(c, inhibit):
        return -1 if c == -1 else (2 if c == 2 and inhibit else (c + 1) % 3)
    return ((advance(u[0], inhibit_u),),
            (advance(v[0], inhibit_v),),
            tuple(advance(c, inhibit_p) for c in p),
            tuple(advance(c, inhibit_q) for c in q))

def synchronized(state):
    return len({c for group in state for c in group if c != -1}) == 1

def weight(k, n):
    return sum((-1)**(k-j)*comb(k,j)*j**n for j in range(k+1))

def run():
    tables = [[[0]*3 for _ in range(3)] for __ in range(10)]
    total = 0
    max_delay = 0
    extremizer = None
    for u,v,p,q in product(range(3), range(3), range(1,8), range(1,8)):
        total += 1
        state = initial(u,v,p,q)
        t = 0
        while not synchronized(state) and t <= 9:
            state = transition(state)
            t += 1
        assert t <= 9 and synchronized(state), (u,v,p,q)
        tables[t][p.bit_count()-1][q.bit_count()-1] += 1
        if t > max_delay:
            max_delay, extremizer = t, (u,v,p,q)
        # Once synchronized the colors advance in unison with period three.
        if synchronized(state):
            assert synchronized(transition(state))
    matrices = tuple(tuple(tuple(row) for row in mat) for mat in tables)
    assert matrices == TARGET, matrices
    assert total == 441 and max_delay == 9
    # The aggregate formula must count every initial configuration.
    for a in range(2,13):
        for b in range(2,13):
            values = [sum(tables[t][i][j]*weight(i+1,a-1)*weight(j+1,b-1)
                          for i in range(3) for j in range(3)) for t in range(10)]
            assert sum(values) == 3**(a+b)
            assert values[-1] > 0
    # For both large interior groups, fully populated 3-color supports dominate;
    # their coefficient is 9 and every other support has an exponentially small weight.
    assert tables[2][2][2] == 9
    assert all(tables[t][2][2] == 0 for t in range(10) if t != 2)
    print('CERTIFICATE_OK: 441 exact color-cohort templates, maximum time 9')
    print('time_matrix_counts:', [(t,sum(map(sum,mat))) for t,mat in enumerate(tables)])
    print('sharp_template:',extremizer)
    print('FORMAL_COUNT_IDENTITY_OK: all tested a,b in 2..12')
    print('LARGE_CLIQUE_TWO_STEP_CONCENTRATION_OK')

if __name__ == '__main__':
    run()
