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

Execute `python3 verify_fano_modules.py` (standard-library Python 3). The checker constructs the seven nonzero binary 3-vectors, the seven Fano lines, both independence-complex face lists, all 168 invertible 3-by-3 matrices, all eight order-seven Sylow subgroups, and signed fixed-face Lefschetz traces for every group element. It computes augmented boundary ranks mod 2 for both complexes and checks that rational Betti ranks are forced by Euler characteristics; it also verifies the classwise character identity and inner products.

A successful run prints `VERIFY_OK; |G|=168; rank(Fano H2)=13; rank(Heawood H3)=6; Sylow count=8` followed by complete class data. Rational homology concentration follows from mod-two boundary upper bounds and Euler characteristic, not from extrapolating samples. The program does not construct a canonical map of topological spaces, an integral module isomorphism, or an external independent audit.
