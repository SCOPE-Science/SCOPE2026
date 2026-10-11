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

From \(J_5(n)=(n/\operatorname{rad}n)^5\prod_{p\mid n}(p^5-1)\), any collision gives a nonzero signed support vector in \(\{-1,0,1\}\) whose valuation coordinates vanish modulo \(5\). The deletion rule is therefore sound: if one active prime \(p\) is the unique active source of a valuation \(v_\ell(p^5-1)\not\equiv0\pmod5\), then its signed coefficient must be zero. I independently rechecked the actual certificate: it contains exactly all \(5133\) primes at most \(50000\); every displayed factor is prime under deterministic 64-bit Miller–Rabin, every factorization multiplies exactly to \(p^5-1\), every witness is unique in its active round, and rounds \(5074,51,5,3\) exhaust the active set. Thus no collision can have all prime divisors at most \(50000\).

## originality

PASS

Fu's primary paper supplies the signed valuation reduction and the recursive elimination algorithm for general \(k\), but its theorem treats noninjectivity only for \(k=3,4,6\), and its quantitative cutoff results are for those exponents. The inspected full ten-page paper contains no \(k=5\) support bound. The present contribution is therefore not a new method, but an exact certified application to the untreated \(J_5\) case through all primes at most \(50000\). Current Resultary and web searches located no stronger \(J_5\) support cutoff.

## value

PASS

The fifth Jordan totient is a natural untreated case in the same collision program, and the certified statement excludes every collision supported on more than five thousand small primes. This is a meaningful finite obstruction that materially narrows any future collision search; its value does not depend on inventing a new elimination algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
