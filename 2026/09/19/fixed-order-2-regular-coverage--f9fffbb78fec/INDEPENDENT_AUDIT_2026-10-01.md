# Independent scientific audit — SCOPE-20260919-f9fffbb78fec

Audited at: 2026-10-01T13:18:12.002998Z

Disposition: **passed**

## Correctness — PASS

The source finite-order upper inequality gives the claimed deficiency floor. The all-orders construction is valid: for every odd block order N at least r+2, a Walecki decomposition yields a one-deficient block with one vertex of degree r-1, all others degree r, and a spanning Hamilton cycle. Attaching (r-2)t+2 such blocks to a t-vertex core path makes a connected simple r-regular graph. The baseline order is \((r^2-3)t+2(r+2)\), and the even excess below \(r^2-3\) can be absorbed by enlarging one odd block. All core and attachment edges are bridges, so core vertices are omitted by every 2-regular subgraph, while block Hamilton cycles cover every non-core vertex. Independent arithmetic checks reproduced the admissible-excess conditions.

## Originality — PASS

The full primary paper proves the sharp asymptotic proportion and, in its sharpness section, constructs equality examples only at orders \((r^2-3)t+2(r+2)\). It does not interpolate every admissible order. The cubic case is already exact in prior work. Resultary search found no earlier all-orders odd-degree formula beyond the assigned record.

### Equivalent formulations

No earlier equivalent all-r, all-admissible-n formula was located.

### Broader coverage

Neither source dominates the claimed general odd-r fixed-order interpolation.

### Exact database or table

The exact function is not a known table lookup in the sources inspected.

### Claim versus prior implication

The every-order sharpness does not follow from the source endpoint examples without the additional variable-order construction.

## Value — PASS

The result converts a sharp asymptotic theorem and sparse equality examples into the exact extremal function at every admissible order for a natural graph invariant. The variable-order block lemma gives a reusable mechanism for filling all residue classes, so this is a motivated complete finite-order classification rather than an arbitrary computation.

## Sources inspected

- Nearly Spanning Regular Subgraphs — https://arxiv.org/abs/2609.19777. NOT_COVERING: The source gives the finite upper inequality and examples at orders \((r^2-3)t+2(r+2)\), but not equality at every admissible order.
- Largest 2-Regular Subgraphs in 3-Regular Graphs — https://arxiv.org/abs/1903.08795. COVERING_SPECIAL_CASE: This covers r=3, which the audited record explicitly credits, but not general odd r.

## Checked sources

- https://arxiv.org/abs/2609.19777
- https://arxiv.org/abs/1903.08795
- https://doi.org/10.1002/jgt.20443
- Resultary semantic search

## Residual risks

- Older factor-theory literature may contain an equivalent interpolation under different terminology; no such result was located.

## Limitations

- The exact every-order law is for 2-regular subgraphs of simple regular graphs.
- The cubic specialization and the finite upper inequality are prior results.
- No corresponding exact fixed-order theorem for k at least 3 is claimed.
