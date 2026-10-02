# Independent mathematical audit — SCOPE-20260930-12c6f0655c30
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
The class of treeable Turing degrees is closed under finite Turing joins; degrees of unique paths through computable trees are likewise closed under finite joins; consequently, if finitely many strong degrees of categoricity have join above \(\mathbf 0\), then their join is again a strong degree of categoricity.

## Correctness
Status: **PASS**.

For two witness trees, the computable coordinatewise product tree has exactly the paired paths. Every product path computes both of its coordinate paths; leastness in each factor therefore makes the joined distinguished path reducible to every product path, and the distinguished paired path has exactly the join degree. Iteration gives finite closure and uniqueness is immediate. The categoricity consequence uses the corrected Csima–Rossegger characterization: every strong degree is treeable, and above \(\mathbf 0\) every treeable degree is a strong degree. The finite verification script checks only the combinatorics of product path sets and uniqueness, not the infinite Turing-reducibility theorem.

## Originality
Status: **PASS**.

The full Csima–Rossegger paper introduces treeable degrees and gives the strong-degree characterization on the cone above \(\mathbf 0\), but the inspected text does not state finite-join closure or a product-tree closure theorem. Published-record semantic search returned this record as the only matching theorem. Standard product constructions for computable trees are background, but no inspected prior source states or implies the specific algebraic closure result together with the categoricity consequence.

### Equivalent formulations
- Search/source: Barbara F. Csima and Dino Rossegger, Degrees of categoricity and treeable degrees, arXiv:2209.04524v2
- Search/source: Published-record semantic query: treeable degrees finite Turing joins product computable trees least path degrees
- Evidence: The inspected primary source defines treeability and states the strong-degree characterization but not finite-join closure.
- Reasoning: No equivalent theorem was found.

### Broader coverage
- Search/source: arXiv:2209.04524v2
- Evidence: The characterization of strong degrees above \(\mathbf 0\) is broader background but does not assert that treeable degrees are join-closed.
- Reasoning: The categoricity corollary depends on the new closure lemma plus the published characterization.

### Exact database or table
- Search/source: Published-record semantic corpus
- Evidence: No exact database or table is relevant to this degree-class closure theorem.
- Reasoning: The named check is specifically inapplicable because the object is an infinite degree class, not a tabulated finite invariant; the theorem corpus was searched instead.

### Claim versus prior implication
- Search/source: arXiv:2209.04524v2
- Evidence: The source characterization alone does not imply join closure without proving that product witnesses remain least.
- Reasoning: The computable product-tree argument is the additional substantive step needed for the final claim.

### Source inspections
- **Degrees of categoricity and treeable degrees** (arXiv:2209.04524v2): trigger — primary source introducing treeable degrees and the categoricity characterization; material read — full accessible text around the definition of treeability, the strong-degree theorem, the corrected cone characterization, and related constructions; method — lawful arXiv full-text inspection; assessment — BACKGROUND_NOT_COVERING_JOIN_CLOSURE; evidence — The inspected source states that strong degrees are treeable and gives the converse above \(\mathbf 0\), but no finite-join or product-tree closure theorem was found.

## Value
Status: **PASS**.

The source explicitly treats the structure of treeable degrees as a research object. Finite-join closure is a natural algebraic property of that class and yields a concrete closure theorem for strong degrees of categoricity on the classified cone. The proof is short, but it is a motivated structural lemma rather than a routine parameter substitution.

## Checked sources
- Barbara F. Csima and Dino Rossegger, Degrees of categoricity and treeable degrees, arXiv:2209.04524v2; Journal of Mathematical Logic 24(3), 2450002.
- Published-record semantic query: treeable degrees finite Turing joins product computable trees least path degrees.

## Residual risks
- Because the product-tree argument is elementary, an equivalent folklore observation may exist outside the searched terminology.
- No countable-join theorem is claimed; nonuniformity of the individual reductions is a genuine boundary.

The audit distinguishes finite reproducibility checks from proofs of infinite statements and makes no claim beyond the final claim above.
