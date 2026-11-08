# A Cauchy first-pivot law and unbounded expected row-skeleton loss

## Finding
For every real \(t>0\), consider the nonnegative, full-column-rank matrix
\[
 A_t=\begin{pmatrix}1&0\\0&1\\t&t\end{pmatrix}\in\mathbb R^{3\times2}.
\]
Draw a Gaussian matrix \(\Omega\in\mathbb R^{2\times\ell}\) with independent standard-normal entries, for **any fixed integer** \(\ell\ge1\). Apply ordinary partial row pivoting to the **first column** of \(Y=A_t\Omega\), choosing an index \(J\in\{1,2,3\}\) maximizing the absolute entry. Let \(r_J\) be the corresponding row of \(A_t\), and let \(P_J=r_J^\mathsf{T}r_J/\|r_J\|_2^2\), the orthogonal projector onto its row span.

With \(p_t=\mathbb P(J=3)\),
\[
 p_t=\begin{cases}0,&0<t\le1/2,\\
 \frac2\pi\arctan(2t-1),&t>1/2.
 \end{cases}
\]
The **complete squared-Frobenius error law** of the best rank-one reconstruction using this selected row is
\[
 \|A_t-A_tP_J\|_{\rm F}^2\ \stackrel d=\
 \begin{cases}1,&\text{probability }p_t,\\
 1+t^2,&\text{probability }1-p_t.
 \end{cases}
\]
The optimal unrestricted rank-one error, as well as the optimal one-row-skeleton error, is exactly \(1\). Consequently
\[
 \frac{\mathbb E\|A_t-A_tP_J\|_{\rm F}^2}
 {\min_{\operatorname{rank}B\le1}\|A_t-B\|_{\rm F}^2}
 =1+t^2(1-p_t)
 \sim\frac{t}{\pi}\quad(t\to\infty).
\]
Yet \(p_t\to1\). Thus a pivot that chooses the optimal skeleton with probability tending to one has an **unbounded expected squared-error ratio**. The first-pivot law is unchanged by adding independently Gaussian sketch columns; this does **not** assert anything about complete rank-adaptive or multi-row algorithms.

## Assumptions and scope
All statements use exact real arithmetic and an unscaled first-column maximum-absolute-entry partial row pivot, with ties resolved arbitrarily (ties have probability zero except that no row-three tie occurs at \(t=1/2\) almost surely). Sketch columns are independent \(N(0,I_2)\) vectors. The reconstruction is the optimally least-squares-fitted rank-one matrix constrained to the span of the selected original row, not the interpolation coefficients returned by LUPP. Every rank-one interpolative reconstruction using only the same selected row has no smaller Frobenius loss. No result about the final output of a multi-pivot or adaptive algorithm is claimed.

## Proof
**1. Singular-value and row-subset benchmarks.** Direct multiplication gives
\[
 A_t^\mathsf{T}A_t=I_2+t^2\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
with eigenvalues \(1+2t^2\) and \(1\). By Eckart--Young, the best rank-one squared Frobenius error is exactly \(1\). For \(r_1=(1,0)\) or \(r_2=(0,1)\), orthogonal projection of all rows onto \(\operatorname{span}(r_j)\) leaves squared loss \(1+t^2\). For \(r_3=(t,t)\), the residuals from \(r_1,r_2\) each have squared length \(1/2\), and the third row is exactly fitted; their sum is \(1\). Hence row three is the uniquely optimal one-row choice for every \(t>0\).

**2. The first-pivot event.** Write the first sketch column as \((Z_1,Z_2)^\mathsf{T}\), with independent standard normals. The three absolute pivot scores are \(|Z_1|\), \(|Z_2|\), and \(t|Z_1+Z_2|\). Set \(S=Z_1+Z_2\), \(D=Z_1-Z_2\). These independent random variables are both \(N(0,2)\), and the identity \(\max(|Z_1|,|Z_2|)=(|S|+|D|)/2\) holds pointwise. Thus row three wins precisely when
\[
 (2t-1)|S|>|D|.
\]
If \(t\le1/2\), the event is impossible except a null set. If \(t>1/2\), the ratio \(D/S\) is standard Cauchy, giving
\[
 p_t=\mathbb P\{|D/S|<2t-1\}
 =\frac2\pi\arctan(2t-1).
\]
The first pivot ignores all later sketch columns, hence the law is invariant under any choice of \(\ell\ge1\).

**3. Error distribution, expectation, asymptotics.** Combining Step 1 with Step 2 gives the two-point law and its exact mean. For \(t>1/2\), the complementary failure probability is
\[
 1-p_t=\frac2\pi\arctan\left(\frac1{2t-1}\right).
\]
Since \(\arctan x/x\to1\) as \(x\downarrow0\), we have \(t(1-p_t)\to1/\pi\); hence \(\mathbb E\|A_t-A_tP_J\|_{\rm F}^2/t\to1/\pi\), while \(p_t\to1\). This is an infinite-parameter proof, not an extrapolation from finite tests.

**4. Stronger first-row interpretation.** Every reconstruction \(B=C r_J\) with a single row-skeleton basis vector \(r_J\), for any coefficient column \(C\in\mathbb R^3\), satisfies \(\|A_t-B\|_{\rm F}^2\ge\|A_t-A_tP_J\|_{\rm F}^2\) by rowwise orthogonal projection. Thus the divergence is a lower bound even if interpolation is optimally refitted after the pivot. It does not make claims about using further pivots or increasing the output rank.

## Verification
The standalone `CHECK.py` script tests exact rational row-projection identities for representative positive parameters, numerical angular integration of the Gaussian pivot distribution and expected loss at seven distinct parameters, and the invariance of the first pivot to later random sketch columns. Run `python CHECK.py` from a directory containing the extracted file. These finite computations are secondary checks; the analytic proof above handles every \(t>0\) and integer \(\ell\ge1\).

## Relationship to prior work
Pearce, Chen, Dong and Martinsson (2023), Sections 2.4, 3.1, 4.1 and Appendix 7, formulate Gaussian sketching \(Y=A\Omega\) followed by LUPP for row skeleton selection and investigate adaptive full-decomposition algorithms, using oversampling in their experiments. The first pivot of the sketched matrix, isolated here, follows their LUPP pivoting convention; their complete adaptive method is **not** being evaluated or contradicted. Dong, Chen, Martinsson and Pearce (2023), Sections 2--4 and 6, study robustness and other randomized pivot strategies, including adversarial instances for other rules, without this exact first-column Cauchy law. Pan, Qian and Yan (2014), Sections 7.2--7.4, study Gaussian range finding \(Q(AH)\) and projection \(QQ^\mathsf{T}A\), **not** choosing an original row via the first sketched-column pivot. The distinction between randomized range projection and selecting an original row is essential. Classical Cauchy ratios and the Eckart--Young identity supply standard ingredients, not claimed contributions; the particular pivot-selection distribution, oversampling-independent first-pivot blindness and unbounded expected skeleton-loss classification are the asserted claim.

## Limitations
This is an exact benchmark for one first-pivot selection on a \(3\times2\) family, not a guarantee for arbitrary matrices, other pivoting strategies, or full rank-adaptive IDs. Extra Gaussian columns do not affect the **first** pivot but can improve later decisions. The risk uses squared Frobenius error and optimal least-squares reconstruction restricted to one selected row, which lower-bounds any other interpolation from that row. The result does not imply an infinite expectation for a fixed finite matrix parameter; each \(t>0\) has finite expected loss. Publication precedence remains subject to specialized Gaussian-pivot literature not found in the scoped searches.

## References
1. K. J. Pearce, C. Chen, Y. Dong and P.-G. Martinsson, *Adaptive Parallelizable Algorithms for Interpolative Decompositions via Partially Pivoted LU*, arXiv:2310.09417 (first posted 2023-10-13), https://arxiv.org/abs/2310.09417.
2. Y. Dong, C. Chen, P.-G. Martinsson and K. Pearce, *Robust Blockwise Random Pivoting: Fast and Accurate Adaptive Interpolative Decomposition*, arXiv:2309.16002 (first posted 2023-09-27), https://arxiv.org/abs/2309.16002.
3. V. Y. Pan, G. Qian and X. Yan, *Random Multipliers Numerically Stabilize Gaussian and Block Gaussian Elimination: Proofs and an Extension to Low-rank Approximation*, arXiv:1406.5802 (first posted 2014-06-23), https://arxiv.org/abs/1406.5802.
4. P.-G. Martinsson and S. Voronin, *A randomized blocked algorithm for efficiently computing rank-revealing factorizations of matrices*, arXiv:1503.07157 (first posted 2015-03-24), https://arxiv.org/abs/1503.07157.
