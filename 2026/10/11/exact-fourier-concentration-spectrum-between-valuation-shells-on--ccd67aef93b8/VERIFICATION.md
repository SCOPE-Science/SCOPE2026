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

Independently reconstructed the full theorem for every prime p, n>=2, 0<=s,t<n. With unitary Fourier characters and X_s=p^sG\p^{s+1}G, F_t=p^tG\p^{t+1}G, subgroup orthogonality gives exactly B_ab=p^{-s}1_{p^{n-s}|a-b}-p^{-s-1}1_{p^{n-s-1}|a-b}. For s+t<=n-2, (p-1)p^{n-s-t-2} coarse congruence classes each split into p fine classes of p^s elements, with compressed normalized matrix I_p-J_p/p; hence unit eigenspace dimension (p-1)^2 p^{n-s-t-2}, remaining zero. At s+t=n-1 there are p-1 fine classes of p^s elements, giving I_{p-1}-J_{p-1}/p, with eigenvalues 1 [p-2] and 1/p [1], including p=2 boundary with no eigenvalue one. For s+t>=n the frequency shell differences lie in both required annihilator congruences; B=(p-1)p^{-s-1} J_M, giving exactly β=(p-1)^2/p^{s+t-n+2} [1] and zero [M-1]. Coarse/fine indicator vectors give all nonzero eigenspaces; nulls are within-fine zero-sum directions. The largest eigenvalue and Rayleigh quotient characterize all equality cases, including p=2. Independent direct normalized DFT checks of 84 distinct (p,n,s,t) cases for p=2,3,5,7 with p^n<=343, total frequency dimension 2043, matched all eigenvalues within 2e-11; these tests corroborate the universal congruence-block proof and are not claimed exhaustive.

## originality

PASS

Qualified best-of-knowledge PASS: Compared complete theorem statements and the material relevant to the exact compression, not just titles. Zhu--Wakin defines the same general abelian time/frequency cutoff operator and studies general asymptotic concentration, without an explicit prime-power two-shell spectrum. Kozyrev diagonalizes a p-adic derivative using disk-supported wavelets, not the finite double-shell projector. Marceca--Romero--Speckbacher give spectral-deviation counts for Euclidean/discrete Fourier settings, not exact cyclic finite p-group multiplicities. The complete published minimum-tight-frame and dyadic-four-point Fourier-zero proofs determine different invariants. No independent prior statement implying the three-regime exact spectrum with optimizer classification was found; older or unindexed ultrametric spectral calculations remain a genuine priority risk. A general subgroup orthogonality identity is known and is not credited as new.

## value

PASS

Valuation shells are canonical difference layers of the p-adic subgroup filtration, and their Fourier duals are natural fixed frequency bands. For every prime power and both scale parameters, the theorem determines the complete concentration eigenspectrum rather than only a trace or generic plunge estimate: it gives exact dimensions of perfectly doubly localized subspaces, the sharp arithmetic boundary s+t=n-1 with the p=2 exception, one explicit nontrivial intermediate eigenvalue, and all optimizer directions. These structural facts provide reusable precise localization limits for hierarchical Fourier analysis. The problem and invariant are motivated independently of small finite computations, and this all-parameter closed classification was not mechanically stated/implied by the examined prior concentration/eigenwavelet theorems. Value is limited to centered cyclic prime-power masks; no broader group claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
