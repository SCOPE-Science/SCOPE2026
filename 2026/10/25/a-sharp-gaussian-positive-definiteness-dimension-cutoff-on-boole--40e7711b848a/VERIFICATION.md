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

Translation-invariant Walsh characters diagonalize K(x,y)=q^{h(x,y)^2}; the exact eigenvalues are the Krawtchouk sums. When dq<=2 and q<=1/16, the absolute remainder R_d=sum_{j>=2} C(d,j)q^{j^2} satisfies R_d<q, so every nonparity character eigenvalue exceeds B_d(q) by at least 2(d-k)q-2R_d>0. Alternating-series signs give B_d>0 when d<=floor(1/q), the first possible nonpositive case is d=m+1, and B_{m+2}<0; coordinate subcube inheritance handles all larger d. The derivative tail bound makes the single root q_d unique in (1/d,1/(d-1)) for d>=17. Taylor expansion of B_d gives q_d=1/d+1/(2d^3)+O(d^-4). Independently verified exact parity-minimality in 148 dimension/character cases and high-precision roots for d=17,19,25,40; finite checks do not establish the infinite inequalities.

## originality

PASS

Classical Walsh/Krawtchouk harmonic analysis gives the eigenbasis. Feragen–Lauze–Hauberg (2014) Theorem 1 concerns geodesic metric spaces with Gaussian kernels positive definite for ALL bandwidths, not the finite nongeodesic Boolean cube at a fixed strong damping. Jayasumana et al. (2015) gives a generic Gaussian metric criterion, not the exact cube phase boundary. No inspected primary text or semantic result gave the parity-minimal theorem, single borderline binomial polynomial and uniform dimension cutoff; best-of-knowledge with residual equivalence risks.

## value

PASS

Whether a natural distance Gaussian is positive definite is a structural kernel-design question. The sharp finite-dimension transition, unique obstruction representation, explicit rank defect and analytic damping-root asymptotics are useful exact boundary facts beyond generic metric negative-type tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
