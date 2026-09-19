# The multi-stage ARP product factor is asymptotically sharp

## Statement

Grigori and Xue's multi-stage adaptive randomized pivoting (MSARP) selects columns incrementally by combining projection-DPP/ARP sampling with conditional DPPs. If stage sizes are
\[
k_1,\ldots,k_t\ge 1,\qquad d=\sum_{r=1}^t k_r,
\]
their analysis gives the expected Frobenius-error factor
\[
\prod_{r=1}^t (1+k_r)
\]
relative to the rank-\(d\) residual. They explicitly note that singleton stages yield the exponential factor \(2^t\), while their numerical experiments are much closer to one-shot ARP.

The product factor is nevertheless a genuine worst-case phenomenon, not merely an artifact of multiplying stagewise inequalities.

**Theorem.** For every stage partition \(k_1,\ldots,k_t\) with \(t\ge2\), there is a family of square matrices \(A_\varepsilon\in\mathbb R^{(d+1)\times(d+1)}\) and an allowed ordered orthonormal basis \(V=[V_1,\ldots,V_t]\in\mathbb R^{(d+1)\times d}\) of the exact leading right-singular subspace of \(A_\varepsilon\), with \(V_r\) containing \(k_r\) columns, such that MSARP followed by the ordinary orthogonal column projection satisfies
\[
\lim_{\varepsilon\downarrow0}
\frac{\mathbb E\,\|A_\varepsilon-P_{A_\varepsilon(:,S)}A_\varepsilon\|_F^2}
{\|A_\varepsilon-(A_\varepsilon)_d\|_F^2}
=
\prod_{r=1}^t(1+k_r).
\]
Thus the universal constant in the MSARP bound cannot be reduced without additional assumptions, even if the supplied subspace is the exact best rank-\(d\) right-singular subspace and even if the final error is measured with the optimal orthogonal projector onto the selected columns rather than the larger oblique interpolation error used in the analysis.

On the same family, one-shot ARP using the final \(V\) satisfies
\[
\lim_{\varepsilon\downarrow0}
\frac{\mathbb E\,\|A_\varepsilon-P_{A_\varepsilon(:,S_{\rm one})}A_\varepsilon\|_F^2}
{\|A_\varepsilon-(A_\varepsilon)_d\|_F^2}
=d+1.
\]
Hence the worst-case staged/one-shot gap approaches
\[
\frac{\prod_r(1+k_r)}{d+1}.
\]
For \(k_1=\cdots=k_t=1\), this is \(2^d/(d+1)\): the exponential factor highlighted in the new MSARP analysis can actually occur asymptotically in the expected CSSP approximation error.

## Construction

Let
\[
N_1=\{1,\ldots,k_1+1\},
\]
and for \(r\ge2\) append a disjoint block \(G_r\) of \(k_r\) coordinates, defining
\[
N_r=N_{r-1}\cup G_r,
\qquad |N_r|=1+\sum_{q=1}^r k_q.
\]
Let \(e_1\) be the unit vector that is constant on \(N_1\),
\[
e_1=\frac{1}{\sqrt{k_1+1}}\mathbf 1_{N_1},
\]
and let \(w_r\) be the unit vector constant on \(G_r\). Define recursively
\[
e_r=\cos\theta_r\,e_{r-1}+\sin\theta_r\,w_r,
\qquad r=2,\ldots,t.
\]
The subspaces
\[
H_r=\{x:\operatorname{supp}(x)\subseteq N_r,\ x^Te_r=0\}
\]
are nested and satisfy \(\dim H_r=\sum_{q=1}^r k_q\). Choose the ordered blocks of \(V\) so that its first \(\sum_{q=1}^r k_q\) columns form an orthonormal basis of \(H_r\). The stage-\(r\) projection DPP kernel is therefore
\[
K_r=I_{N_r}-e_re_r^T
\]
on its active coordinates.

Finally set \(e=e_t\), complete \(V\) by \(e\) to an orthogonal matrix
\[
O=[V,e],
\]
and define
\[
A_\sigma=\operatorname{diag}(1,\ldots,1,\sigma)O^T,
\qquad 0<\sigma<1.
\]
Its singular values are \(1\) with multiplicity \(d\) and \(\sigma\) once, so \(V\) is an exact leading right-singular basis and
\[
\|A_\sigma-(A_\sigma)_d\|_F^2=\sigma^2.
\]

## The hole process

After stage \(r\), the selected set has size \(|N_r|-1\), so write it as
\[
S_r=N_r\setminus\{h_r\}.
\]
At the first stage, projection-DPP sampling from \(H_1\) omits a uniformly random point:
\[
\Pr(h_1=j)=\frac1{k_1+1},\qquad j\in N_1.
\]

Suppose \(h_{r-1}=h\). The next conditional DPP must select all previous points and add \(k_r\) points from
\[
\{h\}\cup G_r,
\]
leaving exactly one new hole. Schur-complement conditioning and the determinant identity for the codimension-one projector \(I-e_re_r^T\) give
\[
\Pr(h_r=j\mid h_{r-1}=h)
=
\frac{e_{r,j}^2}
{\cos^2\theta_r\,e_{r-1,h}^2+\sin^2\theta_r},
\qquad j\in\{h\}\cup G_r.
\]
Thus the full MSARP distribution reduces exactly to a one-dimensional Markov chain for the omitted coordinate.

For the oblique interpolant associated with \(V\), omitting coordinate \(j\) gives normalized squared error
\[
\frac{\|A_\sigma-A_\sigma(:,S)V(S,:)^{-T}V^T\|_F^2}{\sigma^2}
=
\frac1{e_j^2}.
\]
Consequently, if
\[
Z_r=\frac1{e_{r,h_r}^2},
\]
then
\[
\mathbb E[Z_r\mid h_{r-1}=h]
=
\frac{k_r+1}
{\cos^2\theta_r\,e_{r-1,h}^2+\sin^2\theta_r}
=
\frac{(k_r+1)Z_{r-1}}
{\cos^2\theta_r+\sin^2\theta_r Z_{r-1}}.
\]

Choose the hierarchical angles
\[
\theta_r(\varepsilon)=\varepsilon^{2^{r-2}},\qquad r\ge2.
\]
Every nonzero component created before stage \(r\) is then much larger than \(\theta_r\), uniformly over all possible holes. Hence
\[
\sin^2\theta_r\,Z_{r-1}\to0
\]
uniformly, and the conditional multiplier tends to \(k_r+1\). Since \(\mathbb E Z_1=k_1+1\), induction yields
\[
\mathbb E Z_t\longrightarrow\prod_{r=1}^t(k_r+1).
\]
This already proves asymptotic sharpness for the oblique error in the theorem of Grigori and Xue.

## The same factor survives optimal orthogonal projection

The selected-column CSSP error is smaller than the oblique interpolation error, so sharpness of the latter alone would not show sharpness of the actual orthogonal projection error. For the matrix family above, however, that error is explicit.

If the final set omits coordinate \(j\), the selected \(d=n-1\) columns are linearly independent. The distance of the omitted column to their span is
\[
\frac{1}{\|A_\sigma^{-T}e_j^{\rm std}\|_2},
\]
which gives
\[
\frac{\|A_\sigma-P_{A_\sigma(:,S)}A_\sigma\|_F^2}{\sigma^2}
=
\frac1{\sigma^2(1-e_j^2)+e_j^2}.
\]
Now take
\[
\sigma(\varepsilon)=\sin^2\theta_t(\varepsilon).
\]
The smallest component of \(e_t\) has squared size comparable to \(\sin^2\theta_t\), while \(\sigma^2=\sin^4\theta_t\). Therefore
\[
\sup_j\frac{\sigma^2(1-e_j^2)}{e_j^2}\to0,
\]
so the orthogonal-projection ratio converges uniformly to \(1/e_j^2\). The same product limit follows.

## Exact two-stage law

For two stages \((k,p)\), take
\[
e_1=\frac1{\sqrt{k+1}}\mathbf1_{k+1},
\qquad
e_2=\cos\theta\,e_1+\sin\theta\,w,
\]
where \(w\) is uniform on the \(p\) new coordinates. Then the oblique expected-error factor is not merely asymptotic but exactly
\[
\boxed{
\mathbb E\,Z_2
=
\frac{(k+1)(p+1)}{1+k\sin^2\theta}
}.
\]
As \(\theta\downarrow0\), this tends to the source bound \((k+1)(p+1)\).

The mechanism is a rare-event amplification. Conditional on the first-stage hole, the total probability of omitting one of the new coordinates is only
\[
\frac{(k+1)\sin^2\theta}{1+k\sin^2\theta},
\]
but each such omission has interpolation loss of order \(\sin^{-2}\theta\). The vanishing probability and diverging loss cancel, leaving a finite factor \(p(k+1)\) in expectation.

## One-shot comparison

For one-shot ARP on the final projector \(VV^T=I-ee^T\), a size-\(d\) projection DPP omits coordinate \(j\) with probability \(e_j^2\). Hence the oblique expected ratio is exactly
\[
\sum_{j=1}^{d+1} e_j^2\frac1{e_j^2}=d+1.
\]
For the orthogonal CSSP error of \(A_{\sigma(\varepsilon)}\), the same uniform argument gives the limit \(d+1\). Therefore incremental conditioning can be genuinely much worse in expectation than resampling once from the final subspace, even though both use the exact same final leading singular subspace.

## Numerical verification

The accompanying script directly implements the nested conditional-DPP hole chain and independently checks the selected-column orthogonal projection error from the constructed matrices.

For blocks \((2,2,1)\), the product bound is \(18\) while the one-shot factor is \(6\). With the stated hierarchy, the orthogonal expected factor progresses
\[
13.6341,\ 15.8325,\ 17.1684,\ 17.6225
\]
as the construction approaches its limiting regime, while one-shot ARP approaches \(6\).

For four singleton stages, the staged product is \(16\) and the one-shot factor is \(5\); the verified orthogonal factors include
\[
13.3559,\ 14.5891,\ 15.2482,
\]
again moving toward the predicted exponential factor. A direct QR projection check agrees with the closed-form per-omission formula to about \(8\times10^{-13}\) in the displayed test.

## Significance and limitations

This result shows that the multiplicative stage penalty in the new MSARP analysis is universally sharp: the exponential singleton-stage factor cannot be removed solely by a better proof of the same assumptions. Any uniformly smaller guarantee must use extra structure, a different incremental rule, oversampling, or another restriction on the matrix/subspace geometry.

The construction is deliberately adversarial. It uses a nearly rank-\(d\) matrix and an ordered basis inside a degenerate leading singular subspace; it does not imply that typical applications exhibit this behavior, and it does not contradict the favorable experiments reported for MSARP. The result concerns expected Frobenius CSSP error and does not establish a comparable lower bound for Nyström error, spectral-norm error, or high-probability tails.

## Originality boundary

Projection DPPs, volume sampling, one-shot ARP, and the classical \(d+1\) CSSP factor are prior work. Grigori and Xue already prove the MSARP upper bound \(\prod_r(1+k_r)\), and they prove tightness of a separate conditional bound when the initial set is prescribed. The claim here is specifically the asymptotic sharpness of the *full multi-stage product factor*, including the actual orthogonal selected-column error, with the supplied \(V\) equal to the exact leading right-singular subspace. No equivalent construction or sharpness theorem was located in the checked source and related literature.

## References

1. L. Grigori and Z. Xue, *Incremental Column Subset Selection via Conditional Determinantal Point Processes*, arXiv:2609.20556, 2026. https://arxiv.org/abs/2609.20556
2. A. Cortinovis and D. Kressner, *Adaptive randomized pivoting for column subset selection, DEIM, and low-rank approximation*, SIAM J. Matrix Anal. Appl. 47(1), 25--47, 2026; arXiv:2412.13992. https://arxiv.org/abs/2412.13992
3. A. Deshpande, L. Rademacher, S. Vempala, and G. Wang, *Matrix Approximation and Projective Clustering via Volume Sampling*, Theory of Computing 2 (2006), 225--247. https://doi.org/10.4086/toc.2006.v002a012
4. A. Belhadji, R. Bardenet, and P. Chainais, *A determinantal point process for column subset selection*, JMLR 21(197), 1--62, 2020. https://jmlr.org/papers/v21/19-080.html
