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

# Verification of rank-refined clarification spectra

Run `python3 verify.py` using Python 3.8+ and the standard library. An actual execution completed with `VERIFY_OK`.

The program enumerates the entire binary incidence-table space for each size from \(1\times1\) to \(4\times4\), not a random sample. For each matrix it computes the number of distinct rows, distinct columns, and finite-field rank by direct elimination and compares that triple to the closed counting formula. It also tests \(\mathbb F_3\) for sizes through \(2\times2\), checks the independent finite-field rank-stratum normalization for \(q\in\{2,3\}\) and \(r,m\le6\), and independently checks the sharp tuple-support criterion for \(d\le5\) in characteristic two.

The finite checks validate implementations and boundary cases only; the infinite result depends on the elementary exact factorization and subspace-lattice Möbius arguments in RESULT.md. No formal proof assistant, independent peer review, or external certification is claimed.
