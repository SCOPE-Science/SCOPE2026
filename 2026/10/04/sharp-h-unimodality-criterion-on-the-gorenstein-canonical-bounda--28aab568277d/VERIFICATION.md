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
The bundled checker uses exact integer arithmetic only.

For every \(2\le r\le400\) and every divisor \(t\mid2r\), it computes the Ehrhart \(h^*\)-vector directly from
\[
w(m)=m-\sum_i\left\lfloor\frac{m q_i}{1+\sum_jq_j}\right\rfloor
\]
for \(\mathbf q=(1^{r-1},2r/t,r+2r/t)\). It compares that vector coefficient-by-coefficient with the claimed even/odd factorizations and compares direct coefficient unimodality with the stated threshold. It also checks
\[
h^*_{\mathbb P(1^r,r,r)}=(1+\cdots+z^{r-1})(1+z+z^2)
\]
for every \(2\le r\le400\).

As a separate regression, for every \(2\le r\le60\) it scans all \(1\le a\le2r\), \(a\le b\le3r\), tests the Gorenstein divisibility conditions, and recomputes canonicity and terminality from every nonidentity Reid--Tai element in both heavy charts. The resulting Gorenstein canonical/non-terminal set is required to equal exactly the divisor family plus \((r,r)\).

These are finite checks; the all-dimensional proof is in `RESULT.md`.

Expected terminal output: `VERIFY_OK`.
