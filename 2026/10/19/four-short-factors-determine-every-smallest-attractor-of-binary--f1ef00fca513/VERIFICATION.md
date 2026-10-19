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

Run `python verify.py` in a standard Python 3 environment and compare stdout with `verification_output.txt`. The script constructs all distinct nonempty factors, the union of every occurrence's covered positions, and then exhaustively tests every unordered two-position set. Its expected list is separately built from the two boundary-pair formulas and checked for equality. It checks 64 rectangular-grid triples and six additional asymmetric tests (70 in total). All observed equality checks passed.

The proof is universal for integers \(a,b,m\ge2\); brute force is only finite corroboration and does not establish the theorem for untested parameters. No formal proof assistant or independent scientific audit was used. The evidence is the included source program and its reproducible deterministic output, not a test log alone.
