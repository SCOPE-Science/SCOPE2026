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

For Bℓ<1, k_B(t−s)>0 on I×I, so the compact A has a unique positive even norm-one principal u and gap γ>0. Reflection of the left component makes the full operator exactly [[A,C_L],[C_L,A]] with C_L kernel k_B(2L+t+s) and ||C_L||=O(L^-1); its parity operators are A±C_L. Analytic perturbation of the isolated top eigenvalue yields λ(A+C)−λ(A−C)=2<u,Cu>+O(||C||^3), with derivative error O(||C||^2||C_L' ||)=O(L^-3). Expanding the cross kernel gives Δ=M² sin(2πBL)/(πL)−MM1 cos(2πBL)/(πL²)+O(L^-3) and Δ'=2BM² cos(2πBL)/L+O(L^-2); the factors 2MM1 follow from evenness and the sine product identity. Positivity M,M1>0 fixes nonzero coefficients. On J_n the sine has opposite endpoint signs while cos has fixed sign bounded away from zero, proving exactly one transverse crossing for each sufficiently large integer n. The one-interval gap isolates these as the top two full eigenvalues, and root substitution gives L_n=n/(2B)+M1/(πMn)+O(n^-2). A separate Nystrom calculation at B=1,ℓ=.8, Gauss–Legendre sizes 32 and 56 reconstructed all seven frozen Git blob tree entries and roots for n=6,10,20,40,80; numerical values are corroboration, not proof.

## originality

PASS

Best-of-knowledge: general bandpass degeneracies, exact Fourier duality, parity compression, and numerical high-modulation pairing are known. The audited claim adds an infinite sequence of exact crossings of the maximal eigenvalue, uniquely and transversely in specified windows, and a positive shape-dependent 1/n moment shift. Primary full texts of SenGupta et al. (2012) and Hogan–Lakey (2017), and the relevant main theorems of Fahs–Krasovsky (2020), do not logically imply these quantitative conclusions. Morrison 1963/1965 full texts remain inaccessible serious historical-priority risks; no whole-document novelty is claimed against them.

## value

PASS

Optimal Slepian concentration on two separated equal windows is a canonical spectral-geometric problem; crossings select between symmetric and antisymmetric optimal signals and produce exact top-eigenvalue nonuniqueness. Quantifying an infinite crossing locus with a nonzero shape-dependent moment coefficient is a motivated spectral refinement beyond previously known possibility of degeneracy and numerical high-frequency pairing. The result is a structural analytic all-large-index theorem, not an unmotivated finite-table correction; restrictions on Bℓ and equal components are clearly stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
