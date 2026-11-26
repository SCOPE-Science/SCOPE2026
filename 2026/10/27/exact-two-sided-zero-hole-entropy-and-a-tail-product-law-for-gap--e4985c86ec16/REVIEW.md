# Independent mathematical audit

## correctness

PASS

A hit centered at an internal marker is precisely a gap transition g to h with g>=r and h>=s. Tracking only the old bit g>=r gives a two-state weighted graph. With a=A_r, b=A_s, c=A_max(r,s), the rows are (T-a,a) and (T-a-b+c,a-c), so its trace is T-c and its determinant is ab-Tc<=0. Thus the scalar determinant equation picks out only the Perron crossing. The zero-gap loop and the positive short-to-long and long-to-short weights give strict Perron monotonicity; the radius diverges as z approaches 1 from above and vanishes at infinity. Removing positive weight from the unrestricted irreducible matrix gives strict loss. For the lower entropy bound, in finite truncations expand each edge to length g+1: loops from a fixed gap boundary inject into binary words by reading successive 0^g1 blocks, so the Perron growth is realized by words that extend to valid sequences. The finite roots increase to the full root by entrywise convergence and strict monotonicity. For the upper bound discard end restrictions, bound the two terminal zero runs by geometric series, and sum the internal complete gaps by the matrix resolvent above the root. Words with at most one 1 contribute only polynomial growth. Both tails and their derivatives vanish locally uniformly when min(r,s) grows; at the old root the determinant is exactly ab, and its derivative at the intermediate root tends to -T'(lambda)=mu/lambda. The mean-value and logarithm expansions give the relative asymptotic without a threshold-rate assumption. The powers-of-two example has non-eventually-periodic allowed gaps and the unchanged-tail plateaus follow directly. Frozen verify.py and VERIFICATION.md were inspected, not executed: the reported 288 finite-model checks corroborate reduction and orbit counts but do not prove the infinite-alphabet or asymptotic steps.

## originality

PASS

The closest primary result covers one-ended holes in general and the special d-gap family for two-ended holes. The supported distinction is the exact two-ended formula across arbitrary infinite S containing 0 and its two-threshold relative asymptotic. No equivalent or dominating prior result was established in the inspected literature and bounded published-record search; this is not a priority guarantee.

## value

PASS

This resolves a natural missing class of perturbations in the gap-shift problem. The exact scalar equation works without a finite presentation, and the relative leading loss remains informative for sparse alphabets and uneven thresholds, where threshold sizes alone ignore plateaus and the sizes of the permitted tails. It does not claim a formula for general multi-marker holes or a general escape-rate theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
