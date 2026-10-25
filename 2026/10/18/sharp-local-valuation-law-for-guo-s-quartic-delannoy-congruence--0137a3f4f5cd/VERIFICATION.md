---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: For every odd prime p the involution k->p-1-k and product formula for coefficients of D_k(x) give coefficientwise p-divisibility of the whole defect H_p. Exact alternating-sum identities give h_0=0, h_1=4p^3, and p^3|h_2,h_3 including p=3,5 exceptions. At x with v_p(x)=h>=1, degree>=4 terms have valuation >=1+4h>=h+4 and degrees 2,3 have >=3+2h, giving H_p(x) congruent 4p^3x mod p^(h+4); odd p implies exact valuation h+3. Legendre symmetry D_k(-1-x)=(-1)^k D_k(x), and the even fourth power plus invariance of x(x+1),(2x+1)^2, establish the reflection branch near -1. Independently evaluated exact defects for p=3,5,7,11,13 and depths 1..3 with unit multipliers and reflected values; checked exceptional low coefficients. x=0,-1 have H=0, not finite valuation. No statement at other residues.

## originality

PASS

PASS best-of-knowledge: Guo Theorem 1.4 already establishes global p^2 and Conjecture 5.2 proposes global p^3. This local result establishes a stronger exact order 3+h of the proposed defect at the two specific 0/-1 neighborhoods, with leading term. Those are not supplied by the cited general p^2 or conjectured p^3 statements. Similar later Delannoy supercongruences were checked for their sums/exponents and did not establish this valuation; unindexed local expansions remain a risk.

## value

PASS

PASS: Directly studies the defect of a named unproved p-adic congruence and establishes all-depth sharp behavior in natural residue neighborhoods x(x+1)=0 mod p. The leading unit controls optimal modulus and local nonvanishing, a motivated exact invariant rather than arbitrary modular spot checking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
