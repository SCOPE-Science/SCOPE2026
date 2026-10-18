---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed the original APIILx CDF and differentiated to get h(x)=θ/(λ+x)·α(e^t−1)/(e^{αt}−1), t=−log(1−v/2). The exact logarithmic derivative is [θK_α(t(x))−1]/(λ+x); K_α=(e^t−1)[α/(1−e^{−αt})−1/(1−e^{−t})]. For α≤1, K≤0; for α>1, both e^t−1 and D_α(t) rise strictly because a/(1−e^{−at}) increases with a and sinh(z)/z with z. Therefore K increases from 0 to B(α)=α/(1−2^{−α})−2 as t increases while t(x) strictly decreases. This proves exact decreasing region θB≤1 (including equality on positive times), otherwise one strict peak and no bathtub/ever-increasing shapes. Scale λ cancels the boundary. Independent symbolic checks at α=1,2,3 confirm derivative identity; infinite claim is analytic.

## originality

PASS

Best-of-knowledge: the exact APIILx three-parameter hazard in Kalt et al. 2026 is credited. The inspected complete original publisher paper describes decreasing or unimodal hazards qualitatively with plots, but does not provide the necessary-and-sufficient parameter criterion, global at-most-one-peak theorem, or root equation. Later-named power-Lomax distributions use distinct generators and do not dominate this phase theorem.

## value

PASS

An exact parameter-level answer to whether a new lifetime family can exhibit decreasing or unimodal failure-rate regimes is a natural model-intrinsic question. The iff boundary, proof of exactly one possible maximum, explicit monotone peak equation, and scale-independence replace ambiguous shape plots with usable mathematical classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
