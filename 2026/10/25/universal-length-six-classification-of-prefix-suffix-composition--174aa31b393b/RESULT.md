# Universal length-six classification of prefix–suffix composition ambiguity

## Finding

Let \(\Sigma\) be any alphabet of cardinality \(q\ge 2\). For a word \(w\in\Sigma^n\), the **prefix–suffix composition deck** \(\mathcal M(w)\) is the multiset of the Parikh (symbol-count) vectors of all its nonempty prefixes and nonempty suffixes, each of the two full-word occurrences retained. A fiber is the set of words of length \(n\) with the same deck.

**Theorem.** For every finite \(q\ge2\):

1. Every fiber at lengths \(1\le n\le5\) consists of a word and its reversal (with the duplicate suppressed if the word is a palindrome). Thus the number of distinct decks at length \(n\le5\) is \((q^n+q^{\lceil n/2\rceil})/2\).
2. Every length-six fiber has size \(1\), \(2\), or \(4\). The size-four fibers are precisely
   \[
   \{abcdab,\ abdcab,\ bacdba,\ badcba\},
   \]
   where \(a,b,c,d\in\Sigma\), \(a\ne b\), \(c\ne d\). Each is indexed **uniquely** by the ordered pair \((\{a,b\},\{c,d\})\) of two-element subsets (the subsets may intersect).
3. The numbers of length-six fibers of respective sizes \(1,2,4\) are
   \[
   q^3,\qquad \frac{q^6-q^3-4\binom q2^2}{2},\qquad \binom q2^2.
   \]
   Consequently the number of distinct length-six decks is
   \[
   N_q(6)=\frac{q^6+q^3}{2}-\binom q2^2.
   \]
   This is also the maximum size of a code in which distinct length-six words must have distinct prefix–suffix composition decks.

In particular the earliest possible failure of reconstruction up to reversal is length six for every \(q\ge2\); at \(q=4\), six of the \(36\) four-word fibers use all four symbols, an effect invisible in binary reconstruction.

## Assumptions and scope

Words have fixed known length, distinct symbols have distinguishable coordinate labels in their Parikh vectors, and observations retain multiplicities. There are no mass collisions between distinct Parikh vectors. The theorem applies to every integer \(q\ge2\) and lengths through six; it says nothing about larger lengths or noisy decks. The known ambiguity of a word and its reversal is not regarded as a reconstruction failure.

## Proof

Write \(\mathbf e_x\) for the coordinate unit vector corresponding to \(x\in\Sigma\), and define
\[
L_i=\sum_{j=1}^{i}\mathbf e_{w_j},\qquad R_i=\sum_{j=1}^{i}\mathbf e_{w_{n+1-j}},\qquad L_0=R_0=0.
\]
At length \(i\) the deck gives exactly the unordered pair \(\{L_i,R_i\}\), with multiplicity. Let \(T=L_n=R_n\) be the total composition. For each \(i\),
\[
L_{n-i}=T-R_i,\qquad R_{n-i}=T-L_i.
\]
Thus the entire deck is equivalent to \(T\) and the unordered two-path layers \(\{L_i,R_i\}\) for \(1\le i\le\lfloor n/2\rfloor\). At odd length \(n=2m+1\), the central symbol is uniquely recovered from the unit vector \(T-L_m-R_m\). At even length \(n=2m\), the two paths of \(m\) inward steps exhaust the word.

**Unique-matching lemma.** Suppose \(A\ne B\) are two Parikh vectors of equal weight and \(C\ne D\) two Parikh vectors of weight one greater. At most one of the two perfect matchings between the pairs \(\{A,B\}\) and \(\{C,D\}\) can use only unit-coordinate-increment edges. Indeed, if both matchings worked, then
\[
C=A+\mathbf e_i=B+\mathbf e_j,
\qquad D=A+\mathbf e_k=B+\mathbf e_\ell.
\]
Hence \(B-A=\mathbf e_i-\mathbf e_j=\mathbf e_k-\mathbf e_\ell\). Since \(A\ne B\), the positive and negative coordinate of this difference uniquely determine respectively \(i=k\) and \(j=\ell\), implying \(C=D\), a contradiction.

Reversing a word exchanges the two inward paths globally. The lemma shows that while both vertices in two consecutive layers are distinct, their continuation is forced once the paths are named. More explicitly, decompose the nonzero inward levels into maximal consecutive intervals on which the two vertices are distinct. On each such interval, a valid orientation of the two paths is determined by the orientation at its first level. The two choices of orientation are both valid, because they are just exchanges of the two paths throughout that interval. At every intervening equal-vertex level, the paths can be rejoined or separated without an additional constraint; consequently the interval orientations are independent. If there are \(r>0\) such intervals, the deck has exactly \(2^r\) word realizations (and \(2^{r-1}\) reversal orbits); if \(r=0\), the word is a uniquely determined palindrome.

For \(n\le5\) there are at most two nonzero inward layers. Between the initial coincident layer and these two layers, there is no interior meeting separating two nontrivial excursions. Every realization therefore differs from any other only by a global exchange of the two paths, i.e. reversal. The central symbol in odd length is fixed as above.

For \(n=6\) there are three inward layers. Two reversal-inequivalent realizations can occur precisely when
\[
L_1\ne R_1,\qquad L_2=R_2,\qquad L_3\ne R_3.
\]
Necessity follows from the lemma: the first and third separated layers then admit an independent relative exchange across the middle coincident layer. In every other equality pattern among layers one can propagate path names uniquely modulo one global exchange. Sufficiency follows because both separated excursions may independently exchange path names while maintaining every unit step.

Unpacking those three conditions, write \(w=w_1w_2w_3w_4w_5w_6\). The middle equality says the multisets \(\{w_1,w_2\}\) and \(\{w_5,w_6\}\) coincide. The first inequality forces \(w_1=a\ne b=w_6\), so \(w_2=b\), \(w_5=a\). The final inequality is exactly \(w_3=c\ne d=w_4\). Hence the four realizations for fixed unordered pairs are exactly the four displayed words. They are distinct, share a deck, and represent two reversal pairs. Moreover the deck at length one determines \(\{a,b\}\) and the two distinct length-three vectors, after subtracting the common length-two vector, determine \(\{c,d\}\). Distinct ordered pairs of two-element subsets therefore never describe the same fiber.

There are \(\binom q2^2\) such four-word fibers. Exactly \(q^3\) length-six words are palindromes; their deck determines them uniquely because at each inward layer the two Parikh vectors coincide and their increments recover the first half. Every other fiber not among the four-word fibers is a reversal doubleton. Subtracting the \(q^3\) singleton words and \(4\binom q2^2\) four-fiber words from \(q^6\), then dividing by two, gives the stated size-two count. Summing the three counts gives \(N_q(6)\). Selecting one word per fiber is both necessary and sufficient for a distinct-deck code, proving the final assertion. \(\square\)

## Verification

The fully independent `CHECK.py` builds all length-at-most-six words over alphabets of sizes \(2\) through \(7\), computes each deck directly as a multiset of Parikh vectors, and separately recomputes the same observation as a sequence of unordered inward-path layers. It tests every fiber against the theorem, including the explicit pair-of-pairs classification of size-four fibers. The checked length-six deck counts for \(q=2,3,4,5,6,7\) are respectively \(35,369,2044,7775,23211,58555\). Execute with `python3 CHECK.py` (standard library only). These finite checks support but do not replace the alphabet-uniform proof above.

## Relationship to prior work

Gabrys, Pattabiraman and Milenkovic [1] formalized prefix/suffix composition-based reconstruction for binary polymer strings and multiple-source codes. Ye and Elishco [2], particularly Example III.6 and Corollary III.12, established the binary length-six four-word collision and uniqueness up to reversal for binary lengths at most five. Those binary statements are **not claimed as new**. The present theorem classifies all fibers at the first ambiguous length for every alphabet size, including fibers supported on three or four different symbols, and derives the full \(q\)-dependent size distribution and optimal reconstruction-code cardinality. Chen [3] further develops binary erroneous prefix/suffix composition reconstruction, not the alphabet-uniform six-position fiber census.

## Limitations

Reconstruction uses exact distinguishable Parikh vectors, not real-valued masses with possible collisions. Nothing is claimed for lengths greater than six or missing/erroneous observations. The finite checker is not a proof for arbitrary alphabet sizes. Prior-work equivalence under another name remains a possibility; no independent mathematical audit has been performed.

## References

[1] R. Gabrys, S. Pattabiraman and O. Milenkovic, *Reconstruction of Sets of Strings from Prefix/Suffix Compositions*, arXiv:2110.02352, first public submission 2021-10-05. https://arxiv.org/html/2110.02352v1

[2] Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, first public submission 2022-08-31. https://arxiv.org/abs/2208.14963

[3] Z. Chen, *Coding methods for string reconstruction from erroneous prefix-suffix compositions*, arXiv:2503.12342, first public submission 2025-03-16. https://arxiv.org/abs/2503.12342
