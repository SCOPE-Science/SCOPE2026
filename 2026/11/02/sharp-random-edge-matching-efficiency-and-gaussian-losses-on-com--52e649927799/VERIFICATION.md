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

# Verification of the displayed theorem

Execute `python3 check.py` in the package directory. It needs only the Python standard library. The checker constructs the exact terminal distribution recursively, independently generates full labeled-edge orderings of small complete split graphs, compares distributions as exact rational numbers, checks moment recursions, and tests the sharp efficiency bound numerically. It also runs independently seeded Monte Carlo diagnostics for the Gaussian limit's predicted mean and variance.

The rigorous infinite-size checks are analytic: the rate-normalized chain has generator jump rates \(xy\) and \(x(x-1)/2\) before scaling; the normalized fluid drift is \((-x^2-xy,-xy)\); \(x/y-\log(y/\beta)\) is conserved by that drift. The two jump vectors produce the displayed quadratic-variation integrand, with the remaining variation after the clique population falls below \(\varepsilon n\) bounded by \(O(\varepsilon^2)\) after multiplying by \(n\). The resulting variance equals \(\beta e^{-r}[4-e^{-r}(r+2)^2]\), and the deterministic ratio is strictly decreasing for \(r<1\) and increasing for \(r>1\).

Finite enumeration and simulation are not infinite proofs. The source comparison is not an exhaustive history of the literature, and independent validation is not claimed.
