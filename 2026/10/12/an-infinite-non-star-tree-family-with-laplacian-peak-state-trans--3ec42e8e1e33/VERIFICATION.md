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

The infinite claim is verified analytically by the following exact chain.

1. Symmetry decomposition shows that leaf-difference and branch-standard eigenspaces have zero root coordinate and therefore zero root-to-child spectral-projector entries.
2. On the fully symmetric subspace, the exact characteristic polynomial is \(\lambda(\lambda-b)(\lambda-(2b+1))\).
3. The exact root-to-child projector entries are \(1/(b(2b+1))\), \((b-1)/(b(b+1))\), and \(-2b/((b+1)(2b+1))\).
4. The mutual-support gcd is \(1\). The published Laplacian peak-transfer parity criterion therefore holds exactly when \(b\) is even and then gives odd multiples of \(\pi\) as all peak times.
5. Summing the absolute projector entries gives \(4b/((b+1)(2b+1))\).

The packaged exact-arithmetic checker evaluates the quotient projectors directly for \(2\le b\le24\), verifies their projector identities and signs, and checks the amplitude/parity conclusions. This finite replay is a consistency check, not the proof of the universal quantifier.
