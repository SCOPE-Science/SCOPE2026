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

The relation (n+1)t^nD(t)=0 forces D(t) into (t) and allows every such image, giving precisely the stated n derivation basis elements. The bracket computed on t has coefficient j−i at degree i+j in that basis until truncation. For f of leading index i<m, the adjoint columns indexed by j<n−i, j≠i have distinct nonzero leading positions; the column at i is dependent by [f,f]=0 and higher columns vanish. This gives C(f)=kf⊕F_{n−i}. A tuple of minimum index i<m therefore has proportional images in F_i/F_{n−i}; conversely such proportional images lift to a common line plus a tail commuting with all of F_i and with itself. The remaining tuples in F_m^s lie in Z_{m−1}: the indicated quotient of F_m has dimension one for even n and zero for odd n. The rank-one locus is geometrically integral by the outer-product parameterization and its nonzero charts, of dimension s+n−2i−1, plus si free tail coordinates. For a comparison Z_i versus Z_j with j>i, the single-entry e_i tuple witnesses noncontainment; when j<i the e_i,e_{n−i} tuple has two independent quotient images, both indices below n−j, so again there is noncontainment. The union of the geometrically reduced pieces gives the reduced bracket variety (geometric-set equality and contraction of the radical ideals); it makes no assertion about the original bracket scheme being reduced. In the finite count the minimum-index column can be any of q^s−1 nonzero vectors, the remaining n−2i−1 quotient columns have q choices each and the si tail coefficients are free. The F_m^s stratum contributes q^{s(n−m)}. Independent enumeration over F_7[t]/(t^5), composing derivations on t for 2401² ordered pairs, gave 35,329 commuting pairs, with 16,464 each at minimum indices 0 and 1 and 2,401 in the all-tail stratum, agreeing with the formula.

## originality

PASS

Pass for the all-arity shorter truncated full-derivation components and finite-field formula, not for the Witt filtration, leading-term centralizer method, or prior modular Witt counts. The most closely checked published theorem uses nilpotent pairs in the full modular algebra or its Borel nilradical. Indexed counts are for the longer full modular algebra or tail subalgebras. The quotient reduction is not an implication because even commuting pairs downstairs need not lift to commuting pairs upstairs. No checked true statement gives the asserted geometry and count at the dominating shorter truncation parameters; unavailable neighboring papers impose a bounded residual risk.

## value

PASS

The full derivations of a shortened polynomial algebra are a natural filtered Lie family in both characteristic zero and large characteristic. Pair commuting varieties hide a distinction: in arity at least three, the same components acquire genuinely different dimensions. The theorem simultaneously resolves which rank-one strata close to components and counts rational tuples without overcounting their intersections, including commuting tuples created by truncation and absent as lifts from the longer algebra. This extends known Witt centralizer methods to a distinct, useful exact invariant rather than re-evaluating a full-Witt census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
