---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For n>=2, strict convexity/equiangularity and opposite-edge parallelism give the central symmetral Q=(P-P)/2 with edge lengths b_j=(ell_j+ell_(j+n))/2 and L(Q)=L(P). The shoelace cancellation and Brunn–Minkowski sign of the oriented midpoint-chain area give A(Q)=A(P)+2|A*(W)|, so the Wigner-enhanced D is L(Q)^2−8n tan(theta)A(Q) with theta=pi/(2n). The zonogon area is the exact circulant quadratic form B_jr=sin(pi|j−r|/n)/2 (diagonal zero). Its nonconstant Fourier eigenvalues are lambda_k=4n sin^2(theta)/(sin^2(pi k/n)−sin^2(theta)), positive for 1<=k<n; the zero mode vanishes. Parseval gives D=n sum lambda_k |bhat_k|^2. Minimizing lambda_k at maximal sin^2 gives sharp kappa_n=4n tan^2(theta) when n even and 4n sin^2(theta)/cos(2theta) when n odd. Exact equality modes are k=n/2 for even n or the conjugate pair (n±1)/2 for odd n, realized by positive small-amplitude centrally symmetric polygons. For n=2,3 every nonconstant frequency is a minimum, so every admissible polygon realizes equality. I independently constructed circulant matrices and DFT spectra for n=2..44 and verified random positive length forms and soft-mode equality, beyond just reading packaged CHECK.py; this is finite corroboration of the analytic diagonalization.

## originality

PASS

Best-of-knowledge novelty is the specific fully quantified invariant, not the underlying classical method or any known special-case total count. The relevant aliases (central symmetral, CPPOS, discrete Fourier inequality and polygonal Wigner caustic) were compared by the actual deficit identities, not by naming alone. An implication in one direction from sharp positivity to zero-deficit classification is not equivalence. The known results do not logically fix lambda_k at each k, so they do not obviously dominate the proposed all-mode refinement.

## value

PASS

The sharp spectral gap quantifies the precise Wigner-enhanced polygonal isoperimetric deficit in a natural CPPOS class; the parity-dependent κ_n and equality Fourier modes are needed to measure and classify near-extremizers, not implied by a nonnegative deficit or a zero-set theorem. The all-n coefficient and exact spectrum constitute a nontrivial quantitative stability refinement with explicit extremizing geometry, not a restatement of standard Jensen convexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
