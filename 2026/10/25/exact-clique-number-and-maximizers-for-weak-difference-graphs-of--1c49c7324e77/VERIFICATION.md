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

The standalone `verify.py` uses Python 3, NumPy, and SciPy (the `scipy.optimize.milp` solver). From the directory containing the file, run `python verify.py`. The solver constructs one binary variable for each nonempty proper support of \([t]\), gives it the exact integer class weight, and adds an exclusion inequality for each pair of disjoint supports. Its objective maximizes total graph-clique weight, independently of the paper's complementary-pair proof.

The checked parameter pairs are \((t,q)=(5,2),(5,3),(5,4),(5,5),(6,2),(6,3),(6,4),(7,2)\). The predicted and solver-certified optimum values, in that order, are \(15,85,275,645,31,326,1491,63\). Each solve returned an optimal integer-program status and the asserted value. Separately, for \(t=6\) the checker forms the \(10\) complementary middle-size pairs, constructs all \(2^{10}=1024\) choices and confirms pairwise intersection with all mandatory large supports and coatoms.

Printed success markers are `VERIFY_OK` and `MAXIMIZER_SUPPORT_CENSUS_OK`. Values with \(q=2\) are boundary controls; the claim that **all** maximizing cliques have the given form is made only for \(q\ge3\).

These computations are finite checks, not exhaustive tests of every field and dimension. An independent mathematical audit has not been performed. The complete mathematical argument is in `RESULT.md`.
