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

# Verification

Run `python3 check_bistar.py` with Python 3.8 or later. The checker independently enumerates all induced-component-bounded simplicial faces for each \(1\le a,b\le3\) and \(2\le r\le a+b+2\). It assembles full mod-two augmented simplicial boundaries and verifies that the sole nonzero reduced Betti number is \(\binom{a+b-1}{r-2}\), or zero above the contractible threshold. For every within-block leaf permutation and every balanced center/branch swap, it computes the signed fixed-face Lefschetz sum and independently computes the exterior-power character from permutation cycles. The two agree in all 45 parameter configurations.

Successful execution prints `DOUBLE_STAR_HIGHER_INDEPENDENCE_CHECKS_PASSED 45 cases; homology and all branch automorphisms`.

Finite exhaustive experiments check only the displayed parameters and primarily mod-two homology; they do not prove arbitrary-parameter integral torsion-freeness or wedge homotopy. Those follow from the explicit integral augmented-chain and two-cone proof in `RESULT.md`. The quotient assertions are rational only. No independent audit has been performed.
