# Independent mathematical audit

## correctness

PASS

The complete observation records every contiguous substring length and ones count with multiplicity. The package source build_census.cpp and verify_independent.cpp group exact full byte signatures, choosing one canonical representative of each reversal orbit and restoring word multiplicity 1 or 2; counter indices exhaust n(n+3)/2 entries without overflow for n<=23. Independently compiled a separate 23-bit complete-signature enumerator, which ran over all 8,388,608 words via 4,196,192 canonical classes and produced exactly 4,096 singleton, 4,191,936 double, and 160 quadruple fibers: weighted sum 8,388,608. Separate independent Python enumeration matched n=8,11,12,14. Consequently the optimal zero-error code cardinality is the exact count of fiber classes. This certifies only finite n<=23, not all binary lengths; the 160 length-23 witness rows were inspected but not independently pairwise regenerated.

## originality

PASS

Acharya et al. introduced the model and known non-reversal collisions (including a length-23 example); those are prior, and the exact complete histogram is the assessed contribution. Published Resultary r=2-limited composition and ordered adjacent-pair spectra concern strictly different observations, not a dominating full-composition count. The fully enumerated n=23 exact count is best-knowledge not a priority guarantee.

## value

PASS

The full composition-multiset observational equivalence relation is a natural reconstruction-code object; exact fiber sizes and optimal one-representative noiseless code size at length 23 quantify ambiguity at a meaningful length known to have nontrivial alternative decompositions. A complete 23-row census with explicit fourfold classes is useful even absent an all-length recurrence, and is not a mere arbitrary substring-truncation parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
