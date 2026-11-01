---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The generalized-quadrangle incidence matrix B has BB^T=(q+1)I+A with collinearity eigenvalues q(q+1),q-1,-(q+1) and respective dimensions 1,f=q(q+1)^2/2,g=q(q²+1)/2; singular values of B are q+1,sqrt(2q),0. On the zero-sum subspace of the full 2v powered-distance matrix the exhaustive sectors are balanced-constant F_q(p), paired R±(p) of multiplicity f, and S(p) of multiplicity 2g, totaling 2v-1. R±<0 for 0<=p<=p0=log2(1+1/q), S<0 for p<p0, while F_q(0)=-1 and F_q(p0)>0, with derivative positive for p>=0; hence exactly one F root strictly before p0. Above it F>0 until p0 and S>0 past p0. Endpoint nullspace exactly one-dimensional, so centered Schoenberg Gram rank drops from 2v-1 to 2v-2. Expanding F_q’(0)=q³log(4/3)-q²log(3/2)+qlog2 and Taylor gives the stated q^-3 and q^-4 terms along existing orders. Independent W(2) incidence graph construction and full 30x30 powered-distance eigenvalue comparisons at p=0.1, 0.345784723476,0.6 verified all predicted spectral sectors; finite q never substitutes for general incidence proof.

## originality

PASS

Weston arXiv:0807.2705 gives lower bounds from cardinality and scaled diameter, not this equality threshold; Sánchez arXiv:1108.0451 gives a general finite-metric criterion and explicit complete-bipartite graph exponents (distances only 1 and 2), not the GQ graph distances 1,2,3,4. DeVille arXiv:1708.02294 gives generalized distance spectra for distance-regular graphs via an algorithm; a suitable specialization can compute sector eigenvalues but the paper does not state the first positive crossing, one-dimensional kernel, snowflake rank, or q^-3 asymptotic for generalized-quadrangle incidence graphs (searched the full text for quadrangle and negative type). Established incidence spectra are used openly, not claimed. Resultary exact-claim query returned no direct stronger claim. As a qualified best-knowledge conclusion, an unindexed earlier specialization is possible.

## value

PASS

Generalized quadrangles form a canonical distance-regular incidence family. Their supremal negative-type exponent, exact critical equality sign vector and minimal Hilbert snowflake rank are natural metric invariants for every existing equal-order case, and a q^-3 rather than q^-1 collapse is a substantial structural asymptotic, not a finite numerical table or parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
