# Scientific review: Hamming-product variable-width spectrum

## Correctness — PASS

The two independent directions have explicit proofs. For necessity, the largest clique containing an edge recovers its coordinate alphabet size, truncated at the variable budget. Each such edge-color class is definable using at most the budgeted variables; recursively composed binary path formulas retain the same variable budget by local bound-variable renaming. The maximum finite distance along each definable color recovers its coordinate multiplicity. For sufficiency, the permanent pebble invariant preserves coordinatewise equality partitions and uses the \(k\)-symbol capacity threshold when moving a pebble. Widths one and two have separate explicit arguments. Boundary cases include one coordinate, binary factors, repeated equal factors, and factors of size exactly the cutoff. The numerical verification comprises 10 exact finite-variable type comparisons and 39 independent clique/colored-distance checks; it supports but does not replace the infinite proof.

## Originality — PASS, with historical-priority qualification

The three-variable Hamming-product classification is already available and is explicitly excluded from the new contribution. It does not imply the all-width formula: width four separates factors of sizes three and four, and width five separates four and five, distinctions invisible at width three. The 2005 Klavžar–Peterin embedding theorems, the 2012 Grohe–Otto general pebble framework, the 2010 Pikhurko–Verbitsky survey, and the 2020 Adler–Benediktsson–Macpherson VC analysis have different conclusions and do not assert this exact hierarchy. Relevant full texts were examined by mathematical section and conclusion. Searches for aliases and stronger implications produced no covering theorem in the accessible material; this is not a uniqueness proof. An implicit generalized-product theorem elsewhere remains a risk.

## Mathematical value — PASS

This is a natural and complete classification, rather than an isolated small finite table: it determines all unrestricted-depth fixed-width theories of every finite Cartesian product of complete graphs, the sharp alphabet threshold at every width, an exact polynomial-in-dimension count of theories at fixed width, the unique smallest representatives, and the exact variable cost of distinguishing any nonisomorphic pair. The transition between neighboring widths is genuine for arbitrarily large alphabets. These sharpen the previously known three-variable case substantially and give reproducible test instances for finite-variable model comparison.

## Limits and closest comparisons

The argument excludes counting quantifiers and stays inside the mixed-alphabet Hamming-product family. The principal historical sources address embeddings, general pebble equivalence, general logical complexity, or VC combinatorics, not the exact product-specific classification. A stronger undiscovered or inaccessible general theorem could imply the result. Neither independent mathematical audit nor full historical-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
