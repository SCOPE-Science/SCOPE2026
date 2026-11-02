# Exact equilibrium run census and parity-dependent welfare loss on a balanced odd cycle

## Finding

For each integer \(m\geq 2\), consider the two-type diversity-seeking jump game on the undirected cycle \(C_{2m+1}\) with \(m\) agents of type A, \(m\) agents of type B, all strategic, and exactly one vacant vertex. The utility of an agent is the fraction of its **occupied** neighboring vertices bearing the opposite type (utility zero when it has no occupied neighbors). An agent may jump to the vacant vertex, leaving its former vertex vacant; a pure Nash equilibrium has no strictly profitable such jump.

Fix a vacancy, and read the \(2m\) occupied types in cyclic order starting immediately after it. A coloring is a pure Nash equilibrium **if and only if** (i) its first and last types differ, (ii) its first and last monochromatic runs each have length one, and (iii) every monochromatic run has length at most two.

Write \(W\) for the sum of all agents' utilities, and \(E_m(k)\) for the number of equilibrium **colorings of the labeled vertices**, with the \(m\) agents of each type indistinguishable, whose welfare is \(2k\). Then

\[
E_m(k)=
\begin{cases}
2(2m+1)\binom{k-1}{m-k}^{2},&\lceil(m+1)/2\rceil\leq k\leq m,\\
0,&\text{otherwise}.
\end{cases}
\]

Every admissible \(k\) occurs. In particular,

\[
\min_{\mathrm{NE}}W=2\left\lceil\frac{m+1}{2}\right\rceil,
\qquad \max_{\mathrm{NE}}W=\operatorname{OPT}=2m.
\]

Thus the exact price of anarchy for this game is

\[
\operatorname{PoA}(m)=\frac{m}{\lceil(m+1)/2\rceil}
=\begin{cases}
\dfrac{2m}{m+2},&m\text{ even},\\
\dfrac{2m}{m+1},&m\text{ odd},
\end{cases}
\qquad \operatorname{PoS}(m)=1.
\]

If individuals of the same type are instead distinguished by labels, multiply each count \(E_m(k)\) by \((m!)^2\); welfare and equilibrium characterizations are unchanged.

For comparison, the published exact price of anarchy for a **line topology** with \(2m\) balanced agents is \(2m/(m+2)\). Closing the line into a cycle with one vacancy yields the same worst-case ratio for even \(m\), but a strictly larger one for odd \(m\). The parity effect is an exact structural distinction, not an asymptotic claim.

## Assumptions and scope

The graph is the simple undirected cycle on \(2m+1\) distinguishable vertices, with \(m\geq2\). All \(2m\) agents are strategic; there are no stubborn agents, no heterogeneous utilities, and only one empty vertex. There are precisely two types with equal multiplicities, and type labels are distinct. An occupied vertex has either one or two occupied neighbors, so the zero-neighbor utility convention does not enter this family. A deviation is unilateral and moves one occupant into the unique currently vacant vertex; its source becomes vacant before the new utility is evaluated. The equilibrium definition forbids strictly profitable deviations, not neutral moves. The price-of-anarchy and price-of-stability ratios use the sum of the \(2m\) utilities, and the optimum ranges over all placements with the same type multiplicities and one vacancy.

## Proof

**Step 1 (the vacancy's two neighbors must differ).** Rotate the vertex labels so the empty vertex is \(0\), and write the occupied word at vertices \(1,\ldots,2m\). Suppose its endpoints are both type A. All \(m\) B agents lie at interior positions. Any B agent jumping to vertex \(0\) would receive utility \(1\), because both neighbors of \(0\) are A and neither is its old location. In equilibrium, each B agent must therefore already have utility \(1\), forcing a type-A neighbor on both sides. Thus all \(m\) B letters are isolated in the occupied word, which begins and ends in A. Isolating \(m\) B letters in that fashion requires at least \(m+1\) A letters, contradicting the exact A count \(m\). The case of two B endpoints is symmetric. Therefore the endpoints differ in every equilibrium.

**Step 2 (necessary and sufficient run criterion).** Rename the types if necessary so position \(1\) is A and position \(2m\) is B. If the A at position \(1\) jumps to vacancy \(0\), its only occupied neighbor at its new location is the type-B agent at position \(2m\), and its new utility is \(1\). Consequently, equilibrium forces the old utility of the first agent to be \(1\), so position \(2\) must be B. Similarly, position \(2m-1\) must be A. The first and last monochromatic runs therefore have length one.

For any occupant of an interior vertex \(j\in\{2,\ldots,2m-1\}\), jumping to vacancy \(0\) leaves the A and B endpoints in place. Its post-jump utility is exactly \(1/2\). In equilibrium, it must already have utility at least \(1/2\), meaning at least one of its two occupied neighbors differs from its own type. Combined with the just-established endpoint condition, this says exactly that no monochromatic run has length three or more.

Conversely, suppose the first and last letters differ and their runs have length one, while all other runs have length at most two. Both endpoint agents already have utility \(1\), so neither can strictly improve by jumping. Every interior agent already has at least one unlike neighbor and thus utility at least \(1/2\); its post-jump utility would be exactly \(1/2\). No agent can strictly improve. This proves the equivalence.

**Step 3 (run count and welfare).** Every equilibrium word starts in A and ends in B, or vice versa. Hence it contains the same number \(k\) of runs of each type, or \(2k\) runs altogether. Each of the \(k\) A runs has length one or two, but the first A run (or, in the reverse orientation, the last A run) is constrained to length one; the same is true for B. Thus each type count lies between \(k\) and \(2k-1\). Since each type count is exactly \(m\),

\[
\left\lceil\frac{m+1}{2}\right\rceil\leq k\leq m.
\]

Every such \(k\) is realizable: choose exactly \(m-k\) of the \(k-1\) unrestricted A runs and exactly \(m-k\) of the \(k-1\) unrestricted B runs to have length two; give all remaining runs length one.

The occupied vertices form a path after deleting vertex \(0\). Every unlike-color edge contributes \(1\) to total welfare when neither endpoint is an endpoint of this path: each incident agent receives \(1/2\) from that edge. An unlike-color edge at either end of the path contributes \(3/2\): the path endpoint receives utility \(1\) from its sole neighbor, and its interior neighbor receives \(1/2\). The path has exactly \(2k-1\) unlike-color edges (one between each pair of successive runs). Both boundary edges are unlike-colored because the first and last runs have length one. Hence

\[
W=(2k-1)+\tfrac12+\tfrac12=2k.
\]

**Step 4 (exact enumeration).** There are \(2m+1\) choices of the vacant vertex and two choices for the color of the first occupied vertex. Once these are fixed, the \(k\) runs of each color are ordered. One run of each color has its length fixed at one by the endpoint condition. To obtain exactly \(m\) letters of that color, exactly \(m-k\) of its remaining \(k-1\) runs must have length two. This yields \(\binom{k-1}{m-k}\) choices for each color, independently. Multiplying gives \(E_m(k)\). No duplication is possible because the vacancy position, first color, and run lengths are uniquely reconstructed from the coloring. Distinguishable agents simply permute within each type, multiplying the count by \((m!)^2\).

**Step 5 (efficiency extrema).** Every individual utility is at most \(1\), so \(\operatorname{OPT}\leq2m\). An alternating occupied word with one vacancy achieves utility \(1\) for every agent; by Step 2 it is also an equilibrium, proving \(\operatorname{OPT}=\max_{\mathrm{NE}}W=2m\). By Steps 3–4, the smallest equilibrium welfare is attained at \(k=\lceil(m+1)/2\rceil\) and equals twice that number. Division yields the stated \(\operatorname{PoA}\) and \(\operatorname{PoS}\) formulas, including the exact parity split. \(\square\)

## Verification

Run `python3 verify_cycle_game.py` with Python 3's standard library. The self-contained program constructs all \((2m+1)\binom{2m}{m}\) colorings for each \(1\leq m\leq7\), independently computes each mover's pre- and post-deviation payoff, compares the resulting equilibrium predicate to the run criterion, accumulates the exact welfare spectrum, and compares counts against the binomial formula. Every such check passed. As examples: \(m=3\) gives \(14\) equilibria at welfare \(4\) and \(14\) at welfare \(6\); \(m=5\) gives \(22,198,22\) equilibria at welfare \(6,8,10\), respectively. These finite checks are corroboration; the proof above establishes all \(m\geq2\).

## Relationship to prior work

Narayanan, Sabbagh and Voudouris introduce the diversity-seeking jump model and prove potential-game results for regular graphs with one vacancy (Theorem 5.1 of the expanded version); this ensures convergence of improving moves but does not classify equilibrium colorings or their welfare. Their exact balanced two-type price-of-anarchy formula for a **line** (Theorem 6.4) has a different topology and different unilateral deviations at its endpoints. The present result supplies a new odd-cycle census, exact welfare distribution, and a parity-sensitive comparison to that line value. The prior article's universal balanced-type welfare bound \(\operatorname{PoA}\leq2\) remains consistent with the stricter finite formulas above.

The single-peaked jump Schelling game of Friedrich and coauthors uses nonmonotone preference functions and has different equilibrium requirements. The later variety-seeking game of Narayanan and coauthors counts distinct neighboring types rather than the fraction of unlike occupied neighbors; its binary-type utility is not the fraction-based utility used here.

## Limitations

The theorem does not cover unequal type populations, multiple vacancies, stubborn agents, more than two types, cycle graphs of even size with one vacancy and unequal colors, or non-cycle graphs. The price-of-anarchy comparison concerns the specified all-strategic games, not other social welfare notions. The enumeration counts color patterns on fixed labeled vertices; a relabeling factor is supplied explicitly for distinct same-type individuals. Equivalent enumerations under different terminology in literature not identified by the cited comparison remain a bibliographic risk.

## References

1. L. Narayanan, Y. Sabbagh, and A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, arXiv:2305.17757, first posted 2023-05-28, https://arxiv.org/abs/2305.17757 . Expanded open-access version: *Autonomous Agents and Multi-Agent Systems* 39, 32 (2025), https://doi.org/10.1007/s10458-025-09714-8 . Relevant parts: model definition and Theorems 5.1, 6.1, 6.4.
2. T. Friedrich, P. Lenzner, L. Molitor, and L. Seifert, *Single-Peaked Jump Schelling Games*, arXiv:2302.12107, 2023, https://arxiv.org/abs/2302.12107 .
3. L. Narayanan, J. Opatrny, S. Tummala, and A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, IJCAI 2025, https://doi.org/10.24963/ijcai.2025/446 .
