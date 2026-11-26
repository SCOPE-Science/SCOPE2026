---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Stationarity gives switch probability mu=2ab/(a+b), while two successive switches have joint probability ab. Conditioning at the endpoint of the first switch, the centered conditional probability of a switch h steps later is multiplied by lambda^(h-1) under the two-state transition operator. Thus the lag covariance is (ab-mu^2)lambda^(h-1). Summing gives the stated exact variance gap. For m>=2, f(lambda)=(m-1)-m lambda+lambda^m has f(1)=0 and f'<0 on (-1,1), so even alternating correlations give a positive total at a!=b. At the same mean, any m independent Bernoulli variables have variance at most m mu(1-mu), by the sum-of-squares bound on their success probabilities. When a=b, the switch probability conditional on the full history is always a, which gives iid switches; m=1 is Bernoulli for either regime. An independent rational generating-law transfer checked the closed variance formula, its sign, and the symmetric binomial law in 300 chain/horizon cases, including both signs of lambda (replay: python3 /workspace/branches/recompute_frozen.py). The general proof does not depend on these finite checks.

## originality

PASS

On inspected evidence, the distinct contribution is the asymmetric all-horizon exclusion and its exact positive variance gap. Independence in the symmetric case is established prior work. Occupation counts and separate adjacent-pattern marginals do not give the total switch count law.

## value

PASS

This is a distribution-class boundary for a natural observable used to distinguish switching from occupation. The exact variance obstruction handles all horizons at once, even when correlations alternate, and clarifies why the law can differ from any independent-Bernoulli sum, not merely why the original indicators can be dependent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
