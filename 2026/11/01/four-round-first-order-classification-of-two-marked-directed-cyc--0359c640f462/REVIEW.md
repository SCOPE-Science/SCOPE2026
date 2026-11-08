# Independent mathematical audit

## correctness

PASS

The rank-r complete FO type of distinguished constants and chosen tuple has its full equality/successor atomic diagram and SET (not multiset) of possible rank-(r-1) one-point extension types. A selected-vertex cyclic-order encoding with positive gaps is bijective with these diagrams. Splitting a gap g inserts one new element, matching every possible quantifier witness; repetitions are separate block choices. Gap truncation at B_r=2^(r+1) is valid inductively: if two gaps >=2 B_(r-1), any split either leaves one side <B_(r-1), which can be matched exactly while other stays large, or leaves two large sides, which can be matched; smaller gaps agree exactly. Thus all infinite cycles reduce to 32x32 canonical gap pairs at rank4. Independently reimplemented gap partition and complete recursive types, obtaining class counts 4,14,40,108,340 at ranks 0..4 and sharp minimal representative sizes 4,7,11,19,35; the only rank4 maximally large representative was (17,18). No extrapolation from small graph experiments: exhaustive finite table follows the proven quantifier-rank cutoff. Source verify_symbolic.py and verify_direct.py were inspected for exact diagram, reuse/splits, and independent direct recursion.

## originality

PASS

Best-of-knowledge original sharp marked-directed-cycle rank-four type census. Brown–Hoshino’s broad EF theorem uses an undirected edge relation and no named constants; colored linear-order and directed-path theorems have genuinely different signatures/objects. No inspected prior result implies this 340 count or unique 35-vertex class; old software tables remain possible.

## value

PASS

Exact rank-four finite-model-theoretic classification of an infinite natural family gives an implementable test for equivalence, a sharp small-model bound and a unique hard class, improving vastly on generic bounds. The two observable landmark gaps genuinely interact in the FO type recurrence, making 340 nontrivial rather than a routine independent truncation of a and b.

The dated certificate retains the supplied scientific assessment, sources and limitations.
