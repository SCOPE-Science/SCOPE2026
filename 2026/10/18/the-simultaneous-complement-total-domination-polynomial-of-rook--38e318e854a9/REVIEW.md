# Scientific assessment

## Correctness — PASS

The theorem is proved for every integer \(m,n\ge2\). The argument first characterizes ordinary domination by row/column occupancy, characterizes complement-total domination by the impossibility of a single occupied row-column cross, and obtains the exact generating polynomial by disjoint case analysis and inclusion–exclusion. At the \(2\)-row boundary complement-total domination forces two selections per row, hence the exceptional minimum \(4\). For at least three rows, an optimal row transversal fails precisely when one column contains all or all-but-one of its vertices; these two excluded families are disjoint, and a square board requires subtracting permutation matrices from the union of row- and column-based optima. The \(2\)-by-\(2\) case is explicitly separate. Two independent direct adjacency-mask verifiers completed exhaustive finite checks: 271,904 subsets for minima and 1,435,472 subsets for the full polynomial. Exhaustive finite tests are corroboration, not a proof of the infinite quantifiers.

## Originality — PASS with residual risks

The 2024 founding paper [1], which defines the mixed ordinary/complement-total domination invariant, studies modular graph products and motivates independent investigation of the invariant, without giving the all-size rook polynomial or its extremizer classification. Mertens's primary full text [2] counts *ordinary* dominating rook placements, which only satisfy row/column coverage; the new mixed condition excludes every placement confined to a row-column cross and changes minimum-set counts. Earlier simultaneous-factor domination papers discuss related configurations but accessible evidence does not imply the mixed rook result. Searches with the equivalent phrases “global domination together with complement total domination,” “SDCTD,” “rook graph,” and “line graph of complete bipartite graph” found no theorem that covers this result. Residual risks include unindexed sources and insufficiently accessible full texts of older general simultaneous-parameter research. A negative search alone is not a novelty proof.

## Value — PASS

The result is a complete all-cardinality enumeration, structural description, and sharp minimum for a standard two-parameter graph family under a recently proposed mixed domination invariant. It detects a genuine exceptional two-row regime and explains via exact cross obstructions why ordinary rook-domination enumerations overcount admissible configurations. The full polynomial permits exact counts at every size, not merely a routine restatement of the known rook domination polynomial, and responds to the source's explicit suggestion to investigate the mixed invariant.

## Limits and closest literature

The theorem does not cover other graph products or higher-dimensional Hamming graphs. The graph family and parameter have canonical mathematical motivations, but broader literature could contain an equivalent in different terminology. Scientific review here is self-assessment, not independent certification.

Self-review: passed. Independent audit: not yet performed.

## Primary references

[1] S. Bermudo et al., *Domination number of modular product graphs* (2024), arXiv:2404.02853, https://arxiv.org/abs/2404.02853.

[2] S. Mertens, *Domination Polynomial of the Rook Graph* (2024), arXiv:2401.00716, https://arxiv.org/abs/2401.00716.

[3] P. Dankelmann et al., *Simultaneous graph parameters: Factor domination and factor total domination* (2006), DOI:10.1016/j.disc.2006.04.017.
