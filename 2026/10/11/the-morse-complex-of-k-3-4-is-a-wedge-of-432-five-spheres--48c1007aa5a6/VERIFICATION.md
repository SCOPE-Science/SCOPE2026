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
# Exact verification instructions

Use Python 3 and the two attached scripts in the same directory. No external packages or external data are required. Execute `python3 verify_k34.py` then `python3 verify_k34_mod2.py`.

The first program enumerates the 32,000 possible outgoing assignments on the seven vertices, retains 12,800 acyclic choices (empty face included), and checks the six positive-dimensional face counts as well as the 24 vertex count. It greedily constructs 5,887 augmented matching pairs, then exhaustively topologically sorts all 60,480 oriented incidences. After discarding the empty-face pair there is one critical vertex, 297 critical four-faces and 729 critical five-faces. The signed integral boundary has 4,162 nonzero entries (each \(\pm1\) before elimination). All 297 boundary rows are eliminated by integer unit pivots, leaving 432 unpaired five-cells. Expected terminal marker: `VERIFY_OK`.

The independently written second program enumerates faces afresh and performs exhaustive mod-two boundary reduction. It checks the ranks \((1,23,211,981,2376,2592)\) in dimensions zero through five, obtains degree-five reduced rank 432 and vanishing lower reduced homology, and checks the Euler number 432 from the matrix–forest formula. Expected marker: `MOD2_OK`. The mod-two cross-check would not by itself prove integral torsion-freeness or homotopy splitting; those conclusions use the first program's unimodular integer reduction and the CW-cell attaching argument.

The scripts certify a finite exact instance only. They do not assert an infinite-parameter theorem, an external audit, or certification by a proof assistant.
