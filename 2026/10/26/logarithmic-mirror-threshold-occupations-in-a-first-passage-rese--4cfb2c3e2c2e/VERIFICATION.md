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
# Reproduction and limits

The embedded `verify_mirror.py` is an executable Python 3 program requiring SciPy. Run `python verify_mirror.py` from the directory containing that file. It directly quadratures the finite-size renewal probabilities with \(a=L^2/(4D)=1\) and counts \(N=10^3,10^4,10^5,10^6,10^8\). Execution was performed from this package's source path: 35 deterministic comparisons passed. The comparisons include the stationary renewal mean, exact rare occupation probability, counts for \(k=1,\ldots,6\), and conditional critical-layer means for \(k=1,2,3\).

This numerical exercise is only a consistency check. The limiting laws are justified by the separate uniform-integrability and Laplace-type arguments in `RESULT.md`; the code does not certify infinite-population behavior. Numerical rates are slowly varying because the asymptotic parameter is \(\log N\). No random sampling, external downloads or database access are required to run the script.

Scientific scope and limitations are recorded in `RESULT.md`. Independent review has not been performed.
