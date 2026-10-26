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

Run `python3 checker.py` (Python 3 standard library) from a directory containing the extracted files. It enumerates every three-one labeled support in the circle of length \(3p\), for all \(1\le p\le12\), by counting successful starts directly from their three separate block counts. It checks the analytic phase formula for all \(24{,}531\) supports.

The checker also independently enumerates circular distance-triple orbits and checks the exact complete distributions for every \(1\le p\le120\), including the single equally spaced class. The recorded direct run output ended: `VERIFIED 24531 direct labeled weight-three supports, 120 entire necklace distributions`.

No finite enumeration proves a statement for arbitrary \(p\). The proof in `RESULT.md` establishes that generalization through an integer-interval intersection, bounded-composition inclusion–exclusion, Burnside's lemma, and a Riemann-sum limit. The code is corroborating ordinary proof-checking software, not independent mathematical certification.
