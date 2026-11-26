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

Zero mean makes the numerator P divisible by 1−z, leaving exactly q−1 free coefficients of R. Since (1−z^q)/(1−z)=D_q, the Mellin kernel for the ith adjacent difference is t^(s−1)exp(−(x+i)t)/D_q(t). Compact subsets with Re s>0 admit integrable logarithmic derivative bounds at zero and exponential bounds at infinity. On the ordered integration simplex, the evaluation or confluent determinant factors into a positive generalized exponential or log Vandermonde and an exponential determinant of sign (−1)^(m(m−1)/2), the latter from decreasing exponents −(x+i). Andréief gives that strict sign because the weights are positive and the product is integrable; multiplying the basis by Γ(s)>0 contributes only the positive factor Γ(s)^m to each Wronskian. Nonvanishing prefix Wronskians imply the multiplicity bound by generalized Rolle: divide by the first positive basis function and differentiate; the Wronskians of the derived system are the corresponding old Wronskians divided by positive powers of the first function. A nonzero real or imaginary coefficient component preserves at least the multiplicity of every real zero of the complex series. Thus q−1 samples are identifying, as is the jet of orders 0 through q−2 at any positive s (the meaning of derivatives used by the proof). The q^(−s) Leibniz rule gives the displayed matrix, whose row signs (−1)^k cancel the Wronskian orientation. Rank-nullity gives minimal complex scalar measurement count; evaluation minors give a one-dimensional real nullspace for any q−2 distinct positive nodes. Excluding zero, this line realizes those nodes simply and has no others. At q=2 the node set is empty and positivity of H₀ suffices. The mpmath script and its output were read, not executed; solving against Jv tests numerical inversion, not an independent evaluation of jet entries.

## originality

PASS

The supported distinction is the strictly oriented adjacent-difference Stieltjes-jet determinant and the identifying family it yields for every known period and positive shift. The periodic Hurwitz expansion and interpretation of its coefficients as derivatives are established. The positive-axis zero-count mechanism is classical: after mean-zero cancellation, the Mellin numerator has only finitely many sign changes, and the generalized Descartes proof extends to this bilateral transform. That mechanism is not itself new. The strongest inspected arithmetic sources do not give the signed determinant or identify the entire adjacent-periodic basis as a family with strict evaluation and confluent minor signs. The bounded pass is for this explicit arithmetic specialization with its recovery certificate, not an invention of total positivity, finite-dimensional interpolation, or generalized Descartes theory.

## value

PASS

The strict, oriented matrix gives an exact invertibility test across every positive shift and every period, complementing the known forward coefficient formulas with a practical finite inverse. The same positive-kernel structure constrains permissible real zeros and supports exact interpolation at any maximal set of positive nodes. This is a useful structural result for a natural periodic coefficient space, not just a short numerical determinant table or a lower bound from dimension counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
