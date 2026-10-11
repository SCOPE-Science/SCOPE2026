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

Equality of the deleted intensities gives, for every nonzero Fourier shift \(r\), the exact recurrence \(d_\ell+d_{\ell-r}=T\) for Gram-entry differences \(d_m\), with \(d_0=d_{-r}=0\). When \(n\) is odd every \(r\)-orbit has odd length. Solving the recurrence cycle-by-cycle and summing gives \(T=(n-1)T/2\), so for odd \(n\ge5\), \(T=0\) and every off-diagonal Fourier Gram entry agrees. The zero-shift equations similarly give the diagonal entries, hence the entire rank-one Gram matrices agree and the signals differ by a unimodular scalar. For even \(n\), two frequencies separated by the order-two character with coefficient pairs \((1,i)\) and \((1,-i)\) give an exact ambiguity; \(n=2,3\) fail separately. The inspected verifier exactly checks the associated linear systems on representative orders but is not used as the infinite proof.

## originality

PASS

Bartusel--Führ--Oussa establish the prime-field deletion observation and, in Remark 6.12, explicitly ask whether it extends from prime order to general cyclic groups. The audited result answers that question with a sharp parity classification: every odd composite order at least five works, while every even order has a uniform order-two obstruction. Resultary and broader phase-retrieval searches found no intervening theorem resolving this cyclic question.

## value

PASS

The theorem completely answers an explicit source question and reveals the actual arithmetic boundary: oddness rather than primality. The even-order ambiguity is structural and the odd composite proof handles genuinely new shift-orbit geometry, making this a natural complete classification rather than a small extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
