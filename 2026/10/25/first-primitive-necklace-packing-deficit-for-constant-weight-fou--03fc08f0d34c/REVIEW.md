# Scientific review: fixed-weight-four non-overlapping codes

## Correctness — PASS
The proof defines the full prefix/suffix condition including self-overlap and uses the primitive-orbit argument only for an initial upper bound. For lengths \(5\)–\(11\), explicit codebooks reach this bound. At length \(12\), the separate exhaustive covering certificate partitions every one of the \(128\) unbordered weight-four words into \(39\) cliques of pairwise conflicting words. Thus no code can exceed \(39\), and a directly checked \(39\)-word code attains equality. `python verify.py` reruns orbit counts and every relevant overlap test from the included data. The conclusion covers only lengths through \(12\).

## Originality — PASS, with historical-priority risk
The nearest known unrestricted-code papers are Bilotta–Pergola–Pinzani (arXiv:1112.3168), Chee–Kiah–Purkayastha–Wang (arXiv:1209.0236), and Blackburn (arXiv:1303.1026). Their constructions and unrestricted upper bounds do not provide the exact constant-weight-four packing optimum or its particular cross-orbit obstruction. Harju–Nowotka (2005) enumerate primitive/bordered fixed-weight words; those individual-word counts alone do not imply the optimum for pairwise non-overlap. Searches for fixed-weight, cross-bifix-free and necklace-transversal formulations uncovered no direct prior theorem. Historical novelty cannot be established definitively by database search alone; unindexed restricted tables remain a risk.

## Value — PASS
The result isolates a natural sharp transition in synchronization coding: the first weight-four length for which a primitive necklace cannot be represented by every orbit at once. The strict deficit is not merely a table entry: the upper certificate exhibits a global partition obstruction beyond the standard necklace counting argument, matched by a construction. It is independently reproducible without an optimization solver.

## Limits
The theorem gives a finite cutoff only, not an asymptotic conjecture, unrestricted optimum, or uniqueness classification. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
