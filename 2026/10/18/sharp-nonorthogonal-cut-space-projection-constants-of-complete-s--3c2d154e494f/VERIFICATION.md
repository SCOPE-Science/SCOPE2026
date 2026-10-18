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
# Reproducibility and scope

The analytic proof in `RESULT.md` applies to every integer pair \(m,n\ge2\); no finite test establishes that universal assertion.

`VERIFY.py` uses Python standard-library exact rational arithmetic. From an extracted package directory run `python VERIFY.py`. It constructs oriented incidences, inverts the grounded integer Laplacian, computes the Euclidean projector, adds the explicit circulation-to-cut correction, checks projection idempotence and pointwise identity on cuts, and checks all predicted rational norms and gaps. It passed all \(16\) configurations with \(2\le m,n\le5\), totaling \(276\) tested projector columns.

`VERIFY_LP.py` optionally solves the *unrestricted* minimum-operator-norm projection linear program using NumPy and SciPy's `linprog` with the HiGHS backend. Run `python VERIFY_LP.py` after installing NumPy/SciPy. It passed \((m,n)\) equal to \((2,2),(3,2),(3,3),(4,2),(4,3)\), with discrepancies smaller than \(10^{-8}\). This numerical optimization is corroborative only, not a proof of global minimality in all dimensions.

Both programs have complete local inputs: no network calls or external data files are required. The proof's source normalization is the unweighted edge-\(\ell_1\) norm, and the target is the graph-gradient subspace, not the cycle subspace.
