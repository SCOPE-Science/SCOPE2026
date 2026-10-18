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

The theorem is proved symbolically in RESULT.md using the two Gram identities for a symmetric design, the zero-mean Laplacian equations, and an exhaustive classification of edge-current signs. No enumeration or numerical approximation is needed for the all-design statement.

Reproduce the independent finite checks with `python check_design_projections.py` (Python 3, standard library only). The checker constructs four concrete designs and inverts each grounded Laplacian exactly using `fractions.Fraction`. It checks all transfer-current entries, projector symmetry/idempotence, and exact column norms. Its tested designs are \(2\)-\((7,3,1)\), \(2\)-\((13,4,1)\), \(2\)-\((11,5,2)\), and \(2\)-\((5,4,3)\).

Observed cut/cycle norm pairs are respectively \((53/21,16/7)\), \((40/13,81/26)\), \((159/55,172/55)\), and \((11/5,23/10)\). For both projective planes every entry and all four level multiplicities agree with the closed formulas. These computations do not establish anything about unrealized or larger designs; that rests on the proof.

The uniform bounds are algebraic consequences of the general formula and \(1\leq\lambda<k\); sharpness is witnessed by existing prime-power projective planes of arbitrarily large order. The asserted norms concern the canonical Euclidean orthogonal operators considered as \(\ell_1\) maps; minimality among all projections and intermediate-exponent norms are not claimed. Independent mathematical audit has not been performed.
