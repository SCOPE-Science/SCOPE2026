# Independent mathematical audit

## correctness

PASS

A four-one word is determined by its five zero-run lengths. Any Abelian-square factor contains 0, 2 or 4 ones; zero-only squares give floor(max(r_i)/2); two-one factors are unique triples (gap,u,v) obeying equal-half parity and |u-v|<=gap with occurrence bounds (union prevents duplicate substrings); four-one factors are unique (u,v) under exact half-boundary inequalities. An independently coded direct-substring vs run-count comparison checked all four-one words through length 22. Separately compiled and ran the assigned combinatorial C++ counting implementation afresh through n=128; it exhaustively processed 275234400 four-one configurations and output minimum and multiplicity table for every n=4..128, matching floor((n+2)/4) and 2,2,8,4 for all 110 target lengths. Separately checked every proposed optimizer word and reversal at each of the 110 lengths against the exact run formula, verified the full proposed family has the exhaustively certified minimizer count, and therefore ruled out additional minimizers within the finite range. It does not extrapolate to n>=129; independent direct substring checking covers a shorter range than the optimized enumeration.

## originality

PASS

Closest statement/implication comparisons and bounded primary reading support best-of-knowledge originality with explicitly named residual priority risks; no claim of exhaustive historical uniqueness.

## value

PASS

The motivating 2026 fixed-Parikh distinct Abelian-square problem leaves four occurrences of a minority letter as the first unclassified interior class. Exact minima and every extremizer for 110 consecutive nontrivial lengths are independently useful finite combinatorial classification data; the exact 0/2/4-one factor decomposition supports reproducibility. Finite exhaustive results are valuable here because the parameter range is stated exactly, not generalized beyond certification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
