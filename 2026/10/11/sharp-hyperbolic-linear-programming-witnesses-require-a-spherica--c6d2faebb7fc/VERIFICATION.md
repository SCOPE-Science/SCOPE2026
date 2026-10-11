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

The proof was checked in two independent pieces. First, the source identities give
\[
\eta_\mu^+(F)=\widehat\eta_\mu(\widehat F)+i_\mu^2\widehat F(\mathbf 1)
\]
and
\[
\eta_\mu^+(F)\le i_\mu F(e).
\]
At equality in the stated density bound their lower and upper endpoints coincide, so the nonnegative spectral term must be zero.

Second, nonvanishing of reduced diffraction was checked without any spectral ansatz. A nonnegative radial test supported strictly below the hard-core separation sees only diagonal pairs, hence its autocorrelation value is \(i_\mu\). Shrinking the test makes its Haar integral smaller than \(1/i_\mu\), so subtracting the background leaves a strictly positive reduced-autocorrelation value. Therefore reduced diffraction cannot vanish.

No numerical experiment, finite truncation, or external certification is used. The conclusion is limited to positive intensity, positive radius, and the compact-support direct witness class; no existence or quantitative stability statement is verified.
