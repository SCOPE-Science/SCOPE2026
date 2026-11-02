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

Run `python3 verify_lipschitz.py` from the directory containing the packaged file; it requires only the Python 3 standard library. It exhaustively evaluates the published Newton-polyhedron/lattice-subgroup membership criterion for the \((n-1)^2\) gap candidates at each \(n=3,4,5,6,7,8\). In this family, the generators besides \((1,0)\) have first coordinate either zero or \(n\), making Newton membership a two-point segment test. The complementary subgroup contains \((1,0)\), so its second-coordinate gcd decides lattice membership. This is a separate combinatorial verification of the metric proof in `RESULT.md`.

The recorded execution printed:

```
n=3 holes=1 minimal_generators=6 checked_q=4
n=4 holes=3 minimal_generators=8 checked_q=9
n=5 holes=6 minimal_generators=10 checked_q=16
n=6 holes=10 minimal_generators=12 checked_q=25
n=7 holes=15 minimal_generators=14 checked_q=36
n=8 holes=21 minimal_generators=16 checked_q=49
VERIFY_OK: 139 full-subset decisions; 1383503 subsets actually tested
```

The checker also directly computes minimal generators of both original and predicted saturated semigroups, checking the claimed cardinality \(2n\). This is finite evidence only. The arbitrary-parameter theorem rests on the explicit complex analytic Lipschitz estimates and root-of-unity obstruction in `RESULT.md`; no independent mathematical audit is claimed.
