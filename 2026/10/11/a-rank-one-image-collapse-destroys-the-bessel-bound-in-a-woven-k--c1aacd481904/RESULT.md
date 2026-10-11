# A rank-one image collapse destroys the Bessel bound in a woven \(K\)-fusion construction

## Finding
Proposition 2.5 of Bhandari--Mukherjee asserts that applying any bounded operator \(K\) to the subspaces of two weaving fusion frames produces two weaving \(K\)-fusion frames. The assertion is false even for a rank-one operator with closed range and closed image subspaces.

Let
\[
H=\ell^2(\mathbb N)
\]
with orthonormal basis \((e_i)_{i\ge1}\), and define
\[
W_i=V_i=\operatorname{span}\{e_i\},\qquad
w_i=v_i=1.
\]
Because the two families are identical orthogonal decompositions, every weave is the same Parseval fusion frame:
\[
\sum_{i\in\sigma}\|P_{W_i}f\|^2+
\sum_{i\in\sigma^c}\|P_{V_i}f\|^2
=
\|f\|^2
\]
for every \(\sigma\subseteq\mathbb N\) and \(f\in H\).

Now define
\[
K(x_1,x_2,\ldots)
=
\left(\sum_{i=1}^{\infty}2^{-i}x_i\right)e_1.
\]
This is a bounded rank-one operator. For every \(i\),
\[
K e_i=2^{-i}e_1\ne0,
\]
and therefore
\[
K W_i=K V_i=\operatorname{span}\{e_1\}.
\]
All image subspaces are closed.

For \(f=e_1\), however,
\[
\sum_{i=1}^{\infty}\|P_{K W_i}f\|^2
=
\sum_{i=1}^{\infty}1
=
\infty.
\]
Thus the image family is not even \(K\)-fusion Bessel. The same holds for the second image family, so the claimed weaving \(K\)-fusion-frame conclusion fails.

## Assumptions and scope
The counterexample uses the source's countable-index setting and its definition of a \(K\)-fusion frame as a weighted collection of closed subspaces satisfying both lower and upper inequalities.

The operator \(K\) has closed range:
\[
R(K)=\operatorname{span}\{e_1\}.
\]
Hence the failure is not caused by nonclosed operator range or by nonclosed image subspaces.

The example isolates the upper-Bessel defect. The source's lower-bound computation is compatible with the example; the failure is that the image collection need not have any finite upper bound.

## Proof
The coefficient sequence
\[
a=(2^{-1},2^{-2},\ldots)
\]
belongs to \(\ell^2(\mathbb N)\), with
\[
\|a\|^2=\sum_{i=1}^{\infty}4^{-i}=\frac13.
\]
Therefore
\[
\left|\sum_{i=1}^{\infty}2^{-i}x_i\right|
\le
\frac1{\sqrt3}\|x\|,
\]
so \(K\) is bounded.

Each original subspace is one-dimensional and mutually orthogonal to all the others. Since \(W_i=V_i\), every partition simply chooses the same subspace at each index. Hence the original pair is woven with exact universal bounds \(1\) and \(1\).

For every \(i\),
\[
K(W_i)
=
\operatorname{span}\{K e_i\}
=
\operatorname{span}\{e_1\}.
\]
Consequently, every image projection equals \(P_{\operatorname{span}\{e_1\}}\). At \(f=e_1\),
\[
\sum_i\|P_{K W_i}e_1\|^2
=
\sum_i1,
\]
which diverges. This contradicts the upper Bessel inequality required of every \(K\)-fusion frame.

The source proof invokes its Proposition 1.5 to obtain the universal upper bound. Proposition 1.5 applies only when the two input families are already \(K\)-fusion Bessel sequences. The construction above proves that this premise does not follow from the hypotheses of Proposition 2.5.

For a repaired statement, suppose \(K\ne0\), all image subspaces are closed, and the two image collections have \(K\)-fusion Bessel bounds \(C_W\) and \(C_V\). Let \(A\) be a universal lower bound for the original weaving fusion frames. The projection identity used by the source gives, for every weave and \(f\in H\),
\[
A\|K^*f\|^2
\le
\|K\|^2
\left(
\sum_{i\in\sigma}w_i^2\|P_{K W_i}f\|^2+
\sum_{i\in\sigma^c}v_i^2\|P_{K V_i}f\|^2
\right).
\]
Thus the image weave has lower \(K\)-fusion bound
\[
\frac{A}{\|K\|^2}.
\]
Proposition 1.5 then gives the universal upper bound
\[
C_W+C_V.
\]
This proves the repaired sufficient statement.

## Verification
The public preprint was inspected at Definition 1.1, Definition 1.4, Proposition 1.5, Lemma 1.7, and the complete statement and proof of Proposition 2.5.

Proposition 1.5 explicitly assumes that both families entering a weave are already \(K\)-fusion Bessel sequences. Proposition 2.5 proves only the lower image estimate and then cites Proposition 1.5 for the upper bound without establishing that prerequisite.

The counterexample is exact. Its only infinite calculation is the elementary geometric-series test showing that \(K\) is bounded; the divergence of the transformed fusion energy at \(e_1\) is immediate.

## Relationship to prior work
A 2025 paper on woven \(g\)-frames under operators gives counterexamples to operator preservation of \(g\)-frame wovenness and shows that injectivity is essential in that different setting. That result does not cover the present fusion-frame failure: applying the rank-one operator to the vectors \(e_i\) retains the amplitudes \(2^{-i}\) and produces a Bessel vector sequence, whereas passing to the image subspaces \(K W_i\) discards those amplitudes and leaves infinitely many copies of the same line.

The source itself treats the upper-Bessel issue correctly in Proposition 1.5 and, in Lemma 2.1, imposes extra hypotheses when constructing image \(K\)-fusion frames. The failure in Proposition 2.5 is therefore specific to dropping all image-Bessel control while claiming preservation for every bounded \(K\).

A separate 2020 paper on weaving \(K\)-fusion frames was checked at the article metadata, abstract, classification, and indexed references. Its accessible indexed material does not state the present image-collapse counterexample; theorem-level noncoverage was not inferred from the abstract alone.

## Limitations
The finding refutes Proposition 2.5 as stated and supplies a sufficient repair by adding closed-image and image-Bessel hypotheses.

It does not claim that those hypotheses are necessary in their stated form, nor does it classify all bounded operators that preserve woven fusion frames after passing to image subspaces.

An unindexed erratum, thesis remark, or later theorem may contain the same image-multiplicity observation.

## References
1. A. Bhandari and S. Mukherjee, *On wovenness of \(K\)-fusion frames*, arXiv:1912.07530v1, 13 December 2019; later published in Springer Proceedings in Mathematics and Statistics 384 (2022), 93--101, DOI 10.1007/978-3-030-96401-6_8.
2. Z.-Q. Xiang and C.-X. Lin, *A New View on the Wovenness of \(g\)-Frames Under Operators*, Journal of Mathematics (2025), Article 7185421, DOI 10.1155/jom/7185421.
3. H. Liu, Y. Huang and C. Li, *Weaving \(K\)-fusion frames in Hilbert spaces*, Mathematical Foundations of Computing 3 (2020), 101--116, DOI 10.3934/mfc.2020008.
