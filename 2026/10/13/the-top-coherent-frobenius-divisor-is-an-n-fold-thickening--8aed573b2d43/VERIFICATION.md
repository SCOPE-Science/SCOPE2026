---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof in `RESULT.md` is scheme-theoretic and uses no experiment. For the unrestricted base, Stacks Project Lemma 36.30.1 makes \(Rf_*\mathcal O_{\mathcal X}\) perfect with derived base change. A local finite free complex can be simplified by canceling unit entries until all differentials vanish on the residue field. The geometric fibre cohomology then shows that its remaining terms occur only in even degrees, and those differentials vanish over the base. This gives the line bundles and underived base change; constant geometric fibre ranks alone over a nonreduced base would not suffice.

Cup power on the line bundles is an isomorphism by the fibre algebra in Zou's Definition 4.10. Naturality for relative Frobenius gives \(h_i\circ F_S^*c_i=c_i\circ h_1^{\otimes i}\) before restriction to any fibre. Consequently the ideal of the zero scheme in degree \(2i\) is locally \((a^i)\) when that in degree two is \((a)\). Over an integral base, a nonempty Frobenius-split locus guarantees that \(a\) is regular in every nonempty trivializing open.

For the support statement use the geometric-fibre criterion from Zou's Lemma 6.2 and the fibrewise dichotomy of Corollary 4.16 used in Theorem 6.7. If every geometric fibre fails to split, all section coefficients vanish modulo the nilradical; they are zero as sections when the base is reduced, but pointwise vanishing is not a zero-section argument on an arbitrary base. The multiplicity computation does not assert reducedness of the degree-two divisor.
