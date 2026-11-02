---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed prime-power multiplicativity and exact cancellation p^(2^k)+1=q Q_k(p). For k=1 integrality forces p-1|2, so p=2,3 and q=5. At k=2, remainder (x-1)^2+1 lies strictly between 0 and Q=x^2+x-1. At k>=3 put U=x^(2^(k-2)), V=sum_{j=0}^{k-3}x^(2^j). Q=U^2+U+V-1 and U^4+1 congruent (U+V-1)^2+1 mod Q. The difference R-Q=U(2V-3)+(V-1)(V-2)+1>0. The induction U>=3(V-2) holds at k=3 since x^2>=3(x-2), and extends because U^2>=4U>=3(U+V-2); it yields 2Q-R>=2U^2/9>0. Thus Q<R<2Q uniformly. New independent arbitrary-precision calculation verified 343 (x,k) cases x=2..50, k=2..8 and 630 distinct-prime pair comparisons, finding only the two stated solutions. The interval induction is the infinite proof.

## originality

PASS

Existing work records the motivating equality and examples and a published finite classification of exponents a<=49. Because 2^k<=49 only for k<=5, its exact finite classification does not imply exclusion of k>=6, whereas the integer-base modular lemma does. An older equivalent lacunary polynomial divisibility lemma remains a priority risk.

## value

PASS

The all-k impossibility theorem resolves a natural infinite exponent ray in an open divisor-function comparison problem, with a stronger prime-independent algebraic obstruction; it is not a bounded example search or reformulation of OEIS terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
