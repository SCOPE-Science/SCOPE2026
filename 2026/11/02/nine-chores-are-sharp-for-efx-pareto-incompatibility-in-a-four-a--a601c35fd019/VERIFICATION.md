---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For precisely four agents in two identical disutility pairs and three item cost types A=(r,r,r,r), B=(1,1,r,r), C=(r,r,1,1), with arbitrary real r>3, I reconstructed the integer 4×3 allocation incidence matrices and checked that EFX removes an item from the comparing agent’s own bundle while PO quantifies over all allocations. There are C(11,3)=165 profiles with <=8 chores, and 125970 allocation matrices summed over profiles. Every EFX and dominance inequality is affine in r with integer coefficients bounded by eight: the complete sign partition of (3,infinity) has breakpoints 7/2,4,5,6,7,8. I independently implemented exact scaled-integer vectorized enumeration of all 13 representative cells × 165 profiles; every profile has EFX+PO, and for the nine-item (3,3,3) case no EFX+PO occurs in the four independently tested cells. The unrestricted nine-item obstruction is credited to He–Tao Theorem 2, not extrapolated from the four checks. These finite cells are mathematically exhaustive for the positive claim only because all parameter-breakpoint signs were justified.

## originality

PASS

Qualified acceptance for the universal <=8-chores compatibility statement in the precisely specified complementary class family. The 9-item obstruction is explicitly prior work; neither that counterexample nor EFX-only existence implies all <=8 EFX+PO cases.

## value

PASS

The first joint EFX/PO incompatibility size in this natural positive-cost two-pair market is a mathematically motivated sharp threshold: a nine-item counterexample already existed, but this result rules out all smaller instances in the same domain. The exact 165-profile, 13-parameter-cell certificate is a substantive all-instance classification and independent reproducible boundary, not a routine reparameterization of the known bad example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
