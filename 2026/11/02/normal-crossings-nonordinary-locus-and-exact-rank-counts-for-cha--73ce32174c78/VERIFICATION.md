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

For smooth standard Ciani plane quartics over algebraically closed char 3, the partial derivatives imply the exact open U excluding r^2=s^2=t^2=1 and Delta=r^2+s^2+t^2-rst-1=0. From F^2 all Hasse–Witt off-diagonal terms vanish by parity and diagonal entries equal 2(s+rt), 2(t+rs), 2(r+st); Frobenius powers preserve their zero set and give p-rank as number of nonzero entries, a-number=3-rank. Each h_i=0 is an affine graph open in A2; pairwise intersections reduce to axes in U (r^2 !=1 etc), with linearly independent gradients, and all three gradients independent at origin, hence simple normal crossings. For q=3^m, discriminant root counts follow sum_{u in F_q}chi(u²-1)=-1 and exclusion t=±1, giving smooth total (q-2)^3-(q-3)^2. Each Hasse component has q²-6q+10 points; inclusion-exclusion gives N0=1, N1=3(q-3), N2=3(q-3)(q-5), N3=(q-3)(q²-7q+18). Independently enumerated F9 in polynomial field u²=-1: ranks 1,18,72,216 for 0,1,2,3 and total 307. This checks a finite case only; all-extension formulas are proved by character sums, not sampling.

## originality

PASS

Ohashi 2022 studies the exact same Ciani family and already proves smoothness and elliptic-quotient/prime-to-p isogeny, and results on superspecial members. That antecedent is credited; reviewed sections did not yield the coefficient-space SNC triple arrangement and four exact all-extension rank count polynomials. Broader Ciani stratification remains a historical risk; best-of-knowledge PASS.

## value

PASS

The rank-jump divisor in a genus-three Ciani quartic parameter family has a natural normal-crossings geometry with a unique superspecial coefficient point. The full geometric rank stratification and all-extension polynomial number of ordered coefficient equations go beyond the known smoothness criterion and elliptic-quotient isogeny. They give an exact arithmetic-geometric census at a characteristic that is genuinely exceptional for the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
