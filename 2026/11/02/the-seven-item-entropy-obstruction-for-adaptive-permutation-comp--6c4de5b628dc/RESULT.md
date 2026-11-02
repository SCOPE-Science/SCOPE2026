# The seven-item entropy obstruction for adaptive permutation comparisons

## Finding

Let \(\mathcal R_n\) be the Boolean concept class consisting of all strict total orders on \([n]=\{0,\ldots,n-1\}\). Its query domain is the collection of unordered pairs \(\{a,b\}\) with \(a<b\), and the answer to query \((a,b)\) is one exactly when \(a\) precedes \(b\) in the order. Define \(\operatorname{Ldim}\) through complete binary trees in which each internal node chooses one comparison, and every binary root-to-leaf answer sequence is realized by at least one order.

**Theorem.** The exact Littlestone dimensions through seven elements are
\[
\begin{array}{c|rrrrrrr}
 n&1&2&3&4&5&6&7\\ \hline
 |\mathcal R_n|&1&2&6&24&120&720&5040\\
 \operatorname{Ldim}(\mathcal R_n)&0&1&2&4&6&9&11\\
 \lfloor\log_2(n!)\rfloor&0&1&2&4&6&9&12.
\end{array}
\]
In particular, seven is the first order at which the elementary cardinality upper bound on Littlestone dimension is **not attainable** by pairwise-comparison queries. On seven items an adaptive depth-eleven comparison tree is shattered, but no adaptive depth-twelve tree is shattered.

The classical nonadaptive comparison-support characterization gives \(\operatorname{VCdim}(\mathcal R_n)=n-1\) for positive \(n\). It is recalled only for comparison and is **not** claimed as a new static VC calculation. For every positive integer \(s\), the entire unrestricted class \(\mathcal R_{6s}\) satisfies
\[
\operatorname{Ldim}(\mathcal R_{6s})\ge 9s,
\qquad
\operatorname{Ldim}(\mathcal R_{6s})-\operatorname{VCdim}(\mathcal R_{6s})\ge 3s+1.
\]
Thus unrestricted permutation-comparison classes have an unbounded adaptive-minus-static shattering gap, with an explicit linear lower bound along multiples of six.

## Assumptions and scope

All orders are labeled, complete, strict, and consistent; ties are forbidden. The underlying unknown order is chosen from all \(n!\) possibilities; the learner may adapt pair queries to earlier answers. The orientation convention assigns bit one to the smaller numeric label preceding the larger numeric label. Repeated comparisons are permitted by the definition but cannot occur on a genuinely shattered root-to-leaf branch because one answer would then be determined.

The exact adaptive values above are asserted only for \(1\le n\le7\). The unbounded-gap inequality holds for every positive integer \(s\). No formula, entropy-bound equality, or asymptotically sharp Littlestone dimension is asserted for arbitrary larger \(n\).

## Proof

**1. General size upper bound.** A complete shattered tree of depth \(d\) has \(2^d\) leaves. Different leaves disagree on at least one common queried comparison, so one concept cannot witness two leaves. Therefore \(2^d\le |\mathcal R_n|=n!\). This proves
\[
\operatorname{Ldim}(\mathcal R_n)\le\lfloor\log_2(n!)\rfloor.
\]
For \(n\le6\), the depth certificates described in Step 2 attain this upper bound. The single order for \(n=1\) has dimension zero.

**2. Explicit lower witnesses.** The complete file `permutation_witnesses.json` gives a labeled binary tree for each \(n=2,\ldots,7\), at respective depths \(1,2,4,6,9,11\). Each internal node stores a pair \((a,b)\) and two descendants `zero` and `one`. Each leaf stores an explicit full permutation. The independent `verify.py` reconstructs the actual comparison answers and checks that, for every node, both child branches remain consistent with some order; every leaf order agrees with every comparison on its root-to-leaf path. It also checks that all leaves at the asserted depth have distinct witnesses. The numbers of leaf witnesses are, respectively, \(2,4,16,64,512,2048\). These are finite, complete mathematical certificates: existence of every asserted depth follows simply by traversing and verifying the provided tree.

**3. Complete exclusion of depth twelve for seven items.** Assume a depth-twelve shattered comparison tree for \(\mathcal R_7\). The root chooses two distinct items \(a,b\). Permuting the seven labels maps either answer class to the class of total orders extending the single relation \(0<1\). Hence either root branch would have to shatter a depth-eleven tree inside that conditioned class. It suffices to rule this out.

The file `poset_upper.py` performs an exhaustive finite proof of this nonexistence. A state consists of seven bitmasks recording the strict predecessor sets of a transitively closed acyclic partial order \(P\). For incomparable elements \(a,b\), the two feasible answers produce the respective transitive closures of \(P\cup\{a<b\}\) and \(P\cup\{b<a\}\). Closure is exact: any new path through the added edge starts at a predecessor of \(a\) (possibly \(a\) itself) and ends at a successor of \(b\) (possibly \(b\) itself), and precisely all these pairs are added.

The number \(e(P)\) of linear extensions is computed without approximation by the subset recurrence
\[
E_P(D)=\sum_{v\notin D:\,\operatorname{Pred}_P(v)\subseteq D}E_P(D\cup\{v\}),
\qquad E_P([7])=1,
\]
where \(D\) is the set of already chosen elements and \(e(P)=E_P(\varnothing)\).

Let \(Q(P,d)\) mean that a depth-\(d\) complete comparison tree can be shattered by the linear extensions of \(P\). For \(d=0\), \(Q(P,0)\) holds. If \(e(P)<2^d\), it fails. In every other case, it holds exactly when at least one incomparable pair has **both** oriented successor states satisfying \(Q(\cdot,d-1)\). This equivalence is the definition of complete adaptive shattering, and enumerating all pairs is exhaustive. Caching states cannot change the answer. Evaluating \(Q(P,11)\) for the one-relation state \(0<1\) returns false. The checked execution traverses 16,587 distinct state-and-depth pairs and calculates 37,565 distinct extension-count states; these numbers report coverage of the exact algorithm, not a probabilistic sample.

As an independent implementation, `verify_bitset_upper.py` uses a different state space: bitsets of the 5,040 explicitly generated permutations. At every step it intersects each state with the true/false incidence bitset for each of the 21 possible comparisons. It establishes that the whole class shatters depth eleven but not twelve, using 74,797 cached state-and-depth calculations. The two algorithms have different representations of hypotheses and different extension-count machinery. This independently corroborates the upper obstruction. Together with Step 2 this proves the seven-item value eleven.

**4. The static baseline and amplification.** A comparison support is VC-shattered by all total orders if and only if its undirected query graph is a forest. Indeed, a cycle admits a cyclic orientation which no total order realizes; conversely any orientation of a forest is acyclic and extends to a total order. Therefore the largest support has \(n-1\) edges and \(\operatorname{VCdim}(\mathcal R_n)=n-1\) for \(n\ge1\).

Partition \(6s\) labels into \(s\) consecutive groups of six. Restrict attention to total orders in which all elements of an earlier group precede all elements of a later group, while internal orders in separate groups vary independently. Graft the depth-nine shattered tree for six items from Step 2 at every leaf of a prior block's tree, using only comparisons within the next six-item group. The resulting complete tree has depth \(9s\), and every answer path is realized by concatenating independently chosen block orders. This restricted class is contained in \(\mathcal R_{6s}\), so its shattered tree witnesses the asserted lower bound for the unrestricted class. The static formula then gives the stated gap.

## Verification

The package includes the exact witness data and three Python standard-library programs: `verify.py`, `poset_upper.py`, and `verify_bitset_upper.py`. The separate program `make_cert.py` regenerates the witness tree JSON through search; its output is not needed to validate the mathematical certificate. Run in a directory containing the included files:

```
python3 verify.py
python3 poset_upper.py
python3 verify_bitset_upper.py
```

All three checks succeeded. `verify.py` checked all six trees, including all \(2,048\) seven-item paths. The two upper-bound checkers independently excluded the potentially problematic depth twelve. Exact integers and finite bitmasks are used throughout; no floating-point tolerance, heuristic termination, external download, or randomness enters these checks. The saved `verification_output.txt` records the outcome.

## Relationship to prior work

Agarwal, Agarwal, Assadi, and Khanna (2017) study limited adaptivity and query complexity for (possibly noisy) top-\(k\) ranking from pairwise comparisons. Their model and proved bounds do not settle the exact complete binary mistake-tree depth of the deterministic full-permutation concept class; in particular, the inspected ranking section does not state a seven-item entropy obstruction. Alon, Livni, Malliaris, and Moran (2018) motivate Littlestone dimension as a standard measure of online learnability, but the accessible bibliographic and abstract material does not give this finite comparison-family calculation. Ghazi, Golowich, Kumar, and Manurangsi (2021) provide broad closure bounds for Littlestone dimension, not the indicated exact permutation table. Alon, Moran, and Moran (2026) examine a distinct *counterexample-oracle* sorting interaction in which a learner proposes a whole order, not a single pair at each node; their inspected Introduction and Related Work distinguish that query model from ordinary pairwise comparisons.

The established VC-dimension formula for the linear-extension comparison class of any finite poset, when specialized to an antichain, already implies the static \(n-1\) formula here. The claimed new content is the **adaptive** dimension classification, its first strict deficit relative to the cardinality bound, and the block-amplified gap. Related classical work on learning total orders and balancing linear extensions may provide earlier equivalent descriptions under different terminology; this is a residual historical-priority issue, not a proved uniqueness claim.

## Limitations

Finite exhaustive computation is used only to prove the finite exact upper threshold for seven items; it is **not** extrapolated into an unproved claim for larger orders. The witness certificate verifies a particular shattered tree, while the separate exhaustive state recursion establishes nonexistence of the next depth. Exact bitset and transitive-closure algorithms are described and included for reproducibility; no external proof assistant or independent scientific audit is claimed. Historical originality remains subject to a broader check of older comparison-tree and online-sorting literature, including partially inspected pre-digital sources.

## References

1. A. Agarwal, S. Agarwal, S. Assadi, S. Khanna, *Learning with Limited Rounds of Adaptivity: Coin Tossing, Multi-Armed Bandits, and Ranking from Pairwise Comparisons*, COLT/PMLR 65 (2017), 39–75. https://proceedings.mlr.press/v65/agarwal17c.html . Public conference publication July 2017.
2. N. Alon, R. Livni, M. Malliaris, S. Moran, *Private PAC Learning Implies Finite Littlestone Dimension*, arXiv:1806.00949 (first version June 4, 2018). https://arxiv.org/abs/1806.00949 .
3. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT/PMLR 132 (2021), 686–696. https://proceedings.mlr.press/v132/ghazi21a.html .
4. N. Alon, S. Moran, S. Moran, *Sorting from Counterexamples*, arXiv:2608.21579v1 (August 2026). https://arxiv.org/html/2608.21579v1 .
