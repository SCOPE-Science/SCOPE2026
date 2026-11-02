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
# Reproducibility and limits

Run `python3 checker.py` with Python 3.9 or later. The script performs self-contained exact calculations for every rim length \(5\le k\le12\). It enumerates all unordered zero-cells, edge/vertex one-cells, and pairs of disjoint graph edges as two-cells. It verifies the integral composition \(\partial_1\partial_2=0\), expected cell counts, finite-field boundary ranks for primes \(2\), \(3\), and \(1000003\), and the character of each of the \(2k\) dihedral elements computed independently from oriented fixed cells. It also checks exact rotation/reflection character sums. The successful final output is `WHEEL_TWO_PARTICLE_DIHEDRAL_CHECKS_OK`.

The forest boundary argument and explicit dihedral fixed-cell classification in RESULT.md are the proof for arbitrary \(k\ge5\). Finite-field checks for finite \(k\) do not establish the infinite result, nor do they alone exclude integral torsion outside the checked range. The theorem's integral torsion claim follows instead from characteristic-independent forest injectivity and universal coefficients.

Independent external validation has not been performed.
