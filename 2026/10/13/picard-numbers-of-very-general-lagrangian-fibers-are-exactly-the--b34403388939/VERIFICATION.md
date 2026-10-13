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

The initiating source was checked at Definition 2.2, Corollary 1.3, and Proposition 2.8. Definition 2.2 identifies Hodge-generic weight-one Hodge structures with maximal Mumford--Tate group \(\operatorname{GSp}\). Corollary 1.3 gives a divisor \(d\mid g\) and an isogeny from the very general fiber to \(d\) pairwise non-isogenous Hodge-generic factors of dimension \(g/d\). Proposition 2.8 realizes every pair \((h,d)\) with \(g=hd\) by a primitive-symplectic Lagrangian fibration.

The degree-two calculation was reconstructed directly. For \(V=\bigoplus_iV_i\),
\[
\Lambda^2V=
\bigoplus_i\Lambda^2V_i\oplus\bigoplus_{i<j}V_i\otimes V_j.
\]
Each independent symplectic factor has a one-dimensional invariant space in \(\Lambda^2V_i\), while no cross tensor has invariants. Thus the rational Hodge classes have dimension exactly \(d\). Lefschetz \((1,1)\) identifies this with \(\operatorname{NS}\otimes\mathbf Q\), and an isogeny preserves the resulting rank.

Oguiso's arXiv:0803.1205 was checked because its title is a plausible stronger prior result. Its Theorem 1.1 concerns Picard number of the scheme-theoretic generic fiber over the function field, and the paper explicitly notes that smooth closed fibers can have Picard number at least two. It therefore does not cover the very-general-closed-fiber statement verified here.

No computation or finite enumeration is used to justify an infinite claim. The proof does not address isotrivial fibrations, special fibers, or the unresolved smooth hyper-Kähler attainability of all intermediate factor counts.
