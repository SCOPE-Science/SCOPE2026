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

Run `python3 verify.py` using Python 3 and no third-party packages. The verifier exhaustively checks all \(16\) two-dimensional evolution multiplication tables and every linear operator over \(\mathbb F_2\), then all \(256\) such tables and operators over \(\mathbb F_4\). Both ordinary Rota–Baxter identities are tested on all natural-basis pairs; the pointwise-local predicate is tested at every input, with witnesses drawn from the completely enumerated ordinary operators. The structural classification, operator counts and numbers of labeled tables are compared exactly. Five representative types over \(\mathbb F_8\) are checked independently. Nilpotent chains in dimensions three and four over \(\mathbb F_2\) are also checked over all \(512\) and \(65,536\) endomorphisms respectively. Finite-field multiplications use specified irreducible binary polynomials; no integer-modulo-four substitution is used. Successful execution prints `VERIFY_OK`.

These finite experiments do not establish the theorem for all even prime powers or arbitrary-dimensional characteristic-two fields. That part is proved by the square-zero-output identity and by the bilinear-form and projective-line arguments in `RESULT.md`. Neither statistical support nor a test timeout is construed as an all-parameter theorem.
