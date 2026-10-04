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

The claim is verified by finite exact algebra; no numerical integration, asymptotic extrapolation, or parameter fitting is used.

For the unit-control check, the source values \(c=1/2\), \(\lambda=1/40000\), \(\omega=3/1000\), and \(\theta=3/200\) give \(A=\omega/\theta=1/5\). With \(S=100\) and \(I=10\), exact arithmetic yields
\[
\frac{\lambda SI}{1+cA}=\frac1{44},\qquad
\frac{\lambda SI}{1+A}=\frac1{48},\qquad
\frac1{44}-\frac1{48}=\frac1{528}>0.
\]

For the transfer-balance check, with \(r_1=1/500\), \(r_2=23/1000\), \(r_3=1/50\), \(A=1/5\), \(I=10\), \(Q=5\), \(H=2\), and \(u_1=1/2\),
\[
A(r_1I+r_2Q+r_3H)=\frac7{200},
\]
and the spurious human-population source equals \(7/400\).

The bundled `verifier.py` reproduces those fractions and uses symbolic coefficient bookkeeping to verify that the repaired Hamiltonian derivative is
\[
B_1u_1+(\xi_6-\xi_3)r_1AI+(\xi_6-\xi_4)r_2AQ+(\xi_6-\xi_5)r_3AH.
\]

The verification does not establish a complete repaired optimal-control solution or infer authorial intent.
