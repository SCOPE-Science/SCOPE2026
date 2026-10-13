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

# Verification of quadratic multiplication-rank spectra

The reproducibility artifact is `VERIFY.py` (Python 3 standard library only). From the directory containing the result, run `python3 VERIFY.py`.

The script enumerates every \((a,b,c)\in\mathbb F_q^3\) for \(q\in\{2,3,4,5,7,8,11,13\}\) and \(3\le m\le60\), computes continuant determinants using actual arithmetic in each finite field, and compares their exceptional coefficient counts with the claimed \(\gcd\) expression. For an independent structural check it constructs the entire graded multiplication matrix of \(ax^2+bxy+cy^2\) in \(\mathbb F_q[x,y]/(x^m,y^m)\) for additional small \((m,q)\) and computes ranks by Gaussian elimination. The successful run prints `VERIFY_OK_QUADRATIC_LEFSCHETZ` and the case count.

The exhaustive finite experiments are restricted to those named parameters; the algebraic argument in `RESULT.md` proves the general claim. The nonstandard characteristic and Frobenius orbit boundaries are addressed in the proof, not extrapolated from the tests. There is no independent mathematical audit.
