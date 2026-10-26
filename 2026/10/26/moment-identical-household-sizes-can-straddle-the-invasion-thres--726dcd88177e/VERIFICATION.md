---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The displayed finite calculations were checked from the formulas in RESULT.md. For a path of size \(m\), the probability that a target at distance \(d\) is reached is \(2^{-d}\), and there are \(2(m-d)\) ordered seed-target pairs at that distance. This gives \(H_m=1+\frac{2}{m}\sum_{d=1}^{m-1}(m-d)2^{-d}\), hence \(H_1=1\), \(H_2=3/2\), \(H_3=11/6\), and \(H_4=33/16\).

The two household laws each sum to one and have \(\mathbb E[M]=2\), \(\mathbb E[M^2]=5\), and variance \(1\). Substitution into \(\mathcal R_*=\beta\sum_m q_m mH_m/\mathbb E[M]\) gives \(403/400\) and \(2387/2400\). The strict threshold comparisons hold for the whole interval \(8/13<\beta<48/77\); the selected \(31/50\) lies inside it because \(403>400\) and \(2387<2400\).

Limits: the branching interpretation assumes a large population so repeated external infections of the same household are negligible. The result does not certify a real-world model, an arbitrary household topology, or the uniqueness of this example in all literature. Independent audit and independent validation have not been performed. No independent-audit or external-validation evidence is supplied here.
