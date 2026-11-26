---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Each complementary block supplies one arbitrary bit; one extra zero cannot fit, so the shortest absent length is exactly the number of blocks plus one. In an embedding of that extra-length target, the block index minus the target index starts nonnegative, ends negative, and drops by at most one per step. At its first crossing, two adjacent letters occupy both positions of the block with the same index. Conversely that double match allows all remaining letters to be placed singly. This proves the exact local exclusion rule and the two shear matrices. Complementation conjugates by the swap J, so P_{j+1}=(P_j J)^2; trace s_j and determinant -1 of P_j J give d_{j+1}=s_j^2+2 and s_{j+1}=s_j d_j, for diagonal and off-diagonal sums d_j,s_j. Thus s_j=a_j, H_m=d_{m-1}+s_{m-1}, including the separate H_1=3. The logs b_j=log(a_j a_{j+1}) obey b_{j+1}=2 b_j+log(1+2/a_j^2); the normalized sums converge to L by a geometric bound. The normalized individual log obeys an affine contraction of slope -1/2 with limiting fixed point L/3. The diagonal sums have the same log limit, and the log of their sum differs from the maximum by at most log 2. Hence the rate and exponential-fraction assertion follow; L<=log 6 supplies a rigorous bound below 2. An independent greedy-state calculation reproduced counts through m=9 and a high-precision series evaluation confirmed the displayed digits of rho.

## originality

PASS

Arch structure, local transfer counting and the binary extremal bound are prior. A distinct indexed Thue–Morse record gives exactly the same integer recurrence in different variables, so the recurrence is not additional content relative to that record. Its listed date is later, which does not support priority for it; the assessment does not infer authorship or priority from catalogue metadata. The supported distinction even against that exact overlap is the explicit exponential base with a convergence formula for the fixed dyadic family. The earlier inspected methods do not determine that rate.

## value

PASS

Finite Thue–Morse prefixes are a natural nonperiodic substitution family and shortest absence is the onset of failure of scattered universality. The exact base, approximately 1.568665 per complementary block, quantifies that failure relative both to all binary targets and to the extremal binary growth ceiling. The iteration provides counts without constructing the exponentially long prefix, but the scientific value against the equivalent recurrence is the exact rate and its derivation, not a repackaging of the same fast count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
