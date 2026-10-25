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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. No network, repository checkout, data files, libraries, or external tools are needed. The program constructs the 27 points and all 5,949 flag simplices directly from the metric and checks all eight bitset boundary ranks, the mod-two Betti vector, all 22 cycle-product conjugacy classes, all 1,296 symmetry traces, independently signed Lefschetz traces for every class representative, and all 22 rational wreath-product irreducible character inner products.

Expected success line: `TERNARY_HAMMING_WREATH_CHARACTER_VERIFIED 5949 22 1296 7`. The computation is exact over integers and binary finite fields. The rational homology step uses the comparison of rational with mod-two matrix ranks together with the Euler characteristic; no inference of integral homology from modular ranks is made.

The verifications establish a finite, fixed 27-vertex result; they do not certify an infinite family, an integral G-module, or a genuine equivariant wedge decomposition. The checks are self-review only, not independently audited.
