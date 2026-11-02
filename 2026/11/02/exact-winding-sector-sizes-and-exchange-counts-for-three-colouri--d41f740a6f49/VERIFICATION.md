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
# Finite verification accompanying the proof

Run `python3 check_components.py` and `python3 check_transfer.py` with Python 3 and the standard library. These are separate, self-contained implementations.

`check_components.py` generates named proper three-colourings directly as legal ordered pairs of rung colours. It enumerates every one-vertex recolouring, performs a complete breadth-first connected-component partition, computes the winding and counts sector edges. Its exhaustive tests cover the prism lengths \(3\le n\le10\), including the frozen triangular prism and multiples of three. Successful run terminates with `PRISM_DIRECT_COMPONENTS_PASS`.

`check_transfer.py` constructs the two-orientation Laurent transfer matrix and the marked recolourability transfer independently. It checks exact integer polynomial coefficients at every winding for \(3\le n\le30\), and separately cross-checks a six-state colour-pair matrix for \(3\le n\le9\). Successful run terminates with `PRISM_LAURENT_TRANSFER_PASS`.

Both programs were executed on these complete source files and passed. The mathematical proof for all integer \(n\ge3\) relies on the general established three-colour reachability theorem and the explicit Laurent-transfer identity. Computational checks are finite corroboration only; they do not prove infinite-family novelty or replace full historical comparison. A separate scholarly audit has not been performed.
