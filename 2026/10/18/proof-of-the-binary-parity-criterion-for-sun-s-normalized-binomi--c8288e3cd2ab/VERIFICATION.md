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

# Reproducibility and proof boundary

Run `python3 verify.py` (Python 3 standard library). The packaged script directly constructs the published normalized binomial convolution and confirms the integer quotient, the exact factorial-valuation identity for each summand, the reflection-pair parity formula, and the mod-16 classification for every \(1\le n\le512\). The observed output is:

`VERIFY_OK: n=1..512; exact integer normalizations, valuation formulas, mod-16 dichotomy, and parity counts`

No numerical experiment is an infinite proof. The proof in `RESULT.md` uses Legendre's formula, binary carry identities, reflection symmetry, and the established normalization theorem of Guo. Full text of Guo's original arXiv version was consulted for Theorem 1.2 and its integral-factorial justification. Independent audit has not been performed.
