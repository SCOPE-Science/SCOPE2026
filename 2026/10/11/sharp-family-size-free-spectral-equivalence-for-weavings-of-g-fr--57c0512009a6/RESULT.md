# Sharp, family-size-free spectral equivalence for weavings of \(g\)-frames

## Finding
Under the all-subsets, pairwise relative perturbation condition of Li--Leng--Huang--Li's \(g\)-frame weaving theorem, **each weaving frame operator is uniformly comparable in positive-operator order to every constituent frame operator**. The optimal comparison constant is
\[
c_K=(1+\sqrt K)^2,
\]
independently of the number of constituent frames.

Precisely, if \(S_j\) is the frame operator of the \(j\)-th original \(g\)-frame, and \(S_\sigma\) is the operator of a weaving selected by any partition, then
\[
\boxed{\quad c_K^{-1}S_j\preceq S_\sigma\preceq c_K S_j\quad}
\]
for every \(j\) and every partition. Here \(\preceq\) is the usual order on bounded self-adjoint operators.

This yields the simultaneous, number-of-frames-independent bounds
\[
\boxed{\quad
\frac{\max_j A_j}{(1+\sqrt K)^2}\,\|f\|^2
\le \langle S_\sigma f,f\rangle
\le (1+\sqrt K)^2\min_j B_j\,\|f\|^2.
\quad}
\]
The factor \(c_K\) is the smallest possible for all allowed systems, even in the scalar one-index case. The resulting comparison also controls conditioning:
\[
\kappa(S_\sigma)\le c_K^2\kappa(S_j).
\]
These formulas refine the quantitative information supplied by the published \(g\)-frame weaving criterion, whose lower constant depends on the number of frames and whose generic upper bound sums all constituent Bessel bounds.

## Assumptions and scope
Let \(H\) be a real or complex Hilbert space and \(m\ge2\) be finite. Let \(I\) be a finite or countable index set. For each \(i\in I\), let \(K_i\) be a Hilbert space, **the same for all \(m\) columns**, and let
\[
\Lambda_{ij}:H\longrightarrow K_i
\]
be bounded, for \(1\le j\le m\). Each column \(\Lambda_j=(\Lambda_{ij})_{i\in I}\) is a \(g\)-frame, so it has frame bounds \(0<A_j\le B_j<\infty\) satisfying
\[
A_j\|f\|^2\le\sum_{i\in I}\|\Lambda_{ij}f\|^2\le B_j\|f\|^2
\]
for every \(f\in H\).

Fix \(K\ge0\). Require that for all distinct column labels \(j,\ell\), all vectors \(f\in H\), and every subset \(J\subseteq I\),
\[
\sum_{i\in J}\|(\Lambda_{ij}-\Lambda_{i\ell})f\|^2
\le K\min\left\{
\sum_{i\in J}\|\Lambda_{ij}f\|^2,
\sum_{i\in J}\|\Lambda_{i\ell}f\|^2
\right\}.
\]
This is the specific, strong *all-subsets relative perturbation* hypothesis. It is not replaced by a weaker global bound for \(J=I\).

Define
\[
S_j=\sum_{i\in I}\Lambda_{ij}^{*}\Lambda_{ij},\qquad
S_\sigma=\sum_{k=1}^m\sum_{i\in\sigma_k}\Lambda_{ik}^{*}\Lambda_{ik},
\]
where \(\sigma_1,\ldots,\sigma_m\) are disjoint and cover \(I\). The positive-operator sums exist in the strong operator topology since the individual columns are Bessel and \(m\) is finite.

## Proof
Let \(\sigma\) be any partition and fix a source column \(j\). For each \(k\), consider the coefficient vectors indexed by \(\sigma_k\):
\[
X_{j,k}(f)=(\Lambda_{ij}f)_{i\in\sigma_k},\qquad
X_{k,k}(f)=(\Lambda_{ik}f)_{i\in\sigma_k}.
\]
These belong to the same Hilbert direct sum \(\bigoplus_{i\in\sigma_k}K_i\). If \(k\ne j\), the hypothesis with \(J=\sigma_k\) gives
\[
\|X_{j,k}(f)-X_{k,k}(f)\|^2
\le K\min\{\|X_{j,k}(f)\|^2,\|X_{k,k}(f)\|^2\}.
\]
The triangle inequality therefore yields *both* inequalities
\[
\|X_{j,k}(f)\|\le(1+\sqrt K)\|X_{k,k}(f)\|,
\quad
\|X_{k,k}(f)\|\le(1+\sqrt K)\|X_{j,k}(f)\|.
\]
For \(k=j\) both are trivially true because the two vectors coincide. Squaring and summing over the finitely many blocks \(k=1,\ldots,m\) gives
\[
\sum_{i\in I}\|\Lambda_{ij}f\|^2
\le (1+\sqrt K)^2
\sum_{k=1}^m\sum_{i\in\sigma_k}\|\Lambda_{ik}f\|^2
\]
and the reverse comparison with the same factor. Equivalently, for every \(f\in H\),
\[
c_K^{-1}\langle S_jf,f\rangle
\le\langle S_\sigma f,f\rangle
\le c_K\langle S_jf,f\rangle.
\]
Because the operators are bounded and self-adjoint, comparison of all quadratic forms is equivalent to
\[
c_K^{-1}S_j\preceq S_\sigma\preceq c_KS_j.
\]
Using the frame bounds of each column and maximizing the lower estimates, or minimizing the upper estimates, proves
\[
\frac{\max_j A_j}{c_K}\|f\|^2
\le\langle S_\sigma f,f\rangle
\le c_K\min_j B_j\|f\|^2.
\]
Since the left constant is positive, every weaving is a \(g\)-frame.

To establish *global sharpness* of the factor, choose any \(m\ge2\) and \(K\ge0\). In the scalar system
\[
H=K_1=\mathbb C,\quad I=\{1\},\quad
\Lambda_{11}=(1+\sqrt K)I,\quad
\Lambda_{1j}=I\ (2\le j\le m),
\]
all columns are tight \(g\)-frames. For different column labels, their difference is either zero or \(\sqrt K I\); the minimum of the two coefficient energies is \(\|f\|^2\), so the hypothesis holds with equality for the unequal pair. For a partition selecting the first column,
\[
S_\sigma=c_KI,
\]
and a partition selecting any other column has
\[
S_\sigma=I.
\]
With anchor \(j=2\), the first partition attains \(S_\sigma=c_KS_2\). With anchor \(j=1\), the second partition attains \(S_\sigma=c_K^{-1}S_1\). Thus no smaller universal positive-operator comparison factor works for a prescribed \(K\), including the trivial case \(K=0\). For this same family the sharp all-weavings scalar bounds are exactly \(1\) and \(c_K\), and they agree with \(\max_j A_j/c_K\) and \(c_K\min_j B_j\), respectively.

Lastly, the two positive-order inequalities imply
\[
\lambda_{\min}(S_\sigma)\ge c_K^{-1}\lambda_{\min}(S_j),\qquad
\|S_\sigma\|\le c_K\|S_j\|.
\]
For an infinite-dimensional Hilbert space, \(\lambda_{\min}\) denotes the infimum of the spectrum. Dividing the bounds proves
\[
\kappa(S_\sigma)\le c_K^2\kappa(S_j).
\]

## Verification
The proof uses no finite exhaustive computation. It applies to any finite number of frames and finite or countable coefficient index sets, including infinite-dimensional Hilbert spaces, because each compared block lies in a Hilbert direct sum and the coefficient-energy sums are finite.

The sharpness witness can be checked directly with the exact scalar values
\[
A_1=B_1=c_K,\qquad A_j=B_j=1\quad(j\ge2).
\]
The only nonzero relative difference is \(\sqrt K I\), so its squared norm is exactly \(K\|f\|^2\) and the smaller coefficient energy is \(\|f\|^2\). The two extremal partition energies are precisely \(1\) and \(c_K\). No numerical approximation is needed.

The full statement and proof of Theorem 3.5 in the open preprint were checked, including the rendered theorem and proof pages. The corresponding Hilbert \(C^*\)-module analogue (Theorem 2.7 of Rajput--Sahu--Mishra) and the classical weaving perturbation literature were compared at the level of assumptions and operator implications.

## Relationship to prior work
Theorem 3.5 of Li--Leng--Huang--Li already proves that this all-subsets perturbation condition forces weaving and supplies a lower frame bound depending on \(m\) and an upper bound obtained by summing the individual \(B_j\). It does **not** state the sharp two-sided spectral equivalence to every original frame operator. The same type of hypothesis and a corresponding numerical sufficient bound occur in Rajput--Sahu--Mishra's module-valued extension. The present claim is restricted to Hilbert spaces, where coefficient Hilbert-direct-sum comparisons imply positive-operator inequalities without any module-valued norm-versus-order ambiguity.

Bemrose--Casazza--Gröchenig--Lammers--Lynch prove perturbation results using synthesis-operator proximity and nearly identity operators. Those are different perturbation assumptions. Li--Zhu study stability of already woven frames under convergence of frame operators; that does not supply the sharp pairwise relative subset factor here. Xu--Leng study Parseval and dual-frame weaving identities rather than this all-subsets relative comparison.

The new quantitative statement gives a partition-independent preconditioner: **any original frame operator spectrally preconditions every weaving operator with factor at most \(c_K\)**. It simultaneously provides a sharper upper estimate when the sum of the individual Bessel bounds grows with \(m\), and the exact optimal factor is established by the same single-index family for the upper and lower sides.

## Limitations
The all-subsets condition is materially stronger than an estimate restricted to \(J=I\), and it is essential to the blockwise argument. No claim is made for merely globally close coefficient arrays, for infinitely many source frames, or for arbitrary Hilbert \(C^*\)-modules.

The constants in the original source and the new constants need not be ordered for every conceivable list of nonoptimal supplied \(A_j,B_j\). The new assertion is the sharp **individual-operator comparability factor**, not that it always dominates every earlier independent numerical estimate. The one-index witness proves the factor is universal-optimal; a specific family may have better spectral comparisons.

Novelty is assessed against inspected papers and indexed scientific searches, not inferred from the absence of search hits. An unindexed or implicit earlier derivation of the same simple factor remains possible.

## References
1. D. Li, J. Leng, T. Huang and X. Li, *On weaving \(g\)-frames for Hilbert spaces*, arXiv:1709.05154v3, first publicly posted 15 September 2017; Complex Analysis and Operator Theory 14 (2020), article 33, DOI 10.1007/s11785-020-00991-7.
2. E. Rajput, N. K. Sahu and V. N. Mishra, *Woven \(g\)-frames in Hilbert \(C^*\)-modules*, Korean Journal of Mathematics 29(1) (2021), 41–55, DOI 10.11568/kjm.2021.29.1.41.
3. T. Bemrose, P. G. Casazza, K. Gröchenig, M. C. Lammers and R. G. Lynch, *Weaving Frames*, arXiv:1503.03947v1 (2015); Operators and Matrices 10(4) (2016), 1093–1116.
4. X.-B. Li and Y.-C. Zhu, *Stability of Woven Frames*, Frontiers in Physics 10 (2022), article 873955, DOI 10.3389/fphy.2022.873955.
5. Y. Xu and J. Leng, *New inequalities for weaving frames in Hilbert spaces*, Journal of Inequalities and Applications (2021), article 188, DOI 10.1186/s13660-021-02722-8.
