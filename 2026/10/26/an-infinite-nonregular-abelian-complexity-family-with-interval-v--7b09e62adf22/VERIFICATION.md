---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

C PASS. Every ordered pair of ternary letters occurs, allowing the factor-weight upper/lower induction. For length k^m with k=r+1, the maximizing-word splice in σ_r^(m+1)(c−1)σ_r^(m+1)(c)=U_(c−1)^r U_c^(r+1) U_(c+1) proves T_(m+1)=T_m+r max_a W_m(a); using weights ±1 at letter zero yields P_r(k^(m+1))−P_r(k^m)=r(max N_m−min N_m). Fourier diagonalization of cyclic incidence matrix gives N_m(a)=(k^m+2ρ^m cos(mθ−2πa/3))/3. The convergent H_r series therefore gives exact P_r(k^m)=ρ^m H_r(mθ)+2−H_r(0). θ/π is irrational by roots of unity in Q(ω); nonconstant continuous H_r has a full interval of phase limits. C-finite/nontrigonometric Fourier contradiction proves lack of k-regularity for every r>=4, and base-power invariance gives infinitely many 2-automatic not 2-regular examples r=2^e−1. Independent full sliding-window factor enumerations matched r=4,5,7 and m=0..3; finite checks do not establish the infinite result.

## originality

PASS

O PASS best of knowledge, materially qualified. Allouche–Rampersad–Rigo–Shallit–Stipulanti 2026 explicitly construct a single r=3 binary automatic non-regular abelian complexity example and raise other exponents in the assigned source comparison; the submitted all-r>=4 exact phase series and interval of limit points are extra theorems. The highly relevant original 2026 12-page paper could not be read in full: arXiv and lawful OA text retrieval failed, and authorized Oxford returned vpn_disconnected. Its uninspected appendices are a material priority risk; no whole-document NOT_COVERING conclusion is made. The 2025 Pisot-type framework excludes the growing non-Perron eigenvalues of modulus ρ>1.

## value

PASS

V PASS. Extending one nonregular example to a parameter-uniform infinite family and identifying a nondegenerate exact interval of normalized abelian-complexity limits are motivated, natural structural results; this is not arbitrary finite sampling or a mere renaming of the r=3 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
