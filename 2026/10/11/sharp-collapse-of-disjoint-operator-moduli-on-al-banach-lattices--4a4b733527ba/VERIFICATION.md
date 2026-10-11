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

# Verification of the analytic claim

1. **Disjoint-span identity.** For every finite set of coefficients, compare \(\|\sum a_n x_n\|\) with \(\sum|a_n|\), using disjoint lattice moduli and AL positive additivity. Density gives the operator norm identity on the full closed span, over both scalar fields.
2. **Subsequence comparison.** For arbitrary bounded nonnegative image norms, select an infinite subsequence lying below its original \(\liminf\) plus any prescribed positive tolerance. Apply the norm identity to prove \(\Gamma_d\leq\beta\); the reverse bound follows immediately from definitions.
3. **Tail-to-block contradiction.** If no tail restriction is bounded below by \(\beta-\varepsilon\), choose successively normalized finitely supported vectors from later tails whose image norms are strictly below \(\beta-\varepsilon/2\). Their supports do not overlap, so their disjoint sequence contradicts the definition of \(\beta\). Taking the \(\tau_d\) supremum over tail sequences and the \(\kappa_d\) infimum proves \(\beta\leq\kappa_d\).
4. **Restriction and published perturbation lemma.** Equip each disjoint span with the transported coordinate AL order (its disjoint sequences are the same as those inherited from the ambient lattice); reapply the AL argument to identify \(\Delta_d\). Substitute the equality into González–Martinón (2021), Proposition 4.5, once for \(T+S\) and again for \(T=(T+S)-S\). Their Proposition 4.4 identifies the vanishing perturbation modulus with disjoint strict singularity.
5. **Sharpness.** For the identity on any infinite-dimensional AL lattice, every normalized disjoint vector has image norm \(1\), all restricted identity norms are \(1\), and the same is true of \(\Delta_d(I_E)\); the factor \(1\) is attained in the perturbation inequality with \(T=0\).

These are exact analytic verifications; finite numerical tests cannot replace the disjoint-block construction or the infinite-dimensional quantifiers. The result does not settle the comparison question beyond AL lattices, and no independent audit has been performed.
