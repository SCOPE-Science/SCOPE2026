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

The proof uses an independent-leaf upper bound, an equality rigidity argument, nine explicitly listed small cyclic mask words, and a local triple-gluing rule. The finite checks were run by Python 3 with no third-party package.

Run `python3 verify.py` from a folder containing `verify.py`. The script constructs all graph adjacencies, computes the conflict relation directly, and checks exact maximum values for each \(n=3,\ldots,40\) with a separately coded transfer dynamic program. It then directly verifies the constructive witnesses for each \(n=3,\ldots,200\), and enumerates all six-edge candidate packings at \(n=6\), obtaining six. Output is preserved in `verification_output.txt`.

The infinite claim is proved by explicit concatenation and an upper-bound equality argument, not by extrapolation from the finite computations. The finite checker does not establish bibliographic priority or independent validation.
