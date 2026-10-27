# Review of the crown-graph total Roman \(\{2\}\) enumerator

## Correctness

**PASS.** The proof starts from the original open-neighborhood defense and total-positive-neighbor requirements. The missing matching forces at least two positive labels on each side. Once this is established, each side falls into one of exactly three support regimes: robust, two unit labels, or one double and one unit label. The two forced-positive generating functions subtract all and only the exceptional regimes. The six resulting pairings are disjoint and exhaustive; their counts yield the asserted polynomial. Evaluation at \(z=1\), the first two nonzero coefficients, and the exponentially small rejection fraction are algebraic consequences. An adjacency-based verifier, independent of the classification, checked all \(597{,}780\) ternary assignments for \(n=3,4,5,6\) and the complete polynomial coefficients. The finite checks corroborate but do not replace the arbitrary-\(n\) proof.

## Originality

**PASS, subject to residual priority risk.** The first public source (Cabrera García et al., online 28 November 2019, DOI 10.2989/16073606.2019.1695230; manuscript arXiv:2101.02537) develops general numerical bounds and graph-class results for the parameter, not the complete crown-graph weight distribution. A related paper by Abdollahzadeh Ahangar et al. (DOI 10.7151/dmgt.2316) and indexed literature on Cartesian graph products were compared. A published complete-multipartite all-weight enumerator cannot be specialized to a crown graph because deleting a perfect matching changes local defense and support constraints; perfect Roman crown-graph results use a different condition. Published mathematical record searches for crown, \(K_{n,n}-M\), bipartite double-cover, Italian, and total Roman \(\{2\}\) formulations returned no covering statement. These negative searches do not establish universal uniqueness: equivalent unindexed publications and full texts unavailable during this examination remain risks. In particular, neither the previously known general domination bounds nor their implied scalar minima are advertised as new.

## Value

**PASS.** Total Roman \(\{2\}\) domination is studied for its minimum weight, but the complete weight profile contains the number of solutions at every budget and distinguishes the two kinds of low-weight local obstructions caused by a deleted matching. The formula is a fixed-length expression of elementary polynomials for an infinite, vertex-transitive bipartite family. It gives exact minimum and next-minimum multiplicities and an explicit total count with exponential asymptotics; those facts are not implied by a bare domination-number bound. The special value at \(n=3\) coincides with an ordinary cycle, but the proof handles every \(n\ge3\).

## Closest sources and limitations

The principal comparison is the 2019 *Quaestiones Mathematicae* article and its freely available 2021 manuscript. General results on \(\gamma_{t\{R2\}}\) and its relationship to double domination can explain numerical lower bounds but not the displayed all-weight enumeration. The complete-multipartite published record is not a supergraph-enumerator transfer theorem. The theorem does not cover the disconnected crown graph at \(n=2\), other Roman parameters, or automorphism-orbit counts. The indexed abstract of Q. Chen's 2024 Cartesian-product study and part of a 2024 survey were accessible, but their full text was not; this limits any claim about their contents. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
