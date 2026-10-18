---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Under fully specified continuous F0 and n≥2, applying the exact iid centered-Hilbert quadratic-form covariance formula to W_n²=⟨S,I S⟩ and U_n²=⟨S,P S⟩ yields Cov=(n−1)/(180n), Var W=(4n−3)/(180n), Var U=(n−1)/(360n), Corr=sqrt(2(n−1)/(4n−3)). Independently integrated Brownian-bridge kernel C(s,t)=min(s,t)−st to obtain tr Σ²=1/90, ||Σe||²=1/120, ⟨e,Σe⟩=1/12; so tr ΣPΣ=1/360 and tr ΣPΣP=1/720. For each one-observation bridge Z_y, ||Z_y||²=(y−1/2)²+1/12 and ⟨Z_y,PZ_y⟩=1/12 constant; one-sample joint covariance zero. Pairings give all n exactly; n=2 and the n→∞ correlation limit follow. This proof, not finite experiment or prior checker log, controls every n.

## originality

PASS

Best-of-knowledge PASS for an explicit exact joint finite-n second moment linking two natural goodness-of-fit statistics. Closest original Pearson–Stephens 1962 article was newly retrieved through authorized academic access and all six pages materially read: sections 2–4 deal with marginal W and U behavior, section 5 relates asymptotic marginal cumulants, not finite-n joint covariance. Hwang–Kuriki 2024 handles separate limiting eigenlaws; neither source supplies the cross-statistic covariance formula.

## value

PASS

Joint finite-sample dependence, nonzero asymptotic correlation 1/sqrt(2), and monotone n-dependence are natural useful quantitative diagnostics for statistical-test comparison; this is not a renaming of marginal moments. The exact deterministic projected single-observation contribution explains non-obvious simplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
