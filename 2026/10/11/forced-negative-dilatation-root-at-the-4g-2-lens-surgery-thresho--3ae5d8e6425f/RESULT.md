# Forced negative dilatation root at the \(4g-2\) lens-surgery threshold
## Finding
Let \(K\subset S^3\) be a hyperbolic knot of genus \(g\) admitting a lens-space surgery with slope \(\pm(4g-2)\). Let \(\lambda>1\) denote the pseudo-Anosov dilatation of the fiber monodromy. Then
\[
\Delta_K(-\lambda)=0.
\]
Equivalently, the homological monodromy has eigenvalue \(-\lambda\). Since the normalized Alexander polynomial is reciprocal, \(-\lambda^{-1}\) is also a root. Hence the real root outside the unit circle in the spectral obstruction at this slope is not merely of unspecified sign: it is necessarily negative.

## Assumptions and scope
The Alexander polynomial is the symmetrized normalization with \(\Delta_K(1)=1\). For a negative lens-space surgery, replace \(K\) by its mirror. Mirroring preserves the Alexander polynomial, genus, and hyperbolicity; it changes the sign of the surgery and replaces the fiber monodromy by the inverse up to orientation conjugacy, so the pseudo-Anosov dilatation is unchanged.

The argument uses two inputs. First, Guo proves that at slope \(\pm(4g-2)\) the capped invariant foliations are orientable and that the homological monodromy has an eigenvalue \(\rho=\pm\lambda\), hence \(\Delta_K(\rho)=0\). Second, the Alexander polynomial of a knot admitting an L-space surgery has the alternating staircase form of Ozsváth--Szabó, recorded explicitly by Krcatovich.

No assertion is made for other surgery slopes or for arbitrary fibered hyperbolic knots.

## Proof
After mirroring if needed, assume the lens-space surgery has positive slope \(4g-2\). Such a knot is an L-space knot. Write the positive Alexander exponents in its staircase form as
\[
0<n_1<n_2<\cdots<n_m=g.
\]
Then
\[
\Delta_K(t)=(-1)^m+\sum_{j=1}^m(-1)^{m-j}\bigl(t^{n_j}+t^{-n_j}\bigr).
\]
Fix \(t>1\) and put
\[
F_j(t)=t^{n_j}+t^{-n_j}.
\]
Because \(n\mapsto t^n+t^{-n}\) is strictly increasing for positive integers \(n\),
\[
F_1(t)<F_2(t)<\cdots<F_m(t).
\]
If \(m\) is even, pair consecutive terms to obtain
\[
\Delta_K(t)=1+\bigl(F_2-F_1\bigr)+\bigl(F_4-F_3\bigr)+\cdots+\bigl(F_m-F_{m-1}\bigr)>0.
\]
If \(m\) is odd, then
\[
\Delta_K(t)=\bigl(F_1-1\bigr)+\bigl(F_3-F_2\bigr)+\cdots+\bigl(F_m-F_{m-1}\bigr)>0,
\]
because \(F_1(t)>2\). Therefore an L-space-knot Alexander polynomial has no positive real zero greater than \(1\).

Guo's proof of the \(4g-2\) spectral obstruction gives a real eigenvalue
\[
\rho=\pm\lambda,
\qquad \lambda>1,
\]
of the homological monodromy and proves \(\Delta_K(\rho)=0\). The positivity just proved excludes \(\rho=+\lambda\). Hence
\[
\rho=-\lambda
\]
and therefore \(\Delta_K(-\lambda)=0\).

Finally, the symmetrized Alexander polynomial satisfies \(\Delta_K(t)=\Delta_K(t^{-1})\), so \(-\lambda^{-1}\) is a root as well. Mirroring back, if it was used, leaves the Alexander polynomial and dilatation unchanged, so the statement holds for either surgery sign.

## Verification
The recent source was inspected at its statement of the spectral obstruction, its primary MSC classification, the homological-monodromy formula, the orientability criterion, and the complete proof of the obstruction. In particular, the proof explicitly stops at an eigenvalue \(\rho=\pm\lambda\) before passing to \(\Delta_K(\rho)=0\).

Krcatovich's full text was inspected at Corollary 1.2 and Remark 1.3, which record the alternating Alexander-polynomial staircase for knots admitting L-space surgeries and its mirror-invariant extension. The sign argument above is symbolic: it pairs successive values of the strictly increasing function \(t^n+t^{-n}\) for \(t>1\), so no finite experiment is being used as an infinite proof.

The two parity cases were also checked algebraically by direct expansion of the displayed paired sums. No numerical approximation to \(\lambda\) is required.

## Relationship to prior work
Guo's Theorem 1.2 states that a hyperbolic genus-\(g\) knot with lens-space surgery slope \(\pm(4g-2)\) has a real Alexander root \(\rho\) with \(|\rho|>1\). In the proof, orientability of the capped pseudo-Anosov foliations gives only \(\rho=\pm\lambda\); the sign is not resolved there.

Ozsváth--Szabó's L-space surgery theorem, in the form recorded by Krcatovich, supplies the alternating staircase shape of the Alexander polynomial but does not supply the existence of a root of modulus greater than one. Combining the two facts forces the previously ambiguous root to be \(-\lambda\), and reciprocity gives \(-\lambda^{-1}\).

Targeted searches for the exact negative-root formulation, the equivalent \(-\lambda\) homological-eigenvalue formulation, and broader L-space/pseudo-Anosov variants did not locate a published statement subsuming this sign refinement. The closest located work concerns other Alexander-polynomial obstructions for L-space knots or unrelated monodromy phenomena.

## Limitations
The result does not determine \(\lambda\) numerically, prove that the two negative roots are simple, or classify any additional real or complex roots of \(\Delta_K\). It does not claim that every L-space knot has a real root outside the unit circle; the existence of such a root here comes specifically from the \(\pm(4g-2)\) lens-surgery argument.

The conclusion is a sign refinement of a recent spectral obstruction, not a classification of all lens-space surgeries. An unindexed note or a later revision of the recent source could conceivably record the same short consequence.

## References
1. Q. Guo, *Lens Space Surgeries and the Bleiler--Litherland Conjecture*, arXiv:2609.31757v1, first posted 2026-09-26; current text v2, 2026-09-30.
2. D. Krcatovich, *A restriction on the Alexander polynomials of L-space knots*, arXiv:1408.3886v1, 2014; Pacific J. Math. 297 (2018), 117--138.
3. P. Ozsváth and Z. Szabó, *On knot Floer homology and lens space surgeries*, arXiv:math/0303017v1, 2003; Topology 44 (2005), 1281--1300.
