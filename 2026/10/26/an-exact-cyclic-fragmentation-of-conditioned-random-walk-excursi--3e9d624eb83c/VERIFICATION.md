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
# Mathematical verification record

The proof establishes the all-size result by primitive-excursion enumeration, Catalan convolution, an explicitly normalized size-biased splitting kernel, a cyclic preimage count, and majorization. Every step is in `RESULT.md`.

The standalone standard-library checker `CHECK.py` confirms by rational arithmetic all compositions and all successive return levels for \(2\le n\le10\); independently it enumerates all signed walks of length \(2n\) for \(1\le n\le6\) to confirm the Catalan bridge weights, and checks that conditional quadratic expectation strictly falls. `CHECK_OUTPUT.txt` records its successful run. These finite tests are not an infinite proof.

The published Serlet conditioned-composition formula is prior work, not counted as original. Full-text comparison includes three works on discrete excursions and their ranked laws. The newly established all-\(n\) kernel and pathwise majorization are mathematical claims reviewed here only under the stated self-review status. No independent audit has been conducted.
