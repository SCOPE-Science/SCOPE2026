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

The proof is checked by `artifacts/verify.py` using only the Python standard library. The script verifies the local-instrument completeness identities through the exact squared diagonal entries, the exact branch probabilities \(1/4\) and \(3/4\), the branch values \(1\) and \(0\), and the strict input bound.

The key nonnumerical certificate is \(2^{19}<7^7\), which implies \(\log_2 7>19/7\), hence \(h_2(1/8)<5/8\). Exact rational arithmetic then checks \(125/512<1/4\). The floating-point value printed for the initial product is diagnostic and is not used to establish the theorem.

The verification does not test a mixed-state extension or the geometric-mean MEMS quantities; those lie outside the claim.
