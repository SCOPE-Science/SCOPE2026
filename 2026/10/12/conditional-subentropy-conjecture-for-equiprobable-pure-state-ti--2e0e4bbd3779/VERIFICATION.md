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

For any n>=d>=1 unit-norm equal-prior pure tight frame, rho_B=I_d/d and rho_XB has exactly n eigenvalues 1/n. For any POVM, P_guess<=d/n since projectors <=I; the tight-frame POVM E_x=(d/n)|psi_x><psi_x| sums to I and attains d/n. The uniform-rank subentropy identity Q(I_r/r plus zeros)=log r-H_r+1 follows analytically from the normalized-simplex representation: sum of first r Dirichlet(1,...,1) coordinates S has Beta(r,N-r), with E[S]=r/N and E[S log S]=(r/N)(H_r-H_N). Hence Q(X|B)=log(n/d)-(H_n-H_d), gap from H_min exactly H_n-H_d, equality iff n=d (square frame orthonormal); all logs natural and ambient zeros handled. Independent beta-integral and harmonic checks corroborate concrete dimensions; analytic derivation controls all frames and all n.

## originality

PASS

Datta-Dorlas-Jozsa-Benatti introduce conditional subentropy, prove the two-label pure-state case and explicitly conjecture Q(X|B)<=H_min. Tight-frame optimal discrimination p_guess=d/n was already proved in quantum measurement/frame work including Eldar-Forney and Farokhi-Xiao; it is credited, not new. Their statements do not compute the harmonic-number conditional subentropy gap for every tight frame. This resolves a meaningful all-dimensional sector of the conjecture, conditional on the exact uniform-rank simplex formula, with no equiangularity requirement.

## value

PASS

An exact theorem across the natural unit-norm tight-frame/projective one-design class settles a nontrivial infinite family of an explicit open information-theoretic inequality. The exact harmonic gap and strictness criterion are useful quantitative invariants independent of the frame geometry and apply even where optimum discrimination probability was already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
