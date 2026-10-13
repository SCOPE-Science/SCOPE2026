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

The primary geometric inputs are Zhao's quotient-stack description and standard action for a general smooth complete intersection of two quadrics.  The orbifold-cohomology input is the global-quotient fixed-locus and age formalism of Fantechi–Göttsche.

The exact replay checks the following finite consequences: \(|A[2]|=16\), \(|G|=32\), there are \(16\) elements of the form \((T,-1)\), each has \(16\) fixed points forming one \(G\)-orbit, the sector stabilizer has order \(2\), and the derivative is \(-I\), hence age \(1\).  It then applies the even-total-degree invariant Hodge diamond of an abelian surface and verifies \(h^{1,1}_{\mathrm{CR}}=20\), orbifold Betti numbers \((1,22,1)\), and orbifold Euler characteristic \(24\).

Run `python3 verify_orbifold_hodge.py`.  The recorded `verification_output.txt` terminates with `VERIFY_OK`.

Limits: the replay checks arithmetic and finite fixed-sector bookkeeping, not the cited geometric theorems.  The result is restricted to the general smooth fiber over \(\mathbf C\) and does not determine the Chen–Ruan product.
