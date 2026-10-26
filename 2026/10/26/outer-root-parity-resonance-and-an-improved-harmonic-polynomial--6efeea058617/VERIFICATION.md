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

# Verification evidence and boundaries

The mathematical proof is given in `RESULT.md`. Its key independent deductions are: all zeros lie on \(n\) lines; the rescaled degree-\(n\) polynomial has \(n-m\) simple, nonzero limiting outer roots; real outer-root signs form a cyclic cosine grid; the real Kostlan zero intensity integrates to \(\sqrt m\); and parity rounds the limiting expectation to the existential valence bound.

Run `python verification.py` with SymPy installed. The checker performs exact rational Sturm root counts on six finite perturbation examples, finite trigonometric phase-grid comparisons on every pair \(2\le n<45\), \(1\le m<n\) at five phases per pair, and exact integer/parity checks for the degree-\((77,5)\) consequence. These checks pass in the packaged environment. The cosine comparisons use floating-point evaluation with explicit nonzero margins; they are finite sanity checks, not proofs of uniformity or the general theorem.

All-degree correctness rests on the analytic arguments, not the finite tests. The existence proof does not output explicit coefficients, does not determine an optimal perturbation size, and does not imply that the finite and escaping zero counts are independent. Historic originality is assessed against accessed sources and is not independently certified. No independent scientific audit has been performed.
