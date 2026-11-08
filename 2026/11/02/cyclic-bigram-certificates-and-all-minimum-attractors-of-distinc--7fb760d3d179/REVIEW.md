# Independent mathematical audit

## correctness

PASS

Any attractor needs one position of each of q>=3 distinct letters. With exactly q positions, hitting every cyclic transition a_j a_(j+1) is necessary and sufficient: for factors of length<=period realign around a selected transition or inside a constant run; factors longer than the period have translated overlapping occurrences covering every internal period-boundary position. Inclusion–exclusion over q transition types gives the exact 2^q-term product formula, including singleton-run overlap and the missing terminal period edge. For all run lengths>=2 each selected position witnesses at most one transition; the only two cyclic orientations yield 2 k^(q-1)(k-1) optimal sets. For all singleton runs only the terminal adjacency can be missed and count is k^q-k^(q-2). Independently enumerated literal factor occurrence masks for mixed (2,1,3),k=2 (18 attractors), (2,2,2,2),k=3 (108), (1,1,1),k=3 (24), and (2,2,2),k=2 (8), agreeing with short certificate and special formulas. Finite checks are corroborative only.

## originality

PASS

Best-knowledge PASS for an all-factor certificate using length-1/2 conditions and complete minimum-set counting polynomial for powers of distinct-run periods. Mantaci–Restivo–Romana–Rosone–Sciortino prove general word-power inequalities for minimum attractor sizes but no classification of every minimizing position set in this family; Dvořáková–Hendrychová analyze aperiodic binary Rote words. Related previously published Resultary attractor enumerations target other automatic/pseudopalindromic sequences.

## value

PASS

The string attractor is a natural compression-theoretic invariant; a constant-length certificate replacing all substring constraints and a parameter-uniform exact count of every minimizer reveal structural rigidity of periodic words. The all-run-length and all-k formula is more than a finite sample or alphabet-size lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
