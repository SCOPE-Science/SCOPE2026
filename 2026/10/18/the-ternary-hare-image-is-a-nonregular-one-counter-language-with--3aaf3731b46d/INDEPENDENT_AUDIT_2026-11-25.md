# Independent mathematical audit

## correctness

PASS

Hare sorts any binary segment, since splitting at all maximal 1s leaves only zeros. Splitting a ternary input at its k copies of 2 gives k+1 such segments and moves the 2s to the end. Therefore each 10 in the binary prefix of an output must cross a segment boundary and there are at most k. Conversely the cuts at all 10s produce nondecreasing pieces; pad with empty pieces, then interleave k separators. This includes the empty prefix and the k=0 binary case. The ordered weak cuts are unique for the segment lengths of any one input, and choosing each segment with its prescribed counts gives the product of binomial coefficients, so summation neither omits nor duplicates inputs. A deterministic machine increments for 10 and decrements (saturating at zero) on the final 2-block, using finite state for phase and previous symbol and accepting at counter zero. Appending 2^i separates (10)^i and (10)^j for i<j. A prefix with d descents has 2d mandatory run letters in 2d+2 run exponents, giving z^(2d)/(1−z)^(2d+2) and the stated binomial counts. The terminal block contributes z^d/(1−z), yielding the rational series; its denominator expands to 1−3z+3z²−2z³+z⁴, giving the recurrence. For λ(λ−1)²=1 there is just one real root (the local maximum on [0,1] is 4/27 and negative λ cannot solve it). The other reciprocal roots have modulus λ^(−1/2) by the conjugate-pair product. The coefficient of (1−z/r)⁻¹ is −1/[r(1−r)q′(r)] for q(z)=(1−z)²−z³, agreeing with the given constant; division by 3^n gives exponential decay.

## originality

PASS

Pass for the local ternary image criterion, its language-theoretic boundary and the simple explicit ternary fiber specialization. The general fertility formula is prior, and the output-count sequence, series, recurrence and numerical growth are not distinct numerical results; their identification with the ternary image is the contribution. The exact image criterion and language classification also occur in a later Resultary record, explicitly distinguished below.

## value

PASS

The first alphabet beyond binary sorting already gives a genuine regular-to-nonregular boundary. The local image test, simple one-counter recognition and exact individual binomial fibers provide access to the full information collapse for arbitrary ternary words, rather than re-tabulating an integer sequence or merely invoking general hook formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
