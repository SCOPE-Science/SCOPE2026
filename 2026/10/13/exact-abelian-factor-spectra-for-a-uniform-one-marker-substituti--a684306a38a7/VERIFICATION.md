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

Run `python3 verify.py` beside `certificate.json` using a standard Python 3 interpreter.

The verifier implements substitution expansion and a separate digit-recursive construction. It compares the resulting words, independently checks all aligned prefix counts and factor boundary formulas, and enumerates exact observed Hamming-weight spectra for \(2\le b\le17\) and \(1\le n\le8b-1\).

For each tested parameter it checks that both oriented binary disagreements occur at lags \(1\) through \(128\). These finite computations are regression evidence only. The infinite proof uses the elementary block structure, aperiodicity, and a bounded telescoping identity and is given in `RESULT.md`.
