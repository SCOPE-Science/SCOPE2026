# Independent mathematical audit

## correctness

PASS

At length N=q^k a factor crosses at most one aligned block boundary. Since precisely 00, 01, 10 occur as adjacent letters of the block coding, the suffix-plus-zeros and zeros-plus-prefix families exhaust the factors, including aligned blocks and the all-zero word. Shifting through an internal zero preserves the necklace and passing a one decreases the suffix weight or increases the prefix weight by one, so each family supplies one class at each of its weights. The two interior-weight representatives reverse each other since the substituted one-block is palindromic. Its one-positions are the base-q expansion with digits (q−1) times the binary digits of the one index; the internal gap at index j is (q−2)q^{v_2(j)}+1 by carrying. For the prefix representative, the complementary wraparound gap is the only gap congruent to 1 modulo q−1, so rotations cannot shift its position relative to the sequence of internal gaps. The two classes coincide exactly when the latter sequence is its own reversal. If m is a power of two then v_2(j)=v_2(m−j) throughout. For odd m>1, j=1 fails, and for m=2^s u with odd u>1, j=2^s fails. This includes the empty gap list at m=1 and handles k=0 with only the two extreme classes. Counting gives 2^{k+1}−k. The suffix family has N distinct linear words from their differing terminal zero-run lengths, proving the ratio limit without an assumption on ordinary complexity.

## originality

PASS

The credited claim is the substitution-scale rotation count, particularly the exact power-of-two criterion for a single class at interior weight. The closest cyclic-complexity theorem inspected has a one-site-discrepancy hypothesis absent here. The closest same-word and same-scale results classify different equivalence relations or use a distinguished subset of words at different lengths. No source inspected gives or mechanically implies the frozen per-weight classification or total. The ratio limit is a corollary, not a separate basis for originality.

## value

PASS

Rotation classes are a standard refinement of weight classes and a coarsening of ordinary factor complexity. The natural substitution scales give a complete exact comparison for every base, including a nontrivial criterion for when the two reflected candidates are actually rotations and a vanishing fraction of distinct linear factors after quotienting. The class count and its per-weight structure provide useful test data and a structural characterization, not just selected computed values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
