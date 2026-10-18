---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

At positive depth, Lagrange interpolation at x_j=h_j^2 gives alternating c_j signs. With b_j=|c_j|h_j, adjacent ratio b_{j+1}/b_j=sqrt(x_j/x_{j+1}) product_{i!=j,j+1}|x_j-x_i|/|x_{j+1}-x_i|, bounded below by >2 product_{q=1}^j(1-4^-q)>4/3 for j>=1 (and >=2 for j=0), since strict nesting forces x_{j+1}<=x_j/4. Thus b_j increases strictly. Collected interior node of first appearance level ell has alternating tail W_ell=c_ell h_ell+...+c_d h_d>0; if ell<d its remainder below b_d is negative when grouped into adjacent pairs. Endpoints have W_0/2>0 and <b_d. Because d>=1 there are newly introduced interior nodes receiving b_d; last interpolation coefficient supplies exact product. ∑w_i=b-a for constants and positivity gives sharp absolute perturbation norm. Independent exact Fraction calculations agree on mixed depth>=1 chains. Crucial boundary: original unqualified depth statement would include d=0,N0=1, where two trapezoidal endpoint weights equal h0/2 but claimed product maximum is h0. The complete guarded replacement RESULT.md and SLOGAN.txt explicitly impose d>=1 and retain the full proof/scope and nonnested counterexample; this is a substantive repaired final claim, not an unmodified PASS.

## originality

PASS

Statement/implication comparison, not mere title search. The exact variable-ratio Richardson result strictly enlarges the fixed-r published theorem without assuming it implies mixed ratios.

## value

PASS

All mixed-ratio nested composite-trapezoidal Richardson rules retain positive sample weights, an intrinsic stability property absent from arbitrary nonnested chains; it strictly extends the earlier fixed-geometric-r theorem. The exact largest weight and optimal absolute sample-noise norm are useful quantitative invariants, and the explicit zero-depth correction makes boundary quantifiers correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
