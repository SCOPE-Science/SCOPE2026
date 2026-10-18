---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Parity grouping u_k=x_{2k},v_k=x_{2k+1} and bilateral Fourier transform is unitary on ℓ²(Z;C²), giving multiplier A(z)=[[-a,1],[z,−b]] on |z|=1. A* A has z-independent trace S=2+|a|²+|b|² and determinant |ab−z|², so its smaller eigenvalue is [S−√(S²−4|ab−z|²)]/2. The minimum of |ab−z| on circle is δ=||ab|−1|. δ>0 iff invertible; rationalization gives exact K²=[S+√(S²−4δ²)]/(2δ²). If δ=0, a continuous singular fiber at one phase forces infimum singular value zero, despite trivial ℓ² kernel. At fixed positive r≠1, K increases strictly in S, minimized by |a|=|b|=√r with K=1/|√r−1|, and diverges at fixed r with large imbalance. When ab≠0, the optimal phase is one Haar-null singleton and L² norm is not attained by nonzero data; if ab=0, |ab−z| and top inverse singular value are constant, so a measurable singular-vector field yields nonzero attainers. Independent two-by-two arithmetic agrees for (2,2) K=1 and (8,1/2) ≈2.710347891355; these checks are not the all-parameter proof.

## originality

PASS

PASS best of knowledge. The original Anderson–Onitsuka–Rassias paper, including its period-two results, treats one-sided time-grid h-difference equations and pointwise bounded-error (sup-type) Hyers–Ulam constants; its coefficients and norm estimates do not imply the bilateral Hilbert ℓ² inverse singular-value formula. Xu–Brzdęk and Jung likewise study constant coefficients and pointwise framework. The natural unitary 2×2 Fourier block symbol is standard, but the asserted optimal energy constant, dependence on within-period moduli at fixed Floquet product, and exact norm-attainment criterion for ab=0 are distinct statements not found in checked originals or indexed findings.

## value

PASS

For a natural minimal nonconstant periodic recurrence, an exact inverse conditioning norm in ℓ² is an independently useful invariant: it quantifies how two coefficient profiles with the same Floquet product differ arbitrarily in residual-error sensitivity, identifies balanced optimum, and determines when sharp error ratios are attained by genuine ℓ² vectors. These consequences refine the mere stability dichotomy and do not require a larger periodic theory to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
