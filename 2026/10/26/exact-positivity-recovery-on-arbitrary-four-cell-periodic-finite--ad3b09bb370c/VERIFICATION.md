---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The element integrals give positive definite M and positive semidefinite K, with K1=0; hence Q is positive definite for t>=0 and P(0)=I. Independently used Cramer's column-replacement determinants of 6Q, each replacing column i by column j of 6M. Multiplying each determinant by abcd/3 gives exactly the frozen G_ij. Expanding by permutations over rationals and clearing the length reciprocals gave coefficient signs in degrees 0..3: (+,+,+,+) on the diagonal, (0,+,+,+) on ordered adjacent pairs, and (0,-,mixed,+) on ordered opposite pairs, where the strict signs mean all nonzero monomial coefficients have that sign and each indicated polynomial is nonzero. The positive determinant preserves these signs; after the exact factor t is removed the opposite quadratic has positive leading and negative constant coefficient, two real roots of opposite signs, and the stated positive radical. The maximum includes equality for entrywise nonnegativity. The alternating specialization has monic quadratic t^2+(ab/6)t-ab(a+b)^2/72 and recovers its known root. At (1,2,3,4) the four roots are distinct (about 0.34713, 0.48954, 0.86992, 2.04490), and exact arithmetic verified the three reported entry/minimum values. Replay: python /workspace/branches/replay_pos.py (SymPy 1.14); the uploaded checker was inspected, not executed.

## originality

PASS

The alternating and uniform specializations are covered and receive no novelty credit. The actual arbitrary-four-length periodic theorem, in particular the four direction-dependent exact zeros and the sign classification, is distinct from the strongest compared statements.

## value

PASS

Positivity of a completed consistent-mass step is an operational mesh/time-step question. On a graded cycle this gives the exact safe positive-step interval, identifies which pairs can fail, and can avoid a strictly overconservative matrix-sign condition. Directional sign failure is information absent from the alternating formula; the all-parameter statement is not a numerical recomputation of that subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
