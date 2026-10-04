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

The general theorem is proof-based. A finite checker is included only as a consistency test.

For the \(n\)-element chain, the proof verifies directly that each incoming column of an \(\mathbf{AP}\)-compatible doxastic relation is a downset of \(\{0,\ldots,j\}\), hence an initial segment. The \(j\)-th column therefore has exactly \(j+2\) possibilities, independently of the other columns.

The founded count is checked from the literal basic-frame definition: one edge \(vRt\) suffices at every state \(s\) using \(u=\max\{s,v\}\), and the empty relation fails.

The epistemic count is checked from the literal visionary condition and \(\mathbf{AP}\)-compatibility: visionaryness becomes seriality. Doxasticity leaves the top state only the top as a possible successor, so seriality is equivalent to the top loop. AP-compatibility then fills the entire top incoming column. Balbiani's general theorem identifies visionary and futuristic on doxastic frames.

`verify.py` exhaustively enumerates every binary relation for \(1\le n\le4\), applies the definitions literally, and checks the predicted counts. It prints `VERIFY_OK`.

## Limits

The finite checker does not prove the infinite family; it corroborates the closed-form proof. The theorem applies to fixed finite chains, not arbitrary preorders.
