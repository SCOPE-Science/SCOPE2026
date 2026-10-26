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

# Verification of the two-frequency flexural–gravity inverse result

The proof in `RESULT.md` derives the scalar inverse function \(G_U(t)\) and proves its derivative is strictly negative by \(\sinh(2qt)>q\sinh(2t)\) and \(1+q^4b<q^4(1+b)\). Explicit endpoint limits give both necessity and sufficiency of the strict data inequalities for all \(q>1\), \(t>0\), \(b>0\). This is an analytic infinite-parameter proof, independent of the numerical samples.

Run `python checker.py` from the extracted files. The code uses SciPy's `brentq` and standard-library trigonometric functions. It tests 120 positive input triples, evaluates the exact realizability inequalities, verifies the reconstruction and the forward Jacobian sign, and prints a reproducible parameter example. All tested cases passed on the execution environment.

Limitations: The numerical checks are finite and have floating-point tolerances, not exhaustive proofs. No laboratory observations or independent external audit were performed. The idealized massless-sheet dispersion law excludes additional constitutive and inertial parameters, and the inverse need not be well conditioned near limiting depths.
