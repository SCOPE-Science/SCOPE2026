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

The accompanying `verify.py` uses only the Python standard library and rebuilds the result from the finite universe of ternary length-three words.

It performs these checks:

1. Enumerates every one-, two-, and three-word coalition inside a candidate and encodes its descendant as three coordinate symbol masks. Distinct masks are therefore exactly the separability condition.
2. Tests all \(\binom{27}{6}=296010\) six-word subsets and obtains exactly \(135\) valid codes.
3. Tests all \(\binom{27}{7}=888030\) seven-word subsets and obtains zero valid codes. Since separability is hereditary, this excludes every code of size at least \(7\).
4. Traverses the complete group of coordinate permutations and independent coordinatewise symbol permutations, of order \(1296\), on all \(135\) maxima. It obtains exactly two orbits, of sizes \(27\) and \(108\), and hence stabilizer orders \(48\) and \(12\).
5. Checks the two stated canonical representatives, their coordinate multiplicity profiles, and their pairwise Hamming-distance distributions.

Reproduction command: `python3 verify.py classification.json`.

Expected output: `VERIFY_OK maximum=6 labeled_maxima=135 orbits=2 orbit_sizes=27,108 stabilizers=48,12 checked6=296010 checked7=888030`.

The proof is exhaustive only for \(Q=\{0,1,2\}\), length \(3\), and coalition bound \(3\). It is not evidence for an infinite family or for other alphabet sizes.
