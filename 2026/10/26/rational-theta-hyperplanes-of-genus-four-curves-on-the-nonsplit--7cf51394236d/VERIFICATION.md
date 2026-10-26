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

The attached `data/qminus_genus4_results.json` lists all 254 smooth orbit representatives, each orbit size, rational theta-plane mask and rational-point count; it also includes the sixteen cubic basis monomials, all fifteen rational hyperplane descriptions and three-bit linear contact syndromes. Run the following commands from the package root:

```sh
python code/qminus_genus4.py
python code/qminus_secondary.py data/qminus_genus4_results.json
```

The complete generator exhaustively enumerates 65,535 nonzero coefficients as 683 orbits under an explicitly constructed order-120 orthogonal group, applies exact Gröbner ideals over the ground field on every affine chart for smoothness, and evaluates all fifteen rational theta-hyperplane criteria for the 254 surviving representatives. The printed exact distribution is `[(0,5680),(1,13580),(2,7020),(3,320),(4,460)]` (equation-weighted, not orbit-count weighted).

The secondary checker independently evaluates the two Jacobian gradients at every rational point of the quadric over extensions of degrees one through four, on all 254 accepted orbit representatives, totaling 1,016 combinations. It then reconstructs both the main weighted distribution and the two-type incidence table from the stored representatives. A finite extension search alone cannot rule out singularities over higher extensions, so the primary exact characteristic-two Gröbner calculation is essential.

Actual command output is supplied in `data/replay_primary.txt` and `data/replay_secondary.txt`. The program's algebraic-closure smoothness and theta criteria follow from the Jacobian criterion, elimination by Gröbner bases, and elementary square-factor tests in characteristic two; no external infinite theorem prover or independent audit is claimed.
