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
The package contains `verify.py`. It was replayed from the packaged source before ledger assembly and returned `VERIFY_OK`.

The checker verifies with exact rational arithmetic that the finite first-passage sum equals a direct dynamic program for every reciprocal level \(2\le r\le12\) and every horizon through \(150\). It exhaustively checks every short sign string for the equivalence between the Knockoff+ prefix condition and the random-walk hitting event. It also computes the smaller fixed-point root at high precision and verifies the displayed constants for \(r=2\) and \(r=10\).

The checker does not replace the published knockoff sign-flip lemma or the standard Lagrange-inversion theorem; those are used explicitly in the mathematical proof. The result assumes complete nullity, distinct nonzero magnitudes, and exact iid conditional signs.
