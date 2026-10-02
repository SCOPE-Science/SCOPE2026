---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every connected skeleton \(H\) of maximum degree at most \(\Delta\ge3\), twice subdividing each edge and filling each original vertex to degree \(\Delta\) with pendant two-edge arms gives an open-twin-free, \(C_4\)-free graph \(L_\Delta(H)\) with \(\gamma^{\mathrm{IOC}}(L_\Delta(H))=|V(L_\Delta(H))|-|V(H)|\); cycle and path skeletons yield the stated near-extremal densities.

## Correctness — PASS

Pendant supports are forced into every IO-code. The remaining vertices partition into one block of size \(\Delta+1\) per skeleton vertex: the center, its pendant leaves, and the opposite subdivision vertices on incident skeleton edges. Any two omissions from one block either destroy total domination or make two open-neighborhood traces equal, so at most one vertex per block can be omitted. Conversely, omitting exactly all skeleton centers leaves every noncenter with a distinct singleton trace and every center with a distinct \(\Delta\)-element trace, proving the exact optimum. Double subdivision multiplies every skeleton-cycle length by three, hence there is no \(C_4\). The cycle/path order and density formulas follow by substituting \(m=p\) or \(m=p-1\).

**Checked sources.** assigned RESULT.md at tree ac90443fcd4cd6f0542e50d152bb53604c2cce2c; Chakraborty--Foucaud--Henning 2026 full arXiv text; Seo--Slater 2011 abstract; Chellali et al. 2014 open-access article

**Residual risks.** The finite Graph-Atlas verifier was not needed for the infinite proof.

## Originality — PASS

The full 2026 primary source proves the general upper bound and gives large tight examples only in the subcubic case; its concluding section explicitly says that for every fixed \(\Delta\ge4\) the large-order sharpness/improvement question remains open. Searches under both identifying-open-code and OLD terminology found no earlier twice-subdivided arbitrary-skeleton formula or the cycle density \((2\Delta-2)/(2\Delta-1)\).

### Equivalent formulations

The older OLD terminology is definitionally equivalent to identifying open codes and was explicitly included in the search.

### Broader coverage

No inspected broader theorem implies the arbitrary-skeleton exact formula or its asymptotic density.

### Exact database or table

A finite graph table cannot imply the all-skeleton theorem; the construction proof is symbolic.

### Claim versus prior implication

The source does not mechanically imply existence of the audited family; its open problem motivates it.

**Checked sources.** https://arxiv.org/abs/2407.09692; https://doi.org/10.1016/j.dam.2010.12.010; https://doi.org/10.5614/ejgta.2014.2.2.1; Resultary semantic search

**Residual risks.** The unavailable full 2011 tree paper is the main older-literature risk; a differently described subdivision family could exist there or elsewhere.

## Value — PASS

The theorem gives an exact code number for a broad arbitrary-skeleton lift and directly advances an explicit bounded-degree asymptotic construction problem for every \(\Delta\ge4\). The cycle/path specializations are reusable extremal families rather than isolated small examples.

**Checked sources.** Chakraborty--Foucaud--Henning 2026 open problem; older OLD tree/general literature

**Residual risks.** The exact asymptotic extremal constant remains open.

## Limitations

- The construction improves the asymptotic lower benchmark for \(\Delta\ge4\) but does not determine the exact asymptotic extremal constant.
- It does not characterize extremal graphs; for \(\Delta=3\) the known \(5/6\) construction is stronger.
- Older tree literature using different construction language remains a residual originality risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
