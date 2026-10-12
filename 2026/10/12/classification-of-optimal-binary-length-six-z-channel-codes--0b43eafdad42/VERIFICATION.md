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

The finite verification is implemented in `verify.py` using only the Python standard library. It reconstructs all \(64\) binary words and compares two definitions of pair compatibility on every unordered pair: asymmetric distance at least \(2\), and disjoint one-error Z-balls.

It then enumerates every maximal clique in the compatibility graph, independently enumerates every twelve-clique and checks that no thirteen-clique exists, generates all codes from the \(15\) perfect matchings and two transversal parity classes, and checks equality of the two resulting sets of maxima.

For every maximum it verifies the weight distribution \((1,0,3,4,3,0,1)\), matching/complement structure, and exactly \(16\) free points. Finally it applies all \(720\) coordinate permutations to the published length-six example and verifies that the orbit is exactly the full set of \(30\) maxima, with stabilizer order \(24\).

The successful replay output is stored verbatim in `verification_output.txt`. The computation is exhaustive only for binary length \(6\) and one Z-channel error; no claim is made for larger parameters.
