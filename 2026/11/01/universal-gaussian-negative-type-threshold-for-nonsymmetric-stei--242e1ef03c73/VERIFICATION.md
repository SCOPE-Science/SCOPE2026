---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Read complete RESULT.md, check_steiner.py and verification. Reconstructed incidence algebra MM^T=(r-1)I+J with r=(v-1)/(k-1)>k and b=vr/k, and the exact distances 1/2/3/4. On ker M the centered powered-distance eigenvalue is a((k-1)a-k), a=2^p, giving sharp upper cutoff p*=log_2(k/(k-1)) because b>v. The v-1 paired mean-zero sectors have explicit 2x2 H_p with strictly negative principal minors at p* for k>=3, and one zero eigenvector each at k=2; constant contrast C_p<0 at p*, with the proof inequality using beta=log_2(3/2). Strict lower negative type follows from Li–Weston and all t>0 strict Gaussian positivity from distinct squared-Euclidean points. Independently constructed complete pair design v=4 and AG(2,3) and verified shortest-path/centered endpoint eigenvalue signatures k=2 nullity 5 and k=3 nullity 3; these examples corroborate, not prove, universal exponent or all endpoint ranks.

## originality

PASS

Schoenberg negative-type equivalence and Li–Weston strict interpolation are known ingredients. Sánchez treats general finite metric tests and complete bipartite path metrics. Existing affine-plane examples are covered as special cases here, but no inspected theorem on all nonsymmetric Steiner designs was found that forces this exact design-independent threshold with k=2 anomalous nullity.

## value

PASS

A single sharp exponent and Euclidean dimension apply uniformly to arbitrary nonisomorphic Steiner block designs, including affine, projective high-dimensional and nongeometric systems. The exact endpoint null space is a meaningful invariant of incidence graph metrics for Gaussian kernels and embedding geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
