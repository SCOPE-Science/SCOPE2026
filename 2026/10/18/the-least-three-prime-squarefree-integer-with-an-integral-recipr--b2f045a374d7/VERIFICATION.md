---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS. The grouping identity H(n)=(1/n)prod_{q^e||n}(q^(2e+1)+1)/(q+1) specializes to prod F(q)/(pqr). Since F(q)=q^2-q+1 ≡1 mod q, integrality gives each vertex an incoming edge; the minimal-counterexample descent on mutual divisibility of F excludes two-cycles, forcing a 3-cycle. Every smaller qualifying product <=N has smallest p^3<=N, first q|F(p), p*q*(p+1)<=N and last r|F(q), p<r<=N/(pq), F(r)≡0 mod p. Independent SymPy complete exact-factor scan yielded 7339 possible smallest primes, 1948 first edges, maximum intermediate q 19771363 and precisely one closing product N. Divisibility and exact H(N) verified. This is exhaustive by the cutoff argument, not unbounded experiment.

## originality

PASS

PASS best of knowledge. De Koninck–Letendre supplies the multiplicative criterion, counting bound and cycle method; an earlier least-vertex result already obtains 349 and the same three primes, but does not imply minimal product: cycles beginning at larger p could have smaller q*r product. The new exhaustive product-bounded census eliminates that possibility. The displayed A317480 terms and published Resultary Phi_3 pair theorem do not imply this three-prime product minimum. Full preprint/older massive numerical catalogues could contain equivalent value; retained as residual risk.

## value

PASS

PASS. Three distinct prime factors are the first nontrivial squarefree support admitting a directed 3-cycle (2-cycles impossible). The least integral H(pqr) is a motivated exact extremal invariant of a natural arithmetic set and requires a nontrivial globally exhaustive product sieve; it is not deduced from the earlier least-vertex cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
