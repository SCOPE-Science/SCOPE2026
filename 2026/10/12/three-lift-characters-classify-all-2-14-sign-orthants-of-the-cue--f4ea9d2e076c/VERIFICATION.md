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

Run `python verify.py` with Python 3. The program uses only the standard library and performs exact rational/integer operations.

It independently reconstructs the lower regular subdivision from the fifteen integer valuations, verifies sixteen unimodular triangles of total normalized area \(16\), constructs the projective Viro patchwork graph for each normalized sign assignment, checks all \(16384\) sign orthants, and evaluates the three published bitangent-lift characters. It also verifies the four sample sign choices from the source's Table 2.

The certificate establishes only the finite sign classification for this fixed valuation vector. The application of Viro patchworking and the real-bitangent lift rules are imported mathematical results from the cited source; the checker does not reprove those general theorems.

Expected final output:

`VERIFY_OK triangles=16 projective_sign_orthants=16384 patterns=8x2048 census=1oval:2048,2nonnested:6144,3ovals:6144,4ovals:2048 real_bitangents=4,8,16,28`
