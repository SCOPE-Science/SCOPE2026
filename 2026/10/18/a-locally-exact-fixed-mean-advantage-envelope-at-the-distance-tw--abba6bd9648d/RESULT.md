# A locally exact fixed-mean advantage envelope at the distance-two Bernoulli reversal threshold

## Finding

Let \(k\ge1\) be an integer and \(S\) be any finite sum of independent Bernoulli variables, with probabilities in \([0,1]\) and mean \(\mu\). Define the sharp **signed advantage**
\[
A_k(\mu)=\sup_{\mathbb ES=\mu}\left\{\Pr(S=k+2)-\Pr(S=k)\right\}.
\]
Define the integer \(d_k\), threshold \(\mu_k\), and trial count \(m_k\) by
\[
d_k=\max\left\{2,\left\lfloor\frac{9+\sqrt{8k+33}}8\right\rfloor\right\},\qquad m_k=k+d_k,
\]
\[
\mu_k=k+\frac{d_k\sqrt{(k+1)(k+2)}-k\sqrt{d_k(d_k-1)}}{\sqrt{(k+1)(k+2)}+\sqrt{d_k(d_k-1)}}.
\]
**Theorem.** For each fixed \(k\ge1\) there is a positive \(\varepsilon_k\) such that for all \(\mu\in(\mu_k-\varepsilon_k,\mu_k+\varepsilon_k)\),
\[
A_k(\mu)=\binom{m_k}{k+2}\left(\frac\mu{m_k}\right)^{k+2}\left(1-\frac\mu{m_k}\right)^{m_k-k-2}-\binom{m_k}{k}\left(\frac\mu{m_k}\right)^k\left(1-\frac\mu{m_k}\right)^{m_k-k}.
\]
In particular, with \(q_k=\mu_k/m_k\) and \(c_k=\Pr(\operatorname{Bin}(m_k,q_k)=k)\),
\[
A_k(\mu_k)=0,\qquad A_k'(\mu_k)=\frac{2c_k}{m_kq_k(1-q_k)}>0.
\]
Thus, not only the sign-change threshold but the **maximal signed size of the reversal** is known exactly on a two-sided neighborhood. The radius need not be uniform in \(k\).

## Assumptions and scope

The supremum is over all *finite* independent Bernoulli sums of arbitrary finite length, including deterministic trials. Fixed \(k\ge1\). The source theorem supplies the formula for \(\mu_k\), proves \(k<\mu_k<k+1\), and establishes the unique shifted-binomial equality case at \(\mu_k\). Those are **prior results**, not proved as new here. No claim for \(k=0\), where the source has nonunique boundary ties.

## Proof

**1. Reduction to an enumerable family.** For each fixed number of Bernoulli coordinates, the signed advantage is a symmetric multi-affine function of their parameters. The Chebyshev–Hoeffding fixed-mean reduction (as proved in Lemma 4 of Kleiner) says the maximum at a specified mean is attained by a shifted binomial
\[
S=\ell+\operatorname{Bin}(r,(\mu-\ell)/r),
\]
where \(\ell\) and \(r\) are nonnegative integers, \(r\ge1\), and the parameter belongs to \([0,1]\). Since the interval of means under consideration can be chosen inside \((k,k+1)\), every feasible shift satisfies \(0\le\ell\le k\). Set \(s=k-\ell\). For each feasible pair define
\[
f_{\ell,r}(\mu)=\Pr\left(\operatorname{Bin}(r,(\mu-\ell)/r)=s+2\right)-\Pr\left(\operatorname{Bin}(r,(\mu-\ell)/r)=s\right),
\]
interpreting out-of-support masses as zero. Then \(A_k(\mu)\) is the supremum of these functions, plus deterministic laws; deterministic laws are impossible for a noninteger \(\mu\).

**2. An actual gap over every rival.** At \(\mu=\mu_k\), source Proposition 7 and the exact threshold theorem show that the only zero among the feasible shifted-binomial functions is \(f_{0,m_k}(\mu_k)=0\); all others are strictly negative. We must prove their supremum is *strictly* negative, since the index set is infinite. Fix a shift \(\ell\in\{0,\ldots,k\}\). As \(r\to\infty\), \(\operatorname{Bin}(r,(\mu_k-\ell)/r)\) tends to \(\operatorname{Pois}(\lambda_\ell)\), where \(\lambda_\ell=s+\Delta_k\). Thus
\[
\lim_{r\to\infty} f_{\ell,r}(\mu_k)=e^{-\lambda_\ell}\frac{\lambda_\ell^s}{s!}\left(\frac{\lambda_\ell^2}{(s+1)(s+2)}-1\right)<0.
\]
The inequality holds because \(0<\Delta_k<1\), so \(\lambda_\ell<s+1<\sqrt{(s+1)(s+2)}\). There are finitely many shifts, and only finitely many small \(r\) after removing the large-\(r\) tails. Strict negativity of each nonexceptional small-\(r\) value therefore yields a **uniform negative rival gap** \(\gamma_k>0\).

**3. Uniform neighborhood, not merely pointwise continuity.** For fixed \(\ell\), the binomial-to-Poisson convergence is uniform as \(\mu\) varies in a compact neighborhood of \(\mu_k\). Indeed the binomial's parameter is \(\lambda/r\) with \(\lambda=\mu-\ell\) confined to a compact positive interval; the standard coupling bound is at most \(2\lambda^2/r\) in total variation. Consequently all large-\(r\) rival functions remain below a common negative number on a sufficiently small neighborhood. The finitely many remaining rival functions are continuous there, so they also remain negative. In contrast \(f_{0,m_k}(\mu_k)=0\), and it remains arbitrarily close to zero near the boundary. Shrinking the neighborhood again makes \(f_{0,m_k}\) larger than every rival. The fixed-mean reduction of Step 1 now gives \(A_k(\mu)=f_{0,m_k}(\mu)\) throughout that neighborhood. The optimization over arbitrary *finite* lengths is thus controlled, not replaced by a finite enumeration.

**4. Sensitivity formula.** For \(B\sim\operatorname{Bin}(m,\mu/m)\), differentiation gives
\[
\frac{d}{d\mu}\Pr(B=j)=\Pr(B=j)\frac{j-\mu}{m(\mu/m)(1-\mu/m)}.
\]
The two masses at \(k\) and \(k+2\) agree at \(\mu=\mu_k\), each equal to \(c_k>0\). Subtracting their derivatives gives the stated exact positive slope. Hence the envelope crosses linearly, with both one-sided derivatives equal.

## Verification

The companion `verify.py` independently evaluates the source's explicit \(d_k\) and \(\mu_k\), checks the unique best shifted-binomial crossing value against a finite rival grid for seven values of \(k\), and compares the analytic slope against a centered difference. These are finite sanity checks. The infinite-family conclusion depends on the strict Poisson-limit bound and the compactness argument in the proof, **not** on enumeration.

## Relationship to prior work

Kleiner (2026), arXiv:2610.10664v1, provides the exact distance-two reversal threshold, the shifted-binomial reduction, and the unique boundary equality case. This theorem *retains* all of those as prior work. The additional claim is equality of a **global fixed-mean maximum-value function** with a concrete binomial expression throughout an open two-sided neighborhood, plus the exact first-order sensitivity of that maximum. Boundary uniqueness alone does not imply such a neighborhood on the noncompact collection of all finite trial counts; the uniform Poisson-gap argument is the added step. Searches of targeted mathematical records found no matching local-envelope assertion. This absence is not proof of priority.

## Limitations

The neighborhood radius is existential rather than presented as a sharp numerical value; it can in principle be certified by finite comparisons plus a uniform Poisson approximation. Only fixed positive integer \(k\) and means sufficiently close to the published threshold are covered. No global fixed-mean envelope away from the crossing, no uniform-in-\(k\) neighborhood, and no uniqueness assertion for arbitrary non-reduced parameter vectors near the boundary is claimed. Potential priority overlap with older fixed-mean extremal inequalities remains a risk; independent audit has not been performed.

## References

1. I. Kleiner, *Why Distance Two Is Exceptional for Poisson–Binomial Point Probabilities*, arXiv:2610.10664v1 (first publicly posted 2026-10-07), Sections 2, 3, 5–7; https://arxiv.org/html/2610.10664v1.
2. W. Hoeffding, *On the distribution of the number of successes in independent trials*, Ann. Math. Statist. 27 (1956). The fixed-mean extremal principle is cited via Kleiner; its complete text was **not** independently inspected for this claim.
