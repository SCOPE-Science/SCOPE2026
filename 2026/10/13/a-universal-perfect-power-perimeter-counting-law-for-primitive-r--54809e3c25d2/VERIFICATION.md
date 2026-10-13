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

# Exact reproducibility and boundaries

Execute `python artifacts/verify.py` in any ordinary Python 3 environment. It uses integer powers, greatest-common-divisor tests, and exact set comparisons. The two methods are independent: one enumerates Euclid's primitive parameters and tests exact perfect-power membership, the other enumerates the power-perimeter parameters and maps them into Euclid's variables. Their complete solutions agree for all \(m\le2200\) and exponents \(k\in\{2,3,4,5\}\); the script also checks all solutions below the three documented perimeter cutoffs and concrete examples of exponents \(3,4,5\).

The infinite error term is proved analytically by area integration, elementary lattice discrepancy, Möbius inversion, and the Euler product. The executable regression does not independently certify that analysis, exhaust unbounded parameter ranges, or establish unpublished-result priority. The fixed-\(k\) restriction is essential to the stated scope.
