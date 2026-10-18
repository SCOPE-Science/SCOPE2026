---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The diagonal ℓ² construction uses Λ_n f=〈f,e_n〉 and Γ_n f=n^−1〈f,e_n〉 with T=U=I. The Λ energy equals ||f||² (A=B=1), Γ energy ≤||f||² and Γ is complete since each coefficient is nonzero, but for f=e_N its energy N^−2 tends to 0: not a g-frame. The mixed operator is diag(1/n); ||S−I||=sup_n(1−1/n)=1=A and inverse diag(n) unbounded, exactly refuting the printed equality endpoint without finite approximations. For λ<A, S_Λ≥A I and ||S−S_Λ||≤λ give ||S f||≥(A−λ)||f||; applying the same to adjoints yields dense+closed range and bounded inverse. The original Cauchy–Schwarz argument gives Γ lower bound (A−λ)²/B. There is no hidden endpoint equality.

## originality

PASS

PASS best of knowledge. The original Li–Leng full arXiv preprint Theorem 3.4 explicitly includes 0≤λ≤A and concludes invertibility of the mixed operator and a g-frame bound; its proof derives a lower estimate A−λ and inadvertently treats zero as positive at λ=A. The proposed complete diagonal ℓ² witness shows the actual published endpoint false even for complete Γ; the correct λ<A condition follows from the original two-sided bounded-below argument. No matching earlier erratum or diagonal endpoint witness emerged in targeted actual searches. Other published SCOPE controlled-g-frame counterexamples address different K/g-fusion/weaving hypotheses and are not this theorem.

## value

PASS

An exact counterexample to a named published perturbation theorem that asserts invertibility at a non-strict norm threshold has genuine corrective value: a frame can remain Bessel and complete yet lose all positive lower bound at λ=A. Replacing ≤ with < is the minimal mathematically motivated boundary and recovers a quantitative controlled lower bound. This is not a generic numerical toy; infinite-dimensional compact diagonal spectrum is the obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
