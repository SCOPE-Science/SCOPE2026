---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible verification

From the directory containing the original standalone Python scripts, run:

```sh
python3 verify_character.py
python3 verify_morse.py
```

The first program enumerates the rooted forests, compares the face counts to the Laplacian matrix-forest polynomial, computes signed reduced Lefschetz traces for the 144 bipartition-preserving automorphisms, and uses class-weighted inner products to reproduce all 15 rational character entries and all 15 irreducible multiplicities. It also checks that the top simplicial boundary has mod-two rank 2592.

The second program gives an integral check of the previously known nonequivariant wedge type used to isolate the fifth homology trace: it sorts the Hasse digraph on 12,799 nonempty faces with 60,456 arrows and exhibits an integral Morse-boundary minor of determinant −1. The wedge type is credited as prior, not claimed as a new classification. These finite checks apply to this graph only.
