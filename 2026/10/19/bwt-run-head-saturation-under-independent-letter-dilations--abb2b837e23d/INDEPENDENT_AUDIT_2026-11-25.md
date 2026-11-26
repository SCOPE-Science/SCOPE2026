# Independent mathematical audit

## correctness

PASS

For a mixed word, each starting position belongs to one maximal circular run of symbol a and is specified there by its remaining length t. Every row followed by a letter smaller than a sorts before every row followed by a larger letter; t increases in the former class and decreases in the latter. At equal t the post-run continuation determines order, preserved by letter-dependent dilation since the shared prefix is expanded identically. Identical periodic tails determine the backward circular letters too, hence ties cannot affect the output. At t=q h_a the preceding letters form the fixed word B(q); the h_a-1 intervening levels each contribute R(q) copies of a. This proves the entire last-column product, including for periodic words. For h_a>=2 every inserted factor is nonempty, so varying its length cannot change any run head, including across block boundaries. Monochromatic words are immediate, and direct rotation sorting gives BWT(011)=110 versus BWT(0011)=1010, showing sharpness even when just one exponent is 1. An independently written bounded reproduction passed 23,226 comparisons of full last columns and heads, all ternary words of length 1–7 with exponents 2 or 3 on present letters. The uploaded verifier was inspected, not executed.

## originality

PASS

The supported distinct claim is the full arbitrary-parent, arbitrary-ordered-alphabet last-column decomposition and the resulting universal saturation of ordered heads from exponent 2. Mantaci et al. supply order preservation and a subsequence argument for Lyndon inputs, with a genuine special equality case when the source ratio is already maximal. The inspected material does not give the general threshold or the full decomposition. The frozen literature paragraph should qualify the cited theorems as statements for Lyndon inputs; this does not affect the proved finding.

## value

PASS

BWT run counts measure clustering; prior single-letter monotonicity leaves open whether further expansion still changes that clustering. The proof gives an exact, sharp universal cutoff and a stronger ordered invariant, while the full factorization specifies how run lengths can still change. This is useful for predicting cyclic BWT structure without sorting the expanded word.

The dated certificate retains the supplied scientific assessment, sources and limitations.
