# Independent Audit — 2026/09/12/025

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `077249604d0872b0e20feb9d712795a7d80c3a4e`  
**Disposition:** **PASSED**

## Correctness

The depth-two lower bound is independently reproducible from the frozen certificate. I reimplemented the STS pair-balance test, Pasch count, 6-cycle record enumeration, mitre count as a count of distinct seven-point supports, and the hexagon switch itself. All 57 systems in the Netto/A4 roster and all 32 systems in the alternate cyclic roster are valid STS(19)s; every stored child/representative is reached by the recorded legal 6-cycle switch; and all recomputed (Pasch, hexagon-record, mitre) keys equal the stored keys and are pairwise distinct within each roster. Hence the certificate proves at least 57 distinct isomorphism classes within distance at most two of the A4 starter, and at least 32 for the alternate starter.

## Originality

The 2010 complete STS(19) property census identifies A4 as the unique 5-sparse STS(19) and reports 171 hexagons, but it does not give a radius-two 6-cycle-switching ball. Erskine and Griggs (2025) determine the global connected components of the 6-cycle switching graph S_6(19), including components of sizes 24, 284,433, and 11,084,590,371, but targeted inspection found no local radius-two roster or the 57-class A4 lower bound. A global component cardinality does not imply the claimed local branching bound.

## Scientific value

A certified local branching invariant around the unique 5-sparse STS(19) is a nontrivial, reusable datum about the geometry of the 6-cycle switching graph. The explicit depth-two representatives and invariant certificates can be used to benchmark switching searches and to distinguish local expansion from the already-known global component structure. The result is modest but clears the value threshold as an exact invariant of a canonical extremal design.

## Limitations

- The result is a lower bound on a radius-two ball, not an exact radius-two census and not a statement about the full S_6(19) component size.
- Distinctness is certified by pairwise-distinct exact invariant triples; the audit does not claim those triples form a complete isomorphism invariant in general.
- The certificate covers the two named cyclic anti-Pasch starters only.

## Evidence

- [Colbourn et al., Properties of the Steiner Triple Systems of Order 19](https://doi.org/10.37236/370): The complete STS(19) census identifies A4 as the unique 5-sparse system and reports its 171 hexagons, but does not state the submitted radius-two switching-ball bound.
- [Erskine–Griggs, Cycle Switching in Steiner Triple Systems of Order 19](https://doi.org/10.1002/jcd.21975): Determines global connected components of the cycle-length switching graphs, including S_6(19), without publishing the submitted local radius-two roster around A4.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `077249604d0872b0e20feb9d712795a7d80c3a4e`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
