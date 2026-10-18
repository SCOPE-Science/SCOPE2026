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

# Verification guide

The proof is the uniform poset-fiber contraction and good-cover nerve argument in `RESULT.md`. No executable computation is needed to establish the full infinite family, but two separate finite verification programs stress-test the key statements.

Run `python3 verify_fibers.py` to exhaustively enumerate every nonempty subset of the cyclic tournament vertex sets of orders 5, 7, 9, 11, 13, and 15. For each subset the program compares Hom upper-fiber nonemptiness with arc containment, checks the exact intersections of in- and out-neighborhoods, and verifies the distinguished vertex dominates all permissible third-coordinate vertices. Successful output terminates with `FIBER_CONTRACTION_CHECK_OK`.

Run `python3 verify_chains.py` to enumerate all directed multihomomorphism cells at orders 5, 7, 9, 11, and 13 and to compute ranks of signed cellular boundaries over the prime field with 1000003 elements. The program checks Betti ranks 1 in dimensions 0 and 1 and 0 in all other dimensions. Successful output terminates with `HOM_CELLULAR_CHAIN_CHECK_OK`. The complete observed output of both programs is `check_output.txt`.

Both programs use Python 3.10 or newer without third-party libraries. These finite checks do not independently prove the infinite family, rule out torsion in arbitrary additional cases, or constitute an independent audit. The proof of integral homotopy equivalence is the explicit finite-poset fiber theorem applied uniformly in the parameter.
