# Scientific review: exact weight-two binary three-read capacity

## Correctness — PASS

For every integer \(n\ge6\), two disjoint weight-two supports differ at four coordinates, whose three-window coverage is at least six. Two supports sharing one position differ at two positions and have read distance six exactly when their two nonshared positions are cyclically separated by at least three. The graph reduction is therefore an equivalence, not an upper-bound relaxation. At every graph vertex, its neighborhood has at most \(\lfloor n/3\rfloor\) elements. When \(3\mid n\), degree-maximal neighborhoods must be entire residue classes modulo three, and degree-maximal vertices cannot occur in all three classes; this produces the sharp deficiency. Explicit complete bipartite/clique, circulant/antipodal, and circulant/matching constructions attain the respective upper bounds. All arithmetic parities and every length \(n\ge6\) are covered.

The independently written direct-metric enumeration in `verify.py` establishes finite checks but is not substituted for the infinite proof. Neither read-error interpretation nor larger weights are asserted.

## Originality — PASS, with residual bibliographic risk

The inspected Yaakobi–Bruck–Siegel primary PDF establishes the b-symbol read model and general bounds and interleaving constructions; it does not classify maximal Hamming-weight-two three-symbol codes. The inspected Yang–Li–Feng preprint and Ding–Zhang–Ge linear MDS paper address other code families; in particular Ding et al.'s exact parameters \(b=3\), \(d_3=6\) are for unrestricted **linear** MDS codes, not codes with every word of Hamming weight exactly two. The inspected de Alba–Carballosa–Leaños–Rivera paper proves an independence-number formula for two-token graphs over \(C_n\), not \(C_n^2\); its general upper estimate does not yield the divisible-by-three correction. The inspected Verma–Patanker–Singh paper treats unrestricted codes and fixed **b-weight**, an inequivalent normalization. Searches under coding and two-token-graph aliases, including comparisons against accessible published research records, did not identify a statement implying the present exact result. An unindexed equivalent theorem remains a specific risk; no comprehensive uniqueness certification is implied.

## Value — PASS

The result determines a natural exact nonlinear coding-theoretic invariant at all lengths for sparse three-read words and characterizes the cyclic arithmetic obstruction that makes the elementary degree bound unattainable exactly when the length is divisible by three. Its nonuniform constructions attain the optimum in the odd-parity residue case and do not follow merely by changing a parameter in a conventional bound. Precise correction of this degree-bound failure is useful for constructing small-weight three-symbol read codes with provable optimal cardinality; no paper-scale generalization is required for this standalone exact classification.

## Scope and risks

The theorem does not address general Hamming weight, other read lengths, other read-distance requirements, or independent external validation. The closest works and their nonimplications are documented in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
