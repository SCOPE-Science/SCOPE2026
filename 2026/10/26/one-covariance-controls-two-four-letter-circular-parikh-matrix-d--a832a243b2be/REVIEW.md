# Independent mathematical audit

## correctness

PASS

In RESULT.md lines 35–62, set N=P(u)−I for a uniformly rotated u. Any strictly increasing matrix path with k≥3 steps has at most one jump of length ≥2, since the total distance is at most four; length-one factors are fixed counts. The only path with two varying factors is 1→3→5 in N², giving precisely Cov(|u|_ab,|u|_cd). The rotations of w^p repeat the powers of all positional rotations equally. Linear Parikh matrices are products of elementary I+E_(i,i+1); alternating diagonal conjugation sends each generator to its inverse, so reversal gives the inverse product. Expanding (I+N)^p and (I+N)^−1 leaves exactly the same quadratic residual with coefficients binomial(p,2) and 1 respectively. For the block check, normalized X on cuts in a and b is 1−j/A and j/B for zero-based cut offsets j, and likewise Y on c and d. In abcd either Y=1 on a,b or X=1 on c,d; in acbd the normalized product sums only on a and d, giving (A+D)/2. Their centered moments give the two representatives in the table. Complementing either pair by swapping its letters negates its covariance and reaches all orders with relabelled sizes. For unit block lengths the six cyclic classes each have four distinct rotations, so all three asserted multiplicities follow. Positional duplicates and absent letters cause no extra terms. VERIFICATION.md and checker.py report finite exact rational checks; the uploaded checker was not executed.

## originality

PASS

The primary paper supplies the framework, ternary identities and one four-letter failure. The common exact covariance with its all-word equivalence and the exhaustive block family are distinct from those results in the inspected sources.

## value

PASS

This resolves the first alphabet size where the published circular laws fail: one scalar decides both identities for every word and power, including positive, negative and vanishing examples on a complete natural family. It turns two known failures into an exact criterion, not merely another counterexample or re-evaluation of [abcd].

The dated certificate retains the supplied scientific assessment, sources and limitations.
