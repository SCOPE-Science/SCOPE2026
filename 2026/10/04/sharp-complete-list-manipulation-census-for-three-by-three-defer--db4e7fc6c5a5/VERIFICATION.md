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
The embedded `verify_da3_permutation_manipulation.py` performs an exact finite replay.

It exhausts every strict complete profile for \(n=1,2,3\). For \(n=3\), this means all \(46{,}656\) truthful profiles. At each profile, every woman's five alternative complete ranking reports are tested.

Two separately implemented men-proposing deferred-acceptance procedures must agree on every truthful and manipulated instance. For each manipulable truthful profile, all six perfect matchings are independently tested for stability under the original true preferences.

The replay verifies:
- no profitable complete-list receiver manipulation for \(n\le2\);
- exactly \(864\) manipulable labeled profiles at \(n=3\), hence probability \(1/54\);
- \(648\) profiles with one manipulating woman and \(216\) with two;
- exactly one profitable permutation report for every manipulating woman;
- every profitable report induces a matching stable under the true preferences;
- exactly \(24\) role-preserving symmetry classes, each of orbit size \(36\);
- the same \(24\)-class quotient by an independent Burnside count.

Run:

`python3 verify_da3_permutation_manipulation.py`

The first line must be:

`VERIFY_OK`

The computation proves only the finite claims stated above. No extrapolation to larger markets is made.
