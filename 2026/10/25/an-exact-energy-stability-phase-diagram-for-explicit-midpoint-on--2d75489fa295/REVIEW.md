# Independent mathematical audit

## correctness

PASS

In dimensionless variables R has diagonal entries 1−x+(1−t)x²/2 and 1−tx²/2, and skew off-diagonals ±√t x(1−x/2). The polynomial replay verifies the pivotal entries and determinant of Q=I−RᵀR. For x>0 the diagonal bound requires x≤4/(1+t). For t<1 the increasing cubic's root is strictly below that bound and the bound is strictly below 2/t, so the determinant changes sign only once in the relevant interval. For t>1 one has 2/t<4/(1+t)<ξ(t), with the first zero now at 2/t. At t=1 both coincide and R=−I at x=2. Thus Q is positive definite at all strictly interior positive steps, and the boundary with t≠1 has a positive second diagonal and determinant zero, hence one singular value equal to one but not two. At x=0 R=I. Writing g=x[(tx−1)²+3]−8 immediately bounds the root by 8/3 with equality only at t=3/8; the reciprocal branch cannot reach this value. For spectral stability the eigenvalues of L/a solve λ²+λ+t=0. On the real branch the larger-magnitude negative eigenvalue must satisfy xλ≥−2, including the repeated eigenvalue at t=1/4. On the complex branch the squared scalar-amplifier defect is x/4 times the stated increasing cubic. On the real branch g_t(S)>0 for t>0; on the complex branch the spectral cubic evaluated at E gives 4−2E<0 for 1/4<t<1 and 4(1/t−1)<0 for t>1. Equality occurs at t=1. Rescaling the spectral cubic by x=c t^(−2/3) gives a cubic converging on bounded c to c³−4, whose positive root is bracketed by continuity and monotonicity. This gives the claimed constant and exponent of the ratio. No eigenvalue argument here asserts monotone energy along arbitrary repeated steps outside E.

## originality

PASS

The combined energy-versus-spectral phase diagram is distinct on the evidence inspected: in particular the exact spectral frontier relative to E for all t and its asymptotically unbounded gap were not covered by the strongest matching statements. Do not credit the energy frontier, unique optimum or −I resonance as distinct from indexed record c4ff16d39c20: they are exact overlaps. The index dates do not resolve provenance or priority. The frozen result already includes the all-ratio comparison, so this decision does not add a replacement claim.

## value

PASS

This canonical damped oscillator isolates the difference between one-step physical-norm contraction and the scalar absolute-stability test for a standard integrator. The exact two thresholds let a researcher distinguish these requirements for any coupling; the asymptotic shows that choosing the spectral step can miss the one-step condition by an arbitrarily large factor, not merely at a hand-picked instance. The scientific value is the sharp quantitative comparison, not reusing the known scalar stability polynomial or reporting a single optimal norm computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
