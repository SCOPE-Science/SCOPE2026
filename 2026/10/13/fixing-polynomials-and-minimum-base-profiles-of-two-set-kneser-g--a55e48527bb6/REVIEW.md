# Scientific review

**Correctness — PASS.** The theorem uses the standard natural action \(\operatorname{Aut}(K(n,2))\cong S_n\), valid for \(n\ge5\). A pointwise stabilizer is trivial exactly when the incidence signatures of all ground vertices are distinct. In the selected-edge graph that means no two-vertex component and at most one isolated vertex. The labeled exponential formula excludes singleton and isolated-edge components, then admits one singleton; coefficient normalization is \(n![t^n]\), not an orbit quotient. The lower-bound and equality argument forces tree components with the listed excess-size profiles. Cayley-tree labeling gives every minimum count. Exhaustive testing of all selected-edge subsets for \(n=5,6,7\) and of minimum-size subsets for \(n=8,9\) agreed with all formulas. The proof, not the computations, establishes the universal claim.

**Originality — PASS with explicit risks.** The public 2017 fixing-polynomial article [1, Section 3] defines the polynomial and gives family examples without the two-set Kneser enumeration. Boutin's point-separation criterion, reproduced in [2, Lemma 2.1] and [3, Lemma 1.1], implies the selected-edge feasibility rule; those earlier feasibility facts and the previously known scalar base size are not reclaimed. [2, Lemmas 2.2–2.4, Section 2] develop the dual hypergraph viewpoint, but do not count labeled bases of every size or classify/count all optimal bases. [4, Section 4] determines distinguishing colorings using selected determining sets, not a fixing polynomial. [5, Theorem 1.1, Sections 2–3] supplies the scalar symmetric-group base size but no all-cardinality enumeration. Targeted public-literature searches and published-finding-index queries for these claims, aliases, and the full exponential formula found no equivalent. The known separation lemma plus labeled graph enumeration are a short route to the answer, so earlier implicit or unindexed versions remain a genuine residual risk.

**Value — PASS.** The fixing polynomial is a natural previously defined graph invariant that describes every cardinality of symmetry-breaking vertex sets, whereas the known determining number gives only its least degree. The structural component test determines the whole fixing-set space, and the explicit \(n\pmod3\) classification gives exact multiplicities of optimal selections of sensors/coordinates. The family includes the Petersen graph and an infinite symmetry-rich family; neither the exact all-cardinality count nor minimum-base multiplicities follow numerically from a scalar base size alone.

**Limitations and proximity.** The identity treats only two-subset Kneser graphs; the general Kneser separation criterion and the scalar minimum are published. Possible equivalent formulas under permutation bases, separating families or graphical incidence signatures are not excluded by a finite literature search. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.

## Literature cited

[1] Javaid–Fazil–Ali–Salman, *On Some Parameters Related to Fixing Sets in Graphs*, public author upload 2017-05-22.
[2] Cáceres–Garijo–González–Márquez–Puertas, *The determining number of Kneser graphs*, DMTCS (2013).
[3] Das–Dey, *Determining Number of Kneser Graphs: Exact Values and Improved Bounds*, arXiv:2009.08787 (first 2020).
[4] Albertson–Boutin, *Using Determining Sets to Distinguish Kneser Graphs*, Electronic Journal of Combinatorics (2007).
[5] del Valle–Roney-Dougal, *The base size of the symmetric group acting on subsets*, arXiv:2308.04360 (2023), published (2024).
