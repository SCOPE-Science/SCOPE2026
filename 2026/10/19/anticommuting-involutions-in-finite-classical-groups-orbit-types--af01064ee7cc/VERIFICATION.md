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

# Verification and limits

Run `python verify_pairs.py` with Python 3.8 or newer. It constructs all matrices in several dimension-two general-linear and orthogonal groups over odd prime fields, tests their actual matrix identities, and independently counts ordered anticommuting involution pairs. It similarly enumerates the full two-dimensional unitary group over an explicit nine-element field, including the determinant image used in special-unitary orbit splitting.

A second direct enumeration constructs each two-plane in the four-dimensional vector space over \(\mathbb F_3\), tests Gram nondegeneracy, and classifies symmetric two-planes by the finite-field Witt sign. These computations produce 2160 symplectic pairs and 432 orthogonal pairs using actual subspace counts, rather than using the full-group orbit formula to count the subspaces.

All assertions passed and the checker returned `ALL_EXACT_CHECKS_PASSED`. The finite computations do not establish the theorem for arbitrary dimension or odd prime power; the general proof is in RESULT.md. No independent audit has been performed.
