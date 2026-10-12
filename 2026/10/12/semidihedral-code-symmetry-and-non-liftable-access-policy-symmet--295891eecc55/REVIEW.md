# Review

## Correctness

PASS. The source generator is reconstructed exactly over \(\mathbb F_3\). Exhaustion of all \(81\) codewords reproduces the published weight enumerator and, using the support-minimal definition, reproduces the exact \(15\)-set access structure printed in the source. All \(8!=40320\) coordinate permutations are tested, giving exactly \(16\) code automorphisms. The displayed generators have orders \(8\) and \(2\), satisfy \(srs=r^3\), and generate all \(16\). All \(7!=5040\) participant permutations are tested, giving exactly four access-hypergraph automorphisms, a Klein four group. The dealer stabilizer inside the code group has order \(2\), so the non-lifting comparison is exact.

## Originality

PASS. The primary paper states cyclicity, prints the exact generator and access family, and uses the code for secret sharing, but does not determine either full automorphism group or compare policy symmetry with code symmetry. The older perfect-nonlinear-function source is a genuine coverage risk because the 2026 paper says the covering structures match; its public abstract describes covering structures and minimal access sets, not automorphism groups. Exact public and research-record searches by parameters, generator polynomial, group order/presentation, and access-set fingerprints found no statement implying the combined claim. Residual risk remains from unindexed short-code classifications or inaccessible incidental calculations.

## Value

PASS. Symmetries of a secret-sharing access policy determine which participant labels are interchangeable, while code automorphisms describe symmetries realizable at the underlying coordinate level. Showing that the source example has a semidihedral order-\(16\) code group but a larger dealer-policy stabilizer in the precise sense above gives a structural distinction directly relevant to the application developed in the source, rather than a routine recomputation of its parameters.

Self-review: passed. Independent audit: not yet performed.
