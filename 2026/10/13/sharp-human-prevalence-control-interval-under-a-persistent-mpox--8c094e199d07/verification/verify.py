#!/usr/bin/env python3
"""Exact rational consistency checks for a standard-incidence human–rodent Mpox model.

This is a finite verification supplement. The all-parameter mathematical proof
is in RESULT.md. Requires Python's standard library only.
"""
from fractions import Fraction as Q


def coeff(h):
    A = h['delta'] + h['gamma'] + h['mu']
    B = h['mu'] + h['dh'] + h['phi']
    C = h['mu'] + h['dh'] + h['tau'] + h['psi']
    p = h['delta'] / (A * B)
    q = h['gamma'] / (A * C)
    r = (h['phi'] * p + h['psi'] * q) / h['mu']
    k = Q(1) / A + p + q + r
    D = Q(1) - h['tau'] * q
    assert all(z > 0 for z in (A, B, C, p, q, r, k, D))
    return A, B, C, p, q, r, k, D


def human_state(h, force):
    A, B, C, p, q, rr, k, D = coeff(h)
    Sh = h['Lam'] / (h['mu'] + D * force)
    inc = force * Sh
    Eh = inc / A
    Ih = p * inc
    Qh = q * inc
    Rh = rr * inc
    Nh = Sh + Eh + Ih + Qh + Rh
    assert Nh == Sh * (Q(1) + k * force)
    return Sh, Eh, Ih, Qh, Rh


def rodent_state(ro, force):
    a = ro['mu'] + ro['nu']
    b = ro['mu'] + ro['dr']
    Sr = ro['Lam'] / (ro['mu'] + force)
    Er = force * Sr / a
    Ir = ro['nu'] * Er / b
    Nr = Sr + Er + Ir
    assert Nr > 0
    return Sr, Er, Ir


def rhs(h, ro, states):
    Sh, Eh, Ih, Qh, Rh, Sr, Er, Ir = states
    Nh = Sh + Eh + Ih + Qh + Rh
    Nr = Sr + Er + Ir
    assert Nh > 0 and Nr > 0
    L = h['beta1'] * Ir / Nr + h['beta2'] * Ih / Nh
    Lr = ro['beta3'] * Ir / Nr
    A, B, C, *_ = coeff(h)
    return (
        h['Lam'] + h['tau']*Qh - L*Sh - h['mu']*Sh,
        L*Sh - A*Eh,
        h['delta']*Eh - B*Ih,
        h['gamma']*Eh - C*Qh,
        h['phi']*Ih + h['psi']*Qh - h['mu']*Rh,
        ro['Lam'] - (ro['mu'] + Lr)*Sr,
        Lr*Sr - (ro['mu'] + ro['nu'])*Er,
        ro['nu']*Er - (ro['mu'] + ro['dr'])*Ir,
    )


def check(h, ro, states):
    residuals = rhs(h, ro, states)
    assert len(residuals) == 8
    assert residuals == (Q(0),) * 8, residuals


h = {
    'Lam': Q(12), 'mu': Q(1), 'dh': Q(1),
    'delta': Q(2), 'gamma': Q(1), 'tau': Q(1),
    'phi': Q(1), 'psi': Q(1),
    'beta1': Q(2), 'beta2': Q(49,16),
}
ro = {
    'Lam': Q(12), 'mu': Q(1), 'dr': Q(1),
    'nu': Q(2), 'beta3': Q(6),
}
A, B, C, p, q, rr, k, D = coeff(h)
assert (A, B, C, p, q, rr, k, D) == (
    Q(4), Q(3), Q(4), Q(1,6), Q(1,16), Q(11,48), Q(17,24), Q(15,16))
Rhuman = h['beta2'] * p
Rrodent = ro['beta3'] * ro['nu'] / ((ro['mu']+ro['nu'])*(ro['mu']+ro['dr']))
assert Rhuman == Q(49,96) < 1
assert Rrodent == Q(2) > 1

ar = ro['mu'] + ro['nu']
br = ro['mu'] + ro['dr']
Lr = (ro['beta3']*ro['nu'] - ar*br)/(br+ro['nu'])
assert Lr == Q(3,2)
rodent = rodent_state(ro, Lr)
assert rodent == (Q(24,5), Q(12,5), Q(12,5))
rodent_fraction = rodent[2]/sum(rodent)
assert rodent_fraction == Q(1,4) == Lr/ro['beta3']
z = h['beta1'] * rodent_fraction
assert z == Q(1,2)

# Human-endemic branch forced by reservoir with human-to-human reproduction < 1.
L = Q(3,4)
expected_contact = (L-z)*(1+k*L)/(p*L)
assert expected_contact == h['beta2'] == Q(49,16)
human = human_state(h, L)
assert human == (Q(768,109), Q(144,109), Q(96,109), Q(36,109), Q(132,109))
states = human + rodent
check(h, ro, states)
J = human[2] / sum(human)
floor = p*z/(1+k*z)
assert J == Q(4,49)
assert floor == Q(4,65)
assert floor < J < p/k == Q(4,17)
assert h['beta2'] == 1/(p-k*J) - z/J
assert (k*L**2 + (1-k*z-Rhuman)*L - z) == 0

# Human-to-human contact suppressed entirely: exact sharp positive floor.
hzero = dict(h, beta2=Q(0))
human0 = human_state(hzero, z)
check(hzero, ro, human0 + rodent)
J0 = human0[2]/sum(human0)
assert J0 == floor
assert (1/(p-k*J0) - z/J0) == 0

# Disease-free branch and a rodent-free/human-only endemic branch.
rofree = dict(ro, beta3=Q(1))
rodent0 = rodent_state(rofree, Q(0))
assert rodent0 == (Q(12), Q(0), Q(0))
check(h, rofree, human_state(h, Q(0)) + rodent0)
hhigh = dict(h, beta2=Q(8))
assert hhigh['beta2'] * p == Q(4,3) > 1
Lhumanonly = (hhigh['beta2']*p-1)/k
assert Lhumanonly == Q(8,17)
check(hhigh, rofree, human_state(hhigh, Lhumanonly) + rodent0)

print('VERIFY_OK')
