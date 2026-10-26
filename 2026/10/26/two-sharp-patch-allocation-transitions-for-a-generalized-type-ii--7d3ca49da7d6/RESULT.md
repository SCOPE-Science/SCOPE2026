# Two sharp patch-allocation transitions for a generalized Type III feeding response

## Finding

A minimal two-patch feeding model exhibits a **local-extremum threshold strictly below a global-optimality threshold**. The separation is valid for every real Hill exponent \(p>1\), not only quadratic Type III responses. Let \(K>0\), let \(B>0\) be a fixed prey-abundance budget, and assume each of two identical, noninteracting predators occupies one identical patch. Each predator's instantaneous feeding response to its patch's allocated prey abundance \(u\) is
\[
 f_{p,K}(u)=\frac{u^p}{K^p+u^p}.
\]
For a split \(0\leq x\leq B\), total normalized intake is
\[
 I(x)=f_{p,K}(x)+f_{p,K}(B-x).
\]
Put \(N=B/K\). The two thresholds are
\[
 N_{\mathrm{loc}}(p)=2\left(\frac{p-1}{p+1}\right)^{1/p},\qquad
 N_{\mathrm{glob}}(p)=(2^p-2)^{1/p}.
\]
For **every** \(p>1\), the strict ordering \(0<N_{\mathrm{loc}}(p)<N_{\mathrm{glob}}(p)\) holds. All global maximizers of intake are exactly
\[
 \begin{cases}
 \{0,B\},&0<N<N_{\mathrm{glob}}(p),\\
 \{0,B/2,B\},&N=N_{\mathrm{glob}}(p),\\
 \{B/2\},&N>N_{\mathrm{glob}}(p).
 \end{cases}
\]
The two end allocations are strict one-sided local maxima for every positive budget. If \(0<N\leq N_{\mathrm{loc}}(p)\), the equal split is the sole interior critical point and a strict local minimum (including equality, where its quadratic curvature vanishes). If \(N>N_{\mathrm{loc}}(p)\), there are exactly three interior critical points: two symmetric strict local minima and the equal split, now a strict local maximum. In the nonempty interval \(N_{\mathrm{loc}}(p)<N<N_{\mathrm{glob}}(p)\), equal splitting is therefore locally but not globally intake-maximizing.

The noncentral minima emerge with a universal square-root law. Write their normalized locations as \(x_\pm/B\). As \(N\downarrow N_{\mathrm{loc}}(p)\) from above, for each fixed \(p>1\),
\[
 \left|\frac{x_\pm}{B}-\frac12\right|
 =\frac{\sqrt3}{2}\sqrt{\frac{N}{N_{\mathrm{loc}}(p)}-1}
 +o\left(\sqrt{\frac{N}{N_{\mathrm{loc}}(p)}-1}\right).
\]
The leading coefficient does not depend on the Hill exponent. At the global threshold, the maximizer switches discontinuously from fully concentrated prey to evenly distributed prey, with three precisely tied maximizers.

## Assumptions and scope

The two patches have equal area, the two predators have equal fixed maximum feeding rates, and predator locations are fixed (one per patch). The prey budget is divisible and nonnegative. No prey movement, recruitment, predator redistribution, interference, handling dynamics beyond the Hill response, or species interactions are included. The model optimizes **instantaneous total predator intake**, not prey survival, long-run population equilibria, or a behavioral/evolutionary optimum.

An overall positive feeding-rate multiplier does not affect any optimizer. Rescale prey abundance by \(K\) to set \(f_p(u)=u^p/(1+u^p)\) and \(\Phi_{p,N}(t)=f_p(t)+f_p(N-t)\) on \([0,N]\). Statements are for all real \(p>1\) and \(N>0\); no integer-exponent assumption is made.

## Proof

**1. Response curvature and local threshold.** For positive arguments,
\[
 f'_p(u)=\frac{p u^{p-1}}{(1+u^p)^2},\qquad
 f''_p(u)=\frac{p u^{p-2}\bigl((p-1)-(p+1)u^p\bigr)}{(1+u^p)^3}.
\]
Thus the single inflection point is \(u_0=((p-1)/(p+1))^{1/p}\). Symmetry forces \(\Phi'_{p,N}(N/2)=0\), and \(\Phi''_{p,N}(N/2)=2f''_p(N/2)\), so its quadratic curvature changes sign precisely at \(N_{\mathrm{loc}}=2u_0\). At the boundary, strict minimality will follow from the global count in Step 3, not from this second-derivative test alone. Since \(f'_p(0)=0<f'_p(N)\), the left endpoint has negative right derivative for every \(N>0\).

**2. Exact parametrization of all off-center critical points.** On the left half \(0<t<N/2\), write
\[
 t=\frac{N e^{-z}}{2\cosh z},\qquad N-t=\frac{N e^z}{2\cosh z},\qquad z>0.
\]
Set \(\alpha=(p-1)/2\) and \(\beta=(p+1)/2\). Rearranging the positive equation \(f'_p(t)=f'_p(N-t)\) gives precisely
\[
 N=Q_p(z):=2\cosh z
 \left(\frac{\sinh(\alpha z)}{\sinh(\beta z)}\right)^{1/p}.
\]
We prove that \(Q_p\) is strictly increasing for every real \(p>1\). Define \(G(s)=s\coth s\), \(H(s)=G'(s)=\coth s-s\operatorname{csch}^2s\) for \(s>0\). Direct differentiation shows
\[
 H'(s)=2\operatorname{csch}^2s\,(s\coth s-1)>0.
\]
Also \(H(s)<\tanh s\), since \(\tanh s-H(s)=(s-\tanh s)/\sinh^2s>0\). The quotient \(H(s)/s\) is strictly decreasing. Indeed, its derivative is negative exactly when
\[
 \sinh^2s+s\tanh s>2s^2.
\]
The difference between the two sides is
\[
 (\sinh s-s)(\sinh s+s)-s(s-\tanh s)
 >s\bigl(2\sinh s+\tanh s-3s\bigr)>0.
\]
For the final inequality, the quantity in parentheses vanishes at zero and has derivative
\[
 2\cosh s+\operatorname{sech}^2s-3
 =\frac{(\cosh s-1)^2(2\cosh s+1)}{\cosh^2s}>0.
\]
Because \(\beta-\alpha=1\), the mean-value theorem and these strict inequalities yield
\[
 \frac{G(\beta z)-G(\alpha z)}{z}
 <H(\beta z)<\beta H(z)<\beta\tanh z<p\tanh z.
\]
Consequently,
\[
 \frac{d}{dz}\log Q_p(z)
 =\tanh z-\frac{\beta\coth(\beta z)-\alpha\coth(\alpha z)}p>0.
\]
The endpoint limits are
\[
 Q_p(0+)=2\left(\frac\alpha\beta\right)^{1/p}
 =N_{\mathrm{loc}}(p),\qquad
 Q_p(z)\sim\exp((1-1/p)z)\to\infty\quad(z\to\infty).
\]
Hence the left half contains exactly one off-center critical point when \(N>N_{\mathrm{loc}}\), and none otherwise; reflection gives the full classification of stationary-point counts.

**3. Signs and strict extremum types.** For \(0<t<N/2\), \(\Phi'_{p,N}(t)=f'_p(t)-f'_p(N-t)\) is negative near zero. If \(N\le N_{\mathrm{loc}}\), it has no zero on that open half, hence remains strictly negative; the center is then a strict local minimum, even when \(N=N_{\mathrm{loc}}\) and the quadratic term vanishes. If \(N>N_{\mathrm{loc}}\), the center has negative second derivative, so its left-neighbor derivative is positive; Step 2 gives exactly one preceding simple sign-changing critical point, a strict local minimum. Reflection supplies the other minimum. The endpoints are always strict one-sided maxima, and no other candidates exist for global maximizers.

**4. Global switch and strict separation.** The only global candidates are the two endpoints and the center. Their normalized payoffs satisfy
\[
 \Phi_{p,N}(0)=\frac{N^p}{1+N^p},\qquad
 \Phi_{p,N}(N/2)=\frac{2N^p}{2^p+N^p},
\]
so that
\[
 \Phi_{p,N}(N/2)-\Phi_{p,N}(0)
 =\frac{N^p\left(N^p-(2^p-2)\right)}{(2^p+N^p)(1+N^p)}.
\]
This proves the complete global classification. At \(N=N_{\mathrm{loc}}\), the center is a strict minimum by Step 3; therefore the expression above is negative there, proving \(N_{\mathrm{loc}}<N_{\mathrm{glob}}\) for every \(p>1\). In particular, the interval with a locally maximizing but globally inferior equal split is genuinely nonempty.

**5. Universal onset.** Standard expansions at \(z=0\) give
\[
 \log\frac{Q_p(z)}{N_{\mathrm{loc}}(p)}
 =\log\cosh z+
 \frac1p\left[\log\frac{\sinh(\alpha z)}{\alpha z}
 -\log\frac{\sinh(\beta z)}{\beta z}\right]
 =\frac{z^2}{3}+O_p(z^4).
\]
For the smaller off-center minimum, \(t/N=(1-\tanh z)/2\). Inverting the preceding expansion and using \(\tanh z=z+O(z^3)\) yields the stated square-root law and its exponent-independent coefficient.

## Verification

The accompanying standard-library program `verification.py` reproducibly checks 1,500 seeded parameter configurations across all three allocation regimes. Each is sampled over 401 feasible splits, giving 601,500 payoff comparisons. It also reconstructs off-center stationary points from the exact hyperbolic equation, verifies derivative equalities and stationary order, tests the critical square-root scaling at seven Hill exponents, and performs 2,093 independent monotonicity comparisons. Numerical checks do not substitute for Steps 1–5.

For the quadratic Hill response \(p=2\), the two thresholds are
\[
 N_{\mathrm{loc}}=2/\sqrt3\approx1.154700538379,
 \qquad N_{\mathrm{glob}}=\sqrt2\approx1.414213562373.
\]
At \(N=\sqrt2\), the three global maximizers yield exactly \(2/3\). The two off-center minima are at
\[
 t_\pm=\frac{\sqrt2\pm\sqrt{4\sqrt3-6}}2
\]
and their common payoff is \((3-\sqrt3)/2\), giving the exact intake barrier
\[
 \frac23-\frac{3-\sqrt3}{2}=\frac{3\sqrt3-5}{6}\approx0.0326920704511.
\]

## Relationship to prior work

Real (1977) established a generalized sigmoidal functional-response framework that motivates the Hill feeding curve, not the two-patch optimization theorem. Nachman (2006) analyzes prey patchiness and predator aggregation in a substantially richer population-response model, including qualitative advantages of different spatial arrangements; its assumptions and outcomes are not the fixed-predator, identical-Hill, constrained two-patch extremum classification. Hossie and Murray (2016) observe empirical dependence of functional-response shape on prey arrangement rather than deriving the present exact transition.

The closest mathematical coverage is Fazel and Chiang (2005), who treat sums of nonconcave resource utilities, explicitly including rational Hill-type sigmoid functions, by sum-of-squares optimization. Udell and Boyd (2014) develop general global approximation algorithms for sums of sigmoids under convex constraints. These frameworks contain the displayed objective as an optimizable special case and can calculate numerical optima for specified parameters. Their inspected statements do **not** give a uniform closed-form two-threshold diagram for arbitrary real \(p>1\), the exact stationary-point count, or the exponent-independent square-root onset. The latter structural statements are the present contribution; the existence of the framework and any algorithmic global-optimality guarantees are not claimed anew.

## Limitations

This is an exact mathematical statement for a deliberately minimal, equal-patch, fixed-predator model; natural systems may require unequal patch sizes, movement, adaptive predators, stochastic prey counts, depletion and predator density dependence. The displayed endpoint solutions maximize predator intake, not a normative ecological management objective. The general sigmoidal-optimization literature is broad; a more specialized prior theorem or unpublished analytical result could cover the same phase diagram. The original 1977 source's full text was not accessible, although its bibliographic record and abstract were inspected. No independent mathematical or historical-priority audit has been performed.

## References

1. Real, L. A. (1977), “The Kinetics of Functional Response,” *The American Naturalist* 111(978), 289–300, https://doi.org/10.1086/283161 (first published 1977-03-01; accessible abstract).
2. Fazel, M., and Chiang, M. (2005), “Network Utility Maximization With Nonconcave Utilities Using Sum-of-Squares Method,” *IEEE CDC/ECC*, 1867–1874, https://doi.org/10.1109/CDC.2005.1582432 (open full text: https://faculty.washington.edu/mfazel/cdc-final2-edit.pdf).
3. Nachman, G. (2006), “A functional response model of a predator population foraging in a patchy habitat,” *Journal of Animal Ecology* 75, 948–958, https://doi.org/10.1111/j.1365-2656.2006.01114.x (first published 2006-06-23; open article text).
4. Udell, M., and Boyd, S. (2014), “Maximizing a Sum of Sigmoids,” working draft dated 2014-05-05, https://stanford.edu/~boyd/papers/pdf/max_sum_sigmoids.pdf (open full manuscript).
5. Hossie, T. J., and Murray, D. L. (2016), “Spatial arrangement of prey affects the shape of ratio-dependent functional response in strongly antagonistic predators,” *Ecology*, https://doi.org/10.1890/15-1535.1 (first published 2016-04-08; accessible article text).
