# Independent mathematical audit

## correctness

PASS

For an actual code, the first-letter set A and last-letter set c(A) are disjoint, hence A is a partial transversal with a<=h. Under allowed first-letter set A, unused-middle-letter reverse-complement pairs contribute a²(h−a) independent 2-word orbits; used-middle orbits correspond to nonloop arcs on A, where opposite arc directions conflict but distinct chosen first letters are compatible. Each undirected pair contributes 2(1+x²)^a−1. All words appear in size-two reverse-complement orbits since the complement is fixed-point-free and length is odd. Allowed-vs-exact A is corrected by binomial inversion, giving precisely the polynomial. At h=1 only the empty code remains; for h>=2 the maximum h²(h−1) and 2^{h+binom(h,2)} optimum codebooks are correct but previously known. Independently enumerated all reverse-complement orbits, built pairwise word compatibility, and counted every clique for alphabets q=2,4,6; the histograms [1], [1,12,8], and [1,60,726,3072,6276,7344,5256,2304,576,64] match the formula. Universal proof is combinatorial, not finite enumeration.

## originality

PASS

Best-of-knowledge PASS ONLY for the complete nonmaximal all-size generating polynomial. Fimmel et al. 2023 Proposition 5.9 already proves the all-even-alphabet maximum size, number of optimal codes, and partition/tournament description, while Fimmel–Michel–Strüngmann 2017 already counts the full q=4 special case. These known consequences are explicitly excluded from novelty. Inspected 2023 full relevant sections show no complete all-cardinality symmetric enumerator; a different structural paper could still imply it.

## value

PASS

The exact all-cardinality spectrum of constrained self-synchronizing codebooks is a natural enumeration independent of maximum size. Its coefficients quantify the feasible nonmaximal choices for every even alphabet, and require substantive allowed-support inclusion–exclusion rather than a known extremal table. A precise finite-by-size invariant of a natural object can be useful without a broader coding theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
