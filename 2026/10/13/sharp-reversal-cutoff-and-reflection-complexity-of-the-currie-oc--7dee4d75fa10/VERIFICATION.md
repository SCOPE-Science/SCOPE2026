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

Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the fixed point from
\[
0\mapsto01,\qquad 1\mapsto21,\qquad 2\mapsto0.
\]
For each \(1\le n\le8\), it verifies that the generated prefix realizes exactly \(2n+1\) distinct length-\(n\) factors. Combined with the published factor-complexity theorem, this certifies that each such factor set is complete.

It independently recomputes the reflection-class counts
\[
3,3,6,7,10,12,15,17,
\]
confirms that \(1012101\) is the only length-\(7\) factor whose reversal occurs, and confirms that it is a palindrome. It checks the complete \(17\)-element length-\(8\) list stored in `certificate.json` and verifies that none of those factors has its reversal in the list.

As a nonessential regression check, the script directly verifies the absence of reversed factor pairs through length \(40\). The theorem for every larger length is instead obtained from the exact length-\(8\) cutoff by the prefix/suffix argument in `RESULT.md`.
