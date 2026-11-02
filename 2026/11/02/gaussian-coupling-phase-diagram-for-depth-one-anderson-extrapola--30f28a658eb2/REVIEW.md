# Review of the Gaussian-coupling theorem

## Correctness — PASS

The Anderson algebra reduces exactly to the ratio of independent Gaussian sum and difference modes, including both singular covariance endpoints. Its denominators are almost surely nonzero. The denominator-window integration, bounded density and finite Gaussian absolute moment yield the sharp positive \(t^{-1}\) constant; the tail integral gives the exact moment boundary. Exceptional endpoint distributions follow by substitution, while a one-variable logarithmic derivative proves the unique worst correlation when the trials are centered. All quantifiers, the fixed trial-point requirement, positive noise scale, strict affine contraction, and endpoint cases are stated. Exact-fraction and Gaussian-window checks reproduce representative identities and limits; experiments alone are not used as proofs.

## Originality — PASS (qualified)

The stochastic mixing algorithm of Wei, Bao and Liu (2021), inspected through its method and proof sections, employs damping and adaptive regularization for stability and does not state a complete unregularized two-evaluation Gaussian-correlation phase diagram. Scieur, d'Aspremont and Bach (2017), inspected through its stochastic stability and convergence results, treats regularized extrapolation bounds rather than this exact distributional classification. Earlier Anderson convergence theory imposes different hypotheses, and Gaussian ratio tails are classical; neither fact alone claims the theorem's coupling-dependent exceptional regimes and unique maximal tail coefficient. The indexed deterministic depth-one counterexample concerns positivity loss in two dimensions rather than stochastic tails in one dimension. A 2017 analysis of inaccurate Anderson evaluations could be especially relevant; its full body was inaccessible, so publication priority and possible overlap remain explicit risks, not established exclusions.

## Value — PASS

The correlation of two equally accurate Gaussian evaluations, rather than just their separate variances, controls whether unsafeguarded Anderson extrapolation has any finite first absolute error moment. Both extreme noise couplings avoid the reciprocal tail for centered trials, yet the worst extreme-tail risk is uniquely interior, with an explicit testable correlation and coefficient. This distinguishes noisy extrapolation from deterministic contraction and gives an exact benchmark for noise reuse, antithetic sampling, and safeguard design without claiming a convergence theorem for any regularized method.

## Literature and limitations

Sources inspected: Wei–Bao–Liu (arXiv:2110.01543) and Scieur–d'Aspremont–Bach (arXiv:1706.07270), both full HTML text in relevant sections; Toth and collaborators (DOI:10.1137/16M1080677), abstract and opening-page publisher preview only. Classical Gaussian ratios, deterministic Anderson mixing and regularized stochastic methods are background. The result is a one-output, two-fixed-point scalar Gaussian model; the exact antithetic equality presumes trial centering at the actual fixed point. Independently validating the proof and searching inaccessible specialized work remain appropriate before any publication-priority claim.

Self-review: passed. Independent audit: not yet performed.
