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

The primary analytical verification is the rational beta-integral identity and its shifted-quadratic Hurwitz argument. The included `checker.py` independently evaluates the defining correlation integral at seven combinations of positive rates, positive/negative/zero delay and positive/negative/zero frequency, using high precision numerical quadrature. Its maximum scaled deviation from the derived formula was below \(4\times10^{-16}\), with an asserted tolerance of \(10^{-13}\).

The checker symbolically verifies the polynomial shift, the discriminant \((1-\rho)^2(\rho^2-14\rho+1)\), and the nonvanishing of all five numerator values at pole locations. It also verifies the root real-part bound and the crossover at \(\rho=7-4\sqrt3\) in representative cases. None of those finite samples purports to establish universal or nonvanishing-frequency claims on its own; those follow from the exact displayed polynomial identities and the positivity argument.

The extension to general nonequispaced triple rates and higher convolution orders is unproved. The uniqueness of this result in the historical literature has not been independently certified.
