# Independent mathematical audit

## correctness

PASS

The cycle has all 27 cyclic triples once. A nine-mark solution must partition the 27 linear triple starts into three-start consecutive intervals; covering start 1 with full capacity forces mark 3 and induction forces 3,6,…,27 (one-based). This marks cyclic residue r=c+2 mod 3. In residues 0,1,2 the omitted bigram respectively is 02, 01, 12, with start residues 1,2,0, so both coordinates avoid the marks, including any repeated unmarked suffix. Independently computed occurrence-union bitmasks for every length in every one of the 27 cuts give exactly one missed factor with these nine marks, and adding one position in that factor hits every factor. Analytically, any factor longer than three has a unique triple suboccurrence, so hitting all triples already hits all such factors. This proves both minima exactly ten and both quantifiers over the given instance.

## originality

PASS

Best-of-knowledge PASS for the explicit universal-cut witness with exact minima 10 for both ordinary and 3-attractors. The elementary lower bound and a single bad unfolding are prior context; the distinct claim is that all unfoldings of one cyclic ternary order-three word fail the target nine. The primary text explicitly separates this all-cycles question from the existence of some favorable cycle and has a favorable cut for its own illustrative cycle. The closest inspected Resultary profile is binary order four and has favorable cuts, not this witness.

## value

PASS

The explicit witness rejects a universal rotation fix (not just a single bad linear representation); it separates forcing the exact-length factors from hitting all shorter factors. The modest finite certificate resolves a natural quantifier in the de Bruijn attractor question and gives a structural obstruction through the forced residue class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
