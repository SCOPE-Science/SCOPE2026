# Independent mathematical audit

## correctness

PASS

Cauchy–Davenport makes 4A all of F_p once |2A|≥(p+1)/2. For p=4m+1, strict majority gives |A|≥m+1, enough directly. For p=4m+3≥19 the only remaining case is |A|=m+1, |2A|=2m+1≤p−2. Both summands have size ≥2, so Vosper makes A an arithmetic progression. Independently checking the obstruction: restrict starting points x to x≠0,−1,−2; the three pair-character sums are −1−χ(2), 0, −1−χ(2), from the full sum −1 (count (u−v)(u+v)=1) and subtraction of the excluded terms with χ(−1)=−1. The equal-sign indicator is (1+ab+ac+bc)/4, and x↦−2−x exchanges the two common signs. Thus each sign has (p−5−2χ(2))/8 starts. Dividing a progression by its nonzero step produces m−1 distinct starts of one sign, more than this count. This covers every prime ≥13 in both congruence classes. At 7 and 11, iterated Cauchy–Davenport gives 6A and 5A respectively. Independent enumeration of multisets with repetition found the stated witnesses miss exactly {4}, {0,2}, and {0} at (p,h)=(7,5),(11,4),(13,3) and miss nothing at h+1. It also checked membership and strict majority. Replay: `python3 /workspace/branches/review_replay.py 1`. The frozen verifier was read but not executed.

## originality

PASS

The supported distinct contribution is the uniform sharp four-summand cover for a strict majority of nonzero prime-field squares, together with the precise small-field obstructions in scope. The bounded comparison did not establish equivalent coverage. It does not assign novelty to Cauchy–Davenport, Vosper, or the general technique of quadratic-character pair sums.

## value

PASS

This identifies the exact uniform additive basis order at a natural density threshold in a multiplicative subgroup. It resolves the case where direct Cauchy–Davenport alone can leave |2A| one short of covering after doubling, and shows exactly why a uniform order of three cannot replace four. The arithmetic-progression obstruction and the separate orders at 7 and 11 distinguish structural and small-field effects, rather than merely recomputing a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
