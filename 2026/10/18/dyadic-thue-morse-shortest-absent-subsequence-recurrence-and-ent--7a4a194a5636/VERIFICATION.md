---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

This assessment is for repairs/4/RESULT.md. For k=2^(m-1), the k binary blocks each contain both symbols, so all length-k strings embed and k+1 zeros do not. The first block that greedily consumes two symbols, if any, does so on the original target pair at that block index; one double consumption suffices for a length-(k+1) target to embed. Hence the two allowed-pair matrices count strings, not embeddings. Their product P_r satisfies P_(r+1)=(P_r J)^2; P_r J has determinant -1, so Cayley–Hamilton proves the two updates and the entry sum is s_r+t_r. For the repaired asymptotic, log2(s_r) obeys the forced linear recurrence with roots 2 and -1, and the proof retains both modes. The bound eps_j <= (2/ln 2)*4^(-j) controls each omitted tail by O(4^(-r)) after scaling. The initial correction cancels because eps_0-eps_1=1; the strictly decreasing positive eps_j then give C>0 by pairing the remaining alternating terms. Taking first differences gives the second logarithm with correction -2*(-1)^r*C. Exponentiation and summation give the two displayed normalized limits, with odd minus even equal to (u-u^(-1))*(u+u^(-1)-1)>0. Independent direct target enumeration for m=1 through 5 matched 3,5,12,74,2666; bounded Decimal series evaluation with the geometric tail gives lambda between approximately 0.649537093097466276 and 0.649537093097466307. Those checks are finite corroboration only. The unchanged frozen count checker was inspected, not executed, and does not check either leading constant.

## originality

PASS

The PASS applies to the repaired parity-resolved asymptotic, not to the frozen recurrence claim. A separate catalog record states the exact same shortest length and count dynamics after a coordinate change. The classical trace map also covers the scalar trace recursion; the exponential rate is the escape exponent for its positive orbit, not a different constant under relabeling. The surviving result gives explicit, provably unequal parity multipliers for the shortest-absent-string count and controls the error to them. The inspected recurrence, trace-dynamics and Lyapunov statements do not give those multipliers.

## value

PASS

Quantifying the growth of the set of shortest nonembeddable strings in canonical Thue–Morse prefixes is an exact question about a natural object. The repaired result goes beyond computing a rate from an already available recurrence: even after removing the leading exponential, doubling the prefix alternates between provably different multiplicative constants. This rules out a single-constant equivalent, and the series and convergence rate make the parity effect quantitative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
