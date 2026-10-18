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

The provided `verify.py` was executed with Python and SymPy after constructing this result. It produced `PASS: 1905 exact Chebyshev/finite-Markov checks; N=2..60`. The checks enumerate all interior start positions for the stated dimension range, verify the full sign polynomial coefficient-by-coefficient using integer arithmetic, and independently compare the matrix-inverse expected absorption time with the Chebyshev formula at three exact rational reset rates for dimensions at most ten. These calculations are finite and do not by themselves imply the infinite-family theorem; the coefficient proof in `RESULT.md` does. No external or independent audit is reported.
