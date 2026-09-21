# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof reduces quantized Fisher information to the conditional expectation of the full location score on each quantizer cell. The exact identity
\[
J-J_Q(\theta)=\mathbb E_\theta[\operatorname{Var}(S_\theta(X)\mid Q(X))]
\]
shows that equality holds exactly when the score is almost everywhere constant on every shifted cell. Positivity of the density turns this into a Lebesgue-a.e. statement, and the fixed interval boundaries then force all essential score changes to lie among the shifted thresholds. This gives the translate-containment criterion \(K+\theta\subseteq T\) without an approximation step.

The simultaneous-location result follows by unioning the required translated knot sets. The finite-real-line sumset inequality \(|K+\Theta|\ge |K|+|\Theta|-1\) yields the cardinality bound. The arithmetic-progression construction attains the bound. The universal extremal classification is also forced: an integrable full-support density cannot have zero score knots, while one knot gives exactly an asymmetric Laplace density with opposite-sign tail scores.

Checks against possible hidden hypotheses included the two infinite outer cells, the sign convention under translation, repeated nonadjacent score values, minimality of the knot set, and the possibility of non-finite-step scores. None changes the equivalence. A compact numerical verification artifact separately checks the asymmetric-Laplace equality at aligned thresholds and strict loss away from thresholds, together with the sharp sumset construction.

## Originality

PASS, to the best of our knowledge, with a material residual literature risk explicitly retained.

The one-location information monotonicity and equality mechanism are established prior art and are not claimed. Hobza, Molina and Vajda (2005), Theorem 3.1, give an if-and-only-if equality condition for interval quantization of location models in a probability-coordinate formulation. Cabral Farias and Brossier (2013) give the score-projection loss identity and explicitly note exact binary preservation for a Laplace location model when the threshold is placed at the true location.

The claimed contribution begins only after fixing one quantizer while allowing the location parameter to vary: the full lossless-location set as a translate-incidence set, the exact threshold budget for a finite collection of target locations, the sharp sumset cardinality bound, and the asymmetric-Laplace uniqueness statement for the maximal number of exactly lossless locations. Searches using Fisher-information preservation, discretized/grouped observations, fixed quantizers, location families, piecewise-exponential scores, Laplace/double-exponential models, threshold alignment, and equivalent score formulations did not locate these statements.

The closest unresolved source is Pötzelberger and Felsenstein (1993), DOI 10.1080/00949659308811499. Its bibliographic metadata and abstract establish that it studies finite interval partitions, Fisher-information loss for location parameters, and double-exponential examples. A complete theorem-level inspection was not available here, so it remains the strongest source capable of containing an equivalent special case or formulation. This uncertainty is scientifically relevant but is not evidence of coverage. Mayoral et al. (2003) and Hobza et al. (2005) were also checked as later members of the same literature line; the accessible Hobza theorem confirms the one-location equality criterion but does not supply the fixed-quantizer multi-location sumset law claimed here.

## Value

PASS.

The theorem converts a local equality condition into an exact global design law for a quantizer that cannot track the unknown location. It gives a finite combinatorial obstruction to exact information preservation, an exact cell complexity for prescribed target locations, and a sharp extremal family. It also cleanly separates Laplace-type models, where exact preservation is possible at finitely many aligned locations, from smooth common location models, where every finite fixed interval quantizer loses Fisher information at every location.

## Scientific limitations

The setting is one-dimensional, full-support, deterministic interval quantization with finite nonzero location Fisher information. The theorem does not treat multidimensional parameters, vector quantizers, randomized/non-interval cells, adaptive quantizers, finite-sample decision risk, global sufficiency, or approximate near-losslessness. Exact equality is a local Fisher-information statement and should not be interpreted as equality of statistical experiments. The incomplete theorem-level access to Pötzelberger--Felsenstein (1993) is the principal originality uncertainty.
