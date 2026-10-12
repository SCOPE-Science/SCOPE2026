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

The final claim is proved analytically for arbitrary finite dimension. No numerical search, finite enumeration, or empirical log is used as evidence for the universal statement.

For a Hilbert--Schmidt orthogonal projection \(\mathcal E\), the identities
\[
\operatorname{Tr}(\rho^2)=\operatorname{Tr}((\mathcal E\rho)^2)+\lVert(I-\mathcal E)\rho\rVert_2^2
\]
and
\[
\operatorname{Tr}(\rho\sigma)=\operatorname{Tr}((\mathcal E\rho)(\mathcal E\sigma))+\operatorname{Tr}(((I-\mathcal E)\rho)((I-\mathcal E)\sigma))
\]
were checked symbolically from orthogonality of the range and kernel. Substituting them into superfidelity gives exactly one Cauchy--Schwarz deficit in a direct-sum real Hilbert space, so no unverified auxiliary lemma remains.

For projective measurement, self-adjointness follows from cyclicity of trace and orthogonality of the projectors, and idempotence follows from \(P_iP_j=0\) for \(i\ne j\). Positivity and trace preservation are immediate. Thus the published Eq. (29) is within the proved scope for arbitrary noncommuting density matrices.

The proof does not establish monotonicity under arbitrary quantum channels, selective measurements, or infinite-dimensional conditional expectations. Those cases remain outside the claim.
