# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The argument was checked at the level of the stated formulas.

Bdarneh's Theorem 6.2 gives the degree-\(m\) radial eigenvalue as a normalized
moment with density \(r^{2m+2n-1}e^{-2h(r)}\). For the logarithmic weight and
the substitution \(u=\log r\), the exponent is
\(F_m(u)=a_mu-u^{3/2}\), \(a_m=2m+2n\), with unique maximum at
\(4a_m^2/9\). The proposed annular boundaries correspond to \(a_m-1\) and
\(a_m+1\). Direct substitution gives exponent losses
\(-4(3a_m-2)/27\) and \(-4(3a_m+2)/27\), so the normalized mass outside the
target annulus tends to zero. This estimate is uniform with respect to the
chosen bounded annular values after multiplication by \(\|c\|_\infty\).

The compactness step is exact: the homogeneous spaces \(P^m(\mathbb C^n)\)
are finite dimensional, so a block-scalar diagonal operator
\(\bigoplus d_m I_{P^m}\) is compact exactly when \(d_m\to0\). Therefore the
asymptotic eigenvalue interpolation is precisely interpolation modulo the
compact ideal, and it yields every class of \(\ell^\infty/c_0\).

The projection and essential-spectrum consequences follow from the standard
diagonal model. The classical-Gaussian comparison was checked separately:
an idempotent modulo \(c_0\) in the square-root-uniform algebra must be
asymptotically \(\{0,1\}\)-valued, while uniform continuity and
\(\rho(m,m+1)\to0\) prohibit infinitely many switches between the two branches.

No numerical computation is needed for the proof.

## Originality

Verdict: PASS, to the best of our knowledge.

The most relevant primary source inspected is Bdarneh,
arXiv:2609.20652v1. Its Section 9 constructs a single alternating annular
symbol in one complex dimension and concludes that the square-root-metric
description fails. The paper states neither arbitrary bounded-sequence
interpolation modulo \(c_0\), nor the full Calkin image
\(\ell^\infty/c_0\), nor the Stone--Cech corona conclusion. Its general
Theorem 6.2 supplies the higher-dimensional moment formula used here.

The classical Gaussian characterization of Esmeral--Maximenko and its
higher-dimensional quasi-radial extension by Dewage--Olafsson were checked
through their published descriptions and the way they are quoted in Bdarneh.
They characterize the Gaussian radial algebra by square-root uniform
continuity, rather than the logarithmic-weight quotient obtained here.

Literature searches using combinations of "radial Toeplitz", "weighted Fock"
or "small Fock" with "Calkin", "corona", "ell infinity / c0", "Stone-Cech",
and "every bounded sequence" did not locate a prior equivalent theorem.

Residual risk remains from older radial Toeplitz and small-Fock literature
whose full texts were not exhaustively inspected. In particular, the complete
text of Esmeral--Maximenko (2016) was not used to rule out every possible
corona reformulation, although its advertised theorem concerns the classical
Gaussian weight. The small-Fock papers cited by Bdarneh concern reproducing
kernels rather than this Toeplitz-algebra quotient, making direct coverage less
likely but not impossible.

## Value

Verdict: PASS.

The result identifies a complete operator-algebraic boundary hidden behind a
single counterexample in the source paper: for this slow logarithmic weight,
the radial Toeplitz algebra is maximal modulo compacts among all
\(U(n)\)-intertwiners. The conclusion supplies all diagonal Calkin projections
and arbitrary compact essential spectra, and it exposes a qualitative change
from the classical Gaussian radial corona, which has no nontrivial
projections.

## Limitations

The result is tied to the displayed logarithmic weight and bounded radial
symbols. It is a quotient statement, not an operator-norm equality of the
radial Toeplitz algebra with the full diagonal intertwiner algebra. It does not
classify which other weights have the same saturation property.
