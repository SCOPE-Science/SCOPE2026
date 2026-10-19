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

# Finite exact verification

Execute `python3 verify.py` in a directory containing the attached standalone source. Python 3 with its standard library suffices. The program exhausts the Eulerian circuits of the four-bit binary de Bruijn graph rooted at the unique `00000` edge, evaluates the sentinel-free cyclic BWT of each accepted cycle by full rotation sorting, and independently exhausts all \(65536\) pair-block BWT candidates with the LF single-cycle test.

The verification asserts equality of the two complete sets of \(2048\) BWT output strings and of all six exact histogram cells. No randomized inputs, timeouts, heuristic search, floating-point calculations, precomputed external databases, or dependence on other artifact files are used.

Expected output:

`VERIFY_OK order5 necklaces=2048 orientations=65536 independent_methods=2 bwt_sets_identical=2048 histogram=20:38,22:426,24:840,26:608,28:130,30:6`

The scope is solely binary de Bruijn cycles of order five, modulo rotation and not modulo reversal or complement. The count is based on linear runs in the full sentinel-free BWT last column. The proof's exhaustive coverage is established by the unique `00000`-edge rooting and the bounded graph traversal; machine logs alone do not establish coverage. External, independent scientific audit is not performed.
