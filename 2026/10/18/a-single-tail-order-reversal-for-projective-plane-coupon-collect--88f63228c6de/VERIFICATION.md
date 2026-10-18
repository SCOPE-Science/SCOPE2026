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

# Verification and reproducibility

Execute `python verify.py` using Python 3.9 or later. No third-party dependency, external file, or network access is required.

The code enumerates all \(2^{13}-1=8191\) nonempty sets of possibly missing points and reconstructs the full exact inclusion-exclusion coefficients of the projective mechanism. It also enumerates all \(8191\) nonempty line subfamilies and verifies that their exact covering-count formula agrees with the probability expansion. For the full mechanism, a separate combinatorial formula and an exhaustive enumeration over all \(715\) allowed blocks give the same coefficient table.

An independent occupied-state dynamic program checks cover probabilities at times four and five under both mechanisms, including exact rational arithmetic and no simulation. Exact arithmetic establishes the sign at times five through nine and the strict rational bound \(B_{10}<41/50\) in the analytical proof. Positivity for every \(t\ge10\) uses the monotonicity of the six exponential ratios in the proof, not finite case checking.

The pre-delivery execution printed PASS and the fractions \(-15480/2924207\) and \(2178216/418161601\) for the two adjacent crossing times. Mean values from the earlier literature were separately reproduced as regression checks; their proof and priority are not claimed here.

Limits: only the complete thirteen-point case is certified. Nothing about larger orders or all finite block systems is inferred from numerical checks. Independent audit has not been performed.
