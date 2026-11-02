---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Verified exact pinned RESULT.md. For invariant mu with Lebesgue X marginal, conditioning the next state on x produces uniform inverse doubling branches and c(x)=cos(2pi x); m=c+alpha Pm and s=c^2+2alpha c Pm+alpha^2 Ps. Pcos(2pi x)=0, Pcos(4pi x)=cos(2pi x), P1=1 imply unique L2 solutions m=c and s=1/[2(1-alpha^2)]+(alpha^2/2)c+(1/2)cos(4pi x). Explicit independent SymPy branch averaging and substitution checked Pm=0, both moment residuals=0 and s-m^2=(alpha^2/2)(1/(1-alpha^2)+c). Since |alpha|<1, ||P||L2<=1 and Neumann inverse is valid; bounded attracting strip gives finite moments. Integrating s and m gives mean zero/global variance 1/[2(1-alpha^2)]; using -1<=c<=1 gives exact min alpha^4/[2(1-alpha^2)] and max alpha^2(2-alpha^2)/[2(1-alpha^2)]. At alpha=0 variance is identically zero and m=c, so positivity explicitly only for alpha!=0; alpha negative is covered. Does not extend to arbitrary non-Lebesgue invariant marginals or infinite second moments. The simple packaged verify.py alone is not taken as proof. Reconstructed eight pinned Git blob SHAs into matching Git tree 05b17d974604237c7f1be798f629fcc8e7bec5c1.

## originality

PASS

Best-of-knowledge qualified PASS for the exact conditional mean/variance profile, not for the map, transfer operator, or global variance. The fully accessible Kaplan-Yorke application in Liang 2016, section III.C, formulates the map and transfer operator for information-flow calculations, but does not present the stationary conditional moment profile and says its generic density integrals cannot be explicitly evaluated without specifying the density. Kaplan-Yorke 1979 publisher preview is the foundational chaotic-attractor source, not a checked conditional-moment theorem. A serious unclosed priority risk is R. Graham 1983, whose publisher abstract states that exact solutions for maps introduced by Kaplan and Yorke are used to calculate moments, correlations and probability densities. The protected PDF was not available and authorized Oxford access was VPN-disconnected; the abstract does not reveal whether the identical forcing, joint stationary distribution and fiberwise second moments were actually treated. Beck 1991 addresses higher-order correlations in Kaplan-Yorke-type extensions, but available abstract does not state the assessed fiber variance. This is an explicit qualified assessment rather than a claim of exhaustive priority or that inaccessible work is non-covering.

## value

PASS

The first two conditional moments as explicit functions of the expanding coordinate are a natural statistical invariant of a canonical fractal-skew-product stationary law, beyond global variance and Lyapunov dimension. The nonconstant conditional variance measures a genuine heteroscedastic location dependence; its sharp finite min/max and degenerate alpha=0 boundary give concrete benchmarks for invariant-density estimates and conditional-statistics computations. This is mathematically motivated by the named canonical map and natural moment functions, not an arbitrary finite slice. Scientific modesty: it is an elementary closed Fourier-mode consequence of transfer-operator invariance, supplies no full conditional distribution, entropy, dimension theorem or new operator mechanism, and should not be advertised as a major general dynamical theorem. Value does not rely on code reproducibility or possible priority alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
