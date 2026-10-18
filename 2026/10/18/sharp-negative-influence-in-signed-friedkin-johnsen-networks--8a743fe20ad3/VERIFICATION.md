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

# Verification of the sharp signed-graph influence bound

## Evidence paths and commands

The companion standalone file `verify_signed.py` uses Python standard-library `fractions.Fraction`, `itertools`, and explicit Gauss–Jordan elimination. Run `python3 verify_signed.py` from any directory containing that file. It uses no downloaded files, external packages, or generated source artifacts.

## Exact boundary checks

The checker visits all \(3^6=729\) signed/absent labeled four-vertex edge assignments. Precisely \(624\) are connected. It independently solves \((I+L_\sigma)h=\mathbf1\) with fractions, checks the sharp all-order bound for all tested sizes, checks the graph-specific Schur barrier at two, three and four vertices, and matches negative structure centrality exactly to the stated four-vertex graph condition. It independently calculates all canonical permutation representatives, confirming \(104\) labeled cases in orbit sizes \(4,4,12,12,12,12,24,24\). It also checks the analytical hostile-hub equality solution for every order from three through thirty.

Expected output contains `n=2: connected=2, negative=0, min=1/3`, `n=3: connected=20, negative=0, min=0`, `n=4: connected=624, negative=104, min=-1/5`, and a final `PASS` message.

## Unproved limits

The finite enumeration proves only the stated finite graph-order boundary and orbit census. The claim over every \(n\ge3\) relies on the analytical Neumann-series, Schur-complement and Laplacian comparison steps in `RESULT.md`. Publication priority is not certified by a failed literature search, and no independent audit has been conducted.
