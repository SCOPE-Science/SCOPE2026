# Review of an alternating-habitat dispersal threshold

## Correctness — PASS

The full two-season product is \((J P_c(d) D_1)^2\), and its annual spectral growth multiplier is the largest eigenvalue of a fixed-diagonal-similarity symmetric matrix. For \(B>b>0\) and \(0<c\le1\), its closed-form expression is a strictly convex function of the migration fraction \(d\). The endpoint comparison gives the exact optimal-strategy switch at \(c=\sqrt{b/B}\), with no optimal interior point even at equality. Differentiation yields the quantitative uniform gap. The program independently checks exact matrix products, the characteristic discriminant, and a rational positivity certificate at the nontrivial equality witness. No finite computation is used as a universal proof.

## Originality — PASS (with residual bibliographic risk)

McPeek and Holt (1992) analyze a density-regulated ecological dispersal model and explicitly assume no deaths during dispersal in their original model description. Schreiber and Li (2010) analyze periodic dispersal and evolutionary stability under explicitly cost-free migration; their accessible full preprint calls finite dispersal costs a mathematical challenge. That general cost-free result encompasses part of the present \(c=1\) limit but does not establish the all-parameter threshold under trip survival \(0<c<1\) or its strictly positive interior penalty. Hutson et al. (2001) study a different reaction–diffusion selection system. A 2015 life-cycle study incorporates direct migration costs but the complete material was inaccessible; it is retained as a possible closer source. The exact result is not asserted to be bibliographically unique without further independent checking.

## Mathematical value — PASS

A complete optimization classification is obtained for a motivated seasonal source–sink caricature, including a sharp cost phase boundary, a genuine endpoint tie without partial-strategy indifference, and an explicit penalty for compromise dispersal. These statements distinguish demographic growth optimization from the well-studied competition/ESS problem and give a precise benchmark for models where migrating is costly. The narrow model is an exact reference point rather than an empirical prediction.

## Limits

The fixed strategy is optimized against zero density and a deterministic exactly alternating landscape. The result is not about stochastic persistence, density dependence, or selection in a polymorphic population. The closest ecology and mathematical population papers should be checked again in a separate independent bibliographic review; unavailable full texts remain a novelty risk.

Self-review: passed. Independent audit: not yet performed.
