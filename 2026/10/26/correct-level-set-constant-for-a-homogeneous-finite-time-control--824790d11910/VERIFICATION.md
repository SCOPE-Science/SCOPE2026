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

The value-function derivative was derived from the source's HJB equation and optimal feedback. Compactness of the unit value-function level set and positivity of the running cost imply a strictly positive minimum. Weighted homogeneity converts this minimum into the required lower comparison coefficient, and direct integration gives the settling-time estimate.

The admissible example uses \(n=2\), \(q=2\), \(d=2\), \(\mu=1/5\), and \(F(x_1,x_2)=|x_1|^{10/7}+|x_2|^{5/3}\). Its homogeneity weights are \((7/5,6/5)\), and it satisfies \(\mu<d(q-1)/(qn)\). Assuming \(F\) constant on the unit value-function level set forces \(V_\infty=C F^{11/10}\); the HJB equation at \((s,0)\), \(s\ne0\), then gives the contradiction \(F(s,0)=0\).

Limits: this establishes the minimum-based estimate and shows that the maximum cannot be substituted in the displayed comparison argument. It does not prove that the printed maximum-based estimate is false by every possible alternative argument. No independent audit or external validation has been performed.
