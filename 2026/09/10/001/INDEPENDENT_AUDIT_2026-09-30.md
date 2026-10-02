---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

For the committed degree-20 action of PSL(2,19), exactly 6840 ordered exact-order (2,3,19) pairs occur; all generate PSL(2,19), they split into two simultaneous-conjugacy classes of size 3420 that fuse under the outer diagonal automorphism, and the pure Hurwitz-braid action has two orbits of size 3420, giving reduced degree 2.

## Correctness — PASS

A fresh reconstruction from the committed Möbius generators produced a group of order 3420 with 171 involutions, 380 elements of order 3 and 360 elements of order 19. Scanning all 171×380 candidates gave exactly 6840 exact-order pairs, with uniform fibers 40, 18 and 19. Direct conjugation split the pairs 3420+3420; the order-18 diagonal map normalized the group, lay outside it with square inside it, and generated an extension of order 6840. A fresh pure-braid BFS gave orbit sizes 3420 and 3420. Generation follows both from the inspected per-pair verifier and the subgroup argument that a proper subgroup containing a 19-element cannot also contain the required involution.

## Originality — PASS

ATLAS records the group order, outer automorphism order, degree-20 representation and existence of standard generators of orders (2,3,19), but not the generation-filtered Nielsen count, simultaneous-conjugacy split, or pure-braid orbit census. A published-corpus semantic search returned the present result as the only direct match for the exact 6840/3420 data. The prior group-theoretic facts therefore supply setup, not the audited census.

### Equivalent formulations

The standard-generator condition is the same order pattern, but existence of one pair is not a Nielsen census.

### Broader coverage

Broader group data do not imply the exact orbit census without the additional enumeration.

### Exact database or table comparison

Database absence is not novelty proof, but no competing exact table was located.

### Claim versus prior implication

Neither existence of standard generators nor Out(G)=2 determines the number of exact-order pairs or their braid orbits.

## Value — PASS

An exact Nielsen-class and braid-orbit census for a standard-generator type of a finite simple group is a natural Hurwitz-space invariant. The result gives a complete orbit structure for the fixed type rather than a sampled computation, so the exact count and reduced degree are reusable structural data.

## Sources inspected

- Git tree/blobs: RESULT.md, status files, verify.py and committed group/orbit logs. Reconstructed the theorem inputs and checked the certificate logic.
- ATLAS L2(19): full group page including order, outer automorphism order and standard-generator section. Confirms setup but does not state the audited Nielsen or braid counts.

## Residual risks

- The full-braid 2×20520 side computation was not elevated into the audited final claim; it remains supporting logged evidence. A specialist unpublished Nielsen database could overlap with the count, but no published exact table was located.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
