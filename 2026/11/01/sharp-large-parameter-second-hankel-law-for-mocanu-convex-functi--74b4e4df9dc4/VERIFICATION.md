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

# Verification record

The proof identifies the positive-real-part coefficients \(c_1,c_2,c_3\) and derives the exact recurrence for \(a_2,a_3,a_4\). Uniformity follows from the Carathéodory coefficient bounds \(|c_j|\le1\) and explicit denominators \(1+k\alpha\), \(k=1,2,3\).

`check.py` was run with SymPy against the actual candidate file and returned:

`CHECK_OK: coefficient reduction, moment boundary, two regimes, extremal leading law`

The checker verifies exact polynomial identities, the moment maximum at \(u=3/14\), the upper-branch algebraic envelope, and the two-point moment evaluation. It does not attempt to exhaust numerical parameter samples or independently prove the existence of the univalent integral transform. Those are addressed in `RESULT.md` by the Schur/Herglotz theorem, directional convexity argument, and standard Mocanu representation.

The full text of arXiv:2606.21574 (14 pages, especially pages 12–13) and arXiv:2610.21260 (21 pages, especially theorem 3.1) was reviewed for statement comparison. The Sokół–Thomas 2018 abstract was accessible, but complete original text was not; its parameter-dependent upper bound as reproduced by the second source is insufficient to imply the new sharp coefficient. This access limitation is material to historical priority, not a proof gap.

The finding is limited to the first asymptotic term with an absolute \(O(\alpha^{-3})\) remainder. No exact finite-\(\alpha\) classification or independent audit is asserted.
