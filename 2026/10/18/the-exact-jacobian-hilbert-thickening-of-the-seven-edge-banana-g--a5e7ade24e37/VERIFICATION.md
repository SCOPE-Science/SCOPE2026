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

# Exact verification and limitations

Install the pinned dependency using `pip install -r requirements.txt`, then execute `python check.py` with Python 3. The script works entirely over exact rational coefficients and regenerates the degree-six graph polynomial, its seven Jacobian generators, their 51-member Gröbner basis, Hilbert numerators, graded monomial dimensions for degrees five through nine, and the transverse local degree-three calculation. Successful output ends with `VERIFY_OK` and prints the precise series and Hilbert-polynomial difference.

The seven-variable Hilbert series follows from an exact Buchberger computation plus the standard monomial-ideal colon exact sequence, rather than from partial interpolation or experimental extrapolation. The checker requires a correctly functioning SymPy 1.14 implementation; this is a self-review, not an independent audit or human certification. No claims concerning characteristic other than zero, a full primary decomposition, or untested other banana sizes are verified.
