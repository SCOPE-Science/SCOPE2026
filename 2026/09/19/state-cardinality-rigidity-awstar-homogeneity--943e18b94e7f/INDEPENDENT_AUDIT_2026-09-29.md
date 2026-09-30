# Independent Audit — 2026-09-30

**Record:** `2026/09/19/state-cardinality-rigidity-awstar-homogeneity--943e18b94e7f`  
**Title:** State-cardinality rigidity for transfinite AW*-homogeneity  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `ada6ebc7bfe465316784fcf2c0da885c26936806`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. For any state and pairwise orthogonal nonzero projections, the indices on which the state is positive are countable because, for each n, at most n of the projections can have value at least 1/n. A separating family therefore covers a homogeneous family only if |I|≤|F|·aleph_0. A countable separating family has a faithful convex combination, so the least separating-state cardinal is either 1 or uncountable. These two facts give kappa=max(aleph_0,s(M)) under the simultaneous hypotheses. The downward spectrum argument is also sound: for every infinite lambda≤kappa, partition kappa into lambda blocks of size kappa and use Berberian addability to show each block join is equivalent to 1. The same counting bound excludes larger homogeneous decompositions. Arulseelan's Corollary 6.2 indeed constructs both a separating family and a kappa-homogeneous decomposition from a maximal p-copy family, so the choice-independence corollary follows.
- **Originality — PASS:** PASS, qualified against older AW*/Baer-* dimension theory. Arulseelan's current public text states Theorem A with kappa-homogeneity plus kappa ordinary separating states, explicitly notes the countable weighted-sum collapse, and in Corollary 6.2 builds a separating family indexed by the number of copies of the faithful corner. It does not state the lower capacity bound for ordinary states, the exact identity kappa=max(aleph_0,s(M)), or the full interval of possible infinite homogeneity cardinals. The individual counting and addability ingredients are standard; the claimed novelty is the cardinal synthesis for the new transfinite setup.
- **Scientific value — PASS:** PASS. The result turns the cardinal in the new transfinite theorem from an apparently chosen parameter into an intrinsic invariant, proves optimality of the number of ordinary states in the uncountable case, and makes the Zorn-produced copy cardinal in the local-corner application canonical. That is a meaningful structural sharpening.

## Independent findings
- The state-counting lemma requires no normality and works in every unital C*-algebra.
- The dichotomy s(A)=1 or s(A) uncountable follows immediately from a positive weighted sum of a countable separating family.
- Cardinal partitioning works for singular as well as regular kappa, and Berberian addability supplies equivalence of each block join with 1.
- Arulseelan's public text explicitly says ordinary states, not normal states, and constructs the relevant separating family in Corollary 6.2.

## Independent checks
- Reproved the countable-support lemma from finite orthogonal sums.
- Checked the cardinal arithmetic in both the countable and uncountable branches.
- Checked the downward homogeneity construction for arbitrary infinite lambda≤kappa.
- Read the current public Arulseelan text around Definition 1.2, Theorem A, and Corollary 6.2.

## Literature evidence
- https://arxiv.org/abs/2609.20718 — Arulseelan current public text: kappa-homogeneity, Theorem A, ordinary-state separation, and Corollary 6.2.
- https://doi.org/10.1112/blms/16.4.407 — Christensen–Pedersen countable predecessor.
- https://doi.org/10.1007/978-3-642-15071-5 — Berberian, Baer *-Rings; addability and projection-decomposition background.

## Limitations
- The exact homogeneity spectrum is proved only under the simultaneous kappa-homogeneity and ≤kappa ordinary-state separation hypotheses.
- The audit does not assert an analogous invariant for normal states.
- Older AW*/Baer-* dimension literature was not exhaustively searchable under every possible terminology; originality is therefore to the best of the inspected evidence.

The assigned source-tree SHA still matches the current record tree inspected on `main`. GitHub was used only as read-only evidence; no repository writes were made.
