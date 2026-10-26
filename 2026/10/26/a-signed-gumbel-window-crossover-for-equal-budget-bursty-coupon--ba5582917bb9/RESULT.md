# A signed Gumbel-window crossover for equal-budget bursty coupon collection

## Finding
For \(n\ge2\) coupon types, compare a fixed budget of one uniform independent coupon per round with a random budget of either zero or \(b\ge2\) independent coupons, where a nonempty round occurs with probability \(1/b\). Both policies draw one coupon per round on average. The random-budget policy has a strictly larger expected cover time but can finish earlier with strictly positive probability before the fixed policy can possibly finish. Their completion probabilities cross in the weak sense that their ordering reverses between early and late times, and the signed finite-size difference has an explicit universal Gumbel-window profile. Write \(F_1(t)\) and \(F_b(t)\) for the probabilities of completion by integer round \(t\). For each fixed integer \(b\ge2\), real \(x\), and \(t_n=\lfloor n\log n+nx\rfloor\),
\[
\lim_{n\to\infty}\frac{n}{\log n}\bigl(F_b(t_n)-F_1(t_n)\bigr)=\frac{b-1}{2}e^{-x}(e^{-x}-1)e^{-e^{-x}}.
\]
The limiting difference is positive for \(x<0\) and negative for \(x>0\). The exact finite-sample penalty is \(\mathbb E C_{n,b}-nH_n=\mathbb E[b\lceil T_n/b\rceil-T_n]\in(0,b-1)\), with \(\mathbb E C_{n,2}-nH_n=[1-(-1)^n/\binom{2n-1}{n}]/2\).

## Assumptions and scope
Fix integers \(n,b\ge2\). Draws are iid uniform from \(\{1,\ldots,n\}\); all batch occupancy is with replacement. In the fixed protocol one draw occurs each integer round, and \(T_n\) is the number of rounds until each coupon has appeared. In the burst protocol independent Bernoulli indicators of parameter \(1/b\) choose between \(b\) independent uniform draws and an empty round; its completion time is \(C_{n,b}\). All randomizations are independent. Write \(H_n=\sum_{j=1}^n 1/j\), and use \(0^0=1\) when defining time-zero probabilities. In the asymptotic statements \(b\) and \(x\) are fixed while \(n\to\infty\); no uniformity for growing \(b\) is asserted.

## Proof
**Exact distributions.** A fixed set of \(j\) coupon types is missed in one fixed round with probability \(1-j/n\); in one burst round its miss probability is \(a_b(j)=1-1/b+(1-j/n)^b/b\). Inclusion--exclusion therefore gives, for every integer \(t\ge0\),
\[
F_1(t)=\sum_{j=0}^n(-1)^j\binom nj(1-j/n)^t,\qquad
F_b(t)=\sum_{j=0}^n(-1)^j\binom nj a_b(j)^t.
\]
**Mean and residue law.** Put one iid uniform infinite coupon tape behind both policies, independently of the burst indicators. The ordinary cover time \(T_n\) is the number of tape draws required. The burst collector needs exactly \(R=\lceil T_n/b\rceil\) nonempty rounds; conditional on \(T_n\), the expected round of the \(R\)-th Bernoulli success is \(bR\). Thus
\[
\mathbb E C_{n,b}=\mathbb E[b\lceil T_n/b\rceil]=nH_n+\Delta_{n,b},\quad
\Delta_{n,b}=\mathbb E[(b-(T_n\bmod b))\bmod b].
\]
The classical waiting-time decomposition \(T_n=\sum_{j=1}^n G_j\) has independent geometric variables on positive integers with success parameters \(j/n\); it yields \(\mathbb E T_n=nH_n\). The distribution of \(T_n\) assigns positive probability to every integer \(k\ge n\), hence the rounding residual is not almost surely zero and is not almost surely \(b-1\); therefore \(0<\Delta_{n,b}<b-1\). For \(b=2\), the residual equals the indicator that \(T_n\) is odd. The geometric probability generating function gives
\[
\mathbb E[(-1)^{T_n}]=\prod_{j=1}^n\frac{-j/n}{2-j/n}=\frac{(-1)^n}{\binom{2n-1}{n}},
\]
so the claimed parity formula follows. For fixed \(b\), each nontrivial \(b\)-th root of unity \(\zeta\) satisfies
\[
|\mathbb E[\zeta^{T_n}]|=\prod_{j=1}^n\frac{j/n}{|1-(1-j/n)\zeta|}\le\rho_b^{\lfloor n/2\rfloor-\lceil n/4\rceil},
\]
where \(\rho_b<1\) is the maximum of the displayed single-factor ratio over \(j/n\in[1/4,1/2]\) and all \(\zeta\ne1\) with \(\zeta^b=1\). Fourier inversion on residues shows \(\Pr(T_n\bmod b=r)=1/b+O_b(e^{-c_b n})\), proving \(\Delta_{n,b}=(b-1)/2+O_b(e^{-c_b n})\).

**Early and late crossings.** For \(t=n-1\), the fixed protocol cannot cover \(n\) coupons, while the burst protocol can have \(n-1\) nonempty batches and cover all coupon types among their \(b(n-1)\ge n\) draws, an event of positive probability. For fixed \(n,b\), write \(\alpha=1-1/n\) and \(\beta=1-1/b+(1-1/n)^b/b\). The strict Bernoulli inequality implies \(0<\alpha<\beta<1\). For either protocol its missing-one inclusion--exclusion term dominates the others exponentially at large \(t\): \(1-F_1(t)\sim n\alpha^t\) and \(1-F_b(t)\sim n\beta^t\). Consequently \(F_b(t)<F_1(t)\) for all sufficiently large \(t\). This proves stochastic-order incomparability, not a claim of a unique finite crossing.

**Signed critical-window expansion.** Put \(t_n=\lfloor n\log n+nx\rfloor\). For each fixed \(j\ge1\), Taylor expansion at \(z=j/n=0\) gives
\[
\log\!\left(1-\frac1b+\frac{(1-z)^b}b\right)-\log(1-z)=\frac{b-1}2z^2+O_b(z^3).
\]
Hence, writing \(c_1(j)=1-j/n\) and \(c_b(j)=a_b(j)\),
\[
\frac n{\log n}\binom nj\bigl(c_b(j)^{t_n}-c_1(j)^{t_n}\bigr)\longrightarrow\frac{b-1}2\frac{j^2e^{-jx}}{j!}.
\]
We justify summing these signed differences, rather than assuming pointwise convergence suffices. Let \(J_n=\lceil 4\log n/\log\log n\rceil\) for large \(n\). For the number of missing coupons \(U\), Bonferroni bounds the error in truncating \(\Pr(U=0)=\sum_{j\ge0}(-1)^j\mathbb E\binom Uj\) at \(J_n\) by \(\mathbb E\binom U{J_n+1}\). For each protocol this is \(\binom n{J_n+1}c_i(J_n+1)^{t_n}\le e^{C_x(J_n+1)}/(J_n+1)!\), because the logarithms above show \(\log c_i(j)\le-j/n+O_b(j^2/n^2)\) uniformly for \(j\le J_n+1\), and \(J_n^2\log n/n\to0\). Stirling's bound makes each truncation error \(o(\log n/n)\). The same expansions, using \(\binom nj c_1(j)^{t_n}\le e^{C_xj}/j!\), bound the absolute scaled summands uniformly for \(j\le J_n\) by \(C_{b,x}j^2e^{C_xj}/j!\), a summable sequence. Dominated convergence then yields
\[
\frac{b-1}2\sum_{j=0}^\infty(-1)^j\frac{j^2e^{-jx}}{j!}
=\frac{b-1}2 e^{-x}(e^{-x}-1)e^{-e^{-x}},
\]
using \(\sum_{j\ge0}(-1)^jz^j/j!=e^{-z}\) and two differentiations. The signs on each side of \(x=0\) follow.

## Verification
The accompanying standalone `verify.py` performs exact-rational checks from an independent finite-state recursion against inclusion--exclusion for \(2\le n\le6\), \(2\le b\le4\), \(0\le t\le10\); compares two independent exact-rational computations of the full expected cover time; checks early noncomparability; and confirms the parity formula for \(2\le n\le40\). It reports 249 passed assertions. This finite verification corroborates, but does not replace, the all-parameter analytic argument.

## Relationship to prior work
Kobza, Jacobson and Vaughan (2007) survey random-sample-size coupon collection and give general Markov-chain methods for cover-time distributions and expectations. Thus mere computation of a cover-time expectation or CDF by a finite Markov chain is not claimed as new. Betken and Thäle (2022) study fixed-size, without-replacement group drawings and quantitative Gaussian/Poisson approximation for missing coupons, not equal-mean zero-or-\(b\) with-replacement batch comparison. The contribution assessed here is the **combined exact mean-penalty and stochastic incomparability classification, especially the signed leading \(\log n/n\) difference in the coupon-collector critical window**. These comparisons do not establish exhaustive historical priority.

## Limitations
The critical-window expansion holds for each fixed integer \(b\), not a growing-batch regime. It does not claim a unique finite-time crossing or uniform error in \(x\). Literature on arbitrary random-sized coupon drawings is broad, and an inaccessible full text of the 2007 survey may contain relevant specializations; prior work may imply some finite formulas. Independent historical-priority validation is not performed.

## References
1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485v1, first posted 2022-02-15, https://arxiv.org/abs/2202.07485.
2. J. E. Kobza, S. H. Jacobson and D. E. Vaughan, *A survey of the coupon collector's problem with random sample sizes*, Methodology and Computing in Applied Probability 9 (2007), 573–584, https://doi.org/10.1007/s11009-006-9013-3.
3. M. Ferrante and N. Frigo, *A note on the coupon-collector's problem with multiple arrivals and the random sampling*, arXiv:1209.2667 (2012), https://arxiv.org/abs/1209.2667.
