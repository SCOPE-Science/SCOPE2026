# Ten species are the sharp threshold for survival-dependent protection of an entire pollination guild

## Finding

**Theorem.** Let \(G=(P\sqcup Q,E)\) be any finite, simple, connected bipartite plant–pollinator graph with both guilds nonempty. Every pollinator independently survives with the common probability \(p\in(0,1)\), except that exactly one chosen pollinator is guaranteed to survive. A plant is considered retained precisely if at least one of its original pollinator neighbors survives. Let \(R_j(p)\) be the probability that **every plant** is retained after guaranteeing pollinator \(j\in Q\).

If \(|P|+|Q|\le 9\), then there exists a pollinator \(j\) maximizing \(R_j(p)\) simultaneously for every \(p\in(0,1)\). More strongly, its coefficients in the survival-subset (Bernstein) expansion dominate the corresponding coefficients of every other pollinator.

This is sharp at ten species. For five plants and five pollinators \(A,B,C,D,E\), use plant-neighborhood sets

\[
\{A,B\},\quad \{A,C\},\quad \{B,C,D\},\quad \{B,C,E\},\quad \{B,D,E\}.
\]

In this connected graph, \(B\) is the **unique** optimal protected pollinator for \(0<p<1/2\), while \(A\) is uniquely optimal for \(1/2<p<1\); only \(A,B\) tie at \(p=1/2\). In particular, ten species are necessary and sufficient for a change in the optimum in this model.

## Assumptions and scope

The graph is unweighted, undirected, finite, simple, bipartite and connected, with nonempty plant and pollinator classes. All nonprotected pollinators survive independently with the **same** probability \(p\), and exactly one is perfectly protected. Plants do not suffer independent primary loss: each is present if and only if at least one of its original pollinator neighbors remains. The joint objective is the probability **all** plants remain, not the expected number of plants, nor network connectivity or long-term dynamical coexistence. No new interactions or rewiring arise.

For each protected pollinator \(j\), and \(0\le k\le |Q|-1\), define

\[
c_j(k)=\#\{S\subseteq Q\setminus\{j\}:|S|=k,\ \text{every plant has a neighbor in }S\cup\{j\}\}.
\]

Then, with \(r=|Q|\), the exact probability is

\[
R_j(p)=\sum_{k=0}^{r-1}c_j(k)p^k(1-p)^{r-1-k}.
\]

The coefficients count successful configurations; they are not normalized binomial probabilities. Hence if \(c_j(k)\ge c_i(k)\) for all \(k\), then \(R_j(p)\ge R_i(p)\) for all \(0<p<1\).

## Proof

**(1) Exact finite reduction.** If either guild has size one, the conclusion is immediate: there is only one protection choice or all choices are equivalent by connectedness. Otherwise write \(m=|P|\ge2\) and \(r=|Q|\ge2\). Number the pollinators \(0,\ldots,r-1\). A plant can be encoded by a nonzero \(r\)-bit neighborhood mask. Permuting plants leaves the protection objective unchanged; consequently every bipartite graph is represented by exactly one nondecreasing sequence of \(m\) masks drawn from \(1,\ldots,2^r-1\). The connectedness requirement excludes isolated resources and disconnected incidence networks; it is checked by breadth-first search on the bipartite graph. Pollinator labels are **not** quotiented, so no isomorphism-class completeness assumption is required.

**(2) Exhaustive coefficientwise dominance.** For each \(m,r\ge2\) with \(m+r\le9\), enumerate every nondecreasing mask sequence. For each connected case, for each protected pollinator \(j\), and for all \(2^{r-1}\) subsets of the remaining pollinators, test coverage of every plant and increment precisely one \(c_j(k)\). Examine all \(r\) coefficient vectors and assert that some \(j\) satisfies \(c_j(k)\ge c_i(k)\) simultaneously for every other \(i\) and all \(k\). The full finite search covers **64,820** connected row-multiset representatives and has **zero failures**. The counts by total species \(m+r=4,5,6,7,8,9\) are respectively \(3,16,87,588,5158,58968\); the more granular \((m,r)\) counts are included in `certificate.json`. The transparent standalone generator `verify_joint_protection.py` replays this exhaustive check without third-party dependencies. The loop bounds and coverage of all row-mask representatives above turn the finite verification into a proof of the finite-size claim; no infinite extrapolation is involved.

**(3) Sharp witness.** For the displayed ten-species graph, encode the five plant neighborhoods, in the bit order \(A,B,C,D,E\), as \((3,5,14,22,26)\). Direct subset enumeration gives the coefficient vectors \((c_j(0),\ldots,c_j(4))\):

\[
\begin{array}{c|ccccc}
  j&0&1&2&3&4\\\hline
  A&0&1&6&4&1\\
  B&0&2&5&4&1\\
  C&0&1&5&4&1\\
  D&0&0&4&4&1\\
  E&0&0&4&4&1
\end{array}
\]

Thus \(A\) strictly dominates \(C,D,E\) for every \(0<p<1\), while the only remaining comparison is

\[
R_B(p)-R_A(p)=p(1-p)^3-p^2(1-p)^2
  =p(1-p)^2(1-2p).
\]

The prefactor is strictly positive inside \((0,1)\), so the sign changes once, exactly at \(p=1/2\). This proves both the claimed unique optima and sharpness of the nine-species result.

## Verification

Run `python3 verify_joint_protection.py` with Python 3.9 or later (standard library only). Compare its full JSON output with `certificate.json`. The program independently constructs each incidence graph by nondecreasing plant masks, checks connectedness by a bipartite breadth-first search, evaluates all survival subsets using integer arithmetic, and tests coefficientwise domination. It also checks the witness coefficients exactly and performs an additional direct rational-probability survival-state summation at \(p=1/4,1/2,3/4\). Every check succeeds. Finite tests are applied only to the finite cutoff; positivity of the coefficient basis and the exact polynomial factorization establish the assertions for **all real** \(p\in(0,1)\).

## Relationship to prior work

Bascompte, Jordano, Melián and Olesen (2003) analyzed the nested incidence structure of mutualistic plant–animal networks and its potential consequences for persistence. Kaiser-Bunbury and collaborators (2010) studied pollination-network response to species removal and rewiring through empirical simulations, but did not present a finite exact joint-persistence protection classification. In classical coherent-system reliability, component-importance rankings and improvement actions were studied by Butler (1977); the present event is specifically a positive conjunctive normal form, one clause per plant, with its connected incidence graph and one component set perfectly reliable. The exact **ten-total-species cutoff**, its stronger coefficientwise statement below the cutoff, and the switching graph are the claims assessed here, not the underlying reliability representation or general importance concept.

The expected number of retained plants is a distinct objective: summing marginal plant-survival probabilities does not determine the probability that *all* plants survive. In particular, earlier finite expected-richness comparisons do not imply the joint-persistence theorem. An equivalent prior classification under coherent reliability, stochastic set cover, or monotone Boolean-function terminology remains possible.

## Limitations

This is a finite structural cutoff and an exact worst-case counterexample, not a model of measured community resilience. The proof is exhaustive for graphs with at most nine total species and analytical for the ten-species witness; it does not classify all ten-species exceptions or assert uniqueness of the witness. The claims do not cover heterogeneous or correlated extinctions, imperfect protection, partial persistence objectives, plant primary extinction, rewiring, or long-term ecological dynamics. Literature coverage cannot establish absolute priority without independent bibliographic scrutiny.

## References

- D. A. Butler, *Technical Note—An Importance Ranking for System Components Based upon Cuts*, Operations Research **25** (1977), 874–879. https://doi.org/10.1287/opre.25.5.874 (online date 1977-10-01; abstract inspected).
- J. Bascompte, P. Jordano, C. J. Melián and J. M. Olesen, *The nested assembly of plant–animal mutualistic networks*, PNAS **100** (2003), 9383–9387. https://doi.org/10.1073/pnas.1633576100 (first online 2003-07-24; full author-posted text inspected).
- C. N. Kaiser-Bunbury, S. Muff, J. Memmott, C. B. Müller and A. Caflisch, *The robustness of pollination networks to the loss of species and interactions*, Ecology Letters **13** (2010), 442–452. https://doi.org/10.1111/j.1461-0248.2009.01437.x (first online 2010-01-21; full author-available text inspected).
- P. Romero, *Uniformly optimally reliable graphs: a survey*, Networks **80** (2022), 466–481. https://doi.org/10.1002/net.22085 (online 2021-12-06; abstract and bibliography examined).
