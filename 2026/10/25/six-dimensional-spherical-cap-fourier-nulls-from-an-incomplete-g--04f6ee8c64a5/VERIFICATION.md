---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed all quantifiers: for every sufficiently large positive n there is one locally unique real pair (h_n,t_n), h_n in (-1,1), t_n>0, for the axial transform of the solid unit ball cap in dimension d=6, using Fourier phase exp(-it u). The 5D section volume gives F_h(t)=integral_h^1 (1-u^2)^(5/2)e^(-itu)du up to |B_5|. Independent evaluation of the full-ball Bessel identity gives F_-1(t)=sqrt(pi) Gamma(7/2)(2/t)^3 J_3(t), so its t^(7/2)/2^(5/2) leading term is 2 Gamma(7/2) cos(t-7pi/4). Setting h=-1+c/t and t=pi n+theta, subtraction of the short bottom tip yields C^1 convergence to L(c,theta)=e^(i theta) i^(-7/2) Gamma(7/2,ic)+e^(-i theta)i^(7/2)Gamma(7/2). The lower incomplete-gamma series has gamma/Gamma=K c^(7/2)[(U-V)-i(U+V)], K=8/(15 sqrt(2pi)); hence modulus-square difference equals 2K c^(7/2) H(c). Independently coded exact Fraction alternating bounds give H(9/10) in [-0.02210871,-0.02198629], H(1) in [0.01409752,0.01425575], and the uniform derivative lower bound H'>=0.1452132065 over [0.9,1]. Thus there is exactly one transverse amplitude crossing in that interval. Independent mpmath root c*=0.96131491167342160479, phase theta*=0.74848728058477646; real Jacobian determinant d|a(c)|^2/dc=1.48844249165883 nonzero. Uniform C^1 endpoint asymptotic plus the quantitative inverse/implicit function theorem gives a genuine locally unique zero for every large n; O(1/n) scaled correction yields the claimed t_n and h_n expansions. Independent complex quadrature gave residuals under 2e-50 for additional n=15 and 30 roots; these are only consistency witnesses, not proof of all n. Independently reconstructed the exact eight-entry Git tree SHA fe92650c5710801914e2dc01049408e0e41c1990 from all eight fetched file blob SHAs. Boundaries: c* uniqueness asserted only in (0.9,1), not globally; all claims restricted to six dimensions, solid cap and axial real frequencies.

## originality

PASS

Best-of-knowledge PASS for the specific infinite local axial-zero family of noncentrally symmetric six-dimensional truncated balls. Read BLP09's relevant primary full text: its Bessel unit-ball formula supplies an input, and its balanced-domain zero-distance results do not imply the cap result. Read the recent Gómez-Serrano–Levitin–Platt–Polterovich arXiv:2609.10517v1 full relevant text: its new unboundedness and axis positivity concern centrally symmetric bipyramids, the opposite geometric setting. DLMF §8.13 describes incomplete-gamma zeros, not this nonzero modulus level set. Resultary searches for caps, equivalent gamma constants, and Fourier-null aliases found related bipyramid zero-free strips but no dominating cap result; searches of published GitHub SCOPE package content for overlapping terms returned none. An indexed historical cap diffraction or special-function paper may still contain the same amplitude crossing, so no exhaustive priority claim is made. All four structured comparisons and actual source inspections are recorded.

## value

PASS

The object is a natural convex solid spherical cap, the invariant is an exact real axial Fourier null, and an explicit threshold of endpoint truncation versus high frequency is a meaningful geometric Fourier-analysis boundary case. An integer-endpoint Bessel zero is destroyed by asymmetry, and the fractional 5/2 section weight forces a genuinely noninteger 7/2 incomplete-gamma interference condition. The result is not merely a routine substitution: it gives infinitely many genuine two-parameter real cancellations, an exact locally unique crossing constant with certified transversality, and sharp frequency/height asymptotics. This is independently useful in Fourier null varieties and endpoint diffraction; it does not purport to solve the global zeros or a general-dimensional phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
