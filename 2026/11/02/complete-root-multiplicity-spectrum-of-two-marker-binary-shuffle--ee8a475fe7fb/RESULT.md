# Complete root-multiplicity spectrum of two-marker binary shuffle squares

## Finding

For every integer \(n\ge 1\), let \(\mathcal W_n\) be the set of binary words of length \(2n\) containing exactly two ones. A *shuffle root* of \(W\in\mathcal W_n\) is a length-\(n\) binary word \(X\) for which the positions of \(W\) can be divided into two increasing subsequences, each spelling \(X\). Count distinct root **words**, not different splittings. Denote this count by \(R(W)\), allowing \(R(W)=0\).

Define, for every integer \(m\),
\[
H(m)=\begin{cases}0,&m\le0,\\1+\frac{3m(m-1)}2,&m\ge1.\end{cases}
\]
**Theorem (complete inverse root spectrum).** For every \(n\ge1\) and \(r\ge1\),
\[
\#\{W\in\mathcal W_n:R(W)\ge r\}=H(n-3r+3),
\]
\[
\#\{W\in\mathcal W_n:R(W)=r\}=H(n-3r+3)-H(n-3r).
\]
Hence the sharp maximum is \(\lfloor(n+2)/3\rfloor\). The numbers of words attaining that maximum are respectively \(1\), \(4\), and \(10\) when \(n\) is congruent to \(1\), \(2\), and \(0\) modulo \(3\).

The result refines the known count \(H(n)\) of words with at least one shuffle root: it determines **all root multiplicities**, not just shuffle-square membership.

## Assumptions and scope

Every word is linear, with ordered positions and the labeled alphabet \(\{0,1\}\). Reverse words and cyclic rotations are not identified. For \(W\in\mathcal W_n\) write uniquely
\[
W=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\qquad a+b+c=2n-2.
\]
Every root necessarily contains exactly one one, so it is of the form \(X_u=0^u1\,0^{n-1-u}\) for an integer \(0\le u\le n-1\). The theorem counts the number of permissible values of \(u\), not the number of interleaving colorings.

## Proof

**Root interval.** Exchange the two identical copies if necessary so that the first one of \(W\) is assigned to the first copy and the second one to the second. If both copies have \(u\) zeros before their ones, then the first copy takes \(u\) of the initial \(a\) zeros. The second takes the other \(a-u\) initial zeros and must take \(2u-a\) of the middle \(b\) zeros. The second copy needs \(n-1-u\) final zeros after its one, all taken from the last gap. These requirements are feasible exactly when
\[
0\le u\le a,\qquad 0\le2u-a\le b,\qquad n-1-u\le c.
\]
The remaining zeros automatically complete the first copy, because the total zero count is \(2n-2\). Consequently the feasible roots are precisely the integers in \([L,U]\), where
\[
L=\max\!\left(\left\lceil\frac a2\right\rceil,n-1-c\right),\qquad
U=\min\!\left(a,\left\lfloor\frac{a+b}{2}\right\rfloor\right).
\]
Thus
\[
R(W)=\max(0,U-L+1).
\]
This interval is an exact characterization for all nonnegative gaps, including adjacent ones and boundary gaps.

**Gap lower bounds and contraction.** From the bounds defining \(L,U\), one obtains
\[
R(W)\le\left\lfloor\frac a2\right\rfloor+1,\qquad
R(W)\le\left\lfloor\frac b2\right\rfloor+1,\qquad
R(W)\le\left\lfloor\frac c2\right\rfloor+1.
\]
For the last inequality use \(a+b=2n-2-c\), so \(\lfloor(a+b)/2\rfloor=n-1-\lceil c/2\rceil\). It follows that \(R(W)\ge h+1\) requires \(a,b,c\ge2h\).

For such gaps delete \(2h\) zeros from each of the three gaps, giving the shorter word
\[
W'=0^{a-2h}1\,0^{b-2h}1\,0^{c-2h},\qquad n'=n-3h\ge1.
\]
In the shorter word the root-interval endpoints satisfy \(L'=L-h\) and \(U'=U-2h\). Hence
\[
R(W')=\max(0,R(W)-h).
\]
In particular, with \(h=r-1\), every word with at least \(r\) roots contracts uniquely to a word with at least one root at length \(2(n-3r+3)\). Conversely, inserting \(2(r-1)\) zeros into **each** of the three gaps of any shorter shuffle square produces a word with at least \(r\) roots, by the same interval identities. These operations are inverse bijections.

**Count of one-root-or-more words.** A word \(0^a1\,0^b1\,0^c\in\mathcal W_m\) has \(R(W)\ge1\) if and only if \(b\le m-1\) and either \(b\ge1\) or \(a\) is even; this follows by comparing \(L\) and \(U\). In terms of the positions of the two ones, the forbidden cases consist of a separation greater than \(m\) (there are \(m(m-1)/2\) such pairs) or adjacent ones beginning at an even position (there are \(m-1\) such pairs). The two forbidden families are disjoint. Therefore
\[
\#\{W\in\mathcal W_m:R(W)\ge1\}
=\binom{2m}{2}-\frac{m(m-1)}2-(m-1)
=1+\frac{3m(m-1)}2=H(m).
\]
For \(m\le0\), the shorter family is empty by definition. Applying the contraction bijection proves the claimed tail count. Subtracting consecutive tails yields the exact multiplicity formula.

**Sharp maximum.** The tail is positive if and only if \(n-3r+3\ge1\), equivalently \(r\le\lfloor(n+2)/3\rfloor\). At this maximum the shorter length parameter is \(1\), \(2\), or \(3\) according as \(n\equiv1\), \(2\), or \(0\pmod3\). The maximizer counts are therefore \(H(1)=1\), \(H(2)=4\), or \(H(3)=10\), as claimed. This proves the theorem.

## Verification

A standalone, standard-library Python checker is included as `verify.py`. Invoke `python3 verify.py` from the extracted files. It independently recognizes interleavings using a two-index dynamic program, compares the resulting root counts with the interval formula for every two-marker word of lengths \(2n\) with \(1\le n\le12\), and independently enumerates the tail, maximum, exact-multiplicity, three-gap-contraction, and total root-incidence identities through \(n=100\). Its verified output ends with `VERIFY_OK`.

For example, at \(n=7\) the word \(0^4 1\,0^4 1\,0^4\) has exactly three roots, corresponding to \(u=2,3,4\). The exact multiplicity counts at that length are \(45\) words with one root, \(18\) with two, \(1\) with three, and \(27\) with none, totaling \(\binom{14}{2}=91\). As a separate incidence check, the total number of word-root pairs is \(\binom{n+2}{3}\), consistent with summing the known numbers of shuffle squares generated by each one-one root.

## Relationship to prior work

Grytczuk, Pawlik and Pleszczyński, *Variations on shuffle squares* (first posted 2023), Theorem 3 and Corollary 1, already characterize **which** weight-two words are shuffle squares and count them as \(H(n)\). Those facts are not claimed as new. The contribution here is the complete **inverse multiplicity distribution** \(\#\{R(W)=r\}\), the exact root interval, and the three-gap contraction bijection which shifts each multiplicity tail by three units of half-length.

Datko and Pawlik, *Roots of Binary Shuffle Squares* (2025), study the number of words generated by a fixed root, numerical maximum root counts, and special one-root families; the one-marker root outgoing counts are not the inverse multiplicities for fixed two-marker output words. Grytczuk, Pawlik and Ruciński, *Shuffle squares and ordered nest-free graphs* (2025), include four- and five-run membership characterizations but do not state this inverse-root spectrum in the inspected relevant sections. No global novelty or independence claim is inferred solely from database search.

## Limitations

The theorem applies only to binary words with exactly two ones (and, by complementing symbols, exactly two zeros). It does not enumerate all binary shuffle squares, all interleaving colorings, or words of arbitrary composition. The algebraic proof is for all specified lengths; finite dynamic-programming checks are independent crosschecks, not a substitute for the argument. Priority assessment is limited by indexed literature coverage, especially any inaccessible supplementary material of relevant works. Independent scientific validation has not been performed.

## References

- J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882, first submitted August 26, 2023, especially Theorem 3 and Corollary 1: https://arxiv.org/abs/2308.13882
- D. Datko and B. Pawlik, *Roots of Binary Shuffle Squares*, *Symmetry* 17(2), 305 (2025), especially Proposition 1, Theorem 2, and root-count tables: https://doi.org/10.3390/sym17020305
- J. Grytczuk, B. Pawlik and A. Ruciński, *Shuffle squares and ordered nest-free graphs*, arXiv:2503.22043, especially Section 3.1: https://arxiv.org/abs/2503.22043
