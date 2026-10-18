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

The source `check_heisenberg_abelian_endos.py` can be run with Python 3.9 or newer and no external dependencies. It uses independent row-reduction enumeration of matrices, not a circular restatement of the generating function.

Observed complete matrix strata for \(n=1\): over \(\mathbb F_3\), ranks \((r,s)=(0,0),(1,0),(1,1)\) have counts \(1,20,12\); over \(\mathbb F_5\), \(1,114,30\); over \(\mathbb F_7\), \(1,328,56\). Corresponding abelian-image fixed-point-free group-map counts are \(189\), \(2875\), \(16121\).

For a fixed isotropic image in four-dimensional symplectic space, direct enumeration gives \(X_{2,1,s}(3)=(53,27)\), \(X_{2,2,s}(3)=(3675,2484,81)\), \(X_{2,1,s}(5)=(499,125)\), and \(X_{2,2,s}(5)=(297005,89250,625)\). An independent enumeration confirms the 40 totally isotropic planes over \(\mathbb F_3\). A direct exhaustive multiplication-table test confirms one nontrivial fixed-point-free abelian-image homomorphism on the order-27 Heisenberg group.

The final checker output is `ALL_FPF_AB_IMAGE_COUNTS_PASSED`. The general theorem, including all odd primes and all ranks, rests on the proof in `RESULT.md`, not finite samples. No independent audit or validation is claimed.
