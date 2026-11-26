# Independent mathematical audit

## correctness

PASS

An Abelian border longer than half the word gives a complementary shorter one by subtracting Parikh vectors. A longer-than-one factor with equal ends is bordered at length one. The one-marker factors with unequal ends have no Abelian border. For a two-marker factor 0ʲ10ᵇ1, when j>b every prefix of length at most half contains no marker and the matching suffix contains one; when j≤b, 0ʲ1 is itself a literal border. Reversal gives the other side. This proves the disjoint factor set and U=2+2T for m≥1; for 11 only the single-letter word 1 qualifies. The balanced triples attain the lower bound, and T=m occurs exactly when b=0 or b=m. Fixing b between ceil((m−t)/2) and t then counting pairs a+c=m−b with both at most t gives the finite CDF. The normalized simplex slice at b/m=B has length (1−B)−2max(1−B−x,0), on (1−x)/2≤B≤x. Integrating against normalized area gives the two stated pieces. The moments are correct: the tail integrals on [1/3,1] yield 1/3 and 13/36 and must be augmented by 1/3 and 1/9 from [0,1/3], respectively; line 91 omits that interval in its wording. The corrected integrals give 2/3 and 17/36, hence variance 1/36. The statistic and its square are Lipschitz on the simplex, so boundary-grid and interior quadrature errors are O(1/m), giving the stated rates after rescaling. Independent bounded checking constructed every substring, tested equal-length prefix/suffix Parikh vectors, and compared deduplicated sets, CDF counts, extrema and maximum multiplicities for all 1,771 gap triples with m≤20.

## originality

PASS

The supported distinct contribution is the exact per-source distinct-factor census, its extrema and its conditional finite and limiting laws. Ordinary and Abelian borderedness agree for factors of this weight, so neither the distinction between the predicates nor the elementary local border test is credited as a novel property. The closest located work counts whole words by border statistic, or counts a different set of factors in the same gap family. No inspected statement supplies this aggregate census and probability law.

## value

PASS

Weight two is a natural first case with two competing marker separations and orientation-dependent factors. The per-word exact diversity, rather than global existence of borders, identifies a genuine boundary between diversity controlled by one gap and by a+c−b. The census gives fully classified extrema and a nondegenerate law under a natural fixed-composition random model. These results are useful benchmarks for sparse-word factor diversity even though the individual border test reduces to the ordinary one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
