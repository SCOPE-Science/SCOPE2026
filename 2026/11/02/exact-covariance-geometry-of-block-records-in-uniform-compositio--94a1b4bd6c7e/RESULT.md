# Exact covariance geometry of block records in uniform compositions

## Finding

Let \(n\ge k\ge2\) be integers. Choose an ordered composition \((B_1,\ldots,B_k)\) of \(n\) into \(k\) positive parts uniformly. Independently assign continuous, identically distributed random labels to the \(n\) positions. Let \(R_i\) be the number of strict left-to-right record labels within block \(i\). The joint law of these block counts is the canonical block-record representation of the Lah distribution.

Set \(d=n-k+1\), \(\Delta=H_n-H_{k-1}\), and \(T_s=H_n^{(s)}-H_{k-1}^{(s)}\), where \(H_m^{(s)}=\sum_{j=1}^{m}j^{-s}\), with \(H_0^{(s)}=0\). For distinct \(i,j\), the *entire* covariance matrix has diagonal entry

\[
V_{n,k}=\operatorname{Var}(R_i)
=\frac nd\left(\Delta-T_2-\frac{k-1}{d}\Delta^2\right)
\]

and off-diagonal entry

\[
C_{n,k}=\operatorname{Cov}(R_i,R_j)
=\frac{n}{d(d+1)}\left(2\Delta-\frac{k-1}{d}\Delta^2+\frac1{n+1}-(n+1)\left[T_2+\frac1{(n+1)^2}\right]\right).
\]

Thus \(\Sigma_{n,k}=(V_{n,k}-C_{n,k})I_k+C_{n,k}\mathbf1\mathbf1^{\mathsf T}\). Its eigenvalues are \(V_{n,k}-C_{n,k}\) (multiplicity \(k-1\)) and \(V_{n,k}+(k-1)C_{n,k}\) (multiplicity one). For \(n>k\), the off-diagonal value is strictly negative and the covariance matrix is positive definite. For \(n=k\), every record count is one and the covariance matrix is zero.

The exact off-diagonal formula yields four complementary asymptotic regimes for any distinct blocks:

1. For fixed \(k\ge2\) as \(n\to\infty\),
\[
C_{n,k}=H_{k-1}^{(2)}-\frac{\pi^2}{6}+O_k\!\left(\frac{\log n}{n}\right).
\]
In particular, a strictly negative covariance survives when \(n\) diverges.
2. If \(k\to\infty\) and \(k/n\to0\), then \(kC_{n,k}\to-1\).
3. If \(k/n\to\alpha\in(0,1)\), then
\[
nC_{n,k}\longrightarrow-\frac{(1-\alpha+\alpha\log\alpha)^2}{\alpha(1-\alpha)^3}.
\]
4. For fixed integer \(r\ge1\), if \(k=n-r\) then \(n^2C_{n,k}\to-r/4\). When \(r=0\), covariance is identically zero.

## Assumptions and scope

The composition is uniform among precisely \(\binom{n-1}{k-1}\) positive ordered compositions. Labels are independent and have any common continuous distribution, so ties have probability zero. Each block is read from left to right. Strict records include the first element of every block. No assumption on relative growth of \(n\) and \(k\) is made for the finite identities. The four displayed limits use their stated and distinct parameter regimes.

## Proof

**Conditional record laws.** Conditional on \((B_1,\ldots,B_k)\), the record counts in different blocks are independent. For a block of length \(m\), classical uniform-permutation record indicators are independent Bernoulli variables with success probabilities \(1,1/2,\ldots,1/m\). Hence
\[
\mathbb E[R_i\mid B_i=m]=H_m,\quad
\mathbb E[(R_i)_2\mid B_i=m]=H_m^2-H_m^{(2)},
\quad\operatorname{Var}(R_i\mid B_i=m)=H_m-H_m^{(2)}.
\]
In particular, \(\operatorname{Cov}(R_i,R_j)=\operatorname{Cov}(H_{B_i},H_{B_j})\) for \(i\ne j\).

**Exact coefficient evaluations.** Write \(L(z)=-\log(1-z)\) and \(A(z)=z/(1-z)\). Then \(\sum_{m\ge1}H_mz^m=L(z)/(1-z)\), while the generating function of the second factorial moment of the record count is \(L(z)^2/(1-z)\). The normalizing composition count is \([z^n]A(z)^k=\binom{n-1}{k-1}\). Marking a single block, and marking two distinct blocks, respectively, yields
\[
\mathbb E R_i=\frac{[z^n]A(z)^{k-1}L(z)/(1-z)}{\binom{n-1}{k-1}}
=\frac nd\Delta,
\]
\[
\mathbb E(R_i)_2=\frac nd(\Delta^2-T_2),
\]
\[
\mathbb E[R_iR_j]
=\frac{[z^n]A(z)^{k-2}L(z)^2/(1-z)^2}{\binom{n-1}{k-1}}
=\frac{n(n+1)}{d(d+1)}\left[(\Delta+1/(n+1))^2-T_2-1/(n+1)^2\right].
\]
These coefficient identities follow by differentiating \([z^m](1-z)^{-a}=\binom{a+m-1}{m}\) with respect to \(a\) once and twice. Taking the required differences of moments gives \(V_{n,k}\) and \(C_{n,k}\) above; the latter simplification uses \(n(n+1)/(d(d+1))-n^2/d^2=-n(k-1)/(d^2(d+1))\).

**Strict sign and nonsingularity.** Conditional on \(B_i=a\), the other \(k-1\) lengths form a uniform composition of \(n-a\). A classical Pólya-urn coupling increases every component weakly when the total increases, and increases each specified component with positive probability. Thus \(\mathbb E[H_{B_j}\mid B_i=a]\) decreases strictly as \(a\) grows through its support. Since \(H_a\) strictly increases and \(B_i\) is nonconstant for \(n>k\), their covariance is strictly negative. Moreover, each \(R_i\) has positive conditional variance on an event of positive probability, because \(B_i\ge2\) is possible for \(n>k\). The conditional covariance matrix is diagonal and its expected diagonal entries are all strictly positive. Its sum with the covariance of the conditional means is therefore positive definite.

**Asymptotic calculations.** The exact off-diagonal identity can also be written
\[
C_{n,k}=\frac{n}{d(d+1)}\left(2\Delta-\frac{k-1}{d}\Delta^2-(n+1)\sum_{j=k}^{n+1}\frac1{j^2}+\frac1{n+1}\right).
\]
For fixed \(k\), \(\Delta=\log n+\gamma-H_{k-1}+O(1/n)\), and the square-sum tends to \(\pi^2/6-H_{k-1}^{(2)}\), yielding the first regime and its remainder estimate. If \(k\to\infty\) but \(k/n\to0\), then \(k\sum_{j=k}^{n+1}j^{-2}\to1\) and \((k/n)\log(n/k)\to0\), \((k/n)^2\log^2(n/k)\to0\); the other terms vanish after multiplication by \(k\). If \(k/n\to\alpha\in(0,1)\), then \(\Delta\to-\log\alpha\), \((n+1)\sum_{j=k}^{n+1}j^{-2}\to1/\alpha-1\), and direct substitution simplifies to the displayed negative function. Its numerator is nonzero because \(1-\alpha+\alpha\log\alpha>0\) on \((0,1)\).

Finally fix \(r=n-k\). Put \(X_i=B_i-1\) and \(J_i=\mathbf1_{\{X_i\ge1\}}\). Uniform weak compositions give
\[
\mathbb E J_i=\frac r{n-1},\qquad
\mathbb E[J_iJ_j]=\frac{r(r-1)}{(n-1)(n-2)}.
\]
For fixed \(r\), \(H_{1+X_i}=1+J_i/2+E_i\), where \(E_i\) vanishes unless \(X_i\ge2\). The joint weak-composition counts imply \(\operatorname{Cov}(E_i,J_j)=O_r(n^{-3})\) and \(\operatorname{Cov}(E_i,E_j)=O_r(n^{-4})\). Therefore \(C_{n,k}=\operatorname{Cov}(J_i,J_j)/4+O_r(n^{-3})=-r/(4n^2)+O_r(n^{-3})\). This proves the last regime.

## Verification

The standalone program `checker.py` uses exact rational arithmetic. It compared the two closed covariance entries and the mean against explicit uniform-composition sums for \(2\le n\le14\), then independently enumerated the underlying label orders and compositions for smaller values. It passed 432 exact identities/sign assertions and explicitly enumerated 305826 label-order/composition microstates. The finite checks corroborate, but do not replace, the all-order coefficient and limit proofs. Reproduce with `python3 checker.py`.

## Relationship to prior work

Kabluchko and Marynych (arXiv:2105.11365, first submitted 24 May 2021) introduced the block-record construction of the Lah distribution. Their Proposition 2.3 gives the conditional representation, Lemma 5.14 proves negative association of uniform composition lengths, and Equation (5.31) establishes that the covariance of two harmonic-number transforms of distinct lengths is nonpositive. Their Theorem 3.5 and Corollary 3.6 give factorial moments of the total number of records. Those results provide the key representation and qualitative bound, but do not state the two explicit covariance-matrix entries or the four sharp cross-block covariance scales above. This finding does not claim the Lah distribution, its total-count factorial moments, or negative association of composition lengths as new.

Finch (arXiv:2010.06643, first submitted 13 October 2020) investigates part count versus maximum part for unrestricted random compositions; this is a different statistic and sampling ensemble. General record-indicator independence and harmonic generating functions are classical. The new claimed content is the *quantitative all-size blockwise covariance geometry and its scaling transitions*, not these inputs. The possibility that equivalent formulas are implicit in earlier generating-function literature remains a priority risk.

## Limitations

The exact theorem concerns independent continuous labels and uniform compositions with a fixed number of blocks. The limiting regimes do not by themselves give uniform finite-sample error bounds when their parameters move between regimes. An explicit formula can be derivable from existing total-count and marginal generating functions without previously having been displayed; this is a meaningful residual historical-priority risk. Neither independent validation nor a literature-completeness certificate is asserted.

## References

1. Z. Kabluchko and A. Marynych, *Lah distribution: Stirling numbers, records on compositions, and convex hulls of high-dimensional random walks*, arXiv:2105.11365, v1 posted 24 May 2021, https://arxiv.org/abs/2105.11365.
2. S. Finch, *Covariance within Random Integer Compositions*, arXiv:2010.06643, v1 posted 13 October 2020, https://arxiv.org/abs/2010.06643.
3. K. Joag-Dev and F. Proschan, *Negative association of random variables, with applications*, Annals of Statistics 11 (1983), 286–295; cited for the classical dependence framework, not an originality claim.
