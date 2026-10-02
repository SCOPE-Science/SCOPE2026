# Independent mathematical audit — 2026-10-01

## Final claim

For a complete multipartite graph \(K_{n_1,\ldots,n_r}\) with \(n_1\ge n_2\ge\cdots\) and \(n_2=0\) when \(r=1\), membership in bicoloured-interval and interval-sandwich are equivalent and occur exactly when \(n_2\le2\), equivalently exactly when there is no induced \(K_{3,3}\); every positive instance admits a monochromatic centre-containment representation.

## Correctness — PASS

PASS. The negative direction is exact because two parts of size at least three induce \(K_{3,3}\), and the full Basit--Suter--Zhang proof establishes \(K_{3,3}\) as a forbidden induced subgraph of interval-sandwich. The positive direction was checked directly from the frozen construction: place the one possible large part on separated unit-radius centers, place each remaining two-vertex part as a far left/right pair with the prescribed large radius, and give singletons sufficiently large radii. Same-part pairs then miss the monochromatic threshold, while every cross-part pair meets it. The one-part convention is consistent. Thus the construction gives a valid monochromatic, hence bicoloured-interval, representation for every \(n_2\le2\).

## Originality — PASS

PASS. The full introducing preprint was inspected. It proves the complete bipartite classification \(K_{s,t}\) belongs exactly when \(\min\{s,t\}\le2\), and proves the \(K_{3,3}\) obstruction, but it does not state the complete multipartite classification or the monochromatic shell construction. Targeted searches for complete multipartite tolerance/bicoloured-interval formulations found no prior theorem. The bipartite theorem supplies the negative obstruction and special cases, but it does not mechanically construct all multipartite positive cases.

### Equivalent formulations

The multipartite statement is stronger than the bipartite subcase and includes a constructive monochromatic representation.

### Broader coverage

Class inclusions alone do not decide membership of all complete multipartite graphs in the new classes.

### Exact database or table

Search failure is secondary evidence; the full primary-text comparison is decisive for best-knowledge originality.

### Claim versus prior implication

The positive multipartite construction is additional mathematical content rather than a stated corollary of the primary paper.

## Scientific value — PASS

PASS. Complete multipartite graphs are a canonical extension of the complete bipartite family singled out in the introducing paper. The theorem collapses two new representation classes to one simple induced-subgraph criterion on that natural class and strengthens the positive side to a monochromatic representation. This is a complete natural classification, not an arbitrary slice.

## Sources inspected

- **Abdul Basit, David Suter, and Erchuan Zhang, Bicoloured interval graphs and slab-hypergraph links** (arXiv:2609.12293): BIPARTITE_SUBCASE_NOT_MULTIPARTITE_COVERAGE. The paper proves the exact complete-bipartite classification and \(K_{3,3}\) obstruction, but does not state the arbitrary complete-multipartite iff theorem or its monochromatic construction.

## Residual risks

- The positive construction is elementary enough that it may exist as an unindexed folklore consequence in tolerance-graph literature.
- No general closure theorem located in this run decisively covers the arbitrary multipartite positive direction.

## Disposition

**passed**
