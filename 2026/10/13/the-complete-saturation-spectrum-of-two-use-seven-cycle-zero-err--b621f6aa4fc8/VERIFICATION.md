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

The complete two-use seven-cycle search was reproduced with the bundled Python 3 (`verify_a.py`) and C++17 (`verify_b.cpp`) programs. Both independently construct all compatibility edges, enumerate every maximal clique by a complete pivot recursion, check every output directly for zero-error feasibility and nonextendability, and partition the same outputs under five symmetry generators. Their sorted 83,181-mask outputs agreed byte-for-byte. Histogram by code size: 7:28, 8:9016, 9:73157, 10:980. Orbit-size distribution: size-7 (28:1); size-8 (196:8,392:19); size-9 (49:1,98:2,196:18,392:177); size-10 (196:1,392:2). Hash of decompressed canonical list: `362d213751756f339a3319847ce2bc6b580fd2ddc34d124b265e0a1dd417de13`.

The usual Bron–Kerbosch pivot invariant establishes exhaustive search over **all** maximal cliques, rather than sampling or merely checking witnesses. Direct nonextendability checks certify each candidate. This finite computation does not prove broader parameter or asymptotic claims. Literature review establishes neither external independence nor absolute priority: related exact extremal sizes and independent-domination results are known, and one specialist 2005 full text could not be examined.
