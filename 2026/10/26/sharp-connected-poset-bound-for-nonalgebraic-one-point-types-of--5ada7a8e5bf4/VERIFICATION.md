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

The companion standard-library Python program `verify.py` enumerates all naturally labeled finite posets through order six. It constructs admissible ideal/filter pairs independently and verifies the exact bound and star equality cases for every connected input, together with the maximal-vertex doubling inequality and equality implications. The program also checks the block deletion condition by graph reachability.

Run: `python3 verify.py`. Expected printed result appears in `verification_output.txt` and ends `ALL_CHECKS_PASS`. There are 2996 connected-poset cases and 4823 extension comparisons; these finite checks are illustrative and are **not** an exhaustive proof for unbounded \(n\). The mathematical argument in RESULT.md provides the inductive all-size proof. No independent audit has been performed.
