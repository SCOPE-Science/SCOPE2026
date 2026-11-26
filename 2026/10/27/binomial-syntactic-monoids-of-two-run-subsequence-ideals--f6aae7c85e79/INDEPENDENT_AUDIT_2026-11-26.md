# Independent mathematical audit

## correctness

PASS

Independently checked the greedy DFA: each state is reached by a prefix of the target, and a target suffix completing the higher of two states is too short to complete the lower one. Therefore the automaton is minimal and its transition monoid is the syntactic monoid. If the input contains z zeros, c=max(r-z,0) is the first state that can reach the ones phase; below c the map is translation by r-c. At a state i between c and r−1 its final displacement above r counts ones after the (r−i)th zero, capped at s; starting at r all ones count, and states above r translate by that total with a cap. This proves the signature is weakly increasing and fixes every image. In reverse, the image of 0 determines c and the images of c through r recover all signature entries. Interlacing r−c zeros with successive differences of the entries and putting t_c ones after the last zero realizes the tuple with at most r+s letters; c=r uses only ones. The number at fixed c is binomial(s+r−c+1,r−c+1), and summing gives binomial(r+s+2,r+1)−1. A nonempty zero-containing word strictly moves state 0, and an all-ones nonempty word strictly moves r, proving the distinct empty identity. For balanced parameters (r=s, or bounded difference), Stirling's formula gives the stated order 2^N/sqrt(N) with N=r+s+1.

## originality

PASS

The distinct result is the exact cardinality and signature bijection for the syntactic monoid of the scattered two-run ideal. The automaton, its state complexity, and the relation to the extensive order-preserving monoid are known or standard, but do not enumerate the specific two-generator monoid. Close exact factor-language results concern a different acceptance condition. A targeted literature query did not produce relevant additional coverage; this is not a priority guarantee.

## value

PASS

The monoid count is an exact algebraic size for a natural family of principal shuffle ideals. The signature identifies all actions and yields short word representatives rather than only a count. Balanced patterns give a concrete family with linear DFA state count yet exponentially many distinct actions, in contrast to the polynomial census for the contiguous-factor version of the same pattern. This provides an exact benchmark for studying the extra algebraic complexity induced by gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
