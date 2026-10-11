---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

At small \(\mu\), substituting \(2\pi-t_g=s u\) with \(s=\sqrt\mu\) removes the double degeneracy and the implicit-function expansion gives \(u=2\sqrt\pi-(2/3)\pi^{3/2}s^2+O(s^3)\); exponentiation yields the stated \(H_g\) and width. At large \(\mu\), the left side of the grazing equation vanishes at \(t_0=\pi+\arctan(1/\mu)\), and the exact trigonometric rewrite shows the true root differs by only \(O(e^{-\pi\mu}/\mu)\). Expanding \(t_0\), \(H_g\), and \((2\cosh(\pi\mu)-1)^{-1}\) gives the displayed coefficients. Independent numerical root checks converge to the predicted small- and large-parameter rescalings.

## originality

PASS

The source paper defines the exact oscillatory wedge and proves only that both boundary curves coalesce to one as \(\mu\to0^+\) and to zero as \(\mu\to\infty\). It does not state the Puiseux small-\(\mu\) grazing scale, the two-term wedge width, or the exponentially separated large-\(\mu\) boundaries. The audited singular rescalings extract genuinely finer endpoint geometry rather than specializing a published asymptotic theorem.

## value

PASS

The two endpoint regimes quantify how the existence wedge is actually lost: algebraically with a square-root grazing layer at one end and with two different exponential scales at the other. These rates sharpen a qualitative parameter classification and are useful for continuation and numerical resolution of the oscillatory region.

The dated certificate retains the supplied scientific assessment, sources and limitations.
