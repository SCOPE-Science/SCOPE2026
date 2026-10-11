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

# Verification

The proof's finite certificate consists of explicitly constructed integral state matrices, not inferred values from a floating-point calculation. Run `python3 artifacts/verify.py` from the extracted package root. The standard-library verifier reconstructs all 21 allowable six-row masks, the transition matrix and three boundary vectors, and checks the three **exact 21-component equalities** after 28 matrix multiplications. A separate three-state computation proves the four-step two-row boundary identity. It independently rebuilds every vertex orbit and conflict edge for the four automorphisms on all widths \(1\le n\le8\), evaluating the signed independence polynomial by deletion-contraction recursion. Expected output: `VERIFY_OK`.

The same run checks the complete 28- and 56-entry tables, the boundary values at \(n=0,1,57\) where applicable, all claimed periodicities through representative additional periods, minimal period 56 by excluding divisors 28, 8, 7, and integrality of virtual one-dimensional character multiplicities for 120 widths.

The computer-assisted component is an **exhaustive finite matrix identity on 21 states**; once established, the mathematical proof implies the result at every positive width. Direct graph enumerations in finitely many widths are confirmatory and are not presented as an infinite proof. The claims do not determine degreewise equivariant homology outside the specified \(n=8\) example and do not constitute independent audit or external certification.
