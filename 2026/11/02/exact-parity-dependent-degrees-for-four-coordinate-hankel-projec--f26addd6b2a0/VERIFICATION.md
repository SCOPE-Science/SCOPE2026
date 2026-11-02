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

# Verification notes

The algebraic argument reduces a generic three-observation fiber to the conic \(S^2=Q(P)\), and checks that the leading coefficients of the remaining moment functions are nonzero if \(s_0s_2(s_2^2-s_0s_4)\ne0\). The exact map degree follows from a degree-two conic projection for even moments, or a univariate eliminant with a unique lift for odd moments. These are proofs valid for every integer \(n\ge6\) over \(\mathbb C\).

The enclosed `verify_degree.py` is an optional exact symbolic consistency checker. It uses rational coefficients \((s_0,s_2,s_4)=(2,3,5)\) and verifies recurrences and generic-degree polynomial identities for \(6\le n\le21\), including the six independently published values for \(7\le n\le12\). The successful run prints `VERIFY_OK`. The finite computation is not a substitute for the proof or independent verification.

No independent mathematical audit or external validation has been performed. The unproved scope includes branch loci, higher rank, exceptional fibers, and other observation subsets.
