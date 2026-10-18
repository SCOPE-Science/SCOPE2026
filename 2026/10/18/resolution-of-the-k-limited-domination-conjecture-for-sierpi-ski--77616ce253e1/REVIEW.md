# Review of the Sierpiński limited-domination theorem

## Correctness — PASS

The lower proof independently establishes the base-clique link-matching structure, separates empty from nonempty base cliques, and charges each empty one to the other \(m-1\) vertices of its quotient clique. The resulting loss of \(m-k\) is offset by at least \(m-1\) excess selections. The upper construction uses an even-degree circulant relation with a uniform diagonal bit and proves that links never cross the chosen/omitted cut. This proves the equality for every stated \(n,m,k\), including the smallest and parity-boundary cases. The accompanying standard-library verifier completed the direct and exhaustive checks reported in `VERIFICATION.md`; these checks supplement rather than replace the proof.

## Originality — PASS, with residual priority risk

Božović's arXiv:2610.01584v1 explicitly poses the general formula as Conjecture 12, while proving only \(k=1\) for all alphabet sizes and the ternary-alphabet cases. The foundational arXiv:2606.22422 derives general bounds and regular-graph links to \((1,t)\)-domination, not the proposed value for arbitrary Sierpiński alphabets. Tepeh's arXiv:2606.22428 focuses on Cartesian products, and Liu's arXiv:2008.09807 treats different domination variants. Alias and implication comparisons found no covering result. Earlier equivalent proofs under other names or later-unindexed work remain possible; no definitive bibliographic-priority certification is claimed.

## Value — PASS

The result resolves an explicit fresh three-parameter conjecture over an infinite self-similar graph family. The nontrivial component is the lower-bound obstruction created by potentially empty base cliques, coupled to an all-parameter construction on the final two symbols. This is not a relabelling of the known cases; it settles their previously unproved joint extension.

## Limits

Only minimum cardinalities are determined, not minimizer counts or generalized Sierpiński graph inputs. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
