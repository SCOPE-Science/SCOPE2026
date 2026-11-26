# Independent mathematical audit

## correctness

PASS

An internal cut has a one-letter border. At a boundary cut, a proper border of x^p y^q x^r y^s x^t y^u starts with x and ends with y; six runs would force an initially shortened suffix run, and four runs would force p<=r=t and u<=s=q, hence already imply the two-run border. The two-run border exists exactly for p<=t and q>=u. Rotating that criterion gives all six indicators, and no unbordered shift is duplicated since an unbordered word is primitive. The all-length enumeration is exact: for each weak-order type, positive level increments are independent and an increment contributes its tail multiplicity to the length. The finite exact check python3 /workspace/review_replay.py words independently classified all 169 type pairs by literal longest-border computation, regenerated the five nonzero common-denominator polynomials by formal polynomial arithmetic, and found counts (1,0,15,42,81,30,0). Ordinary compositions at lengths 6 to 11 give no U=5 before 11 and twelve at 11; (1,1,2,3,2,2) is one witness. In the proof's positivity sentence it is the reciprocal of the denominator, not the denominator itself, that has nonnegative power-series coefficients; its (1-z)^-2 factor ensures positivity at every later length. The two sixth-order leading terms at 1 are both 1/2; alternatively the 36 strict order pairs split 18/18, equally weighted by permutation symmetry, and ties occupy only O(n^4) compositions. The result counts ordered positive sextuples of linear zero-start words, not necklaces.

## originality

PASS

The marker-law overlap and the prior general characterization of U=2 are real special portions of the finding and are not credited as new. The surviving joint claim is the exact six-parameter criterion with arbitrary positive run lengths on both letters, its rational fixed-length distribution, and the 4/5 conditional limit. No inspected prior result supplies these; the closest exact databases cover bounded marker counts instead.

## value

PASS

Six runs is a natural structural regime: four-run proper borders must be considered but are subsumed by a two-run criterion, turning a word-level problem into comparisons of two independent run triples. This yields sharp finite-length thresholds and a nondegenerate conditional limiting distribution that unrestricted word statistics and marker counts do not reveal. The fixed-length rational generating functions and the threshold are exact usable enumeration results, not a finite census presented as a theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
