# Independent mathematical audit

## correctness

PASS

Count distinct length-(n+2) outputs of exactly one insertion, without complements. At sites i<j, trimming the common outside portions reduces equality to B_i U=U B_j, where U=w_{i+2}…w_{j+1} and B_i,B_j are the two-letter inserts. For tandem this is exactly period two on w_i…w_{j+1}; equality classes are consecutive runs, giving 1 plus the distance-two inequalities. For two palindromic inserts, if j=i+1 the three aligned letters force the source triple constant. Otherwise the common middle has period two (both copies of U agree at a shift of two); U ends in w_jw_{j+1} whereas the final insert reverses these letters, making the two parity classes equal. Thus nonconstant palindromic sites give distinct outcomes. Constant sites already belong to the tandem set. For a nonconstant palindromic site i and a tandem site j≤i+1, comparison at the two inserted positions excludes equality. If j≥i+2 those positions require w_{i+2}=w_{i+1} and w_{i+3}=w_i; this is sufficient with j=i+2, giving exactly the abba subtraction. Saturation of both positive sums gives the q≥3 extremum and the count. For binary words, the deficit from n is #zeros minus #changes plus #101 in the transition word. A boundary zero-run costs length minus one and an interior run costs length minus two plus the indicator of length one. The all-zero transition word never maximizes. The qualifying runs give the stated generating function and each transition word has two preimages. Uniform expectation uses probability (q-1)/q for either inequality and (q-1)/q³ for each abba correction, with no corrections for n<4.

## originality

PASS

Separate tandem and palindromic sphere formulas and general duplication-code settings are prior. The distinct result is the exact mixed union, especially its cross-channel intersection correction and the resulting alphabet transition and binary maximizing classification. The mean is a corollary, not a separate originality claim.

## value

PASS

The distinct descendants are the exact confusability neighborhood for a natural single-error channel permitting either copy orientation. A mixed neighborhood cannot be sized by adding the individual channel formulas. The correction identifies the precise local obstruction, and the alphabet-dependent extremum and binary maximizing census reveal which sources have the largest ambiguity. These exact local counts are useful independently of an optimal global code bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
