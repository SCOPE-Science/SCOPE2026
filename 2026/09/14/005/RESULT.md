# Empty reducible q-locus for symmetric half-exponent Heun at t=2 (Kovacic Case-1)

## Context and motivation

The Fuchsian Heun operator with four regular singularities is a central object in
special-function theory and differential Galois theory, with the accessory parameter
q controlling the global monodromy while leaving the local exponents fixed. The
symmetric half-exponent point gamma=delta=epsilon=1/2 is the algebraic Lame case,
a natural and classical parameter choice. The admitted target asks for the complete
classification, over all q in C, of those q for which the operator at cross-ratio
t=2 admits a Kovacic Case-1 Liouvillian solution, equivalently a rational solution
of the associated Riccati equation, equivalently a Picard-Vessiot group contained in
a Borel subgroup (reducibility over C(z)). This finite q-locus was unknown before
computation and is needed for any downstream use of this operator in symbolic
integration or Galois-group certification.

## Definitions

Let

H(2,q): y'' + (1/2)(1/z + 1/(z-1) + 1/(z-2)) y' + (z/16 - q)/(z(z-1)(z-2)) y = 0,

i.e. the normalized Fuchsian Heun operator with gamma=delta=epsilon=1/2,
alpha=beta=1/4, t=2 (Fuchs relation 3/2=3/2), q in C. Write p(z) for the
coefficient of y' and r(z) for the coefficient of y. A Kovacic Case-1 solution
means a hyperexponential solution y with theta=y'/y in C(z), equivalently a
rational solution u of u'+u^2+p u+r=0, equivalently a one-dimensional submodule
of the solution space over C(z).

## Result

Theorem. For every q in C, H(2,q) has no Kovacic Case-1 Liouvillian solution: its
Picard-Vessiot group is not contained in any Borel subgroup. The complete
reducible q-locus is the empty list. The exclusion holds uniformly over all of C
in one computation because the accessory parameter never enters the relevant
local data.

## Proof and evidence

Put Y=y exp((1/2) integral p), so Y''=sY with s=p'/2+p^2/4-r. Exact rational
arithmetic gives s=N(q,z)/(16 z^2 (z-1)^2 (z-2)^2) with
N(q,z)=-4z^4+15z^3-26z^2+24z-12+q(16z^3-48z^2+32z). The q-dependent part factors
as 16q z(z-1)(z-2) and hence vanishes at each finite pole, so
N(q,0)=-12, N(q,1)=-3, N(q,2)=-12: nonzero and q-independent. Thus the poles of
s at 0,1,2 are exactly of order 2 for every q; since deg numerator is 4 with
q-free leading coefficient -4 and deg denominator is 6, ord_infinity(s)=2 for
every q. The double-pole coefficients are b_0=b_1=b_2=-3/16 and b_infinity=-1/4,
all q-independent. Kovacic Step 1 gives E_c={3/4,1/4} at each finite pole and the
singleton E_infinity={1/2}. Candidate degrees d=1/2-(a_0+a_1+a_2) over the 8 sign
choices take values -1/4,-3/4,-5/4,-7/4, never a nonnegative integer, so Case 1
admits no candidate for any q. An independent hand-checkable exponent/residue
count reaches the same conclusion: any rational-submodule generator would need
theta=e_0/z+e_1/(z-1)+e_2/(z-2)+P'/P with e_c in {0,1/2}, forcing
deg P=-(sum e_c)-1/4 in the same fractional-negative set, impossible. The
certificate script output/artifacts/kovacic_case1_normalform.py re-executes this
verification with exact arithmetic and enumerates all 8 combinations.

## Limitations

The theorem classifies only Kovacic Case-1 (reducible/Borel) solutions as the
target requires. It does not rule out irreducible Liouvillian solutions of
Kovacic Cases 2 or 3 (dihedral or finite primitive groups) for special q, nor
does it address cross-ratios t other than 2 or non-symmetric exponents. The
logarithmic behavior at infinity (coincident exponents 1/4,1/4) does not affect
the degree obstruction, which already fails before any recurrence.

## Reproducibility

Run `python3 output/artifacts/kovacic_case1_normalform.py` with sympy installed.
It prints the numerator and factored denominator of s, the values N(q,c), the
double-pole data, the alpha sets, and the enumeration of all 8 candidate
degrees, ending with CERTIFICATE OK.

## References

- DLMF 31.2 (Heun equation, normal form, exponents), 31.8 (solutions via
  quadratures / finite-gap family), 31.14 (Kovacic's algorithm).
- Hounkonnou-Ronveaux, Generalized Heun and Lame equations: factorization,
  arXiv:0902.2991 (nearest factorization prior; different parameters).
- Kovacic (1986), algorithm for second-order Liouvillian solutions.
