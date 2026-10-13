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

The standalone `artifacts/verify.py` reconstructs the claim from the fix-free definition. It enumerates all \(2^4\) subsets of the length-two words and all \(2^8\) subsets of the length-three words, discards every incompatible pair, and for each remaining pair counts all length-four words whose prefix and suffix avoid the selected shorter words. Since equal-length distinct words do not create prefix/suffix conflicts, this available count is exactly the maximum admissible longest layer for that pair.

The script checks the complete claimed table exactly. It then scans every integer profile with scaled Kraft weight \(4a_2+2a_3+a_4\le16\), confirms that all profiles of scaled weight at most \(12\) are feasible, and finds scaled weight \(13\) as the first infeasible level, with unique profile \((2,0,5)\). The captured output in `artifacts/verification_output.txt` starts with `VERIFY_OK`.

The verifier was replayed directly from the embedded verification artifact. The proof uses the exhaustive computation only for this finite domain; no claim is made for other allowed lengths or alphabets.
