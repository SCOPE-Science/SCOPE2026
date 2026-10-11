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
The proof reduces the sharp norm to one exact polynomial-elimination problem. The packaged `artifacts/verify.py` recomputes, with exact rational arithmetic, the polynomial-division identity between the two stationary equations, the nonzero resultant of the two remainder coefficients, the substitution factorization through \(P(r)\), and rational Sturm root counts.

The checker certifies that \(P\) has exactly two positive roots, one in \((17/20,43/50)\) and one in \((91/100,23/25)\); that the first forces \(u<0\); and that the second gives the unique admissible critical point. Numerical decimals are then produced only by bisection inside the certified second interval.

The finite computation is not used as a sample-based substitute for the global argument. Compactness, the exact boundary bound \(5/2\), the interior value \(11/3\), and uniqueness of the admissible stationary point prove global optimality.
