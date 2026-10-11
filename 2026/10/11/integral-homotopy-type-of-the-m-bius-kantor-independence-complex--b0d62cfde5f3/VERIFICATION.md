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

The independent external audit has not been performed. Two standalone standard-library Python programs reproduce the finite calculations described in `RESULT.md`.

Run `python3 verify_dual.py`: the eight derived incidence triples, 140 nonempty Alexander-dual faces, 67 pairs, all 424 directed face incidences, six critical cells and the zero integral boundary vector are checked by assertions. Its successful completion prints `DUAL_VERIFY_OK`. The homotopy reduction from incidence graph to suspension uses Tsukuda's Corollary 4.11 as an external mathematical theorem, not as a numerical assumption.

Run `python3 verify.py`: it reconstructs the 16-vertex graph and independently enumerates 1,090 nonempty independent-set faces; checks 541 discrete-Morse pairs, the complete 4,272-incidence acyclicity directed graph, a signed 5-by-2 integral critical boundary with primitive rank one, the complete original simplicial boundary ranks over the field with two elements, and the resulting reduced Betti numbers. Successful completion prints `VERIFY_OK`.

Neither computation certifies novelty against unindexed literature, and neither supplies an infinite-family classification. No third-party verification is claimed.
