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

# Verification and limits

`verification/verify.py` is a standalone Python program using only the standard library. Run it from the directory containing that script; its expected complete stdout is in `verification/expected_output.txt`.

For width five, it enumerates the 3,481 augmented allowed faces, constructs the quotient's 696 nonempty orbit cells, checks all integer compositions of consecutive cellular differentials, and computes boundary ranks over primes two, five and seven. Over five it obtains Betti dimensions \((1,1,1,1,1,19)\), including mod-five classes in degrees two and four arising from torsion in the preceding degrees. Over two and seven it obtains \((1,0,0,0,0,19)\). It also verifies all nonidentity translations act freely for widths five and seven, and checks explicit fixed half-turn faces for even widths four, six and eight.

The finite computer calculation is not an infinite proof or a Smith normal form of all widths. The proof's external input is the cited multiple-chessboard connectivity theorem, which was inspected at its primary theorem statement. The remaining general steps are explicit orbit arguments, finite inclusion-exclusion, Armstrong's theorem, and ordinary covering homology. Independent audit was not performed.
