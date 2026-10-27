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

Run `python3 proof_checker.py` with SymPy. It uses polynomial ideals over \(\mathbf F_2\), a four-chart Gröbner criterion, the complete 16-bit coefficient space, and five explicit generators of the order-72 group. It asserts 84 smooth point-free equations, orbits 24/24/36, and the three extension point-count vectors.

Independently compile `cc -O2 independent_check.c -o independent_check` and run `./independent_check > masks.txt`. This standalone finite-field implementation determines which candidates have no geometric singular point over \(\mathbf F_{2^d}\) for \(1\le d\le6\). Its output `masks.txt` must exactly equal `smooth_masks.txt`, containing 84 sorted masks. The C search alone cannot prove geometric smoothness over all extensions; the Gröbner computation supplies the proof. The singular candidates all receive a singular-point witness within the six checked degrees.

Boundary: The result is about smooth curves on a split quadric, not every genus-four curve over \(\mathbf F_2\). Point counts over only four extensions distinguish these examples but do not establish full zeta functions. The scientific review is self-review only; no independent scientific audit was performed.
