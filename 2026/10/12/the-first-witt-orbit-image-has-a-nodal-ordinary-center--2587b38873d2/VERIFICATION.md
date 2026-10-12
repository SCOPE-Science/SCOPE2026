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

The proof was replayed symbolically from the published identities for the first orbit image.

1. The localization is \(A_1\otimes k[v,v^{-1},(v-1)^{-1}]\), whose center is the Laurent coefficient ring because the first Weyl algebra has center \(k\) in characteristic \(0\).
2. Intersecting back with \(T_1=A_1\otimes k[v]\) puts every central element in \(k[v]\).
3. The published kernel \(\ker(\Pi_{1,0}|_{B_1})=T_1v(v-1)\) implies \(p(v)\in B_1\cap k[v]\) only if \(p(v)-p(0)\) is divisible by \(v(v-1)\); conversely that divisibility puts the polynomial in \(B_1\).
4. With \(w=v(v-1)\) and \(z=wv\), the relation \(v^2=v+w\) reduces \(k+w k[v]\) to \(k[w]+z k[w]\), and \(z^2-wz-w^3=0\).
5. The tangent cone \(z(z-w)\) has two distinct lines. The finite birational map into \(k[v]\) is the normalization, with exactly \(v=0,1\) over the node.

No finite enumeration, floating-point computation, or external certificate is used. The proof does not extend the claim beyond the stated field assumptions or beyond the first orbit image.
