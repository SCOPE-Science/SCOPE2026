# Independent audit — SCOPE-20260918-831655b0b665

Audit date (UTC): 2026-10-01

## Final claim

For every pair of component Euclidean lengths \(0\le u<v\), the Lin--Spreer canonical construction has exactly \(2^u\) positive torus-knot types, hence \(a_n=2^{\lceil n/2\rceil}-1\) canonical constructions of size \(n\).

## Correctness

**PASS** — The proof was reconstructed from the positive determinant-one split. Away from the boundary, determinant one forces both coordinates of one column to dominate the other, so simultaneous column subtraction is the unique parent and decreases both row Euclidean lengths by one. The roots are exactly the two boundary families; inverse column addition has two children and increases both lengths by one. Thus the depth-\(u\) generation over the root indexed by \(v-u\) has \(2^u\) matrices. The torus-knot swap exchanges the two row lengths and gives one representative with \(u<v\). A fresh exact enumeration through canonical size 15 reproduced the claimed size sequence and unique knot pairs. Lin--Spreer Proposition 4.3 and Corollary 4.4 were inspected in full HTML and establish the unique positive split and the Euclidean-length size formula.

## Originality

**PASS** — The nearest primary source reports the finite cutoff count 3,049 at size 19 but does not state the all-size formula or the refined component-length count. Nathanson gives the classical free binary monoid structure of nonnegative determinant-one matrices, which explains the ancestry but does not connect it to the simultaneous two-row Euclidean lengths of the canonical torus-knot split. The source companion CSV was inspected and contains only finite cumulative counts through 19. No exact or stronger published census formula was located.

### Equivalent formulations

Aliases, parameter normalizations, and source-specific formulations were compared by implication rather than by title similarity. Exact-title, exact-claim, alias, and primary-literature searches found no equivalent stronger statement beyond the qualifications below.

### Broader coverage

The closest general results and source theorems were inspected directly. General machinery that is prior art is excluded from the novelty claim; none of the inspected broader statements implies the final claim at the stated strength.

### Exact database or table

Finite computations and tables were treated as corroborative evidence only. They were not used to infer an infinite theorem or to establish novelty.

### Claim versus prior implication

The nearest primary source reports the finite cutoff count 3,049 at size 19 but does not state the all-size formula or the refined component-length count. Nathanson gives the classical free binary monoid structure of nonnegative determinant-one matrices, which explains the ancestry but does not connect it to the simultaneous two-row Euclidean lengths of the canonical torus-knot split. The source companion CSV was inspected and contains only finite cumulative counts through 19. No exact or stronger published census formula was located.

## Value

**PASS** — This is a natural complete classification of the canonical constructions attached to every positive torus knot, replaces a finite census by an all-size formula, and explains the source cutoff 3,049. The result is explicitly limited to canonical size, not true triangulation complexity, so it does not overclaim the open minimality conjecture.

## Sources inspected

- Torus knots as loop-edges in three-sphere triangulations — https://arxiv.org/html/2609.14200v1 — NOT_COVERING: supplies the split and finite cutoff data but not the all-size refined census.
- Lin--Spreer companion code/data — https://github.com/HimalayanRainstorm/TorusKnots — NOT_COVERING: cumulative canonical counts are tabulated only through 19; no closed all-size formula appears in the inspected data.
- Free monoids and forests of rational numbers — https://arxiv.org/abs/1406.2054 — BACKGROUND: establishes the free binary monoid of nonnegative determinant-one matrices, but not the torus-knot row-length census.

## Residual risks and limitations

- The motivating torus-knot preprint is very recent, so a contemporaneous unindexed derivation remains a priority risk.
- The theorem counts the canonical construction only; equality with actual triangulation complexity remains conjectural.

## Disposition

**PASSED**
