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

All computations use Python 3 standard library only. Place `verify_morse.py`, `verify_chains.py`, and `morse_certificate.json` in the same directory. Run both scripts as described in `RESULT.md`.

The Morse script enumerates all 1025 nonempty faces of the original complex, reconstructs the specified 18-edge Frucht graph from LCF data, and independently verifies a matching and complete acyclic directed face-poset graph for the original and for each of eighteen edge deletions. It rechecks every pair and critical face against the full included certificate. The original has one critical vertex and twenty critical three-simplices. Each deletion has one critical vertex and the listed number of critical three-simplices, no others. This establishes the homotopy results via the finite discrete-Morse theorem, not simply by computing field homology.

A separate brute-force enumerator constructs all nonempty matchings from possible edge subsets and checks mod-two simplicial boundary ranks. In the full complex the degrees-one-through-five ranks are \((17,100,233,144,8)\), yielding third Betti number twenty and zero other reduced Betti numbers. The deletion checks agree with the Morse certificate. These mod-two computations do not by themselves certify integral homotopy; the acyclic Morse matchings do.

`checks.txt` contains actual success output. The external literature comparison remains subject to possible unindexed or inaccessible equivalent results. No independent audit has been performed.
