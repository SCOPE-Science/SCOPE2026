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

With prescribed column sup norms, the objective is convex on the box of matrix entries and some box vertex maximizes it. Each vertex has the prescribed norms, including zero weights. A projective sign class with a represented row attains T²; an absent class differs from any row and its negative, so both agreement and disagreement have weight at least b, giving a bound (T−2b)². There are at most m represented classes. Flipping one coordinate of minimum weight pairs the classes without fixed points for n≥2; deleting one from each of r≤k/2 different pairs realizes the bound in every class. At fixed squared sum and minimum b the objective increases with T, so making the remaining n−1 norms equal is optimal by Cauchy–Schwarz. For d=n−1 the quotient then is (d²+dAq+q²)/(d+q²) with q∈[0,1]. The top eigenvector of the displayed symmetric matrix is feasible: for d>1 its q equals dA/[2(λ₊−1)]≤1; squaring if needed reduces the inequality to d(d−1)A(2−A)≥0. For d=1, q=1 suffices when A>0 and all ratios work at A=0. This gives both endpoints, including n=2,m=1 and m=k. The five-row witness has three absent classes paired by column 3 and q=√19−4; substitution gives 2+√19/4.

## originality

PASS

The saturated value and its all-sign row construction, the n=m=3 specialization including its fixed-length calculation, and the general sign-averaging operator are already covered. The distinct result is the sharp weighted two-level coverage formula throughout the near-saturation interval and the resulting exact unrestricted constants beyond those cases. The inspected general sign-average representation and adjacent modified/geometric objectives do not mechanically imply it.

## value

PASS

The result supplies exact values of a standard Banach-space geometric invariant where the dimension alone no longer guarantees saturation. More strongly it determines worst-case behavior at arbitrary prescribed lengths by a sharp covering construction and identifies a genuinely intermediate value at n=4,m=5. The weighted construction explains why optimizing at unequal lengths can matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
