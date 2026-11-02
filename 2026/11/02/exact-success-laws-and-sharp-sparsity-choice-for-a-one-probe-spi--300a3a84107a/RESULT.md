# Exact success laws and sharp sparsity choice for a one-probe spiked range finder

## Finding

Fix an integer \(m\ge 2\), numbers \(a>b>0\), and an oblivious sparsity parameter \(0<p\le1\). The \((m+1)\)-dimensional input is \(A=\operatorname{diag}(a,b,\ldots,b)\). Draw a single probe \(\omega\) with independent coordinates taking \(+p^{-1/2}\) and \(-p^{-1/2}\), each with probability \(p/2\), and zero with probability \(1-p\). This is an isotropic sparse Rademacher probe. Construct the rank-at-most-one range approximation \(PA\), where \(P\) projects onto \(A\omega\) when nonzero and \(P=0\) when \(A\omega=0\).

Let \(S=\|A-PA\|_2^2\) and \(F=\|A-PA\|_F^2\), and, for \(j=0,\dots,m\), set

\[
\delta_j=\frac{b^2j(a^2-b^2)}{a^2+b^2j},\qquad s_j=b^2+\delta_j,\qquad f_j=mb^2+\delta_j.
\]

The complete joint law consists of exactly the following support points and masses (zero masses are permitted at \(p=1\)):

| Event | \((S,F)\) | Probability |
|---|---|---|
| Leading probe coordinate is active and exactly \(j\) trailing coordinates are active, \(0\le j\le m\) | \((s_j,f_j)\) | \(p\binom{m}{j}p^j(1-p)^{m-j}\) |
| Leading coordinate inactive and at least one trailing coordinate active | \((a^2,a^2+(m-1)b^2)\) | \((1-p)[1-(1-p)^m]\) |
| Every coordinate inactive | \((a^2,a^2+mb^2)\) | \((1-p)^{m+1}\) |

Moreover, \(s_0<\cdots<s_m<a^2\) and \(f_0<\cdots<f_m<a^2+(m-1)b^2\). For each \(0\le k<m\), any squared spectral tolerance \(u\in[s_k,s_{k+1})\) or squared Frobenius tolerance \(v\in[f_k,f_{k+1})\) has the **same exact success probability**

\[
q_{m,k}(p)=p\sum_{j=0}^{k}\binom mjp^j(1-p)^{m-j}.
\]

Its **unique** maximizer on \(0<p\le1\) is \(p_{m,k}=t_{m,k}/(1+t_{m,k})\), where \(t_{m,k}>0\) is the unique positive root of

\[
\sum_{j=0}^{k}\binom mjt^j-m\binom{m-1}{k}t^{k+1}=0.
\]

In particular,

\[
p_{m,0}=\frac1{m+1},\qquad p_{m,m-1}=(m+1)^{-1/m}.
\]

At any squared tolerance at least the dense-probe error \(s_m\), respectively \(f_m\), the dense choice \(p=1\) already succeeds with probability one. It is the unique maximizing choice until the tolerance reaches the absolute maximum error \(a^2\), respectively \(a^2+mb^2\), where all choices tie. Consequently, sparsity is strictly optimal for every nontrivial tolerance strictly below the dense-probe error, whereas the dense probe wins at and above its own error. If the tolerance is below \(s_0=b^2\) or \(f_0=mb^2\), success is impossible under any choice.

For each **fixed** \(k\ge0\), as \(m\to\infty\) with \(m>k\),

\[
mp_{m,k}\to\lambda_k,\qquad m\max_p q_{m,k}(p)\to\theta_k,
\]

where \(\lambda_k\) is the unique positive root of

\[
\sum_{j=0}^{k}\frac{\lambda^j}{j!}=\frac{\lambda^{k+1}}{k!},\qquad
\theta_k=\lambda_ke^{-\lambda_k}\sum_{j=0}^{k}\frac{\lambda_k^j}{j!}.
\]

Thus rare high-accuracy success requires a probe with expected support of constant order, and its best one-probe success probability is asymptotic to \(\theta_k/m\). With \(r\) independent probes and the best error retained, the optimal success probability is exactly \(1-(1-\max_pq_{m,k}(p))^r\); for a fixed target confidence \(1-\varepsilon\) and fixed \(k\), the required number of independent probes is asymptotic to \(m\log(1/\varepsilon)/\theta_k\).

## Assumptions and scope

The sampling law is independent across all coordinates and exchangeable, and the single parameter \(p\) is selected without knowing the location of the distinguished singular direction. The analysis is in exact arithmetic, with one sketch column, no oversampling, no power iterations, and the convention \(P=0\) when the sampled vector is identically zero. Both errors are **squared** residual norms, not residual norms. The matrix is specified in singular coordinates solely to give an exact benchmark; for an arbitrary rotation, independent coordinatewise sparsity need not have this law. A non-oblivious design that already knows the leading singular direction can choose that direction deterministically instead.

## Proof

**1. Exact residuals.** Let \(B\) be the indicator that the leading probe coordinate is nonzero and let \(K\sim\operatorname{Binomial}(m,p)\) be the number of nonzero trailing coordinates. These variables are independent. If \(B=1\) and \(K=j\), the probe image has squared length proportional to \(a^2+jb^2\), and the normalized image direction \(q\) satisfies

\[
\|A^\mathsf Tq\|_2^2=\frac{a^4+jb^4}{a^2+jb^2}.
\]

Therefore, by \(\|A-qq^\mathsf TA\|_F^2=\operatorname{tr}(A^\mathsf TA)-\|A^\mathsf Tq\|_2^2\), the squared Frobenius residual is \(f_j\).

For the squared spectral residual, examine \(A^\mathsf T(I-qq^\mathsf T)A\). It has an \((m-1)\)-dimensional trailing invariant subspace with eigenvalue \(b^2\) and a two-dimensional leading/trailing plane with one zero eigenvalue and one eigenvalue

\[
\frac{a^2b^2(j+1)}{a^2+jb^2}=b^2+\delta_j.
\]

At \(j=0\) the same statement follows directly from the diagonal residual. Since \(\delta_j\ge0\), its largest eigenvalue is \(s_j\). The remaining two cases follow by projecting onto a trailing vector or by setting \(P=0\). Thus every nonzero probe satisfies the exact identity \(F-S=(m-1)b^2\), while the all-zero probe has \(F-S=mb^2\). Counting the independent active entries proves all three probability masses, including the zero-probe atom.

**2. Strict order and threshold laws.** From \(a>b>0\), the increment \(\delta_{j+1}-\delta_j\) is positive, while

\[
(a^2-b^2)-\delta_j=\frac{a^2(a^2-b^2)}{a^2+jb^2}>0.
\]

Hence the ordered support and the success event \(\{B=1,K\le k\}\) for either intermediate squared-norm tolerance. Its probability is \(q_{m,k}\). If the tolerance reaches the dense outcome, \(p=1\) is successful surely. For a submaximal tolerance any \(p<1\) has a positive all-zero probability and cannot attain certainty; below the smallest level none can succeed.

**3. Uniqueness of the optimal sparsity.** Write \(H_{m,k}(p)=\Pr(\operatorname{Binomial}(m,p)\le k)\). Telescoping adjacent binomial terms gives

\[
H_{m,k}'(p)=-m\binom{m-1}{k}p^k(1-p)^{m-1-k}.
\]

For \(k<m\), the derivative of \(pH_{m,k}(p)\), multiplied by the positive factor \((1-p)^{-m}\), has the sign of

\[
G_{m,k}(t)=\sum_{j=0}^k\binom mjt^j-m\binom{m-1}{k}t^{k+1},\qquad t=\frac p{1-p}.
\]

Its coefficient sequence has exactly one sign change, \(G_{m,k}(0)=1\), and its leading coefficient is negative. Descartes' rule of signs therefore gives exactly one positive root; the derivative is positive before it and negative after it. The endpoint limits of the success probability are zero. This is the unique global maximizer. Direct differentiation yields the two displayed endpoint-band formulas.

**4. Fixed-band dimension limit.** Put \(p=\lambda/m\) and let \(m\to\infty\) with \(k\) fixed. Then \(G_{m,k}(p/(1-p))\) converges locally uniformly to

\[
G_k(\lambda)=\sum_{j=0}^k\frac{\lambda^j}{j!}-\frac{\lambda^{k+1}}{k!}.
\]

This polynomial also has exactly one positive zero, is positive near zero, and is negative beyond that zero. Bracketing the finite-dimensional unique zeros on either side of that limiting zero shows \(mp_{m,k}\to\lambda_k\). The binomial-to-Poisson limit gives \(m q_{m,k}(p_{m,k})\to\theta_k\). Independence across restarts gives the stated exact geometric amplification and its fixed-confidence asymptotic.

## Verification

Run `python verify.py` with Python 3 and NumPy. The verifier enumerates finite sparse-sign outcomes, directly forms the projected matrices, independently computes singular values and Frobenius norms, checks all rational support masses, checks the polynomial derivative and its numerical optimizer, and checks the low-band Poisson limits. Its latest completed execution printed `PASS: 384994 independent finite checks`.

These checks support, but do not replace, the symbolic argument for all integer dimensions and every real \(a>b>0\), \(0<p\le1\), or the asymptotic limit. The exact probability law also handles the all-zero probe rather than discarding or resampling it.

For example, with \(m=2\), \(a=3\), \(b=1\), squared spectral levels are \(s_0=1\), \(s_1=9/5\), and \(s_2=27/11\). At any target in \([1,9/5)\), the unique best parameter is \(p=1/3\), with success probability \(4/27\); the dense probe has success probability zero. This illustrates the nontrivial design threshold without relying on simulation.

## Relationship to prior work

Saibaba and Międlar (2023, arXiv:2308.05814v1) explicitly introduce sparse Rademacher probes and analyze randomized range approximation through general sub-Gaussian bounds. Their Theorem 3.3, Appendix B.1, and Appendix C assess sufficient sample size and mean/error behavior for oversampled constructions. Those statements do not give this one-column spiked matrix's joint finite distribution, its all-threshold sparsity optimizer, or its rare-success Poisson law. The exact result is complementary, not an improvement of their large-sample bounds: the optimized target is a tail success probability rather than a mean or uniform high-probability upper error bound.

Halko, Martinsson, and Tropp (2009/2011, arXiv:0909.4061) provide the foundational randomized range-finder framework and general deterministic/error bounds, but the inspected relevant analysis does not yield the explicit sparse-zero-atom threshold phase diagram. Existing general projector identities and binomial calculus are used in the proof; neither is claimed as new. The nonzero-probe expected-error ordering under iid sampling, and Gaussian covariance majorization benchmarks, concern different estimands and/or probe families. A specialized existing calculation of this exact sparse one-probe distribution remains a publication-priority risk; a search failure alone cannot establish priority.

## Limitations

The conclusion applies only to one-column iid **coordinatewise** sparse-sign probes in a one-spike diagonal singular basis. It makes no minimax claim among all isotropic sketch laws, no claim for arbitrary singular-vector rotations, multiple-column sketches, or noisy matrix products, and no guarantee that optimizing one tail event minimizes expected error. For thresholds at or above the maximum attainable error, every sparsity ties, so uniqueness is expressly restricted to lower nontrivial thresholds. No floating-point or implementation timing guarantees are asserted. Scientific originality was compared against the inspected sources and available published records, not exhaustively against all possible literature; independent review has not been performed.

## References

1. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814 (first version dated 10 August 2023), https://arxiv.org/abs/2308.05814.
2. N. Halko, P. G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061 (first version dated 22 September 2009), https://arxiv.org/abs/0909.4061.
