# Surjectivity, not invertibility, is the exact image criterion in a tensor controlled-frame theorem

## Finding
Theorem 4.9 of Ghosh--Samanta, first posted as arXiv:2109.00543v1 and retained as Theorem 13 in the journal version, states that the image of the tensor controlled frame under \(W=U_1\otimes U_2\) is a controlled frame if and only if \(W\) is invertible. The necessity is too strong. Under the theorem's existing commutation assumptions, the exact operator criterion is surjectivity of \(W\).

If \(S\) denotes the original tensor controlled-frame operator and
\[
\alpha I\le S\le\beta I,
\]
then the transformed controlled-frame operator is
\[
S_W=WSW^*.
\]
Consequently the transformed family is a controlled frame exactly when \(W\) is surjective. In that case,
\[
\alpha m(W^*)^2 I\le S_W\le\beta\|W\|^2 I,
\]
where
\[
m(W^*)=\inf_{\|x\|=1}\|W^*x\|>0.
\]

## Assumptions and scope
The claim uses the hypotheses already imposed in the cited theorem: the two original families are controlled frames in the associated Hilbert spaces, the controls commute with \(U_1\) and \(U_2\), and the transformed controlled-frame operator is therefore \(WSW^*\). No assertion is made after removing those commutation hypotheses.

For an explicit counterexample, use the standard Hilbert-induced \(2\)-inner-product model on an ambient Hilbert space with anchor \(e_0\). Its associated Hilbert space is \(e_0^\perp\), identified with \(\ell^2(\mathbb N)\). Put \(C_1=I\), and define
\[
f_1=\frac{e_1+e_2}{\sqrt2},\qquad
f_2=\frac{e_1-e_2}{\sqrt2},\qquad
f_i=e_i\quad(i\ge3).
\]
This is an orthonormal basis of the associated Hilbert space. For the second factor use the same standard \(2\)-inner-product model with associated Hilbert space \(K_G\cong\ell^2(\mathbb N)\), let \((g_j)_{j\ge1}\) be its orthonormal basis, and put \(C_2=I\).

Let \(U_1=L\) be the backward shift
\[
Le_1=0,\qquad Le_{m+1}=e_m\quad(m\ge1),
\]
and let \(U_2=I\). Then \(W=L\otimes I\) is bounded and surjective but has nonzero kernel, so it is not invertible.

## Proof
For the counterexample,
\[
Lf_1=\frac{e_1}{\sqrt2},\qquad
Lf_2=-\frac{e_1}{\sqrt2},\qquad
Lf_i=e_{i-1}\quad(i\ge3).
\]
Hence, for every \(x=\sum_{m\ge1}x_me_m\),
\[
\sum_{i\ge1}|\langle x,Lf_i\rangle|^2
=
\frac12|x_1|^2+\frac12|x_1|^2+\sum_{m\ge2}|x_m|^2
=
\|x\|^2.
\]
Tensoring this Parseval family with the orthonormal basis \((g_j)_{j\ge1}\) gives a Parseval tensor family, while \(W\) remains noninjective. This disproves the published necessity of invertibility without using zero frame atoms.

For the exact repair, suppose first that \(W\) is surjective. For bounded operators between Hilbert spaces, surjectivity of \(W\) is equivalent to \(W^*\) being bounded below, so \(m(W^*)>0\). Thus
\[
\langle WSW^*x,x\rangle
=
\langle SW^*x,W^*x\rangle
\ge
\alpha\|W^*x\|^2
\ge
\alpha m(W^*)^2\|x\|^2.
\]
Also,
\[
\langle WSW^*x,x\rangle
\le
\beta\|W^*x\|^2
\le
\beta\|W\|^2\|x\|^2.
\]
Therefore \(WSW^*\) is a positive invertible controlled-frame operator with the displayed bounds.

Conversely, if the transformed family is a controlled frame, then \(WSW^*\) is onto. Since
\[
R(WSW^*)\subseteq R(W),
\]
we get \(R(W)\) equal to the whole target Hilbert space. Thus \(W\) is surjective. There is no implication that \(\ker W=\{0\}\), and the backward-shift example shows that injectivity can fail.

## Verification
The source statement and converse proof were reconstructed from the full arXiv text. The proof explicitly identifies the transformed frame operator as \(WSW^*\) and then infers invertibility of \(W\) from invertibility of \(WSW^*\) and \(S\). The same implication appears in the published 2024 theorem. The counterexample is symbolic: the original and transformed frame sums are computed exactly, \(L\) is explicitly surjective, and \(\ker L=\operatorname{span}\{e_1\}\).

The corrected criterion uses only standard Hilbert-space operator facts: \(W\) is surjective exactly when \(W^*\) is bounded below, and an onto positive operator \(WSW^*\) has range contained in \(R(W)\). No finite experiment is used as evidence for an infinite-dimensional assertion.

## Relationship to prior work
The general fact that a bounded operator sends an ordinary frame to a frame when it is surjective is standard frame/operator theory and is not claimed here as a new general principle. The source-specific point is that Theorem 4.9, and its published Theorem 13, assert the stronger necessity of invertibility even though their own frame-operator identity only forces surjectivity. The explicit noninjective Parseval counterexample shows that this is a genuine failure of the theorem, not merely a nonoptimal proof.

A later paper on weaving \(K\)-frames in \(n\)-Hilbert spaces uses surjective operators in a different weaving construction. That literature is consistent with surjectivity being the natural range condition, but it does not state this correction to the Ghosh--Samanta tensor controlled-frame theorem.

## Limitations
The correction is confined to the theorem under its stated commutation and controlled-frame hypotheses. It does not classify image families when those assumptions are removed. The originality claim is likewise source-specific: it concerns the falsification and exact repair of the cited theorem, not the general Hilbert-space equivalence between surjectivity and bounded-below adjoint.

A residual literature risk remains that an unindexed erratum, thesis remark, or informal author note may have observed the same source-specific defect.

## References
1. P. Ghosh and T. K. Samanta, *Controlled frames in n-Hilbert spaces and their tensor products*, arXiv:2109.00543v1, 1 September 2021, Theorem 4.9.
2. P. Ghosh and T. K. Samanta, journal version of the same work, DOI 10.26907/0021-3446-2024-5-8-29, Theorem 13.
3. G. Wang, *Some properties of weaving \(K\)-frames in \(n\)-Hilbert space*, AIMS Mathematics 9 (2024), 25438--25456, DOI 10.3934/math.20241242.
