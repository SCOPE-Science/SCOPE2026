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

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses only the standard library and reconstructs the entire finite instance from definitions.

It enumerates all \(720\) permutations in \(S_6\), deletes each of the five possible adjacent coordinate pairs, standardizes every residual word into \(S_4\), and builds the exact descendant mask for every source permutation. It checks that there are \(24\) possible received permutations and \(610\) distinct nonempty descendant masks, with multiplicity distribution \(1:538, 2:50, 3:6, 4:16\).

The dynamic program uses the exact least-available-output recurrence proved in `RESULT.md`. It returns maximum code size \(12\), exactly \(67{,}163{,}560\) labeled maximum codes, and footprint histogram
\[
16:100,\ 17:3240,\ 18:47958,\ 19:415120,\ 20:2283083,\ 21:8134400,\ 22:18331932,\ 23:23922912,\ 24:14024815.
\]
The script asserts that these entries sum to the labeled maximum-code total. It also reconstructs the explicit twelve-word witness from the embedded constants and verifies that its descendant masks are disjoint and cover all \(24\) received permutations.

The recorded replay output is stored in `verification_output.txt`. Limits: the replay establishes only the finite fixed-exact-two-burst claim for \(S_6\); it does not prove results for the at-most-two model, other lengths, or other burst sizes.
