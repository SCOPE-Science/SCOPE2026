---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Exact normal equations yield E1=(X·Y/||X||²)(U·V/||U||²) as independent G/chi factors, proving moments from gamma integrals. Independent rows yield E2=(ΣW_iZ_i)/(ΣW_i²) with W,Z iid products of independent Gaussians. The product-normal K0 density has a logarithmic singularity at 0, and spherical-polar integration with integrable angular logs gives t^-R(log t)^R; layer cake yields the boundary p=R divergence. Dense error is G/chi_R, giving pure t^-R tail. Conditioning on W then on first Gaussian factors and strict Jensen establishes E(E2²)>1/(R-2) if R>2. Independently recomputed C1=4/π²,C2=1/π,C4=3/π² by product normal moments. Explicit argument covers R=1 and R=2 and dimension independence, with no implication that four rows cost identical runtime.

## originality

PASS

Chen–Li–Newton–Wright study precisely both tensor sketch constructions, but their full primary HTML Theorems 3–4 and proof sections concern high-probability embeddings rather than unconditional estimator inverse moments and logarithmic tail equivalents. Dense Gaussian sketch and product-normal Bessel singularity are classical, but their exact synthesis for the two competing structured regressions is not contained in the inspected guarantees. Related published Resultary products concern other quantities.

## value

PASS

The comparison identifies a sharp rare-failure and mean-square-error separation despite equal sketch row counts and well-conditioned one-column design; this is a motivated quantitative limitation of structure reuse, useful when interpreting probabilistic sketch guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
