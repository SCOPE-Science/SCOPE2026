# Sharp observation-budget staircase for stable miscoordination in two-size sampling dynamics

## Finding

Consider the one-population symmetric two-action coordination game in which matching on action \(a\) yields payoff \(u>1\), matching on \(b\) yields \(1\), and mismatching yields \(0\). In the continuous-time sampling best-response dynamics, a share \(\alpha\in(0,1)\) of new agents samples two independent population actions, and the other share samples \(k\ge2\), responding optimally to the sampled payoffs and choosing \(a\) on exact ties. Let \(p\) be the population share playing \(a\).

**Sharp observation-budget theorem.** There exists a mixture share \(\alpha\in(0,1)\) with an asymptotically stable interior population state if and only if
\[
\boxed{k>2(u+1).}
\]
Equivalently, the **least feasible larger sample size** is
\[
\boxed{k_{\min}(u)=\lfloor 2(u+1)\rfloor+1,\qquad u>1.}
\]
This is a complete, unbounded integer staircase in the payoff advantage: for example \(k_{\min}=5\) when \(1<u<3/2\), \(k_{\min}=6\) when \(3/2\le u<2\), and \(k_{\min}=7\) when \(2\le u<5/2\). All equality cases are included, rather than excluded as generic payoff parameters.

The sufficient direction is constructive, with an explicit rational mixing share independent of the magnitude of \(u\) inside each staircase cell. Whenever \(k>2(u+1)\), put
\[
C=\binom{k}{3},\qquad \varepsilon=\frac{1}{4C},\qquad
\alpha=\frac12+\frac{\varepsilon^2}{8}.
\]
Then the dynamics has an attracting interior stationary state and at least one further interior stationary state separating its basin from the pure state \(p=1\). Thus, for every \(u>1\), finite heterogeneous sampling can maintain miscoordination, but no smaller observation budget can do so when one subpopulation observes exactly two actions.

## Assumptions and scope

The population has unit mass and follows the autonomous ODE
\[
\dot p=w(p)-p,\qquad
w(p)=\alpha[1-(1-p)^2]+(1-\alpha)F_m^k(p),
\]
where \(X\sim\operatorname{Binomial}(k,p)\), \(F_m^k(p)=\Pr(X\ge m)\), and \(m=\lceil k/(u+1)\rceil\). The tie-breaking rule is fixed in favor of \(a\), exactly as in the motivating source; equality at an integer sample threshold is therefore significant. Samples are independent draws with replacement from the current population. The model is deterministic at the infinite-population level. All quantifiers in the finding range over real \(u>1\), integers \(k\ge2\), and possible mixing shares \(0<\alpha<1\). An attracting interior equilibrium means local asymptotic stability for this one-dimensional ODE, not merely a finite-time metastable state.

## Proof

**1. A structural polynomial lemma.** The small-sample response is always \(F_1^2(p)=2p-p^2\) because \(u>1\). Set \(m=\lceil k/(u+1)\rceil\). In the low-observation regime \(k\le 2(u+1)\), one has \(m\le2\).

If \(m=1\), then \(F_1^k(p)=1-(1-p)^k\ge p\) and \(2p-p^2>p\) for \(0<p<1\). Therefore \(\dot p>0\) on the open interval and no interior stationary state is attracting.

If \(m=2\), necessarily \(k\ge3\). Introduce the odds coordinate \(y=p/(1-p)>0\), and multiply the drift by the strictly positive factor \((1+y)^{k-2}/[p(1-p)]\). An exact binomial expansion and Pascal's identity give
\[
\frac{(1+y)^{k-2}}{p(1-p)}(w(p)-p)
=2\alpha-1+
\sum_{j=1}^{k-2}
\left[\binom{k-2}{j}+(1-\alpha)\binom{k-2}{j+1}\right]y^j.
\]
Every nonconstant coefficient is strictly positive. For \(\alpha\ge1/2\), the polynomial is positive for every \(y>0\); for \(0<\alpha<1/2\), it has exactly one positive zero, changing sign from negative to positive. Thus any interior stationary state is repelling, never asymptotically stable. This proves the **necessary** condition uniformly for all sample sizes and all payoff values, including ties.

**2. Explicit construction at and above the sharp threshold.** Suppose \(k>2(u+1)\). Then \(m\ge3\), whereas \(m\le k-1\), and \(C=\binom{k}{3}>0\). The binomial triple-union bound gives, for every \(p\in[0,1]\),
\[
F_m^k(p)\le\Pr(X\ge3)\le Cp^3.
\]
At \(p=\varepsilon=1/(4C)\) and \(\alpha=1/2\),
\[
\dot p=\tfrac12\{F_m^k(\varepsilon)-\varepsilon^2\}
\le-\frac38\varepsilon^2.
\]
Increase the mixing share to \(\alpha=1/2+\varepsilon^2/8\), which lies strictly between zero and one. Since both response probabilities lie in \([0,1]\), changing \(\alpha\) changes the drift at \(\varepsilon\) by at most \(\varepsilon^2/8\). Therefore
\[
\dot p\big|_{p=\varepsilon}\le-\frac14\varepsilon^2<0.
\]
Near zero, \(F_m^k(p)=O(p^3)\), so
\[
\dot p=(2\alpha-1)p+O(p^2)>0
\]
for all sufficiently small positive \(p\). Near one, \(m\le k-1\) implies \(F_m^k(p)=1-O((1-p)^2)\) and the small-sample response has the same property, whence \(\dot p=(1-p)+O((1-p)^2)>0\) sufficiently near one. By continuity, the drift crosses from positive to negative between zero and \(\varepsilon\), yielding a locally asymptotically stable interior equilibrium; it crosses back from negative to positive between \(\varepsilon\) and one, yielding a further interior separator. A nonzero polynomial cannot change sign without an odd-multiplicity root, so no genericity assumptions are hidden in the crossing argument.

**3. Exact minimal size and staircase.** The forbidden regime is \(k\le2(u+1)\), whereas the construction works for every integer \(k>2(u+1)\). The least allowed integer is exactly \(\lfloor2(u+1)\rfloor+1\), proving both directions and every boundary claim.

## Verification

A standalone standard-library script `verify.py` recomputes binomial-tail polynomials over many rational payoff regimes, directly checks the exact odds-coordinate identity for all integer sample sizes from three through thirty, verifies the positivity of every nonconstant coefficient, confirms the staircase threshold at rational and tie-boundary payoff inputs, and checks the explicit constructive drift inequalities in exact rational arithmetic. It is run with `python verify.py`. The infinite theorem is supplied by the symbolic argument above, not by extrapolating the finite checks.

At \(u=3/2\), the first admissible larger sample size is \(k=6\). Here \(C=20\), \(\varepsilon=1/80\), and \(\alpha=1/2+1/51200\); every smaller \(k\) is excluded for *every* possible mixing share. At \(u=2\), an exact sample tie forces the threshold to jump to \(k=7\).

## Relationship to prior work

Arigapudi, Heller and Schreiber's *Heterogeneous Noise and Stable Miscoordination*, arXiv:2305.10301, defines precisely this sampling best-response ODE in Section 2 and proves in Theorem 2 that sufficiently large sampling heterogeneity can stabilize an interior state for suitable distributions. Its Theorem 1 establishes the opposing instability of homogeneous populations. Its discussion of Oyama, Sandholm and Tercieux (2015) addresses related sufficient conditions for global convergence. The present theorem identifies an **exact minimal finite large-sample observation budget for every payoff advantage** when the small sample size is fixed to two, with explicit constructive mixture shares and the complete cutoff including all tie boundaries; this sharp if-and-only-if statement is not a consequence of the cited qualitative existence result.

The lowest payoff plateau \(1<u<3/2\) admits a direct fixed-degree proof of the five-observation boundary. The substantive extension here is the uniform all-payoff minimum-size law, its infinitely many higher plateaus and precise tie transitions, obtained from an all-degree coefficient argument and an explicit binomial concentration certificate.

## Limitations

The result is specific to the two-point sample-size distribution with one support point exactly two, the common positive coordination payoff advantage \(u>1\), independent binomial sampling, the source's favorable tie-breaking convention and continuous-time deterministic one-population dynamics. It is not a characterization for arbitrary sample-size mixtures, asymmetric two-population games, or logit/finite-population stochastic dynamics. Its existential assertion does not characterize all stable states or all viable mixture shares for larger sample sizes. Unindexed specialist results could establish an equivalent observation-budget cutoff; no independent audit is claimed.

## References

1. S. Arigapudi, Y. Heller and A. Schreiber, *Heterogeneous Noise and Stable Miscoordination*, arXiv:2305.10301v1, first publicly posted 2023-05-17; expanded full-text version arXiv:2305.10301v2, 2025-01-25. https://arxiv.org/abs/2305.10301 ; https://arxiv.org/html/2305.10301v2
2. H. Oyama, W. H. Sandholm and O. Tercieux (2015), related sampling dynamics and sufficient global-convergence results, as compared in Section 2.6 of Arigapudi, Heller and Schreiber, arXiv:2305.10301.
