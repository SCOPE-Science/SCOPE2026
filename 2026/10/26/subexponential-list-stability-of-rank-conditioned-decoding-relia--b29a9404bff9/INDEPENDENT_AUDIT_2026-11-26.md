# Independent mathematical audit

## correctness

PASS

PASS for the corrected package, not for an unrestricted reading of the frozen endpoint. RESULT.md:7–26,47–51 of the original invokes fixed-list regularity but only writes y_L<1 as the rank restriction, and applies an unstated moving strict-tail limit. The reference's Lemma 5 and Proposition 2 actually require y_L<H_0, the guesswork support endpoint, which can be below 1. For uniform noise on a subspace of size K_n=2^{floor(hn)}, 0<h<1, the rate is I(x)=h−x on [0,h], infinite elsewhere. Take L_n=n eventually, with early ranks 1,2 and last rank K_n, all ranks within the support. Then I(h)=0 and y_L=h<1, but the strict tail is zero, so S_n=1/n. For R>1−h the original displayed Delta evaluated with the closed-set rate is 1−R−h<0, falsely predicting exponential decay under these weaker hypotheses. This does not refute the intended claim if one imports the reference's interior restriction. The corrected RESULT.md, SLOGAN.txt and claim in METADATA.json make the limits on the actual rank sequences explicit and no longer claim that y_L<1 supplies the tail limit. Independently, for a fixed received word each admissible completion of a given tuple has common codebook and transmitted-word factors; a listed putative transmitted rank is in every completion, while a given allowed unlisted one is in the fraction (M_n−L_n)/(2^n−q_L) of completions. Weighting by its noise probability gives the exact posterior, with feasibility eventual because R<1 and y_L<1. The sum of later listed likelihoods lies between p_{q_2} and (L_n−1)p_{q_2}, preserving its point exponent. The uniform inclusion factor has rate 1−R. Taking the minimum of the later-list and unseen-tail rates, then dividing by p_{q_1}, gives rate Delta for the posterior odds against the first entry. The odds going to zero or infinity yields exactly the two claimed limits and exponents. The source interior hypothesis is verified for moving ranks by its point-mass window and squeezing the fixed strict tails on either side of y_L, with the trivial upper probability bound one when y_L=0. There is no claim at Delta=0, no stronger inference from an LDP alone, and no assertion that a change of list length leaves the observed endpoint exponents unchanged. The frozen verification is analytic; there is no executable certificate needed.

## originality

PASS

The repaired claim is the subexponential-list asymptotic statement, not the exact finite posterior or the fixed-list boundary. The source gives the exact finite posterior for admissible L, but its asymptotic Proposition 2 only treats fixed L and fixed distinct rank exponents. The joint n-dependent aggregate bound is needed to pass from that identity to the growing-list result, and the correction states the moving-limit regularity explicitly. Compared list-guesswork and list-error exponents are about other quantities, not this rank-conditioned posterior. Originality is bounded to this precise extension.

## value

PASS

The list-size issue is natural for decoders outputting polynomial or other growing lists. The result identifies which observations still determine strict-sign exponential reliability and shows that the aggregate of many later candidates introduces no further rate on that scale under explicit noise regularity. It is a narrow extension of known posterior theory, not a new decoding model or a resolution of the critical surface. The repaired endpoint distinction prevents a concrete incorrect reliability-exponent prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
