# Independent mathematical audit

## correctness

PASS

Local non-Wieferichness is equality of each numerator valuation with its exponent in n. For an odd support prime p, LTE and the LCM of the prime-power orders give s_p + max(0,a_p-s_p,h_p) = max(a_p,s_p+h_p); only the other odd primes in S contribute to h_p. A dyadic order contributes no odd-prime valuation. For b=1 mod 4 the binary valuation at the global order is d + max(g,0,a_2-d), giving a_2 >= d+g. For b=3 mod 4, a_2=1 works exactly when g=0; for a_2>=2 the binary valuation is e + max(g,1,a_2-e), giving a_2 >= e+max(1,g). This covers the empty odd support and the gap 2<=a_2<=e in the exceptional branch. Unit cubes anchored at nonnegative lattice points sandwich the logarithmic simplex between its original size and a bounded shift in its intercept; the isolated layer has one lower dimension, including an O(1) contribution when S={2}. This proves the stated leading constant and error. The independent repeated-multiplication and modular-congruence replay checked 4,146 cases across ten bases, supports of size at most three, and exponents 1–4, including b=7 and n=6,12,24,48,96 with outcomes yes/no/no/yes/yes. Replay: /workspace/branches/b92e88fa-1565-4d23-a229-34512642428b/replay_record4.py. These checks are finite; neither bundled code execution nor formal or expert certification is asserted.

## originality

PASS

Substantial exact overlap is credited for the odd-support classification and, for base 2, for the logarithmic count. The supported distinction of the full theorem is its extension to supports containing 2 for odd bases, including the necessary-and-sufficient isolated low-exponent layer, and the resulting counting statement on those supports. No inspected statement supplies that extension. The nearby indexed records' dates alone are not evidence of priority or independence.

## value

PASS

The classification turns orders depending on the full integer into explicit support constants and describes exactly when monotonicity in an exponent fails at 2. The gap between the isolated admissible layer and the upper orthant, witnessed at the single support {2,3} in base 7, is a meaningful structural boundary, not merely a change of notation or a generic lattice count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
