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
# Reproducible checks

Run `python3 verify.py` in the directory containing this file and the script. The program exhaustively enumerates all \(2\times r\) coefficient arrays and tests every pairwise minor using ring arithmetic; it does not use valuation strata or factor the answer into outer products.

Twelve cases cover residue sizes \(2,3,4\), nilpotency lengths up to four, two or three tuple elements, both \(\mathbb Z/p^m\mathbb Z\) and truncated-polynomial chain-ring models. The exhaustive counts in the run are printed with the expected final marker `VERIFY_OK_HEISENBERG_CHAIN 12 cases`. The check for \(q=4\) explicitly uses the extension field \(\mathbb F_4\), not integers modulo four.

The script verifies the \(2\times r\) determinantal factor; multiplying by \(q^{mr}\) accounts for all independent central coordinates of the group tuples. Independent verification of the all-parameter theorem is not claimed. The mathematical proof is in `RESULT.md`.
