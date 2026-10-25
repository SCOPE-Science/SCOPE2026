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

The proof uses the exact coupled quadratic Laplace transform and a finite recurrence of derivatives at the origin. The positivity criterion follows from the Neumann-series zero pattern of a nonsingular \(M\)-matrix inverse, an induction on labeled derivatives, and the positive Lévy-measure identity for mixed cumulants. It is valid at every integer order, not just those checked computationally.

The executable `cumulant_checker.py` requires only Python 3 standard-library components. The stored `checker_output.txt` was produced by executing the included source file and reports 1,588 exact arithmetic assertions. These checks cover every 6-type target word of length at most four, and an independent formal-power-series reconstruction through degree four. This is finite corroboration, not an exhaustive computational proof for arbitrary dimension or order.

The assumptions \(B\) nonsingular \(M\), \(\eta>0\), \(t>0\) are indispensable to the stated strict positivity equivalence. Historical priority is not independently validated; a relevant general first-passage source was available at abstract level but not in full text.
