# Independent mathematical audit

## correctness

PASS

For each invertible two-row block the block projector is I, so the exact error multiplier is -sqrt(1-v_ij/v_star). Squaring and using independent uniform draws proves the product mean-square law; q is nonnegative since every v_ij<=v_star. The doubled angles turn 4v_ij into squared chord distances. For a diameter pair of squared length d², the sum of the two squared distances from any third point equals d²/2 plus twice its squared distance from the midpoint. The midpoint is strictly inside the unit circle, so retaining just these terms and the diameter gives sum(v_ij)>Mv_star/2 for M>=3 and hence q<(M-2)/(M-1). With row angles -t,t and distinct c_j t², the unique largest angle difference is 2t in the monotonic range of sin²; the volume ratios tend to 1 for that pair, 1/4 for the 2(M-2) incident pairs, and 0 for the rest, proving the nonattained supremum. A separate rational check on M=3..6 and t=1/8,1/32,1/128 corroborated the unique maximizer, chord identity, and strict bound; the limit argument, not the checks, proves sharpness. From nonzero initial error, the first exact hit is the first draw of one of the r maximizing pairs, giving an independent geometric law and largest mean binom(M,2) on the same sharpness family. Unrelaxed projection and normalization from the first draw before its update both solve in one step. These statements are for exact arithmetic, consistent planar systems, and the stated initialization, not arbitrary online maxima. The supplied verifier was inspected, not executed; its recorded output is supplementary.

## originality

PASS

Credit the relaxation and square-block convergence factor to the inherited scheme; the one-step online fact alone is also immediate from its known rule and full rank. The distinct assessed result is the nonattained sharp planar row-count envelope and its near-extremizers exhibiting maximal quadratic mean waiting time under fixed normalization versus the one-step online behavior. The strongest inspected statements do not supply this joint sharp classification. Priority is not certified.

## value

PASS

The diagnostic is sharp in a setting where every unrelaxed block would be an exact solver. It quantifies a concrete loss from global relaxation as redundant rows are added and distinguishes two quantities that could otherwise be confused: worst mean-square contraction and the first exact hit. The same family approaching the contraction bound exhibits the longest expected exact-hit time, while the online initialization removes this delay. No extrapolation to noisy problems, smaller blocks or empirical runtime is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
