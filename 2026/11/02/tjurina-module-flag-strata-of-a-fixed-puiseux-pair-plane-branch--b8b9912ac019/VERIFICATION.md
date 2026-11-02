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

# Reproducibility and limits

`artifacts/verify_tjurina.py` is a standalone exact-arithmetic Python script requiring SymPy. Run it from the directory containing the six accompanying documents with `python3 artifacts/verify_tjurina.py`. It performs 38 independent Gröbner calculations in the polynomial rings over \(\mathbb Q\), enumerates standard monomials, checks the predicted leading-term ideal, checks representative parameter strata (including zero and nonzero higher coefficients), and verifies the weighted Euler coefficient identity. The observed output was `VERIFY_OK: 38 exact Gröbner quotient checks`.

The theorem for every \(m\ge5\), \(q\ge2\) and all complex coefficients is established by the algebraic proof in `RESULT.md`, not by extrapolation of the finite computations. The script does not certify the literature-comparison result, geometric equivalence beyond the stated local family, or a projective global Hodge claim. Independent mathematical validation has not been performed.
