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

# Verification record

The theorem's domain has 24 unit quaternions and exactly 2024 three-element supports. The finite-group Fourier-block decomposition establishes every complex nullity symbolically. A separate standard-library Python program, `check_hurwitz_census.py`, performs exact multiplication with doubled integer quaternion coordinates and fraction-free integer elimination on the 24-dimensional left-regular convolution matrix. It verifies all 253 distinct identity-containing triples, the exact quotient cosets, and the two representative edge-order tables used for counting. Every fractional elimination division is asserted exact. Left translation gives 24 choices for each normalized triple, with three normalizations of each unnormalized support, so the exact 253 checks cover all 2024 supports.

Observed direct-exact output for nullities (nullity: support count) was `0:1512, 2:288, 6:96, 8:96, 16:32`. The checker also verified the two orbit-representative edge-order tables. No floating rank, timeout-based exclusion or extrapolation is used. Independently validating the mathematics and publication priority remain open.
