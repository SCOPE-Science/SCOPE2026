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

The zero-current density has positive even prefactor 2v0/(v0^2-v1^2 tanh^2(ux)); its logarithmic derivative is odd and tends to -2(B+C)/(v0^2-v1^2) on the right, giving normalizability. On the slice g=3u the positive-half-line derivative has the sign of A-F(s), s=tanh^2(ux), where F(s)=[B+3C+(3B+C)s]/[(1-s)(1+3s)]. Independently differentiating, the numerator of F'(s) is B-5C+6(B+3C)s+3(3B+C)s^2, strictly increasing on [0,1] and positive at 1. Thus F rises from A_c if B>=5C; otherwise it decreases to a unique nondegenerate minimum and then increases to infinity. Clearing denominators gives the frozen quadratic and its discriminant. At the minimum this quadratic has a double root with positive vertex. Of the two A-roots of the discriminant the smaller one has 2A-3B-C<0, so the minimum equals the displayed larger root A_f. This proves the shoulder case and both sides of the fold, including 0<A_f<A_c, with derivative signs immediately giving the maxima and minima. At A=A_c the polynomial is s[(5C-B)-3A_cs], giving a fourth-order minimum or maximum for B<5C or B>5C, respectively. At B=5C, A=A_c=8C the derivative of log p begins with -48Cu^5 x^5/v0^2, giving the stated sextic maximum. In the exact witness Phi=-(4/5)(3s-1)(10s-1), the origin is nondegenerate and both off-axis pairs are simple. The implicit-function theorem preserves at least three strict maxima in an admissible full six-parameter neighborhood. Independent Simpson quadrature of the two stationary transport coefficients gave ratios 0.999525403218619 and 1.00008878159230, consistent with the recorded checks. Two nonmaterial proof slips: at line 76 the constant term is positive, not negative (the root product is negative; the endpoint signs and concavity also suffice), and the vertex bound at line 82 follows directly from (2A_f-3B-C)/(6A_f)<1/3, not from the sign at s=1 alone. Neither affects the stated theorem.

## originality

PASS

The exact model, stationary law, central criterion and implicit extremum equation are prior. The supportable distinct claim is the trimodal counterexample to the extra two-maxima assumption in that same model, the full exact g=3u boundary including its sextic merger, and persistence around the admissible witness. The nearest inspected catalogue overlap is a fixed subfamily of the slice, not general fold or merger coverage.

## value

PASS

This changes the stationary shape classification of an existing six-parameter model, rather than just supplying a new expression for its equilibrium law. It produces an admissible counterexample to the concrete two-maximum assumption, analytically separates the two bifurcations on a naturally exactly reducible slice, and identifies an order-six meeting point and open persistence beyond that slice. These conclusions carry information well beyond a numerical example or arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
