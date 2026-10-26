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

# Verification evidence and limits

The full all-parameter proof is in `RESULT.md`. The standalone standard-library `verify.py` program was executed successfully from the package's actual source path. It checked the derived second-residue thresholds for each base \(2\le b\le60\), totaling 75,697 residues, by direct enumeration of all two-generator coefficient pairs below the claimed maximal threshold. An algorithmically separate unbounded-coin-change dynamic program counted all factorizations through one full modulus beyond the claimed conductor for \(2\le b\le32\). Both checks passed. The output was:

`VERIFIED: second Apéry thresholds in bases 2..60 (75697 residues); independent full denumerant DP for bases 2..32`

The finite checks only exercise the stated ranges; they do not establish the theorem for arbitrary bases without the algebraic argument. External independent verification has not been performed. Bibliographic comparisons are not proof of exhaustive publication priority.
