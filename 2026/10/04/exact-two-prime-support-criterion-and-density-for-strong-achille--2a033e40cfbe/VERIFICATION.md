---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(n=2^ap^b\), powerfulness and non-perfect-power reduce to \(a,b\ge2\) and \(\gcd(a,b)=1\). The totient has exponent vector \((a+t-1,b-1,c_1,\ldots,c_r)\), so its Achilles condition gives exactly \(b\ge3\), all \(c_j\ge2\), and the second gcd condition. For fixed \(p\), exponent pairs lie in a logarithmic triangle. At a prime \(\ell\nmid g\), only the residue pair \((0,0)\) is excluded; at \(\ell\mid g\), the distinct pair \((1-t,1)\) is additionally excluded, producing the stated Euler product. When the odd part is absent, both exclusions occur at every prime. A fresh computation of the universal product through primes below \(100000\) gave \(0.322634616605\), consistent with the submitted constant.

## originality

PASS

The exponent-vector criterion is standard and is not credited as new. The originality-bearing part is the fixed-support existence criterion together with the support-wise \((\log X)^2\) asymptotic and explicit Euler-product constant. OEIS A194085 and Project Euler provide the sequence, definitions, benchmark counts and programs, while the inspected detailed solution explains general exponent bookkeeping; none states a fixed-prime support density. Resultary likewise found no stronger strong-Achilles support-wise theorem.

## value

PASS

For a fixed support, exponent space is the natural way to analyze Achilles-type conditions. The theorem gives a complete existence criterion and a quantitative infinitude law with an explicit density constant, replacing raw sequence enumeration by a closed support-wise asymptotic. That is a natural classification/counting result for the stated arithmetic object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
