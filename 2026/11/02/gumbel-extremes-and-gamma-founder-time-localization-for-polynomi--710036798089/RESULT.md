# Gumbel extremes and Gamma founder-time localization for polynomially immigrating critical branching clans

## Finding
Fix real constants \(c>0\) and \(\alpha>0\). At each integer time \(k\ge1\), introduce exactly \(b_k=\lfloor c k^\alpha\rfloor\) immigrants, with each immigrant founding a distinct clan. Every individual in every subsequent generation independently produces a number of children with probability \(\Pr(\xi=j)=2^{-j-1}\), \(j=0,1,2,\ldots\). Let \(Z^{(k,j)}_t\) be the size of the clan founded by immigrant \(j\) at time \(k\), after \(t\) generations, and let
\[
M_n=\max_{1\le k\le n}\max_{1\le j\le b_k}Z^{(k,j)}_{n-k}.
\]
Define the unique positive number \(\lambda_n\) by
\[
\lambda_n^{\alpha+1}e^{\lambda_n}=c\Gamma(\alpha+1)n^\alpha.
\]
If \(J_n\) denotes the earliest immigration time among clans attaining \(M_n\), then
\[
\left(\frac{M_n}{n}-\lambda_n,\frac{J_n\lambda_n}{n}\right)
\Rightarrow (G,U),
\]
where \(G\) has standard Gumbel distribution \(\Pr(G\le x)=e^{-e^{-x}}\), \(U\) has Gamma distribution with shape \(\alpha+1\) and rate \(1\), and \(G\) and \(U\) are independent. The probability of a tie for the largest clan tends to zero. More precisely, the point process of rescaled clan sizes and founder times converges above each fixed size threshold to the Poisson point process on \((0,\infty)\times\mathbb R\) with intensity
\[
\frac{u^\alpha e^{-u}}{\Gamma(\alpha+1)}\,du\; e^{-x}\,dx.
\]
The centering has the explicit expansion
\[
\lambda_n=\alpha\log n-(\alpha+1)\log\log n+
\log\!\left(\frac{c\Gamma(\alpha+1)}{\alpha^{\alpha+1}}\right)+o(1).
\]
If \(S_n\) is the total population at time \(n\), then
\[
\frac{S_n}{n^{\alpha+1}}\longrightarrow \frac{c}{\alpha+1}
\quad\text{in }L^2,
\qquad
\frac{n^\alpha}{\log n}\frac{M_n}{S_n}
\longrightarrow \frac{\alpha(\alpha+1)}c
\quad\text{in probability}.
\]
The second ratio is understood on \(S_n>0\), an event of probability tending to one. Thus the largest clan is unusually large but still an asymptotically vanishing fraction of the population.

## Assumptions and scope
All \(\xi\) variables for every individual, generation, and immigrant are mutually independent; immigration counts are deterministic, and there are no deaths or movements except through reproduction. The reference time \(n\) is an integer tending to infinity, with fixed \(c,\alpha\). Distinct immigrants, including immigrants born at the same time, define distinct clans. A generation-zero clan has size one. Ties for \(M_n\) are broken by earliest founder time (and then arbitrary immigrant index). The theorem does not treat \(\alpha=0\), which is a different extremal regime, nor a common random environment, offspring distributions other than the specified critical geometric law, or a joint limit in which \(c\) or \(\alpha\) changes with \(n\). The primary subject is branching-process genealogy (MSC 60J80).

## Proof
**1. Exact single-clan law.** The offspring probability-generating function is \(f(s)=(2-s)^{-1}\). Direct induction gives, for every integer \(t\ge0\),
\[
f^{\circ t}(s)=\frac{t-(t-1)s}{t+1-ts}.
\]
For \(t\ge1\), the size \(Z_t\) of a one-founder clan therefore has \(\Pr(Z_t=0)=t/(t+1)\) and
\[
q_t(h):=\Pr(Z_t\ge h)=\frac1{t+1}
\left(\frac{t}{t+1}\right)^{h-1},\qquad h=1,2,\ldots.
\]
Consequently, for integer \(h\ge2\), independence of families yields the **exact finite-time identity**
\[
\Pr(M_n<h)=\prod_{k=1}^{n-1}(1-q_{n-k}(h))^{b_k}.
\]
The last cohort at time \(n\) has size one and hence does not affect thresholds \(h\ge2\).

**2. Location-marked exceedance intensities.** Since \(\lambda_n\to\infty\), \(\lambda_n=O(\log n)\), and
\[
\frac{c n^\alpha e^{-\lambda_n}}{\lambda_n^{\alpha+1}}
=\frac1{\Gamma(\alpha+1)},
\]
fix any real \(x\) and set \(h_n(x)=\lceil n(\lambda_n+x)\rceil\). Put \(u_{k,n}=k\lambda_n/n\). Uniformly for \(u_{k,n}\) in a fixed compact subset of \((0,\infty)\), we have \(k=o(n)\) and, by the exact formula,
\[
q_{n-k}(h_n(x))=\frac1n\exp(-\lambda_n-x-u_{k,n}+o(1)).
\]
Here the term \(-u_{k,n}\) arises from the additional age penalty
\(n(\lambda_n+x)/(n-k)-(\lambda_n+x)\). Also \(b_k\sim c k^\alpha\) uniformly on the same compact windows. Riemann sums with step \(\lambda_n/n\) give, for every interval \(A\subset(0,\infty)\) with finite positive endpoints,
\[
\sum_{k:u_{k,n}\in A}b_kq_{n-k}(h_n(x))
\longrightarrow e^{-x}\int_A\frac{u^\alpha e^{-u}}{\Gamma(\alpha+1)}\,du.
\]

**3. No hidden early or late founders.** For \(1\le k\le n/2\), the exact tail and \((1-y)^{h-1}\le e^{-(h-1)y}\) give, for all large \(n\), an envelope of the form
\[
q_{n-k}(h_n(x))\le \frac{C_x}{n}e^{-\lambda_n}e^{-u_{k,n}/2}.
\]
Thus the total expected exceedances over \(k\le\delta n/\lambda_n\) tend to at most \(C\int_0^\delta u^\alpha du\), and over \(R n/\lambda_n\le k\le n/2\) to at most \(C\int_R^\infty u^\alpha e^{-u/2}du\). Both vanish in the respective limits \(\delta\downarrow0\) and \(R\uparrow\infty\). For \(k\ge n/2\), \(q_{n-k}(h_n(x))\) is bounded by \(q_{\lfloor n/2\rfloor}(h_n(x))\) when \(n\) is large because \(h_n(x)>n+1\) and the function \(y(1-y)^{h-1}\) decreases for \(y>1/h\). Thus the remaining contribution is
\[
O(n^\alpha e^{-2\lambda_n})
=O\!\left(n^{-\alpha}\lambda_n^{2\alpha+2}\right)=o(1).
\]
The compact-window intensity therefore exhausts all founders, giving the limiting intensity \(e^{-x}\) on all \((0,\infty)\).

**4. Poisson process and unique leader.** For fixed \(x\), each immigrant contributes an independent Bernoulli indicator of an exceedance above \(h_n(x)\). Since \(h_n(x)>n+1\), the same monotonicity gives
\[
\max_{1\le t\le n}q_t(h_n(x))
\le q_n(h_n(x))=O(n^{-1}e^{-\lambda_n})=o(1).
\]
The sum of squared Bernoulli probabilities is bounded by this maximum times the total exceedance intensity and hence tends to zero. The law of small numbers, applied also to disjoint founder windows and disjoint rescaled-height intervals, proves Poisson point-process convergence on every region above a fixed height threshold. The density in height is \(e^{-x}dx\), as follows by differencing the limiting exceedance intensities at two thresholds. Exhaustion from Step 3 ensures no escaped founder can win. The limiting point process has a unique largest point almost surely, so the continuous mapping theorem gives the joint maximum/location limit and shows the probability of a discrete tie for the original maximum tends to zero. By factorization of the intensity into a probability density in founder position and \(e^{-x}dx\) in height, its top point has independent Gamma-distributed founder mark and Gumbel height.

**5. Explicit centering and population share.** Taking logs of the centering equation gives \(\lambda_n+(\alpha+1)\log\lambda_n=\alpha\log n+\log(c\Gamma(\alpha+1))\). First \(\lambda_n/\log n\to\alpha\); substitution into the logarithm then yields the stated \(o(1)\)-accurate centering. The exact offspring mean and variance are \(1\) and \(2\). For a critical one-founder population, \(\mathbb EZ_t=1\) and \(\operatorname{Var}(Z_t)=2t\), by the conditional-variance recursion. Consequently
\[
\mathbb ES_n=\sum_{k=1}^n b_k\sim\frac{c}{\alpha+1}n^{\alpha+1},
\qquad
\operatorname{Var}(S_n)=2\sum_{k=1}^n b_k(n-k)
\sim\frac{2c}{(\alpha+1)(\alpha+2)}n^{\alpha+2}.
\]
Since \(\alpha>0\), variance divided by the square of the leading population scale tends to zero. This proves the \(L^2\) law of large numbers. The Gumbel limit implies \(M_n/(n\log n)\to\alpha\) in probability; division by the population law proves the claimed leading-clan fraction.

## Verification
The standalone `checker.py` uses only the Python standard library. It checks the iterated generating-function identity at rational arguments, rational tail probabilities and moments, exact product/Poisson comparison bounds, and numerical solutions of the centering equation, for 3,214 assertions. Re-run as `python3 checker.py` from the package's extracted directory. The accompanying `verification_output.txt` records the actual run. These finite calculations are supplementary: Steps 1–5 above supply the infinite-population proof. The numerical rates can converge slowly due to terms of order \(1/\log n\), and no finite example is represented as an asymptotic certificate.

## Relationship to prior work
Barczy and Bezdány (2026, arXiv:2609.18503, initial submission September 16, 2026) study aggregate functional scaling limits for branching processes with inhomogeneous immigration; their Theorem 3.3 produces integrated immigration limits, not an extremal immigrant-clan point process. Their subsequent October 29 paper (arXiv:2610.39771, Theorem 3.1) treats deterministic aggregate scaling, likewise without maximum-clan or founder-location statistics. Mitov, Pakes, and Yanev (2003, arXiv:math/0312510, §§2 and 4) prove geometric-row extreme-value results and study the maximum **number of direct offspring of a particle** within a generation, not the maximum number of extant descendants of one of differently aged immigrant founders. Their zero-modified geometric asymptotics are relevant background, but the heterogeneous-age Laplace saddle, Gamma founder-time marking, and population-share normalization here are additional steps. Smadi and Vatutin (2021, arXiv:2109.13315, §§1 and 3–5) study the size of a clan **conditional on that clan being the only surviving clan** in a common random environment; this does not establish the unconditional largest-clan limit with deterministic polynomial immigration. Another model of independent nonextinguishing founders with random fitness (Fontes and Schinazi, arXiv:2610.29759) yields a different leader regime and does not imply the critical extinction-based theorem here.

## Limitations
This is a special but natural critical geometric offspring model, not an arbitrary finite-variance offspring universality theorem. The \(\alpha>0\) assumption is essential for the displayed centering and concentration; the constant-immigration endpoint needs different scaling. The total-population concentration is in \(L^2\), not asserted almost surely. No finite-\(n\) optimal error bound or model with shared random environments is claimed. Priority comparisons address the examined literature and accessible records, not an exhaustive proof of novelty; in particular, older implicit extreme-value theorems for nonidentical geometric triangular arrays remain a residual historical risk. No independent mathematical audit has been carried out.

## References
1. M. Barczy and D. Bezdány, *Functional limit theorems for Galton–Watson processes with inhomogeneous immigration*, arXiv:2609.18503, first posted 2026-09-16, https://arxiv.org/html/2609.18503v2.
2. M. Barczy and D. Bezdány, *Functional limit theorems for Galton–Watson processes with inhomogeneous immigration towards a deterministic limit function*, arXiv:2610.39771, first posted 2026-10-29, https://arxiv.org/html/2610.39771v1.
3. K. V. Mitov, A. G. Pakes, and G. P. Yanev, *Extremes of geometric variables with applications to branching processes*, arXiv:math/0312510, 2003, https://arxiv.org/html/math/0312510v1.
4. C. Smadi and V. A. Vatutin, *Critical branching processes in random environment with immigration: the size of the only surviving family*, arXiv:2109.13315, 2021, https://arxiv.org/abs/2109.13315.
5. G. P. Yanev and C. P. Tsokos, *Family size order statistics in branching processes with immigration*, Stochastic Analysis and Applications 18 (2000), 655–670, https://doi.org/10.1080/07362990008809690.
6. L. R. G. Fontes and R. B. Schinazi, independent-founder branching model, arXiv:2610.29759, 2026, https://arxiv.org/abs/2610.29759.
