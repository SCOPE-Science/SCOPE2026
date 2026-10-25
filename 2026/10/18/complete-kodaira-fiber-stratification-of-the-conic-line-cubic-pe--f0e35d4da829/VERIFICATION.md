---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The explicit nine base points are distinct and transverse when a!=0,1 and a^2-a+1!=0, so the blow-up gives a relatively minimal rational elliptic surface with section and Euler number 12. On y=1, the plane cubic is P(u)-v^2 L(u), birational to quartic double cover w^2=P(u)L(u). Independent exact SymPy calculations verified Res_u(P,L)=t(a-1)(a+t)(t+1), the full discriminant factorization -t^2(a-1)^2(t+a)^2(t+1)^2 D_a(t), Disc_t D=512(a-1)^4(a^2-a+1)(71a^2-196a+71)^3 and special D(0),D(-1),D(-a) factorizations. The four reducible members have line/conic contacts yielding generic I2, tangent III or triangular I3; a triple root of P at the two roots of the 71a^2-196a+71 factor produces an irreducible ordinary cusp II, while other distinct D roots are nodal I1. Distinct excluded, tangent, reducible and cusp parameter loci and Euler sum 12 rule out missing fibers. Thus the four asserted baskets are valid on the prescribed nine-simple-basepoint locus, not merely a sample of t-values.

## originality

PASS

The same pencil appears in Suluyer’s 2024 thesis and 2024 arXiv preprint as a four conic-line member pencil, and in the 2026 journal article. Comparing actual cubic generators and a-parameter normalization is necessary; merely comparing title or parameter symbols would be insufficient. The present theorem classifies all Kodaira fibers of the blow-up, not just the number of line-conic members. Persson and Miranda catalog possible elliptic surface fiber baskets abstractly, but a general list of possible Kodaira types does not identify their parameter values in Suluyer’s explicit pencil. Suluyer’s general theorem about the maximal number of conic-line members does not determine the remaining irreducible fibers or the cusp collision. Knowing four line-conic cubic members gives four I2 fibers generically, but does not imply that the remaining quartic discriminant has distinct roots or an A2 cusp exactly at 71a^2-196a+71=0. The extra discriminant, resultant and local-type computation is essential.

## value

PASS

For a natural published family of rational elliptic surfaces the exact singular-fiber geography is a standard structural invariant. The proof distinguishes tangencies (III), split triangles (I3) and coalesced cuspidal irreducibles (II), gives complete exceptional a-loci and accounts for all 12 Euler contributions. This is more informative than counting conic-line cubic members and directly useful for further elliptic fibration studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
