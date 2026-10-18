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
# Reproducibility and proof boundaries

Run `python3 verify.py` in a directory containing the standalone verification script. The script requires Python 3 with its standard library only. It performs exact modular matrix arithmetic; no randomness affects conclusions because the pseudorandom term generator uses a fixed seed.

It verifies the linear-algebraic hypotheses, constructs polynomial matrices of degrees below the space dimension, independently closes binary term coefficients under the affine operation and checks that they equal the polynomial coefficient ring, exhaustively counts each coefficient kernel and tests multiple three-variable term equations by evaluating every input triple. Six listed cases pass, with ranks:

- Scalar matrix over \(\mathbb F_3\) in dimension 2: \(\{0,2\}\).
- Nontrivial Jordan block over \(\mathbb F_3\) in dimension 2: \(\{0,1,2\}\).
- Irreducible quadratic over \(\mathbb F_2\) in dimension 2: \(\{0,2\}\).
- Distinct scalar eigenvalues over \(\mathbb F_5\) in dimension 2: \(\{0,1,2\}\).
- A Jordan block plus a scalar block over \(\mathbb F_3\) in dimension 3: \(\{0,1,3\}\).
- A squared irreducible quadratic over \(\mathbb F_2\) in dimension 4: \(\{0,2,4\}\).

The expected output terminates with `ALL CHECKS PASSED`. This is an arithmetic cross-check, not an exhaustive theorem prover for all primes, dimensions or terms. The universal mathematical proof is given in RESULT.md and uses the principal-ideal and finite-subquasigroup lemmas explicitly. Bibliographic comparison uses reviewed primary papers but absolute priority and independent audit remain open.
