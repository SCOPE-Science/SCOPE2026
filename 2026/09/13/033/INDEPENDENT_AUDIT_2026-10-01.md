# Independent mathematical audit — SCOPE-20260913-033

Disposition: **PASSED**.

## Correctness
**PASS** — Every Fano plane has exactly seven Pasches: omitting each of its seven points leaves four lines forming one Pasch. Hence any Fano-containing STS has at least seven. The stored 70-block witness was independently checked to be an STS(21), to contain the marked Fano subplane, and to have exactly seven total Pasches, proving the claimed minimum 7. The larger census totals are auxiliary and were not independently replayed.

## Originality
**PASS** — The classical tricyclic classification and later subsystem classifications define broader families, but targeted Resultary/literature searches found no prior statement of this Fano-restricted Pasch extremum; the exact witness/minimum was not mechanically implied by the inspected tables.

### Equivalent formulations
For the minimum itself, it is enough to exhibit one sigma-invariant STS(21) with a Fano subplane and exactly seven total Pasches.

### Broader coverage
Those classifications define broader universes but do not mechanically state the extremal Pasch count.

### Exact database or table
The load-bearing minimum does not require trusting the saved 135,128-row census: the universal Fano lower bound plus the explicit witness proves it.

### Claim versus prior implication
The classification alone does not give the extremal invariant without an additional count/witness.

## Value
**PASS** — The extremum is a natural interaction between two standard STS configurations in a classical symmetry class, and the exact boundary is certified by a structural universal lower bound plus an explicit extremal design.

## Source inspections
- **A class of Steiner triple systems of order 21 and associated Kirkman systems** (Mathon, Phelps, Rosa, Math. Comp. 37 (1981), with 1995 addendum): Abstract/bibliographic search material identifying the three-disjoint-7-cycle family and corrected class count context. Assessment: FAMILY_CLASSIFICATION_NOT_EXACT_EXTREMUM. Classification context does not state the Fano-restricted Pasch minimum in inspected material.
- **Audited witness.json** (repository blob aa0e27c9b5718c55a7f49e4f781bab3c9d11c568): Complete JSON witness. Assessment: SUPPORTS_MINIMUM. 70 blocks; marked Fano set has seven internal blocks; independent Pasch count is exactly seven.

## Residual risks
- The auxiliary census claims 135,128 total labeled systems, 61,040 Fano-containing systems, and 1,764 minimizers were not fully replayed in this run. They are not needed for the final minimum theorem and are not treated as independently certified here.
- Metadata used obsolete output/artifacts paths; the ready status update corrects the listed artifact paths.
