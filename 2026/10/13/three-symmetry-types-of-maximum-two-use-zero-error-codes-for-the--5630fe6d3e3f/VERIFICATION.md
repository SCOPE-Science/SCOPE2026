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

Run `python3 verify.py` with a standard Python 3 interpreter.

The verifier first enumerates the \(29\) independent subsets of one \(7\)-cycle and uses them as row states in an independent transfer computation for the seven-row toroidal strong square. This regenerates the entire independence polynomial and therefore proves that the maximum size is \(10\) and that exactly \(980\) maxima exist.

A separate branch-and-bound procedure works in the 49-vertex compatibility graph. It enumerates every size-\(10\) code containing \(00\), finding \(200\), and expands these by all \(49\) translations to obtain exactly \(980\) distinct labeled maxima. The equality \(980\cdot10=200\cdot49\) is checked.

The verifier then generates all \(392\) elements of the natural group \((D_{14}\times D_{14})\rtimes S_2\), partitions the complete maximum-code census into orbits, checks stabilizers, and recomputes the \((u,v)\) fingerprints and coordinate multiplicity profile for every maximum.

The verifier does not attempt to determine the full abstract automorphism group of \(C_7\boxtimes C_7\).

Expected first terminal line:

`VERIFY_OK vertices=49 layer_states=29 maximum=10 maxima=980 normalized_origin=200 natural_group=392 orbits=3 orbit_sizes=196,392,392 stabilizers=2,1,1 orbit_fingerprints=(0,2):392;(1,1):392;(1,2):196 row_col_profile=2,2,2,1,1,1,1 normalized_sha256=2e8d95cfc42c76a63db408aa2c68122678e83dd8f3ec0e4190e605cc810f2675 maxima_sha256=91a218e8c389d722d411f23ba32fee36aecf2072afb12619c7954b2d31f15bc5`
