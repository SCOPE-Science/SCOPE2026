# Review

## Correctness

**PASS.** Conditioning on one vertex being isolated restricts all remaining points independently to one arc of length \(1-2r\); integrating the triangular two-point separation law yields the exact conditional edge probability. This gives a closed mixed-moment formula. The sign theorem then follows from a discriminant-negative five-vertex polynomial, strict monotonicity of the sign expression in vertex count, and its explicit quadratic/linear zero locations. The edge case \(n=2\), the branch point \(r=1/3\), and both zero-covariance endpoints are explicitly covered. The independent discrete-circle enumerator and algebraic checker passed 653 assertions; unrestricted quantifiers are justified by the integral/algebraic proof.

## Originality

**PASS on inspected evidence.** Last–Nestmann–Schulte (2018) treat Poisson component-count covariance, Badiu–Coon (2021) treat interval random-graph structural entropy, and Wilsher–Dettmann–Ganesh (2022) treat isolated-node limits for soft periodic random graphs and explicitly exclude the hard connection function. None of these inspected texts states or subsumes the two exact finite-\(n\) isolation/total-edge covariance sign boundaries. Searches for equivalent circle/torus notation, occupancy identities, thresholds, and the exact six-vertex window did not surface a dominating result. Priority risk remains from older random-geometric-graph general moment formulas, including uninspected portions of book literature: the elementary conditional identity may be latent in them.

## Value

**PASS.** The two basic network statistics have conflicting local and global influences: a marked isolated vertex destroys incident edges but forces the remaining points into a shorter arc, increasing their mutual edge density. The theorem gives a sharp sign phase diagram for *all* vertex counts and radii, including the unexpectedly positive regime, a minimal positive size of six, both transition radii and their asymptotic scaling. It supplies more than a re-expression of a known mean or a routine single-parameter inequality.

## Limitations

Only the fixed-size uniform periodic hard model is covered. The exact sign classification does not transfer automatically to interval, Poisson, nonuniform, higher-dimensional or soft graphs. Older general moment methods could implicitly contain the evaluated cross moment; independent historical priority verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
