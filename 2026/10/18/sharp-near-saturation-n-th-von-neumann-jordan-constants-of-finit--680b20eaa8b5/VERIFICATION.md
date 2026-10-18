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

# Verification notes

A standard-library exact-rational checker enumerates every subset of \(m\) represented projective sign rows for each \(2\le n\le4\) and \(2^{n-2}\le m\le2^{n-1}\). Three test weight vectors are used in each instance: equal weights, a half-size final weight, and a doubled first weight. All 30 exact-fraction comparisons agree with the sharp fixed-length formula. This enumeration does not establish the all-\(n\) theorem.

The mathematical proof uses a separate exhaustive-in-structure argument: there are exactly \(2^{n-1}\) projective sign classes; with at most half absent, choose absent classes in distinct minimal-coordinate flip pairs. Thus the optimal expectation has only two possible magnitudes and is valid for all admissible integer parameters.

For the five-dimensional four-input example, the proposed minimum weight \(q=\sqrt{19}-4\) satisfies \(q^2+8q-3=0\), and the direct quotient simplifies to \(2+\sqrt{19}/4\). The included checker is a finite corroboration and requires no external package. Independent audit is not performed. The unavailable full PDF of the foundational 1998 paper is a bibliographic limitation.
