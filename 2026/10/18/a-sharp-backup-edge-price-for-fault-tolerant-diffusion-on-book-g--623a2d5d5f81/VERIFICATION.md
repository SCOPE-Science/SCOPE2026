---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: For each deleted edge the surviving lambda2 is minimum Rayleigh quotient on 1-perp and is concave in edge conductances; min over outages remains concave. Automorphism averaging gives a global symmetric optimum and preserves the single fixed hub-edge weight across every unrestricted optimum. For uniform spoke a and b/a=r, spoke deletion is strictly more damaging than deleting AB; the spoke-deleted quotient block characteristic zP_m(z,r) has unique simple positive eigenvalue f_m(r)<2. Direct independent exact determinant reconstruction plus 45 full Laplacian spectra gave error ≤4.6e-15. Rank-one perturbation yields f_m'(r)>0 and f_m''(r)<0 since Fiedler vector has unequal hub entries and d is not an eigenvector. The derivative of B0 f/(2m+t r) crosses at most once, giving t_c(m)=2m f_m'(0)/f_m(0), retention iff t<t_c. For m=2 symbolic simplification yields 3+2sqrt(2), and cubic asymptotic gives m*t_c→2. Intact gap is 2a, so bridge nominally optimally absent. The proof does not claim all asymmetric spoke weights unique.

## originality

PASS

PASS best-of-knowledge: Sun/Boyd/Xiao/Diaconis nominal continuous-time weighted gap has no one-edge-outage adversarial objective, Boyd/Diaconis/Parrilo/Xiao symmetry reduction treats fastest-mixing and intact graphs, Sydney/Scoglio/Gruenbacher edge rewiring optimizes nominal connectivity with a discrete modification set. Nothing inspected implies this exact worst-outage book-graph threshold and universal hub-weight necessity. Unindexed robust spectral design could cover the instance as a corollary; retained as a risk.

## value

PASS

PASS: A sharp, mathematically natural fault-tolerant design theorem exhibits an optional backup hub edge that is useless in nominal connectivity but compulsory at every optimum below a nontrivial price. The uniform edge-price threshold across infinitely many book sizes and its universal all-optimizer conclusion are independently useful network-design facts, not arbitrary one-off computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
