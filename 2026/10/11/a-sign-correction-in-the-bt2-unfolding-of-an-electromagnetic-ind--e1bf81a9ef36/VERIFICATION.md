---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

The source equation preceding Theorem 5.1 explicitly gives \(\beta_1=-0.6956435964\lambda_1+43.44299811\lambda_2\) and positive scaling \(\bar\beta_1=(b^4/a^3)\beta_1\) with \(a=4.537776612\times10^{-4}>0\), \(b=0.4552873824>0\). Thus the first coefficient must be negative. Fresh high-precision decimal replay gives approximately \(-319889446.9717\), consistent with \(-3.19889447\times10^8\), and the second coefficient approximately \(1.99771214917\times10^{10}\). The source immediately before its Theorem 5.1 indeed prints that negative coefficient; its equation (16) alone switches to positive. The source's own saddle-node tangent is \(-\bar\lambda_1+62.4500798\bar\lambda_2=0\), whereas the printed positive sign would yield the opposite first-parameter tangent. Primary PDF page 3224 was visually inspected and directly establishes both discrepancies. Rounded source data certify sign and displayed precision, not hidden full-model center manifold.

## originality

PASS

The source directly supplies both conflicting signs and the associated saddle-node curve, but does not explicitly issue the correction. Generic BT normal form papers do not determine the source-specific numerical coefficient. Searches by DOI, distinctive coefficient and erratum language did not locate an equivalent published corrigendum, although the dedicated published-record semantic service was temporarily unavailable. An unindexed author note is an explicit residual risk. The correction is not claimed independent of source data or a new dynamical-system bifurcation theorem.

## value

PASS

A wrong sign in the constant term of a displayed Bogdanov--Takens unfolding reverses its linear saddle-node orientation if that formula is reused. Correcting the mathematically material local normal form resolves a contradiction between the published theorem and its derivation, even though the source's later bifurcation curves already happen to use the correct sign.

The dated certificate retains the supplied scientific assessment, sources and limitations.
