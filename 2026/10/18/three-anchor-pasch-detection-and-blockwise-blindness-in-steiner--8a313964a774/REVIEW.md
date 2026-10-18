# Scientific assessment: three-anchor Pasch detection

## Correctness — PASS

The all-parameter blindness theorem follows from an explicit colour-compatible equitable partition. Pair uniqueness forces every off-block block to meet the distinguished block in at most one point; the complete point/block cell sizes and cross-incidence counts depend only on \((v,k,t)\). Colour refinement therefore produces matching colour multisets on any two such marked designs. For three noncollinear marked points in a Steiner triple system, the two-variable formulas selecting the three pair-completion points have quantifier rank two, so existence of a block through all three is a quantifier-rank-four sentence. The initial three refinement stages prove that no rank-at-most-three sentence separates the chosen order-fifteen witnesses. The programs verify both independently specified finite block systems, check all pairs and triples, and enumerate all four-block Pasch configurations. No finite test is used as an argument for the universal design statement.

## Originality — PASS with residual priority risk

The general \(C^2\)/colour-refinement correspondence and coarsest-equitable-partition framework are established by Kiefer–Schweitzer–Selman (arXiv:1503.08792) and Arvind–Köbler–Rattan–Verbitsky (arXiv:1502.01255); their inspected papers supply tools rather than the explicit arbitrary-Steiner-design block-marker partition or the sharp three-landmark, rank-four Pasch boundary. Ling–Colbourn–Grannell–Griggs (2000) treat combinatorial anti-Pasch constructions; the accessible bibliographic and abstract material does not assert a counting-logic threshold. A special-purpose earlier treatment of landmark refinement on Steiner triple systems remains possible, and the 2000 full text was not accessed. Published Pasch enumerations, including those for order fifteen, cannot alone imply the two-versus-three landmark property without the refinement argument. Targeted published-literature and scientific-record comparisons returned no directly covering claim.

## Value — PASS

Pasch is the canonical smallest nontrivial configuration in Steiner triple systems. The theorem identifies an exact *logical landmark complexity*: even separately naming every point of a common block in a general Steiner design is information-theoretically ineffective for \(C^2\), whereas three noncollinear marks detect a genuinely structural four-block incidence pattern in constant depth. The explicit two order-fifteen systems realize the boundary, including a sharp rank-four separator. This is a structural limitation and threshold for descriptive graph invariants, not an arbitrary small census or a restatement of the general equitable-partition theorem.

## Verification, comparison and limits

The two standalone scripts are independent finite checks, one using point-pair completion and joint colour-refinement signatures and the other enumerating four-block Pasch configurations and checking equitable degree matrices. The proof does not claim a general formula for arbitrary noncollinear landmark sets or an improved higher-dimensional counting-logic hierarchy. The possibility of specialized antecedents in inaccessible or unindexed literature remains the main originality risk; independent audit was not performed.

Self-review: passed. Independent audit: not yet performed.
