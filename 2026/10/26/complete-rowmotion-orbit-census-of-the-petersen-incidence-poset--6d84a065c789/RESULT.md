# Complete rowmotion orbit census of the Petersen incidence poset

## Finding

Let \(P\) be the Petersen graph and let \(Q=\operatorname{Inc}(P)\) be its vertex–edge incidence poset. On the set \(J(Q)\) of all order ideals, classical rowmotion \(R\) has exactly \(133958\) states, \(6207\) cycles, and \(39\) distinct cycle lengths. Its complete cycle multiplicities \(c_\ell\) are:

| Length | Cycles | Length | Cycles | Length | Cycles |
|---:|---:|---:|---:|---:|---:|
| 2 | 891 | 21 | 10 | 64 | 30 |
| 3 | 11 | 22 | 90 | 66 | 30 |
| 5 | 5 | 24 | 15 | 68 | 30 |
| 6 | 685 | 28 | 300 | 72 | 60 |
| 7 | 10 | 32 | 120 | 74 | 60 |
| 8 | 456 | 33 | 40 | 88 | 60 |
| 10 | 715 | 34 | 60 | 92 | 30 |
| 11 | 10 | 36 | 180 | 100 | 60 |
| 12 | 510 | 40 | 30 | 116 | 30 |
| 14 | 690 | 42 | 80 | 118 | 60 |
| 16 | 120 | 44 | 90 | 120 | 24 |
| 18 | 70 | 52 | 75 | 136 | 30 |
| 20 | 390 | 60 | 20 | 192 | 30 |

Every unlisted length has multiplicity zero. Consequently,
\[
\operatorname{ord}(R)=356800176532800,
\qquad \max\{\ell:c_\ell>0\}=192,
\]
and precisely thirty cycles have length \(192\). There are no fixed ideals. The order has eleven distinct prime divisors:
\[
356800176532800=2^6\,3^2\,5^2\,7\,11\,13\,17\,23\,29\,37\,59.
\]

## Assumptions and scope

The Petersen graph is the simple graph on the ten vertices \(u_i,v_i\), \(i\in\mathbb Z/5\mathbb Z\), with fifteen edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). The poset \(Q\) consists of a minimal element for each graph vertex and a maximal element for each graph edge; a vertex is less than exactly those edge elements incident to it. An ideal contains the two endpoints of every edge element that it contains. The claim concerns *ordinary* rowmotion, not birational rowmotion, and counts fully distinct labelled ideals without quotienting by graph automorphisms.

## Proof

Write an ideal uniquely as \((U,F)\), where \(U\subseteq V(P)\) is the selected vertex set and \(F\subseteq E(P[U])\) is the selected edge set in the induced graph on \(U\). Every such pair is an ideal, and no other pairs are ideals. Define \(E(U)=\{ab\in E(P):a,b\in U\}\). The minimal elements of the complement of \((U,F)\) are exactly the omitted vertices \(V(P)\setminus U\) and the omitted edges whose two endpoints are already selected, namely \(E(U)\setminus F\). Taking their downward closure gives the exact transition
\[
F'=E(U)\setminus F,\qquad
U'=(V(P)\setminus U)\cup\bigcup_{ab\in F'}\{a,b\}.
\]
This identifies rowmotion on **every** admissible ideal, with no unproved state-space restriction.

The finite enumeration loops over every one of the \(2^{10}\) choices of \(U\), and then over every subset \(F\) of \(E(U)\); each admissible pair appears exactly once. It constructs the successor of every pair using the displayed transition, and traverses disjoint cycles until all ideals have been removed from the unvisited set. As a composition of the elementary toggles from the upper rank to the lower rank, rowmotion is bijective; the verifier also explicitly checks that every traversal closes at its own starting ideal. The resulting multiplicities are displayed above. The arithmetic checks are
\[
\sum_{\ell} c_\ell=6207,\qquad
\sum_{\ell}\ell c_\ell=133958,\qquad
\operatorname{lcm}\{\ell:c_\ell>0\}=356800176532800.
\]

For an independent check of the transition, the supplied verifier also computes rowmotion by toggling each selected or unselected maximal edge element, then each minimal vertex element, according to the ideal legality rule. Both maps agree on all \(133958\) states in the generalized-Petersen model \(GP(5,2)\). The entire census is then recomputed from a second, combinatorially distinct model of the Petersen graph: the Kneser graph \(KG(5,2)\) of pairwise disjoint two-subsets of a five-element set. That second census uses only the toggle transition and gives the identical \(39\) multiplicities.

## Verification

The standalone Python 3 program `verify_petersen_rowmotion.py` uses only the standard library. Run `python3 verify_petersen_rowmotion.py` from the directory containing this file. It regenerates the two graph models, enumerates every ideal, verifies closure and transition equality, checks that every cycle closes without collisions, and compares every length multiplicity. The final line is `VERIFY_OK`. Its exact histogram and arithmetic checks can be inspected or changed in the program; no inaccessible dataset or library is required.

## Relationship to prior work

Grinberg and Roby introduce the general rowmotion formalism and determine orders on a class of skeletal posets in their 2014 preprint (eventually published in 2016). Their full-text Sections 10 and 11 concern recursively grafted or disjoint unions of graded posets. The Petersen incidence poset is connected, and no element of either rank is comparable with all elements of the other rank; hence it does not arise from the final nontrivial graft operation defining a connected height-two skeletal poset. In particular, their inductive order formulas do not supply this census.

Elizalde, Plante, Roby and Sagan study exact rowmotion orbits on *fences*, whose Hasse diagrams are paths (arXiv:2108.12443, initially posted in 2021). The present poset's Hasse graph is the subdivision of the Petersen graph, not a path; their fence orbit formulas do not specialize to it. The new enumeration concerns a distinct natural non-skeletal height-two poset with an unexpectedly varied period structure, rather than a restatement of a known periodicity theorem.

## Limitations

This result is an exact, finite, computationally reproducible census for one specified \(25\)-element poset, not a uniform theorem for arbitrary incidence posets, graphs, or higher-rowmotion analogues. The enumerator verifies all ideal states but does not provide a shorter symbolic classification of its cycles. Prior unindexed computational tables could contain equivalent counts. Independent audit has not been performed.

## References

- D. Grinberg and T. Roby, *Iterative properties of birational rowmotion I: generalities and skeletal posets*, arXiv:1402.6178 (first posted 2014-02-25); *Electronic Journal of Combinatorics* 23(1), P1.33 (2016), Sections 1, 10, 11. https://arxiv.org/abs/1402.6178
- S. Elizalde, M. Plante, T. Roby, and B. E. Sagan, *Rowmotion on fences*, arXiv:2108.12443 (first posted 2021-08-27). https://arxiv.org/abs/2108.12443
