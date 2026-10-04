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
The embedded `verify_egalitarian_sexequal_boundary.py` is an exact finite replay using only the Python standard library.

Two independent stability tests are implemented. One uses precomputed rank maps; the other compares positions directly in the preference lists. They are required to return exactly the same stable-matching set for every profile.

The replay verifies:
- all \(16\) strict \(2\times2\) profiles have \(E(I)=S(I)\);
- all \(46656\) strict \(3\times3\) profiles are exhausted;
- exactly \(40056\) profiles have equal optimum sets;
- exactly \(3720\) have \(S(I)\subsetneq E(I)\);
- exactly \(360\) have \(E(I)\subsetneq S(I)\);
- exactly \(2520\) have disjoint optimum sets;
- zero profiles have nonempty nonnested overlap;
- the stable-count marginal is \(34080,11484,1092\);
- the displayed \(3\times3\) witness has exactly two stable matchings with objective pairs \((12,2)\) and \((11,3)\).

Run:

`python3 verify_egalitarian_sexequal_boundary.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary. It does not classify larger markets.
