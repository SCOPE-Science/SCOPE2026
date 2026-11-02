# Ordered EF1 for all two-level valuations on the eight-good four-agent laminar key matroid

## Finding

**Theorem.** Let the eight goods be partitioned into three disjoint categories \(C_1=\{1,2,3\}\), \(C_2=\{4,5,6\}\), and \(C_3=\{7,8\}\). There are four agents, and a feasible bundle contains at most two goods and at most one good from each category. Each agent \(i\) has a nonnegative additive valuation taking at most two (agent-dependent) numerical values over the eight goods. For **every prescribed order** of the agents, a complete feasible allocation \((A_1,A_2,A_3,A_4)\) exists that is envy-free up to one good (EF1), and in which no agent envies an agent later in the prescribed order.

Here \(A_i\) is a pair of goods from two different categories; \(v_i(A_i)\ge v_i(A_j)\) whenever \(i<j\), and \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\) for some \(g\in A_j\) whenever \(i\ne j\). The indices are positions in the prescribed order, not fixed agent identities.

A finite exhaustive certificate establishes the binary-valued case for all \(2^{32}=4,294,967,296\) labeled valuation profiles. Equal-cardinality affine reduction gives the claimed continuum of two-level nonnegative valuations.

## Assumptions and scope

The feasibility family is the rank-two laminar matroid with total quota two and category quotas one on three category sets of sizes \((3,3,2)\). Every feasible **complete** allocation necessarily has exactly two goods per agent. Additivity and nonnegative singleton values are required; the low and high values can differ between agents, and agents may disagree arbitrarily about which goods they value highly. No nondegeneracy, strict ranking, or Pareto-optimality assumption is used. The statement concerns this key matroid only, not arbitrary four-colorable laminar matroids or the distinct twelve-good key matroid.

For one fixed prescribed order, a binary valuation is represented by an eight-bit integer \(x_i\in\{0,\ldots,255\}\) and \(s_i(B)=|B\cap S_i|\), where \(S_i\) contains the goods at set-bit positions. Bit positions zero through seven correspond to goods one through eight. The theorem permits zero-valued and all-valued masks.

## Proof

**Step 1 (all feasible allocations).** A complete allocation uses all eight goods and gives each agent a pair. Form an unordered perfect matching of eight goods, forbidding any pair whose goods belong to the same category. The recursive enumerator `rec` in `verify_exhaustive.cpp` chooses the first remaining good and pairs it with each remaining good in a different category, recursively. This generates every admissible unordered matching exactly once. The exact count is \(36\). Permuting its four pairs among four labeled agents yields all \(36\cdot4!=864\) feasible complete allocations, with no omissions or duplicates.

**Step 2 (the exact binary predicates).** For a binary mask \(x\), let \(c_x(B)=|B\cap S_x|\) for any pair \(B\). The required ordered-no-envy condition for agent \(i\) and later agent \(j\) is precisely \(c_{x_i}(A_i)\ge c_{x_i}(A_j)\). The EF1 condition for any ordered pair \(i\ne j\) is precisely \(c_{x_i}(A_i)\ge c_{x_i}(A_j)-\mathbf1_{c_{x_i}(A_j)>0}\). Since the envied bundle has two goods, EF1 fails **if and only if** \(c_{x_i}(A_i)=0\) and \(c_{x_i}(A_j)=2\). When \(i=1\), ordered no-envy already implies all its EF1 comparisons.

**Step 3 (complete exact finite enumeration).** For each of the \(864\) allocations \(A\), the program constructs a 256-bit set \(W(A)\) containing exactly those first-agent masks \(x_1\) for which \(c_{x_1}(A_1)\ge c_{x_1}(A_j)\) for \(j=2,3,4\). For each later position \(i\in\{2,3,4\}\), each mask \(x\), and each allocation \(A\), it marks \(A\) admissible for \((i,x)\) exactly when (a) the agent has no envy of any later agent and (b) no other bundle contains two approved goods while its own bundle has zero approved goods. The latter enforces EF1 against **all** other agents, including earlier agents.

For each triple \((x_2,x_3,x_4)\) of binary masks, it intersects these three 864-bit admissibility sets and unions \(W(A)\) over the allocations in the intersection. The resulting 256-bit union covers all masks \(x_1\) in **every one** of the \(256^3=16,777,216\) triples. The program checks coverage by comparing all four 64-bit words to all-one words; it does not sample masks. This proves, by a finite exhaustive calculation, that all \(256^4=4,294,967,296\) binary profiles have an allocation with both properties. `verify_exhaustive.cpp` is part of this package and recompiles without external mathematical libraries. The certificate is finite, not an assertion about an infinite search space or a timeout.

**Step 4 (two-level valuations).** For each agent, let the smaller singleton value be \(a_i\ge0\) and the larger be \(a_i+b_i\) with \(b_i\ge0\). The valuation of any set is \(v_i(B)=a_i|B|+b_i s_i(B)\). For the allocation obtained in Step 3, every agent's bundle and each other agent's bundle both have cardinality two; hence the no-envy inequalities for \(s_i\) remain true after multiplying by \(b_i\) and adding \(2a_i\). For EF1 choose the good removable in the binary case. Its removal leaves exactly one good, and
\[
v_i(A_i)-v_i(A_j\setminus\{g\})
=a_i+b_i\bigl(s_i(A_i)-s_i(A_j\setminus\{g\})\bigr)\ge0.
\]
Thus the same allocation works for every nonnegative two-level valuation. For an agent with \(b_i=0\), either bit mask may be used, and all comparisons remain valid. Relabeling the agents proves the claim for any prescribed order. \(\square\)

**Concrete stress instance.** Agent approval sets \(S_1=\{1,3,4,8\}\), \(S_2=\{1,2\}\), \(S_3=\{3,5,6\}\), and \(S_4=\{1,2,5,6\}\) admit ordered EF1 via \(A_1=\{1,4\}\), \(A_2=\{2,5\}\), \(A_3=\{3,7\}\), and \(A_4=\{6,8\}\). The two top-set dispersal requirements for agents three and four in Lemma 12 of the motivating paper cannot both hold for these approvals, so the new guarantee is not merely a consequence of that particular dispersal test.

## Verification

The bundled exhaustive checker (`verify_exhaustive.cpp`) prints `allocations=864 checked triples=16777216 binary preference profiles=4294967296 failed triples=0` and exits successfully after checking the exact Boolean coverage. To reproduce with a GNU-compatible C++17 compiler, run:

```sh
g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
python3 verify_independent.py
```

The independent Python checker constructs matchings separately and directly evaluates the literal EF1 condition by testing the removal of each good, rather than applying the compressed two-level predicate. Its deterministic tests cover 3,200 pseudorandom profiles and 65,536 structured profiles. The exhaustive proof relies on the complete C++ coverage, not these samples.

## Relationship to prior work

Cookson and Shah, *Constrained Fair Allocations via Partition Matroid Reductions* (first posted August 31, 2026), Definition 13 and Appendix B, isolate precisely the eight-good rank-two laminar key matroid. They reduce the arbitrary-valued four-agent laminar question to two key matroids but leave their ordered-no-envy EF1 existence unresolved; Lemma 12 gives an obstruction to a proposed **top-goods-separation method**, not a counterexample to EF1 itself. This theorem resolves the entire **heterogeneous two-level valuation class** of the eight-good key case with that stronger prescribed-order property.

Dror, Feldman and Segal-Halevi prove heterogeneous binary EF1 under partition matroids and only up to three agents under general common base-orderable matroids; neither result directly supplies four-agent ordered no-envy on this rank-two truncation of a three-category partition matroid. Akrami, Liu, Raj and Végh prove general matroid equitability and heterogeneous bi-valued **maximin-share** existence, but maximin-share inequalities do not imply the ordered-no-envy EF1 conditions here. This result does not claim novelty for ordinary unconstrained EF1 or for classical finite search and bitset methods.

## Limitations

The key eight-good instance has a fixed matroid and four agents; finite enumeration cannot establish the analogous result for more goods or the twelve-good key matroid. The argument is a reproducible exhaustive finite computational proof rather than a short hand-only structural classification of all profiles. It does not prove arbitrary additive valuations, EFX, efficiency, strategyproofness, or the original full four-agent laminar conjecture. Literature searches cannot rule out unindexed equivalent results; an independent scientific audit has not occurred.

## References

1. Benjamin Cookson and Nisarg Shah, *Constrained Fair Allocations via Partition Matroid Reductions*, arXiv:2608.31121, August 31, 2026, especially Appendix B, Definitions 13–14 and Lemma 12. https://arxiv.org/abs/2608.31121
2. Amitay Dror, Michal Feldman, and Erel Segal-Halevi, *On Fair Division under Heterogeneous Matroid Constraints*, arXiv:2010.07280, initial posting October 14, 2020; revised full-text version April 24, 2022. https://arxiv.org/pdf/2010.07280
3. Hannaneh Akrami, Siyue Liu, Roshan Raj, and László A. Végh, *Matroids are Equitable*, Combinatorica 46, article 22 (2026), DOI:10.1007/s00493-026-00217-y; particularly Theorem 1.12. https://doi.org/10.1007/s00493-026-00217-y
