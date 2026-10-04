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

Run `python3 verify.py`.

The program implements reversal and the binary exchange antimorphism directly.  At every directive step it constructs the shortest corresponding pseudopalindromic closure, checks the required symmetry, and verifies that no shorter prefix-extension is already a pseudopalindrome of the required type.  This reproduces the five stated prefixes and the length-36 target word.

For the attractor upper bound, the verifier enumerates every distinct nonempty factor of the target word and all occurrence starts.  There are 500 distinct factors.  It confirms that the position set \(\{3,7,15,21,25\}\) crosses at least one occurrence of every factor.

For the lower bound, it verifies the complete occurrence lists and eligible-coordinate unions of the seven factors displayed in the proof.  Their coordinate supports split into three disjoint ranges.  The left triple has empty common intersection, the middle factor is confined to its own range, and the right triple has empty common intersection, forcing at least \(2+1+2=5\) positions.  As a redundant finite check, the program also tests all 58,905 four-position subsets and confirms that none crosses all 500 factors.

The verification proves only the stated finite counterexample.  It does not search all directive pairs, determine the next valid universal bound, or establish unboundedness.
