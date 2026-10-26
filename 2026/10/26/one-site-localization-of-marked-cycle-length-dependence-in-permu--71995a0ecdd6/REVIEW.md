# Review of the marked-cycle-length descent law

## Correctness — PASS
The statement fixes a uniform permutation, a cycle containing symbol \(1\), and ordinary one-line descents, with all quantifiers \(n\ge3\), \(1\le k\le n\), \(2\le i<n\). Uniform marked-cycle size follows by \( (n-1)!\) completions for each length. Conjugating by the adjacent label swap \( (i\ i+1)\) gives opposite interior comparisons except two exceptional image configurations that have equal conditional probability. For the first position, uniform cycle-complement sampling and symmetry of labels \(3,\ldots,n\) yield the displayed four cases; summing them proves the stated covariance. Exact rational enumeration of all permutations \(3\le n\le9\) confirms 336 assertion groups. The finite replay is corroboration, not the infinite proof.

## Originality — PASS (provisional priority)
Fulman (arxiv:math/9712240, Sections 3–5) and Gessel–Zhuang (arxiv:2001.00654v2, Sections 1 and 7) provide unmarked cycle-type/descent enumeration and probabilistic shuffle refinements; their inspected results do not retain which cycle contains the distinguished symbol \(1\). Elizalde–Troyka (arxiv:1710.05103v3, Corollary 4.2) already establish the full \(K=n\) descent-set law for first \(n-2\) positions, so that slice is covered and excluded from the claimed novel contribution. Reutenauer's scanned 1989 work and Gessel–Reutenauer's 1993 treatment count unmarked cycle structures. Related published local covariance results concern fixed-point indicators (the \(K=1\) slice), while cycle-count/inversion covariance is an aggregate statistic that cannot determine \(K\). Full inspection of Diaconis–McGrath–Pitman (1995) was unavailable, and an equivalent earlier marked-cycle refinement remains a concrete originality risk. No assertion of independent historical priority is made.

## Mathematical value — PASS
Conditioning on a fine global orbit statistic can change the first descent strongly but leaves every other local descent exactly fair and individually independent of the conditioning. The sharp boundary and the entire four-regime law are nontrivial, with a stable positive limiting covariance \(1/4\) despite all remaining sitewise covariances being zero. This isolates information not present in unmarked cycle-type or marginal Eulerian counts.

## Boundaries and evidence
The result does not prove joint independence of all interior indicators, does not concern nonuniform permutation models, and does not transfer to descents in standardized cycle words. The published record searches and full-text inspections delimit originality but cannot logically prove priority. The reproducible exact checker is in `verify.py`.

Self-review: passed. Independent audit: not yet performed.
