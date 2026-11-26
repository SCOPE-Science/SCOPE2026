---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Weierstrass formula cancels to h(Q/P), with h(z)=1728(1-27z²). The quadratic pencil Q-zP has discriminant disc(P)z²-2p(P,Q)z+disc(Q), also when a repeated root is at infinity in the t-line. The inner degree-two map has two distinct critical values, both finite and nonzero by simplicity of the zero and pole divisors. Their images under h coincide exactly when the linear coefficient is zero. Over C(z), the two square classes represented by Δ(z), Δ(-z) differ when their branch sets differ; in that case the Galois closure has degree eight and embeds in (hence fills) the degree-four block stabilizer D4. On the polar locus Δ is even, and z↦-z lifts fixing sqrt(Δ); together with the quadratic deck involution this gives V4. Ramification of the two successive maps gives two (2,2) and two (2,1,1) partitions in the first case and three (2,2) in the second. The examples satisfy the root hypotheses: for Q=t²+t+2 the discriminants of P±3√3 Q are -193∓36√3; the even example factors as P±3√3 Q with both constant and leading coefficients nonzero. Coprimality gives no overlap between these factors. The polarization scales by the square of the determinant under base coordinate changes. This is a proof for the stated open locus and for j-cover monodromy only. The frozen checker was inspected, not executed; its scope is algebraic consistency, not the function-field argument.

## originality

PASS

The normal form and quadratic-cover theory are prior. The supported distinct contribution is the intrinsic equation for the jump within this open elliptic-surface family, including the exact j-branch partitions and realization of both strata. No equivalent coverage was found in the inspected sources.

## value

PASS

The jump for a natural moduli family distinguishes non-Galois covers from Galois ones and identifies all ramification types on the given open locus. The coordinate-invariant equation and proven proper nonempty locus give a usable parameter test; the value is not the familiar observation that a composition of two quadratic maps is imprimitive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
