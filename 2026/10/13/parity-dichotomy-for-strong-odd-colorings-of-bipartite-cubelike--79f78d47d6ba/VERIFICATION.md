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

# Verification

Run `python3 verification/check.py` in the artifact root, using Python 3.8 or later. The script uses only the standard library and its deterministic output is stored verbatim in `verification/output.txt`. It checks all nonempty generator subsets of every affine parity-hyperplane coset in dimensions \(1\le d\le4\) (\(3,940\) pairs counting distinct functionals), plus \(240\) seeded higher-dimensional cases and \(20\) exact odd-Hamming-shell instances. For each it checks all graph vertices, all neighbor multiplicities, properness, construction of coordinate witnesses, odd fiber counts, and the even-degree two-step-adjacency parity. It does not enumerate all three-colorings; their impossibility is proved mathematically by the adjacency-operator argument.

Checks of finitely many dimensions cannot establish the infinite theorem. The written proof derives the parity-fiber and square-zero identities for all \(d\) and all nonempty admissible \(S\). No external independent review was performed.
