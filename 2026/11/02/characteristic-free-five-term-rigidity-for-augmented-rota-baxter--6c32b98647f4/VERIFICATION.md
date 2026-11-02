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

The symbolic proof uses linear independence of the three endomorphisms of the square-zero test algebra, ordinary tensor associativity, a two-point dual-number coefficient restriction, and finite pointwise-function Rota–Baxter algebras. The pivotal all-characteristic calculation is \(\mathscr P(X)\mathscr P(Y)=\lambda^2(\delta_2+\delta_3)\otimes\delta_3\) with \(\mathscr P(\mathscr P(X)Y+X\mathscr P(Y)+\lambda XY)=0\), for nonzero weight. This is independent of the characteristic.

Run `python3 verify.py`. The checker reconstructs the operators from matrices, confirms their defining identities on each pair of coordinate idempotents over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_5\), and confirms the four-point obstruction. The observed exact output is `VERIFY_OK`. It does not computationally prove the full all-field theorem. The positive constructions and the characteristic-zero associativity classification were checked directly in the cited primary paper; no independent external audit or formal proof certification was performed.
