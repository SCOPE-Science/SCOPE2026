# Eight-voter balanced-sextuple obstruction with four exact symmetry classes

## Finding
Let \(W=\{1,2,\ldots,8\}\). Choose exactly one four-element subset from each complementary pair \(\{A,W\setminus A\}\), and call the resulting family \(\mathcal F\). Let \(\mathcal M=\mathcal F\cup\{A\subseteq W:|A|\ge5\}\). This is a maximal standard family of majority coalitions.

**Theorem.** If six **pairwise distinct** sets \(A_1,\ldots,A_6\in\mathcal F\) satisfy
\[\sum_{j=1}^{6}\mathbf1_{A_j}(w)=3\quad\text{for every }w\in W,\]
then four **pairwise distinct** sets \(B_1,\ldots,B_4\in\mathcal F\) satisfy
\[\sum_{j=1}^{4}\mathbf1_{B_j}(w)=2\quad\text{for every }w\in W.\]
The set of all complement-free balanced six-families of distinct four-subsets of \(W\) consists of exactly \(35{,}280\) labelled families and precisely four orbits under the full permutation group of \(W\), of respective sizes \(5{,}040\), \(20{,}160\), \(3{,}360\), and \(6{,}720\).

**Corollary.** If a maximal standard eight-point social decision frame has incoherence index exactly \(6\), then every witnessing balanced length-six sequence must contain a repeated coalition. This is a necessary condition, not an existence assertion for such a frame.

## Assumptions and scope
Only the finite set \(W\) of size \(8\), the specified maximal choice of half-size coalitions, and ordinary pointwise incidence counts are used. A balanced family of length \(2r\) is a sequence of \(2r\) majority coalitions in which each voter occurs exactly \(r\) times. Repetitions are allowed in the *general* definition of coherence, but are explicitly excluded from the six-element hypothesis of this theorem. The result is about the middle layer of size-four subsets, not general arbitrary voting games.

## Proof
**Reduction to selected half-sets.** With six chosen members of \(\mathcal M\), if each voter occurs at most three times, the total incidence is at most \(24\). Every member of \(\mathcal M\) has size at least four, so all six must have size exactly four and all eight degrees must be exactly three. Similarly, any balanced length-four obstruction consists entirely of four-sets. Because precisely one of each complementary pair belongs to \(\mathcal F\), neither a balanced distinct six-family nor a balanced four-family can contain complementary pairs.

**Complete orbit census.** There are \(70\) four-subsets of \(W\) and \(35\) complementary pairs. Encode a six-family by six distinct four-subsets with degree three at every point and no complementary pair. Every such family admits a partition into two three-families. For each three-family \(T\), record the eight-component degree vector \(d(T)\). Pair all three-families whose vectors add to \((3,\ldots,3)\), retain only six distinct subsets without complements, and deduplicate the resulting six-families. This finite and complete computation gives \(35{,}280\) families. Apply each of the \(40{,}320\) point permutations to obtain the four orbits, with representatives (each row lists six coalitions) and sizes:

| Orbit size | Representative (concatenated vertex labels) |
|---:|---|
| \(5{,}040\) | 1234, 1235, 1267, 3678, 4568, 4578 |
| \(20{,}160\) | 1234, 1235, 1467, 2568, 3678, 4578 |
| \(3{,}360\) | 1234, 1256, 1278, 3457, 3568, 4678 |
| \(6{,}720\) | 1234, 1256, 1357, 2478, 3678, 4568 |

**Four local contradiction certificates.** Give each complementary pair \(\{S,W\setminus S\}\) a Boolean choice variable, represented by the unique member \(S\) containing vertex \(1\). A candidate balanced quartet forbids the conjunction that all its four oriented members are selected. The exhaustive incidence test produces exactly \(1{,}260\) distinct such forbidden signed quartets. Fix the six variables required by one representative. Repeatedly apply the elementary rule: if three literals of a forbidden quartet are already selected, its fourth must be rejected. The four representative instances give contradictions after respectively \(4\), \(5\), \(3\), and \(3\) forced assignments. In each instance, the final forbidden quartet has all four literals selected. All required choices are forced, so no completion of that six-family to a maximal \(\mathcal F\) can avoid a balanced quartet. The attached standalone checker constructs every family, all four orbits, every forbidden quartet, each inference, and the final conflict using exact integer arithmetic. Permuting the vertices transports these contradictions to every balanced distinct six-family. This proves the theorem.

**Index implication.** For maximal frames, a violating sequence of length six with no shorter violation must be balanced, because all six members have size at least four and each of eight voters can appear at most three times. The theorem shows that a sequence of six *distinct* members would force an earlier balanced length-four violation. Hence any index-six witness must have repetitions.

## Verification
Run `python checker.py` with Python 3; no third-party packages or external data are needed. The program enumerates \(70\) size-four subsets, \(35{,}280\) complement-free balanced distinct sextuples, four \(S_8\)-orbits, and \(1{,}260\) forbidden quartet patterns. It verifies all four unit-propagation contradictions and prints `ALL_CHECKS_OK`. An independent enumeration using five-subsets completed by their forced sixth member recovered the same \(35{,}280\) families; direct mixed-integer feasibility tests of sampled cases agreed with the forbidden-quartet obstruction. These finite exhaustive certificates cover the specified eight-point domain only.

## Relationship to prior work
Moss and Pedersen, *The Measurable Majority* (first posted 22 June 2026), introduce maximal standard frames, coherence and the incoherence index. Their appendix describes the eight-point index-six case as unresolved. The subsequent *Measurable Majorities Are Not Finitely Axiomatizable* (first posted 24 June 2026) establishes unbounded index by constructions on suitable larger universes. Neither inspected accessible statement supplies the four-orbit eight-point distinct-six obstruction proved here. General forbidden-intersection problems for four-sets have different predicates and do not directly give the degree-balanced conclusion. No assertion is made that the underlying balanced-trade terminology or the general coherence criterion is new.

## Limitations
The requirement that the six witnessing four-sets be **distinct** is essential to the proved domain. General coherence allows repeated coalitions. The computation and argument do not decide whether any eight-voter maximal standard frame has incoherence index six using such repetitions, nor do they prove any global lower bound for larger voter sets. An equivalent earlier incidence-design classification under other terminology remains a priority risk. Independent validation has not been performed.

## References
- Lawrence S. Moss and Arthur Paul Pedersen, *The Measurable Majority*, arXiv:2606.23853, initial public version 2026-06-22, especially §5 and Appendix B. https://arxiv.org/abs/2606.23853
- Lawrence S. Moss and Arthur Paul Pedersen, *Measurable Majorities Are Not Finitely Axiomatizable*, arXiv:2606.25954, initial public version 2026-06-24. https://arxiv.org/abs/2606.25954
