# Exact multiscale covariance spectrum of fair knockout scores

## Finding
Consider a fixed, complete balanced single-elimination bracket with \(n=2^\ell\) labelled entrants, \(\ell\ge1\). Every played match is resolved by an independent fair coin. Write \(S_i\) for the number of matches won by entrant \(i\), and \(\Sigma_\ell\) for the \(n\)-by-\(n\) covariance matrix of the vector \(S\).

If distinct entrants \(i,j\) belong to opposite children of a smallest common bracket subtree of \(2^d\) leaves, write \(d(i,j)=d\); thus they could first meet in round \(d\). Then
\[
\mathbb E S_i=1-\frac1n,\qquad
\operatorname{Var}(S_i)=2-\frac{2\ell+1}{n}-\frac1{n^2},\qquad
\operatorname{Cov}(S_i,S_j)=-\left(2^{1-d(i,j)}-\frac1n\right)^2.
\]
The nullspace of \(\Sigma_\ell\) is precisely the constant vectors. For each \(d=1,\ldots,\ell\), the contrasts between the two children of a bracket subtree of \(2^d\) leaves are eigenvectors with eigenvalue
\[
\boxed{\lambda_d=\frac6{2^d}-\frac{2(\ell-d)+5}{2^\ell}},
\]
of multiplicity \(2^{\ell-d}\). These are all nonzero eigenvalues, and \(\lambda_1>\cdots>\lambda_\ell=1/n\) when \(\ell\ge2\).

Consequently every real contrast \(a\) satisfying \(\sum_i a_i=0\) obeys the sharp bounds
\[
\boxed{\frac1n\|a\|_2^2\le \operatorname{Var}\left(\sum_i a_i S_i\right)
\le\left(3-\frac{2\ell+3}{n}\right)\|a\|_2^2.}
\]
For \(\ell\ge2\), equality in the lower bound holds exactly for scalar multiples of the final-half contrast; equality in the upper bound holds exactly for the span of the first-round sibling contrasts. The condition number on the zero-sum subspace is exactly \(3n-2\ell-3\).

Under an independent uniform random allocation of entrants to the bracket leaves (or an exchangeable random draw), the score vector has the same marginal variances, but the covariance has just one positive eigenvalue \(n\operatorname{Var}(S_i)/(n-1)\), with multiplicity \(n-1\). Let \(\det_+\) denote the product of the nonzero eigenvalues. Then, as \(\ell\to\infty\),
\[
\boxed{\left(\frac{\det_+\Sigma_{\mathrm{fixed},\ell}}{\det_+\Sigma_{\mathrm{random},\ell}}\right)^{1/n}\longrightarrow\frac34.}
\]
More precisely, the empirical spectral distribution of the fixed-draw covariance converges weakly to \(\sum_{d\ge1}2^{-d}\delta_{6/2^d}\), whereas the randomized-draw distribution converges to \(\delta_2\). These conclusions describe second moments and linear contrasts, not stochastic independence or inference about varying player skills.

## Assumptions and scope
The number of entrants is a power of two, every entrant begins in a distinct leaf, the bracket is complete and deterministic unless expressly randomized, and all internal-node winner choices are mutually independent Bernoulli fair coins. Players have equal ability, draws have no byes, and scores count wins, not matches played, prizes, or skill estimates. For a random draw, the allocation of labels to leaves is uniform and independent of match outcomes. Both covariance matrices have the single deterministic zero-sum direction because \(\sum_i S_i=n-1\) almost surely. The inequalities and multiplicities include \(n=2\), at which the lower and upper eigenvalues coincide.

## Proof
**1. Independent bracket coins and two-entrant dependence.** At each internal node choose independently the winner from the left or right child subtree with probability \(1/2\). For entrant \(i\), let \(W_{i,r}\) indicate survival through round \(r\); then \(S_i=\sum_{r=1}^{\ell}W_{i,r}\) and \(\mathbb P(W_{i,r}=1)=2^{-r}\). For distinct \(i,j\), let \(d=d(i,j)\). If \(r<d\) or \(s<d\), the sets of node coins defining \(W_{i,r}\) and \(W_{j,s}\) are disjoint and the indicators are independent. If both \(r,s\ge d\), both survival events require contradictory choices of their first common node, so their product vanishes. Hence
\[
\operatorname{Cov}(S_i,S_j)
=-\sum_{r=d}^{\ell}\sum_{s=d}^{\ell}2^{-r-s}
=-\left(\sum_{r=d}^{\ell}2^{-r}\right)^2
=-\left(2^{1-d}-2^{-\ell}\right)^2.
\]
For the diagonal, \(W_{i,r}W_{i,s}=W_{i,\max(r,s)}\). Therefore
\[
\mathbb E S_i^2=\sum_{t=1}^{\ell}(2t-1)2^{-t}
=3-(2\ell+3)2^{-\ell},
\]
which yields the displayed mean and variance on subtracting \((1-2^{-\ell})^2\).

**2. Diagonalization.** Put \(c_h=-(2^{1-h}-2^{-\ell})^2\) and \(v=\operatorname{Var}(S_i)\). Every row of \(\Sigma_\ell\) sums to zero because total wins equal \(n-1\); for any leaf, precisely \(2^{h-1}\) other leaves first meet it at round \(h\). Consequently \(v=-\sum_{h=1}^{\ell}2^{h-1}c_h\).

For any bracket subtree \(B\) of \(2^d\) leaves, define its Haar contrast \(h_B\) to be \(+1\) on its left child, \(-1\) on its right child, and zero outside \(B\). For a leaf outside \(B\), every leaf in \(B\) has the same first potential meeting round, so the positive and negative halves cancel when \(\Sigma_\ell h_B\) is evaluated. For a leaf inside \(B\), the within-child leaves at rounds \(h<d\) have the same sign, while the \(2^{d-1}\) opposite-child leaves have the opposite sign. Thus \(\Sigma_\ell h_B=\lambda_d h_B\), with
\[
\lambda_d=v+\sum_{h=1}^{d-1}2^{h-1}c_h-2^{d-1}c_d
=2^d a_d^2+\sum_{h=d+1}^{\ell}2^{h-1}a_h^2,
\qquad a_h=2^{1-h}-2^{-\ell}.
\]
Expanding the geometric sums gives exactly \(\lambda_d=6\cdot2^{-d}-(2(\ell-d)+5)2^{-\ell}\). In particular \(\lambda_\ell=2^{-\ell}\), and for \(d<\ell\),
\[
\lambda_d-\lambda_{d+1}=3\cdot2^{-d}-2\cdot2^{-\ell}>0.
\]
There are \(2^{\ell-d}\) pairwise orthogonal subtree contrasts at level \(d\), and their union together with the constant vector forms an orthogonal basis: \(1+\sum_{d=1}^{\ell}2^{\ell-d}=n\). Thus no spectral directions are missing, all nonconstant modes have positive variance, and the equality cases and sharp contrast bounds follow from the Rayleigh quotient. The ratio of the largest to smallest positive eigenvalues is \(3n-2\ell-3\). The lower-extremizing final-half contrast has score difference \(+1\) or \(-1\) because its two halves each produce a fixed number of internal wins and only the championship contributes the difference.

**3. Uniform random draw and asymptotic generalized variance.** Regardless of outcomes, the multiset of scores is deterministic: \(2^{\ell-1}\) zeros, \(2^{\ell-2}\) ones, continuing through one score of \(\ell-1\) and one of \(\ell\). Uniformly randomizing entrant labels makes \(S\) exchangeable with equal off-diagonal covariances. The constant-total identity forces each off-diagonal to be \(-v/(n-1)\), where \(v\) is the same marginal variance as above. The eigenvalue on the zero-sum hyperplane is therefore \(nv/(n-1)\).

For fixed \(d\), \(\lambda_d\to6/2^d\) as \(\ell\to\infty\); its empirical multiplicity weight is exactly \(2^{-d}\). The omitted weight after level \(D\) is at most \(2^{-D}\), proving the claimed weak spectral limit. Also \(2^{-d}\le\lambda_d\le6\cdot2^{-d}\) for all \(1\le d\le\ell\): use the positive-sum formula above for the lower bound and the closed form for the upper bound. Hence \(\sum_d2^{-d}|\log\lambda_d|\) is dominated by a summable sequence independent of \(\ell\). Consequently
\[
\lim_{\ell\to\infty}\frac1n\log\det_+\Sigma_{\mathrm{fixed},\ell}
=\sum_{d\ge1}2^{-d}\log\frac6{2^d}
=\log6-2\log2=\log\frac32.
\]
As \(v\to2\) and \((n-1)/n\to1\), the analogous limit for the random-draw covariance is \(\log2\). Subtracting and exponentiating proves the three-quarter limit.

## Verification
Run \(\texttt{python3 verify_knockout_spectrum.py}\) from a directory containing the standalone checker. It enumerates all \(2^{n-1}\) independent bracket-coin assignments for \(n=2,4,8,16\); computes raw first and second score moments with integer arithmetic; compares each entry with the claimed rational covariance; verifies all dyadic Haar eigenvector identities, spectral ordering, extremal eigenvalues, and the condition-number identity. The checker uses only the Python standard library and executes 1,085 exact rational assertions plus finite floating-point diagnostics. It does not infer any infinite-size claim from finite enumeration; all-range identities and asymptotic arguments are proved above.

## Relationship to prior work
Adler, Cao, Karp, Peköz and Ross (2016) analyzed knockout tournament formats and win probabilities under strength-dependent outcomes and random match formation. Malinovsky and Rinott (2022 preprint, 2023 journal) studied negative dependence of tournament score vectors for both random and fixed brackets, explicitly describing the score multiset under random draws. Su, Zou and Hu (2025 preprint) subsequently established negative association for equal-strength **fixed** knockout brackets, correcting the earlier claim that a fixed bracket supplies a counterexample to negative association. These dependence theorems already imply nonpositive covariance signs and are not claimed as new here. The present specific claim is the exact dyadic covariance kernel, full ordered eigenspectrum, sharp linear-contrast bounds, empirical spectral law and three-quarter generalized-variance comparison; these are not stated in the inspected primary texts. A historical search cannot prove novelty.

## Limitations
The proofs require independent fair outcomes, a complete balanced bracket without byes and a fixed set of participants. No weighted-skills, adaptive seeding, or nonbinary tournament theorem is asserted. The spectral and determinant limits concern score covariance, not likelihood information, causal inference, or classification accuracy. The three-quarter ratio is a geometric-mean generalized **variance** ratio; the corresponding covariance-ellipsoid volume ratio would involve a square root. Literature priority is not independently certified and an older hierarchical-kernel calculation might subsume the result. The manuscript and checker have not received independent mathematical validation.

## References
1. I. Adler, Y. Cao, R. M. Karp, E. A. Peköz, and S. M. Ross, *Random Knockout Tournaments*, arXiv:1612.04448, publicly posted 2016-12-14, https://arxiv.org/abs/1612.04448.
2. Y. Malinovsky and Y. Rinott, *On Tournaments and Negative Dependence*, arXiv:2206.08461, v1 publicly posted 2022-06-16; *Journal of Applied Probability* 60 (2023), 945–954, https://arxiv.org/abs/2206.08461.
3. Y. Su, Z. Zou, and T. Hu, *Negative Dependence in Knockout Tournaments*, arXiv:2505.01971, v1 publicly posted 2025-05-04, https://arxiv.org/abs/2505.01971.
