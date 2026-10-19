"""Numerical checks for a scalar exponential-clock Euler stability law.

Requires mpmath >= 1.3; checks approximate identities only. Mathematical
infinite-horizon conclusions require the accompanying analytic proof.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 70
nchecks = 0

def near(a, b, tolerance=mp.mpf('1e-46')):
    global nchecks
    assert abs(a - b) <= tolerance * max(1, abs(a), abs(b)), (a, b)
    nchecks += 1

def integ(t, p):
    a=1/t
    return mp.quad(lambda x: mp.exp(-x)*abs(1-t*x)**p, [0,a,mp.inf])

def integ_log(t):
    a=1/t
    return mp.quad(lambda x: mp.exp(-x)*mp.log(abs(1-t*x)),[0,a,mp.inf])

for t in [mp.mpf('0.15'),mp.mpf('0.35'),mp.mpf('0.75'),mp.mpf('1'),mp.mpf('1.2'),mp.mpf('2'),mp.mpf('2.5'),mp.mpf('3'),mp.mpf('5')]:
    near(integ_log(t),-mp.exp(-1/t)*mp.ei(1/t))
    near(integ(t,1),1-t+2*t*mp.exp(-1/t))
    near(integ(t,2),1-2*t+2*t*t)

u=mp.findroot(mp.ei,(mp.mpf('0.3'),mp.mpf('0.5')))
tc=1/u
assert 2.68450 < tc < 2.68452
nchecks+=1
near(mp.ei(1/tc),0)
assert mp.ei(mp.mpf('1')/mp.mpf('2.68450'))>0
assert mp.ei(mp.mpf('1')/mp.mpf('2.68452'))<0
nchecks+=2
assert -mp.exp(-1/mp.mpf('2.5'))*mp.ei(1/mp.mpf('2.5')) < 0
assert -mp.exp(-1/mp.mpf('3'))*mp.ei(1/mp.mpf('3')) > 0
nchecks+=2

# Independently solve for the positive moment cutoff in the mixed regime.
t=mp.mpf('1.2')
logmoment=lambda p: mp.log(integ(t,p))
cut=mp.findroot(logmoment,(mp.mpf('1.05'),mp.mpf('1.8')))
assert 1 < cut < 2
near(logmoment(cut),0,mp.mpf('1e-43'))
assert logmoment(mp.mpf('0.75')) < 0 < logmoment(mp.mpf('2.5'))
nchecks+=2

# Verify the exact one- and two-moment frontiers, and mean-sign boundary.
t1=1/mp.log(2)
near(1-t1+2*t1*mp.exp(-1/t1),1)
near(1-2+2,1)
assert 1<t1<2<tc
nchecks+=1

# Large-sample path checks are deliberately excluded: finite simulations
# cannot certify an almost-sure long-time statement.
print('VERIFICATION_OK; numerical identity and threshold checks:',nchecks)
print('critical_t:',mp.nstr(tc,55))
print('critical_root_Ei:',mp.nstr(u,55))
print('p_cutoff_at_t_1.2:',mp.nstr(cut,50))
print('absolute_first_moment_t:',mp.nstr(t1,50))
