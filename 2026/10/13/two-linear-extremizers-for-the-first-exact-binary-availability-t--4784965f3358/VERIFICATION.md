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
`artifacts/verify.py` uses only the Python standard library.

It enumerates all
\[
\binom{15}{7}=6435
\]
multiplicity vectors for the eight possible columns of a \(3\times8\) binary generator matrix. Each vector is tested for rank \(3\), global minimum distance at least \(4\), and all-symbol \((2,2,2)\)-availability.

For availability, every helper set of size \(1\) or \(2\) is tested by direct enumeration of the corresponding punctured local linear code, and two disjoint valid helper sets are required at every coordinate.

Exactly \(28\) vectors survive. All \(168\) elements of \(\operatorname{GL}(3,2)\) are then generated, giving exactly two survivor orbits of sizes \(21\) and \(7\).

For the two representatives, the verifier recomputes the Hamming weight distributions, all seven two-dimensional subcode supports, generalized Hamming weights, linear-column stabilizers, and coordinate-permutation automorphism orders.

Successful replay prints `VERIFY_OK`.
