# Fukuda First-Layer Stabilization over Q(sqrt29) at p = 5

## Context

Let k = Q(sqrt29) and let k_infty/k be its cyclotomic Z_5-extension, with
[k_n:k]=5^n.  Write A_n for the 5-primary part of Cl(k_n).  Fukuda's
stabilization theorem gives an efficient route to Greenberg's conjecture in
this setting: once the primes above 5 are totally ramified, equality of two
consecutive 5-class-group orders forces stabilization.  The point of this
record is to certify the first equality |A_0|=|A_1| for the pair (k,p) =
(Q(sqrt29),5).

## Definitions and first layer

Write O_k=Z[omega], omega=(1+sqrt29)/2, with minimal polynomial
y^2-y-7.  Let Q_1 be the degree-5 subfield of Q(zeta_25), with

m_Q1(x)=x^5-10x^3+5x^2+10x+1.

Then k_1=k Q_1 has degree 10 over Q and degree 5 over k.  One primitive
polynomial produced by the exact resultant calculation is

T^10 - 5T^9 - 45T^8 + 220T^7 + 520T^6 - 2394T^5
 - 2150T^4 + 7635T^3 + 2985T^2 - 1445T - 107.

The fundamental unit used below is epsilon=(5+sqrt29)/2=2+omega, of norm -1.

## Result

For the cyclotomic Z_5-extension of k=Q(sqrt29),

|A_0|=|A_1|=1,

both primes of k above 5 are totally ramified throughout the tower, and
therefore

lambda_5(k)=mu_5(k)=0.

## Proof

### Base layer

The real-quadratic Minkowski bound is sqrt(29)/2<2.7.  The polynomial
x^2-x-7 is irreducible modulo 2, so 2 is inert and there is no ideal of norm
2.  Hence every ideal class contains the unit ideal and h(k)=1.  Thus
|A_0|=1.

### Cyclotomic first layer and ramification

The Gaussian-period construction in `artifacts/period_Q1.py` gives the
degree-5 polynomial m_Q1 above.  Q_1 is the degree-5 subfield of Q(zeta_25),
so it is cyclic and ramified only at 5; locally at 5 it is totally ramified
of degree 5.

Since 29 is a square modulo 5, 5 splits in k.  The roots of y^2-y-7 mod 5
are 2 and 4 and are simple, so the two completions k_p above 5 are both
Q_5.  Consequently, after forming k_1=kQ_1, each of the two primes above 5
is totally ramified of relative degree 5.  The same cyclotomic-local
description gives total ramification at every higher layer.

### Ambiguous classes and the unit norm obstruction

For the cyclic extension k_1/k of degree 5, the Chevalley ambiguous class
number formula gives

|Cl(k_1)^G| = 5/j,

where

j=[E_k : E_k ∩ N_{k_1/k}(k_1^×)]

and j is 1 or 5.  The exact Pell scan in `artifacts/unit_obstruction.py`
confirms that epsilon=(5+sqrt29)/2 is a fundamental unit.

The local norm test needed here is the following *specific cyclotomic
Q_5 statement*.  Let F/Q_5 be the degree-5 subfield of Q_5(zeta_25).
Local reciprocity identifies Gal(Q_5(zeta_25)/Q_5) with
(Z/25Z)^×.  The norm subgroup for F is the preimage of the unique subgroup
of order 4, namely the fifth powers modulo 25.  Therefore a Q_5-unit is a
norm from F exactly when its residue modulo 25 lies in

{1,7,18,24},

equivalently when u^4=1 mod 25.  No claim is made that
N(U_L)=U_K^5 for an arbitrary unramified base extension K/Q_5 of higher
residue degree.

Hensel lifting sends omega at the two split 5-adic places to 12 and 14
modulo 25.  Hence epsilon=2+omega maps to 14 and 16.  Their fourth powers
are

14^4 = 16 mod 25,   16^4 = 11 mod 25,

so epsilon is not a local norm at either place and therefore is not a global
norm.  Thus j=5 and |Cl(k_1)^G|=1.

If the 5-primary part A_1 were nontrivial, the order-5 group G acting on the
finite 5-group A_1 would have a nontrivial fixed point (equivalently, on
A_1[5] the order-5 action is unipotent).  Since Cl(k_1)^G is trivial, A_1 is
trivial.  Therefore |A_1|=1=|A_0|.

### Fukuda stabilization

Fukuda's 1994 stabilization theorem applies because the primes above 5 are
already totally ramified from the base layer and |A_0|=|A_1|.  Hence the
5-primary class-group orders stabilize and lambda_5(k)=mu_5(k)=0.

## Reproducibility

The exact arithmetic packaged with this record is repository-relative:

- `artifacts/minkowski_h1.py`
- `artifacts/period_Q1.py`
- `artifacts/compositum_k1.py`
- `artifacts/unit_obstruction.py`

The JSON outputs in `artifacts/` record the corresponding polynomial,
discriminant, Hensel-lift, and unit-congruence data.  These scripts verify
the explicit arithmetic; the use of Chevalley's formula, local reciprocity,
and Fukuda's theorem remains a mathematical theorem dependency rather than
a machine-checked step.

## Limitations

This proves only the 5-primary stabilization in the cyclotomic Z_5 tower of
Q(sqrt29).  It does not compute the full class group of k_1 or higher layers,
nor does it establish a new general local norm theorem.  The priority of
this isolated numerical instance relative to all earlier real-abelian
Iwasawa computations is not asserted.

## References

- T. Fukuda, Remarks on Z_p-extensions of number fields, Proc. Japan Acad.
  Ser. A 70 (1994), 264-266.
- T. Fukuda and H. Taya, The Iwasawa lambda-invariants of Z_p-extensions of
  real quadratic fields, Acta Arith. 69 (1995), 277-292.
- T. Tsuji, On the Iwasawa lambda-invariants of real abelian fields,
  Trans. Amer. Math. Soc. 355 (2003), 3699-3714.
- Standard local class field theory/local reciprocity for Q_p cyclotomic
  extensions.
