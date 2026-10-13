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

The proof was reconstructed from the annihilator definition rather than inferred from computational output. The critical symbolic checks are:

1. \(\operatorname{ann}(xy)=\operatorname{ann}(x)+\operatorname{ann}(y)\) in a product of fields, and union equals sum exactly for comparable coordinate annihilator ideals.
2. Every two distinct supports have different open neighborhoods, so the support partition is graph-theoretically canonical.
3. The quotient degree formula is \(2^r+1-2^k-2^{r-k}\), isolating singleton and co-singleton supports at minimum degree for \(r\ge3\).
4. The induced minimum-degree subgraph has automorphism group \(S_r\times C_2\), and all other supports are recovered from their comparability pattern with singleton supports.
5. Complement-type size preservation yields \(A^2=A^r\), forcing the Boolean boundary when \(r\ge3\).
6. The same multiplicity equations handle graph isomorphisms between two different products and force equality of their unordered field-order lists.

The packaged standard-library checker exhaustively verifies quotient automorphisms for \(r=2,3,4\), full automorphism orders for several small field products, exact false-twin classes, and bounded cross-parameter reconstruction. The finite replay is supportive evidence only; the theorem's infinite quantifiers rest on the symbolic proof.

Known limits: finite commutative reduced nonfields only. No claim is made for rings with nilpotents or for infinite rings. Independent audit has not been performed.
