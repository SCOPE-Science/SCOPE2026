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

Rogers Theorem 3.1, Eq. (3.4), gives the transformed series for the defining Domb numbers. Its hypergeometric coefficients and extraction of [z^(n-2k)](1-4z)^(-3k-1) give the integer factors in (1). Applying v2(m!)=m-s2(m) gives summand valuation 2(n-2k)+4s2(k)+s2(n-2k)-s2(n+k). Set n=2^r-1 and k=2^(r-1)-1-j. For k>0, n+k=2^r+[(2^(r-1)-1)-(j+1)], whence s2(n+k)=r-s2(j+1) by bitwise complement. Equation (3) follows; j=0 gives 3r and j>=1 costs at least j-1+s2(j+1)>=1 more. At k=0 the valuation is 2^(r+1)-2>3r: the inequality holds at r=3 and its gap grows. Only the upper endpoint summand survives as an odd integer after division by 2^(3r). Direct computation gives D_1=4 and D_3=256, confirming the exceptional valuations. Replay: python3 /workspace/reproduction/frozen_checks.py 1, using the classical exact three-term recurrence checked against selected defining-sum terms, corroborated Mersenne valuations for r=1 through 12. This finite check is not a proof of the identity or of the valuation law. The frozen checker was read, not executed; its Python 3.8+ compatibility note is overly broad because int.bit_count needs Python 3.10+. This documentation mismatch does not affect the proof or the available reproducibility.

## originality

PASS

The supported distinct result is the uniform sharp Mersenne valuation and its unique-minimal-summand proof, not the Domb sequence, transformed sum or general binary lower bound. No equivalent was found in the relevant statements inspected; priority is a best-of-knowledge assessment.

## value

PASS

The all-ones indices are a natural infinite family distinguished by the adjacent-one exceptions to the existing digit-sum bound. An exact unbounded divisibility threshold for a classical lattice-walk and Apéry-like sequence is useful arithmetic information beyond low-modulus congruences. Single-term domination explains the answer, without claiming a valuation classification at arbitrary indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
