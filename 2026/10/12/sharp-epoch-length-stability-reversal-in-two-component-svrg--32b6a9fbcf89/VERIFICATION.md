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

For any a_1,a_2>0 distinct, mu=(a1+a2)/2>0 and z=((a1-a2)/(a1+a2))^2 in (0,1), iid signed-curvature noise yields the exact normalized last-snapshot recurrence y_j=(1-t-t xi_j)y_{j-1}+t xi_j. Because y_1=1-t and the Walsh monomials in xi_2,xi_3 are orthogonal, conditional epoch factors are exactly F2=(1-t)^4+zt^4 and F3=(1-t)^6+zt^4((1-t)^2+(2-t)^2)+z^2t^6. Independence across epochs yields E[s_k^2]=F_m(t,z)^k s0^2, so both strict necessity and sufficiency (including endpoint nonconvergence for nonzero s0) follow, and fixed finite inner-index moments inherit convergence. For F2, the unique cutoff is monotone after t=1. For F3, the degree-6 Bernstein coefficient pattern b=(1,0,0,0,z/3,2z/3,z(1+z)) and Descartes sign argument give at most one root for 0<t<1, and the expanded derivative in y=t-1 is strictly positive on t>=1. Together there is exactly one positive cutoff. At t=tau2, z=(2-t)(t^2-2t+2)/t^3 decreases strictly, and F3-1=(t-2)C(t), C(t)=2t^3-8t^2+13t-8, with C strictly increasing; hence exactly one threshold t_c and one z_c root of 128z^3-41z^2+6z-1. Strict rational witnesses show both directions. Independent SymPy expansion and exact rational branch sums reproduced moment factors, Bernstein coefficients, crossing identity, derivative signs, root intervals and both witnesses. Finite sampled parameter roots only corroborate the analytic proof; no higher epochs/nonquadratics are claimed.

## originality

PASS

The algorithm itself is Johnson--Zhang Option I prior work. The new scope is an exact necessary-and-sufficient scalar mean-square cutoff for the two smallest nontrivial fixed last-snapshot epoch lengths and its uniquely signed heterogeneity crossing. Reviewed original and proximal SVRG literature, Free-SVRG and quadratic Q-SVRG, plus complete published exact-frontier sources for Loopless SVRG and PAGE; their different snapshot/estimator state recurrences or only sufficient guarantees do not imply this fixed-epoch comparison. Search results for the exact crossing cubic also yielded no matching published prior. This is a qualified best-of-knowledge judgment, not a proof of historical nonexistence.

## value

PASS

The first stochastic last-iterate epoch is m=2 (m=1 is deterministic). Comparing m=2 with m=3 is a structurally motivated minimal change in a standard variance-reduced method, not an arbitrary numerical slice. The exact z_c phase transition proves a nonmonotonic direction: an added inner update expands mean-square admissible stepsizes for lower curvature heterogeneity but shrinks them for higher heterogeneity. Two exact positive-curvature rational witnesses establish both regimes and the unique cubic provides a sharp parameter discriminator. This is a self-contained theoretically useful counterexample and exact classification; no universal practical epoch-cost recommendation or higher-dimensional extrapolation is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
