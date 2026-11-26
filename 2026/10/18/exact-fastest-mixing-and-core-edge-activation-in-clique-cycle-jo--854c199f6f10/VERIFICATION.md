---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Averaging over core permutations and cycle dihedral symmetries preserves feasibility and cannot increase the centered spectral norm. On invariant kernels the mean-zero eigenvalues are 1-(k+m)a, 1-ma-kc, and 1-ka-b times the cycle Laplacian in the precise sense 1-ka-bD_j. The first two sectors are the set contrast and core-sum-zero space. For feasible a, c=(1-ma)/k nulls the core sector; the unique balancing of the two rim endpoints is feasible because delta+Delta>4 (for odd m use cos(pi/m)>cos(2pi/m)). At the claimed optimum ka<1, so the rim holding is strictly positive. On the increasing branch of |1-(k+m)a|, the unique intersection with the strictly decreasing rim bound is a0. The constraint a<=1/m truncates at a_*; both 1/m and 1/k exceed the contrast zero, and a0<1/k. The rim bound is active even at truncation, forcing the stated b in every invariant optimum. The remaining core eigenvalue inequality and row budget give precisely the claimed c interval. Saturation at k<=tau forces averaged core entries including the diagonal to vanish, hence each original such entry vanishes by nonnegativity. For k>tau the lower spectral constraint has numerator k(1+rho)-2m rho: zero core edges remain feasible at k=2tau, and the nonzero choice c_* is feasible throughout k>tau. Beyond 2tau an entirely zero core off-diagonal would survive averaging and contradict the positive invariant lower bound. The large-size branch limits agree at alpha=1/2. Inspected verify.py and requirements.txt without executing frozen code; its LP concerns only invariant kernels. Independently applied full rational transition matrices to the constant, contrast, core and five rim modes at (k,m)=(2,6),(3,6),(6,6), reproducing 2/5, 1/3, 3/13. Replay: python3 /workspace/branches/independent_finite_checks.py (check 5). The proof, not the finite replay, decides the unrestricted result. In RESULT.md line 87, 'positive-branch' is the increasing absolute-value branch, with negative contrast eigenvalue.

## originality

PASS

Credit the known wheel solution, orbit averaging and clique-lift theorem, including the latter's canonical lifting allocation. The established distinct content is the explicit nonuniform-wheel minimax for the family, the entire invariant optimal core interval, the global core-support cutoffs, and the associated size limit. The strongest matched same-date catalogue result gives support phases on a different rim graph, not implied equivalence; order within that date is not established.

## value

PASS

The multi-hub periodic network is a motivated extension of the standard fastest-mixing wheel. Exact support constraints answer whether internal edges must be absent, may be used, or are unavoidable even for nonsymmetric allocations (with the kernel itself still reversible and symmetric as a matrix). The interval and the limiting size thresholds give usable quantitative design information not supplied by the canonical lift alone. This does not classify all noninvariant optimizers or quantify finite-time total variation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
