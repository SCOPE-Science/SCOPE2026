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
# Verification and limits

The analytic verification covers the entire integer family \(r\geq2\), \(m\geq1\) and all \(t\geq0\). It uses the four orthogonal spectral subspaces of the Laplacian; the exact evolved hub-minus-leaf signed mass; the sign inequality \(rz-(r-1)-z^r\leq0\) on \(0\leq z\leq1\); a cost-achieving transport plan and matching 1-Lipschitz potential; and global reduction to graph edges. Differentiation establishes the sharp phase threshold and unique maximum.

`CHECK.py` is a standalone supplementary numerical comparison requiring Python, NumPy and SciPy. Executing `python CHECK.py` on the packaged file contents produced the following completed assertions: 270 edge/time transport linear-program comparisons, 1,380 global Dirac-pair comparisons, 144 arbitrary probability-pair checks and 72 maximizing-time classifications. Re-running these finite computations does not establish the infinite-family theorem; the analytical proof supplies the universal quantifiers.

Results for heterogeneous cliques, nonunit conductances, degree-normalized walks, infinite graphs or \(W_p\) with \(p\ne1\) are not proved. Older historical priority under alternative terminology remains an uncertainty. Independent proof and priority assessment have not been performed.
