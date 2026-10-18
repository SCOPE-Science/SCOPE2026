# Self-review

## Correctness: PASS

For any incidence table, the Galois concept pairs correspond bijectively to maximal independent sets of the bipartite graph of missing incidences (including empty-side concepts). Maximal-independent-set counts multiply over connected components. For every fixed two-colored tree type, the component expectation and \(O(n)\) variance follow by counting labeled embeddings and forbidden outside edges. Components with a fixed positive cycle have only \(O(1)\) expected copies. The subcritical Galton–Watson domination controls large components in mean, permitting the finite-type sums to converge in \(L^1\) to the absolutely convergent series. The first three sizes of trees give the stated cubic expansion. The standalone code independently checked 1,226 finite contexts and each tested tree recurrence; it does not replace the asymptotic proof.

## Originality: PASS, with residual risk

The 2020 formal-context null-model paper supplies the model but no subcritical typical entropy theorem. Sakurai's 2021 paper gives expected concept counts and a superpolynomial lower bound for constant incidence density, not the near-one regime or a normalized logarithm law. Drmota et al. 2018 address average *counts* and size distributions of maximal independent sets in uniformly sampled tree/series-parallel graph classes, not the quenched logarithm of a random sparse bipartite graph's total MIS count. Jenssen et al. 2023 count all independent sets for approximation algorithms, not maximal independent sets. Previously documented mathematical results on fixed-density, sparse-incidence, and critical-incidence random contexts do not imply the near-complete formula. Semantic searches for missing-incidence, complement, random bipartite MIS, typical logarithm, and tree-entropy formulations did not reveal a dominating result. This is not proof of global priority: older general random-graph additive-functional laws may cover the limit as a corollary.

## Mathematical value: PASS

The object is the number of semantic fixed points of a Bernoulli formal context, a natural complexity measure. In the near-complete regime, the deterministic complete table has only one concept but a vanishing fraction of missing incidences produces exponentially many with an *exact positive entropy per object*. The coefficient is computable via a local tree recursion with exponential truncation error, and the first nonlinear small-density correction detects four-vertex path components through \(\log3\). This gives more than a generic existence bound, elementary parameter renaming, or a single finite enumeration.

## Boundaries and literature

The claim covers \(0<c<1\), not criticality at one, other aspect ratios, the limiting law of fluctuations, or the logarithm of the expected number of concepts. Historical accessibility limits and the possibility of equivalent results under graph additive-functionals are stated in the audit. The proof uses standard component and branching ingredients, which are not claimed individually new.

Self-review: passed. Independent audit: not yet performed.
