"""Independent local-history and geometric checks for two-colour RSA at short times.

Run: python verify.py (requires Python 3 and mpmath).
"""
import math
import random
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 50
checks = 0

def check(name, statement):
    global checks
    assert statement, name
    checks += 1

# Dimensionless unit interaction range and unit proposal intensity.
E1 = Fraction(2)
T1 = Fraction(3)
check('one-dimensional exclusion-pair measure', E1 ** 2 - T1 == 1)
check('1D uniform-random cubic coefficient', (E1**2 + T1) / 12 == Fraction(7,12))
check('1D priority cubic coefficient', T1/6 == Fraction(1,2))
check('1D gap cubic coefficient', (E1**2 - T1)/12 == Fraction(1,12))

# Independent one-variable integral of the area overlap of two disks.
def disk_intersection(r):
    return 2*mp.acos(r/2) - r*mp.sqrt(4-r*r)/2
T2_num = 2*mp.pi*mp.quad(lambda r: r*disk_intersection(r), [0,1])
T2_closed = mp.pi**2 - (3*mp.sqrt(3)*mp.pi)/4
check('two-dimensional disk intersection integral', abs(T2_num-T2_closed)<mp.mpf('1e-45'))
random_2d = (mp.pi**2+T2_closed)/12
priority_2d = T2_closed/6
gap_2d = (mp.pi**2-T2_closed)/12
check('2D cubic difference positive', gap_2d > 0)
check('2D coefficients consistent', abs(random_2d-priority_2d-gap_2d)<mp.mpf('1e-45'))
check('2D exact difference', abs(gap_2d-mp.sqrt(3)*mp.pi/16)<mp.mpf('1e-45'))

# A finite, explicitly ordered three-arrival witness: two earlier centers
# nonoverlapping with one another but both conflicting with the third.
def placed_colors(points, mode, random_values):
    placements = []
    for x, u in zip(points, random_values):
        prohibited = {c for y,c in placements if abs(y-x)<1}
        available = [c for c in (0,1) if c not in prohibited]
        if not available:
            continue
        c = available[0] if mode=='priority' else available[int(u*len(available))]
        placements.append((x,c))
    return placements

witness_positions = [-0.9, 0.9, 0.0]
witness_draws = [0.1, 0.9, 0.25]
check('three-arrival random rule blocks third rod',len(placed_colors(witness_positions,'random',witness_draws))==2)
check('three-arrival priority rule accepts third rod',len(placed_colors(witness_positions,'priority',witness_draws))==3)

# Monte Carlo checks for exclusion geometry only (not an infinite-time proof).
rng = random.Random(240221)
for dimension, target, n, tol in [(1, .75, 160000, .004), (2, float(T2_closed/mp.pi**2), 230000, .004)]:
    overlaps=0
    for _ in range(n):
        if dimension==1:
            p=(2*rng.random()-1,0.)
            q=(2*rng.random()-1,0.)
        else:
            theta1=2*math.pi*rng.random(); radius1=math.sqrt(rng.random())
            theta2=2*math.pi*rng.random(); radius2=math.sqrt(rng.random())
            p=(radius1*math.cos(theta1),radius1*math.sin(theta1))
            q=(radius2*math.cos(theta2),radius2*math.sin(theta2))
        overlaps += (p[0]-q[0])**2+(p[1]-q[1])**2<1
    estimated=overlaps/n
    check(f'{dimension}D Monte Carlo overlap fraction',abs(estimated-target)<tol)
    print(f'{dimension}D overlap probability: MC={estimated:.8f}, exact={target:.8f}')

print('1D exact density corrections: random = -7/12, priority = -1/2; difference = 1/12')
print('2D random cubic loss:',mp.nstr(random_2d,25))
print('2D priority cubic loss:',mp.nstr(priority_2d,25))
print('2D priority-minus-random cubic gain:',mp.nstr(gap_2d,25))
print(f'Passed {checks} deterministic assertions.')
