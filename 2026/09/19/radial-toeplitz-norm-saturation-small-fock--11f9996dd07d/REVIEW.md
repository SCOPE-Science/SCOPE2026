# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The radial eigenvalue formula follows directly from polar coordinates and the
homogeneous decomposition. The proof was checked in three
mathematical pieces.

First, for
\[
F_M(u)=Mu-u^{3/2},\qquad M=2m+2n,
\]
the maximizer is \(u_M=4M^2/9\), and direct substitution gives
\[
F_M\!\left(\frac49(M-1)^2\right)-F_M(u_M)
=-\frac4{27}(3M-2),
\]
\[
F_M\!\left(\frac49(M+1)^2\right)-F_M(u_M)
=-\frac4{27}(3M+2).
\]
The derivative at the upper endpoint is exactly \(-1\). These identities make
the normalized moment mass outside the designated shell exponentially small.
The shell construction therefore works for every bounded target sequence,
not only for the alternating target used in the source paper.

Second, the \(c_0\) step was checked for uniform rather than coordinatewise
convergence. Orthogonality of the degree-\(N\) Jacobi polynomial forces the
first \(N\) moments to vanish, normalization makes the \(N\)-th eigenvalue
exactly one, and
\[
A_{m,n}\ge [2(m+n)]^{-1}
\]
converts the remaining moments into the uniform estimate
\[
\sup_{m>N}|\lambda_{a_{N,\delta}}(m)|
\le C_{N,n}\delta^2.
\]
Thus coordinate vectors genuinely belong to the operator-norm closure.

Third, the representation-theoretic conclusion uses the multiplicity-free
decomposition
\[
\mathcal A_h(\mathbb C^n)=\bigoplus_{m\ge0}P^m(\mathbb C^n).
\]
The \(\mathrm U(n)\)-commutant is therefore exactly the scalar block-diagonal
algebra \(\ell^\infty\), and the diagonal compact operators correspond exactly
to \(c_0\). No complementability, compactness inheritance, or hidden
infinite-dimensional block assertion is used.

Potential overclaims were removed: the record does not assert that the
single-symbol eigenvalue map is onto \(\ell^\infty\), only that its norm closure
is all of \(\ell^\infty\).

## Originality

**PASS, to the best of our knowledge.**

The closest source is Bdarneh, arXiv:2609.20652v1, submitted 17 September
2026. Its Section 9 treats the same logarithmic weight in one dimension and
constructs one shell symbol with eigenvalues asymptotic to \((-1)^m\). Its
stated conclusion is failure of the square-root-metric description. The paper
does not state arbitrary bounded asymptotic interpolation, \(c_0\) recovery,
norm density in the full diagonal algebra, the \(\ell^\infty/c_0\) quotient,
or the extension to every complex dimension.

Esmeral--Maximenko (2016) identifies the classical Gaussian radial Toeplitz
algebra with the proper square-root-uniformly-continuous sequence algebra.
García--Maximenko (2025), arXiv:2503.23276, constructively approximates
convergent sequences in the classical Gaussian Fock space. Bauer--Herrera
Yáñez--Vasilevski characterize the standard weighted Bergman radial algebra by
slowly oscillating sequences. These are relevant prior mechanisms but do not
cover the present small-Fock norm saturation.

Searches were made using the exact source identifier and title, the exact
logarithmic weight, "small Fock" with radial Toeplitz terminology, eigenvalue
sequence interpolation, "all bounded sequences", "all diagonal operators",
\(\ell^\infty\), and radial Toeplitz \(C^*\)-algebras. No equivalent theorem was
found.

Residual risk: older or non-indexed work on radial Toeplitz algebras for
general moment spaces could contain a general asymptotic-disjointness criterion
that implies this example. The accessible highly relevant sources above were
inspected at the theorem/abstract level or in full text where available; no
concrete evidence of such coverage was found.

## Value

**PASS.**

The result changes the operator-algebra description from a single obstruction
to an exact algebra identification. For the same weight used to show one
non-square-root-uniformly-continuous sequence, the radial Toeplitz algebra is
in fact as large as it can be under \(\mathrm U(n)\)-symmetry:
\[
\mathcal T_{\rm rad}=\operatorname{End}_{\mathrm U(n)}\cong\ell^\infty.
\]
It also gives an explicit reusable mechanism: asymptotically disjoint saddle
shells provide interpolation modulo \(c_0\), and localized orthogonal-polynomial
probes provide norm control of the compact diagonal ideal. The result sharply
contrasts with classical Gaussian Fock and standard weighted Bergman radial
algebras.

## Limitations

The theorem is not a classification of radial weights. The local Jacobi
construction uses that the displayed weight is flat on a neighborhood of the
origin, and the shell argument uses the strong separation of consecutive
Laplace saddles. No assertion is made for arbitrary small-Fock weights,
quasi-radial symbol algebras, or the surjectivity of the single-symbol
eigenvalue map.

Originality is reported only to the best of our knowledge.
