# Scientific review: transient habitat occupancy ranking reversals

## Correctness — PASS

The affine occupancy equations give exact exponential trajectories for all rates and initial probabilities in the stated domain. Once the two relaxation rates are ordered, the difference has the form \(A(t)=d+u e^{-r_f t}-v e^{-r_s t}\) with strictly positive initial and limiting values. Its derivative has at most one zero. The derivative can form a negative minimum exactly when \(u,v>0\), \(r_fu>r_sv\), and \(d<m\), so continuity and strict monotonicity give exactly two positive simple zeros; otherwise there cannot be two. At equality the minimum is a tangency. The second derivative at the minimum equals \(r_fr_sm\), proving the local square-root duration law. An interior exact-rational counterintuitive example passes sign checks; finite randomized tests are supplementary rather than infinite proofs.

## Originality — PASS, with residual risk

Levins (1969) addresses migration/extinction and heterogeneity, not a two-habitat transient ranking. MacKenzie et al. (2003) focuses on detection-adjusted estimation, not this mean-difference phase diagram. Yackulic et al. (2015) is a materially close primary source: the accessed theoretical sections investigate transient habitat association and show a single directional sign change from invasion/empty starting conditions, but do not exhibit or classify **two strictly positive reversal times with both nonzero initial occupancies and the same initial and final ordering**. The generic exponential-zero bound alone does not certify a biologically feasible two-reversal regime or threshold. Published-record searches and accessible prior claim comparisons revealed no dominating statement. The full 2015 publisher view/supplements could not be completely retrieved and generic exponential-polynomial literature remains a priority risk.

## Mathematical value — PASS

This is a complete, sharp parameter criterion for an ecologically meaningful counterintuitive transient: the apparently favored habitat at both endpoints can be disfavored between two distinct times without any change in underlying colonization/extinction rates. It gives two necessary physical mechanisms (simultaneous above-equilibrium or below-equilibrium relaxation, with the correct faster habitat), a strictly interior robust witness, and the exact square-root disappearance law that quantitatively describes how long the reversed ranking persists. These address the interpretation of longitudinal occupancy surveys, rather than a gratuitous parameter substitution. No claim is made about field frequencies, observation error, or priority certification.

## Closest literature and limits

Yackulic et al. (2015), DOI 10.1890/14-1361.1, explicitly explores transient habitat differences; overlap is confined to the model family and one-crossing scenarios, not the joint two-reversal criterion, based on accessible theoretical material. MacKenzie et al. (2003), DOI 10.1890/02-3090, describes the discrete survey/detection framework, and Levins (1969), DOI 10.1093/besa/15.3.237, supplies the older habitat-heterogeneity background. An inaccessible complete publisher presentation of the 2015 source and potential general exponential-sum results remain residual risks. The theorem does not apply to interacting habitats, temporally varying rates, or imperfect observations.

Self-review: passed. Independent audit: not yet performed.
