---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For even q, aligned index pairs (2j,2j+1) form successive cyclic letters with opposite parity, so centered height H_q(2j)≡0(mod 4) and H_q(t)≡t(mod 2). If an odd-order additive cube existed, the four endpoint heights would form an arithmetic progression with odd common difference Δ, but two even-index endpoints two steps apart would force 2Δ≡0(mod 4), contradiction. In q=4 each aligned four-letter block has integer sum 6, so H_4(4j)=0; also H_4(4j+2)=0 when u_4(j) is odd. For n=4v, take a=0; for n=4v+2, m=2v+1, choose h sufficiently large with 3h−s_4(m−1) odd, let k=4^h−m, a=4(k−v). The base-four complement identity makes u_4(k) odd and u_4(k+m)=1, forcing all four endpoint heights 0 and block sums exactly 3n/2. Independent literal-digit checks confirmed every even witness n=2..160 and odd-order impossibility n<37 over 1100-position prefixes for even q=2,4,6,8,10; symbolic proof, not finite tests, covers the infinitely many orders and bases.

## originality

PASS

Published additive-complexity and generalized Thue-Morse results establish bounded complexity, some unspecified power occurrences and Parikh-vector/Abelian data; they do not determine the exact integer additive-cube order spectrum for q=4 nor the parity obstruction over every even base. The digit complement witness is a new concrete constructive spectrum compared with these inspected statements.

## value

PASS

A full order spectrum for a standard canonical automatic word is a natural combinatorics-on-words invariant: the universal odd-order obstruction and explicit witnesses for every even order quantify exactly when equal-sum triples occur. The base-four if-and-only-if and even-alphabet parity mechanism are structural, not a textbook Parikh-vector recount or an arbitrary slice of positions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
