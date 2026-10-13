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

The bound quiver and relation convention were checked directly against Liu--Xin Example 6.3. In particular, paths are composed left to right and the source quiver has arrows \(u:S_1\to P_1\), \(v:P_1\to S_1\), \(b:P_1\to P_3\), and \(a:P_3\to P_1\). Thus \(vu\) and \(ba\) are both cycles at \(P_1\).

For the three-edge Brauer path, the type-I relation at the central edge is exactly \(vu-(ba)^m\), and the only cross-cycle type-III relations are \(ub\) and \(av\). The standard minimality criterion confirms that no endpoint type-II relation must be added to the minimal generating set. Direct reductions also verify those consequences: \((uv)u=u(vu)=u(ba)^m=0\) and \((ab)^m a=a(ba)^m=avu=0\), with the analogous central cycle-ending relations obtained from \(ub=av=0\).

The additional source relation \(uv=0\) therefore gives the quotient map \(C_m\twoheadrightarrow B_m\). In \(C_m\), the nonzero path \(uv\) is annihilated on both sides by the arrow ideal, so its span is a one-dimensional socle ideal. The source basis for \(B_m\), together with \(uv\), gives the dimension check \(\dim_k C_m=4m+6\).

The all-parameter representation-finiteness conclusion then uses only two standard facts: a Brauer tree algebra has finite representation type, and any quotient of a representation-finite finite-dimensional algebra is representation-finite. No computational experiment is used to extend a finite check to arbitrary \(m\).

Limits: the proof concerns exactly the Example 6.3 family and does not establish a Brauer-tree cover for arbitrary endomorphism algebras outside the G-condition.
