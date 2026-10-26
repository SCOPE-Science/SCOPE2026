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

The `verify.py` program runs on Python 3 without external dependencies. Its direct method enumerates the complete diagonal-choice space for each sunlet \(S_n\) with \(3\le n\le8\), reducing the **original** \(2n\)-by-\(2n\) adjacency matrices by binary Gaussian elimination. The independent reduced method enumerates all retained cycle subsets and diagonal bits through \(n=10\). A separate polynomial-convolution implementation extracts the rational formula coefficients through \(n=12\). All comparisons include coefficient counts, normalization to \(4^n\), and the stated least rank.

The recorded deterministic result in `verify_output.txt` ends with `VERIFY_OK`. The script verifies finitely many cases, not an infinite quantified theorem. The proof in `RESULT.md` establishes all orders, including the distinction between the exceptional triangle and longer cycles.
