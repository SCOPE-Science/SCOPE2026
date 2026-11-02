# Exact joint top-cycle and Pareto cardinalities in three- and four-agent house allocation

## Finding

Under impartial culture (independent uniform strict rankings), the complete joint law of the numbers of majority-top-cycle assignments and Pareto-optimal assignments is given by the 42 exact entries in the table below, for three and four labeled agents and the same number of labeled houses. The result is an exact finite-population classification, not an asymptotic approximation.

For four agents, the marginal top-cycle law is:

| Top-cycle size | Number of labeled profiles | Exact probability |
|---:|---:|---:|
| 1 | 31,104 | \( 3/32 \) |
| 2 | 20,736 | \( 1/16 \) |
| 21 | 288 | \( 1/1152 \) |
| 22 | 15,552 | \( 3/64 \) |
| 23 | 25,056 | \( 29/384 \) |
| 24 | 239,040 | \( 415/576 \) |

In particular, a completely nonselective top cycle of all 24 assignments occurs with probability \(415/576\). Precisely 18,432 profiles (probability \(1/18\)) have a full top cycle yet only three Pareto-optimal assignments. The expected top-cycle size is \(1299/64\), the expected Pareto-optimal set size is \(1597/288\), and the top cycle strictly contains the Pareto-optimal set in \(11663/13824\) of all profiles. The rare four-agent top-cycle size 21 occurs with probability \(1/1152\).

The complete joint table (duplicated in the machine-readable `joint_counts.csv`) is:

| Agents | Top-cycle size | Pareto size | Labeled profiles |
|---:|---:|---:|---:|
| 3 | 1 | 1 | 48 |
| 3 | 2 | 2 | 36 |
| 3 | 4 | 3 | 36 |
| 3 | 4 | 4 | 18 |
| 3 | 6 | 3 | 36 |
| 3 | 6 | 4 | 36 |
| 3 | 6 | 6 | 6 |
| 4 | 1 | 1 | 31,104 |
| 4 | 2 | 2 | 20,736 |
| 4 | 21 | 4 | 288 |
| 4 | 22 | 3 | 1,152 |
| 4 | 22 | 4 | 3,456 |
| 4 | 22 | 5 | 1,728 |
| 4 | 22 | 6 | 4,320 |
| 4 | 22 | 7 | 576 |
| 4 | 22 | 8 | 2,016 |
| 4 | 22 | 9 | 576 |
| 4 | 22 | 10 | 1,152 |
| 4 | 22 | 12 | 288 |
| 4 | 22 | 14 | 288 |
| 4 | 23 | 3 | 1,152 |
| 4 | 23 | 4 | 6,912 |
| 4 | 23 | 5 | 5,760 |
| 4 | 23 | 6 | 3,744 |
| 4 | 23 | 7 | 4,032 |
| 4 | 23 | 8 | 1,152 |
| 4 | 23 | 9 | 1,728 |
| 4 | 23 | 11 | 576 |
| 4 | 24 | 3 | 18,432 |
| 4 | 24 | 4 | 43,200 |
| 4 | 24 | 5 | 40,896 |
| 4 | 24 | 6 | 31,968 |
| 4 | 24 | 7 | 40,896 |
| 4 | 24 | 8 | 23,400 |
| 4 | 24 | 9 | 10,368 |
| 4 | 24 | 10 | 13,968 |
| 4 | 24 | 11 | 5,760 |
| 4 | 24 | 12 | 5,592 |
| 4 | 24 | 14 | 3,744 |
| 4 | 24 | 16 | 216 |
| 4 | 24 | 18 | 576 |
| 4 | 24 | 24 | 24 |

## Assumptions and scope

For \(n\in\{3,4\}\), agents and houses are labeled \(\{0,\ldots,n-1\}\). A preference profile \(P=(\succ_0,\ldots,\succ_{n-1})\) gives each agent a strict total order on all houses. Every one of the \((n!)^n\) profiles has equal probability. An assignment \(\mu\) is a bijection from agents to houses, encoded by the tuple \((\mu(0),\ldots,\mu(n-1))\).

For distinct assignments \(\mu,\lambda\), put an edge \(\mu\to\lambda\) when at least as many agents prefer their house in \(\mu\) to their house in \(\lambda\) as prefer their house in \(\lambda\) to their house in \(\mu\). An indifferent agent, receiving the same house, contributes zero. A tied majority comparison creates both directed edges. The **top cycle** \(\mathrm{TC}(P)\) consists of those assignments from which every assignment is reachable by a finite directed path (including the length-zero path to itself). A matching is in \(\mathrm{PO}(P)\) if no other assignment weakly improves every agent and strictly improves at least one. The reported joint coordinates are \((|\mathrm{TC}(P)|,|\mathrm{PO}(P)|)\).

This is the weak-majority (Smith/top-cycle) convention used in the cited assignment literature, and it is distinct from the top-trading-cycles mechanism. No preference ties, capacities beyond one, endowments, or nonuniform priors are considered.

## Proof

This finite theorem admits an exhaustive mathematical certificate with a provably complete search space. Fix a number of agents \(n\) equal to three or four. Let \(\mathfrak S_n\) be the set of all \(n!\) permutations, used both as strict rankings and as agent-to-house assignments.

**Step 1: Canonical representatives.** Relabel the houses simultaneously so that agent zero has ranking \((0,1,\ldots,n-1)\). Every original labeled profile has exactly one normalized representative, since a strict ranking of the first agent uniquely specifies the relabeling. Conversely each normalized representative has exactly \(n!\) differently house-labeled profiles. Both output cardinalities are invariant under house relabeling. Consequently enumerating all \((n!)^{n-1}\) choices for the other agents and multiplying counts by \(n!\) is exact, neither a sample nor a quotient that loses multiplicities. There are 36 normalized profiles at \(n=3\) and 13,824 at \(n=4\).

**Step 2: Majority adjacency.** For each ordered pair of assignments compute the signed integer margin

\[
m_P(\mu,\lambda)=\sum_{i=0}^{n-1}\bigl(\mathbf1_{\mu(i)\succ_i\lambda(i)}-\mathbf1_{\lambda(i)\succ_i\mu(i)}\bigr).
\]

Add \(\mu\to\lambda\) precisely when the margin is nonnegative. The code performs direct ranking comparisons, so ties and unchanged house recipients are handled without floating point.

**Step 3: Complete reachability and Pareto test.** Calculate the complete transitive closure of this graph on exactly \(n!\) vertices. For each assignment, test reachability of every other assignment; the number passing is by definition \(|\mathrm{TC}(P)|\). Independently, for each assignment, loop through the remaining \(n!-1\) assignments and test whether any gives every agent a weakly better house and some agent a strictly better one. Count the assignments with no dominator to obtain \(|\mathrm{PO}(P)|\). Increment the unique joint cell and multiply by the orbit size \(n!\). Every possible input profile and every possible rival assignment is visited, which proves the displayed finite distribution if the listed algorithms execute as specified.

**Step 4: Redundant implementation and exact arithmetic.** `census.cpp` uses 24-bit integer reachability masks and Floyd–Warshall closure. `verify.py` instead builds explicit adjacency sets, performs breadth-first reachability independently from every assignment, and uses a separately written Pareto test. Both compute the same 42 joint counts; the second tests every cell against the embedded `joint_counts.csv`. The CSV sums to \(216=6^3\) profiles at three agents and \(331776=24^4\) at four agents. This is a complete small finite domain and requires no unverified asymptotic extrapolation.

There are additional hand-counted crosschecks: \(24/4^4=3/32\) of four-agent profiles have four distinct top houses and a singleton top cycle. There are exactly 20,736 four-agent profiles with two top-cycle assignments, counted by choosing which pair of agents shares a first and second choice, the ordered shared first and second houses, the two remaining top houses, and the allowed suffix orderings; this matches the direct enumeration and the small-cycle characterization of the source.

## Verification

Run `g++ -O2 -std=c++17 census.cpp -o census && ./census` to independently print all joint cells, followed by `python3 verify.py` to recalculate every normalized profile with a disjoint graph-reachability implementation and assert equality with the provided CSV. Both programs require only the standard C++ and Python libraries. The finite certificate is the exhaustive combinatorial enumeration, checked by two different algorithms; numerical approximation is not used. The machine-readable data are in `joint_counts.csv`.

## Relationship to prior work

Brandt, Chen, Dong, Lederer and Schlenga (2026) introduce the assignment majority graph, prove inclusion of the Pareto set in its top cycle, and characterize allowed top-cycle sizes for \(n\ge5\). Their Remark 3 identifies the allowed sizes for three and four agents and the two symmetry types of the four-agent 21-assignment exception. **None of those allowed sizes or the existence of the exception is claimed new here.** The present result is the previously unstated exact prevalence of every size and, more importantly, the full joint distribution with Pareto efficiency. The source analyzes uncovered-set size frequencies in five-agent markets, but its inspected sections do not provide this three-/four-agent joint law. The earlier general top-cycle characterization by Brandt and Lederer (2023) studies incentive properties in ordinary elections, not the house-allocation joint count.

## Limitations

The theorem is exclusively for independent uniform strict profiles with three or four agents/houses. It does not extend the finite table to larger markets, to incomplete rankings or to other stochastic preference models. The main paper's size restrictions are already known; only the exact frequencies, joint Pareto classification, and derived prevalence statements are new claims. Exhaustive computation certifies this finite domain, not an arbitrary-population theorem. An unindexed equivalent table or unpublished enumeration is a remaining priority risk; there has been no independent external audit of this package.

## References

1. Felix Brandt, Haoyuan Chen, Chris Dong, Patrick Lederer, and Alexander Schlenga, *Majoritarian Assignment Rules*, arXiv:2602.14816v1, first public version February 16, 2026, https://arxiv.org/html/2602.14816v1 ; especially Section 4.1, Remark 3, and Appendix B.
2. Felix Brandt and Patrick Lederer, *Characterizing the Top Cycle via Strategyproofness*, Theoretical Economics 18 (2023), 837–883, https://doi.org/10.3982/TE5120 .
