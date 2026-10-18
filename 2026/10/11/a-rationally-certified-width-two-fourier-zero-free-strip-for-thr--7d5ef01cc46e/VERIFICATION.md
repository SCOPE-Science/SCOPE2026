---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Integrating disk slices and twice integrating by parts gives \(u^2F(u,s)/(4\pi)=H(u,s)=\int_0^1g(s(1-x))(1-\cos ux)\,dx\) with \(g(z)=J_0(z)-zJ_1(z)\), transverse \(s=\|\eta\|_2/\alpha\). The Bessel sign estimates make \(g\) strictly decreasing on \([0,2]\), so the continuum of transverse frequencies reduces to \(s=2\). The analytic inequalities prove \(H(u,2)\ge11u^2/120\) for \(0<u\le1\), and \(H(u,2)>1/175\) for \(u\ge14\). For \(1\le u\le14\), a fresh independent exact-Fraction evaluation of the paper-defined degree-40/11-term integrated Taylor polynomial on all 261 nodes found minimum about 0.11520649; its exact rational value exceeds \(1/20\), the uniform Taylor remainder is less than \(10^{-10}\), and the proved derivative interpolation error is at most \(3/80\). This is a complete continuum certificate, not an unsupported finite grid. The zero-axial-frequency original slice integral is positive. Volume \(2\pi/(3\alpha^2)\) and \(j_{3/2,1}<9/2\) give the equal-volume ball comparison at \(\alpha\ge23\). The nonempty closed real zero-set theorem ensures the attained minimum is strictly beyond the closed strip.

## originality

PASS

The initiating 2026 Fourier-zero isoperimetry preprint proves a positive but unquantified transverse zero-free strip and reports a numerical elongated bicone; it does not imply a universal explicit width of two or threshold 23. A prior mathematical note reportedly established width roughly 1.25578 and sufficient cutoff roughly 91.625 from convexity of the slice kernel. That pointwise-convexity argument ceases to apply at width two; positivity of the integrated oscillatory kernel and its rational certificate are an additional strengthening. The earlier note was identified but its standalone full text was not accessible; the comparison retains an explicit risk.

## value

PASS

This is a substantive quantitative advance on an explicitly motivated Fourier-zero isoperimetric counterexample family. It certifies a strictly wider *all-frequency* zero-free region and lowers a sufficient geometric elongation parameter from about 92 to 23 by combining analytic inequalities and an exact rational continuum certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
