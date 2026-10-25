---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The coordinate map interval indicator v_ij=sum_{k=i}^j e_k is a unimodular map onto type A positive roots e_i-e_{j+1}. The h=x_1+x_m value is 2 at the apex u=v_1m, 1 on proper prefix/suffix contact vertices, 0 on strict interior intervals. The identity u+v_ij=v_1j+v_i,m replaces all paired apex/interior masses on both sides of h=1, proving exact dissection P_m^- and conv(u,F_m). Since proper complementary prefix/suffix pairs sum to u, F_m is a centrally symmetric crosspolytope; the lattice chart (x_1,...,x_(m-1),h) is unimodular and F_m has chart generator determinant ±1/2. The height in h is exactly one, giving m! volume loss=2^(m-2), including m=2 with a lower-dimensional P_m^-. An independent SciPy hull calculation for m=2,...,7 returned normalized losses 1,2,4,8,16,32 exactly; the symbolic dissection, not finite hulls, proves all m.

## originality

PASS

Known positive-root polytopes, general directed-edge face theory, and full-object Catalan volume are acknowledged, while the isolated highest-root deletion dissection and sharp 2^(m-2) loss are not supplied by the examined result statements. A related published SCOPE one-skeleton theorem does not determine the pyramid volume.

## value

PASS

The single highest-root deletion is a distinguished natural combinatorial operation; its crosspolytopal vertex cap and exact lattice volume loss illuminate type-A root-polytope geometry rather than a renamed routine determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
