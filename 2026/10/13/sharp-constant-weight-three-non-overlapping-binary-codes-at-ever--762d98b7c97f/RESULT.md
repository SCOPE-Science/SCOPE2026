# Sharp constant-weight-three non-overlapping binary codes at every length

## Finding
For every integer \(n\geq4\), let \(M_3(n)\) be the maximum cardinality of a family \(C\subseteq\{0,1\}^n\) in which every word has exactly three ones and, for every ordered pair \(u,v\in C\) (including \(u=v\)), no nonempty proper prefix of \(u\) equals a suffix of \(v\) of the same length. Then
\[
M_3(n)=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
Every primitive cyclic rotation class of binary words of length \(n\) and weight three has exactly one representative in an explicit optimal family. This exhausts the universal primitive-necklace upper bound.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); all codewords have a common integer length \(n\geq4\) and Hamming weight three. Overlap means equality of a nonempty *proper* prefix with an equally long suffix, across ordered codeword pairs including self-pairs. Cyclic rotation classes are considered only to establish a sharp counting upper bound; the members of a code are ordinary linear words, not cyclic words. A word is *primitive* if none of its nontrivial cyclic shifts fixes it. No Hamming-distance, error-correction, or asymptotic claim is made.

## Proof
**1. Universal upper bound.** Write a length-\(n\) word as \(uv\) where \(u,v\) are both nonempty. Its rotation \(vu\) has suffix \(u\) equal to a proper prefix of \(uv\), so no two distinct members of one cyclic-rotation class can coexist in a non-overlapping code. A nonprimitive word has a proper period and thus a nonempty proper border, so it cannot occur even as a singleton codeword. Hence \(|C|\) is at most the number \(P_3(n)\) of primitive weight-three necklaces.

There are \(\binom n3\) binary weight-three words. If a weight-three word is nonprimitive, its repetition count divides three and therefore must be exactly three. This is possible precisely when \(3\mid n\); then the nonprimitive words are the \(n/3\) rotations of a block of length \(n/3\) with exactly one one, repeated three times. Every primitive rotation class has exactly \(n\) members. Consequently
\[
P_3(n)=\frac{\binom n3-\mathbf 1_{3\mid n}\,n/3}{n}
=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
The last equality follows by reducing \((n-1)(n-2)\) modulo six: its residue is two when \(3\mid n\) and zero otherwise.

**2. Construction.** Put \(t=\lfloor n/3\rfloor\), and take every word of the form
\[
0^a1\,0^b1\,0^c1,
\qquad a+b+c=n-3,\quad a\geq t,\quad b\geq0,\quad0\leq c<t.
\]
Here \(a,b,c\) are integers. Every such word has length \(n\) and weight three. In particular it begins with zero and ends with one.

**3. No overlap.** Let \(x=0^a1\,0^b1\,0^c1\) and \(y=0^A1\,0^B1\,0^C1\) both belong to the construction. Since any suffix of \(y\) ends in one, a prefix of \(x\) that could match it must end at the first or second one of \(x\) (the third one ends the entire word).

If the prefix ends at its first one, it is \(0^a1\). A suffix of \(y\) with one one consists of at most \(C\) preceding zeros and the final one. Matching would force \(a\leq C\), contradicting \(a\geq t>C\).

If the prefix ends at its second one, it is \(0^a1\,0^b1\). A suffix of \(y\) with two ones must have the form \(0^d1\,0^C1\) with \(0\leq d\leq B\). Matching would force \(b=C\) and \(a\leq B\). The equal-total-length relation \(a+b+c=A+B+C\), together with \(b=C\), yields \(a+c=A+B\), and hence \(c=A+B-a\geq A\geq t\), contradicting \(c<t\). The argument permits \(x=y\), so it proves non-overlap including self-borders.

**4. Cardinality.** Let \(n=3t+r\), where \(r\in\{0,1,2\}\). For each integer \(c\in\{0,\ldots,t-1\}\), choose \(a\) among the integers \(t,\ldots,n-3-c\) and set \(b=n-3-a-c\). For \(n\ge4\) this interval is nonempty. The number of distinct words is
\[
\sum_{c=0}^{t-1}(n-2-t-c)
=\frac{t(3t+2r-3)}2
=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
It meets the upper bound, proving the theorem and, because the code contains one member from each primitive class, the asserted rotation-class transversal property. \(\square\)

## Verification
The standalone `verify.py` is a finite supplementary check, not the proof for all lengths. Run `python3 verify.py` using Python's standard library. It independently constructs the family, directly checks all ordered prefix-suffix pairs for lengths four through forty, checks size and composition, and, through length twenty-five, separately enumerates every weight-three word from three-position subsets and checks the equality of the resulting primitive-necklace classes. Its last line is `VERIFY_OK`; full numerical output is provided in `TABLE.csv`. The infinite theorem follows from the four proof steps above, not from this finite range.

## Relationship to prior work
Bilotta, Pergola and Pinzani study binary cross-bifix-free sets and Dyck-path nonexpandable constructions, not exact fixed-weight-three capacity. Chee, Kiah, Purkayastha and Wang optimize unrestricted-alphabet-composition cross-bifix-free constructions, and Blackburn proves general upper bounds and unrestricted optimal constructions in certain parameters. The later structural theory of non-overlapping codes by Stanovnik, Moškon and Mraz concerns unrestricted maximizers and maximal codes. None of these inspected conclusions states an optimal *fixed-weight-three* construction reaching every primitive rotation class at every length. The primitive-necklace counting bound itself is standard; the sharp fixed-composition realization is the claim under assessment. Earlier unindexed or differently named results remain possible.

## Limitations
This is an exact binary weight-three result only. It gives no formula for weight four or higher, nonbinary symbol compositions, error tolerance, or unrestricted maximum code size. Scientific originality was checked against identified accessible sources and indexed research records, not guaranteed against every unpublished or unindexed work. The accompanying finite checks do not replace the all-length argument.

## References
1. S. Bilotta, E. Pergola, R. Pinzani, *A new approach to cross-bifix-free sets*, arXiv:1112.3168v1 (public 14 December 2011), https://arxiv.org/abs/1112.3168 .
2. Y. M. Chee, H. M. Kiah, A. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (2012), https://arxiv.org/abs/1209.0236 .
3. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (2013), https://arxiv.org/abs/1303.1026 .
4. J. Stanovnik, M. Moškon, and N. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography, https://doi.org/10.1007/s10623-023-01344-z .
