# A budget-dependent reversal in two-site invasive-species removal surveys

## Finding

Two independent candidate habitats are surveyed by one crew under a **hard, realized survey-time budget**. Site \(i\) is occupied with probability \(p_i\in(0,1)\); at an occupied site, time to first detection during active surveying is exponential with rate \(\lambda_i>0\), while an empty site never yields a detection. In a one-switch policy \(i\to j\), survey the first site until the first detection or an abandonment cap \(c\in[0,T]\), whichever comes first, and spend all remaining time at the second site until its first detection or the common deadline \(T>0\). The objective is to maximize the **expected number of occupied sites detected**.

Writing \(L_{ij}(T,c)\) for the expected number of occupied but undetected sites, the exact loss is
\[
\begin{aligned}
L_{ij}(T,c)={}&p_i e^{-\lambda_i c}\\
&+p_j\left[(1-p_i)e^{-\lambda_j(T-c)}
+p_i e^{-\lambda_jT}\left(\lambda_i\int_0^c e^{(\lambda_j-\lambda_i)t}\,dt
+e^{(\lambda_j-\lambda_i)c}\right)\right].
\end{aligned}
\]
Define the posterior conditional hazard of first detection at site \(i\), after surveying it unsuccessfully for time \(c\), by
\[
h_i(c)=\frac{p_i\lambda_i e^{-\lambda_i c}}{1-p_i+p_i e^{-\lambda_i c}}.
\]
For every order and deadline the optimal cap is **unique**. It equals \(0\) if \(p_i\lambda_i\le p_j\lambda_j e^{-\lambda_j T}\), equals \(T\) if \(h_i(T)\ge p_j\lambda_j\), and otherwise is the unique solution in \((0,T)\) of
\[
\boxed{h_i(c)=p_j\lambda_j e^{-\lambda_j(T-c)}.}
\]
These endpoint conditions are mutually consistent; equality places the unique optimum at the corresponding boundary.

For large deadlines the optimum is interior, and, with \(s=\lambda_i+\lambda_j\) and \(\mu=\lambda_i\lambda_j/s\),
\[
\boxed{c_{ij}^*(T)=\frac{\lambda_jT+\log\!\left(\frac{p_i\lambda_i}{p_j\lambda_j(1-p_i)}\right)}s+o(1)}
\]
and
\[
\boxed{L_{ij}^*(T)=K_{ij}e^{-\mu T}(1+o(1)),\quad
K_{ij}=\frac{s}{\lambda_j}\left(\frac{\lambda_j}{\lambda_i}\right)^{\lambda_i/s}
 p_i^{\lambda_j/s}[p_j(1-p_i)]^{\lambda_i/s}.}
\]
In particular, the *sharp asymptotic order comparison* is
\[
\boxed{\frac{K_{ij}}{K_{ji}}=
\left(\frac{(1-p_i)^{\lambda_i}}{(1-p_j)^{\lambda_j}}\right)^{1/s}.}
\]
When the indices differ, the large-deadline optimal order starts with the site maximizing \(\lambda_i[-\log(1-p_i)]\), **not** necessarily the site maximizing the initial detection intensity \(p_i\lambda_i\). If \(p_i\lambda_i>p_j\lambda_j\), then \(i\to j\) is strictly better for every sufficiently small positive deadline.

The two orderings can therefore reverse as the deadline grows. An exact rational example is
\[
(p_A,\lambda_A,p_B,\lambda_B)=\left(\frac14,\frac{11}{5},\frac12,1\right).
\]
The initial intensities satisfy \(11/20>1/2\), but the long-run priority indices satisfy \((11/5)\log(4/3)<\log 2\), equivalently \(3^{11}>2^{17}\). Accordingly, the strictly better policy visits A first for sufficiently short deadlines and visits B first for all sufficiently long deadlines. This guarantees at least one budget-dependent ordering reversal, without asserting that the crossover is unique.

## Assumptions and scope

The two occupancies are independent Bernoulli variables. Detection processes are independent conditional on occupancy, stationary during active surveying, and have no false positives. The exponential clock counts **active** surveying time rather than calendar time. The crew has a fixed realized time limit \(T\), zero travel and switching time, immediate recognition of detection, and never returns to a site after switching away. The first-site cap is precommitted but an earlier detection releases its unused time to the second site. A detection at the second site ends that site's survey. Each site contributes reward one on detection, zero otherwise, so expected missed occupancy equals \(p_i+p_j\) minus expected detected count. All formulas and order comparisons apply for every \(0<p_i,p_j<1\), \(\lambda_i,\lambda_j,T>0\), except that a strict order comparison requires unequal indices as specified. No claim concerns all possible adaptive policies permitting revisits, additional sites, correlated occupancies, misclassification, travel time, or competing management costs.

## Proof

**Loss identity.** Let \(Z_i\) equal infinity when site \(i\) is empty and an independent exponential detection time of rate \(\lambda_i\) when occupied. The first-site survey duration is \(S_i=\min(Z_i,c)\). The miss probability at the first site is \(p_i e^{-\lambda_i c}\). Independence makes the unconditional miss probability at the second site \(p_j\mathbb E[e^{-\lambda_j(T-S_i)}]\). Separating an empty first site, detection at time \(t<c\), and no detection by \(c\) gives the displayed exact integral. This also covers \(\lambda_i=\lambda_j\), where the integral is \(c\).

**Unique cap.** Differentiating the conditional-expectation formula yields
\[
\frac{\partial L_{ij}}{\partial c}
=(1-p_i+p_i e^{-\lambda_i c})
\left[p_j\lambda_j e^{-\lambda_j(T-c)}-h_i(c)\right].
\]
The multiplier is positive. The first term in brackets is strictly increasing in \(c\), while
\[
h_i'(c)=-\frac{p_i(1-p_i)\lambda_i^2e^{-\lambda_i c}}{(1-p_i+p_i e^{-\lambda_i c})^2}<0.
\]
The derivative therefore changes from negative to positive at most once, proving strict uniqueness of the global minimum and the three endpoint/interior alternatives.

**Long-budget asymptotics.** For sufficiently large \(T\), the derivative has opposite signs at \(0\) and \(T\), so its root is interior. Its exact defining identity is
\[
s c=\lambda_j T+
\log\!\left(\frac{p_i\lambda_i}{p_j\lambda_j(1-p_i+p_i e^{-\lambda_i c})}\right).
\]
The root tends to infinity with \(T\), and the displayed expansion for \(c_{ij}^*(T)\) follows. Set \(A=p_i\) and \(B=p_j(1-p_i)\). At this root, the first two terms of the loss are
\(A e^{-\lambda_i c}\) and \(B e^{-\lambda_j(T-c)}\); their leading derivatives balance as \(\lambda_i A e^{-\lambda_i c}\sim \lambda_j B e^{-\lambda_j(T-c)}\). The remaining positive terms are of order \(O(e^{-\lambda_j T})\), \(O(T e^{-\lambda_j T})\), or \(O(e^{-2\mu T})\), respectively as \(\lambda_j<\lambda_i\), \(\lambda_j=\lambda_i\), or \(\lambda_j>\lambda_i\), and each is \(o(e^{-\mu T})\). Substitution gives the coefficient \(K_{ij}\). Interchanging \(i,j\), division and cancellation give the exact ratio above. Hence the long-budget index and its strict comparison follow.

**Short-budget order and reversal.** Assume \(p_i\lambda_i>p_j\lambda_j\). For sufficiently small \(T>0\), continuity and the cap test show that the best \(i\to j\) policy has \(c=T\), whereas the best \(j\to i\) policy has \(c=0\). The latter surveys only \(i\). The former surveys \(i\) for the same duration unless detection comes early, in which case it has a strictly positive probability of detecting \(j\) in the remaining time as well. Thus its expected number detected is strictly greater. In the rational example, \(p_A\lambda_A>p_B\lambda_B\), but the large-budget index prefers B because \(3^{11}>2^{17}\). By the long-budget loss ratio, the advantage of B-first is eventually strict. The optimal values are continuous in \(T>0\), since their loss functions are continuous and minimized over \(c\in[0,T]\); thus at least one equality of the two optimal orders lies between the two strict regimes.

## Verification

The standalone `verify.py` evaluates the closed loss by a second conditional-density quadrature, compares the analytic first derivative with symmetric differences, tests the optimized cap against grids for independently generated parameter choices, and checks the asymptotic coefficients and two different ordering regimes. Run with `python3 verify.py`; only the Python standard library is required. The exact integer checks \(11/20>1/2\) and \(3^{11}>2^{17}\) certify the reversal inequalities. The checker is corroborative: numerical tests are not a substitute for the proof of the universal assertions.

## Relationship to prior work

Guillera-Arroita, Hauser and McCarthy (2014) derive optimal invasive-species removal-survey allocations using the same occupancy-plus-Poisson detection assumptions, but their budget restriction is on **expected** total survey cost, with sitewise allocated caps rather than an ordered single-crew policy subject to one shared realized deadline. The authors explicitly distinguish variability of actual survey costs from the expected budget. The present result changes the operational constraint and objective, and derives order-dependent time-recycling and a limiting order index, not a corollary of their sitewise first-order conditions as stated. Hauser and McCarthy (2009) optimize a nonremoval surveillance design, under which a first detection does not release survey time. Brown (1980) analyzes finite-time search for one moving hidden target, rather than independent potentially present targets each rewarding a successful detection. These are conceptual distinctions, not claims that all possible equivalent results have been excluded from the older search literature.

## Limitations

The model is intentionally idealized and may not suit actual survey programs with significant travel time or a need to revisit habitats. Long-horizon optimality is within the one-switch, one-pass policy class; it is not global optimality over arbitrary switching and fully adaptive sensing. At equality of long-horizon indices, the leading asymptotic terms tie and no eventual ordering claim is made. At intermediate horizons, the analysis establishes existence, not uniqueness, of an ordering reversal for the example. The source comparison is best-knowledge historical, not independent priority certification. The complete full text of Hauser and McCarthy (2009) was not accessible in this review; an older equivalent special-case search result remains a residual risk. No ecological field-data calibration or external validation is claimed.

## References

1. Guillera-Arroita, G., Hauser, C. E., and McCarthy, M. A. (2014). *Optimal surveillance strategy for invasive species management when surveys stop after detection*. Ecology and Evolution 4, 1751–1760. First publicly online 2014-04-11. https://doi.org/10.1002/ece3.1056
2. Hauser, C. E., and McCarthy, M. A. (2009). *Streamlining ‘search and destroy’: cost-effective surveillance for invasive species management*. Ecology Letters 12, 683–692. https://doi.org/10.1111/j.1461-0248.2009.01323.x
3. Brown, S. S. (1980). *Optimal Search for a Moving Target in Discrete Time and Space*. Operations Research 28, 1275–1289. https://doi.org/10.1287/opre.28.6.1275
