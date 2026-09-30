# Independent Audit — A 16/27 lower bound for four-colour rainbow Schur triples

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/a-16-27-lower-bound-for-four-colour-rainbow-schur-triples--7de6a4bc1e41`
Audited tree: `9fe929697f4d8cfb210fec11665fff00365671ff`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. The asymptotic calculation is correct. Independently enumerating the 27 interval cells for each ordered residue pair modulo 3 gives good areas 0 for (0,0), 47/144 for each of the four pairs with exactly one zero residue, 1/4 for (1,1) and (2,2), and 31/72 for (1,2) and (2,1). Their sum is exactly 8/3; multiplying by the 1/9 lattice density of each residue pair yields (8/27)n^2+O(n) rainbow ordered Schur pairs. Since the total number of ordered positive pairs with x+y<=n is n(n-1)/2, the limiting fraction is 16/27. Rational cut boundaries and residue restrictions contribute only O(n) boundary error, so the liminf claim follows.

## Originality

**PASS**. The closest preprint, Hegde–Kumar–Pratibha arXiv:2609.18474, was posted 2026-09-16 and its public description gives new general k-colour bounds but no 16/27 four-colour construction. The record's documented comparison specializes that paper's lower bound to 10/21 at k=4. Targeted searches for the exact constant 16/27 together with four-colour/rainbow-Schur terminology did not locate an equivalent or stronger pre-2026-09-17 result. Given the one-day separation from the parent preprint, contemporaneous unpublished calculations remain a real but unverified priority risk.

## Scientific value

**PASS**. This is a genuine asymptotic infinite-family improvement, not a finite optimization. The explicit mod-3 colouring with two macroscopic cut points raises the documented four-colour lower bound from 10/21 to 16/27 and reduces the proof to an exact rational polygon-area table. The exact value remains open, but a substantial constant improvement in a newly active anti-Ramsey multiplicity problem is sufficient standalone scientific value.

## Literature evidence

- https://arxiv.org/abs/2609.18474 — Hegde–Kumar–Pratibha, A somewhat sure note on an un-Schur problem, posted 2026-09-16; closest general k-colour source and immediate benchmark.
- https://hegdeswaroop.github.io/research/ — Author research page describing the same 2026 preprint and its general-k scope.

## Independent checks

- Recomputed all nine residue-pair polygon areas with exact rational inclusion-exclusion.
- Verified total good area 8/3, rainbow n^2 coefficient 8/27, and limiting fraction 16/27.
- Checked that the ordered Schur-pair denominator is n(n-1)/2 and that rational boundary rounding is lower order.

## Limitations

- The closest preprint was only one day old when the record was published; unpublished or unindexed contemporaneous work may overlap.
- The exact four-colour asymptotic optimum is not determined.
- The compressed archived source report was not needed for the audit; no inaccessible source is represented as read.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.
