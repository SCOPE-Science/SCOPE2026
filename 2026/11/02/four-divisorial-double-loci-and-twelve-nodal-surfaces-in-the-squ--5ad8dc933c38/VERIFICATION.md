---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The full projective product P3_[x:y:z:w]×P2_[s:u:v] over C is used; with A=xw, B=yz, D=A-B the claimed quartic is precisely F=A²(u-v)²−2AB(s(u+v)+u²+v²)+B²(s+u+v)². Its quadratic matrix in (s,u,v) has determinant −4A²B²(A−B)², so the smooth-conic case ABD!=0 is nonsingular. On A=0, B=0, D=0, the restricted first derivatives and chain rule identify exactly four 3D coordinate-line×P2 loci and twelve additional irreducible 2D surfaces; at A=B=0 all first derivatives vanish. Each surface has points off the others, proving irreducible components rather than just candidates. Transverse Hessians of the five surface symmetry types have rank three on a dense open, giving A1 ordinary quadratic nodes, while the discriminant of the normal quadratic in (A,B) is 16uv(s+u)(s+v) generically nonzero on the 3D loci, giving normal crossings. As the hypersurface is irreducible and has codimension-one singular divisors, R1 fails and it is nonnormal (no claim about Jacobian nilpotents or intersection analytic types). Independent symbolic algebra confirms polynomial identity, Q determinant and normal discriminant; these computations support but do not replace the algebraic saturation-by-cases proof.

## originality

PASS

Best-of-knowledge: compare the exact theorem and quantifiers with inspected primary results and relevant published summaries, rather than matching titles/numbers. Known ingredients are credited, and any plausible inaccessible or broader literature remains a qualified priority risk; no definitive independence or priority certification is claimed.

## value

PASS

The square-support logarithmic A-discriminant is a natural low-dimensional test example of a new discriminant construction. Its entire reduced singular support, generic transverse types and nonnormality are substantive geometric data required for normalization/intersection calculations, not a routine restatement of the known defining polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
