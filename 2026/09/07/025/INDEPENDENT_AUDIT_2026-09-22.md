# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/07/025`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `3611d205c795122d1e40e534cdf12e8cbc1aeab1`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

The exact point-line incidence maximum M(8,8)=24 in PG(2,4), with exhaustive extremal-set and pair census and degree-profile split.

## Correctness — PASSED

A separate construction of PG(2,4) and exhaustive enumeration of all 8-point sets reproduced the top-eight line-degree ceiling 24, exactly 7560 attaining point sets, and the dual count. Recounting compatible top-degree line choices reproduced 22680 attaining point-line pairs and the stated profile split. The pair-counting bound and explicit witnesses were also checked. Thus the finite theorem and census are correct.

## Originality — PASSED

The literature contains 24-incidence configurations related to the Möbius-Kantor geometry, so the existence of a single 24-incidence witness is not treated as novel. The audit did not locate a prior exact proof that 24 is the 8-by-8 ceiling in PG(2,4), nor the 7560/22680 exhaustive census and profile split. Relative to the checked finite-geometry literature, that exact ceiling plus census survives as the original contribution.

## Scientific value — PASSED

An exact small-order extremal incidence number closes a case where standard KST/spectral bounds are loose, and the complete attainer census supplies concrete regression data for finite-plane and incidence-enumeration software. The result therefore has a specific reusable role beyond an isolated example.

## Search and independent checks

Independent checks:

- independent PG(2,4) reconstruction and exhaustive 8-set enumeration
- independent attainer-pair/profile recount
- comparison with prior small finite-geometry incidence constructions

Literature/search queries:
- `PG(2,4) 8 points 8 lines 24 incidences`
- `Möbius Kantor PG(2,4) incidence 8 8`
- `finite projective plane order 4 maximum incidences 8 points lines`

Sources:
- https://doi.org/10.1007/s10623-022-01131-2

## Final disposition

**PASSED.** The record remains accepted on all three audited axes.
