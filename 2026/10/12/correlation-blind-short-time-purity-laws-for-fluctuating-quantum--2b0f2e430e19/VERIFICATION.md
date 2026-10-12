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

The proof was replayed from the packaged formulas. For the source's leading rapid-switching generator, direct differentiation of \(\operatorname{Tr}(\rho^2)\) for a pure state gives
\[
R_\psi=2J^2\Delta t\operatorname{Tr}(C K_\psi).
\]
The exchange matrices satisfy \(\operatorname{Tr}(V_eV_f)=2\delta_{ef}\) for distinct unordered edges, and for a localized state \(|v\rangle\), \(K_v\) is exactly diagonal with unit entries on edges incident to \(v\). These identities establish the localized law without numerical assumptions.

The Haar step uses the exact second moment of a Haar-random pure state in dimension \(N\), yielding
\[
\mathbb E K_\psi=\frac{2}{N+1}I.
\]
Therefore
\[
\mathbb E R_\psi=\frac{4J^2\Delta t}{N+1}\operatorname{Tr}C.
\]
For Bernoulli edge indicators, \(C_{ee}=p_e(1-p_e)\), so all off-diagonal edge correlations disappear from both stated probe classes.

The standalone checker uses only exact integer and rational arithmetic. It verifies edge-operator Hilbert--Schmidt orthogonality, all localized \(K_v\) matrices, and the homogeneous closed forms for several dimensions. Its successful finite replay corroborates but does not replace the all-dimension proof.

Scientific limits: the source generator is already a rapid-switching truncation. The theorem does not control omitted higher switching orders; it does not give a concentration bound around the Haar mean; and it does not extend the correlation-blindness conclusion to coherent probe states or arbitrary finite times.
