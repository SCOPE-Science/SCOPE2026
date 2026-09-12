# Exact genus-zero one-pointed psi^7 divisor descendant on toric dP3 in class 4H-2E1-E2-E3

## Context

This record resolves the admitted target: the exact rational value of a genus-zero
one-pointed descendant Gromov-Witten invariant of the smooth toric del Pezzo
surface of degree 6 (dP3). The surface, curve class, marking number, divisor
insertion, and psi-power were fixed before computation in the topic
specification. The invariant is a zero-dimensional virtual integral, hence a
single rational number, and is a standard test datum for toric mirror-symmetry
software, quantum cohomology of del Pezzo surfaces, and descendant
correspondences.

## Definitions

Let X3 be the smooth projective toric surface obtained by blowing up P^2 at the
three torus-fixed coordinate points p1=[1:0:0], p2=[0:1:0], p3=[0:0:1] for the
standard 2-torus action. Let H be the pullback hyperplane class and E1,E2,E3 the
exceptional divisors. The Picard group is Z H + Z E1 + Z E2 + Z E3 with
intersection pairing <H,H>=1, <Ei,Ej>=-delta_ij, <H,Ei>=0.
The anticanonical class -K_X3=3H-E1-E2-E3 is ample, so X3 is toric Fano.

Let beta3=4H-2E1-E2-E3 in H_2(X3;Z). Let Mbar_{0,1}(X3,beta3) be the moduli
stack of genus-zero one-pointed stable maps of class beta3, with cotangent line
class psi_1 and evaluation map ev_1. For a divisor class D, write

<tau_k(D)>_{0,1,beta3}^{X3} := integral over [Mbar_{0,1}(X3,beta3)]^vir of
psi_1^k cup ev_1^*(D).

The six torus-invariant prime divisors in cyclic order are
D1=E1, D2=H-E1-E3, D3=E3, D4=H-E2-E3, D5=E2, D6=H-E1-E2,
each with self-intersection -1 and consecutive intersection +1. One has
D1+D2+D3=H and D3+D4+D5=H in Pic(X3).

## Result

For exactly this surface, class, one marking, and insertion H with psi-power 7:

<tau_7(H)>_{0,1,beta3}^{X3} = -7/8.

That is, the integral of psi_1^7 cup ev_1^*(H) over the virtual class of
Mbar_{0,1}(X3,beta3) equals the explicit rational number -7/8.

## Proof / evidence

Dimension: c1(X3).beta3 = 3*4-2-1-1 = 8. For n=1, g=0,
vdim Mbar_{0,1}(X3,beta3) = dim X3-3+1+c1.beta3 = 2-3+1+8 = 8.
Insertion degree deg psi_1^7 + deg H = 7+1 = 8, so the integral is a
zero-dimensional virtual number, not forced to vanish.

Pairings k_i := D_i.beta3 give k=(2,1,1,2,1,1), sum 8 = c1.beta3, and
product k_i! = 2!1!1!2!1!1! = 4. Harmonic numbers H_2=3/2, H_1=1 give
S := sum_i H_{k_i} D_i = 3/2 D1+D2+D3+3/2 D4+D5+D6
= 7/2 H - 1/2 E1 - 3/2 E2 - 3/2 E3, so the H-basis coefficient is S_H=7/2.
Effectivity: 2E2+2E3+2D4+D2+D6 = beta3 exhibits beta3 as effective.

Givental toric mirror theorem for smooth toric Fano manifolds gives
J(tau(y),z)=I(y,z), with small I-function
I(y,z)=z sum_beta y^beta prod_i prod_{m=-inf}^{0}(D_i+mz)/prod_{m=-inf}^{k_i(beta)}(D_i+mz).
For beta3 all k_i>=0,
I_{beta3} = z y^{beta3} prod_i prod_{m=1}^{k_i} 1/(D_i+mz)
= y^{beta3}/4 [z^{-7} - S z^{-8} + O(z^{-9})] using
prod_{m=1}^k(D+mz)=k! z^k (1+H_k D/z+O(z^{-2})) and C(beta3)=8.

Selection lemma: the J-function one-point coefficient of H z^{-8} at class
beta' is exactly <psi^7 H>_{0,1,beta'}, vanishing by the dimension axiom
unless C(beta')=8. Mirror-map corrections f(y) are supported on C=1 effective
classes (z-power count: only C=1 feeds z^0); any monomial y^delta in
e^{f.beta'} has C(delta)>=0 with equality iff delta=0 by -K ampleness.
Contributing to (y^{beta3},H z^{-8}) needs beta'+delta=beta3 effectively and
C(beta')=8, forcing C(delta)=0, delta=0, beta'=beta3. The classical z+tau piece
lives in z^{>=0} and cannot reach z^{-8}. Hence mirror-map mixing drops out of
this top-power slot and [I]_{y^{beta3},H z^{-8}} = <tau_7(H)>.
Since the Poincare dual of H is H, the coefficient is -(1/4)(7/2)=-7/8.

Computation: exact rational-arithmetic scripts verify all intersection numbers,
Picard relations D1+D2=D4+D5 and D2+D3=D5+D6, duality, effectivity, factorial
product, harmonic sum, and the final -7/8. Both scripts pass.

## Limitations

Relies on the published Givental toric mirror theorem J(tau(y),z)=I(y,z) for
smooth toric Fano manifolds, the divisor equation, and standard virtual-dimension
vanishing. The accompanying scripts verify only the intersection-theoretic and
rational-arithmetic steps, not the cited mirror theorem itself.

## Reproducibility

Run output/artifacts/verify_all.py and output/artifacts/mirror_check.py with
Python 3 (exact Fraction arithmetic, no external dependencies). They assert
c1.beta3=8, k-vector (2,1,1,2,1,1), factorial product 4, S_H=7/2, effectivity,
pairing duality, Picard relations, and the invariant -7/8.

## References

- A. Givental, Equivariant Gromov-Witten invariants, IMRN 1996 (toric mirror theorem).
- T. Coates, A. Givental, Quantum Riemann-Roch, Lefschetz and Serre, 2007; H.-H. Tseng refinements.
- D. Cox, S. Katz, Mirror Symmetry and Algebraic Geometry, Ch. 8-11 (toric I-/J-functions, divisor equation).
- M. Kontsevich, Yu. Manin, Gromov-Witten classes, quantum cohomology, and enumerative geometry.
- T. Mandel, H. Ruddat, Descendant log Gromov-Witten invariants for toric varieties and tropical curves (arXiv:1612.02402).
- A. Gholampour, H.-H. Tseng, On computations of genus zero two-point descendant Gromov-Witten invariants, Michigan Math. J. 62(4).
