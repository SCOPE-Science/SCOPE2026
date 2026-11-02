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

For a fixed zero-sum vector, cyclic root i yields m_i=h_max-h_i and s_i,k=h_(i+k)-h_i. Summing the deterministic orbit identity 2 sum_i m_i s_i,k=sum_i s_i,k^2, using zero sum and cyclic invariance gives Cov(M,S_k)=Var(S_k)/2 for every interior k without sign assumptions. Under negated-reversal invariance, reverse cyclic path from lag k to zero to pair (M-S_k,-S_k); centering gives the exact joint reflection. The skew orbit of (2,-1,-1) has nonsymmetric S_1 and is an explicit boundary witness.

## originality

PASS

Best-of-knowledge originality: inspected the frozen final theorem and compared mathematical implications with published related sources rather than titles. The cited ingredients and simpler special cases are prior; the claimed additional precise joint law/spectral bound/bridge law/Dyck rigidity/cyclic construction is not established by the inspected results. Unlocated equivalent prior coverage remains an explicit risk.

## value

PASS

A universal bridge maximum/position covariance law requiring only cyclic stationarity and a pathwise zero sum, plus a stronger joint reflection under additional precisely named symmetry. It covers dependent skew cyclic increment laws where familiar exchangeable/sign-symmetric endpoint arguments do not apply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
