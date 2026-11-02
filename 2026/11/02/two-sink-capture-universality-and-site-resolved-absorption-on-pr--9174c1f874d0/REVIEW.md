# Scientific assessment

## Correctness — PASS

The proof uses the exact three-eigenvalue adjacency algebra for primitive strongly regular graphs and the strict spectral inequalities of both the graph and its complement to make two nonprincipal sink Gram matrices invertible. It identifies the exact five-dimensional bright space, establishes the absence of nondecaying bright modes for **any** two positive sink rates, and evaluates the diagonal projector. Algebraic class counts give the full site distribution and both universal averages. All quantifiers, initial-state normalizations, strict positivity hypotheses and imprimitive boundary are stated. The packaged `verify.py` checks 598 sink pairs and 8,849 individual site comparisons across seven independent graph instances, and `exact_examples.py` supplies exact fraction checks. Their output is recorded in `verification_output.txt`. Finite numerical checks are supporting evidence, not the infinite-family argument.

## Originality — PASS, with historical priority risk

Novo et al. (arXiv:1412.7209) and Razzoli et al. (arXiv:2011.13794) cover the general Krylov/single-sink transport framework; neither inspected full text asserts the two-sink strongly regular site-distribution theorem. Li et al. (2019; DOI 10.1007/s11128-019-2250-5) is a particularly close two-marked-vertex study using real Hermitian loop potentials and unitary spatial search, rather than irreversible capture. Its full text could not be inspected, so the possibility of a broader relevant theorem in it remains a priority risk. The aggregate \(5/v\) law for individual special graph families does not alone establish the all-primitive, parameter-only site-resolved law. Neither a failed text search nor the absence of a matching title proves uniqueness; the examined evidence supports provisional originality of the precise combined theorem.

## Value — PASS

This is a natural exact absorption benchmark for the entire infinite class of primitive strongly regular quantum networks, including graphs without vertex transitivity. It shows experimentally distinguishable *site-resolved* absorption statistics can be blind to graph isomorphism once the parameters and sink adjacency agree (for example, the nonisomorphic Shrikhande and rook graphs). It sharply separates the primitive rank-five law from failure in complete multipartite imprimitive examples and yields exact normalization-independent averages. This is more than a direct single-trap renaming or a finite table.

## Scope and limitations

All findings require classical finite graph adjacency, uniform coherent hopping, two strictly positive irreversible sink rates and infinite-time one-excitation capture; no decoherence or additional sinks. Unavailable full historical text and future independent comparison could change the novelty assessment.

Self-review: passed. Independent audit: not yet performed.
