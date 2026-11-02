# Necklace-perfect constant-weight-three binary non-overlapping codes

## Finding
For every integer \(n\ge4\), let \(M_3(n)\) be the largest cardinality of a code \(C\subseteq\{0,1\}^n\) such that every word contains exactly three ones and, for every \(u,v\in C\) (including \(u=v\)) and every \(1\le\ell<n\), the length-\(\ell\) prefix of \(u\) is not the length-\(\ell\) suffix of \(v\). Then
\[
M_3(n)=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
Write \(k=\lfloor n/3\rfloor\). All maxima in the displayed cardinality are attained by the explicit code
\[
C_n=\left\{1 0^{a-1}1 0^{b-a-1}1 0^{n-b-1}:
1\le a\le k,\quad a<b\le n-k-1\right\}.
\]
The three ones occur at zero-indexed positions \(0,a,b\). Moreover, \(C_n\) contains exactly one representative from **each primitive length-\(n\) binary cyclic-rotation class having three ones**. It therefore saturates the primitive-necklace upper bound simultaneously for all \(n\ge4\).

## Assumptions and scope
Words are linear, all are binary and of identical length, and the weight constraint counts ones exactly. Prefix/suffix overlaps are forbidden at every nonempty proper length, including self-overlaps. A rotation class (necklace) identifies words under cyclic rotation; a word is *primitive* if no rotation by an index strictly between \(0\) and \(n\) fixes it. No Hamming-distance, balancing, run-length, or reverse-complement restriction is imposed.

## Proof
**Upper bound.** Every codeword must be primitive: a nonprimitive word with proper period \(d\mid n\) has the same prefix and suffix of length \(n-d\), violating non-overlap. Also, distinct codewords cannot be cyclic rotations of one another, because a rotation by \(r\in\{1,\ldots,n-1\}\) makes a nonempty proper prefix equal to a suffix (or conversely). Every primitive rotation class contains exactly \(n\) words.

Exactly \(\binom n3\) length-\(n\) binary words have weight three. If one is nonprimitive, its repetition number divides three and is at least two, so it is necessarily a triple repetition of a block of length \(n/3\) containing exactly one one. This occurs only when \(3\mid n\), in which case exactly \(n/3\) such words exist. Therefore every permissible code satisfies
\[
|C|\le\frac{\binom n3-\mathbf 1_{3\mid n}(n/3)}{n}
=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
Here \(\mathbf 1_{3\mid n}\) equals one when three divides \(n\) and zero otherwise.

**Construction and non-overlap.** Every \(u\in C_n\) begins with one, and has its second one at position \(a\le k\) and third at \(b\le n-k-1\). Any proper suffix of a codeword that begins with one must begin at position \(a\) or \(b\). A suffix starting at \(b\) has length \(n-b\ge k+1\) and contains just one one, whereas the prefix of every codeword of that length has at least two ones (the first and the second, at a position at most \(k\)). A suffix starting at \(a\) has length \(n-a\ge n-k\) and contains exactly two ones, whereas the prefix of every codeword of that length has all three ones (the last at a position at most \(n-k-1\)). Every remaining proper suffix begins with zero, while each nonempty prefix starts with one. Thus no proper suffix of any member equals a prefix of any member; \(C_n\) is non-overlapping.

**Cardinality.** For each \(a\in\{1,\ldots,k\}\), the permitted values \(b=a+1,\ldots,n-k-1\) number \(n-k-1-a\). Hence
\[
|C_n|=\sum_{a=1}^k(n-k-1-a)=\frac{k(2n-3k-3)}2.
\]
For \(n=3k\), \(3k+1\), and \(3k+2\), respectively, this becomes \(3k(k-1)/2\), \(k(3k-1)/2\), and \(k(3k+1)/2\), exactly the upper bound in every case.

**Canonical necklace transversal.** A word of weight three determines three positive cyclic gaps \((g_1,g_2,g_3)\), each giving the distance between consecutive ones, with sum \(n\). Let \(k=\lfloor n/3\rfloor\) and call a gap *short* if it is at most \(k\) and *long* otherwise. Any cyclic gap triple contains both kinds unless \(n=3k\) and all three gaps equal \(k\), which is precisely the excluded nonprimitive case. In a cyclic ordered triple containing both kinds, there is exactly one transition from a long gap to a short gap. Root the word at the one immediately following this transition. The first cyclic gap is then short (\(g_1=a\le k\)), and the last is long (\(g_3=n-b\ge k+1\)), precisely the defining inequalities of \(C_n\). Uniqueness of the long-to-short transition gives exactly one representative of each primitive necklace.

## Verification
The included standalone standard-library script `verify.py` reconstructs every codeword directly from the three one-positions; directly tests disjoint proper-prefix and proper-suffix sets; exhaustively enumerates all weight-three primitive cyclic classes; and checks that the code selects each class exactly once. It completes these definition-level checks for every \(4\le n\le40\), printing `VERIFY_OK`. These finite checks are corroboration. The all-length result follows from the explicit counting and combinatorial arguments above.

For illustration, the maximum sizes at lengths \(n=4,5,6,7,8,9,10,12,20,30,40\) are \(1,2,3,5,7,9,12,18,57,135,247\), respectively.

## Relationship to prior work
Chee, Kiah, Purkayastha and Wang (2012) give general cross-bifix-free constructions and asymptotic bounds without this fixed-weight-three sharp count. Blackburn (2013) proves general non-overlapping-code bounds and constructions. Stanovnik, Moškon and Mraz (2025) give the primitive-word upper-bound method for composition-constrained codes in a more general near-balanced setting (Proposition 5); that general upper-bound principle alone does not establish a weight-three construction that attains the primitive-necklace bound for every blocklength. The distinguishing statement here is simultaneous all-length attainment by a very simple explicitly indexed, cyclically canonical, constant-weight-three code.

## Limitations
The theorem concerns exactly three ones, the ordinary cross-bifix-free condition, and exact binary words. It does not assert that the same necklace upper bound is attainable for higher weights, nor any robustness against symbol errors, reverse complementation or insertion/deletion noise. The possibility of an earlier specialized fixed-weight-three construction not identified in the inspected literature remains a priority risk.

## References
- Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, first publicly posted 2012-09-03, arXiv:1209.0236, https://arxiv.org/abs/1209.0236.
- S. R. Blackburn, *Non-overlapping codes*, first publicly posted 2013-03-05, arXiv:1303.1026, https://arxiv.org/abs/1303.1026.
- U. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, https://doi.org/10.1007/s40314-024-03055-0, 2025, Section 3, Proposition 5.
