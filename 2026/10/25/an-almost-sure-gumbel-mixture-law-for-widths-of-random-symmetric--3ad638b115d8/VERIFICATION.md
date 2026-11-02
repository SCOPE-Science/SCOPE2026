---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The canonical zero-sum symmetric edge polytope has width w_G(U)=2 max_edges |U_i-U_j|. Gaussian normalization gives (sqrt(n-1)/2)w_G(U)=D_G(g)(1+o_P(1/log n)) uniformly over graphs, since b_n^2=O(log n). Opposite Gaussian extreme processes converge jointly to independent intensity exp(-x)dx Poisson processes; independent ER edge marks survive on every finite extreme window. The Poisson no-edge probability for all crosspairs above level t reduces, conditional on upper exp-transformed arrivals S_k, to exp(-e^(-t) sum_k p(1-p)^(k-1)/S_k). This produces H+log A_p, with A_p>0 finite. For any fixed t the change to f_n(G)=P_g(D_G<=2b_n+t/b_n) upon one edge flip is at most q_n=O(sqrt(log n)/n^2). McDiarmid yields exp(-c n^2/log n) graph concentration, summable for arbitrary couplings of ER marginals. Rational t and continuity yield almost-sure quenched weak convergence. The maximal and minimal Gaussian labels form one uniformly random unordered pair, proving exact coincidence probability |E|/binom(n,2). Splitting A_p=p/S_1+B with E B=-p log p yields sharp upper tail p t exp(-t). The finite 5-vertex exhaustive verification in supplied checker and independent simulation are diagnostic only.

## originality

PASS

Chen–Davis–Korchevskaia classify symmetric-edge-polytope facets via graph subgraphs, Braun–Bruegge–Kahle analyze random facet-supporting hyperplanes, and Donzelmann et al. establish CLTs for counts of edges/triangulation edges. None of the inspected theorems concerns uniform-DIRECTION spherical widths or derives the marked two-Gaussian-extreme Gumbel mixture and almost-sure graph quenched law. Exact deterministic coincidence probability is a useful component, but the central novelty is the complete second-order width distribution.

## value

PASS

For a canonical random symmetric edge polytope, a complete quenched second-order width law with explicit random shift and upper tail is a natural geometric probability result not reducible to known face-count CLTs. The exact coincidence identity also measures how random edge deletion affects extremal directions despite the unchanged first-order width. Fixed-p and Euclidean embedding restrictions are essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
