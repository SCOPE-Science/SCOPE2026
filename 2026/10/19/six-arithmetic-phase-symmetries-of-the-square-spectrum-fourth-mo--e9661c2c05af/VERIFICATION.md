---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Parseval applied to the square of the polynomial and equality in each complex triangle inequality give exactly the equal-two-square relations, since all ordered-pair magnitudes are positive. Modulo 16 the unordered pairs of classes 0 mod 4, 2 mod 4, and odd have disjoint squared-sum residue sets. Modulo 3 the count of nonmultiples of 3 is fixed. Modulo 5 the sole ambiguity among unordered pairs of square residues is {0,0} versus {1,4}, both with character sum zero. The matrix of the resulting six features on indices 1–6 has determinant 120 (independently computed by the signed permutation formula). Independent grouping of unordered pairs with repetition found exactly the collisions 50, 65, 85 at N=10 and additionally 125, 130 at N=11. They solve with unit pivots for 7,8,9,11,10. For k≥12 take the representative a of 3k mod 5 in {1,...,5}, then ((3k+4a)/5,(4k−3a)/5) is integral, positive, and strictly below k in each coordinate. The orthogonal identity replaces k by earlier indices with unit pivot. Thus the full torus is the graph over the first six phases, without extra torsion components; the determinant is the degree of the specific parameter map. The N=10 group instead has seven free coordinates. The supplied checker was inspected, not executed; its documented replay is `python3 verify.py` from the package directory, and its large-index and numerical tests are not needed for the infinite conclusion.

## originality

PASS

The supported distinction is the full integral equal-two-square relation classification in the positive-square truncations, hence the stable connected equality torus, with onset and degree. The classical even-moment majorant argument and the isolated first collision are not credited as new. The closest available moment and collision results do not cover this statement.

## value

PASS

Squares are a natural sparse Fourier spectrum with collisions, so the classical majorant inequality does not describe its equality geometry. The exact result determines when rigidity stabilizes, shows the four additional arithmetic phase directions, and gives a usable six-coordinate parametrization for every larger truncation and positive weight vector. The all-truncation classification, not the isolated determinant or a small-instance computation, is the useful result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
