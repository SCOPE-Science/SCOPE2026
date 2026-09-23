# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/07/022`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `84c5b784d9240beebc350b555cd849e685ed6d7e`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

An exact census of the seven finite mutation classes meeting the connected five-vertex, arrow-multiplicity-at-most-two stratum S(5,2), with labeled mutation-class orders, exact diameters and replay certificates.

## Correctness — PASSED

A fresh implementation of Fomin-Zelevinsky mutation and breadth-first search reproduced all seven finite classes and the exact labeled sizes/diameters 270/7, 600/8, 720/9, 1440/11, 1680/11, 1980/11 and 2184/11. The soundness of the bounded-search decision was also checked against the finite-mutation weight bound and the stored rank-3 escape certificates. No substantive correctness gap was found.

## Originality — PASSED

The original context overstated novelty by omitting prior software. John Lawson's `qvfin` repository describes itself as finding all mutation-finite quivers of a given size and predates this record, so the record cannot claim to be the first enumeration of mutation-finite five-vertex quivers. The audit did not locate, in qvfin or the checked classification literature, the exact arrow-bounded stratum S(5,2) as this seven-class table together with labeled class orders, exact labeled exchange-graph diameters and replay certificates. With the context narrowed to that finite benchmark, originality passes relative to the checked evidence.

## Scientific value — PASSED

The repaired contribution is a compact exact benchmark for quiver-mutation software: seven complete labeled mutation graphs with exact orders and diameters, explicit infinite escape witnesses, and deterministic replay checks. Those data are reusable regression targets and are more than a rephrasing of the general FST classification.

## Search and independent checks

Independent checks:

- fresh Fomin-Zelevinsky mutation/BFS reproduction of all seven class orders and diameters
- recheck of rank-3 escape certificates and class disjointness
- comparison with Felikson-Shapiro-Tumarkin and jwlawson/qvfin

Literature/search queries:
- `mutation finite five vertex quivers enumeration`
- `qvfin mutation finite quivers five vertices`
- `finite mutation quiver exchange graph diameter rank 5`

Sources:
- https://github.com/jwlawson/qvfin
- https://arxiv.org/abs/0811.1703

## Repair / salvage attempt

RESULT.md context was narrowed to acknowledge qvfin as prior five-vertex mutation-finite enumeration software and to claim only the exact bounded S(5,2) table/orders/diameters/certificates.

## Final disposition

**REPAIRED.** The record remains accepted after the bounded wording/context repair above.
