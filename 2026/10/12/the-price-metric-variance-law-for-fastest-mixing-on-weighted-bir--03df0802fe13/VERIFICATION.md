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

PASS: For every n>=2, positive normalized stationary masses pi and prices c, define g_i=sqrt(c_i), cumulative s_j, D=Var_pi(s)>0, P_i=sum_{j<=i}pi_j, G_ij=P_min(i,j)(1-P_max(i,j))>0 and F=Gg. The nested-indicator identity Var_pi(f)=d^T G d was reconstructed. Test f=s yields gamma(w)<=1/D for all feasible ∑ c_i w_i=1. Candidate w_i=F_i/(Dg_i)>0 has exact budget 1; direct expansion establishes ∑w_i d_i²−D^{-1}d^T G d=(2D)^{-1}∑G_ij g_i g_j(d_i/g_i−d_j/g_j)^2>=0 for every gradient, proving attainment and simplicity, including n=2. Any optimum has s as lowest eigenvector, and telescoping its first i equations forces w_i=F_i/(Dg_i), hence uniqueness even against disconnected boundary. Differentiation gives ∂gamma*/∂c_i=−gamma*w_i. Independently compared 340 nonsquare-price/mass random instances (n=2..18) with direct generalized symmetric eigenspectrum; worst relative error 1.69e-14; finite checks are not the all-real proof.

## originality

PASS

PASS, bounded priority risk: Fiedler (1990) and Göring–Helmberg–Wappler (2005) optimize unweighted vertex Laplacian with uniform total conductance budget, covering only uniform-mass/unit-price specialization. Boyd et al. (2006) treats discrete-time SLEM for uniform stationary chain; Wan et al. (2008) covers uniform tree allocation; generalized node/edge-weight SDP of Shafi–Arcak–El Ghaoui (2010) formulates but does not state the all-parameter explicit optimal rates. The precise simultaneously heterogeneous mass and individual price square-root variance/flux law was not found in inspected statements or Resultary. Fiedler 1990 full text inaccessible (authorized institutional access disconnected), so any hidden generalized formulation is a real residual priority risk, not an automatic FAIL.

## value

PASS

PASS: Designing fastest-relaxing reversible birth-death dynamics with prescribed heterogeneous equilibrium and per-edge conductance prices is a natural complete resource-allocation family. The theorem yields unique positive *all* optimal rates, exact spectral gap, simple eigenmode, sensitivity, and O(n) algorithm, replacing numerical SDPs across a continuous multi-parameter domain. It is neither a renaming of equal-cost uniform tree models nor merely a finite invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
