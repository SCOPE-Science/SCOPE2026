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

# Reproducibility

Run `python3 verify.py` in this folder. Python standard library suffices.

Observed output:

```text
VERIFY_OK profiles=360 total_vertices=5274 sibling_pairs=2184 exact_rational_witnesses
```

The checker traverses every profile of branch counts in \(\{1,2,3\}^m\) for \(2\le m\le5\). It checks the exact rational vector identity \(Az=0\), the nonvanishing of sibling-leaf sum projections witnessed by \(z\), and disjoint second moments for degree-compatible root/hub pairs. All unrestricted claims are established analytically in RESULT.md, not by the finite checker. Numerical spectral diagonalization is not needed.
