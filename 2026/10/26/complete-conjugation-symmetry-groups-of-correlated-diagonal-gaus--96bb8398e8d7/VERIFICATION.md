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

The proof identifies the entire covariance operator and checks its infinitesimal unitary stabilizer, constructs every block-unitary symmetry, and applies the normalizer of the connected compact group. All quantifiers cover every integer dimension at least two and every positive-semidefinite real symmetric diagonal covariance. The covariance normalization \(\mathbb E|H_{ij}|^2=1\) is essential.

Run `python3 check_correlated_gaussian_symmetries.py` in a directory containing the verification script. The exact-rational script verifies 102 assertions, including each of the 24 permutations of a four-coordinate two-block covariance, intra- and inter-block rational rotations, three unequal rank-one weights with unit-spectrum degeneracy, and a singular full-symmetry boundary covariance. It uses no external packages.

These tests do not enumerate all dimensions, do not directly exhaust complex unitaries, and do not constitute independent validation. The universal case, arbitrary complex phases, and possible disconnected symmetries are established by the analytic proof.
