---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For distinct primes \(p<q\), \(\sigma(pq)=(p+1)(q+1)\). Cross-divisibility shows \(pq\) is Duffinian exactly when \(p\ne2\) and \(q\not\equiv-1\pmod p\). For exceptional odd \(p\le x^{1/3}\), Brun–Titchmarsh gives \(\pi(x/p;p,-1)\ll x/[p(p-1)\log x]\), summable over \(p\). For \(x^{1/3}<p<\sqrt{x}\), discarding the congruence and using \(\pi(x/p)\ll x/[p\log x]\) leaves a bounded reciprocal-prime sum over a fixed logarithmic interval. The \(p=2\) contribution is also \(O(x/\log x)\). Thus the exceptional set is \(O(x/\log x)\), negligible relative to Landau's \(x\log\log x/\log x\) count of squarefree semiprimes. The finite checker confirms only the local criterion, not the asymptotic proof.

## originality

PASS

Pollack's full 2011 paper studies the global distribution of \(\gcd(n,\sigma(n))\) and uses the same \(-1\) congruence/Brun–Titchmarsh mechanism, but full-document searches found no occurrence of 'semiprime' or 'Duffinian' and no theorem conditioning on the two-prime stratum. The global density behavior is qualitatively opposite to the audited relative-density-one result. OEIS and accessible historical metadata list Duffinian numbers but do not imply the semiprime asymptotic. Best-of-knowledge, the thin-stratum theorem is not covered.

## value

PASS

The theorem exposes a genuine density reversal: a globally sparse coprimality property becomes generic on the natural squarefree-semiprime stratum. The exact local criterion and quantitative \(O(x/\log x)\) exceptional bound make this a motivated analytic-number-theory fact rather than a finite sequence observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
