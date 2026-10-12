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
The bundled checker evaluates the published capacity rule
\[
n(L)=\left\lfloor\frac{L}{35}\right\rfloor
\]
at all seven measured lengths.

It verifies the formula-derived capacities
\[
(1,1,1,2,2,2,3)
\]
and converts them to the source's AICc count using
\[
K=2n+2,
\]
giving
\[
(4,4,4,6,6,6,8).
\]

It compares those values with Table 2's Model-M counts
\[
(4,4,4,4,6,6,8)
\]
and verifies that the unique disagreement occurs at \(70\) bp.

As an implementation check, it evaluates equation (4.3) using the displayed \(70\)-bp Model-M values \(M=25\), \(K=4\), and \(\operatorname{RSS}=199.9\). This gives \(61.9735354\ldots\), within \(0.01\) of the table's \(61.98\); the table displays RSS only to one decimal place.

No missing \(n=2\) fit is simulated or inferred.
