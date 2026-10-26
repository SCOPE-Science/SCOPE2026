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
# Verification record

The supplied `verify.py` is a standalone Python 3 standard-library program. Run `python3 verify.py` to replay the complete eight-letter finite census and the lower-length checks. The checker enumerates every ternary word at each even length through eight, tests all subsets of half the positions, checks dihedral agreement by rotation and reflected rotation, separately verifies the four-letter repeated-symbol adjacency criterion, and checks the exact 48-element orbit of `00011022`.

The executed checker returned `DIHEDRAL_SHUFFLE_COUNTEREXAMPLE_PASS` and counts `{2: (3, 0), 4: (21, 0), 6: (183, 0), 8: (1641, 48)}` (pairs are even-word count and obstruction count). It also checked 24 balanced partitions of the witness, with the only ordered outputs `0012`/`0102` and `0102`/`0012`.

The direct proof of the specific witness and the minimality argument use no computation; only the 48-word census depends on a finite exhaustive enumerator. The assertion concerns indexed ternary words of lengths at most eight, not longer words.
