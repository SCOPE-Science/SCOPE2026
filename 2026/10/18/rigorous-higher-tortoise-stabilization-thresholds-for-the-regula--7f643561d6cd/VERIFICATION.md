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
# Verification and proof boundary

`verify.py` uses Python 3 standard-library functions only. Run `python verify.py` in the same directory as `certificate.json`. The program recomputes all factors from the complete two-adic residue templates, their iterated tortoise images, minimum one-counts, and collision classes; it checks byte-equivalent canonical JSON and reproduces `verification_output.txt`.

For \(k=2,3,4,5\), the last-collision lengths are \(12,13,24,25\), where the respective factor-to-image counts are \(48\to46\), \(52\to49\), \(96\to94\), and \(100\to98\). The next lengths \(13,14,25,26\) have injective counts \(52\to52\), \(56\to56\), \(100\to100\), and \(104\to104\), with minimum respective one-counts \(5,5,10,11\).

The enumeration is exhaustive because the paperfolding bit at any index not divisible by \(2^r\) is determined by its residue modulo \(2^{r+1}\), and every length at most \(2^r\) factor contains at most one exceptional index. Every exceptional bit choice occurs somewhere on the same start residue class. The prefix-lifting lemma in `RESULT.md`, proved without computation, upgrades the injective rows to all longer factor lengths. A separate 16,384-bit-prefix check in the program is merely an implementation cross-check, not a premise for infinity.

This document records same-model reproducibility evidence only. No independent audit or external scientific certification has been performed.
