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

The proof was checked directly against the displayed model equations. At the disease-free state, the first derivative of every recovered reinfection term \(R_k I\) is zero, leaving the scalar infectious variational equation \(\dot i=[\beta(t)-(\gamma+\mu)]i\).

For the sinusoidal forcing, direct integration over a full period removes the cosine term and gives the one-period multiplier \(M=\exp(T[\beta_0/2-(\gamma+\mu)])\). Therefore the critical amplitude is \(2(\gamma+\mu)\).

The standalone `verify.py` recomputes the case-study threshold from \(\gamma=1\) and \(\mu=1.622\times10^{-4}\) per week, checks the sign of the Floquet exponent for the three fitted amplitudes reported in rounded form by the article, and reconstructs the arithmetic class-average factors for the three stated susceptibility profiles on the 520-stage weekly partition. The script is a replay aid; the analytic Jacobian calculation is the proof.

No claim is made about global persistence, fitted-trajectory correctness, or a unique numerical convention for periodic \(\mathcal R_0\) beyond the exact threshold equivalence proved here.
