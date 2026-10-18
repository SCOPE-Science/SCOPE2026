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
# Verification and reproducibility

The proof is symbolic and applies to every allowed \(n,d\) and every algebraically closed field. The attached `CHECKER.py` is a standalone standard-library program and enumerates degree-\(d\) monomial generators, tests the generation of all quadratic and cubic chart monomials, exhaustively checks semigroup membership through total degree \(9\), and evaluates five local Hilbert--Samuel length identities for each of five parameter pairs.

Command: `python3 CHECKER.py`.

Observed output concludes with `VERIFY_OK`; tested pairs are (3,5), (3,6), (4,5), (4,6), (5,5). The verifier intentionally does not purport to certify arbitrary parameters or the full cohomological argument. The decisive finite-algebra steps are proved in `RESULT.md` Sections 1--4, and the projective invariants follow from Section 5. No independent audit has been performed.
