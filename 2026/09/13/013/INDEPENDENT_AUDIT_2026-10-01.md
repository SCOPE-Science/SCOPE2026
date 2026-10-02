# Independent audit — 2026-10-01

## Final claim

For strict-majority bootstrap on the d-dimensional torus, conditioned on a fully infected thickness-2 slab and p=1/2+1/sqrt(d), d>=16 and n>=20, the adjacent layer becomes fully infected after one update with probability at most the m-th power of (1-c/sqrt(d)), where c=exp(-8)/4 and m is floor(n/4) to the (d-1)-st power; the repaired proof uses initially healthy under-supported vertices.

## Disposition

**repaired**

## Correctness — PASS

The filed proof omits the possibility that a sampled boundary vertex is already initially infected, so its event F_v alone is not a one-step failure event. The claim is nevertheless repairable with the same stated constant. Let H_v be the event that v is initially healthy and at most d-1 of its 2d-1 non-slab neighbours are initially infected. For d>=16, 1-p>=1/4. The filed point-mass calculation gives P(F_v)>=exp(-6)/(4 sqrt(d)), hence P(H_v)>=exp(-6)/(16 sqrt(d))>=exp(-8)/(4 sqrt(d)). A spacing-4 packing makes the H_v events independent. Whole-layer success excludes every H_v, proving the same bound as the m-th power of (1-c/sqrt(d)), with c=exp(-8)/4. The repaired RESULT states this missing healthy-vertex factor explicitly.

## Originality — PASS

Best-of-knowledge search found broad majority-bootstrap critical-window results for high-dimensional geometric graphs, including tori, but no primary source implying this particular one-step thickness-2 slab obstruction. The finding is an obstruction to a proof mechanism, not a new critical-window theorem.

### Equivalent formulations

Equivalent formulations are a simultaneous one-update infection of an adjacent layer, or absence of any initially healthy locally-under-supported vertex in a separated packing; no prior exact formulation was found.

### Broader coverage

These broader results concern eventual bootstrap percolation, not the probability that an entire conditioned boundary layer advances in one update, so they do not imply the obstruction.

### Exact database or table

There is no relevant finite database row; the claim is an asymptotic probability bound.

### Claim versus prior implication

No inspected prior theorem implies the repaired one-step obstruction; the proof uses a direct independent packing and binomial point mass.

## Scientific value — PASS

The result addresses a specific proposed mechanism for proving slab invasion and gives a structural reason it cannot work: an exponentially large independent packing of initially healthy under-supported vertices blocks simultaneous one-step advance. This is a motivated boundary/counterexample to a proof route, not an arbitrary numerical slice, and it clearly states that multi-round cleanup and the full window law remain open.

## Checked sources

- https://arxiv.org/abs/2406.17486
- https://arxiv.org/abs/math/0702373
- Resultary published-findings semantic search

## Residual risks and limitations

- The numerical artifact checks the binomial tail and packing scale; it does not itself encode the repaired healthy-vertex factor, which is proved analytically in the replacement RESULT.
- No novelty search proves absence from all bootstrap-percolation literature; the PASS is best-of-knowledge and narrowly scoped to the one-step slab obstruction.
- Its value is methodological rather than a resolution of the global percolation threshold.

The repaired proof refutes only a one-step whole-layer advance at p=1/2+1/sqrt(d); it does not prove either side of the full window law or exclude multi-round slab cleanup.
