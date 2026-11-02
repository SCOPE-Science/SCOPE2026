---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The included `verify_weighted.py` constructs grounded weighted Laplacians independently from edges, solves each inverse with exact rational Gaussian elimination, and checks every possible leader pair for the tested parameter instances against the five rational objective expressions. The recorded output follows a direct execution of that program.

Exact tests cover clique sizes from two to six, four independent pairs of positive internal weights, and three positive bridge rates, totaling 300 network configurations and 9000 exact grounded inversions. Two-clique sizes of two are included only as additional computational boundary checks; the stated theorem covers orders at least three. The verification also checks that 2400 same-clique non-gateway patterns are strictly inferior to the corresponding gateway-containing pattern, checks exact ties at \(t=16/115\) and \(t=8/5\) for \((p,q,a,b)=(16,3,1/10,1)\), and tests the no-colocation inequalities for many integer size pairs.

These are finite checks and not an exhaustive verification of infinite ranges, symbolic identities for arbitrary network sizes, uniqueness claims beyond the explicit pattern symmetries, or publication originality. The five-formula calculation and the sharp threshold are proved in `RESULT.md` by exact clique inverses, a cut-edge series law, and strict rational comparisons. No external independent audit has been performed.
