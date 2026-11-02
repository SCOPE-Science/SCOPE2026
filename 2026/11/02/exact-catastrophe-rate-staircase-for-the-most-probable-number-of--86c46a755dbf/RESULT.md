# Exact catastrophe-rate staircase for the most probable number of occupied habitat patches

## Finding

In an exchangeable finite-patch colonization/extinction system with synchronized complete resets, the stationary number of occupied patches has **one mode or one adjacent pair of tied modes**, for every positive catastrophe rate. As the catastrophe rate increases, its mode makes a strict, consecutive downward staircase; the number and ordering of all thresholds can be determined without numerically solving a Markov generator.

Precisely, let \(N\ge2\), \(a,b,c>0\), \(s=a+b\), \(\rho=a/s\), and \(\alpha=c/s\). Write \(P_k(\alpha)=\mathbb P\{K=k\}\) for the stationary count probability. Define
\[
 h=\lceil(N+1)\rho\rceil-1\quad(0\le h\le N).
\]
There exist exactly \(h\) distinct critical positive catastrophe ratios
\[
1>\alpha_0>\alpha_1>\cdots>\alpha_{h-1}>0,
\qquad P_{k+1}(\alpha_k)=P_k(\alpha_k)\quad(0\le k<h).
\]
There are no other adjacent-probability equalities at positive catastrophe rates. For \(\alpha>\alpha_0\), the unique mode is zero; on decreasing \(\alpha\), the unique mode advances successively through \(1,2,\ldots,h\), crossing \(k\leftrightarrow k+1\) only at \(\alpha_k\). At each critical ratio exactly the indicated adjacent pair maximizes the mass. If \(h=0\), the unique mode is always zero. For \(\alpha\ge1\) the entire mass sequence is strictly decreasing.

Equivalently, for any \(0\le k<N\), the ratio \(P_{k+1}(\alpha)/P_k(\alpha)\) is strictly decreasing from \((N-k)\rho/[(k+1)(1-\rho)]\) at \(\alpha\downarrow0\) to zero as \(\alpha\to\infty\). The crossing at one occurs if and only if \(k<h\).

## Assumptions and scope

There are exactly \(N\) permanently available patches. Each empty patch becomes occupied independently at per-patch rate \(a>0\) through an exogenous propagule source. Each occupied patch empties independently at rate \(b>0\). A shared independent Poisson catastrophe clock of rate \(c>0\) instantaneously empties *all* patches, regardless of current occupancy. Between catastrophes patches evolve independently. The count \(K\in\{0,1,\ldots,N\}\) has birth rate \((N-k)a\), ordinary death rate \(kb\), and an additional reset transition from every state \(k>0\) to state zero at rate \(c\). The chain is finite, irreducible and has a unique stationary law. No local density dependence, site heterogeneity, propagule depletion or partial catastrophes are assumed.

## Proof

**Regeneration and exact probabilities.** In the stationary regime, the time \(T\) since the most recent global reset has the exponential law with rate \(c\). Starting empty at a reset, a single patch is occupied after age \(t\) with probability \(\rho(1-e^{-st})\). Conditional on \(T\), the \(N\) patch occupancy indicators are independent. The transformation \(U=1-e^{-sT}\) has density \(\alpha(1-u)^{\alpha-1}\), \(0<u<1\). Thus
\[
P_k(\alpha)=\binom Nk\alpha\int_0^1(\rho u)^k(1-\rho u)^{N-k}(1-u)^{\alpha-1}\,du.
\]
Every mass is positive; the integral sums to one over \(k\). The exact finite-expression form, useful for rational verification, is
\[
P_k=\binom Nk\rho^k\sum_{j=0}^{N-k}\binom{N-k}{j}(-\rho)^j\frac{(k+j)!}{(1+\alpha)_{k+j}},
\]
where \((z)_m=\prod_{i=0}^{m-1}(z+i)\) and \((z)_0=1\).

**Strictly decreasing adjacent ratios.** Fix \(k<N\). Normalize the strictly positive density proportional to \(u^k(1-\rho u)^{N-k}(1-u)^{\alpha-1}\), and let \(\mathbb E_{k,\alpha}\) denote expectation under it. Then
\[
\frac{P_{k+1}}{P_k}=\frac{(N-k)\rho}{k+1}\,
\mathbb E_{k,\alpha}\!\left[\frac{U}{1-\rho U}\right].
\]
If \(\alpha'>\alpha\), the ratio of the two normalized densities is proportional to \((1-u)^{\alpha'-\alpha}\), which is strictly decreasing in \(u\). Because \(u/(1-\rho u)\) is strictly increasing, the expectation, hence the mass ratio, decreases strictly. The \(\alpha\downarrow0\) tilted density converges to a point mass at one, yielding the displayed binomial ratio; the \(\alpha\to\infty\) density concentrates at zero, yielding ratio zero. Therefore \(P_{k+1}=P_k\) at exactly one positive \(\alpha\) precisely when \(k+1<(N+1)\rho\), equivalent to \(0\le k<h\).

**Unimodality and consecutive thresholds.** Write \(\Delta_k=P_{k+1}-P_k\). The stationary balance equation for \(1\le k<N\) gives
\[
 b(k+1)\Delta_k=a(N-k+1)\Delta_{k-1}+(c-a-b)P_k.
\]
If \(0<c<a+b\), once any \(\Delta_{k-1}\le0\), the next difference is strictly negative. Consequently an initially rising stationary sequence can become falling at most once, and can have at most one plateau involving adjacent positions. If \(c\ge a+b\), the boundary equation \(aP_{N-1}=(Nb+c)P_N\) implies \(\Delta_{N-1}<0\), whereas any earlier nonnegative difference would force all subsequent differences nonnegative through the recurrence, a contradiction. Thus every difference is negative in this regime.

Every positive crossing lies in \(\alpha<1\). At the crossing \(\Delta_k(\alpha_k)=0\), with \(k<h-1\), the recurrence at index \(k+1\) gives \(\Delta_{k+1}(\alpha_k)<0\). Since the next adjacent ratio decreases strictly as \(\alpha\) increases, its unique unit crossing must occur at a strictly smaller parameter: \(\alpha_{k+1}<\alpha_k\). The sign pattern proves that these and only these are the global-mode switches. At a crossing the neighboring modes are equal and both strictly exceed every other probability.

**Exact illustrative classification.** For \(N=4\) and \(\rho=1/2\), \(h=2\). With \(D=(\alpha+1)(\alpha+2)(\alpha+3)(\alpha+4)\),
\[
P_0-P_1=\frac{2\alpha^4+12\alpha^3+16\alpha^2-6\alpha-9}{2D},\qquad
P_1-P_2=\frac{(2\alpha+3)(\alpha^2+3\alpha-1)}{D}.
\]
Hence \(\alpha_1=(\sqrt{13}-3)/2\), and \(\alpha_0\) is the unique positive zero of the displayed quartic, lying strictly between \(18/25\) and \(721/1000\). Its numerical value is approximately \(0.72023635\). At \(\alpha=1\), \(1/2\) and \(1/4\) the exact stationary probabilities, indexed by occupied count zero through four, are respectively
\[
(31,26,16,6,1)/80,\quad(83,100,84,40,8)/315,\quad(587,984,1040,576,128)/3315.
\]
Their unique modes are zero, one and two. This demonstrates two separate sharp modal changes for the same patches and the same colonization and local-extinction rates.

## Verification

The standalone `checker.py` uses only Python's standard library. It evaluates the finite stationary mass expression in exact rational arithmetic, checks normalization and all count-state balance equations for a grid of population sizes, local occupancy ratios and catastrophe ratios, verifies the contiguous sign property and strictly decreasing adjacent ratios on that grid, and reproduces the three exact example vectors and rational isolation brackets. Run `python checker.py` from the extracted package directory. The infinite-parameter claims are proved by the preceding renewal and monotonicity arguments, not by finite testing.

## Relationship to prior work

Artalejo, Economou and López-Herrero (2007) study immigration models with binomial/geometric catastrophes and extinction/population-growth measures. Kapodistria, Phung-Duc and Resing (2015) develop equilibrium factorial moments, distributions and stochastic ordering for a linear, unbounded birth/immigration–death process with binomial catastrophes. The new setting has *finite vacant sites*, saturating birth rates and synchronized total reset. Their stochastic-monotonicity conclusions do not themselves determine the stationary modal index or its complete strictly ordered threshold staircase. The catastrophe-age regeneration device is standard and is not claimed as new. Earlier patch-occupancy ecological studies motivate the distinction between population-level typical occupancy and mean occupancy. The assessed contribution is only the exact all-parameter mode and threshold classification for this explicitly stated model.

## Limitations

The claim is about the stationary most probable occupied-patch *count*, not a spatial occupancy pattern, extinction time, ecological viability or observed metapopulation dynamics. It depends on exchangeable independent patches between shared total resets; correlation from dispersal, heterogeneous patches, partial disaster losses or non-Poisson catastrophes may invalidate the classification. For fixed \(\alpha>0\) the stationary count is neither independent-binomial nor a conventional unscaled beta-binomial mixture. The historical-priority comparison is based on accessible primary text and bounded searches; undetected related literature remains possible. No independent scientific audit has been performed.

## References

1. J. R. Artalejo, A. Economou, M. J. López-Herrero, “Evaluating growth measures in an immigration process subject to binomial and geometric catastrophes,” *Mathematical Biosciences and Engineering* 4 (2007), 573–594. https://doi.org/10.3934/mbe.2007.4.573 (publicly available August 2007).
2. S. Kapodistria, T. Phung-Duc, J. Resing, “Linear birth/immigration-death process with binomial catastrophes,” EURANDOM Preprint 2015-006, March 16, 2015. https://studyres.com/doc/16917218/linear-birth-immigration-death-process-with-binomial
3. K. L. Evans, J. J. D. Greenwood, K. J. Gaston, “The roles of extinction and colonization in generating species–energy relationships,” *Journal of Animal Ecology* 74 (2005), 498–507. https://doi.org/10.1111/j.1365-2656.2005.00948.x
