# Exact binary three-subsequence universality counts in every Parikh-matrix class

## Finding
For integers \(a,b\ge3\) and \(0\le c\le ab\), let \(\mathcal F_{a,b,c}\) be the set of binary words having \(a\) zeros, \(b\) ones, and exactly \(c\) scattered occurrences of \(01\). A word is *three-universal* if each of the eight binary length-three words occurs as a (not necessarily contiguous) subsequence. Write \(P_{a,b}(c)=|\mathcal F_{a,b,c}|\) and \(U_{a,b}(c)\) for the number of three-universal members. Set \(h=ab\) and let \(\mathbf1[E]\) be one when statement \(E\) is true, zero otherwise. Define
\[
\begin{aligned}
R_{a,b}(c)={}&\mathbf1[0\le c\le b]+\mathbf1[0\le c\le a]\\
 &+\mathbf1[h-b\le c\le h]+\mathbf1[h-a\le c\le h]\\
 &+\mathbf1[a\mid c]+\mathbf1[b\mid c]\\
 &-3\mathbf1[c=0]-3\mathbf1[c=h]\\
 &-\mathbf1[c=1]-\mathbf1[c=h-1]\\
 &-\mathbf1[c=a]-\mathbf1[c=b]\\
 &-\mathbf1[c=h-a]-\mathbf1[c=h-b].
\end{aligned}
\]
Then the exact three-universal census in every binary Parikh-matrix class is
\[
U_{a,b}(c)=P_{a,b}(c)-R_{a,b}(c),\quad
P_{a,b}(c)=[t^c]\prod_{j=1}^{a}\frac{1-t^{b+j}}{1-t^j}.
\]
Moreover \(0\le R_{a,b}(c)\le2\), and
\[
\sum_{c=0}^{ab}R_{a,b}(c)=3(a+b)-6.
\]
Thus every such Parikh class has at most two members that fail three-universality, regardless of the size of the class.

## Assumptions and scope
Words are finite over the ordered alphabet \(\{0,1\}\), with subsequence occurrences counted by choices of strictly increasing positions. Only three-universality is classified here. The hypothesis \(a,b\ge3\) is essential: it ensures that \(000\) and \(111\) are present and that the exceptional-family collision list below is complete. The parameter \(c\) ranges over the integer interval from zero through \(ab\). The displayed Gaussian polynomial is a polynomial despite the rational-product presentation.

## Proof
**Six avoidance families.** Since \(a,b\ge3\), any word that is not three-universal avoids at least one of \(001,011,100,110,010,101\). Each avoidance class has one member for each parameter \(c\) indicated next (powers denote repetitions and endpoints are interpreted naturally).

* Avoiding \(001\): the words \(1^b0^a\) at \(c=0\) and \(1^{b-c}0\,1^c0^{a-1}\) for \(1\le c\le b\).
* Avoiding \(011\): the words \(1^b0^a\) at \(c=0\) and \(1^{b-1}0^c1\,0^{a-c}\) for \(1\le c\le a\).
* Avoiding \(100\): the words \(0^a1^b\) at \(c=ab\) and \(0^{a-1}1^r0\,1^{b-r}\) for \(1\le r\le b\), with \(c=ab-r\).
* Avoiding \(110\): the words \(0^a1^b\) at \(c=ab\) and \(0^r1\,0^{a-r}1^{b-1}\) for \(0\le r<a\), with \(c=ab-a+r\).
* Avoiding \(010\): the words \(1^{b-j}0^a1^j\) for \(0\le j\le b\), with \(c=aj\).
* Avoiding \(101\): the words \(0^i1^b0^{a-i}\) for \(0\le i\le a\), with \(c=bi\).

For example, \(001\) avoidance forces every \(1\) to have at most one preceding \(0\), so either all ones precede the zero block or exactly one zero may precede a final run of ones; the other descriptions follow by reflection, symbol exchange, or the fact that avoiding \(010\) forces all zeros to be contiguous. Their \(01\) counts are as displayed. This gives the six positive indicator terms in \(R_{a,b}(c)\).

**Exact overlaps.** At \(c=0\), the families for \(001,011,010,101\) share the word \(1^b0^a\), and at \(c=ab\), those for \(100,110,010,101\) share \(0^a1^b\). Each contributes three duplicated counts. In addition, exactly six pairwise coincidences occur, specified by forbidden types and \(c\): \((001,011;1)\), \((100,110;ab-1)\), \((011,010;a)\), \((001,101;b)\), \((110,010;ab-a)\), and \((100,101;ab-b)\). No others occur: the low-\(c\) mixed families and high-\(c\) mixed families are disjoint because \(ab>2\max(a,b)\); within one side, the displayed run structures force the stated junction coincidences; and a word with both symbols in a single contiguous block has either \(c=0\) or \(c=ab\). These coincidences need not have distinct numerical \(c\) values when \(a=b\), but the words at the collisions remain distinct as required. Subtracting precisely these duplicate counts gives the formula for \(R\).

**Bound and total.** In the middle region \(\max(a,b)<c<ab-\max(a,b)\), only the two single-block families can contribute, so \(R\le2\). At low \(c\), the \(001\)- and \(011\)-avoiding families contribute at most two distinct words; an extra single-block family may contribute only at a multiple of \(a\) or \(b\), but any possible third simultaneous candidate is already one of the six junction coincidences above. Hence there are at most two distinct exceptions for low \(c\). The high side follows by reversing the word or exchanging zero and one. Nonnegativity follows from counting genuine words. Counting all six families before overlap removal yields \(3(a+b)+6\) incidences, and the duplicate correction equals \(3+3+6=12\). Thus the number of distinct exceptional words over all fibers is \(3(a+b)-6\).

**Entire fiber size.** Summing \(t^{\#01(w)}\) over all binary words with \(a\) zeros and \(b\) ones gives the Gaussian binomial polynomial \(\prod_{j=1}^{a}(1-t^{b+j})/(1-t^j)\), by the usual last-symbol recursion (equivalently by reversal of the inversion statistic). Taking coefficient \(t^c\) and subtracting the explicit exceptional count completes the proof.

## Verification
The included standalone Python program enumerates every binary word for all \(a,b\ge3\) with \(a+b\le15\). It computes \(\#01\) and all length-three scattered subsequences directly, groups by \((a,b,c)\), and checks the exact formula, the upper bound of two exceptional words, and the total \(3(a+b)-6\). These exhaustive finite checks are independent corroboration of, not substitutes for, the proof for arbitrary \(a,b\).

## Relationship to prior work
Fazekas, Huang, and Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices* (publicly available October 5, 2026, arXiv:2610.06717), give criteria for whether binary Parikh-matrix classes contain universal words, and discuss probabilities and Gaussian binomial coefficients. In particular, their analysis of avoiding length-three subsequences motivates the present finer **exact number per class**; mere existence or nonexistence does not determine that number. A separately recorded closed-form length-only distribution of binary subsequence universality does not determine the joint distribution conditioned on both letter multiplicities and the \(01\) scattered-subsequence count. The result here supplies this conditional distribution together with a uniform bound of two nonuniversal representatives.

## Limitations
This classification assumes both letter multiplicities are at least three and universality is for length-three subsequences, not substrings. There is no assertion about alphabets larger than two or higher universality order. Overlap searches cannot exclude mathematically equivalent statements under unindexed terminology; priority would require an independent literature audit.

## References
Fazekas, Z., Huang, M., and Mercaş, R. *Subsequence Analysis Problems for Binary Parikh Matrices*. arXiv:2610.06717, first public October 5, 2026. https://arxiv.org/abs/2610.06717
