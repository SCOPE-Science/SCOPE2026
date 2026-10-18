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
# Verification and scope

The exact reconstruction is in `RESULT.md`. The accompanying `check_s4_support.py` uses no third-party dependencies; its arithmetic is the exact integer-pair model of \(\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\). The program was executed from its current file path and verified all \(24\) determinant-one signed permutation matrices, all \(81\) pairwise coefficient orthogonality equations, all nine support witnesses, and exact instances of the quartic alternating identity. A deterministic finite-alphabet stress test checked \(15{,}376\) pairs of nonzero vectors and found no forbidden cardinality.

Run: `python3 check_s4_support.py`.

The general impossibility of zero counts \(5\) and \(10\), as well as the bound on other zero counts, follows from the explicit exhaustive case proof in `RESULT.md`, not from the finite-alphabet test. The Fourier transform is normalized by \(1/24\), and the relevant nonzero irreducible block has rank one and degree three. No numerical approximation, exhaustive search over \(\mathbb C\), or independent external verification is asserted.
