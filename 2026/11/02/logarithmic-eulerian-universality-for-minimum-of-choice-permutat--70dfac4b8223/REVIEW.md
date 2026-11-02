# Scientific review: logarithmic Eulerian universality

## Correctness — PASS
The model specifies independent sampling with replacement at every stage. Independent rank coordinates give exactly the adjacent-descent event and its finite-sample probability. A telescoping sum of squared power increments proves strictly negative one-step bias for every integer choice parameter at least two. The fixed-parameter polynomial power-sum expansion gives the logarithmic constant. Quantile coupling to independent minimum-of-uniform coordinates gives an explicit mean discrepancy bound and a Wasserstein lower bound from the expectations. Only adjacent indicator covariances contribute to variance; the Eulerian one-dependent block CLT and a logarithmic coupling remainder give the Gaussian limit. The independent standard-library checker passed 24,443 exact checks; finite enumeration is not used as the general proof.

## Originality — PASS, with residual risk
The exact independent-rank distribution is explicitly already in Travers (2014), Proposition 6, and is cited as input, not a new lemma. We compared the present **local adjacent-descent law, negative correction constant, and logarithmically sharp Wasserstein coupling** against Travers's full text, Jasińska--Ráth's global permuton and nonconsecutive-pattern results, Savage--Visontai's unweighted inversion-sequence Eulerian theory, Fang and collaborators' Mallows descent walks, and Borodin--Diaconis--Fulman's general one-dependent, uniform and Mallows descent results. The sources do not state or directly imply the quantified combination for the k-card-minimum model without additional arguments. The strongest priority risk is that existing general rank-process work could contain an unstated specialization or a historical equivalent not retrieved. Search absence is not proof of uniqueness.

## Mathematical value — PASS
A biased permutation model with pronounced nonuniform global inversion behavior nevertheless has asymptotically Eulerian local fluctuations. The explicit fixed-parameter logarithmic deficit, strict bias at every finite stage and matching logarithmic Wasserstein upper/lower orders quantify a natural local/global contrast and permit approximation by an exactly known reference law. The result is not an arbitrary parameter slice: it covers all fixed positive choice parameters and all finite sizes, with a sharp asymptotic order and a reproducible coupling.

## Boundaries
Statements about the CLT and logarithmic remainder require fixed choice parameter; neither a sharp Wasserstein leading constant nor a local limit is claimed. Independent historical-priority evaluation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
