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

For n≥2 nondegenerate observations, τ=m=min x_i is in allowed support, k≥1 data points attain m, r=n−k have positive residuals y_i. Direct product of the quoted model density yields profile λhat=n/S(σ) where S=Σ(sqrt(1+y_i/σ)−1)~Cσ^(−1/2), C=Σ_{y_i>0}sqrt(y_i)>0. Profile ℓ=nlog(n/S)−n−nlog(2σ)−(1/2)Σlog(1+y_i/σ) gives coefficient n/2−n+r/2=−k/2 on logσ, hence ℓ=−(k/2)logσ+O(1)→+∞ and λhat~n√σ/C→0. Therefore no finite unconstrained three-parameter maximum exists. Independent direct-vs-profile formula reconstruction and high-precision log-step checks for unique/tied minima corroborate, while proof is asymptotic for all nondegenerate samples. All-equal samples explicitly excluded.

## originality

PASS

Best-of-knowledge PASS with material full-text-access limitation: exact 2026 source was retrieved at publisher metadata and abstract, but publisher full PDF inaccessible and institutional authorized attempt returned vpn_disconnected (not bypassed). The audited package supplies a claimed verbatim model density and positive-scale profile, whose mathematical consequence is proved here. General nonregular/support-dependent likelihood literature does not by itself state this particular MERD −(k/2)logσ blowup. The possibility that the unavailable primary body already mentions the ridge is explicitly retained as risk; no whole-paper NOT_COVERING assertion.

## value

PASS

Existence of a finite global MLE is foundational for the cited model’s proposed three-parameter estimation procedure. A universal boundary path with divergence coefficient determined by tied minimum multiplicity invalidates unqualified unconstrained numerical maximization and is a substantive nonregular-likelihood phenomenon, not merely a routine parameter constraint check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
