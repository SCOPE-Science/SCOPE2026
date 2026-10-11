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

Run `python verification/check.py` with Python 3 and no nonstandard dependencies. The expected deterministic success message is:

```
VERIFY_OK p1_exact_pairs=1083 simplex_grid_points=4960 phase_p0=0.630929753571 analytic_global_proof_required=True
```

The script evaluates the minimum over three spanning trees for rational affine coordinates. For \(p=1\) it uses exact rational arithmetic on \(361\) points (including points outside the probability simplex) and checks the universal radius bound; the count \(1083\) is three tree-norm evaluations per point. For ten positive exponents it checks the bound on all \(496\) integer-grid simplex points of mesh \(1/30\), along with leaf and barycenter witnesses; \(4960\) means ten exponents times those points. The check is not an exhaustive enumeration of all affine coefficients or real exponents.

The theorem for every real \(0<p\le1\) relies on the analytic proof in `RESULT.md`: universal upper witnesses, the known exact free-space spanning-tree formula, Banach-envelope lower control, and strict concavity plus equality analysis on the ordered simplex. All limiting statements and all claims of uniqueness come from that proof, not from these finite tests.
