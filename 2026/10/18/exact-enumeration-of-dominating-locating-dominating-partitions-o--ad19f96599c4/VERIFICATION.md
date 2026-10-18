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

# Verification record

Run `python3 verify.py` (Python 3 standard library only) in a folder containing this file and the standalone verifier. The script checks labelled cycles \(C_n\) for each \(3\le n\le16\) by exhaustive membership assignments. It independently evaluates each proposed partition from the actual open-neighbourhood definition, and compares against a direct cyclic pattern scan. For \(n\ge5\) the predicates agree on every assignment. For \(n=4\), the only spurious local solutions are \(0101\) and \(1010\). The script separately computes coefficients through degree \(30\) from the transfer matrix trace formula and from the determinant's coefficient equation, checks equality, and checks the two low-degree corrections. Total assignment checks: \(131064\); the final line should be `VERIFICATION_OK`. The complete recorded output appears in `verification_output.txt`.

**Non-computational part.** The proof's crucial infinite steps are the location-collision equivalence, weighted cyclic run decomposition, determinant identity, and the uniqueness of the dominant positive root. The finite checks cannot establish those steps in full generality. Reproducibility does not constitute independent mathematical validation. Priority relative to all publications is not certified.
