# Independent mathematical audit

## correctness

PASS

Every length-at-most-2^m circular factor is a factor of an aligned T_m T_m in the infinite word, obtained by substituting into 00. Brown et al.'s occurrence-alignment lemma then gives a genuine cyclic desubstitution bijection at even half-length, including for wrapping occurrences. Half-length one is counted by transitions on the source cycle, with V_j=2^j-V_{j-1}. At half-length three an even start is impossible: in the form a A b B c C with capitals denoting complements, comparison of the triples would require a=B, A=c and b=C, a contradiction. At an odd start, the corresponding four source bits must be 0011 or 1100; these lie at odd offsets in the lower image and correspond exactly to alternating triples two levels down. Equal adjacent source letters give two such triples, including across the boundary. This verifies both arrays, including the absent h=N/2 type, which desubstitutes to the nonsquare length-two T_1. Finite sums give S_m and H_m; a square of length 2h crosses precisely the 2h-1 internal cuts and survives the others. The independent six-triple by sixteen-offset replay verified the complete local crossing/starts bound and the length-4, 8 and 16 boundary cases. Under scaling an aligned cut sees G and an interior cut sees G+D. A global maximum must saturate all level pairs; starting at scale zero, saturation forces divisibility by 2^{k+4} when m−k≥5, making the next pair aligned. The final q=3 or 4 pair forces a half-block cut; the q=2 singleton bound is compatible, and handles m=2 directly. The canonical and half-shift cuts attain every bound. A separate exhaustive replay independently checked every half-length and each ordinary linear rotation through m=8, including both sums and the mean.

## originality

PASS

Pass is for the scoped circular occurrence census and especially the sharp uniqueness of the least-repetitive cuts, not the already-classified square-root types or alignment. Brown et al. give the positional language, making the counts tractable, but their inspected counting statistics do not give the extremum on nonwrapping counts across rotations. The strongest circular-exponent and published catalog comparisons study different objects or observables. The nontrivial extra ingredient is the simultaneous local crossing bound and its equality restrictions across scales.

## value

PASS

The exact loss and unique half-shift pair solve a natural extremal problem for all rotations of canonical Thue–Morse blocks. The spectrum, first moment and mean are reusable exact enumerative data. Importantly, the cut extremum needs a local crossing lemma not supplied by the old factor-type result; the contribution is not just a restated allowed-length classification or a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
