---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On S={x:1^Tx=0}, each Q_a is invertible. Splitting p_a=(pi_a+u_a)/2, using Q_0u_0=-Q_1u_1=z, yields (I+rH)z=-r(pi_1-pi_0) with H=-Q_0^-1-Q_1^-1; detailed balance annihilates each phase equilibrium flux. Hence J_e=-r L_e adj(I+rH)delta/[2 det(I+rH)], giving numerator degree <=dim S−1=n−2. H is invertible because Q0+Q1 irreducible on S. det stays positive for r>0 by uniqueness of the full irreducible switched chain and det(0)=1. Independent exact rational 6x6 stationary solution reproduces J=3r(8r−9)/(2(845r²+2559r+1530)) and root 9/8. All-n proof is resolvent algebra, not finite simulation.

## originality

PASS

The exact n−2 numerator-degree ceiling for a single site-independent switching rate between two arbitrary separately reversible finite CTMC generators and its sharp three-site example is not among the inspected discrete-time ratchet, particular six-state engine, or no-pumping theorems. The matrix determinant/adjugate argument could have an unlocated general network-response antecedent.

## value

PASS

A natural finite-size law bounds how many reversals a two-phase flashing molecular transport model can exhibit as one rate varies, with a sharp triangle witness despite zero current in each frozen equilibrium. This is substantive beyond generic rational dependence or a simple negative test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
