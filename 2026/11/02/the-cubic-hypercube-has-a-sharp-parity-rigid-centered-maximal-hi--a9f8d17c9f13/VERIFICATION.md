---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The centered ball operator on unweighted Q3 uses radii 0,1,2,3 with row denominators 1,4,7,8. For nonnegative g=|f|, selecting one maximizing radius at each of 8 vertices exactly represents ||Mg||² as a max over 4^8=65536 positive row-stochastic matrices, whose optimal 2-norm equals the top eigenvalue of A^T A. For either bipartition radius pattern (0 on one parity class, 1 on the other), the bipartite adjacency J-P has singular values (3,1,1,1), and the top Gram block (1/16)[[25,3],[3,1]] has eigenvalue (13+3sqrt(17))/16. Its unique positive eigenvector has parity profile (1,sqrt(17)-4); direct four-radius comparisons show intended radii are active. The pinned standard-library verify.py was inspected: it builds all 65536 assignments and uses fraction-free exact integer leading-minor checks on D=317*56²I-200(56A)^T(56A) for the other 65534, which is a valid Sylvester certificate with strict bound 317/200 < exceptional eigenvalue. An independent full 65536-case floating-point scan found exactly two cases above 317/200, both parity patterns (max 1.5855823048033, next 1.58378143449); this numeric scan corroborates rather than replaces the inspected exact certificate. Perron simplicity and strict inequality classify precisely the two labeled absolute-value norming rays, with arbitrary signs. Does not extend to higher cubes or other p.

## originality

PASS

Compared the exact claim and implications with the named primary mathematics and published Resultary records. The actual semantic query was 'Resultary: sharp centered Hardy Littlewood maximal l2 norm three dimensional Boolean cube Q3 graph balls'. No materially inspected source supplies or logically dominates the stated instance; inaccessible/unindexed source risks remain.

## value

PASS

The eight-vertex cube is the first canonical nontrivial diameter-three Boolean cube; an exact sharp strong-type centered graph-ball maximal norm and complete equality cases capture the competition among radii 0 through 3. Proving all 65534 non-parity choices lose is a substantive finite operator norm extremal result, not implied by the K3,3 lower-bound coincidence. Does not claim any general higher-dimensional constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
