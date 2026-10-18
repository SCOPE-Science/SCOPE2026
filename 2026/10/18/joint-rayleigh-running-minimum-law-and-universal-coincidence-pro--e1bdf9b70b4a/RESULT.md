# Joint Rayleigh running-minimum law and universal coincidence probabilities for overpartition least gaps

## Finding
For a uniformly sampled overpartition of a positive integer \(N\), let \(M_r\) denote the least positive part whose **nonoverlined** multiplicity is less than \(r\). Fix any positive integer \(R\). The vector
\[
N^{-1/4}(M_1,\ldots,M_R)
\]
converges in distribution as \(N\to\infty\) to
\[
(W_1,\min(W_1,W_2),\ldots,\min(W_1,\ldots,W_R)),
\]
where the \(W_a\) are independent with \(\Pr(W_a>x)=\exp(-\pi x^2/4)\) for \(x\ge0\).

In particular, for **every fixed pair** of positive integers \(1\le r<s\),
\[
\lim_{N\to\infty}\Pr(M_r=M_s)=\frac rs.
\]
This second assertion is a separate *discrete diagonal limit*; it is not inferred merely from weak convergence of the vector.

More explicitly, given finitely many integer threshold pairs \((r_i,k_i)\) with \(r_i\ge1\) and \(k_i\ge0\), put \(R=\max_i r_i\), \(K_a=\max(\{k_i:r_i\ge a\}\cup\{0\})\), and \(T_k=k(k+1)/2\). If \(\bar p(m)\) is the overpartition number (extended by zero when \(m<0\)), then the **exact joint count** is
\[
\#\{\pi\text{ an overpartition of }N:M_{r_i}(\pi)>k_i\text{ for all }i\}
=\bar p\!\left(N-\sum_{a=1}^{R}T_{K_a}\right).
\]
Consequently, for \(x_i\ge0\),
\[
\lim_{N\to\infty}\Pr(M_{r_i}>x_iN^{1/4}\text{ for all }i)
=\exp\!\left[-\frac\pi4\sum_{a=1}^{R}
\left(\max(\{x_i:r_i\ge a\}\cup\{0\})\right)^2\right].
\]

## Assumptions and scope
An overpartition is an integer partition in which at most one occurrence of each positive part may be distinguished by an overline. The statistic counts **only nonoverlined copies**, exactly as in the least-gap definition of Aricheta and Donato. The sample space consists of all \(\bar p(N)\) overpartitions with equal probability. All indices \(r,s,R,r_i\) are fixed positive integers independent of \(N\); the threshold \(x_i\) is any fixed nonnegative real. The limit does not assert uniformity as the gap indices grow with \(N\). The empty overpartition at \(N=0\) is allowed in the exact identities.

## Proof
**1. Exact joint removal identity.** For any overpartition, let \(\nu_j\) be the count of nonoverlined copies of part \(j\). The condition \(M_{r_i}>k_i\) means precisely \(\nu_j\ge r_i\) for every \(1\le j\le k_i\). Thus every \(\nu_j\) must exceed the largest applicable threshold. Removing that mandatory number of nonoverlined \(j\)'s for each \(j\) is a bijection onto all overpartitions of weight
\[
N-D,\qquad
D=\sum_{j\ge1}j\max(\{r_i:j\le k_i\}\cup\{0\}).
\]
Indeed, removing or reinserting nonoverlined copies leaves the optional overline on each part unchanged. Decompose a maximal multiplicity into its unit layers: the \(a\)-th mandatory layer contains precisely parts \(j\le K_a\). It follows that \(D=\sum_{a=1}^{R}T_{K_a}\), proving the exact count.

**2. Analytic ratio and vector limit.** The classical overpartition asymptotic, with its Rademacher-error estimate, is
\[
\bar p(N)=\frac{\exp(\pi\sqrt N)}{8N}
\bigl(1+O(N^{-1/2})\bigr)\quad(N\to\infty).
\]
This follows, for example, from the explicit main term and exponentially smaller remainder in Engel's treatment of the Sills series (references [3]–[4]). Uniformly for integer \(0\le D\le C\sqrt N\), with fixed \(C\), expand the square root and prefactor to obtain
\[
\frac{\bar p(N-D)}{\bar p(N)}
=\exp\!\left(-\frac{\pi D}{2\sqrt N}\right)
\bigl(1+O_C(N^{-1/2})\bigr).
\]
Take \(k_i=\lfloor x_iN^{1/4}\rfloor\). Since
\[
\frac{T_{K_a}}{\sqrt N}\longrightarrow
\frac12\left(\max(\{x_i:r_i\ge a\}\cup\{0\})\right)^2,
\]
the explicit joint-tail limit follows. For independent \(W_a\) with the displayed survival function, the condition \(\min(W_1,\ldots,W_{r_i})>x_i\) for all \(i\) is exactly \(W_a>\max_{i:r_i\ge a}x_i\) for each \(a\). Independence gives the same joint-tail function. Its coordinate marginals are continuous, so the multivariate survival convergence implies convergence in distribution.

**3. Exact discrete coincidence identity.** Fix \(1\le r<s\). The event \(M_r=M_s=j\) requires at least \(s\) nonoverlined occurrences of every \(i<j\), but fewer than \(r\) nonoverlined occurrences of \(j\). After removing \(s\) copies of each smaller part, the admissible generating factor for the multiplicity of \(j\) is \(1-q^{rj}\) relative to the unrestricted overpartition factor. Consequently,
\[
\#\{\pi\vdash N:M_r(\pi)=M_s(\pi)\}
=\sum_{j\ge1}\left[\bar p(N-sT_{j-1})-
\bar p(N-sT_{j-1}-rj)\right].\tag{1}
\]
The sum is finite, since \(\bar p(m)=0\) for negative \(m\).

**4. Local limit and tail control.** For any fixed \(K>0\), the analytic ratio from Step 2 applies uniformly for \(1\le j\le\lfloor KN^{1/4}\rfloor\), to both shifts in (1). By the mean-value expansion of the exponential,
\[
\frac{\bar p(N-sT_{j-1})-\bar p(N-sT_{j-1}-rj)}{\bar p(N)}
=e^{-\pi sT_{j-1}/(2\sqrt N)}
\frac{\pi rj}{2\sqrt N}+O_{K,r,s}(N^{-1/2}).
\]
Summing the error over \(O(N^{1/4})\) indices gives \(O(N^{-1/4})\). The main term is a Riemann sum, so
\[
\lim_{N\to\infty}\Pr(M_r=M_s\le KN^{1/4})
=\int_0^K\frac{\pi r x}{2}e^{-\pi sx^2/4}\,dx
=\frac rs\left(1-e^{-\pi sK^2/4}\right).
\]
The omitted event satisfies
\[
0\le\Pr(M_r=M_s>KN^{1/4})
\le\Pr(M_s>KN^{1/4})\longrightarrow e^{-\pi sK^2/4}.
\]
First let \(N\to\infty\), then \(K\to\infty\); the tail tends to zero. This proves the coincidence limit for every fixed \(r<s\).

## Verification
The standalone Python 3 script `verify.py`, requiring only the standard library, independently computes the overpartition numbers from their Euler product, enumerates every overpartition through weight 12 (including optional overlines), and checks 78 joint-tail identities and 39 coincidence identities. It also checks three finite convergence trends through weight 1600. Its expected output begins `PASS:` and explicitly distinguishes finite testing from the infinite proof. The exact finite identities are proved by bijection, the vector limit by a uniform overpartition-count ratio, and the coincidence limit by a locally uniform coefficient estimate plus a tail bound.

## Relationship to prior work
Aricheta and Donato [1] introduced precisely these overpartition least-\(r\)-gaps and established *one-index* generating functions and moment asymptotics. Their Proposition 2 is compatible with the one-threshold specialization of the exact identity above. The present claim concerns the entire fixed finite hierarchy simultaneously and, separately, the asymptotically nonzero probability of exact coincidences. Neither of those two statements appears in the inspected sections of [1]. The present proof uses an independently established quantitative overpartition-count estimate rather than relying on any unverified constant in [1]'s single-index moment asymptotic.

Wagner [2] proved Rayleigh and local limits for individual least gaps in **ordinary** integer partitions, not for the multivariate overpartition process or the diagonal coincidence probability. Sills [3] and Engel [4] provide the analytic coefficient estimates, not the gap statistics. Chern and Xia [5] study marginal moments for ordinary partitions, including congruence constraints. Other overpartition excludant work [6] treats aggregate parity and asymptotics, not the same joint random variables in its available abstract. These comparisons do not establish uniqueness of the theorem.

## Limitations
The convergence fixes every gap index and every threshold before taking \(N\to\infty\). No rates uniform in growing gap indices, higher-order coincidence corrections, or results for distinguished/overlined multiplicity thresholds are claimed. An unindexed multivariate partition-limit theorem might imply part or all of the result; the 2026 preprint [6] could not be inspected beyond its abstract. The finite verifier is corroboration only and provides no infinite certificate.

## References
[1] V. M. R. Aricheta and J. A. L. Donato, *Minimal Excludant over Overpartitions*, arXiv:2309.04398v1 (first public 8 September 2023), especially Definitions 1–2, Proposition 2, and Section 3. https://arxiv.org/pdf/2309.04398

[2] S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan Journal 25 (2011), 229–246; DOI:10.1007/s11139-010-9264-z. https://www.finanz.math.tugraz.at/~wagner/limitdist.pdf

[3] A. V. Sills, *A Rademacher Type Formula for Partitions and Overpartitions*, International Journal of Mathematics and Mathematical Sciences (2010), article 630458; DOI:10.1155/2010/630458.

[4] B. Engel, *Log-concavity of the overpartition function*, arXiv:1412.4603v2 (2014), especially the overpartition Rademacher formula and explicit main-term error in Sections 2–3. https://arxiv.org/pdf/1412.4603

[5] S. Chern and E. X. W. Xia, *Asymptotics for moments of the minimal partition excludant in congruence classes*, arXiv:2507.14431v1 (2025). https://arxiv.org/pdf/2507.14431

[6] D. Sarkar, M. P. Thejitha and S. N. Fathima, *A Note On Certain Minimal Excludants Over Overpartitions*, arXiv:2609.21649v1 (2026); full text not accessible during comparison.
