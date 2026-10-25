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

# Verification details

The proof is analytical. Its critical checks are: (i) exact trial-plane normal form under codimension-one observation; (ii) identification of the projected matrix after centering the symmetric operator and scaling its spectrum to \([-1,1]\); (iii) the two-by-two discriminant and contraction inequality; (iv) the exact largest-eigenvalue calculation; (v) the explicitly extremizing symmetric contraction with eigenvalues \(-1,0,1\); and (vi) reduction to a symmetric matrix at zero angle.

Run `python3 verify.py` in the same directory as this document using Python 3 and its standard library. The script checks an exact-rational \(3\times3\) SPD witness, seven general extremizers spanning very small and large principal angles, and 2,048 independent symmetric-contraction test configurations. The finite checks are neither exhaustive over all matrices nor substitutes for the proof. The case \(\gamma=0\) is excluded because the sampled basis loses rank. No independent audit or floating-point error certification was performed.
