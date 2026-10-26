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

The bundled exact-rational script `verify_trust_game.py` was executed with the Python standard library. Its output was:

Coalition values: empty=0; each singleton=1; each pair=2; grand coalition=3.
Exact Shapley values by permutation enumeration (6 orders): {0: '1', 1: '1', 2: '1'}
Exact internal contributions: {0: '1', 1: '1', 2: '1'}
Exact external contributions: {0: '0', 1: '0', 2: '0'}
Reciprocal-edge-only internal term: {0: '0', 1: '0', 2: '0'}
PASS: all 8 coalitions and all 6 player orders checked with exact rational arithmetic.

The proof covers every finite loopless weighted digraph in the stated model through linearity of the Shapley value; the script checks the three-player counterexample only. No numerical approximation is used. The result does not independently audit other statements in the source preprint, and the script does not certify external publication status or author response.
