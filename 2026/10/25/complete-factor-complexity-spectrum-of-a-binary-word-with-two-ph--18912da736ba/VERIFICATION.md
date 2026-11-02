---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For W=(01)^a0(01)^b0(01)^c (a,b,c>=1), partition its distinct contiguous factors by the number 0,1,2 of the marked 00 defects. No-defect factors are alternating from the maximum-length run T=max(A,B,C), contributing q_T(l). Single-defect factors are bijective with offset pairs in rectangles A×B and B×C, except identical factors in their intersection min(A,B)×min(B,C), giving diagonal H terms by inclusion-exclusion. Two-defect factors have fixed interdefect corridor length B+2 and extension rectangle A×C. This proves every-length formula and summed total 2T-1+AB+BC-min(A,B)min(B,C)+AC. Direct independent enumeration verified all lengths for all 343 triples 1<=a,b,c<=7. Finite checks only corroborate exact counting bijections.

## originality

PASS

The exact full all-length complexity for this three-parameter two-defect word is not implied by general factor complexity bounds from Prezza or unrelated finite-string reconstruction theorems. Resultary published word-spectrum/multispectrum records concern different equivalence-class or inverse-string observables. No matching full two-defect spectrum was found. Primary Prezza full-text access was incomplete, so only the accessible abstract and theorem metadata are used for a bounded comparison; no claim that its whole document was exhaustively excluded.

## value

PASS

The word is a motivated finite perturbation of a periodic word with exactly two phase defects; factor complexity is a standard complete discrete invariant. The precise overlap subtraction is not recovered by adding two single-defect contributions and records interaction between the defects. A three-parameter all-length exact spectrum and total answer may serve repetitive-string enumeration/attractor benchmarks rather than an arbitrary tiny-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
