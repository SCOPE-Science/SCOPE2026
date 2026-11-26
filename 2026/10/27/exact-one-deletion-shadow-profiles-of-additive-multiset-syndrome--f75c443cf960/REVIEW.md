# Independent mathematical audit

## correctness

PASS

For any received y and target syndrome a the unique parent is y plus a copy of a−s(y), so distinct occupied labels give distinct outputs and the shadows tile the received simplex. In the character filter the factor for a coordinate is [1−(1−u)χ(g)z]/[1−χ(g)z]. An order-d character takes each dth root q/d times; multiplying the factors and taking the coefficient of z^n gives exactly the displayed Q, including the zero contribution if d does not divide n. Characters with order dividing e are the dual of G/eG, giving |G[e]| times the indicator a∈eG; divisor inversion gives the integer formula. Translation shifts the syndrome by nb; conversely support one tests membership in nG, and nG is proper when gcd(n,E)>1. For prime q the nontrivial term when q divides n is exactly 1−(1−u)^q. For distinct a,b each occupied g gives the unique allowed transfer g→g+b−a with that removed label; its signed coordinate vector determines g, so the degree is the support and the inter-class edge count is the shadow total. Independent enumeration of sorted words reproduced both order-four group examples, with zero-syndrome rows (4,2,4,0) and (4,6,0,1), respectively, and the prime-five example. Replay: RESULT.md lines 51–100; inspected support_spectrum_check.py and its frozen .out (100 group/length settings, 27,824 multisets and 15 transfer settings, not independently rerun). Scope is n≥1 and the entire finite abelian group alphabet, not general label maps or multiple deletions.

## originality

PASS

The weighted finite-abelian character-order distribution and exact coefficientwise balance criterion survive comparison. The cyclic deletion construction, its implied occupancy, the unweighted or unconditional marginals, and a particular quinary row have prior coverage; the elementary transfer consequences are not the main originality basis.

## value

PASS

Support is exactly the number of distinct possible received multisets per word, used in natural deletion-shadow packing bounds. Resolving its full distribution by checksum shows what equal total occupancy conceals: different class sizes and branching patterns, and different distributions for the same alphabet cardinality under different group structures. This is a motivated exact finite-length invariant, without an unsupported claim of optimal coding rate or improved decoder complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
