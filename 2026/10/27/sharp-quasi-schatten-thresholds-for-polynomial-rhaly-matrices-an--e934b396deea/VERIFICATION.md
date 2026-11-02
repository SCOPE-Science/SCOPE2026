---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For alpha>1 and complex row weights with two-sided c(n+1)^(-alpha)<=|eta_n|<=C(n+1)^(-alpha), the finite lower-triangular all-ones block V_N has V_N^-1=I-L with norm <=2. Keeping strictly previous partition blocks produces rank<=j-1 and error norm <=ceil(N/j), hence s_j(V_N)<=ceil(N/j), while s_N(V_N)>=1/2. Row-dyadic slabs of R_eta decompose into rank-one predecessor rectangles and internally weighted V_N. For p<1 the Schatten p-power quasi-triangle bounds their contributions by O(2^{k p(1-alpha)}+2^{k(1-alpha p)}); summable if alpha p>1. Trace-class follows separately for alpha>1, covering p>=1. Conversely N singular values of each disjoint N-row and N-column compression are >=c 2^(-alpha-1)N^-alpha; if alpha p<=1 its S_p mass cannot vanish, contrary to tail continuity of compact Schatten class. This proves membership iff p>1/alpha including critical exclusion, with arbitrary phases. Direct computation S*^m C S^m-C has row weight -m/[(i+1)(i+m+1)] comparable to (i+1)^-2 for every m>=1, yielding exactly p>1/2. Checks verified separate finite triangular approximants and coefficient identities, not the infinite criterion.

## originality

PASS

Statement/implication comparison of actually read primary theorems and direct published mathematical-finding search supports best-of-knowledge originality for the final narrow claim, with precisely documented broader prior formulas and residual historical risks. Neither a failed search nor literature inaccessibility is treated as a proof of novelty.

## value

PASS

This is a natural quasi-Banach refinement of known Rhaly operator criteria: a polynomial-decay subfamily gives the full 0<p<1 threshold, phase robustness, and exact forbidden critical endpoint. Its Cesàro shift-covariance corollary distinguishes a quantitatively natural commutation defect from unrelated Cesàro self-commutators. It is not a claim to classify all irregular Rhaly sequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
