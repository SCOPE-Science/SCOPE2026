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

# Reproducibility and proof checks

Run `python3 artifacts/verify.py` using Python 3's standard library. The captured deterministic output is `artifacts/verification_output.txt`.

The direct simulator enumerates every state with \(0\le x_v<2\deg(v)\) for \(2\le n\le10\), and applies two actual firing updates to select primitive two-cycles, dividing phase counts by two. The restriction is exhaustive **for periodic two-cycle states only**, because the proof's explicit chip intervals imply it. It covers 349,524 candidate states, not all nonnegative starting configurations. An independent edge-cut/offset implementation, polynomial recurrence and binomial coefficient expansion agree on every tested size. For \(n\le12\) the cut enumeration was also compared, and recurrence/binomial/Pell/palindrome/mean checks continue through \(n\le40\).

The connected-Laplacian firing-count argument, local threshold interval derivation and path transfer identity are given in `RESULT.md`. The Gaussian law follows from analytic dominance and differentiated log moment-generating functions; it is not inferred from the finite enumerations. The sample script does not certify the infinite proof, literature priority, or independent validation. Historical equivalent enumerations cannot be excluded solely by searching, and the 1992 tree paper was not fully inspected.
