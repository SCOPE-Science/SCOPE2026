# Independent mathematical audit

## correctness

PASS

For 10 length-eight words, if d_min>=5 then 45 pairs contribute >=225 Hamming units, while each of 8 coordinates contributes at most 25 for 10 words; impossible. All displayed size-10 representatives have distance four and satisfy all 3-outsider separating conditions. Independently implemented exact increasing-index backtracking over all candidate nonzero words of Hamming weight>=4 with chosen zero, checking every pair and every new triple, and obtained exactly 46,200 size-ten valid systems containing zero. Translation incidence: 10N=256*46,200 yields 1,182,720 labeled sets. Independent enumeration of all 8! coordinate permutations and allowable translations from each representative gave stabilizers 48,32,16 and orbit sizes 215040,322560,645120. The representatives have distinct per-codeword distance-profile histograms, and three orbit sizes sum to all labeled systems, so classification exhaustive. This is finite exact combinatorics, not an unverified random search; baseline max size10 is prior established.

## originality

PASS

The earlier exact 2026/9/21 result proves largest binary length-eight separating set has size 10 but does not enumerate maximum systems by min-distance or classify Hamming-isometry equality strata. This work gives a complete structural refinement after a separate exhaustive computation. No exact prior same census located.

## value

PASS

The maximum size10 was known, but its most-separated equality class is natural for coding theory: a sharp secondary Hamming-distance optimization and a complete labeled/unlabeled optimizer census (3 orbits with different stabilizers) gives reusable exact structural information. The computation is genuinely exhaustive for fixed length eight, not an arbitrary random slice or a claim about longer codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
