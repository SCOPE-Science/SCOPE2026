---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For U unitary, direct Frobenius inner product gives ||U-U_:j U_i:/U_ij||_F^2=n-2+|U_ij|^-2. Under strict threshold t>sqrt(b_n), event is |U_ij|^2<delta, with delta=1/[n(t^2-1)+2]<min(1/n,4/n^2). Each row needs a large entry, hence strictly fewer than n(n-1)*delta/n probability. A complex phase rank-one update of I with flat unit vector produces n(n-1) offdiagonal squared amplitudes q↑delta, yielding exact supremum (n-1)delta, not attained; tail constant (n-1)/n. Independently recomputed pivot norms, sampled probabilities, and unitarity for 15 (n,t) values.

## originality

PASS

Best-of-knowledge PASS: original RPLU work proves expectation/Gram error bounds and a dense-unitary second moment; the present strict high-threshold worst-case probability and constructive phase family are stronger distributional and minimax assertions. Follow-up Divan--Gilles full text was unavailable despite OA/arXiv attempts and authorized institutional access; possible overlap is a material risk, not an automatic O failure.

## value

PASS

Determines an exact high-confidence failure probability for a natural randomized low-rank cross update on perfectly conditioned matrices, with dimension-dependent minimax constant and explicit near-extremizing unitaries; a justified exact risk functional beyond expectation bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
