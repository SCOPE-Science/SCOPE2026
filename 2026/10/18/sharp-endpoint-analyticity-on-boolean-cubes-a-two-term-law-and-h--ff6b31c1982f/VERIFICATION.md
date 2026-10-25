---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Unnormalized cube heat kernel is product Bernoulli with p=(1-e^{-2t})/2. Direct differentiation reduces the row absolute sum to e^{-2t} E|Bin(d,p)-dp|/(pq); telescoping yields the stated (d-1)-binomial mass. Stirling shift a={dp} gives B(t,a)=1/12+(6a(1-a)-1)/(12pq). The smooth leading g(t) has unique t*; uniform expansion plus nondegenerate maximum and selectable half-integer dp witnesses give two-term maximum and O(d^-1) localization/phase O(d^-1/2). Independently optimized near t* at d=200,1000,5000: correction tends toward b*=0.29250016, maximizing fractional part ≈0.5; exact kernel expansion vs finite values agrees. Numerical work is not asymptotic proof.

## originality

PASS

Best-of-knowledge PASS. De Moivre exact deviation, classical fixed-p asymptotics and semigroup bounds cover the initial identity but not continuous-time optimized c*sqrt(d)(1+b*/d) and half-shell locking of EVERY maximizing time. Published SCOPE degree-two Walsh projection lattice phase is a different operator and order; no stronger implication located. The full Elezović 2026 paper was not obtained, priority remains a concrete risk, not declared definitively absent.

## value

PASS

The nontrivial phenomenon that continuous-time optimization suppresses fixed-p lattice oscillations and selects half-integer binomial shells is a motivated endpoint semigroup asymptotic. Exact second coefficient and optimizer phase complement established fixed-parameter deviation theory and can inform optimal derivative norm bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
