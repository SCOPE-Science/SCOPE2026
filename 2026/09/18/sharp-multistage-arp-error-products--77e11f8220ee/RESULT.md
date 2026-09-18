# Worst-case sharpness of multistage adaptive randomized pivoting

## Summary

Grigori and Xue introduced multi-stage adaptive randomized pivoting (MSARP) for incremental column subset selection and proved that, for stage sizes \(k_1,\ldots,k_t\), its expected squared Frobenius error is bounded by
\[
\prod_{i=1}^t (k_i+1)
\]
times the residual associated with the final right-singular subspace. Their paper proves that one conditional stage can attain its factor \(p+1\) for a prescribed initial subset, but it does not establish whether the full unconditional multi-stage product is sharp.

Here the product factor is shown to be worst-case sharp as a supremum for every stage partition. The sharpness persists for the actual orthogonal column-subset projection error, not only for the oblique interpolation surrogate used in the analysis. For singleton stages, the worst-case expected-error ratio between MSARP and one-shot ARP on the same final matrix and final right-singular subspace can approach
\[
\frac{2^d}{d+1}.
\]
The sharp expectation is carried by a rare-event mechanism: vanishing-probability omissions have diverging error.

## Setup

Let \(V\in\mathbb R^{m\times d}\) have orthonormal columns and \(K=VV^T\). A projection DPP with kernel \(K\) samples \(d\) indices with probability equal to the corresponding principal minor. ARP has this projection-DPP law.

MSARP partitions the final basis into blocks of sizes \(k_1,\ldots,k_t\), samples the first block by ARP, and samples each later block from the conditional projection DPP while retaining earlier indices. The source paper proves the upper factor \(\prod_i(k_i+1)\).

## Codimension-one identities

Set \(m=d+1\). Let \(z\in\mathbb R^m\) be unit with all coordinates nonzero and choose \(V\) such that
\[
[V,z]\in O(m).
\]
Then \(VV^T=I-zz^T\). Every \(d\)-subset is the complement of one index \(j\), and
\[
\det((I-zz^T)_{-j,-j})=z_j^2.
\]
Hence a one-shot projection DPP omits \(j\) with probability \(z_j^2\). More generally, conditioned on a selected set \(S\),
\[
\boxed{\mathbb P(J=j\mid S)=\frac{z_j^2}{1-\|z_S\|_2^2},\qquad j\notin S.}
\tag{1}
\]

For the oblique interpolation model with residual row \(z^T\), omission of \(j\) produces squared error ratio
\[
\boxed{R_j^{\rm obl}=\frac1{z_j^2}.}
\tag{2}
\]
Indeed, the residual matches zero on the selected coordinates and therefore equals \(\alpha e_j^T\); orthogonality to \(V\) gives \(\alpha z_j=1\).

Consequently one-shot ARP has
\[
\boxed{\mathbb E R_{\rm one}^{\rm obl}=d+1.}
\tag{3}
\]

## Theorem 1: exact two-stage sharp family

Let the stage sizes be \(k,p\ge1\), so \(d=k+p\). Choose
\[
0<\varepsilon<1/\sqrt p,\qquad
\alpha^2=\frac{1-p\varepsilon^2}{k+1},
\]
and define
\[
z=(\underbrace{\alpha,\ldots,\alpha}_{k+1},
   \underbrace{\varepsilon,\ldots,\varepsilon}_{p}).
\tag{4}
\]
Let \(V_1\) be an orthonormal basis of the zero-sum subspace on the first \(k+1\) coordinates, padded by zeros on the last \(p\) coordinates, and complete it by \(p\) columns to an orthonormal basis \(V=[V_1,V_2]\) of \(z^\perp\).

The first-stage projection DPP selects \(k\) of the first \(k+1\) indices uniformly. Given the one unselected head index, the second stage leaves exactly one index omitted among that head index and the \(p\) tail indices. With
\[
D=\alpha^2+p\varepsilon^2
=\frac{1+kp\varepsilon^2}{k+1},
\]
the final omitted index is the remaining head index with probability
\[
\frac{1-p\varepsilon^2}{1+kp\varepsilon^2},
\]
and lies in the tail with total probability
\[
\boxed{P_{\rm bad}=
\frac{p(k+1)\varepsilon^2}{1+kp\varepsilon^2}.}
\tag{5}
\]
The head omission has oblique error \(1/\alpha^2\), while a tail omission has error \(1/\varepsilon^2\). Therefore
\[
\boxed{\mathbb E R_{\rm MSARP}^{\rm obl}
=
\frac{(k+1)(p+1)}{1+kp\varepsilon^2}.}
\tag{6}
\]
Thus
\[
\boxed{\sup \mathbb E R_{\rm MSARP}^{\rm obl}=(k+1)(p+1).}
\tag{7}
\]
This proves sharpness of the source paper's two-stage factor even though the first-stage subset here is random rather than prescribed.

The same final subspace used by one-shot ARP has mean \(k+p+1\), so the staged/one-shot ratio approaches
\[
\boxed{\frac{(k+1)(p+1)}{k+p+1}.}
\tag{8}
\]

### Rare-event mechanism

Equation (5) gives \(P_{\rm bad}\sim p(k+1)\varepsilon^2\), while the bad error equals \(\varepsilon^{-2}\). Their product therefore tends to \(p(k+1)\). The tail contribution to the second moment is
\[
P_{\rm bad}\varepsilon^{-4}
=
\frac{p(k+1)}
{(1+kp\varepsilon^2)\varepsilon^2},
\tag{9}
\]
so the variance diverges as \(\varepsilon\to0\). Meanwhile the good branch has error tending to \(k+1\), and its probability tends to one. The worst-case expectation is therefore driven by increasingly rare catastrophic omissions.

## Theorem 2: sharpness for every stage partition

Let \(k_1,\ldots,k_t\ge1\). For every \(\eta>0\), there exists a nested orthonormal basis compatible with these stage sizes such that
\[
\boxed{
\mathbb E R_{\rm MSARP}^{\rm obl}>
(1-\eta)\prod_{i=1}^t(k_i+1).
}
\tag{10}
\]
Together with the source upper bound,
\[
\boxed{
\sup\mathbb E R_{\rm MSARP}^{\rm obl}
=
\prod_{i=1}^t(k_i+1).
}
\tag{11}
\]

### Proof

For stage one, take a positive unit vector \(z^{(1)}\in\mathbb R^{k_1+1}\) and let \(V^{(1)}\) span \((z^{(1)})^\perp\). The first projection DPP omits \(j\) with probability \((z_j^{(1)})^2\), so by (2)
\[
R_1=k_1+1.
\tag{12}
\]

Suppose stages through \(r-1\) have been built with null vector \(z^{(r-1)}\), and let \(P_{r-1}(j)\) denote the probability that the one omitted old index is \(j\). Choose
\[
0<\varepsilon_r<1/\sqrt{k_r},\qquad
a_r=\sqrt{1-k_r\varepsilon_r^2},
\]
and extend
\[
\boxed{
z^{(r)}
=
(a_rz^{(r-1)},\varepsilon_r\mathbf1_{k_r}).
}
\tag{13}
\]
Pad every old basis column with \(k_r\) zeros and complete them by \(k_r\) orthonormal columns to a basis of \((z^{(r)})^\perp\). This preserves every earlier stage.

Conditioned on old omission \(j\), the new conditional projection DPP can omit that old index or one of the \(k_r\) new indices. The total conditional DPP weight is
\[
D_j=a_r^2(z_j^{(r-1)})^2+k_r\varepsilon_r^2.
\]
Using (1) and (2), its conditional expected final error ratio is exactly
\[
\frac{k_r+1}{D_j}.
\]
Hence
\[
\boxed{
R_r=(k_r+1)\sum_j
\frac{P_{r-1}(j)}
{a_r^2(z_j^{(r-1)})^2+k_r\varepsilon_r^2}.
}
\tag{14}
\]
For fixed preceding stages,
\[
\lim_{\varepsilon_r\downarrow0}R_r
=(k_r+1)R_{r-1}.
\tag{15}
\]
Choosing the successive \(\varepsilon_r\) sufficiently small proves (10) by induction.

## Sharpness for the actual orthogonal CSS error

The same factors are sharp for orthogonal column projection. For a final \([V,z]\in O(d+1)\), define
\[
A_\delta=
\operatorname{diag}(1,\ldots,1,\delta)[V,z]^T,
\qquad 0<\delta<1.
\tag{16}
\]
Its first \(d\) right singular vectors are the columns of \(V\), and
\[
\|A_\delta-(A_\delta)_d\|_F^2=\delta^2.
\]
If the selected \(d\)-subset omits \(j\), then a Gram-determinant height identity gives
\[
\boxed{
R_j^{\rm CSS}(\delta)
=
\frac{\|A_\delta-P_{A_\delta(:,U)}A_\delta\|_F^2}{\delta^2}
=
\frac1{z_j^2+\delta^2(1-z_j^2)}.
}
\tag{17}
\]
Indeed,
\[
A_\delta^TA_\delta=I-(1-\delta^2)zz^T,
\]
so the full Gram determinant is \(\delta^2\) and the selected principal Gram determinant is \(z_j^2+\delta^2(1-z_j^2)\).

Thus
\[
R_j^{\rm CSS}(\delta)\to z_j^{-2}
\qquad(\delta\downarrow0).
\]
For each fixed staged distribution, finite summation gives
\[
\mathbb E R_{\rm MSARP}^{\rm CSS}(\delta)
\to
\mathbb E R_{\rm MSARP}^{\rm obl}.
\]
Combining this with Theorem 2 yields
\[
\boxed{
\sup
\frac{\mathbb E\|A-P_{A(:,U_{\rm MSARP})}A\|_F^2}
{\|A-A_d\|_F^2}
=
\prod_{i=1}^t(k_i+1).
}
\tag{18}
\]
So the source product is not an artifact of the oblique surrogate.

For one-shot ARP on the same \(A_\delta,V\),
\[
\mathbb E R_{\rm one}^{\rm CSS}(\delta)
=
\sum_j
\frac{z_j^2}
{z_j^2+\delta^2(1-z_j^2)}
\longrightarrow d+1.
\tag{19}
\]

## Corollary: exponential staged-versus-one-shot separation

For singleton stages \(k_1=\cdots=k_d=1\), the same final matrix and final dominant right-singular subspace can be chosen so that
\[
\mathbb E R_{\rm MSARP}^{\rm CSS}\to2^d,
\qquad
\mathbb E R_{\rm one}^{\rm CSS}\to d+1.
\]
Therefore the worst-case ratio can approach
\[
\boxed{\frac{2^d}{d+1}.}
\tag{20}
\]
This is a genuine worst-case cost of nested, irrevocable selection.

## Relation to prior work

Grigori and Xue (2026) introduce conditional DPPs for incremental CSS, prove a conditional factor \(p+1\), give an equality example for a prescribed initial subset, and prove the unconditional two-stage and general MSARP product bounds. They do not give an unconditional multi-stage sharpness construction, an orthogonal-CSS sharpness result, or a staged-versus-one-shot separation.

Cortinovis and Kressner (2026) establish one-shot ARP and its optimal expected Frobenius guarantee. Epperly (2025/2026) connects ARP and volume sampling and develops further one-shot analysis and implementations. Classical volume-sampling work supplies the one-shot \(k+1\) factor and matching lower-bound phenomena. These results do not address the nested conditional-DPP product.

To the best of our knowledge, the full product sharpness, the rare-event mechanism above, and the exponential MSARP/one-shot separation have not previously been stated.

## Limitations

- Sharpness is a worst-case supremum approached through increasingly imbalanced leverage scores; it need not describe typical data.
- The explicit variance divergence is stated for the oblique surrogate. Orthogonal CSS attains the same mean factors through the additional \(\delta\downarrow0\) limit, but no finite-\(\delta\) universal variance theorem is claimed.
- The construction has ambient dimension \(d+1\) and permits repeated leading singular values. It proves worst-case sharpness but does not classify all extremizers.
- No claim is made that MSARP is inferior on natural matrix ensembles. The source experiments showing performance close to one-shot ARP are compatible with the rare-event worst-case mechanism.
- Originality is to the best of our knowledge. The source preprint is very recent, so simultaneous or not-yet-indexed follow-up work remains a residual risk.

## Reproducibility

`artifacts/verify_sharpness.py` checks the exact two-stage formula, recursively constructs representative multistage examples, compares staged and one-shot oblique and orthogonal-CSS ratios, and verifies nested orthonormal bases. It was executed with Python 3.13.5 and NumPy 2.3.5. `artifacts/verification_output.txt` records the output.

The numerical checks support the formulas but are not used as a substitute for the analytic proofs.

## References

1. L. Grigori and Z. Xue, *Incremental Column Subset Selection via Conditional Determinantal Point Processes*, arXiv:2609.20556, 2026. https://arxiv.org/abs/2609.20556
2. A. Cortinovis and D. Kressner, *Adaptive Randomized Pivoting for Column Subset Selection, DEIM, and Low-Rank Approximation*, SIAM J. Matrix Anal. Appl. 47 (2026), 25–47. https://doi.org/10.1137/24M1719189
3. E. N. Epperly, *Adaptive randomized pivoting and volume sampling*, arXiv:2510.02513. https://arxiv.org/abs/2510.02513
4. A. Deshpande, L. Rademacher, S. S. Vempala, and G. Wang, *Matrix Approximation and Projective Clustering via Volume Sampling*, Theory of Computing 2 (2006), 225–247. https://doi.org/10.4086/toc.2006.v002a012
5. A. Deshpande and L. Rademacher, *Efficient Volume Sampling for Row/Column Subset Selection*, FOCS 2010. https://doi.org/10.1109/FOCS.2010.38
