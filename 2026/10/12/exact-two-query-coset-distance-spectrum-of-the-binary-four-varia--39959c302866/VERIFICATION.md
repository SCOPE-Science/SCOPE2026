---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read immutable RESULT.md and verify.cpp. Affine [16,5,8] code has 11 parity-check rows from pivot coordinates 0,1,2,4,8; pair of 11-bit syndromes labels every ordered coset pair. At each of 16 positions two binary errors give precisely four transitions of minimum joint union-support: D_{j+1}(s)=min(D_j(s),1+D_j(s+e_j),1+D_j(s+f_j),1+D_j(s+e_j+f_j)). This inductive recurrence is exhaustive on 2^22 syndromes. Independently implemented recurrence in C++17, executed all 4,194,304 states and recovered exact histogram (1,48,1080,15120,144585,858144,2359602,798000,17388,336), first distance-nine syndrome=(373,207), total 4194304 and radius nine. First four counts also equal binom(16,j)3^j (j=0..3) because minimum codeword support eight, independent consistency check. This proves the finite fixed-code statement, NOT an infinite Reed–Muller family or orbit classification.

## originality

PASS

Elimelech–Wei–Schwartz (arXiv:2107.09902) Table I reports known exact order extremes and bounds for intermediate Reed–Muller generalized covering radii; r=1,m=4 is not an exact case in the table. The submitted much stronger invariant is the ENTIRE two-row ordered-coset distance histogram, not merely radius. Ordinary RM(1,4) deep-hole/weight-enumerator results are single-row, and a binary-to-F4 scalar-extension restatement does not make published scalar one-row distributions imply all ten joint coefficients. Resultary covering-radius findings searched and nearest hits for unrelated BCH families did not dominate this code. No matching full spectrum found within inspected material; novelty is best-of-knowledge, not proof from failed search.

## value

PASS

Natural generalized covering-radius invariant measures minimum joint support for simultaneous two-query retrieval; its complete fixed-code distribution gives farthest-coset counts and all distance layers, independently reusable as an exact benchmark. Enumeration is exhaustive over a canonical small natural Reed–Muller instance with 4,194,304 ordered cosets, not an arbitrary slice or incomplete census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
