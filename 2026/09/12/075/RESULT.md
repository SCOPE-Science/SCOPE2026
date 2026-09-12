# Heun accessory-parameter parameterized Picard–Vessiot trichotomy: case (C) for an admissible sqrt-parameter specialization

## Context
The admitted target asks for the parameterized Picard–Vessiot (PPV) Galois-group
trichotomy of the Heun accessory-parameter Fuchsian family over F=C(t,x) with
commuting derivations dx(x)=1, dt(t)=1: (A) reducible Borel, (B) infinite
imprimitive dihedral, or (C) Zariski-dense differential-algebraic subgroup of
SL2/GL2 with explicit dt-polynomial equations and an isomonodromic versus
non-isomonodromic verdict. The target requires an irreducibility witness via
Riccati rational solvability and non-resonance/monodromy irreducibility at the
four punctures, and the PPV group up to conjugacy.

## Definitions and specialization
Let C be algebraically closed of characteristic 0 and t transcendental over C
(generic t). Fix a=2, c=sqrt(2), d=sqrt(3), e=sqrt(5),
S=c+d+e-1, alpha=(S+sqrt(7))/2, beta=(S-sqrt(7))/2, so the Fuchsian relation
alpha+beta+1=c+d+e holds. Consider
L = dx^2 + (c/x + d/(x-1) + e/(x-2)) dx + (t+alpha*beta*x)/(x(x-1)(x-2)).
Put the operator in SL2 normal form z''=r z via Y=z*exp(-int P/2) with
P=c/x+d/(x-1)+e/(x-2), D=x(x-1)(x-2), Q=(t+alpha*beta*x)/D,
r=P^2/4+P'/2-Q. Then together(r) has numerator degree 4 and denominator
degree 6, r has double poles exactly at x in {0,1,2} with nonzero coefficients
and pole order 2 at infinity, and r_t=-1/D.

## Result
For this admissible specialization with t transcendental, the PPV group is
case (C): up to conjugacy the full SL2 over the dt-constants, Zariski-dense
and Kolchin-dense. The defining dt-ideal is (0) apart from det=1; there are no
proper dt-polynomial equations cutting out the group. The family is
non-isomonodromic in t. Cases (A) Borel and (B) dihedral are excluded.

## Proof / evidence
Double-pole data (exact): b0=1/2-sqrt(2)/2, b1=3/4-sqrt(3)/2,
ba=5/4-sqrt(5)/2, b_inf=3/2; 1+4b0=(sqrt2-1)^2, 1+4b1=(sqrt3-1)^2,
1+4ba=(sqrt5-1)^2, 1+4b_inf=7, all with irrational square roots.
Kovacic case 1: local exponents are {sqrt2/2,1-sqrt2/2} at 0,
{sqrt3/2,1-sqrt3/2} at 1, {sqrt5/2,1-sqrt5/2} at 2, {(1+-sqrt7)/2} at
infinity. All 16 values d=alpha_inf-alpha0-alpha1-alpha_a are irrational:
the Galois flip sqrt2->-sqrt2 moves every combination by -/+sqrt2, and each
minimal polynomial has degree >1. Hence no rational Riccati solution and no
exponential solution; the ordinary PV group is irreducible and (A) is excluded.
Kovacic case 2: since every sqrt(1+4b_c) is irrational, all E-sets collapse to
{2}, giving d=(2-2-2-2)/2=-2<0, so no imprimitive solution; (B) excluded.
Kovacic case 3 requires sqrt(1+4b_c) rational at every pole and fails at every
pole. Thus the ordinary PV group of z''=r z is the full SL2.
Independently, exponent differences 1-sqrt2, 1-sqrt3, 1-sqrt5 at finite
punctures and sqrt7 at infinity are all irrational, hence non-integral: local
monodromies are non-resonant, confirming irreducibility at four punctures.
Non-isomonodromy: by the Arreche-Dreyfus/Cassidy-Singer criterion, isomonodromy
in t is equivalent to a rational Schlesinger factor A(x,t) solving
(1/2)A_xxx-2rA_x-r_x A-r_t=0, i.e. (1/2)A_xxx-2rA_x-r_x A+1/D=0.
A pole (x-c)^{-m} of A would require m(m+2)=4b_c, but
4b0=2-2sqrt2<0, 4b1=3-2sqrt3<0, 4ba=5-2sqrt5 approx 0.53<3=min_{m>=1}m(m+2),
so A has no finite poles. At infinity with b_inf=3/2 the leading balance
k(n-1)[(1/2)n(n-2)-3]=0 forces polynomial A of degree <=1. For A=u x+v the
constant numerator coefficient 32v(1-sqrt2) forces v=0; the x^6 and x^2
coefficients A6(t)u+4 and A2(t)u+16 have eliminant -128t+K of degree 1 in t,
nonzero for transcendental t, so no common u in C(t) exists. Polynomial
ansatze of degrees 1-4 all yield Groebner basis {1}. Hence no rational
solution: the family is not isomonodromic. Irreducible SL2 ordinary group plus
non-isomonodromy implies full-SL2 PPV group by the standard classification.

## Limitations
Proved for the stated admissible specialization with t transcendental
(generic t), not uniformly over all exponent tuples: resonant or rationally
related parameters can bifurcate into (A) or (B). The passage from certified
irreducibility plus non-isomonodromy to the full-SL2 PPV group uses the
standard Cassidy-Singer/Arreche-Dreyfus classification; the computational
certificates are exact and machine-checked.

## Reproducibility
Run `python3 artifacts/reproduce_target.py` (sympy); it asserts every boxed
identity and writes `certificates.json` and `groebner_log.json`.

## References
Cassidy-Singer, Galois theory of parameterized differential equations and
linear differential algebraic groups; Dreyfus arXiv:1110.1053, Computing the
Galois group of some parameterized linear differential equation of order two;
Arreche, On the computation of the parameterized differential Galois group
(JSC 2015) and ISSAC 2014 computation of the differential Galois group of a
parameterized second-order equation; Kovacic algorithm and Schlesinger
isomonodromy criterion as cited therein.
