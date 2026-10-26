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

# Reproducibility
Run `python verify.py` using Python 3 standard libraries only. Expected final output: `VERIFY_OK`.

The script (i) computes integer coefficients \(U_m(n),V_m(n),W_m(n)\); (ii) exhaustively checks the forbidden complementary-pair condition for ranks two and three through finite lengths; (iii) independently counts admissible multisets using XOR-state dynamic programming for ranks three and four, including \((d,n)=(4,16)\); and (iv) checks the rank-three length-eight support-multiplicity census. No floating-point tolerance, random seeds, external data, or nonstandard software are required.

The proof of the general formula is the character-orthogonality and two-point-coset argument given in `RESULT.md`. Finite tests alone do not imply the statement for every \(d\) and \(n\), and the computations are not an independent scholarly audit.
