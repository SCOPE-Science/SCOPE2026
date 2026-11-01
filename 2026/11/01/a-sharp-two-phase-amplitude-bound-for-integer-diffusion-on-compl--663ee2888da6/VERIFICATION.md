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

# Verification of the sharp complete-bipartite diffusion amplitude

Run `python3 verify_diffusion_range.py` with the Python standard library. The supplied `verification_output.txt` is the output from an actual execution of that exact source file, and the final line is `BIPARTITE_DIFFUSION_WIDTH_ALL_CHECKS_PASSED`.

The checker tests explicit strict-reversal two-cycles for every \((a,b)\in\{2,\ldots,14\}^2\), requiring the second step to return exactly and the two-phase amplitude to equal \(a+b+\max(a,b)-2\). Separately, it exhausts independent within-shore label-sorted candidates in a **finite** alphabet up to two larger than the proposed sharp width on five small bicliques. It recomputes both integer steps and rejects any nonrecurrent candidate; all qualifying candidates satisfy the bound. The test totals, scope, and sample maximal states appear in `verification_output.txt`.

Those enumerations do not certify infinitely many graph sizes or unbounded initial integer labels. The all-size proof is the algebraic edge-reversal lemma, the cross-shore gap bound, the phase-normalized case analysis, and a strict-reversal extremizer in `RESULT.md`. The checker is independent executable corroboration rather than an external proof certificate. Independent audit has not been performed.
