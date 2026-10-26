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

The file `verify_polynomial.py` can be run with Python and SymPy using `python verify_polynomial.py`. It reconstructs the derivative's degree-eight numerator, expands the Möbius-substituted polynomial, verifies all displayed coefficient and comparison identities symbolically, and checks sign variation on sample parameter triples. The run returned `PASS: transform, inequalities, and parameter samples`.

The mathematical proof is the exact coefficient cascade followed by Descartes' rule, not an inference from randomized samples. Originality was checked against the recent parent article's unrestricted open question, the unmodulated classical case, the two-periodic specialization and two published same-object research records. The 2025 paper was not available in full through authorized access. No independent audit or external formal certification has been performed.
