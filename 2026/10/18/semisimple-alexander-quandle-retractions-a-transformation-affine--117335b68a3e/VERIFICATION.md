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

# Computational verification

Run `python3 verify.py`. It builds finite quandle multiplication tables directly from the specified linear operators, recursively enumerates every map preserving those tables by constraint propagation, then directly checks the composition-idempotence identity. Its enumeration does **not** restrict candidates to the theorem's normal form, and it compares all rank coefficients as well as the multiplicity distribution of actual specified images.

Seven exhaustive cases:

| Prime | Fixed dimension | Nonunit operator | Underlying set size | All endomorphisms | Retraction rank histogram |
|---|---:|---|---:|---:|---|
| 3 | 0 | no nontrivial block (singleton quandle) | 1 | 1 | \(1:1\) |
| 2 | 2 | no nontrivial block (trivial four-point quandle) | 4 | 256 | \(1:4,\ 2:24,\ 3:12,\ 4:1\) |
| 3 | 0 | scalar \(2\), multiplicity one | 3 | 9 | \(1:3,\ 3:1\) |
| 5 | 0 | scalar \(2\), multiplicity one | 5 | 25 | \(1:5,\ 5:1\) |
| 3 | 1 | scalar \(2\), multiplicity one | 9 | 243 | \(1:9,\ 2:18,\ 3:6,\ 6:6,\ 9:1\) |
| 3 | 0 | scalar \(2\), multiplicity two | 9 | 729 | \(1:9,\ 3:36,\ 9:1\) |
| 2 | 1 | irreducible \(t^2+t+1\) block | 8 | 64 | \(1:8,\ 2:4,\ 4:2,\ 8:1\) |

Each case also passed the independent image-multiplicity census. The checker terminates with `ALL_EXACT_CHECKS_PASSED`.

**Scope and limits:** The computations enumerate these finite cases only; they do not exhaust the infinite family. The arbitrary-dimension conclusion is supported by the direct normal-form and semisimple linear-algebra proof in `RESULT.md`. The verified source papers examine classifications and endomorphism properties; no independent originality guarantee is claimed.
