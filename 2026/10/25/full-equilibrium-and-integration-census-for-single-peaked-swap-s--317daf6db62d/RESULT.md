# Full equilibrium and integration census for single-peaked swap Schelling games on cycles

## Finding
For every integer \(n\ge3\) and \(1\le b\le r=n-b\), consider the single-peaked swap Schelling game on a labeled cycle \(C_n\) at peak \(\Lambda=1/2\). In the notation defined below, its complete equilibrium integration polynomial is

\[
P_{n,b}(z)=\sum_{k=1}^{b}\frac{n}{k}[x^b y^r]\bigl(S(x,z)^kT(y,z)^k+T(x,z)^kS(y,z)^k-S(x,z)^kS(y,z)^k\bigr),
\]
where
\[
S(t,z)=tz+t^2z^2,\qquad T(t,z)=tz+\frac{t^2z^2}{1-t}.
\]
The coefficient \([z^j]P_{n,b}(z)\) counts labeled-vertex colorings that are pure swap Nash equilibria and have exactly \(j\) integrated agents. The coefficients are nonnegative integers, and their support is exactly
\[
\{b+\lceil b/2\rceil+1,\ b+\lceil b/2\rceil+2,\ldots,\min(n,3b)\}.
\]
In particular, the exact number of equilibrium colorings is
\[
E_{n,b}=\sum_{k=1}^{b}\frac{n}{k}\left[\binom{k}{b-k}\binom{r-1}{k-1}+\binom{b-1}{k-1}\binom{k}{r-k}-\binom{k}{b-k}\binom{k}{r-k}\right],
\]
with invalid binomial coefficients interpreted as zero. Moreover the exact degree-of-integration price of anarchy is
\[
\operatorname{PoA}(C_n,b,1/2)=\frac{\min(n,3b)}{b+\lceil b/2\rceil+1}.
\]
The central contribution is the complete equilibrium distribution, not just its extrema; the maximum-integrated equilibrium and price-of-stability-one property are consistent with existing general results.

## Assumptions and scope
Vertices \(0,\ldots,n-1\) of the simple cycle are distinguished; exactly \(b\) are blue and \(r=n-b\) red, with \(1\le b\le r\). All positions are occupied. A move swaps two agents of opposite colors only if *both* strictly improve their own utilities. Agents evaluate the fraction of same-color agents in their **closed** neighborhood, which consists of the agent and its two cycle neighbors. The strictly single-peaked symmetric utility at \(\Lambda=1/2\) has values \(p(1)=0\) and \(p(1/3)=p(2/3)>0\), so an agent has positive utility exactly when at least one of its two neighbors is of the opposite color. A vertex is *integrated* precisely in that case. A run is a maximal cyclic contiguous block of one color. With both colors present there are \(k\ge1\) runs of each color, alternating around the cycle. Identically colored agents are treated as interchangeable when counting vertex colorings; treating agents as individually labeled multiplies each count by \(b!r!\).

## Proof
**Equilibrium criterion.** The only two utility levels attainable here are zero and a common positive value. A mutually strictly profitable swap therefore requires both participating agents to be segregated (have two same-color neighbors). Conversely, take a segregated blue and a segregated red. They are not adjacent, since their neighbors have their own colors. After they swap, each lies between two agents of the *other* color and therefore becomes integrated; hence both improve. A color admits a segregated agent if and only if some run of that color has length at least three. Consequently, a coloring is a pure swap equilibrium exactly when **all runs of at least one color have size one or two**.

**Run polynomial.** A run of length \(\ell\ge1\) contributes \(\min(\ell,2)\) integrated vertices: the endpoints if \(\ell\ge2\), its sole vertex if \(\ell=1\). Thus a positive run whose length is limited to one or two has bivariate series \(S\), while an unrestricted positive run has series \(T\). For \(k\) blue and \(k\) red runs, the equilibrium criterion is the union of two restrictions: blue short or red short. Inclusion-exclusion gives the expression in parentheses of \(P_{n,b}\). An ordered pair of \(k\)-part compositions together with a marked starting vertex describes a coloring with a distinguished blue run; there are \(n\) possible starting vertices. Each coloring with \(k\) blue runs is represented exactly \(k\) times, explaining the factor \(n/k\). This bijection proves the exact coefficient-count claim and integrality, without interpreting individual fractional summands as counts. Substituting \(z=1\), using \([t^m](t+t^2)^k=\binom{k}{m-k}\) and \([t^m](t/(1-t))^k=\binom{m-1}{k-1}\), yields the stated finite sum for \(E_{n,b}\).

**Complete spectrum.** Every coloring has at most \(b\) integrated blue vertices; each of the at most \(b\) blue runs has at most two adjacent integrated red vertices. Hence \(I\le\min(n,3b)\). If all blue runs have length at most two, then their number \(k\) satisfies \(k\ge\lceil b/2\rceil\). When \(k<r\), some red run is not a singleton, so integrated red vertices number at least \(k+1\), giving \(I\ge b+\lceil b/2\rceil+1\). When \(k=r\), all red runs are singletons, so \(I=n\), which also satisfies the bound. If all red runs have length at most two, their number satisfies \(k\ge\lceil r/2\rceil\ge\lceil b/2\rceil\). If \(k<b\), at least \(k+1\) blue vertices are integrated, yielding \(I\ge r+k+1\ge b+\lceil b/2\rceil+1\). If \(k=b\), all blue runs are singletons and \(I=n\), again at least the bound.

For attainment, choose \(k\) blue runs with length one or two for each integer \(\lceil b/2\rceil\le k\le b\), and distribute the \(r\) red vertices over \(k\) nonempty runs. If \(k<r\), exactly \(u\) red runs can have length at least two, for every integer \(1\le u\le\min(k,r-k)\). The integrated count is \(I=b+k+u\). Thus, fixing \(k<r\), every integer in \([b+k+1,\, b+\min(r,2k)]\) is attained. For successive admissible values of \(k\), these intervals overlap or are adjacent because \(\min(r,2k)\ge k+1\) when \(k<r\). At \(k=b\), if \(r>b\) the final interval reaches \(b+\min(r,2b)=\min(n,3b)\). If \(r=b\), the last case has all singleton runs and attains \(I=n\); when \(b\ge2\), the preceding interval already reaches \(n-1\), while for \(b=1\) only \(I=3\) is possible. This proves precisely the stated contiguous support, including the smallest parameters.

**Price of anarchy.** The maximum possible integrated count among all placements is \(\min(n,3b)\): for \(r\ge2b\) place each blue between two distinct red agents; for \(r<2b\), place enough blues in separated groups of length one or two to integrate every red, and every blue, using \(b\le r\). Those maximum-integrated configurations are equilibria by the blue-short criterion. Dividing the optimum by the proved minimum-equilibrium integration proves the ratio. Existing literature already establishes price of stability one for the relevant almost-regular graph class; this argument also provides a direct construction here.

## Verification
The standalone `verify.py` enumerates opposite-color swap pairs directly, recomputes each agent's post-swap integration utility, and exhaustively enumerates all \(\binom nb\) vertex colorings for \(3\le n\le15\) and \(1\le b\le\lfloor n/2\rfloor\). It independently computes the run-composition coefficient polynomial with exact rational arithmetic. All 55 parameter pairs and 35,103 vertex colorings agree with the polynomial, exact total, and spectrum. Representative exact counts are \(E_{6,3}=14\) and \(E_{8,4}=46\). These finite checks are consistency evidence; the proof above establishes the claims for arbitrary \(n\).

## Relationship to prior work
Bilò, Bilò, Lenzner, and Molitor (2022) introduce the same single-peaked swap game and integration objective, prove existence and bounds, exhibit a ring family with price of anarchy approaching two (Theorem 8), and prove the price of stability is one for almost-regular graphs of maximum degree at most three (Theorem 12). Neither those two theorems nor the other relevant portions of that full text state the complete \((n,b,j)\)-resolved equilibrium census or the run-polynomial formula. An apparently similar integration extremum for single-peaked **jump** Schelling games uses unilateral vacant-vertex moves and does not count mutually profitable **swaps** in vacancy-free cycles. This theorem therefore emphasizes the new structural classification and exact integration distribution, rather than claiming the general qualitative extremal phenomena anew.

## Limitations
The result concerns static pure swap equilibria on fully occupied simple cycles with two colors, a common symmetric single-peaked utility peaking at one-half, and strict Pareto improvement of both swapped agents. It does not address asynchronous convergence, inequivalent preferences, additional colors, arbitrary graphs, or unilateral jumping. The finite program does not prove the general theorem independently. No claim of priority over all unindexed or unpublished work is made; analogous cyclic word enumerations could be independently rediscovered or recast using existing enumeration tools. Independent external mathematical validation has not been undertaken.

## References
1. D. Bilò, V. Bilò, P. Lenzner, and L. Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (first publicly posted 2022-04-26), https://arxiv.org/abs/2204.12599. Full author-posted manuscript also available at https://www.researchgate.net/publication/360234915_Tolerance_is_Necessary_for_Stability_Single-Peaked_Swap_Schelling_Games.
2. *Single-Peaked Jump Schelling Games*, arXiv:2302.12107, https://arxiv.org/abs/2302.12107 (distinct movement model, for comparison).
