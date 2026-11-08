# A half-shape ranking transition for Weibull workloads under Gamma service clocks

## Finding

Let \(0<\beta<1\). Independently for every job \(i\geq1\), sample \(W_i>0\) with survivor function \(\Pr(W_i>w)=e^{-w^\beta}\) for \(w\geq0\). Put \(K_i=\lceil W_i\rceil\), sample independent unit-rate exponential variables \(E_{i,1},E_{i,2},\ldots\), independently of all workloads, and define the actual service duration \(L_i=\sum_{j=1}^{K_i}E_{i,j}\). Thus \(L_i\mid W_i=w\) has the \(\operatorname{Gamma}(\lceil w\rceil,1)\) distribution. Let \(I_n\) be the index of the largest workload and \(J_n\) the index of the longest duration among jobs \(1,\ldots,n\); ties are broken by smaller index (and have probability zero).

The index-agreement probability has the complete classification

\[
\lim_{n\to\infty}\Pr(I_n=J_n)=
\begin{cases}
1,&0<\beta<\tfrac12,\\
p_\star,&\beta=\tfrac12,\\
0,&\tfrac12<\beta<1.
\end{cases}
\]

Here \(0<p_\star<1\) is the explicit constant

\[
p_\star=\int_{-\infty}^{\infty}\frac{\phi(g)}{1+A(g)}\,dg,
\qquad A(g)=\int_0^\infty e^u\overline\Phi(g+2u)\,du
=e^{1/8-g/2}\overline\Phi(g-1/2)-\overline\Phi(g),
\]

with \(\phi\) the standard Gaussian density and \(\overline\Phi(g)=\int_g^\infty\phi(z)\,dz\). Numerical quadrature gives \(p_\star\approx0.744414083\).

## Assumptions and scope

The theorem concerns independent jobs, each comprising the integer number \(K_i=\lceil W_i\rceil\) of sequential, independently exponentially distributed unit-service phases. The workload distribution is exactly the stretched-exponential Weibull law of shape \(\beta\in(0,1)\), not a generalized asymptotic tail assumption. Job durations are independent conditionally on their workloads; the exponential phases are independent across jobs. The sample size \(n\) tends to infinity while \(\beta\) stays fixed. No independence of workload and duration is assumed or true. The conclusion concerns agreement of the two maximizer **indices**, not just ratios of their maxima, and does not establish a ranking law for actual random-walk drawdown episodes.

## Proof

**1. Workload extremes and their scales.** Write \(h_n=(\log n)^{1/\beta}\) and \(b_n=h_n^{1-\beta}/\beta\). For each fixed \(x\in\mathbb R\), Taylor expansion gives

\[
(h_n+b_nx)^\beta=\log n+x+o(1).
\]

Consequently the point process of centered workloads

\[
\mathcal N_n=\sum_{i=1}^n\delta_{(W_i-h_n)/b_n}
\]

converges vaguely on sets bounded below to a Poisson point process on \(\mathbb R\) with intensity \(e^{-x}\,dx\). In particular, \(\max_i W_i=h_n+O_{\mathbb P}(b_n)\), the largest limiting atoms are distinct almost surely, and \(\Pr\{\max_i W_i<h_n-Mb_n\}\to e^{-e^M}\). Since \(b_n\to\infty\), replacing a workload by its ceiling changes a normalized value by \(o(1)\).

**2. Conditional service noise.** Given \(W_i=w\), the duration is a sum of \(\lceil w\rceil\) independent unit-rate exponentials. Its mean and variance both equal \(\lceil w\rceil\), its centered fluctuations satisfy the usual central limit theorem, and for every \(t\geq k>0\) its upper tail satisfies

\[
\Pr\{\operatorname{Gamma}(k,1)\geq t\}
\leq\exp\{-t+k+k\log(t/k)\}
\leq\exp\{-(t-k)^2/(2t)\}.
\]

The first inequality follows by optimizing the exponential moment; the second uses \(\log(1+u)\leq u-u^2/(2(1+u))\) for \(u\geq0\). On any fixed compact range \(x=(w-h_n)/b_n\), the conditional centered noise \((L_i-\lceil w\rceil)/\sqrt{h_n}\) converges uniformly in distribution to a standard Gaussian. Moreover

\[
\frac{b_n}{\sqrt{h_n}}=\frac{h_n^{1/2-\beta}}{\beta},
\]

which diverges, equals \(2\), or tends to zero according as \(\beta\) lies below, at, or above one half.

**3. Excluding lower-workload intruders when \(\beta\leq1/2\).** For each fixed real \(K\), the following uniform cutoff holds:

\[
\lim_{M\to\infty}\limsup_{n\to\infty}
 n\Pr\big\{W_1<h_n-Mb_n,\ L_1>h_n-Kb_n\big\}=0.
\tag{1}
\]

Here are the quantitative details. On \(W_1<h_n/2\), the Gamma Chernoff inequality bounds the displayed conditional event by \(e^{-c h_n}\) for large \(n\), with \(c=c(K)>0\); the factor \(n\) is harmless because \(h_n/\log n\to\infty\). In the remaining range, put \(W_1=h_n-sb_n\). For \(s\in[M,h_n/(2b_n)]\), its transformed intensity density obeys \(n f_W(h_n-sb_n)b_n\leq C e^{Cs}\), because the Weibull hazard on \([h_n/2,h_n]\) is bounded above by \(C/b_n\). For \(s\geq M>K+2\), the conditional Gamma upper-tail inequality is at most \(\exp\{-c(s-K)^2b_n^2/h_n\}\). When \(\beta\leq1/2\), \(b_n^2/h_n\) is bounded below by a positive constant for large \(n\). Integrating \(C\exp\{Cs-c'(s-K)^2\}\) over \(s\geq M\) proves (1). This is an actual tail estimate, not a claim that vague convergence alone controls the maximum.

**4. The regime \(0<\beta<1/2\).** On every compact centered-workload range, the independent Gamma fluctuations divided by \(b_n\) converge to zero, as \(h_n/b_n^2\to0\). The marked workload-duration point process therefore converges on such a range to atoms \((x,x)\) of the workload Poisson process. There is almost surely a unique largest atom separated from the second largest. The cutoff (1) excludes competitors with centered workload below \(-M\), while the probability of no workload above \(-M\) tends to \(e^{-e^M}\). Letting \(M\to\infty\) shows that the maximizers of workload and duration have the same index with probability tending to one.

**5. The critical regime \(\beta=1/2\).** Here \(h_n=(\log n)^2\), \(b_n=2\log n=2\sqrt{h_n}\). The marked point process of workload coordinate \((W_i-h_n)/b_n\) and centered Gamma noise \((L_i-\lceil W_i\rceil)/\sqrt{h_n}\), on regions with workload coordinate bounded below, converges to a Poisson process on \(\mathbb R^2\) with intensity \(e^{-x}\phi(g)\,dx\,dg\). Its workload score is \(x\) and its duration score is \(x+g/2\). The cutoff (1), with normal-tail integrability of these limiting scores, allows both maximizers to be identified in the entire limiting process.

Let \((X,G)\) be the atom of greatest workload score. The distribution of \(X\) is \(\Pr(X\leq x)=\exp\{-e^{-x}\}\), and its Gaussian mark \(G\) is independent of \(X\). All other atoms have workload coordinate \(x'<X\). Conditional on \(X=x,G=g\), the expected number that beat its duration score is

\[
\int_{-\infty}^{x}e^{-x'}\overline\Phi\big(g+2(x-x')\big)\,dx'
=e^{-x}A(g).
\]

The Poisson void probability is therefore \(\exp\{-e^{-x}A(g)\}\). Since \(e^{-X}\) is unit exponential, averaging first over \(X\) yields \(1/(1+A(g))\), then over \(G\) yields exactly the stated integral. Integration by parts, followed by completion of the Gaussian square, yields the alternative closed expression for \(A(g)\). For every finite \(g\), \(0<A(g)<\infty\), proving \(0<p_\star<1\).

**6. The regime \(1/2<\beta<1\).** Put \(r_n=\sqrt{h_n}\). Now \(b_n=o(r_n)\), so \(W_{I_n}=h_n+o_{\mathbb P}(r_n)\), and the Gamma central limit theorem shows \(L_{I_n}=h_n+O_{\mathbb P}(r_n)\). On the other hand the number of jobs with workloads in \([h_n-r_n,h_n-r_n/2]\) diverges in probability: its mean is

\[
n\left[e^{-(h_n-r_n)^\beta}-e^{-(h_n-r_n/2)^\beta}\right]
=\exp\{\beta h_n^{\beta-1/2}+o(1)\}
 -\exp\{(\beta/2)h_n^{\beta-1/2}+o(1)\}\longrightarrow\infty.
\]

These jobs are not the largest-workload job with probability tending to one. Given their workloads, their service times are independent, and for every fixed \(K\) the conditional probability \(\Pr\{L_i>h_n+Kr_n\mid W_i\}\) is uniformly bounded below, eventually, by a positive number (for example half the Gaussian tail \(\overline\Phi(K+1)\)). Hence at least one such rival exceeds \(h_n+Kr_n\) with probability tending to one. Taking \(K\) large enough that \(\Pr\{L_{I_n}>h_n+Kr_n\}\) is arbitrarily small proves \(\Pr(I_n=J_n)\to0\).

## Verification

The accompanying `verify_transition.py` is a standalone Python-standard-library checker. It compares the integral and Gaussian closed forms of \(A(g)\) at seven points, verifies the Gamma Chernoff rate inequality on 3000 finite parameter pairs, evaluates the critical constant with composite Simpson quadrature, and independently simulates the limiting marked Poisson process with a fixed seed and specified finite truncation. The checker is a finite numerical consistency test; the infinitary results follow only from the six proof steps above. Its expected output includes `FINITE_CHECKS_OK=3009` and a critical constant near \(0.744414083\). No computer-assisted exhaustive certification of infinite asymptotics is asserted.

## Relationship to prior work

Y. Wu, *When is the deepest drawdown also the longest?*, arXiv:2610.41990v1 (2026-10-30), proves rank separation for iid-increment random-walk drawdowns under a finite exponential loss moment, and rank agreement under regularly varying losses. This motivates a question about the intermediate stretched-exponential regime. The theorem here does **not** extend Wu's random-walk result to that regime: it instead resolves the analogous question for an explicitly specified, independent Weibull-workload/Gamma-service model.

E. Perfilev and V. Wachtel, *Local tail asymptotics for the joint distribution of length and of maximum of a random walk excursion*, arXiv:1907.02578v1, determine a light-tailed Cramér-regime conditional excursion-length Gaussian limit. They do not treat this independent-job Weibull/Gamma maximizer comparison. General Poisson point-process convergence and extreme-order concomitant theory supply proof tools, but the workload/noise balance, the shape-one-half threshold and the displayed integral are model-specific conclusions. Historical equivalence to a more general selection or concomitant theorem cannot be ruled out solely by the searches reported here.

## Limitations

The result assumes exact Weibull workloads, independent jobs and exponential unit-service phases. A different workload tail, correlated jobs, or service-time distributions without the same square-root fluctuation law may alter the transition. The result does not establish whether identical ranking regimes hold for actual positive-drift random-walk excursions in Wu's model. The numeric value of the critical constant is approximate; its defining Gaussian integral is exact. Independent validation and definitive historical-priority assessment have not been performed.

## References

1. Y. Wu, *When is the deepest drawdown also the longest?*, arXiv:2610.41990v1, first posted 2026-10-30. https://arxiv.org/html/2610.41990v1
2. E. Perfilev and V. Wachtel, *Local tail asymptotics for the joint distribution of length and of maximum of a random walk excursion*, arXiv:1907.02578v1, first posted 2019-07-04. https://arxiv.org/html/1907.02578v1
3. H. A. David and J. Galambos, *The asymptotic theory of concomitants of order statistics*, *Journal of Applied Probability* (bibliographic entry; original publication year not verified here). https://www.cambridge.org/core/journals/journal-of-applied-probability/article/asymptotic-theory-of-concomitants-of-order-statistics/0BEA2135DEFD89D7A3AB6B13AED67123
4. B. Basrak, I. Molchanov and H. Planinić, *Extremal behavior of stationary marked point processes*, arXiv:2210.01474, 2022. https://arxiv.org/abs/2210.01474
