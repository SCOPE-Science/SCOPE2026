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

# Verification notes

The proof is self-contained after the cited, established shadow-determinant characterization. Its critical algebraic identities are the five-site matching polynomial, the scalar reduction \(Q=u(S-u)-x_2x_3\), the piecewise minimum of \(Q\) on a bounded simplex, and the least-singular-value inequality. The exact transition values follow from solving \(q=(1+q)^2/9\) and the equality-feasibility condition \(1-q\le2q\).

Run `python CHECK.py` to repeat supplementary finite sampling and exact invariant calculations. The completed run produced `CHECK_OK 3817 cases`. The checker has no external packages or data files. It does not certify a universal optimization claim: the analytical reduction and equality arguments in `RESULT.md` are the proof.

The infimum is genuinely not attained among strictly positive edge weights when \(0<q\le(7-3\sqrt5)/2\). Its positive approximants share the exact shadow, not an approximate shadow. This remains distinct from establishing publication priority. No independent validation has been undertaken.
