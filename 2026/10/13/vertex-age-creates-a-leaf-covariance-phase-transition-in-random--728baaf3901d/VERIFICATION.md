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

In the uniform random recursive tree, leaf probability P(Y_i=1)=(i−1)/(n−1) follows telescoping independent attachments. For 2≤v<j, event P_j=v necessarily destroys leaf indicator Y_v with covariance −(v−1)/[(j−1)(n−1)], but protects all earlier i≠v from being chosen, contributing (i−1)/[(n−1)(j−1)(j−2)]; summing yields exact local Cov(1{P_j=v},L_n)=(j−2v)/(2(n−1)(j−2)). Summing j gives [(n−v)/2−(v−1)(H_{n−2}−H_{v−2})]/(n−1). The unscaled numerator second finite difference equals 1/v>0 and has F_n(2)>0 for n≥7, F_n(n−1)=−1/2, F_n(n)=0; strict discrete convexity supplies one crossing. For v/n→x, harmonic asymptotics give c(x)=(1−x)/2+x log x, unique nontrivial root ρ≈0.284668137; τ_n/n→ρ. Independent enumeration of every parent sequence through n=8 checked all pair covariances, aggregates and E[L_n]. Finite enumeration corroborates but all-n proof is independent.

## originality

PASS

Best-of-knowledge PASS for birth-labeled nonroot local covariance law and 28.4668% age sign transition, after explicitly inspecting published Resultary root-only theorem and distinguishing its special root statistic.

## value

PASS

A natural local-to-global covariance reveals a sharp birth-age phase transition in a canonical random tree model, quantitatively locating a single switch at about 28.47% of the horizon. The precise local law j=2v and aggregate Lambert-W threshold are nontrivial structural statistics potentially useful for recursive-tree correlation theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
