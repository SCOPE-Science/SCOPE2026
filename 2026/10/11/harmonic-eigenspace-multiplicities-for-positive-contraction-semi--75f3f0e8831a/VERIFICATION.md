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

The theorem and its example have **analytic verification**; no computation or empirical extrapolation is used as an infinite-dimensional proof.

The following proof obligations were checked against the cited primary full texts and reconstructed: (1) The hypotheses on \(E\) and \(T_\tau\) exactly match the fixed-space theorem [1, Theorem 3.1], which gives \(F=\operatorname{Fix}(T_\tau)\) the inherited Banach lattice structure and Dedekind completeness. (2) For every \(0\leq s\leq\tau\), commutativity gives invariance of \(F\), while \(T_sT_{\tau-s}=T_\tau\) gives inverse positive restrictions. These are lattice automorphisms, irrespective of whether \(F\) is a sublattice of \(E\). (3) The forward generator-eigenvector implication follows from the semigroup eigenfunction identity. The reverse follows because \(ma\bmod\tau\) is dense when \(a/\tau\) is irrational and the periodic orbit is strongly continuous; the generator derivative then exists with the required eigenvalue. (4) The lattice-homomorphism estimate [2, Proposition 3.1(b)] is valid on order-complete \(F\), with the normalized-powers independence proof in [2, Lemma A.4]. These steps establish both inequalities without assumptions on isolated spectrum or eigenspace finiteness.

For the example, functions \(e^{in\theta}\), \(n\in\mathbb Z\), are the only characters of the circle translations; each associated Fourier mode in one \(L_1(\mathbb T)\) summand has one complex dimension. The first translation speed has generator eigenvalues \(in\), the second \(2in\), yielding dimensions \(1\) at \(i\) and \(2\) at \(2i\). The \(L_1\) direct sum is monotonically complete and has the Fatou property.

Not claimed: verification of all possible equivalent historical formulations; comparison of different infinite cardinalities; multiplicities beyond eigenspaces; generalization to approximate spectrum or arbitrary noncontractive semigroups.

Scientific references: [1] arXiv:2108.05174v1 §§2–3; [2] arXiv:1503.02430v2 §3 and Appendix A.
