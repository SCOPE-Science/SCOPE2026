---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The greedy Zeckendorf recurrence s(F_k+t)=1+s(t) for 0<=t<F_(k-1), together with induction on Fibonacci indices, yields exact boundary arrays for k=2r: s(F_k−4..−1)=(r−1,r−2,r−1,r−1) and k=2r+1: (r−1,r−1,r−1,r), and above a boundary s(F_k+j)=(1,2,2,2,3) for j=0..4. Their four crossing-offset cases close a strong induction proving: when s(n),s(n+2),s(n+4) have the same parity, an adjacent pair are equal. For odd Zeckendorf–Niven triples the summand counts must be odd divisors; equal adjacent counts divide 2, so equal 1 and the two numbers are Fibonacci values 2 apart, forcing candidates n=1,3. n3 fails because s(7)=2∤7; n1 yields (1,3,5). Independent greedy Zeckendorf implementation tested every n from 0 through 999999 for the parity lemma and all odd triples in that range, finding no parity violation and only n1; these tests are ancillary to the unrestricted induction.

## originality

PASS

Best-of-knowledge originality PASS: exact claim-versus-prior implication comparisons, including its aliases and stronger possible coverage, were made using identified primary material and the recorded semantic search. No decisive full-claim coverage was found; negative searches alone are not proof of novelty. The special-case known ingredients are explicitly credited.

## value

PASS

The Zeckendorf digit-sum divisibility analogue of Niven numbers is a natural digital-arithmetic object with known long step-two progressions. The result supplies a complete, sharply different odd-start length-three phenomenon and a reusable infinite parity-rigidity lemma, not merely a tabulation of a handful of values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
