---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Spectral decomposition of the star Laplacian into constants, radial line eigenvalue m+1, and leaf fluctuations eigenvalue 1 gives the exact matrix T_{s,m}(c,x)=x-E_mx+a(E_mx-c), a=(m+1)^(-s). Direct column sums, row sums and singular values yield the advertised 1, infinity, and 2 endpoint norms and the exact hub/leaf crossover a=2/(m+2). Independent eigendecomposition and matrix norm tests at m=2,3,7,16 and s=.2,.5,1,1.7 agree. For fixed 1<=p<infty, decomposition into bounded I-E_m plus hub mass of norm m^{1/p}a proves s<1/p and s>1/p regimes; step-function embedding proves critical D_p. For non-Hilbert p, a two-valued extremizer of the known sharp centering norm C_p has nonzero derivative in scalar c while the input denominator changes by o(|c|), giving strict D_p>C_p. P=1,2 endpoints handled separately. This is an analytic proof, not an inference from finite numerical checks.

## originality

PASS

Exact star matrix and centering norm C_p are known components. The specific all-s finite-star endpoint formula and critical s=1/p hub/leaf phase law with strict D_p>C_p for p non-Hilbert were not implied by the inspected infinite-tree or network-pseudoinverse primary sources.

## value

PASS

The graph fractional gradient on finite high-degree stars is a natural Riesz-type model. The transition at 1/p separates hub-amplification from centered fluctuations and identifies non-Hilbert critical resonance, a meaningful asymptotic change relevant to graph norm estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
