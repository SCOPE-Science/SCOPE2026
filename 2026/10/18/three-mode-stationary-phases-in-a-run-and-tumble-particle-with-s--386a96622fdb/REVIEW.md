# Self-review

**Finding reviewed:** Three-mode stationary phases in a run-and-tumble particle with saturating rates.

## Correctness — PASS

The right/left transport equations and integrability imply a zero-flux stationary density. Differentiating it yields the exact log-derivative with a positive prefactor and the sign-controlling polynomial \(Q(y)\), where \(y=\tanh^2(ux)\). The fourfold hyperbolic-tangent identity is elementary and verified independently. Strict concavity \(Q''(y)=-2(5k+m)-6ky<0\), the endpoint \(Q(1)=-8m-2n<0\), and origin sign conditions prove the exhaustive one-/two-/three-maximum cases for \(g=4u\), including degenerate flat cases. The rational witness has \(Q(0)=-3/16\), \(Q(1/4)=49/256\), and \(Q(1)=-7/2\), hence exactly two simple positive roots, producing precisely three nondegenerate local maxima and two minima. The implicit function theorem gives persistence in the full parameter space. The standalone checker passed 6,407 rational and independent numerical derivative checks. The infinite-domain modal classification is proved analytically; the checks are corroborating evidence.

## Originality — PASS with residual priority risk

Jain and Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521 (first posted 22 May 2024), provide the model and stationary solution. Their modal discussion uses an explicitly assumed maximum count of two in deriving an origin-curvature criterion. It supplies neither the fourfold-steepness cubic trichotomy nor an admissible three-peak stationary example. Monthus, arXiv:2103.08885, supplies the broader zero-current formula but not the stationary peak classification. Bressloff, arXiv:2102.10372, studies a constant-speed inhomogeneous-switching trapping regime, not the joint varying-speed model. Published findings searches for stationary trimodality, aliases, exact parameters, and polynomial classification did not identify an identical or logically stronger prior result. The general stationary formula and previous mode calculations are acknowledged, rather than appropriated. Residual risk: an unlocated paper could previously have applied the general stationary formula to reveal three stationary peaks; independent priority review remains appropriate.

## Value — PASS

The number of stationary density maxima is a physically meaningful shape feature of active-particle localization. Existing origin-curvature analysis is insufficient when outer extrema coexist with a central peak; the proved three-mode region makes that mathematical limitation substantive, not cosmetic. The complete slice trichotomy, exact positive parameter witness, nondegenerate extrema, and open persistence establish a qualitative phase excluded by the earlier two-maximum assumption. This is more than a routine parameter substitution or an unexplained isolated computation.

## Closest work and limits

Primary model and most directly implicated passage: Jain and Chatterjee (2024), arXiv:2405.13521, equations (1)–(17) and the discussion immediately before the assumed unimodal/bimodal criterion. General formula: Monthus (2021), arXiv:2103.08885, Section II. Related trapping geometry: Bressloff (2021), arXiv:2102.10372, Sections II–III. The complete peak count is restricted to \(g=4u\); nearby three-peak persistence does not establish a global bound for all steepness ratios. External independent validation and priority assessment have not been performed.

Self-review: passed. Independent audit: not yet performed.
