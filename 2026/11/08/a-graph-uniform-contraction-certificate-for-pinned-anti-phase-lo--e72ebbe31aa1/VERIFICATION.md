---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed the claimed branch on all finite simple connected d-regular undirected bipartite graphs, d≥1, with output coupling F=C f_mu. Adding two-color swap equations yields mu=(4t+2)/(4t+1-4t²); subtracting yields (1-2epsilon)mu(t-1/2)=1 and epsilon=(4t²-2t-1)/(4t²-1). The t interval ((1+sqrt5)/4,(3+sqrt17)/8] follows from epsilon>0 and mu≤4; epsilon<1/2 and points remain in (0,1). At p, f'(t)=c<0 and f'(1/2)=0. For normalized shore adjacency R with all row and column sums 1, the full two-step derivative is triangular with upper block epsilon²c² RR^T, and top singular value R=1, proving radius v² exactly, not merely on the color subspace. Squaring gives nonnegative 4-iterate blocks with exact row sums v^4 and v³(v+2), since w=(1-epsilon)mu(2t-1)=v+2. Symbolic differentiation confirms v increasing; endpoint yields v=(sqrt17-3)/2 and exact maximum (71-17sqrt17)/2<1/2. Global cube derivative bounds ||DF||∞≤4 and ||D²F||∞≤8 produce B_4≤43520 by chain rule; delta=1/174080 gives derivative ≤3/4 on a convex ball strictly inside the forward-invariant cube, hence uniform F^4 contraction and convergence of intermediate phases. Equal shore cardinality gives directional-sign cancellation, and exact t=7/8 witness has mu=88/23, epsilon=5/33, v=10/23. Independently built SymPy/rational block Jacobians on C6 and K3,3 confirm spectra and fourth-iterate norms, all rational coefficients and Hessian bounds. Finite checks corroborate only; the symbolic algebra and stochastic-matrix argument establish the universal quantified result.

## originality

PASS

Qualified best-of-knowledge originality of the combined critical-point-pinned logistic output-diffusion period-two curve, full spectrum on every finite connected regular bipartite graph, exact graph-uniform four-return infinity norm, and explicit graph/parameter-uniform basin radius. Two-color temporal waves, 1D Fourier reductions and generic local contraction are acknowledged prior art, not claimed as new. Current-source cross-checks distinguish stationary heterogeneous checkerboards and Chebyshev input coupling from this model. The 1993 higher-dimensional and 1997 two-dimensional primary articles were not accessible in full; their possible stronger implications remain named residual priority risks, not deemed disproved by searches or used as automatic FAIL.

## value

PASS

The natural object is a two-color anti-phase periodic state of a commonly studied output-diffusive logistic coupled-map lattice. A critical-point-pinned branch supplies a mathematically motivated exact solvable family: the vanishing derivative at one shore yields a nontrivial whole-network singular-mode simplification, rather than merely testing a tiny arbitrary graph. The exact parameter/domain characterization and sharp full-state two-step spectral radius combine with a topology/size/parameter-independent strictly sub-half four-return norm and explicit 1/174080 local basin. This is a quantitative robustness statement for arbitrary growing regular bipartite networks and is not implied by a numerical ordering observation or a pre-existing ring-wave stability table. The basin radius is conservative and its numerical value by itself is not the innovation; the uniformity and rigorous mechanism are the mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
