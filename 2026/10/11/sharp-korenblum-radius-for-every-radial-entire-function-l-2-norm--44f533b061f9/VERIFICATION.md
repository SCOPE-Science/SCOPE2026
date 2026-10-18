---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Radial orthogonality gives coefficient Hilbert norm Σm_j|a_j|²; Cauchy–Schwarz makes moment ratios m_j/m_{j−1} monotone, hence T=R times the coefficient backward shift is a contraction on the polynomial Hilbert completion. For h=f/g, |h|≤1 on |z|>R forces every quotient pole inside |z|<R, including no pole at boundary/infinity. As g is entire, only finitely many quotient poles lie in that compact disk, so h is rational. H(w)=h(R/w) is a rational Schur function analytic near closed unit disk. From q(z)f(z)=p(z)g(z), reversed polynomials satisfy Q(T)f=P(T)g coefficientwise; Q(T) invertible and rational von Neumann inequality yields ||f||≤||g||. For every S>R, f=c and g=z with R<c<S give exterior domination but ||f||²>||g||². Checked finite rational moment ratios in independently inspected CHECK.py and independently reasoned the pole/functional-calculus assumptions; finite tests not substituted for all-W proof.

## originality

PASS

Stronger than identified 2026 monotone-weight theorem and restricted Gamma exponent range because all positive measurable radial weights with finite moments are covered. Analytic rational Schur functional calculus supplies a proof outside the published sufficient moment-measure criterion. Source full-text gap is explicit; no whole-document noncoverage claim inferred from abstract or indexed snippets.

## value

PASS

The result answers a natural sharp-radius problem for the entire radial Hilbert Fock class, removing monotonicity and covering explicit weights whose earlier sufficient criterion fails. The precise invariant sqrt(m1/m0) is useful for any radial W and follows from a nontrivial backward-shift/rational Schur mechanism; its value is not merely a numerical Gamma calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
