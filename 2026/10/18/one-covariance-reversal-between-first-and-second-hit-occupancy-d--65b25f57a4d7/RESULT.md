# One covariance reversal between first- and second-hit occupancy diversity

## Finding

Independently throw \(s\ge2\) labelled balls into \(b\ge2\) equiprobable boxes, with occupancies \(N_1,\ldots,N_b\). Define the two cumulative occupancy counts
\[
U_{b,s}=\sum_{i=1}^b\mathbf1_{\{N_i\ge1\}},\qquad
V_{b,s}=\sum_{i=1}^b\mathbf1_{\{N_i\ge2\}}.
\]
These are respectively the numbers of different categories seen once or more and seen twice or more. For every integer \(b\ge3\), put \(q=(b-1)/b\), \(r=(b-2)/b\), and define for real \(x\ge0\)
\[
H_b(x)=q^x+(b-1)r^x+\frac{(b-1)x}{b}r^{x-1}-bq^{2x}-xq^{2x-1}.
\]
There exists **exactly one** \(\xi_b>1\) satisfying \(H_b(\xi_b)=0\); in fact \(\xi_b>2\). At every integer \(s\ge2\),
\[
\operatorname{Cov}(U_{b,s},V_{b,s})=bH_b(s),\qquad
\begin{cases}
<0,&2\le s<\xi_b,\\
=0,&s=\xi_b,\\
>0,&s>\xi_b.
\end{cases}
\]
Thus the sign changes at most once as the number of balls increases, and the crossover is characterized by an explicit exponential polynomial—not a numerical conjecture.

The crossover is asymptotically universal:
\[
\boxed{\displaystyle\lim_{b\to\infty}\frac{\xi_b}{b}=\lambda_*},
\qquad e^{\lambda_*}=1+\lambda_*+\lambda_*^2,
\qquad \lambda_*\approx1.7932821329,
\]
where the displayed equation has a unique **positive** solution. Equivalently, if \(s_b/b\to\lambda\in(0,\infty)\) and \(\lambda\ne\lambda_*\), then for all sufficiently large \(b\) the covariance is negative when \(\lambda<\lambda_*\), and positive when \(\lambda>\lambda_*\).

For the two-box boundary, the exact signs are negative at \(s=2\), zero at \(s=3\), and positive at every \(s\ge4\). No assertion is made that \(\xi_b\) is nonintegral for \(b\ge3\).

## Assumptions and scope

The number of boxes \(b\) and the number of independently assigned balls \(s\) are integers in the stated ranges, all boxes have equal selection probability \(1/b\), and both random variables are evaluated at the **same fixed number** of balls. The real parameter \(x\) in \(H_b\) is an analytic interpolation of the exact covariance, not a randomized number of balls. This distinction is important: independently Poissonized box occupancies have nonnegative covariance for the two cumulative counts.

The theorem does not characterize the sign for unequal box probabilities, nor the full covariance matrix of exact occupancy frequencies.

## Proof

**Exact covariance.** Fix \(b\ge3\) and integer \(s\ge2\). Set \(u=q^s\), \(v=(s/b)q^{s-1}\), \(w=r^s\), and \(t=(s/b)r^{s-1}\). For a single box, its probabilities of being empty or a singleton are \(u\) and \(v\), so the probability that it has at least two balls is \(1-u-v\). For the same box, since the second-hit indicator implies its first-hit indicator,
\[
\operatorname{Cov}(\mathbf1_{\{N_i\ge1\}},\mathbf1_{\{N_i\ge2\}})
=u(1-u-v).
\]
For distinct boxes \(i\ne j\), taking complements of both indicators gives
\[
\begin{aligned}
\operatorname{Cov}(\mathbf1_{\{N_i\ge1\}},\mathbf1_{\{N_j\ge2\}})
&=\operatorname{Cov}(\mathbf1_{\{N_i=0\}},\mathbf1_{\{N_j\le1\}})\\
&=w+t-u(u+v).
\end{aligned}
\]
There are \(b\) diagonal and \(b(b-1)\) off-diagonal pairs; summation yields
\[
\operatorname{Cov}(U_{b,s},V_{b,s})
=b\bigl[u(1-u-v)+(b-1)(w+t-u(u+v))\bigr]=bH_b(s).
\]

**The real zero bound.** We use the elementary exponential-polynomial lemma: if \(a_1,\ldots,a_k\) are distinct real numbers and the nonzero real polynomials \(P_i\) have degrees \(d_i\), then \(\sum_iP_i(x)e^{a_ix}\), unless identically zero, has at most \(\sum_i(d_i+1)-1\) real zeros **counting multiplicity**. To prove this, order the exponents and divide by the exponential of the smallest exponent. Differentiation lowers the degree of that exponent's polynomial by one (or removes it), while retaining the other exponentials with polynomial coefficients of no greater degree. Rolle's theorem, including multiplicities, and induction on \(\sum_i(d_i+1)\) establish the claim. The base case is a nonzero constant times an exponential.

For \(b\ge3\), the three positive bases satisfy \(0<r<q^2<q<1\), because \(q^2-r=1/b^2\). In \(H_b\), the coefficients of \(r^x\) and \((q^2)^x\) are linear polynomials in \(x\), while that of \(q^x\) is constant. The lemma therefore bounds the total number of real zeros of \(H_b\), with multiplicity, by \(4\).

Direct substitution gives \(H_b(0)=H_b(1)=0\). Differentiating at the second root simplifies to
\[
H_b'(1)=q\bigl[(b-1)\log r-(2b-1)\log q\bigr]<0.
\]
For the strict inequality, write \(k=b-1\ge2\). Since \(r/q^2=1-1/k^2\),
\[
\left(\frac r{q^2}\right)^k
=\left(1-\frac1{k^2}\right)^k
<e^{-1/k}<\frac{k}{k+1}=q.
\]
Thus \(r^{b-1}<q^{2b-1}\), proving the asserted derivative sign. In particular \(H_b(x)<0\) immediately to the right of \(x=1\).

With exactly two balls, let \(I\) indicate that they choose the same box. Then \(U_{b,2}=2-I\), \(V_{b,2}=I\), and \(\Pr(I=1)=1/b\). Consequently
\[
H_b(2)=-\frac{b-1}{b^3}<0.
\]
As \(x\to\infty\), the term \(q^x\) dominates the other terms, so \(H_b(x)/q^x\to1\), and \(H_b(x)>0\) eventually. Thus at least one sign-changing zero lies in \((2,\infty)\).

There cannot be two distinct zeros in \((1,\infty)\). The zero-count lemma already accounts for \(0\) and \(1\). Starting with a negative sign immediately right of \(1\) and ending with a positive sign, two additional simple crossings would require a third crossing, making at least five real zeros in total. If one of the additional zeros did not change sign, its even multiplicity, together with the necessary sign-changing zero and the zeros at \(0,1\), would likewise require at least five. Hence there is exactly one zero \(\xi_b>2\), and its sign classification follows.

**Asymptotic threshold.** For fixed \(\lambda>0\), put \(x=\lambda b\). Uniformly for \(\lambda\) in a compact subset of \((0,\infty)\), Taylor expansion of \(\log(1-c/b)\) gives
\[
H_b(\lambda b)
=e^{-\lambda}-(1+\lambda+\lambda^2)e^{-2\lambda}+O(b^{-1}).
\]
The sign of the limiting function is the sign of \(g(\lambda)=e^\lambda-1-\lambda-\lambda^2\). The factorization
\[
\frac{g(\lambda)}{\lambda^2}
=-\frac12+\sum_{j=3}^{\infty}\frac{\lambda^{j-2}}{j!}
\]
shows that this quotient is strictly increasing from \(-1/2\) to \(+\infty\) for \(\lambda>0\), so its unique positive zero is \(\lambda_*\). By applying the uniform asymptotic formula at any two values \(0<\lambda_-<\lambda_*<\lambda_+\) and using the unique finite zero, for all sufficiently large \(b\)
\(\lambda_- b<\xi_b<\lambda_+ b\). This proves \(\xi_b/b\to\lambda_*\).

**Two boxes.** For \(b=2,s=2\), the covariance is \(-1/4\). At \(s=3\) every allocation has exactly one box with two or more balls, hence the covariance is zero. If \(s\ge4\), let \(A\) be the event that all balls choose the same box and \(B\) the event that both boxes receive at least two balls. Then \(A\cap B=\varnothing\), \(U_{2,s}=2-\mathbf1_A\), and \(V_{2,s}=1+\mathbf1_B\), so
\[
\operatorname{Cov}(U_{2,s},V_{2,s})
=\Pr(A)\Pr(B)
=2^{1-s}\left(1-\frac{2(s+1)}{2^s}\right)>0.
\]

## Verification

Run `python3 check_occupancy.py` with the Python standard library. It independently enumerates all labelled allocations for \(b=3,4,5,6\) and \(2\le s\le7\), checks the exact covariance against both algebraic forms, verifies the two-box boundary for \(2\le s\le10\), and tests exact rational covariance signs for \(3\le b\le31\) and \(2\le s\le5b+5\). It separately tests numerical derivative signs and a bracket for the asymptotic root. These finite and numerical tests do not establish either all-parameter uniqueness or the limit; those are proved analytically above.

## Relationship to prior work

Derbazi, Gnedin and Marynych (2023) study first- and higher-order record arrivals and prove point-process Poisson limits in the infinite occupancy scheme. Their full 2023 preprint discusses exact-count processes, multivariate approximations and de-Poissonization, but does not state this finite uniform **cumulative-count covariance sign reversal in the number of balls**.

Barbour and Gnedin (2008) establish joint approximations and covariance limits for exact occupancy-frequency counts in infinite unequal-frequency schemes; their scaling and objects differ from the simultaneous equal-box, fixed-ball cumulative counts here.

The publicly available result *A one-switch covariance law for occupancy richness and frequency counts* (2026) gives \(\operatorname{Cov}(K,K_r)\) for every exact frequency count \(K_r\) and a sign switch **as the frequency index \(r\) varies at fixed numbers of balls and boxes**. Summing those covariances for all \(r\ge2\) recovers the raw finite covariance in this result, so the identity alone is not claimed novel. The distinct assertion proved here is a **single reversal as the number of balls varies for fixed box count**, together with its uniqueness proof by exponential-polynomial zero counting and the sharp limiting load \(\lambda_*\). The published frequency-index sign switch by itself does not imply these properties.

## Limitations

The unique real threshold is established only for equal box probabilities. The possibility \(\xi_b\in\mathbb Z\) is not resolved for \(b\ge3\), so no unsupported strictness assertion is made at such an equality. The numerical approximation to \(\lambda_*\) is for convenience; only the defining exact equation is used in the proof. Classical occupancy covariance identities can subsume the algebraic formula; the scientific increment is the parameter-direction sign classification and asymptotic threshold. Unindexed literature may contain a comparable implicit or explicit zero-count argument. No independent audit has been performed.

## References

1. Z. Derbazi, A. Gnedin and A. Marynych, *Records in the Infinite Occupancy Scheme*, arXiv:2308.01739, first public 2023-08-03, primary MSC 60C05; https://arxiv.org/html/2308.01739v1.
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, first public 2008-09-25; https://arxiv.org/html/0809.4387v1.
3. *A one-switch covariance law for occupancy richness and frequency counts*, public research result dated 2026-10-04; https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
