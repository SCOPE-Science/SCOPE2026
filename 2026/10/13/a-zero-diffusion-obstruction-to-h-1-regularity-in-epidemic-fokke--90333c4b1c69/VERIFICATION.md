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
The checkable witness is the transport equation obtained from the source's equation (6) under \(\sigma_S=\sigma_I=0\). With \(\Omega=(0,2)^2\), \(Q=(1/5,2/5)^2\), \(f_0=25\mathbf1_Q\), and \(F(S,I)=(1-S-SI/10,(S/10-2)I)\), the accompanying \(\texttt{verify.py}\) performs exact fraction arithmetic. No external package is needed. Invoke \(\texttt{python3 verify.py}\), and it prints \(\texttt{VERIFY_OK}\).

Proof steps not reducible to finite testing are: uniqueness of the push-forward distribution under a smooth Lipschitz vector field, positive and finite Jacobian for finite times, and the fact that a nonzero jump along a smooth interior arc has a singular distributional gradient and excludes \(H^1\). The verifier checks premises, not an infinite-time or all-weak-solutions certificate. The result concerns only the spatial regularity asserted in Proposition 2.1; positivity and unit mass persist. The publicly inspected source has no explicit uniform ellipticity requirement in the proposition's hypotheses.
