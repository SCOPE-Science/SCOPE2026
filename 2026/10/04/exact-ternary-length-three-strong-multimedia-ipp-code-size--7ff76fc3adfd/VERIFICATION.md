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

Run `python3 verify.py`. The program uses only the Python standard library.

It reconstructs the \(27\) words of \(\{0,1,2\}^3\), implements the parent-set intersection condition through the proved local uniqueness criterion, generates all minimal non-SMIPPC obstructions inside pair-descendant boxes, verifies the explicit \(11\)-word witness, and performs complete branch-and-bound searches for size \(12\) in the three symmetry-normalized second-word cases.

The expected output is:

`VERIFY_OK maximum=11 witness=11 minimal_obstructions=459 sizes=4,5 symmetry_reps=3 nodes=21227,31563,30388`

The normalization is exhaustive because, after mapping one codeword to \((0,0,0)\), a second word is determined up to coordinate and symbol permutations by its Hamming weight \(1\), \(2\), or \(3\). The search is finite and complete; failure of a branch is not inferred from a timeout.

The proof uses the published general upper bound only to reduce the extremal question to excluding size \(12\). No assertion is made for larger alphabets or different lengths.
