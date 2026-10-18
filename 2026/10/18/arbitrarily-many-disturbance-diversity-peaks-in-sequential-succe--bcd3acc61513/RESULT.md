# Arbitrarily many disturbance–diversity peaks in sequential succession

## Finding

**Theorem (successive successional timescales and diversity peaks).** Fix an integer \(n\ge2\). Consider the \(n\)-stage, homogeneous-reset continuous-time succession model defined below, and let \(c>0\) be the disturbance intensity. Let \(S_n(c)=1-\sum_{j=0}^{n-1}\pi_j(c)^2\) be Gini–Simpson stage diversity and \(H_n(c)=-\sum_{j=0}^{n-1}\pi_j(c)\log\pi_j(c)\) be Shannon stage entropy.

1. Set \(R=10^4n^4\) and choose successive forward-transition rates \(\lambda_j=R^{n-2-j}\) for \(0\le j\le n-2\). **Each** of \(S_n\) and \(H_n\) has at least \(n-1\) distinct strict local maxima on \((0,\infty)\). Thus neither index admits a bound on the number of disturbance-intensity peaks that is independent of the number of succession stages. The conclusion persists under sufficiently small perturbations of all transition rates.
2. For \(n=2\), both indices have exactly one strict local maximum, at \(c=\lambda_0\). Therefore **three stages are the sharp minimum** for two strict peaks of either diversity measure.
3. For \(n=3\), put \(r=\lambda_0/\lambda_1>0\). The Gini–Simpson curve has **exactly two** strict local maxima if and only if \(r>r_*\), where \(r_*\in(12,13)\), approximately \(12.2393958692551\), is the unique positive root of
   \[
   F(r)=r^7-27r^6+252r^5-918r^4+594r^3-540r^2-135r-27.
   \]
   For \(0<r\le r_*\), it has exactly one strict local maximum. This exact ratio criterion is asserted only for the Gini–Simpson index; no analogous sharp Shannon ratio criterion is claimed.

## Assumptions and scope

A large homogeneous landscape consists of patches in distinct, successive habitat or community stages \(0,1,\ldots,n-1\). In the absence of disturbance, a patch in stage \(j<n-1\) progresses to stage \(j+1\) at an independent exponential rate \(\lambda_j>0\); the climax stage \(n-1\) has no further forward transition. Independently, a Poisson disturbance of rate \(c>0\) resets each patch to stage \(0\), irrespective of its present stage. Disturbance in stage \(0\) has no state-changing effect. There are no spatial interactions, feedbacks or stage-dependent reset hazards. The continuous-time chain is irreducible for \(c>0\), so the stationary fractions \(\pi_j(c)>0\) are unique.

Define \(y_0(c)=1\), and for \(1\le k\le n-1\),
\[
 y_k(c)=\prod_{i=0}^{k-1}\frac{\lambda_i}{\lambda_i+c}.
\]
Then the stationary fractions are
\[
 \pi_j(c)=y_j(c)-y_{j+1}(c)\quad(0\le j<n-1),
 \qquad \pi_{n-1}(c)=y_{n-1}(c).
\]
All logarithms below are natural. Diversity is **between stages** of succession over the landscape, not within-stage taxonomic species diversity. The number of observable maxima is the number of distinct strict local maxima as the positive real disturbance intensity varies continuously.

## Proof

**Stationary law.** The age of a patch since its last Poisson reset is exponential with rate \(c\). Reaching stage \(k\) requires completing independent exponential sojourns with rates \(\lambda_0,\ldots,\lambda_{k-1}\) before that age; the Laplace transform gives \(\mathbb P(\text{stage}\ge k)=y_k(c)\). The stated difference formula follows. Equivalently, it solves the continuous-time stationary balance equations, including the reset flux. All fractions are positive, sum to one, and converge to a point mass at stage \(n-1\) as \(c\downarrow0\) and at stage \(0\) as \(c\to\infty\). Therefore both diversity indices tend to zero at each extreme.

**An explicit alternating peak–trough certificate.** Fix the rates in part 1. For each \(0\le i\le n-2\) consider the candidate high-diversity intensity \(c=\lambda_i\). Since every earlier rate is at least \(R\lambda_i\), the probability of reaching stage \(i\) is at least \(1-i/R\). The chance of stopping in stage \(i\), conditional on reaching it, is \(1/2\); the mass in stage \(i+1\) is at least \((1-i/R)(1-1/R)/2\) (with the final-stage case even larger). Because \(R=10^4n^4\), both \(\pi_i\) and \(\pi_{i+1}\) exceed \(49/100\). Thus
\[
 S_n(\lambda_i)\ge2\pi_i\pi_{i+1}>2(49/100)^2>0.48.
\]
The inequality \(-\log z\ge1-z\), for \(0<z\le1\), yields \(H_n\ge S_n\), so \(H_n(\lambda_i)>0.48\) as well.

For each \(0\le i\le n-3\), define the intervening intensity
\[
 t_i=\sqrt{\lambda_i\lambda_{i+1}}=100n^2\lambda_{i+1}.
\]
For every \(j\le i\), \(t_i/\lambda_j\le R^{-1/2}\), and \(\lambda_{i+1}/t_i=R^{-1/2}\). The product formula therefore gives
\[
 \pi_{i+1}(t_i)\ge1-\frac{i+2}{\sqrt R}
 \ge1-\varepsilon,\qquad
 \varepsilon:=\frac n{\sqrt R}=\frac1{100n}.
\]
Consequently \(S_n(t_i)\le2\varepsilon\le0.01\). Among all \(n\)-component probability vectors with one component at least \(1-\varepsilon\), entropy is bounded by
\[
 H_n(t_i)\le h_2(\varepsilon)+\varepsilon\log(n-1)
 \le\varepsilon\left(1+\log\frac{n-1}{\varepsilon}\right)
 \le\frac{1+\sqrt{100n(n-1)}}{100n}<0.105,
\]
where \(h_2(u)=-u\log u-(1-u)\log(1-u)\), using \(\log z\le\sqrt z\) for \(z>0\). Hence each designated high-diversity intensity is separated from its neighbors by a much lower-diversity intensity. Together with the zero limits at \(c=0,\infty\), these \(n-1\) high points lie in disjoint intervals whose endpoints have strictly smaller diversity. Both diversity functions are real analytic and nonconstant on each interval. Each interval therefore contains an interior **strict** local maximum. The fixed strict inequalities persist under sufficiently small perturbations of the positive \(\lambda_j\), proving robustness.

**Two and three stages.** When \(n=2\), \(\pi_0=c/(c+\lambda_0)\) and \(\pi_1=\lambda_0/(c+\lambda_0)\). Both indices are uniquely maximized at the equal split \(c=\lambda_0\). For \(n=3\), scale \(\lambda_1\) to one and write \(x=c/\lambda_1\), \(r=\lambda_0/\lambda_1\). Direct substitution gives
\[
 S_3(x)=\frac{2rx\bigl(r+(x+1)^2\bigr)}{(r+x)^2(x+1)^2},
 \quad S_3'(x)=-\frac{2rP_r(x)}{(r+x)^3(x+1)^3},
\]
where
\[
 P_r(x)=x^4+(3-r)x^3+3x^2+(r-1)^2x-r(r+1).
\]
Its discriminant with respect to \(x\) is \(4r^2F(r)\). To determine the sign of \(F\) on the positive axis without numerical root-count assumptions, the coefficients in **descending** powers of \(t\) of \((1+t)^7F(4t/(1+t))\) are
\[
 (-42359,-194085,-313947,-181089,-14229,-12447,-729,-27),
\]
and those of \((1+t)^7F((4+12t)/(1+t))\) are
\[
 (-172719,-6143121,-7014411,-6340005,-5014413,-2274579,-501369,-42359).
\]
Every coefficient is negative, covering \(0\le r\le12\). Finally, \(F(12+t)\) has descending coefficients
\[
 (1,57,1332,16362,112050,409644,616761,-172719).
\]
By Descartes' rule this has exactly one positive root (there is one sign change, and the polynomial changes from negative to positive), establishing the uniqueness of \(r_*\in(12,13)\) and its simplicity. For \(0<r<r_*\), \(\operatorname{disc}_x P_r<0\): the quartic has exactly two real roots, one negative and one positive because \(P_r(0)<0\) and \(P_r(x)\to+\infty\) at either infinity. Therefore \(S'_3\) changes from positive to negative once on \((0,\infty)\). For \(r=20\), the exact signs \(P_r(1)<0<P_r(2)\), \(P_r(4)>0>P_r(5)\), and \(P_r(10)<0<P_r(16)\) exhibit three distinct positive roots. Because the discriminant has no other positive zero, these roots remain distinct for all \(r>r_*\), giving exactly two strict maxima. At the threshold, the additional two critical roots coalesce into a non-sign-changing double root, leaving exactly one strict maximum. This proves part 3.

## Verification

Run `python3 verify_succession.py` with a standard-library Python 3 interpreter. The script independently solves the exact stationary balance equations (rather than assuming the product formula), performs 49 exact rational stationarity comparisons for two through eight stages, and checks 245 exact/sign-inequality conditions for the designated alternating intensities. It regenerates the two all-negative Möbius polynomial coefficient arrays and the shifted-polynomial sign certificate, and verifies the discriminant identity as an **exact polynomial identity**: both sides have degree at most fourteen in \(r\), and equality is checked at fifteen distinct integer inputs using exact Sylvester determinants. It also checks the small three-stage example with forward rates \((100,1)\):
\[
 S_3(1)=\frac{5200}{10201},\qquad
 S_3(10)=\frac{4420}{14641},\qquad
 S_3(100)=\frac{10301}{20402}.
\]
For the same intensities the Shannon entropies are approximately \(0.741830412\), \(0.581578004\), and \(0.720920218\), respectively. These finite evaluations illustrate the theorem; the proof of all-stage behavior is analytical. The decimal entropies are not used as certificates for the theorem.

## Relationship to prior work

Johst and Huth (2005) studied precisely the ecological motivation: stage-structured landscapes subject to homogeneous disturbance, using stochastic succession and age-defined succession models, and documented **two** disturbance–diversity peaks. Their published analysis identifies the long-lived-intermediate-stage mechanism, presents four-stage examples and notes applicability to Simpson diversity. That two-peak observation and the model itself are prior work, not asserted as new here. The present finding instead proves an **unbounded number** of strict peaks using a single explicit rate hierarchy for **both** Shannon and Gini–Simpson indices, a sharp **three-stage minimum**, and an **exact necessary-and-sufficient three-stage Gini–Simpson rate threshold**. Those quantitative statements do not appear in the examined text. Solow and Smith (2006) analyze reverse-time inference in fitted Markov succession models rather than optimizing or counting disturbance–diversity modes.

## Limitations

The existence theorem permits strongly separated (possibly ecologically unrealistic) transition rates, even though the peak structure is stable to sufficiently small perturbations. It establishes **at least** \(n-1\) peaks and does **not** classify the maximum possible number for general \(n\). The sharp rate-ratio bifurcation applies only to three-stage Gini–Simpson diversity, not Shannon entropy. The statements concern diversity of successional **stages**, which can only be interpreted as species diversity under additional assumptions about their constituent assemblages. Spatially correlated disturbances, nonexponential transitions, stage-dependent reset hazards, multispecies interactions and stochastic finite-landscape sampling are outside the theorem. Although relevant literature was examined, bibliographic completeness and independent mathematical validation are not claimed.

## References

1. Johst, K., and Huth, A. (2005). *Testing the intermediate disturbance hypothesis: when will there be two peaks of diversity?* Diversity and Distributions 11(1), 111–120. DOI: 10.1111/j.1366-9516.2005.00133.x. First online publication: 14 January 2005.
2. Solow, A. R., and Smith, W. K. (2006). *Using Markov chain successional models backwards.* Journal of Applied Ecology 43(1), 185–188. DOI: 10.1111/j.1365-2664.2005.01127.x. First online publication: 9 January 2006.
3. Mackey, R. L., and Currie, D. J. (2001). *The diversity–disturbance relationship: is it generally strong and peaked?* Ecology 82(12), 3479–3492. DOI: 10.1890/0012-9658(2001)082[3479:TDDRII]2.0.CO;2. Used for background on empirical curve shapes, not as a proof of the Markov-stage theorem.
