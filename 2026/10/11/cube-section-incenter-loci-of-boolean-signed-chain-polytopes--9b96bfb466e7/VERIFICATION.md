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

# Reproducible verification

Run `python3 artifacts/verify_signed_boolean_incenters.py` using a standard Python 3 interpreter. The program has no third-party dependencies. It independently enumerates all maximal Boolean chains for \(1\le d\le6\), computes exact rational ranks of their incidence matrices, enumerates all vertices of the proposed central cube sections, and tests every rank-subset signed-chain ball slack at each listed vertex. The supplied captured output records the actual successful run.

| \(d\) | Ambient coordinates | Maximal chains | Matrix rank | Incenter-locus vertices |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 2 |
| 2 | 4 | 2 | 2 | 6 |
| 3 | 8 | 6 | 5 | 6 |
| 4 | 16 | 24 | 12 | 30 |
| 5 | 32 | 120 | 27 | 20 |
| 6 | 64 | 720 | 58 | 140 |

Separate numerical linear programs for \(1\le d\le4\) optimized the inscribed radius directly against all nonempty-chain inequalities. Their optima matched \(1/\sqrt{d+1}\) to normal floating-point accuracy. Neither the exact finite ranks nor these numerical programs establish an infinite-dimensional theorem; the proof in `RESULT.md` supplies the arbitrary-\(d\) justification and examines short chains and boundary cases explicitly.
