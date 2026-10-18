---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At p_k=q_k/k!, q_k=Aa^k+Bb^k, the exact curvature D_k=(k+1)q_k^2-k q_{k-1}q_{k+1}=q_k^2-kAB(ab)^(k-1)(b-a)^2. Division by AB(ab)^k yields 2+2cosh(eta+kd)-kC with eta=log(B/A), d=log(b/a), C=(b-a)^2/(ab). The strict-failure intervals for k>r=4/C are eta in (-kd-W(k),-kd+W(k)), W=acosh(kC/2-1). W is increasing strictly concave, W(r+1)=d, so their right endpoints decrease, consecutive intervals overlap, and their union is exactly (-infinity,-Kd+W(K)), K=floor(r)+1. This proves the positive-weight sharp w* cutoff and the boundary equalities; strict convexity of H(x)=2+2cosh(eta+xd)-xC proves that failing integer indices form one finite block. Pure Poisson endpoints w=0,1 are separately strictly log-concave. Independently expanded 2,240 exact rational curvature identities and critical examples (1,2,A:B=256:1) zeros k=8,9 and (1,4,A:B=8:1) zero k=2. Finite tests corroborate rather than prove the infinite assertion.

## originality

PASS

Best-of-knowledge PASS for a quantitative one-sided critical mixing weight and global all-index log-concavity shape theorem. Primary tail theorems and dispersion tests do not imply this indexwise criterion. A historical mixtures review and Le Cam material were not fully accessible and remain explicit risks.

## value

PASS

The exact threshold is a motivated global shape property of a natural two-point mixture, exposing discontinuity at w=0, the connected finite violation band and exact equality pairs. Determining a complete phase boundary is a useful natural invariant, not only a numerical check or standard local deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
