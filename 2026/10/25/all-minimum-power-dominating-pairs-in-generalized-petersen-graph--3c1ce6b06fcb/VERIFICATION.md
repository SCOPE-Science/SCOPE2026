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

`verify.py` is standalone Python 3. Run `python3 verify.py` from the directory containing this file and the checker. The script prints `ALL_VERIFY_OK` only after these checks:

1. Build each graph directly from its three edge families. Independently compare synchronous neighborhood forcing, sequential one-force-at-a-time closure, and the vertex/edge monitoring rules for **every unordered pair** for \(9\le n\le20\).
2. Enumerate every singleton, and prove none power dominates in that range; compare the enumerated successful pairs exactly to the three listed families. Thus the finite range is exhaustively checked rather than sampled.
3. Build the complete optimum exchange graph and verify \(6n\) vertices, degree \(10\), \(30n\) edges, and connectedness for every \(9\le n\le20\).
4. Independently compute graph distances and prove that the only failed distance-three pairs are the \(n\) inner offsets-six pairs for every \(13\le n\le20\).
5. Enumerate all pairs in additional graphs of orders indexed by \(n\in\{21,22,23,29,37,61\}\); independently check local stable-case forcing, and stalled states at \(n\in\{21,22,49,97\}\).
6. Verify the displayed \(n=13\) pair has graph distance three and stalls after observing exactly ten of its twenty-six vertices.

The all-parameter conclusion for \(n\ge21\) uses the proven finite walk-type classification and four-column expansion argument in `RESULT.md`; larger-number computations are consistency tests, not substitutes for that proof. No external certification or independent audit was performed.
