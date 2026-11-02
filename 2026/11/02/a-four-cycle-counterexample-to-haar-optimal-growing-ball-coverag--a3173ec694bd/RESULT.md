# A four-cycle counterexample to Haar-optimal growing-ball coverage

## Finding

**Theorem (failure of Haar optimality).** Let \(S=\mathbb Z/4\mathbb Z\) have its translation-invariant shortest-cycle metric \(d(i,j)=\min\{|i-j|,4-|i-j|\}\), where representatives are chosen in \(\{0,1,2,3\}\). Seeds arrive at rate one according to a Poisson process, each independently located according to \(\mu\) on \(S\). A seed born at time \(\tau\) covers the closed ball of radius \(t-\tau\) at time \(t\ge\tau\). Write \(C_\mu\) for the first time all four points are covered.

For normalized Haar measure \(h=(1/4,1/4,1/4,1/4)\),
\[
\mathbb E C_h=\frac{25}{3}-\frac{32}{3}e^{-1/4}+6e^{-1/2}-\frac43e^{-3/4}-\frac43e^{-1}=2.5449809469642059\ldots.
\]
For the antipodal seed law \(\nu=(1/2,0,1/2,0)\),
\[
\mathbb E C_\nu=2+2e^{-1/2}-2e^{-1}=2.4773024370823822\ldots.
\]
In particular,
\[
\mathbb E C_h-\mathbb E C_\nu=\frac{19}{3}-\frac{32}{3}e^{-1/4}+4e^{-1/2}-\frac43e^{-3/4}+\frac23e^{-1}>\frac{6767}{100000}>0.
\]
Consequently Haar measure does **not** always minimize expected cover time in the standardized growing-ball model on a compact group with translation-invariant metric. This is an explicit counterexample to the unrestricted compact-group question in [1, Section 7.1]. No claim is made that \(\nu\) itself is globally optimal.

## Assumptions and scope

The space is exactly the four-point metric space \(\mathbb Z/4\mathbb Z\), not the geometric circle including its edges. The metric has distances zero, one, and two and is invariant under addition. The seed process has total arrival rate one, geometric growth speed one, independent locations at each birth, and closed metric balls. The seed law may assign zero mass to some sites; this is allowed in the original growth-model definition and causes no infinite cover time because a single seed covers the diameter-two space two time units after birth. All statements concern expectations of this finite-space process, not an asymptotic limit or an optimization over all seed laws.

## Proof

**1. Poisson void probability.** For nonempty \(A\subseteq S\), let \(B(A,r)=\{s:d(s,A)\le r\}\). The event that every site of \(A\) is still uncovered at time \(t\) means there is no Poisson seed in its space-time backward cone. Hence
\[
\Pr(A\text{ is uncovered at }t)=\exp\left[-\int_0^t\mu(B(A,r))\,dr\right].
\]
By inclusion-exclusion over the four target sites and the tail-integral formula for nonnegative random variables,
\[
\mathbb E C_\mu=\sum_{\varnothing\ne A\subseteq S}(-1)^{|A|+1}\int_0^\infty\exp\left[-\int_0^t\mu(B(A,r))\,dr\right]dt.
\]
Set \(a=\mu(A)\) and \(b=\mu(B(A,1))\). Since all distinct sites have distance at least one and the diameter is two, the inner integrated intensity has slopes \(a,b,1\) on the successive intervals \([0,1]\), \([1,2]\), and \([2,\infty)\). Integration yields
\[
I(a,b)=\frac{1-e^{-a}}a+e^{-a}\frac{1-e^{-b}}b+e^{-a-b},
\]
where each quotient is defined as one when its denominator is zero. Thus \(\mathbb E C_\mu=\sum_{A\ne\varnothing}(-1)^{|A|+1}I(\mu(A),\mu(B(A,1)))\).

**2. Haar law.** Every singleton has \(a=1/4,b=3/4\). For every set with at least two vertices, its radius-one neighborhood is all of \(S\), and for a set of size \(j\) we have \(a=j/4,b=1\). Counting the \(4,6,4,1\) subsets by cardinality gives
\[
\mathbb E C_h=4I(1/4,3/4)-6I(1/2,1)+4I(3/4,1)-I(1,1).
\]
Direct expansion of the elementary integrals is exactly the displayed closed form.

**3. Antipodal law.** Let \(T_0,T_2\) denote first arrival times of seeds at the two supported antipodal sites. Poisson thinning makes them independent exponential variables of rate \(1/2\). All later seeds at those same sites are covered by the expanding ball from their first seed, so have no effect on cover time. Write \(M=\min(T_0,T_2)\), \(G=|T_0-T_2|\). The two sites adjacent to both seed locations are covered at time \(M+1\). The opposite seed site is covered either at time \(M+G\) by its own first seed or at time \(M+2\) by the first seed across the diameter. Consequently
\[
C_\nu=M+\max\{1,\min(G,2)\}.
\]
Exponential competition and memorylessness give independent \(M\sim\operatorname{Exp}(1)\) and \(G\sim\operatorname{Exp}(1/2)\). Hence
\[
\mathbb E C_\nu=1+1+\int_1^2e^{-r/2}\,dr=2+2e^{-1/2}-2e^{-1}.
\]
The same value is independently obtained by evaluating the 15-subset Poisson formula for \(\nu\).

**4. Strict comparison without floating-point assumptions.** For every rational \(0<z\le1\), the alternating Taylor sums \(T_j(z)=\sum_{k=0}^j(-z)^k/k!\) obey \(T_{13}(z)<e^{-z}<T_{12}(z)\). Substitute the corresponding rational lower and upper bounds at \(z=1/4,1/2,3/4,1\) in the exact displayed difference, reversing endpoints for negative coefficients. Rational arithmetic yields a certified interval inside \((6767/100000,677/10000)\); in particular the difference is strictly positive.

## Verification

The accompanying standalone Python program `check_counterexample.py` uses only the standard library and independently enumerates all 15 nonempty subsets, exactly expands the elementary integrals into rational linear combinations of exponentials, checks both closed forms, and certifies the strict inequality with rational Taylor bounds. Run `python3 check_counterexample.py` from the directory containing this document and the program. Its printed decimals are diagnostic only; the strict sign follows from exact fractions and alternating-series inequalities, not floating-point calculation.

## Relationship to prior work

Aldous [1] defines this exact Poisson-arrival, unit-speed ball-growth model and asks whether Haar measure minimizes mean cover time on all compact groups with invariant metric; Section 7.1 explicitly leaves that growth-model question open. The counterexample here uses a finite compact group and a concentrated antipodal measure; [1] neither states this four-site strict inequality nor gives a general Haar-optimality theorem. The source mentions analogous fixed-radius nonuniformity, which does not by itself imply anything about expanding balls.

Falgas-Ravry, Larsson and Markström [2, Example 4.1] analyze structured *discrete-time, fixed-coupon* collectors, including transitive distributions that cover faster than exchangeable ones. Their example is related as motivation but does not contain the continuously expanding Poisson birth-growth expectation or the strict four-cycle calculation. Subsequent priority for this exact finite-group example has not been established independently.

## Limitations

Only a strict witness is proved, not the global minimum of \(\mathbb E C_\mu\) on the simplex of all laws \(\mu\), nor the behavior on connected compact groups such as the continuous circle. This result does not disprove any conjecture restricted to connected groups or to large-diameter asymptotic families. No quantitative robustness or uniqueness theorem is claimed. Independent validation and exhaustive historical-priority verification remain outstanding.

## References

[1] D. J. Aldous, *Covering a compact space by fixed-radius or growing random balls*, arXiv:2101.12671, first publicly posted 29 January 2021; ALEA 19 (2022), 755–767, DOI: 10.30757/ALEA.v19-29. https://arxiv.org/abs/2101.12671

[2] V. Falgas-Ravry, J. Larsson and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, arXiv:1601.04455, first publicly posted 18 January 2016; Advances in Applied Probability 52 (2020), 433–462. https://arxiv.org/abs/1601.04455
