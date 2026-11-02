---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every k>=1 and S>=1, B(N+a)/(B(N)B(a)) is a ratio of 3-adic units 1+3^k Z_3 when v3(N)>=k+floor(log_3(2a)); this yields separated-block multiplicativity modulo 3^k. For N=3^R, the b_R=2 prod_{i=1}^{N-1}(1+N/i) expansion has exactly the two exceptional modulo-9 factors at i=N/3,2N/3, whose product is 10=1(mod9), so b_R=2(mod9) and by LTE has exact order 2*3^(k-1) modulo 3^k. Infinite pigeonhole yields a repeating unit u among b_R residues along unbounded exponents; spaced choices yield B(A_t+sum 3^Ri)=B(A_t)u^j mod3^k. The seed A_t=3^S(3^t+1)/2 for t>=1 (or 3^S for t=0) has exactly t ternary carries, so v3(B(A_t))=t; multiplication by u^j traverses all valuation-t units (0<=t<k), while t=k supplies zero. For each fixed residue, infinitely many j in a suitable congruence class and arbitrarily large spaced exponents supply distinct indices. If S>=k, C_{N-1}=B(N)/(2(2N-1))=-B(N)/2 mod3^k for constructed N, transferring all classes. Independent exact checks: seeds t<=8, primitive roots R<=8 and k<=6, 825 separated-block instances, all classes modulo 3,9,27,81,243 among first 30000 Catalans. Finite checks corroborate only; analytical argument proves all k.

## originality

PASS

Best-of-knowledge original: proves the all-exponent Catalan 3-adic density and infinitely many witnesses, answering the explicitly stated Rowland--Yassawi Open Question 3.6. Krattenthaler--Muller give 3-power coefficient formulas, Burns gives prime-modulus surjectivity, and Rampersad--Shallit analyze prime-modulus Catalan automata; none of their inspected statements proves the uniform 3^k surjectivity. Barat--Grabner equidistribution concerns the full triangular Pascal array (n,j), not the constrained central diagonal (2N,N); Sun--Zhang concerns fixed lower binomial index. Unindexed implicit coverage remains a historical-priority risk, not a proof of novelty.

## value

PASS

This is the exact published forbidden-residue question for Catalan numbers modulo every power of 3, not a single finite census or routine fixed-modulus calculation. It proves a strong complete natural classification: every 3-adic residue neighbourhood is hit infinitely often, with a reusable separated-block and primitive-root mechanism. The precise mathematical gap was explicitly recorded as Open Question 3.6 by Rowland--Yassawi; first-index bounds or density are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
