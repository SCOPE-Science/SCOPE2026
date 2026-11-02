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

# Verification of the mathematical claim

The reproducibility command is `python3 checker.py` in the directory containing this document and the complete standalone checker. Its successful terminal marker is `VERIFY_OK`.

The checker enumerates all \(2^{16}=65{,}536\) Boolean four-suffix feedback tables, retains precisely the 2,048 single-32-cycle cases, checks every retained cyclic word has 32 distinct five-bit windows, and compares those words with a completely separate order-four de Bruijn graph Euler-tour enumeration. Every one of the 2,048 words is processed by both a maximal-shift-equality detector and a definition-level minimal-period detector. All returned positioned run sets agree. Checks assert the exact profile counts, all total frequencies, and all period-by-length totals. Small binary and ternary independently constructed de Bruijn words are additionally used to check the symbolic low-period formula.

The general \(q\)-ary result is proved algebraically: de Bruijn uniformity, the Fine–Wilf primitive-root criterion, and two-sided extension boundaries are the critical steps. Computer experiments at finitely many orders are not claimed as a proof of this unbounded statement. The table for binary order five, on the other hand, is certified exhaustively because the feedback-to-cycle correspondence proves the finite search space complete.

Limitations: the finite table does not apply to other orders, and the formula for the total number of period-\(p\) runs requires \(2p+1\le n\). Bibliographic inspection does not amount to independent historical-priority certification, and no independent mathematical audit was performed.
