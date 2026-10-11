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

The Stewart--Sierpiński criterion specializes an exact-two-prime practical integer to \(2^a p^b\) with odd prime \(p\le 2^{a+1}\). Splitting the \(b=1\) count at \(m=\lfloor(\log_2 X-1)/2\rfloor\) gives two dyadic prime sums. Uniform prime-number-theorem estimates on \(1\le s<4\) yield leading terms \(4\,2^m/(m\log 2)\) and \(2s\,2^m/(m\log 2)\). For \(b\ge2\), the admissible-prime bound \(p\le\min\{2^{a+1},(X2^{-a})^{1/2}\}\) gives \(O(X^{1/3}\log X)=o(\sqrt X/\log X)\). With \(\sqrt X=2^m\sqrt{2s}\) and \(\log X=2m\log2\,(1+o(1))\), this reconstructs \((8+4s)/\sqrt{2s}\), whose minimum is \(8\) at \(s=2\) and endpoint value is \(6\sqrt2\). The finite verifier was inspected only as corroboration, not as proof of the asymptotic.

## originality

PASS

The closest full-text source supplies the practical-number criterion and the global asymptotic for all practical numbers, not the exact-two-prime stratum. Targeted Resultary and literature searches using both \(\omega(n)=2\) and \(2^a p^b\) formulations found no prior phase-dependent \(\sqrt X/\log X\) law or the constants \(8\) and \(6\sqrt2\). The phase law requires a new moving dyadic split and a separate lower-order estimate for \(b\ge2\).

## value

PASS

Exact prime-support size is a natural arithmetic stratification. The theorem determines the full leading behavior of the two-prime stratum and reveals a genuine log-periodic/dyadic phase obstruction to a single limiting constant, with exact liminf and limsup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
