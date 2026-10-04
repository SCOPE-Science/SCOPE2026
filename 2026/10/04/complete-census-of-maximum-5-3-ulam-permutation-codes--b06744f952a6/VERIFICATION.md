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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program reconstructs the entire finite instance from definitions; it does not read cached scientific results.

It checks:

- all \(120\) elements of \(S_5\);
- all pairwise Ulam distances via longest common subsequences;
- the \(2520\)-edge, \(42\)-regular compatibility graph for threshold \(d_U\ge 3\);
- every maximal clique, obtaining histogram \(2:60,3:120,4:4020\);
- all six internal distances in each of the \(4020\) maximum codes;
- all \(240\) common-relabeling/position-reversal transformations and their distance preservation on every unordered pair;
- the \(24\) maximum-code orbits and size distribution \(60\) repeated \(5\) times, \(120\) repeated \(7\) times, and \(240\) repeated \(12\) times.

The computation is exhaustive over the stated finite domain. It proves nothing about larger permutation orders or other minimum distances, and it does not claim that the stated \(240\)-element subgroup is the full isometry group.
