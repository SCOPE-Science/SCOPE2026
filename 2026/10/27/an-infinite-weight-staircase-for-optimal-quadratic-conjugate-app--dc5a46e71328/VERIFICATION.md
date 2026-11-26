---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With probability-normalized measure the Beta integral gives m_j=Γ(j+1)Γ(α+2)/Γ(j+α+2). Projection of the normalized j-th input monomial onto holomorphic modes is zero for j<2 and has squared norm m_j/m_(j−2) otherwise. Distinct residuals have distinct angular frequencies, hence the squared norm on every f is the weighted sum of the squared diagonal values; this extends from the dense polynomials by boundedness. With p=α+1 and w_j=(j+1)(j+2)/[(j+p+1)(j+p+2)], v_0=w_0, v_1=w_1 and v_j=w_j−w_(j−2) for j≥2. The adjacent difference for w is 2p(j+2)/[(j+p+1)(j+p+2)(j+p+3)], valid also at j=−1 with w_(−1)=0. Taking the difference of those differences yields the stated positive-factor multiple of Q_n(α)=α²+(1−n)α−2n²−5n, while v_1−v_0 is positive. The denominators are positive, Q_n(−1)<0, Q_n(2n)=−3n and Q_n(2n+1)=2. Thus the sole root above −1 lies strictly between the indicated integer endpoints and those intervals order the roots without ambiguity. The mode sequence increases then decreases except for the one adjacent tie; equality requires the coefficient support to lie precisely in the maximizing eigenspace. The bounds on the thresholds yield n_α/α→1/2 for either maximizer at a tie. Substitution into the exact V_n yields αV_n→4t/(1+t)^3 at t=1/2, or 16/27. The supplied script and its recorded output were inspected, not executed; its finite checks include floating-point projection and asymptotic samples, so they are not proofs of the unbounded claims.

## originality

PASS

The distinct claim is the finite-weight mode classification, exact transitions, and complete equality spaces for the quadratic conjugate symbol. The radial monomial diagonal and the leading high-weight consequences are not credited as separate advances. The closest earlier general-power result gives the exact diagonal, and its high-weight argument extends at once to m=2, but it does not order all finite-weight modes. The 1988 source remains an explicit access risk, not evidence for or against coverage.

## value

PASS

A sharp best-approximation norm and its complete equality space are natural operator invariants. Here knowing an exact moment diagonal or asymptotic scale does not tell which input mode to use for a given weight. The global sign test supplies exact transition weights, all two-mode ties, and shows that no fixed finite collection of modes supplies an extremizer for all weights. This is a complete and usable classification of the motivated quadratic case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
