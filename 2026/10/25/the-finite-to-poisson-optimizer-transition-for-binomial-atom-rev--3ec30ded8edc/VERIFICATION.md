---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Binomial atom ratio is binom(n,r)(p/(1-p))^r, strictly increasing in p, so equality-boundary mean F_r(n)=n/(1+binom(n,r)^(1/r)) and strict reversal needs larger mean. Extend B_r(x)=(x(x-1)...(x-r+1)/r!)^(1/r) to x>=r; B_r is strictly concave for r>=2 by strict variance inequality on reciprocals 1/(x-j). Q_r=x B_r'-B_r strictly decreases, F_r'=(1-Q_r)/(1+B_r)^2. At x=r, Q=H_r-1; at infinity Q→(r-1)/(2(r!)^(1/r)). Exact integer factorial signs cross between r=10 and r=11; induction preserves the r>=11 sign, making F decreasing to its Poisson infimum without finite attainment. r<=4 finite n=r; 5<=r<=10 strictly unimodal and certified adjacent-integer comparisons yield n=7,10,15,25,51,294. Independent Python arbitrary-precision integer-root interval certificates checked each neighboring optimum and the factorial sign transition, avoiding float assumptions. Strict versus tied probability boundary handled correctly. Finite certificates plus global concavity establish the classification, not a sweep over n.

## originality

PASS

Kleiner studies heterogeneous Poisson–binomial endpoint point-mass thresholds and gives a fixed-count binomial starting identity; the general heterogeneous threshold can exploit deterministic shifts that homogeneous (n,p) excludes. The inaccessible complete Kleiner paper could conceivably contain stronger same-family optimization, but the accessible abstract and compared quoted statement do not establish it. Gnedin studies cross-modality/modes of extended binomial sums, not this joint mean minimizer and n transition. No same Resultary result was located. Assessment is best-of-knowledge with explicit access risk.

## value

PASS

The sharp switch between uniquely optimal finite binomial trial count and a Poisson-only limiting infimum is a natural exact extremal property of iid Bernoulli point probabilities. The six nontrivial finite optimizers form a mathematically motivated complete cutoff, not an arbitrary list of small r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
