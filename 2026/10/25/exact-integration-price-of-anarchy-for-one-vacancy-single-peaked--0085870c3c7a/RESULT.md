# Exact integration price of anarchy for one-vacancy single-peaked Schelling cycles

## Finding

In the single-peaked jump Schelling game on the cycle \(C_{r+b+1}\), with \(r\ge b\ge1\) red and blue agents, precisely one vacancy, and single-peaked utility \(p\) with preference peak \(\Lambda=1/2\), write \(I(\sigma)\) for the number of agents having at least one occupied neighbor of the opposite color. For all \(r+b\ge3\),
\[
\max_\sigma I(\sigma)=\min\{r+b,3b\},\qquad
\min_{\sigma\in\mathrm{NE}} I(\sigma)=b+\left\lceil\frac b2\right\rceil+1.
\]
Consequently, the exact integration price of anarchy is
\[
\operatorname{PoA}(C_{r+b+1},r,b,1/2)=
\frac{\min\{r+b,3b\}}{b+\lceil b/2\rceil+1}.
\]
For the exceptional triangle with \(r=b=1\), both optimum and equilibrium minimum equal \(2\), and the price of anarchy is \(1\). The formula is independent of the precise shape of \(p\) within the source model's admissible class. In the imbalanced regime \(r\ge2b\), the ratio tends to \(2\) from below as \(b\to\infty\).

## Assumptions and scope

The graph is the simple undirected cycle with \(r+b+1\ge3\) vertices. Each of the \(r+b\) agents has one of two colors; every site except one is occupied. The utility of agent \(i\) is \(p(f_i)\), with \(f_i\) the fraction of her *closed occupied neighborhood* (including herself) occupied by her own color. The function \(p\) obeys the single-peaked assumptions of Friedrich et al.: its peak is \(1/2\), it strictly increases below the peak, and \(p(f)=p(1-f)\) above the peak, with \(p(1/2)=1\) and \(p(1)=0\). A unilateral move relocates an agent to the one previously vacant site; a pure Nash equilibrium (NE) admits no strict utility-improving move. The degree of integration \(I\) counts agents with at least one occupied opposite-color neighbor. Optimization is over *all* placements with the specified color counts, not only equilibria. No stochastic dynamics, other peaks, extra vacancies, or higher-degree graphs are claimed.

## Proof

**1. Reduction of deviations and exact equilibrium criterion.** Every occupied vertex has one or two occupied neighbors. Its own-color fraction belongs to \(\{1/3,1/2,2/3,1\}\). By the stated utility rules, the corresponding utility levels are \(q,1,q,0\), respectively, with \(0<q<1\). An agent of utility \(1\) cannot improve. An agent of utility \(q\) has two occupied neighbors and is not adjacent to the vacancy. Moving to the vacancy then leaves its original site nonadjacent to the destination, so the destination has two occupied neighbors; the resulting utility cannot exceed \(q\). Hence *only segregated (zero-utility) agents can improve*. This also follows from the potential argument in Theorem 2.4 of the source, but the direct calculation here fixes the exact action convention.

Delete the unique vacant vertex and read the \(r+b\) occupied sites in path order. If the vacant vertex has two red neighbors, a segregated blue agent can jump there and obtain utility \(q>0\). Conversely, no segregated red agent can gain by that jump: after moving it sees only red occupied neighbors, whether or not its previous site was adjacent to the vacancy. Thus this placement is an NE exactly when every blue agent has at least one red neighbor. Interchanging colors gives the criterion for a vacancy with two blue neighbors. If the vacancy has one neighbor of each color, a segregated agent of either color would gain by jumping there; hence a placement of this kind is an NE exactly when *every* occupied agent is integrated. These three cases are exhaustive.

**2. Sharp minimum equilibrium integration.** Suppose the vacancy has two red neighbors. Then the occupied path begins and ends in red. Every blue agent must be integrated at equilibrium, so every maximal blue run has length at most two: a run of length at least three would contain a segregated blue agent. Let \(c\) be the number of nonempty blue runs. Since there are \(b\) blue agents, \(c\ge\lceil b/2\rceil\). The \(c\) blue runs have \(c+1\) *distinct* adjacent red run-boundary agents, each integrated. Thus
\[
I\ge b+c+1\ge b+\lceil b/2\rceil+1.
\]
For a blue–blue vacancy the analogous argument gives \(I\ge r+\lceil r/2\rceil+1\), at least as large because \(r\ge b\). A red–blue vacancy forces every agent to be integrated, giving \(I=r+b\), also no smaller than \(b+\lceil b/2\rceil+1\) whenever \(r+b\ge3\) and \(r\ge b\); for \(b\ge2\), use \(r\ge b\ge\lceil b/2\rceil+1\), and for \(b=1\) use \(r\ge2\).

To attain this lower bound, put \(c=\lceil b/2\rceil\) nonempty blue runs of sizes at most two, totaling \(b\), into a red-terminated occupied path, separated by a *single* red agent and with a single red agent at each end. There are exactly \(c+1\) integrated red agents and all \(b\) blue agents are integrated. Extra red agents are added at the beginning of the path, where they have no blue neighbor and do not change this count. This uses at most \(r\) red agents: for \(b\ge2\), \(c+1\le b\le r\), and for \(b=1\) in the nonexceptional case \(r\ge2\). The vacant vertex lies between the two red ends, and the equilibrium criterion in step 1 applies. When \(r=b=1\), the occupied pair on the triangle consists of opposite colors, so both are integrated and no strict improvement is possible.

**3. Sharp unrestricted optimum.** Every integrated blue agent contributes at most \(b\) to \(I\). Each blue agent has degree two and can expose at most two distinct red agents, so there are at most \(2b\) integrated red agents. Hence \(I\le\min\{r+b,3b\}\). This upper bound is attainable with one vacancy:

If \(r=b\), alternate the colors along the occupied path. Every agent meets the other color. If \(b+1\le r\le2b\), arrange the \(b\) blue agents as isolated singleton runs between \(b+1\) nonempty red runs, the two terminal red runs having length one and the \(b-1\) internal red runs each having length one or two. The total number of red agents can be any integer from \(b+1\) to \(2b\), and every red and blue agent is integrated. If \(r>2b\), start from the preceding arrangement with exactly \(2b\) red agents and add the remaining reds to one terminal red run. The original \(2b\) red agents touching blue still remain integrated, and the \(b\) blue agents remain integrated, giving \(3b\). This proves the optimum and the quotient.

## Verification

The standalone Python program `verify_cycle_enum.py` enumerates every red/blue/vacant placement, every possible unilateral jump, and the degree of integration using exact rational utilities \(p(f)=2\min\{f,1-f\}\). It independently checks both extremal formulas for all pairs \(1\le b\le r\le9\) with \(r+b\le15\), and checks the triangle exception. The enumerations are finite diagnostics and do **not** replace the arbitrary-size run argument. The chosen piecewise-linear utility realizes the same strict preference ordering among the attainable fractions as every admissible \(p\), so the exact equilibrium classification is insensitive to the utility's detailed curvature.

## Relationship to prior work

Friedrich, Lenzner, Molitor, and Seifert (2023), arXiv:2302.12107v1, define this exact jump model and degree of integration. Their Theorem 2.4 proves convergence on one-vacancy cycles at the half peak, Theorem 4.3 gives the general price-of-anarchy upper bound \(\min\{\Delta_G,(r+b)/(b+1)\}\), and their Section 4.2 implies the price of stability is \(1\) here. These facts do not supply the exact *worst-equilibrium* integration count in terms of the color populations or the exact resulting price of anarchy. The present result supplies that finite-parameter classification and matching extremal constructions, not a new proof of price of stability. Bilò et al. (2022) treat the related *swap* game without vacancy; Agarwal et al. (2021) study a distinct monotone preference model. Neither action/preference convention yields the formula merely by identifying the words “Schelling game.”

## Limitations

The result requires a single vacancy, a cycle, two agent colors, and the exact half peak. Deviations, utilities and equilibrium conditions can change with additional vacancies or different peaks. An exhaustive bibliographic uniqueness assertion is not proved; specialized treatments of one-vacancy cycles may exist beyond the identified sources. No equilibrium distribution or dynamic convergence rate is asserted.

## References

1. T. Friedrich, P. Lenzner, L. Molitor and L. Seifert, “Single-Peaked Jump Schelling Games,” arXiv:2302.12107v1, first public 2023-02-23. https://arxiv.org/html/2302.12107v1
2. D. Bilò, V. Bilò, P. Lenzner and L. Molitor, “Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games,” IJCAI 2022. https://www.ijcai.org/proceedings/2022/12
3. A. Agarwal, E. Elkind, J. Gan, A. Igarashi, W. Suksompong and A. A. Voudouris, “Schelling games on graphs,” Artificial Intelligence 301 (2021), article 103576. https://doi.org/10.1016/j.artint.2021.103576
