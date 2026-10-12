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

The proof was replayed from the cited full-text statements rather than from a numerical experiment.

For a positive integer \(m\), Proposition 6.12(2) of arXiv:2610.01354v1 gives a finite flat surjective multiplication map on the Néron model. Therefore the kernel is finite flat over the connected valuation spectrum and has constant scheme-theoretic length equal to the generic degree \(m^{2g-t_\eta}\).

At a fiber \(s\), the identity component is semi-abelian of dimension \(g\) and torus rank \(t_s\), so its multiplication kernel has length \(m^{2g-t_s}\). The algebraically closed residue field permits a point in each component. For every \(m\)-torsion component, surjectivity of multiplication on the identity component adjusts such a point to an actual \(m\)-torsion point. Hence the full fiber kernel is the disjoint union, indexed by \(\Phi_s[m]\), of translates of the identity-component kernel. Comparing lengths yields
\[
|\Phi_s[m]|=m^{t_s-t_\eta}.
\]
This length argument remains valid when the residue characteristic divides \(m\); no étaleness or reducedness assumption is used.

Lemma 5.11 of the same source gives divisibility of \(\Phi_s\). The classification of divisible abelian groups then determines the torsion subgroup from the prime-torsion cardinalities as \((\mathbf Q/\mathbf Z)^{t_s-t_\eta}\). A torsion-free divisible summand is not determined.

The closest classical comparison checked is Grothendieck's rank-one ramified direct-limit theorem, as explicitly summarized in Conrad's notes. It concerns a different object: a direct limit of component groups after finite extensions, rather than the actual component group over the arbitrary-rank valuation ring.
