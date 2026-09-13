# Disproof of the reducible 2-Mahler triangular differential classification as stated

## Context

The admitted target fixes k=2 and operators
L = l0(x) + l1(x) Phi_2 + l2(x) Phi_2^2 with li in C[x], l0*l2 nonzero,
reducible over C(x). It proposes a triangular classification: every Puiseux
solution of L(f)=0 is differentially algebraic over C(x) if and only if both
associated inhomogeneous order-one equations admit differentially algebraic
solutions, and otherwise every solution outside the one-dimensional order-one
submodule is differentially transcendental with parametrized Galois group of
differential dimension 2. A complete answer proves this for all such operators
or gives an explicit reducible L0 plus a certified Puiseux solution violating
it in either direction.

## Definitions

K = C(x), Phi(f)(x) = f(x^2), K_px = union_m C((x^{1/m})).
L1 = x - (1+x) Phi + Phi^2 = (Phi - x)(Phi - 1).
F(x) = -sum_{k>=0} x^{2^k} in x C[[x]] (Fredholm series up to sign).

## Result

The classification is false as stated. L1 has polynomial coefficients with
l0*l2 = x nonzero, is reducible over C(x), and lies in the "otherwise" branch,
yet its (parametrized) Galois group has (differential) dimension at most 1,
not 2. The transcendence half holds for L1: every solution outside C*1 is
differentially transcendental. Only the unconditional dimension-2 clause fails.
The obstruction is structural (diagonal-trivial/unipotent), not computational.

## Proof / evidence

Factorization: (Phi-v)(Phi-u) f = f(x^4) - (u(x^2)+v(x)) f(x^2) + v(x)u(x) f(x).
With u=1, v=x this is Phi^2 - (1+x) Phi + x = L1. Order-one submodule
Phi(y)=y, quotient Phi(z)=x z; both diagonal solutions 1, x lie in K.

Phi-invariants in K_px are C: for f = sum a_q x^q, f(x^2)=f(x) forces only q=0
by ascent/descent on exponents (positive exponents descend q -> q/2 forcing
j divisible by 2^k for all k; negative exponents ascend 2^k q contradicting the
lower bound). Hence {h: h(x^2)=x h(x)} = C*x via ord: 2 ord(h)=1+ord(h).

F satisfies F(x^2) = F(x)+x, so (Phi-1)F = x and (Phi-x)x = 0, hence L1(F)=0
and L1(1)=0. If L1(f)=0, put g=(Phi-1)f; then (Phi-x)g=0 so g=cx; thus
ker_{K_px}(L1) = {a+bF : a,b in C}, submodule C*1.

F is not rational: if F=P/Q with Q(0)=1, then F(x^{2^n}) = P(x^{2^n})/Q(x^{2^n})
in lowest terms has at least 2^n distinct poles from any nonzero root of Q,
while F(x)+x+...+x^{2^{n-1}} has poles only among roots of Q; for 2^n > deg Q
this is impossible, so Q is constant, but F is lacunary hence non-polynomial.
By Becker's theorem (a C[[x]]-solution of a nonzero linear Mahler equation over
C(x) that is differentially algebraic is rational), F is differentially
transcendental; so is every a+bF with b != 0. In particular (Phi-1)g=x has no
differentially algebraic Puiseux solution, placing L1 in the "otherwise" branch.

Galois bound: the splitting field over K is K(F) since both diagonal solutions
are rational. For sigma in the difference Galois group G,
c_sigma = sigma(F)-F satisfies Phi(c_sigma)=c_sigma, hence c_sigma in C by the
constants description; sigma -> c_sigma embeds G into G_a, so dim G <= 1. Any
parametrized delta-refinement is a differential-algebraic subgroup of G_a,
hence of differential dimension at most 1 (0 or all of G_a). This contradicts
the universal differential-dimension-2 assertion.

Finite-order checks in output/artifacts/verify_L1.py (factorization
coefficients; F(x^2)-F(x)=x and L1(F)=0 to order 199) all pass and support the
exact series identities proved above.

## Limitations

Becker's hypertranscendence theorem is cited, not re-proved. The constants
description for the Picard-Vessiot ring uses standard difference Galois theory
(base constants algebraically closed). Exactness of the parametrized group
(G_a versus a proper differential subgroup) is left open; only the upper bound
<=1 is needed. No full corrected classification of all reducible order-two
2-Mahler operators is supplied.

## Reproducibility

Run `python3 output/artifacts/verify_L1.py` (pure Python, no dependencies).
All lemmas are proved from first principles in this record except the cited
Becker theorem.

## References

- T. Dreyfus, C. Hardouin, J. Roques, Hypertranscendence of solutions of Mahler
  equations, J. Eur. Math. Soc. 20 (2018), 2209-2238.
- J. Roques, On the algebraic relations between Mahler functions (survey:
  difference Galois groups, factorization/triangularization of Mahler
  operators, order-two aspects).
- C. Hardouin, A. Minchenko, A. Ovchinnikov, Calculating differential Galois
  groups of parametrized differential equations, Math. Ann. 368 (2017).
- C. E. Arreche, T. Dreyfus, J. Roques, Differential transcendence criteria
  for second-order linear difference equations, J. Ec. Polytech. Math. (2021).
- B. Adamczewski, T. Dreyfus, C. Hardouin, Hypertranscendence and linear
  difference equations, J. Amer. Math. Soc. (2021) — context for Becker-type
  criteria used in Lemma 6.
