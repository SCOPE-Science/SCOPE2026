# Every binary order-five de Bruijn cycle has a seven-position circular attractor

## Finding
Let \(W\) be an arbitrary binary de Bruijn cycle of order \(5\), regarded as a cyclic word of length \(32\). A *circular string attractor* is a set \(\Gamma\subseteq\mathbb Z/32\mathbb Z\) such that every nonempty circular factor of length at most \(32\) has at least one occurrence containing an index in \(\Gamma\). Let \(\gamma_\circ(W)\) be the minimum size of an attractor and \(a_7(W)\) be the number of attractors of size \(7\), counting subsets of the indexed cycle (not modulo rotation).

**Theorem.** Every such cycle has
\[
\gamma_\circ(W)=7.
\]
Moreover, the sharp range of optimal-attractor multiplicities is
\[
216\le a_7(W)\le368.
\]
Among the \(2048\) binary order-five de Bruijn cycles modulo rotation, exactly \(4\) attain \(a_7=216\) and exactly \(2\) attain \(a_7=368\). Summed over all \(2048\) cycles, there are \(589120\) indexed optimal seven-position attractors.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). A cyclic factor is read using indices modulo \(32\), with a specified start and length between \(1\) and \(32\). Each of the \(32\) different length-five factors occurs once in \(W\). Cycles are identified under cyclic shift when enumerating source words; attractor subsets are distinct indexed seven-element subsets in the uniquely rooted representative beginning at the unique occurrence of \(\mathtt{00000}\).

## Proof
**Lower bound and candidate completeness.** Each marked position lies in precisely five length-five circular windows. All \(32\) such windows are different; thus an attractor has at least \(\lceil32/5\rceil=7\) positions. For seven marked positions, list their seven successive positive cyclic gaps \(g_1,\ldots,g_7\). The set meets all length-five windows if and only if \(g_i\le5\) for every \(i\). Since their sum is \(32\), the deficits \(e_i=5-g_i\) are nonnegative and sum to \(3\). There are \(\binom{9}{6}=84\) ordered seven-part weak compositions of \(3\). Choosing an initial marked position in \(32\) ways and dividing by the seven choices of which marked position starts the gap list yields precisely \(32\cdot84/7=384\) distinct size-seven candidates.

**Reduction to short factors.** Every cyclic factor of length at least \(5\) contains a length-five factor as its prefix. Because this prefix occurs at only one indexed starting position on the cycle, any mark intersecting that length-five window also intersects the longer occurrence. Thus a seven-set hitting all length-five windows is a full attractor precisely when it hits at least one occurrence of each circular factor of lengths \(1,2,3,4\). For a short word \(u\), define the 32-bit mask \(M_u\) to have a one in every position covered by at least one occurrence of \(u\). The necessary and sufficient condition is \(S\mathbin{\&}M_u\ne0\) for all short \(u\), where \(S\) is the bitset of the candidate marked positions. There are \(2+4+8+16=30\) such short factors.

**Complete source-cycle enumeration.** Regard a state as a five-bit word \(by\), with \(b\in\{0,1\}\) and \(y\) a four-bit suffix. A de Bruijn cyclic order on the 32 states yields a shift-compatible successor permutation. For the two states \(0y\) and \(1y\) to have different successors, their appended bits must be complementary. Hence for each \(y\) there is one independent choice \(f(y)\in\{0,1\}\), and the transition is \(by\mapsto y(b\oplus f(y))\). There are exactly \(2^{16}=65536\) choices. The choices whose orbit from \(\mathtt{00000}\) is one cycle of length \(32\) are exactly the rooted de Bruijn cycles. The executable checker enumerates all masks and obtains exactly \(2048\) distinct cycles. As a second exhaustive construction, it enumerates Euler tours of the four-bit de Bruijn directed graph, fixing its unique edge \(\mathtt{00000}\) first. It obtains precisely the same \(2048\) rooted cyclic words.

**Finite exact certificate.** For each of those \(2048\) words the checker constructs all \(384\) seven-position candidates from the gap compositions and all \(30\) short-factor position masks, then performs all of the necessary-and-sufficient bit intersections. It verifies \(216\le a_7(W)\le368\), sees the respective extremal counts \(4\) and \(2\), and verifies the total \(589120\). In particular every \(a_7(W)>0\), giving the upper bound \(\gamma_\circ(W)\le7\). Together with the lower bound, this proves the theorem. In addition, each cycle's first passing seven-set is independently checked by reconstructing and comparing all short factors and their covered occurrences; two extremal cycles are also checked at all 32 factor lengths. The full finite enumeration is the computational part of the proof, not an extrapolation from samples.

## Verification
Run `python3 checker.py` with Python 3.8 or later and no external dependencies. Expected summary: `PASS; cycles=2048; tight_sets=384; optimum=7 for all`; minimum \(216\) (four cycles), maximum \(368\) (two cycles), total \(589120\), and \(120\) different realized attractor-count values. The program independently enumerates all source cycles by successor tables and Euler tours, constructs candidate gap patterns, and separately tests selected witnesses using the actual factor occurrences. No previously stored table is used as an input.

## Relationship to prior work
De Bruijn cycles and their word constructions are classical; Ruskey, Sawada, and Williams (2012) study fixed-density cycles. Mantaci, Restivo, Romana, Rosone, and Sciortino (2021, Section 6.2 and Proposition 41) establish asymptotic attractor-size bounds for **linear unfoldings** of de Bruijn sequences, not an exact optimum for every order-five circular cycle. Whittington (2024, Theorem 29) proves optimality for a **particular Lyndon-generated** prime-order de Bruijn sequence and explicitly discusses the question of optimal attractors for general de Bruijn cycles. Neither the one-construction theorem nor the asymptotic linear bounds yields the present exact all-cycle assertion or the multiplicity extremes. Separate research on substring counts, binary de Bruijn BWT runs, palindromes, or scattered-subsequence universality does not determine circular attractor multiplicities.

## Limitations
This is an exhaustive finite theorem for binary order \(5\), not a proof for higher order or larger alphabets. The notion is a circular attractor, not an attractor in an arbitrarily chosen linear unfolding with repeated boundary symbols. The exact multiplicity bounds depend on computer-assisted exhaustive case analysis; although the entire checker is supplied, independent verification has not been performed. Historical priority cannot be established merely from finite literature/database searches.

## References
- F. Ruskey, J. Sawada, A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, SIAM Journal on Discrete Mathematics 26 (2012), 605–617. DOI: https://doi.org/10.1137/100808782 (published online 2012-05-08).
- S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), 236–248. https://doi.org/10.1016/j.tcs.2020.11.006 ; open postprint: https://arpi.unipi.it/handle/11568/1062328 .
- P. Whittington, *Online String Attractors*, arXiv:2407.15599v1 (2024), Section on optimal attractors for de Bruijn sequences. https://arxiv.org/abs/2407.15599 .
- N. Prezza, *String Attractors*, arXiv:1709.05314 (2017). https://arxiv.org/abs/1709.05314 .
