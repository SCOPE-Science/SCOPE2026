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

# Verification and reproducibility

Install Python 3 and SymPy, then run `python check.py` from this package directory. The included `check-output.txt` records the actual run. The program tests 330 exact rational/symbolic assertions for all degrees from one to eleven. These tests exercise the normalized Legendre-square cap integral, the factorial boundary-product formula, positive-root counts, absence of shared positive roots at derivative gap two, and hemisphere-leading-order comparisons.

The proof is in `RESULT.md`. General-degree validity rests on the raising relation, differential equation, repeated Rolle argument, and parity/asymptotic proof. The finite calculation alone does not imply any statement for untested degrees. No nonconsecutive spectral equality classification or general low-pass Slepian claim was checked. Independent mathematical audit has not been performed.
