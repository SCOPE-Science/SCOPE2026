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

PASS: Reconstructed the exact source SDE, environmental ODE, effective rates, stochastic logistic Lemma 2.3, and both positivity hypotheses of Theorem 4.10. For r1=3,r2=2,r0=1,d12=1,d21=0,lambda_i=0,a_i=sigma_i=1, ce=1/2,c0=1/4,f=g=m=1,h=2,u_e=1, environmental derivatives vanish and R1=7/4,R2=2; both R_i-sigma_i^2/2>0. With no immigration to patch 1, it is precisely dx1=x1(7/4-x1)dt+x1 dB; its almost-sure time mean is (7/4-1/2)=5/4. The printed theorem requires >=5/2, while its own proof concludes >=5/4. Independent Fraction arithmetic replay established every displayed rational value and direction. Publisher original PDF pp.11-12 (zero-index pages 10-11) visually confirms the two differing displayed bounds; Example 3 permits zero migration. The false part is the quantitative clause, NOT persistence itself.

## originality

PASS

PASS, best-of-knowledge: The exact source-specific false printed lower bound and an admissible decoupled witness are not among the conclusions of broader stochastic logistic/polluted-population theory. The motivating 2020 full PDF demonstrably prints r_i instead of effective R_i in Theorem 4.10, although its proof uses R_i. Publication/erratum and targeted Resultary searches disclosed no earlier paper-specific correction; no absence-of-search novelty theorem is asserted.

## value

PASS

PASS: The disputed published quantitative long-run per-habitat abundance guarantee is the outcome, not an incidental sign check. Pollution and outward migration change that promised guaranteed population from 5/2 to the true 5/4. The counterexample is exact and identifies the precise corrected rate in the source proof; a researcher relying on persistence bounds would need this distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
