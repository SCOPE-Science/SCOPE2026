# Optimal weight-three non-overlapping binary codes as primitive-necklace transversals

## Finding
For every integer \(n\ge4\), let \(M_3(n)\) be the largest size of a family \(C\) of binary words of length \(n\) and Hamming weight three such that no nonempty proper prefix of any \(u\in C\) equals a suffix of any \(v\in C\), including when \(u=v\). Then
\[
M_3(n)=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
There is an explicit optimal construction that chooses exactly one word from every primitive cyclic-rotation orbit of binary weight-three length-\(n\) words. Consequently, the cyclic rotations of the constructed words partition the complete set of primitive binary words of that length and weight.

## Assumptions and scope
A word has **Hamming weight three** when precisely three of its symbols are \(1\). A code is **non-overlapping** (also called *cross-bifix-free* or *mutually uncorrelated*) when, for every ordered pair \((u,v)\) of codewords, with repetitions permitted, and every \(1\le t<n\), the length-\(t\) prefix of \(u\) differs from the length-\(t\) suffix of \(v\). A word is *primitive* when all its \(n\) cyclic rotations are distinct. Cyclic orbits identify words under rotations, not reversal or complementation.

All word positions below are indexed from \(0\). Let \(h=\lceil n/3\rceil\). Define \(C_n\) to contain, for each choice
\[
h-1\le i<j\le n-2,\qquad n-h\le j,
\]
the length-\(n\) binary word with ones exactly at positions \(i\), \(j\), and \(n-1\). The condition \(n\ge4\) guarantees \(1\le h-1<n-h\), so these are distinct one-positions and all constructed words begin with \(0\) and end with \(1\).

## Proof
**1. Cyclic-packing upper bound.** A non-overlapping word has no nontrivial period (a proper period would give it a nonempty border). Thus its \(n\) cyclic rotations are distinct. Distinct codewords also have disjoint sets of rotations: if \(v\) were a nontrivial rotation of \(u\), a nonempty proper suffix of \(u\) would equal a proper prefix of \(v\); equality at zero rotation forces \(u=v\). Every rotation preserves Hamming weight three. Since there are \(\binom n3\) words of length \(n\) and weight three, every such code satisfies
\[
n|C|\le\binom n3,
\qquad |C|\le\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
The argument applies to every code, not only to the proposed construction.

**2. Non-overlap of the construction.** Fix any ordered pair \((u,v)\) from \(C_n\). Let the internal one-positions of \(u\) be \(i_u<j_u\) and those of \(v\) be \(i_v<j_v\). Every nonempty suffix of \(v\) ends in \(1\). Thus a matching proper prefix of \(u\) can have length only \(i_u+1\) or \(j_u+1\), the proper positions at which a prefix of \(u\) ends in \(1\).

If the length is \(i_u+1\), the prefix of \(u\) contains exactly one \(1\), in its last position. For the suffix of \(v\) to contain no other \(1\), the middle \(1\) of \(v\) must precede the suffix's starting index \(n-i_u-1\). This would require \(i_u+j_v\le n-2\), impossible since
\[
i_u+j_v\ge(h-1)+(n-h)=n-1.
\]
If the length is \(j_u+1\), the matching prefix of \(u\) contains exactly two \(1\)'s. The suffix of \(v\) of this length starts at \(n-j_u-1\), which is at most \(h-1\) since \(j_u\ge n-h\). But \(i_v\ge h-1\), so this suffix contains all three \(1\)'s of \(v\), and therefore cannot match that prefix. These cases exhaust every possible proper overlap, even self-overlaps. Hence \(C_n\) is non-overlapping.

**3. Cardinality.** The choice of \(j\) ranges from \(n-h\) to \(n-2\), and for each such \(j\) the possible \(i\)'s are \(h-1,h,\ldots,j-1\). Therefore
\[
|C_n|=\sum_{j=n-h}^{n-2}(j-h+1)
      =\frac{(h-1)(2n-3h)}2.
\]
Writing \(n=3m\), \(n=3m+1\), or \(n=3m+2\) gives, respectively,
\[
|C_n|=\frac{3m(m-1)}2,\qquad
\frac{m(3m-1)}2,\qquad
\frac{m(3m+1)}2.
\]
These are precisely \(\lfloor(n-1)(n-2)/6\rfloor\). The construction meets the universal upper bound, so it is optimal.

**4. Complete primitive-necklace transversal.** If \(3\nmid n\), a binary weight-three word cannot have a proper period: its number of repeats would be a divisor of both \(n\) and \(3\). Hence all \(\binom n3\) words are primitive. When \(3\mid n\), the only nonprimitive weight-three words are the \(n/3\) rotations of a repeated block of length \(n/3\) containing one \(1\). Thus the number of primitive weight-three words is \(\binom n3\) when \(3\nmid n\), and \(\binom n3-n/3\) otherwise. In both cases this equals \(n|C_n|\), by the formulas above. By step 1 the rotation orbits of distinct constructed codewords are disjoint, and by step 2 every constructed word is primitive. Their union therefore contains every primitive weight-three word exactly once. This proves the transversal statement.

## Verification
The standalone, dependency-free `checker.py` independently generates the proposed code, tests every ordered codeword pair and every proper overlap length, and compares its complete collection of rotations with all primitive weight-three words for \(4\le n\le16\). It additionally tests the closed-form arithmetic identity for \(4\le n\le100000\). These finite checks support, but do not replace, the proof for all lengths.

The initial code cardinalities for lengths \(4\) through \(16\) are \(1,2,3,5,7,9,12,15,18,22,26,30,35\). At \(n=6\), for instance, two weight-three words are nonprimitive and the other \(18\) are partitioned into the three length-six rotation orbits of the constructed code.

## Relationship to prior work
Chee, Kiah, Purkayastha, and Wang introduced general near-optimal cross-bifix-free constructions using runs and generalized Fibonacci counts; Blackburn analyzed broader non-overlapping codes and proved exact results in regimes involving alphabet size or small blocklength. Stanovnik, Moškon, and Mraz developed global optimization and structural characterizations of unrestricted non-overlapping codes. Those statements concern all admissible word compositions, not the maximum confined to exactly three \(1\)'s at every length, and their general size bounds do not provide this sharp constant-weight formula or primitive-necklace transversal.

The upper bound here is the familiar cyclic-orbit packing observation specialized to fixed weight; the new contribution is that an explicitly described non-overlapping family meets it at every length in the weight-three layer. For small lengths, an unrestricted maximum can independently imply a corresponding numerical upper bound; in particular, this result does not claim first discovery of those isolated small values.

## Limitations
Only binary words with exactly three \(1\)'s and lengths \(n\ge4\) are covered. No exact result for arbitrary weight, unrestricted binary codes, reverse-complement constraints, substitution errors, or additional minimum Hamming distance is asserted. Prior-publication comparisons were made against identified directly relevant papers and searchable research records; an obscure earlier equivalent construction or theorem cannot be excluded definitively. The result has not undergone independent external validation.

## References
1. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (first public preprint 2012-09-03); IEEE Transactions on Information Theory 59 (2013), 4668–4674. https://arxiv.org/abs/1209.0236
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (first public preprint 2013-03-05); IEEE Transactions on Information Theory 61 (2015), 4890–4894. https://arxiv.org/abs/1303.1026
3. L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), 1299–1326, DOI: 10.1007/s10623-023-01344-z. https://doi.org/10.1007/s10623-023-01344-z
