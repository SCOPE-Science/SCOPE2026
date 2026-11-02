# Independent mathematical audit

## correctness

PASS

For each n, exactly enumerating all 2^n binary words and rejecting every factor with period p and length 2p+1 generates O_n. An independent prefix-growth route gives identical sets for n=1..14. The Hamming distance to every distinct O_n word gives maxima <=2 through n=12, 3 at n=13, <=3 through n=13 and 4 at n=14. There are exactly four delta=3 words of length 13 and exactly two delta=4 words of length 14, with the listed reversal/complement orbits; direct flipping of every set of 1..k positions confirms delicacy for extremizers. Thus L_2=13, L_3=14, and complete shortest lists. This exhaustive finite check covers exactly the finite domain required for the two claimed minima, not arbitrary k.

## originality

PASS

Best-of-knowledge new exact first-two generalized-delicacy minima and equality cases. The primary 2021/2022 source names generalized k-delicacy and asks its all-k existence question; it classifies only ordinary k=1. A broader 2022 first-order decidability theorem does not evaluate these minima. OEIS A007777 supplies total overlap-free word counts but not Hamming-isolation distances, while the 2024 isometry paper addresses a different invariant. Targeted exact-string/parameter/alias searches and published mathematical-record searches identified no covering result. Inaccessible plausible 2023 slides are a nontrivial residual priority risk, not a mathematical implication or proof of coverage.

## value

PASS

These are not arbitrary chosen word lengths: they are the first two natural generalized k-delicacy parameters beyond the explicitly established k=1 theory and are motivated by Przybocki Question 5.1. Exact first-occurrence thresholds with complete minimum witness lists and symmetry classes answer two meaningful initial cases of the established problem. The finite proof is exhaustive (not a sampling extrapolation), though modest in computational scale. A later study of higher k could use the precise initial thresholds and extremizers as base cases; no general all-k theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
