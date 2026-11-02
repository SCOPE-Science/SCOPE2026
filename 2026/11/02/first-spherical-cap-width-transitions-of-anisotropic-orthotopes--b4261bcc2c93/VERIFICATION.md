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

The theorem's universal steps are mathematical: the unit sphere decomposes into equal orthants, a cap crosses its first coordinate facet exactly at \(q\), no double crossings occur in a small neighborhood of \(q\), and an explicit parabolic blow-up yields the coefficient of \(\varepsilon^{d/2}\). An exact one-dimensional regularized-beta integral supplies the all-dimensional local correction and shows dependence only on \(d,L,m,k\). The explicit four-dimensional noncongruent side vectors have the same four invariants. The four-dimensional antiderivative gives an exact, not approximate, formula.

`verify.py` requires Python 3, NumPy and SciPy. Run `python3 verify.py` from this directory. An actual execution returned `VERIFY_OK 87 independent numeric, exact integration and sphere-distribution tests`. The tests evaluate special cases in dimensions four, five and six, independently integrate individual spherical facet caps, compare the leading asymptotic coefficient, and independently sample over a million random sphere directions in dimension four.

Finite numerical quadrature and sampling do not establish an infinite-dimensional or arbitrary-parameter theorem and cannot certify historical originality. The result does not assert robustness for noisy empirical width distributions. An independent external audit has not been performed.
