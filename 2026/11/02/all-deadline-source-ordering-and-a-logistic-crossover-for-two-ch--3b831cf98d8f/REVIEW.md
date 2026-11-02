# Scientific review

## Correctness
PASS. The model specifies both replacement and alternating bipartite steps. A nonanticipating greedy count coupling proves optimality at every deadline. An exact independent-geometric collector representation gives all finite CDFs. The nonstandard source-order lemma is proved using a positivity-preserving geometric increment factorization and the log-concavity of convolutions; it is not inferred from numerical testing. The source expectation difference is an exact identity bounded by one. The Gumbel and logistic limits follow from a controlled small/large-geometric-summand split and convergence of independent maxima. The packaged standard-library checker independently evaluates small-state Bellman recursions and passes 4,661 finite assertions/diagnostics. Finite checking does not certify infinite quantifiers.

## Originality
PASS with historical-priority qualification. The previous complete-graph and general two-choice-walk results, fixed-source greediness on bicliques, and existing single-collector coupon asymptotics are not claimed as new. The comparison isolates an all-deadline **source-part** comparison and its exact signed logistic critical window, not merely a rephrased one-collector Gumbel theorem. The inspected primary works [1]–[3] do not state these graph/source results. Other work might imply the comparison indirectly; no claim of exhaustive literature priority is made.

## Value
PASS. Source placement is a natural finite-horizon optimization problem, and its stochastic ordering is an exact classification for every complete bipartite size and deadline. The one-step universal ceiling and nontrivial logistic critical window reveal a sharply structured but quantitatively small source effect, while the accompanying Gumbel soft maximum describes competing cover-time bottlenecks. This provides a full benchmark beyond a leading-order expected-time calculation; it is not presented as a substantial runtime speedup.

## Scope and residual risks
The one-collector coupon-collection component is strongly related to known results, including the distinct-offer variant in [3]. Independent historical verification and independent mathematical audit are not available. The theorem does not cover non-bipartite graphs or alternative choice mechanisms.

Self-review: passed. Independent audit: not yet performed.
