# Scientific review

## Correctness (PASS)

The joint probability is obtained by independently ordering the distinct first-occurrence prefix and specifying the repeat label. For each pair of unequal category probabilities, cancellation of positive factors reduces adjacent-time conditional odds to the strict Newton difference \(e_s(q)^2-e_{s-1}(q)e_{s+1}(q)>0\). Endpoint values are covered using the explicit zero conventions, including the two-label case. Likelihood-ratio ordering on the finite support gives a strictly decreasing conditional expectation of every increasing function of category probability, hence the stated strict negative covariance for every strictly increasing time transform. Independence holds exactly when early quadratic-size-biased and late original-mass distributions agree; positivity then forces uniformity. Exact rational independent prefix enumeration passed 2,235 assertions across 25 positive vectors of lengths two to six. Finite checks are not presented as an infinite proof.

## Originality (PASS, qualified)

The important prior benchmark is Camarri–Pitman, whose equations (1) and (13) give first-repeat time and observed-set laws for unequal sampling probabilities; the joint collision-label identity is an immediate refinement, not claimed as independently new. Flajolet–Gardy–Thimonier previously obtained nonuniform birthday waiting-time identities, and Fadnavis established different Schur-concavity results. Distinct from these is an all-size, all-positive-vector **strict MLR ordering of the first repeated label conditional on each waiting time**, with its uniformity characterization and transformed negative-dependence corollary. Full-text review of the core accessible sources found no equivalent statement. The inaccessible full text of Holst (1995) and uninspected older literature remain residual priority risks, not evidence of uniqueness. Identical or stronger theorems could still be present in other sources.

## Mathematical value (PASS)

The type of the first collision and its waiting time are two basic but different observables of nonuniform occupancy sampling. An exact MLR order is substantially stronger than an isolated covariance: it simultaneously determines the direction of every monotone conditional expectation, provides strict covariance inequalities for arbitrary monotone transforms, and detects uniformity through independence. The transition from early quadratic-size bias to late ordinary mass gives the result a natural interpretation relevant to heterogeneous hash collisions, duplicate identifiers, and unequal-species sampling. These are exact finite-sample laws, not ad hoc parameter choices or table entries.

## Closest literature and limitations

Camarri–Pitman (1998/2000) contains the precursor marginal/set laws, and Flajolet–Gardy–Thimonier (1987/1992) treats nonuniform birthday expectations. The novelty claim excludes those known formulas; their existence makes historical-priority assessment necessarily qualified. Holst (1995) was accessible by abstract only. The proof assumes strictly positive masses and a finite set of labels. No independent review has occurred.

Self-review: passed. Independent audit: not yet performed.
