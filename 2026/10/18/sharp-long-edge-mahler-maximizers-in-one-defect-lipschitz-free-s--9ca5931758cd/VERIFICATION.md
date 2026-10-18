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

# Verification of exact long-edge Mahler formulas

The analytic proof reconstructs the equilateral volume by positive/negative mass orthants, isolates two cross-polytope facets upon deleting one edge, computes their pyramid volumes, and integrates a squared-interval correction over the range distribution of core Lipschitz potentials. The derivative sign is proved by an explicit strict inequality for every integer \(d\ge3\), including the endpoint cases; the exceptional \(d=2\) formula is treated separately. Central-binomial asymptotics give the limiting optimal distance and relative gain.

The provided standalone `verify_single_long_edge.py` uses NumPy and SciPy to find hull triangulations, while reconstructing the exact volumes from rational determinant computations and checking exact Lipschitz inequalities. Execute `OPENBLAS_NUM_THREADS=1 python verify_single_long_edge.py` from the extracted directory. The expected final message is `EXACT_ONE_DEFECT_VOLUME_CHECKS_PASS 16 cases`. The checked instances comprise dimensions \(2,3,4,5\) and edge lengths \(1,5/4,3/2,2\), and confirm both primal and polar formulae separately.

The checker is corroborative, not an exhaustive certificate for every dimension and parameter. The mathematical claims in this record have undergone self-review only; an independent audit has not been performed.
