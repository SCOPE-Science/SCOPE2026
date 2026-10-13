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

To verify the theorem, run `python3 verify_graph.py`, `python3 verify_linear.py`, and `python3 verify_grouped.py` using Python 3 with its standard library. Each prints `VERIFY_OK` only if its asserted counts, pair distances, and closure properties hold.

`verify_graph.py` is the exhaustive proof-critical enumeration: for every permitted length, it builds the complete list of nonzero words of pair weight at least the required distance, and recursively enumerates every seven-clique in strictly increasing order. It checks linear closure of every normalized code and all its translated cosets. No higher-dimensional, unexamined, or partial code sample is used.

`verify_linear.py` independently enumerates all three-generator spans and checks their minimum pair weights. Since it restricts to linear spaces, it is a corroboration rather than the proof that no nonlinear code exists. `verify_grouped.py` independently enumerates the 78,125 equality-case selections at length seven. The mathematical Singleton/Plotkin bounds establish the complete parameter range beyond the finite test cases.

Both the exact census and the algebraic affine-coset conversion must hold for the announced counts; all sources, premises, and numerical limits are given in the result. No external formal or independent audit has been conducted.
