---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

A cyclic orientation string has missing edges exactly at transitions (B_i,B_{i+1})=(0,1); M has mean np(1-p), P(M=0)=p^n+(1-p)^n and P(M=1)=n∑_{j=1}^{n-1}p^j(1-p)^{n-j}. Any spanning-tree edge set omits exactly one edge, so symmetric difference >=|M-1|. Uniformly deleting a missing edge, or any edge for M=0, is rotation-equivariant and has uniform tree marginal; equality holds pointwise. Therefore W1=E|M-1|=npq-1+2(p^n+q^n), and TV=1-P(M=1) because the M=1 component is uniform and other components disjoint. For p=λ/n, rare ones form asymptotic isolated transitions, M→Poisson(λ); exact formulas yield f(λ)=λ-1+2e^-λ and TV=1-λe^-λ. Convexity gives unique minimizers log2 and 1; finite-p optimizing sequences cannot stay nonsparse by W1 bound and exponential P(M=1) bound. The edge metric is unnormalized, including n=3 and p endpoints.

## originality

PASS

PASS with residual older run/transport risk. Earlier general uniform-spanning-tree/determinantal approximation statements treat high minimum degree or different randomness and supply neither the exact biased 1-out cycle distributional distances nor the incompatible log2/1 sparse scales. The event M=1 is the one-run cyclic-word event, a classical counting identity; the joint exact optimal coupling and global bias optimization are not shown by the examined prior statements.

## value

PASS

PASS: the cycle is the first nontrivial sparse graph benchmark for comparing locally selected random edges with the uniform spanning tree law. Exact optimal unnormalized transport and total variation exhibit different minimizing sparse biases and nonvanishing sharp limits; this supplies an interpretable boundary to high-degree approximation results, not a merely rescaled probability table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
