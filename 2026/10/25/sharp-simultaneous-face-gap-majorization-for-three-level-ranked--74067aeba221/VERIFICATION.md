---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For P_{a,b}=A_a ⊕ {q} ⊕ A_b, a,b>=1, the order polytope decomposes as a free join of cubes; its nonempty face polynomial is A+B+tAB with A=(2+t)^a,B=(2+t)^b. The chain polytope is a pyramid over the origin-glued subdirect sum of cubes; counting origin-containing and avoiding faces gives F_C=1+(1+t)[A+B-1+(U-1)(V-1)+t(A-U)(B-V)], U=(1+t)^a,V=(1+t)^b. Algebraically D=F_C-F_O=G_aG_b with G_m=1-(1+t)^{m+1}+t(2+t)^m. For m>=2, G_m=t(1+t)h_{m-2}(1,1+t,2+t). Jacobi–Trudi gives D_{a+1,b-1}-D_{a,b}=t^2(1+t)^2 s_{(b-3,a-1)}(1,1+t,2+t) for 2<=a<=b-2; positive tableau terms force every coefficient degrees 2..a+b strictly positive. If a=1 G_1=0, and G_2G_{b-1} is positive in same degrees. Hence for fixed N=a+b>=4 the balanced split uniquely maximizes every intermediate face gap, extreme split minimizes zero; endpoint coefficients computed from first and top G_m terms. Independent integer algebra verified 121 (a,b) factorization identities plus balancing cases; universal claim follows Schur-positive identity, not enumeration.

## originality

PASS

Qualified PASS for simultaneous strict coefficientwise majorization when varying the two outer rank sizes at a fixed total dimension, and an explicit Schur-positivity certificate. Prior general chain-vs-order f-vector inequalities and subdirect-sum face-count formulas are credited; they establish gaps for a fixed poset and yield the factorization ingredient. They do not in the inspected primary statements assert strict all-face improvement under cross-poset balancing or unique balanced optimizer, although an older formula combined with standard Schur positivity may implicitly imply it.

## value

PASS

The Hibi–Li obstruction starts in this minimal three-level complete ranked poset family. Rather than only showing nonnegativity of chain–order face gaps, the result simultaneously ranks every intermediate face dimension with a common exact optimizer. The Schur-positive all-coefficient certificate explains the order rather than merely listing cases; this is a motivated structural extremal lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
