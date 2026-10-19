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

The exact finite domain is the Heawood incidence graph on 14 vertices. The provided `verify_torus_main.py` enumerates all 24 perfect matchings, 28 simple hexagons, 42 vertex angles, and all eight seven-hexagon angle covers. It verifies orientability of every cover, checks that its surface is toroidal, enumerates every face flip, and checks the 24 matching states, the \(3C_7\sqcup3K_1\) decomposition, seven distinct facial labels in each nontrivial cycle, all one-factorizations, and twofold coverage. Running this program against `HEAWOOD_CERTIFICATE.json` checks every entry of that certificate.

The separate `verify_torus_independent.py` uses a cyclic \((7,3,1)\) difference set and bit-mask operations rather than the binary Fano representation. It exhaustively regenerates the matching, cycle, angle-cover, factorization, and component counts and multiplicities. Both verification programs require only the Python standard library. Run:

```
python3 verify_torus_main.py HEAWOOD_CERTIFICATE.json
python3 verify_torus_independent.py
```

The scripts establish the finite classifications through explicit exhaustive recurrences; they do not prove any infinite family theorem. They do not establish historical priority or constitute an independent mathematical audit.
