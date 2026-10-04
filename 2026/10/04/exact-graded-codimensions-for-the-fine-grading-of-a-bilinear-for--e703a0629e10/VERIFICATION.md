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

The proof in `RESULT.md` is symbolic. The critical steps are: (1) each homogeneous component of the fine grading is zero- or one-dimensional; (2) two or more odd nonzero-degree counts force total degree outside the support; (3) when at most one count is odd, equal-degree variables can be paired first and each pair evaluates to a nonzero scalar because the orthogonal basis vectors have nonzero norm; and (4) character orthogonality counts the surviving degree words.

`verify.py` independently enumerates all degree words for \(1\le n\le6\) and \(1\le m\le8\), checks the parity criterion against the closed character-sum formula, and checks the \(n=2\) Klein formula. `verify_output.txt` records the run and ends with `CHECK_OK`.

The finite enumeration is not used as an infinite proof. It verifies only the combinatorial identity and guards against indexing/parity errors. Characteristic \(2\) and non-multilinear finite-field identities are outside the claim.
