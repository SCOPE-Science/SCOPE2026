# Scientific review — weighted odd-cycle SDP gap onset

## Correctness (C): PASS
The sign-alternating vector substitution rewrites the objective as one endpoint chord reward minus positive path chord costs. Weighted Cauchy proves exactness up to the reciprocal-weight threshold and characterizes its equality case. The great-circle contraction lemma reduces the optimum to a planar monotone path; strict local convexity gives the equations \(b_j\sin\delta_j=\lambda\). Expanding the resulting scalar stationary equation and applying the envelope formula verifies the exact coefficient \(3S^4/[4(S^3-T)]\). The nonzero coefficient and a compactness argument exclude a distant competing optimum near criticality. The supporting standard-library script checks independent numerical instances but is not used to prove arbitrary-weight claims.

## Originality (O): PASS, with access-limited risk
The primary SDP paper by Goemans and Williamson exhibits the unit-vector formulation and an unweighted five-cycle but not the path-weight-dependent critical curvature. Later full-text work on MaxCut strict complementarity and computational complexity addresses different questions. The closest public mathematical record on weighted odd cycles concerns a fourth-power energy and a Sturm--Liouville limit, not a Max-Cut SDP gap. An equal-path-weight one-edge family gives only the symmetric specialization and does not imply the arbitrary positive-weight third-reciprocal-moment formula. **Important limitation:** full texts of two relevant Delorme--Poljak 1993 papers were unavailable, so possible stronger spectral-cycle coverage is unresolved and no exhaustive novelty certification is claimed.

## Mathematical value (V): PASS
The exactness threshold alone misses how quickly the optimal SDP certificate becomes inexact. The curvature coefficient quantifies that onset for all positive path profiles, while the square-root angle response identifies the emerging optimizer. At fixed critical effective resistance the coefficient is minimized uniquely for a uniform path and becomes arbitrarily large under heterogeneous weights, providing a sharp and nontrivial sensitivity law.

## Limitations and closest literature
The theorem is local for positive fixed weights, not global across all closing-edge weights. The closest sources are Delorme--Poljak (1993), Goemans--Williamson (1994/1995), de Carli Silva--Tunçel (2018), and Bhardwaj (2026). No claim of independent review is made.

Self-review: passed. Independent audit: not yet performed.
