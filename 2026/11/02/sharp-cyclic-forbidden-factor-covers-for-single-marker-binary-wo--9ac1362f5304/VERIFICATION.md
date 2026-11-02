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

Use Python 3 standard library only:

```sh
python3 verify.py
```

Expected result:

```text
VERIFY_OK orders=3..12 interior_cases= 55 total_constructed_symbols= 74161 literal_exhaustion_n3=8,9_n4=18,19
```

`verify.py` performs its own breadth-first shortest-path search after deleting the forbidden edge, not relying on the closed-form expression for \(\delta\). It then builds the explicitly claimed shortest repair, constructs a full Euler circuit with duplicated edges, and computes the full cyclic length-\(n\) factor multiplicity vector from the actual output symbols. Literal circular-word enumeration separately checks the first nontrivial boundary lengths in order \(3\) and the two noncentral possibilities in order \(4\). Both the exceptional center and noncentral families are included among all interior positions for orders \(3\) through \(12\).

Limitations: Finite replay is not proof of the infinite theorem, and verifying an Euler tour does not enumerate all optimal Euler tours. The mathematical proof in RESULT.md provides the all-order minimality, impossibility cases and unique multiplicity profile. Self-review is passed; no independent audit or external certification has been performed.
