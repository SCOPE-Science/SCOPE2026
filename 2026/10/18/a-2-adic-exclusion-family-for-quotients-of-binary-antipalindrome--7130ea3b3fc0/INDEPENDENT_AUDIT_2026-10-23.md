# Independent mathematical audit

## correctness

PASS

For an odd N in the specified 2*4^j to 4^(j+1) shell, binary length bounds force numerator-minus-denominator half-length s−t=j+1. Because the antipalindromic denominator is even, 2^(h+1)|B(N−1); complementary reversal propagates the last min(h+1,2t) equal bits into prefix equality. A denominator shorter than h+1 forces the leading entire word of the numerator to be B and N≥4^(j+1); otherwise the prefix v≥2^h bounds N>4^(j+1)*2^h/(2^h+1), contradicting the exclusion inequality. Each exact valuation h occupies one residue mod 2^(h+1); shell contributions have O(j) rounding and geometric tails. The concave partial-shell density H(y) has endpoint C, yielding global liminf C/6. Independently recalculated decimal 0.08816659344948140306377 and exact complete-shell counts 1,7,32,134,539,2165,8665,34666 for j=1..8. This bounds density of all unrepresentables from below only; finite tests cannot establish the inclusion.

## originality

PASS

The origin paper Bai–Meleshko–Riasat–Shallit INTEGERS 22 (2022) explicitly proves 1/60 lower density by a bounded three-leading-bit obstruction (published Theorem 12; the submitted source cites an alternative numbering Theorem 18/Corollary 19). The present exclusion tracks arbitrarily many prefix bits through h=nu_2(N−1), handles short denominators and computes the exact liminf of the constructed family, giving 0.0881665... >1/60. The OEIS A351172/3 pages enumerate sample quotients, not this uniform bound. Prior finite-prefix proof does not imply the stronger bound; no stronger direct covering Resultary record was seen.

## value

PASS

Determining the density of a naturally defined, infinite valuation-indexed family of integers excluded as antipalindrome quotients makes substantive progress on the published density problem, increasing an unconditional lower bound more than fivefold. The family is forced by a digit-prefix obstruction rather than an arbitrary numerical slice, and its exact liminf requires an infinite geometric shell argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
