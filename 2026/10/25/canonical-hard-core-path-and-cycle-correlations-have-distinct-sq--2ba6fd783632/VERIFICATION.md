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

Run `python3 verify.py` with Python 3 and its standard library (no third-party dependencies). The executable constructs the exact canonical sample spaces for paths and cycles through 21 vertices, sums occupation indicators as fractions, checks the two rational formulas and their zero loci, and separately checks finite threshold ranges. It constructs the grand-canonical partition functions by direct summation on paths through 15 vertices at activities \(1/7\), \(1/2\), \(1\), and \(7\), checking strict positivity and the conditioning formula.

The executed output from the packaged verifier was:

`VERIFY_OK 1305 exact assertions; 139038 canonical samples; grand-canonical positives`

The proof holds beyond this finite check range via exact binomial enumeration and conditional independence. Finite computation cannot certify infinite parameter ranges or historical novelty.
