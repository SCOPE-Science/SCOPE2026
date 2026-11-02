---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The standard parity halfcube H_n is the [-1,1]^n cube minus 2^(n-1) strict odd-corner simplex interiors defined by s·x>n-2; distinct odd corners differ in at least two signs, so cut interiors cannot overlap. Each removed simplex has volume 2^n/n!, giving Vol H_n=2^n(1-a_n), a_n=2^(n-1)/n!. Uniform n-simplex Dirichlet moments of y_i give E(1-2y_i)^2=(n²-n+2)/((n+1)(n+2))=m_n. Subtracting removed moments from cube and dividing by 1-a_n produces diagonal variance (1/3-a_n m_n)/(1-a_n); even signed coordinate flips and permutations eliminate all means/cross covariance for n>=3. Normalization yields squared isotropic ratio (1-3a_n m_n)/(1-a_n)^(1+2/n). n=3 exact cube-relative squared ratio (3/5)*3^(2/3)>1, n=4 squared ratio (4/5)*sqrt(3/2)<1. For n>=5, b_n=3m_n > p_n=1+2/n by positive cubic numerator and strict Bernoulli inequality implies ratio<1. Logarithmic expansion as a_n->0 yields (1-L_H/L_cube)/a_n->1. Independently checked all exact rational signs by clearing rational powers n=3..60 (float comparisons would lose precision after n=24, and were not trusted).

## originality

PASS

Qualified PASS: Ermel–Walter supply parity-facet inequalities and Manecke–Sanyal–So full halfcube structure/triangulations, without an inspected interior-inertia formula; Kipp supplies isotropic context. Resultary published John/Löwner spin-weight orbit concerns the same vertex set but extremal ellipsoids, not volume-uniform covariance. Published Hanner theorem covers only dimension-four crosspolytope special case; odd halfcubes are not centrally symmetric. A Resultary diagonal-halfcube record is about cutting the cube by one diagonal hyperplane, a distinct body. Historical halfcube inertia tables remain possible.

## value

PASS

The demihypercube/parity polytope is a natural canonical high-dimensional family. A complete Euclidean interior uniform covariance and affine-invariant isotropic profile distinguishes interior mass from John/Löwner contacts, classifies the unique sign reversal at dimension 3, and gives its sharp superfactorial high-dimensional defect. This is substantive all-dimensional geometry even though its tetrahedron/crosspolytope boundary cases are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
