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
The executable check uses exact rational arithmetic for a witness and integer matrix identities for the symbolic covariance structure.

For common transmission-rate noise, the direction vector is \((-1,1)^T\). Its outer product is \(\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), which has rank one and annihilates the total-population direction \((1,1)^T\). Therefore the transmission contribution to \(S+I\) has zero quadratic variation.

For the independent-driver implementation with amplitudes of equal magnitude and opposite sign, the diffusion matrix is diagonal and its covariance is the identity times \(q^2\). This covariance has rank two for \(q\neq0\) and gives quadratic-variation coefficient \(2q^2\) in \(S+I\).

At \(S=1/2\), \(I=1/4\), \(\alpha=0\), and source variance coefficient \(0.02=1/50\), the checker obtains \(q^2=1/3200\), common-driver cross covariance \(-1/3200\), and independent-driver total quadratic-variation rate \(1/1600\).

The checker verifies only these algebraic consequences. It does not solve the corrected Fokker--Planck control problem or validate downstream numerical figures.
