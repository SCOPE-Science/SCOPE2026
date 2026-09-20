# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked at the level of both the moment transform and the resulting
operator algebra.

For fixed \(n\), the normalized radial eigenvalue kernels
\[
k_m(r)=A_m^{-1}r^{2m+2n-1}e^{-2h(r)}
\]
are probability densities. With logarithmic boundaries centered around the unique Laplace
peak of
\[
F_m(u)=(2m+2n)u-u^{3/2},
\]
their mass outside the associated annulus tends to zero exponentially. The endpoint
differences were recomputed explicitly:
\[
-\frac4{27}(3\alpha_m-2),\qquad
-\frac4{27}(3\alpha_m+2),
\quad \alpha_m=2m+2n.
\]
This verifies that Bdarneh's one-dimensional concentration estimate extends to every fixed
dimension \(n\).

For the step-symbol embedding \(S\), the operator
\(T=\Lambda_nS\) satisfies \(T-I=K\) with
\[
\sup_{\|a\|_\infty\le1}|(Ka)_m|\le2\delta_m\to0.
\]
Coordinate truncations therefore approximate \(K\) in operator norm, so \(K\) is compact.
Atkinson's theorem gives closed finite-codimensional range for \(T\). Because
\(\operatorname{ran}T\subseteq\operatorname{ran}\Lambda_n\), the latter range is also closed
and finite-codimensional.

The preadjoint
\[
J:\ell^1\to L^1,\qquad Jc=\sum c_mk_m,
\]
was checked to satisfy \(J^*=\Lambda_n\). Injectivity follows from the entire function
\[
g(z)=\sum c_mA_m^{-1}z^m.
\]
The lower bound \(A_m\ge C_RR^{2m}\) on any fixed interval \([R,R+1]\), with
\(R>\sqrt{|z|}\), gives local uniform convergence of the series. If \(Jc=0\), then
\(g(r^2)=0\) almost everywhere on the positive axis, hence \(g\equiv0\) and \(c=0\).

Since \(\operatorname{ran}J^*\) is closed, the closed range theorem gives closed
\(\operatorname{ran}J\). Injectivity then makes \(J\) bounded below. Hahn--Banach applied to
the functional \(Jc\mapsto\sum b_mc_m\) produces a bounded symbol for every
\(b\in\ell^\infty\), proving surjectivity. The bounded linear right inverse is obtained by
splitting the finite-dimensional kernel/cokernel of the Fredholm map
\(\Lambda_nS\); all required complements are bounded because the exceptional spaces are
finite dimensional.

Bdarneh's homogeneous decomposition identifies the \(U(n)\)-commutant with
\(\ell^\infty\), so surjectivity of the radial eigenvalue map is exactly the claimed
single-Toeplitz realization of every intertwiner. No complementability claim relies on an
unconditional-basis argument.

## Originality

The complete arXiv:2609.20652v1 text was inspected. Its Section 6 gives the radial
eigenvalue formula and identifies the \(U(n)\)-commutant with \(\ell^\infty\); Section 7
proves strong-operator density of invariant Toeplitz operators for general radial weights.
Section 9 treats the logarithmic weight only in dimension one and constructs one bounded
step symbol whose eigenvalues approach \((-1)^m\). It concludes only that the square-root
metric description from the classical Fock space fails.

Searches were made using combinations and synonymous formulations involving bounded radial
symbols, arbitrary bounded eigenvalue sequences, surjective radial moment maps, all
diagonal/intertwining operators, logarithmic and small Fock weights, and
\(\ell^\infty\)-valued spectral transforms. No source was found stating bounded-symbol
surjectivity, a bounded linear lifting, or equality of the bounded-radial Toeplitz set with
the full \(U(n)\)-commutant for this weight.

A particularly important prior result was checked directly: Grudsky--Vasilevski (2002),
Theorem 3.7, prescribes an arbitrary bounded eigenvalue sequence in the classical Fock
space, but uses the larger weighted-integrability symbol class
\(L^\infty_1(\mathbb R_+,e^{-r^2})\), with symbols unbounded in general. This does not imply
surjectivity for bounded symbols; indeed the later Esmeral--Maximenko theorem shows that
bounded radial symbols in the classical Gaussian Fock space have the much smaller
square-root-uniformly-continuous norm closure.

The novelty claim therefore excludes the general moment formula, strong-operator density,
Laplace concentration estimates, Atkinson's theorem, the Banach closed range theorem, and
Hahn--Banach. The claimed contribution is their combination into exact bounded-symbol
surjectivity (in every dimension), the split quotient statement, and the resulting equality
with the full \(U(n)\)-commutant for Bdarneh's logarithmic weight.

No specific inaccessible paper was identified as a likely exact antecedent. The main
residual risk is older Toeplitz moment-problem literature using a different symbol-space
language, or small-Fock-space literature not indexed with Toeplitz terminology. The
Grudsky--Vasilevski result and the recent Bdarneh preprint were available in sufficient
detail to resolve the most obvious coverage risks.

## Value

The recent paper demonstrates that one classical metric description fails by constructing a
single oscillatory sequence. The present theorem shows that the failure is maximal:
bounded radial symbols realize every bounded spectral sequence. It also upgrades a
strong-operator-density statement to exact single-symbol representation and gives a bounded
linear symbol-selection map. The conclusion is structurally sharp for the stated weight and
directly identifies the invariant Toeplitz operator set with the entire commutant.

## Scope and limitations

No claim is made for arbitrary radial weights, for quasi-radial multi-parameter symbols, or
for optimal symbol norms. Representing bounded radial symbols need not be unique. For
\(n>1\), the \(U(n)\)-commutant is block scalar rather than a masa; the masa statement is
only for \(n=1\).

Originality is to the best of our knowledge.
