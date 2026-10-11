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
# Verification

The claim is proved analytically for every \(\alpha>1\) and every integer \(N\geq1\). No numerical computation, sampling argument, or finite search is used.

The critical imported steps checked in arXiv:2609.36723v1 are the leading asymptotic \(K_\tau(x)=e^{-s_0x}P(x)+O(e^{-bx})\), compact-uniform convergence \(K_h(\cdot,0)\to K_\tau\), convergence of finite-truncation kernels, and the conformal kernel identity with a positive real-axis multiplier.

Applying the focal sign lemma to both \(P\) and \(-P\) gives arbitrarily late values of both signs. The smaller remainder transfers those signs to \(K_\tau\). A single sufficiently small periodic spacing and then a single sufficiently large finite truncation preserve any prescribed finite alternating sign pattern. The intermediate value theorem yields zeros in disjoint intervals, and the absence of prescribed real zeros proves they are extraneous.

Unproved limits: no quantitative truncation-size estimate, minimum-cardinality result, or simplicity statement is claimed.
