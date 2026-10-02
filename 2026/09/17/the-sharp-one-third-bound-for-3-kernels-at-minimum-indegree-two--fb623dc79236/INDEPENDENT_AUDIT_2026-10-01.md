# Independent audit — SCOPE-20260917-003

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

Every finite simple digraph with minimum indegree at least two has a 3-kernel of size at most one third of its vertices, and the bidirected triangle shows that the constant one third is sharp.

## Correctness

**PASS** — The proof was reconstructed from the partition supplied by the cited q-kernel algorithm. In the residual set A each vertex has at most one A-outneighbor, so the family of sets C_x has element multiplicity at most two and produces a pseudoforest incidence multigraph. The auxiliary covering lemma was checked componentwise through its matching inequality: cycle components satisfy the bound and deleting a leaf with its neighbor changes the induction potential by at most three. This gives a hitting set P of size at most one third of A. Minimality of P rules out a directed cycle in P under the outdegree-one condition. The resulting acyclic set R union P reaches every vertex within two steps; the cited prekernel lemma then gives a contained 3-kernel. Finally twice the size of R is at most the size of B, yielding the one-third total bound. The bidirected triangle supplies equality. The committed exhaustive program was inspected only as a supplementary check, not as an infinite proof.

## Originality

**PASS** — The primary 2026 minimum-indegree q-kernel paper conjectures the one-over-(delta+1) constant for q at least three and its general theorem gives only one half at delta two, q three. The audited one-third theorem therefore resolves the first uncovered case. The other recent q-kernel paper studies different girth, connectivity, and bipartite questions. No equivalent or stronger result was found.

### Equivalent formulations

Aliases included 3-kernel, q-kernel, minimum indegree two, one-third constant, and c_{2,3}. Evidence: Published-results search returned this record as the exact match. The primary source explicitly formulates the minimum-indegree constants and leaves the delta-two, q-three case below its general bound.

### Broader coverage

No broader theorem found implies the q=3 one-third statement. Evidence: Boyer et al. give c_{2,3} at most one half from their general theorem, not one third. Their exact conjectured constant is already known in a larger-q regime but that corollary starts at q at least four when delta equals two. The Penev et al. paper addresses different hypotheses.

### Exact database or table

The committed small-order census is only a check and is not used as novelty evidence. Evidence: The theorem is uniform over all finite digraphs; no finite table can establish it.

### Claim versus prior implication

The final theorem is not a substitution into the prior bound; it requires a new structural covering argument in the first unresolved parameter case. Evidence: The partition and prekernel-conversion lemma are prior tools, but their published counting argument stops at the weaker one-half bound for this parameter. The new pseudoforest incidence-cover step is what sharpens the count to one third.

## Value

**PASS** — The theorem settles the first minimum-indegree case left open by a recent explicit conjectural program and attains the conjectured sharp constant. The pseudoforest covering lemma provides structural content beyond a small-instance computation.

## Sources inspected

- Small q-kernels in digraphs with minimum in-degree delta — https://arxiv.org/abs/2606.16971. NOT_COVERING; supplies inputs but leaves the audited parameter case unresolved: Its general theorem yields one half for delta two and q three, while the exact one-third regime from its corollary begins at larger q.
- Small q-kernels in digraphs — https://arxiv.org/abs/2608.00825. NOT_COVERING: It studies other q-kernel questions rather than the minimum-indegree constant c_{2,3}.
- Committed proof note and verifier — repository artifacts/research_note.md and artifacts/verify.py at the assigned commit. SUPPORTS the theorem; computation treated only as a finite check: The noncomputational proof closes the counting step through a matching/edge-cover inequality in a pseudoforest.

## Residual risks and limitations

- The literature is very recent; an unindexed revision or concurrent manuscript could affect originality priority.
- The argument depends on the stated properties of the cited partition algorithm and prekernel lemma; those source statements were inspected in accessible full-text excerpts.
- The small-order exhaustive program is corroborative only; the accepted proof is noncomputational.
- Originality is best-of-knowledge because the surrounding conjecture literature is recent.

## Disposition

**PASSED**
