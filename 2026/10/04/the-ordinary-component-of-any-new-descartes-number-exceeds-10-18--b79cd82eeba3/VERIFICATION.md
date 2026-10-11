---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

From \(\sigma(q)(p+1)=2pq\) with odd \(p,q\), the right side has 2-adic valuation one. Since \(p+1\) is even, \(\sigma(q)\) must be odd, and the classical parity criterion makes odd \(q\) a square, say \(q=m^2\). Thus \(q\le10^{18}\) reduces exhaustively to odd \(m\le10^9\). The inspected C++ implementation segments that entire interval, factors each root by every prime needed up to the segment square-root, computes \(\sigma(m^2)\) exactly in 128-bit arithmetic, and tests the exact divisibility formula for the pseudo-prime. Its leftover-factor logic is sound because after division by all primes through \(\sqrt H\), any remainder is prime. The only reported solutions are \((q,p)=(1,1)\) and \((9018009,22021)\), with \(22021=19^2\cdot61\). The stored output confirms completion of the full range but is not used as the sole correctness evidence.

## originality

PASS

Tóth's complete four-page primary article was read and visually inspected. Its Theorem 1 and exhaustive computation stop at \(q>10^{12}\), and the conclusion explicitly proposes extending the computation above \(10^{12}\). A public 2023 computation reports no other odd example through \(10^{16}\) after the same square reduction. Targeted searches found no published \(10^{18}\) bound. The assigned result therefore advances the best located exact frontier by two orders of magnitude beyond that public computation and six beyond the peer-reviewed theorem.

## value

PASS

Descartes numbers are a long-standing surrogate for the odd-perfect-number problem, and the ordinary-component lower bound is the central quantitative output of the previous peer-reviewed computation. Extending that certified exclusion frontier to \(10^{18}\) is a meaningful finite cutoff, especially because the square reduction changes the computational scale by a square root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
