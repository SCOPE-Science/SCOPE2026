# Sharp rare-Poisson obstruction to balanced thinning of centered sums

## Finding

For each fixed \(\lambda>0\) and integer \(n>\lambda\), independently sample \(\xi_{n,i}\sim\operatorname{Bernoulli}(\lambda/n)\) and \(B_{n,i}\sim\operatorname{Bernoulli}(1/2)\), for \(1\le i\le n\), with all selectors independent of all spikes. Write \(X_{n,i}=\xi_{n,i}-\lambda/n\) and

\[Q_n(\lambda)=\frac{\mathbb E|\sum_{i=1}^n B_{n,i}X_{n,i}|}{\mathbb E|\sum_{i=1}^n X_{n,i}|}.\]

Then the denominator is positive and

\[\lim_{n\to\infty}Q_n(\lambda)=R(\lambda):=\frac{\mathbb E|P_{\lambda/2}-\lambda/2|}{\mathbb E|P_\lambda-\lambda|},\]

where \(P_t\sim\operatorname{Pois}(t)\). The **sharp rare-event supremum** is

\[\sup_{\lambda>0}R(\lambda)=R(1)=\frac{\sqrt e}{2}=0.824360635350064\ldots,\]

and \(\lambda=1\) is its **unique maximizer**. As \(\lambda\downarrow0\), the ratio tends to \(1/2\); as \(\lambda\to\infty\), it tends to \(1/\sqrt2\).

It follows that in every universal centered Bernoulli-thinning estimate of the form

\[\mathbb E\left|\sum_i B_i Z_i\right|\le C\sqrt q\;\mathbb E\left|\sum_i Z_i\right|\]

for independent centered bounded summands and independent \(\operatorname{Bernoulli}(q)\) selectors, the constant must satisfy \(C\ge\sqrt{e/2}=1.1658219908\ldots\). This is a lower bound on the best universal constant, **not** a determination of that constant.

## Assumptions and scope

All random variables in each row are mutually independent except for the products within each selected summand. The intensity \(\lambda\) is fixed while \(n\) increases; the thinning fraction is exactly \(1/2\). The family contains bounded iid two-point centered summands and is a natural sparse counterpart to Gaussian-scale or symmetric-sign thinning. Optimization is over every real intensity \(\lambda>0\), not merely over integer intensities. The source's independently centered thinning theorem is broader; the present result only addresses the absolute-moment test function and one explicit rare-event family.

## Proof

**1. Triangular-array limit.** Define \(K_n=\sum_i\xi_{n,i}\), \(A_n=\sum_i B_{n,i}\xi_{n,i}\), and \(M_n=\sum_i B_{n,i}\). Then \(K_n\sim\operatorname{Bin}(n,\lambda/n)\to P_\lambda\), while \(A_n\sim\operatorname{Bin}(n,\lambda/(2n))\to P_{\lambda/2}\). By the law of large numbers, \(M_n/n\to1/2\) in probability. Consequently the unthinned sum \(K_n-\lambda\) converges in distribution to \(P_\lambda-\lambda\), and the thinned sum \(A_n-\lambda M_n/n\) converges in distribution to \(P_{\lambda/2}-\lambda/2\). Their variances are respectively \(\lambda(1-\lambda/n)\) and \(\lambda(1-\lambda/n)/2\), so the sequences have uniformly bounded second moments and hence uniformly integrable absolute values. Therefore both expected absolute values converge. The positive denominator follows from \(0<\lambda/n<1\).

**2. Explicit Poisson ratio.** For \(P_t\sim\operatorname{Pois}(t)\), centering and the identity \(k\Pr(P_t=k)=t\Pr(P_t=k-1)\) yield

\[\mathbb E|P_t-t|=2t\Pr(P_t=\lfloor t\rfloor)=\frac{2e^{-t}t^{\lfloor t\rfloor+1}}{\lfloor t\rfloor!}.\]

Thus

\[R(\lambda)=\frac12 e^{\lambda/2}\frac{(\lambda/2)^{\lfloor\lambda/2\rfloor}}{\lfloor\lambda/2\rfloor!}\frac{\lfloor\lambda\rfloor!}{\lambda^{\lfloor\lambda\rfloor}}.\]

Although floors jump at integer intensities, the probabilities of the two adjacent modes coincide there. Therefore \(R\) is continuous at all positive integers.

**3. Reduction of the global maximum to integer intensities.** On each open interval between consecutive integers \(m\) and \(m+1\), the integers \(a=\lfloor\lambda/2\rfloor\) and \(b=\lfloor\lambda\rfloor\) are constant. Hence

\[\frac{d^2}{d\lambda^2}\log R(\lambda)=\frac{b-a}{\lambda^2}\ge0.\]

Therefore \(\log R\) is convex on every such interval and can have no value exceeding the greater of its endpoint values. On \((0,1)\), the exact formula is \(R(\lambda)=e^{\lambda/2}/2\), strictly increasing. The global supremum is consequently controlled by integer intensities and the limit at infinity.

**4. Every integer other than one is strictly suboptimal.** Put \(p_t(k)=e^{-t}t^k/k!\), and use Robbins's explicit Stirling bounds, which imply for integers \(j,m\ge1\)

\[p_j(j)<\frac1{\sqrt{2\pi j}},\qquad p_m(m)>\frac{e^{-1/(12m)}}{\sqrt{2\pi m}}.\]

At an even integer \(\lambda=2j\), \(j\ge1\),

\[R(2j)=\frac12\frac{p_j(j)}{p_{2j}(2j)}<\frac{\sqrt2}{2}e^{1/(24j)}\le\frac{\sqrt2}{2}e^{1/24}<\frac{\sqrt e}{2}.\]

For odd \(\lambda=2j+1\), \(j\ge1\), one has

\[p_{j+1/2}(j)=p_j(j)e^{-1/2}(1+1/(2j))^j<p_j(j).\]

When \(j\ge2\), this gives

\[R(2j+1)<\frac12\sqrt{\frac{2j+1}{j}}e^{1/(12(2j+1))}\le\frac12\sqrt{5/2}e^{1/60}<\frac{\sqrt e}{2}.\]

Both final strict comparisons are elementary: \(2e^{1/12}<24/11<e\) and \((5/2)e^{1/30}<75/29<e\), by \(e^x\le(1-x)^{-1}\) for \(0\le x<1\) and \(e>65/24\). For the one remaining odd integer \(\lambda=3\), the exact value is \(R(3)=e^{3/2}/6<\sqrt e/2\), since \(e<3\). At \(\lambda=1\), \(R(1)=\sqrt e/2\). Finally the local Poisson mass asymptotic \(\Pr(P_t=\lfloor t\rfloor)\sim(2\pi t)^{-1/2}\) implies \(R(\lambda)\to1/\sqrt2\) as \(\lambda\to\infty\). The endpoint reductions and strict inequalities establish the unique global optimizer.

**5. Consequence for universal thinning.** Apply any proposed universal \(C\sqrt q\) inequality at \(q=1/2\) to the bounded iid centered variables in Step 1; pass to the limit at \(\lambda=1\). It yields \(\sqrt e/2\le C/\sqrt2\), i.e. \(C\ge\sqrt{e/2}\). Nothing here shows equality for the unrestricted universal constant.

## Verification

A standalone Python verifier (`verification/poisson_thinning_verify.py`) uses exact rational enumeration of finite Bernoulli-selector configurations for several row lengths and intensities, checks the exact centered finite laws, independently sums Poisson mass tails at test intensities, and checks sampled values against the analytical integer and interval bounds. It reports 2,210 passed assertions. The finite checks do not establish the theorem: Steps 1–5 above provide the analytical proof, while the code tests its formulas on accessible cases.

## Relationship to prior work

Kontorovich, *A local-to-global principle for \(f\)-divergence homogenization*, arXiv:2610.31164v1 (first public 2026-10-22), Theorem 2.3 and Section 11, proves a universal \(40\sqrt q\) convex thinning bound for arbitrary independent centered summands. Its bound does not identify the sharp necessary constant for the equal-half thinning case or the optimal intensity of the sparse symmetric Bernoulli family. The Poisson absolute-deviation formula, Poisson limit theorem and Robbins's Stirling bounds are classical and are not claimed as new. The new contribution assessed here is their sharp optimization in a natural sparse-thinning extremal family and the resulting universal-constant obstruction.

## Limitations

The optimality assertion concerns only the explicitly defined Poisson-limit rare-event family at retention probability \(1/2\). The best constant over arbitrary independent centered laws and all retention probabilities is not determined. No uniform convergence in \(\lambda\), finite-row sharp bound, or result for general convex test functions is claimed. The quantitative statement of originality is based on examined material; independent historical priority assessment may uncover related sharp thinning or Poisson-deviation ratio results.

## References

1. Aryeh Kontorovich, *A local-to-global principle for \(f\)-divergence homogenization*, arXiv:2610.31164v1, 2026-10-22, Theorem 2.3 and Section 11; https://arxiv.org/html/2610.31164v1 .
2. Herbert Robbins, *A Remark on Stirling's Formula*, American Mathematical Monthly 62 (1955), 26–29, DOI:10.2307/2308012; https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf .
3. Standard Poisson mean absolute-deviation identity; e.g. https://en.wikipedia.org/wiki/Poisson_distribution .
