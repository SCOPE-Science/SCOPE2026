---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The universal proof is analytic. Its critical steps were checked independently within the package construction:

1. For \(n=N-1\), the hypergeometric law is supported on \(\{L-1,L\}\), with masses \(L/N\) and \((N-L)/N\).
2. The matching \(\operatorname{Bin}(N-1,L/N)\) masses at both of those points equal \(\binom NL(L/N)^L((N-L)/N)^{N-L}\).
3. The half-range density-ratio expression and its consecutive quotient were algebraically simplified exactly.
4. The two threshold comparisons reduce to the exact positive quantities \(2k+1\) and \((k+1)/(2k^2(3k+2)^2)\).
5. `verify.py` replays exact rational comparisons for every \(3\le N\le300\), checks the adjacent-sign iff criterion wherever applicable, and verifies the predicted maximizing compositions.

Replay command: `python verify.py`

Expected output: `VERIFY_OK N=3..300`

The finite replay is a regression check only. It does not certify the infinite theorem; the quantified result rests on the analytic inequalities in `RESULT.md`.
