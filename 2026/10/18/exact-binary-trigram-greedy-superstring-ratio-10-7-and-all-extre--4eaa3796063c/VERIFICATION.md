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

Run `python3 verify.py` from a directory containing the accompanying files. Only the Python standard library is needed. The exact output for the run is in `verification_output.txt`.

The proof certificate visits all 255 nonempty subsets of the eight binary three-letter words; exhaustive enumeration of 2040 possible superstrings of lengths three through ten gives exact optimum lengths. The linear word `0001011100` covers all eight words, so no optimal answer lies beyond the search range. A separately coded Hamiltonian-path dynamic program agrees for every subset. All maximum-overlap ordered choices are recursively explored with no branch cutoffs, using exact integer values and memoization; 7405 canonical states were visited. Rational comparisons yield the displayed \(10/7\) bound and exactly four extremizers, plus the complete cardinality profile. This is finite exhaustive evidence, not an inference for larger alphabets or strings.

Scientific limitations: the related 2026 paper could not be inspected in full, and independent external scientific audit is not performed. No human or formal-proof certification is asserted.
