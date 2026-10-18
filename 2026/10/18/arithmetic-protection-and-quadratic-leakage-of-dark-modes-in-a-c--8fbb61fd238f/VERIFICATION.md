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

The proof is analytic and covers all integers \(m\ge1\), all real \(\varepsilon\ne0\), all sites \(1\le s\le m\), and all fixed positive \(J,\gamma\); the local perturbation expansion is at \(\varepsilon=0\).

Reproduce the independent finite-matrix checks by running `python verify.py` with NumPy. The script constructs the whole-chain non-Hermitian matrices directly, tests exact arithmetic survival counts for every \(m\le8\) and allowed defect site at two loss rates, evaluates eigenvector residuals for surviving dark modes, and tests 380 nonnode linewidth configurations by two small-detuning scales. It reports `VERIFY_OK` when all assertions pass. Use `python verify_exact.py` with SymPy to independently reproduce exact characteristic-polynomial derivative comparisons for four \(m,s\) pairs. The infinite family does not depend on finite enumeration; no external/independent review has been performed.
