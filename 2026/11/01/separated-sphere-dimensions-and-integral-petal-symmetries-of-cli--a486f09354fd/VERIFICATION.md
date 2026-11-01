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

# Verification protocol and limits

The theorem is proved for all integers \(m\ge3\), \(t\ge3\), and clique sizes \(s_i\ge t\). Verify the mathematical steps directly: private-block characterization; equality \(X=A\cup(c*B)\); exact integral skeleton homology as exterior powers of the augmentation lattice; connectivity and dimension of the two joins; nullhomotopy of \(B\to A\); cofiber splitting; and Koszul signs under petal swaps.

The script `check_clique_bouquet.py` uses no third-party modules. Execute `python3 check_clique_bouquet.py`. A verified run reports eight finite mod-two reduced-homology computations and 360 integer signed-Lefschetz character checks. The tests include several three-petal and unequal-petal examples. The two-petal boundary checks do not change the scope of the theorem.

Finite mod-two ranks do not prove torsion-freeness, and sample character agreement does not prove an infinite equivariant formula. The integral torsion-free and homotopy claims rest on the explicit mapping-cone and skeleton arguments, not on the experiment. No independent validation or external certification has occurred.
