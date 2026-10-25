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

The standalone program `verify_fold.py` uses only standard Python 3. Execute `python3 verify_fold.py` in the same directory. Its recorded output is `verify_fold_output.txt`, ending in `VERIFY_OK`.

Direct checks include: a graph-theoretic multipath test against an independently generated pairwise conflict graph; exact conflict-graph identification with a two-rail ladder for lengths \(2\) through \(10\); fixed-orbit graph identification under all three nonidentity Klein-four symmetries for those same lengths; direct enumeration of signed invariant simplicial chains for lengths \(2\) through \(9\); and exact reduced mod-two boundary-rank checks for lengths \(2\) through \(7\). The recorded finite calculation tests 974 nonempty simplicial faces through the full Betti computations and 336 invariant (including empty) face instances in signed traces.

These checks do not prove the infinite families or integral homology on their own. The proof uses a uniform local conflict classification, orbit folding, exact chain-level Lefschetz calculation, and the published nonequivariant integral homotopy theorem.
