---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a>1, 0<b<1/a, two patch states M_A=P_m diag(a,b), M_B=P_m diag(b,a), C=a+b-2ab>0. Direct exact determinants give frozen subcritical threshold m_F=(a-1)(1-b)/C and perfectly alternating supercritical threshold m_P=(1-ab)/C. For endpoint m=0,1 and every 0<q<1 the ergodic environmental match chain has half a/half b multipliers, giving gamma=log(ab)/2<0, while at q=1,m=1 gamma=log a>0. At interior m, positive paired left Perron weights give exact lambda multiplication per switch and bounded positive factors per nonswitch, so q log lambda+(1-q)log r>0 near q=1. Independently checked determinant factorizations with symbolic algebra and the exact rational witness (a,b,m,q)=(3,1/4,9/10,3/4), switch=27/10, nonswitch>=18/55, 4-step factor 177147/27500>1. Claims linear almost-sure log growth, not finite population survival.

## originality

PASS

Best-of-knowledge mathematical comparison supports the scoped additional claim, not a discovery of the model, generic method or unconditioned antecedents. Actual published Resultary searches and primary sources reviewed; some historical sources were abstract-only, with named priority risks. The final theorem is not known from inspected stated prior implications; no global novelty certification.

## value

PASS

An exact phase-slip singularity between q=1 deterministic alternation and any q<1 at complete swap, coupled to an interior-mixing survival window, is a natural and mathematically sharp boundary of random positive matrix products. The explicit rational noisy-persistence certificate while every frozen environment is subcritical is a motivated ecological mixing example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
