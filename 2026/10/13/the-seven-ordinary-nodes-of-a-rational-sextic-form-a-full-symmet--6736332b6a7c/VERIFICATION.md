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

# Exact verification

The included `verify.py` uses Python 3 and SymPy with exact rational and modular arithmetic. Run `python verify.py` in the directory containing the file. A successful execution reports `VERIFY_OK`, the degree-seven residue fields, the Galois group, and modular and diagonal-exclusion checks. No numerical root approximations are used.

The checker reconstructs the three antisymmetric coordinate wedges and divides them exactly by the diagonal factor; expresses the quotients in \(u=a+b\), \(v=ab\); recomputes their Gröbner basis over \(\mathbb Q\); verifies the displayed septimic and the unique symmetric sum coordinate; proves both the parameter-pair discriminant and first coordinate remain nonzero; tests irreducibility modulo \(79\); and tests the explicit squarefree factorization with its irreducible quadratic modulo \(199\). These finite certificates are exact identities. The logical passage to \(S_7\) uses transitivity in prime degree and a transposition, and node field equality uses normalization descent.

The published primary construction is used for the independently documented fact that the resulting rational sextic has exactly one \(A_5\) and seven ordinary nodes and that its normalization is proper. The computation tests the new arithmetic classification; it does not purport to certify unrelated curves or a general-family theorem. An independent external mathematical audit has not been performed.
