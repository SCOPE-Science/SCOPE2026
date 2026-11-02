# Parity dichotomy for circular 2-Abelian squares of Rudin–Shapiro prefixes

## Finding
For every integer \(k\ge 2\), let \(R_k=r(0)r(1)\cdots r(2^k-1)\), where \(r(t)\in\{0,1\}\) is the parity of the number of (overlapping) occurrences of \(11\) in the ordinary binary expansion of the nonnegative integer \(t\). Number positions from zero. At a cyclic cut \(i\), form the length-\(2^k\) rotation and divide it into consecutive halves \(U_i,V_i\) of length \(2^{k-1}\). Call the cut *2-Abelian-square-producing* if both halves have equal occurrences of **every** binary factor of length one or two.

The complete set of such cuts is
\[
\mathcal A_k=\begin{cases}
\varnothing,&k\text{ even},\\
\{i:1\le i<2^{k-2}\}\,\cup\,\{i:2^{k-1}<i<3\cdot2^{k-2}\},&k\text{ odd}.
\end{cases}
\]
Thus the number of positioned 2-Abelian-square-producing rotations is zero for even ranks and exactly \(2^{k-1}-2\) for odd ranks. The odd-rank fraction of such rotations tends to \(1/2\) while every even rank has none.

## Assumptions and scope
The binary expansion used to define \(r(t)\) has no leading ones; leading zeros do not affect the statistic. Cyclic rotations are indexed by their starting **positions**, not identified as abstract conjugates. Only a full-length rotation, cut into exactly two equal halves, is considered; this theorem does not classify shorter 2-Abelian squares within the word. Equality of length-one and length-two factor counts is evaluated linearly inside each half, so there is no two-letter factor crossing the internal boundaries of a half.

## Proof
Encode binary symbols by signs \(+1\) for \(0\) and \(-1\) for \(1\). Set \(P_0=Q_0=(+1)\) and recursively concatenate sign words by
\[
P_{j+1}=P_jQ_j,\qquad Q_{j+1}=P_j(-Q_j),
\]
where \(-Q_j\) negates every sign. The coefficient of \(P_k\) at index \(t\) is \((-1)^{r(t)}\): for an appended leading zero the lower-digit count is unchanged, while appending a leading one changes the parity by the previous highest bit. The latter contribution is precisely the difference between \(P_j\) and \(Q_j\) in the upper half. The assertion also follows directly by induction from the displayed recursion, which is the standard Rudin–Shapiro recursion.

Write \(m=k-2\), \(L=2^m\), \(A=P_m\), and \(B=Q_m\). The full sign word underlying \(R_k\) is
\[
P_k=A\,B\,A\,(-B).
\]
Let \(p_j\) and \(q_j\) be the total signs in \(P_j\) and \(Q_j\). They obey
\[
(p_0,q_0)=(1,1),\qquad (p_{j+1},q_{j+1})=(p_j+q_j,p_j-q_j).
\]
A two-step induction gives \(q_{2h}=2^h\) and \(q_{2h+1}=0\) for every \(h\ge0\). Consequently, \(B\) and \(-B\) have the same numbers of each sign exactly when \(m\) is odd.

We use a binary characterization: two equal-length words of length at least two are 2-Abelian equivalent if and only if they have equal counts of one of the two symbols, equal first and last symbols, and equal numbers of transitions between unequal adjacent symbols. Necessity follows because first/last symbols can be recovered from the one-symbol counts and the two-letter counts. For sufficiency, the endpoints and the transition total determine separately the numbers of \(01\) and \(10\); the one-symbol counts then determine \(00\) and \(11\).

A cut beginning within the \(B\) block or within the \(-B\) block cannot work: the two halves begin with opposite signs, since the blocks separated by half the full length are \(B\) and \(-B\). A cut at the first position of either copy of \(A\) also fails: the two halves are \(AB\) and \(A(-B)\), which have opposite last signs.

All remaining cuts lie strictly inside one of the two copies of \(A\). Fix such a cut, at offset \(i\) with \(0<i<L\) inside its copy. Up to exchange of the halves, the two sign words being compared are
\[
X=A[i:L]\,B\,A[0:i],\qquad Y=A[i:L](-B)A[0:i].
\]
Their first and last symbols coincide. The internal transition count of \(B\) is unchanged under sign negation, and the two \(A\) fragments agree literally. It remains to compare the two transitions at the joints. For \(m\ge1\), the first sign of each of \(A,B\) is \(+1\), while the final signs of \(A\) and \(B\) are respectively \((-1)^{m-1}\) and \((-1)^m\), as follows by induction from the recursion. Their final signs are opposite. Thus **exactly one** of the two joints is a transition for \(X\), and exactly one is a transition for \(Y\). The transition totals are equal. Their symbol counts agree precisely when \(q_m=0\), equivalently \(m\) is odd. Since \(m=k-2\), this means \(k\) is odd.

There are \(L-1\) strict interior cuts in each of the two \(A\) copies. Their zero-based positions are \(1,\ldots,L-1\) and \(2L+1,\ldots,3L-1\). The formula and count follow. At \(k=2\), \(L=1\) and there are no strict interior cuts, so the same conclusion holds without using the \(m\ge1\) endpoint identity. This proves all ranks.

## Verification
Run `python3 checker.py` in the same directory. The standalone checker constructs signs independently in two ways: from the bitwise overlapping-\(11\) count and from the two-word recursion. It directly computes all five 2-Abelian signature components (one-symbol count and four two-symbol counts) of both halves at every cyclic starting position, and compares the exact sets of cuts for ranks \(2\) through \(14\) inclusive. It also checks the sign-sum and endpoint identities used in the proof. These finite computations check the implementation and boundary cases; the proof above establishes the unrestricted statement.

## Relationship to prior work
Parreau, Rigo, Rowland and Vandomme (2014 preprint; 2015 publication) develop 2-Abelian factor-complexity methods for Thue–Morse and period-doubling, not this positioned cyclic Rudin–Shapiro rotation classification. Lü, Chen, Wen and Wu (2016) analyze **1-Abelian complexity of the infinite Rudin–Shapiro sequence**, which does not determine equality of adjacent-pair counts for the two finite halves. Brillhart, Erdős and Morton (1983), and Rampersad and Shallit (2025), investigate sums of Rudin–Shapiro coefficients; their sum identities alone do not establish the boundary-transition conditions required here. In particular, the main statement classifies 2-Abelian-square *positions*, not the distribution of letter sums. This comparison is based on the specifically inspected material, not a claim that every publication has been exhaustively checked.

## Limitations
The exact formula concerns the canonical binary coding of **complete dyadic prefixes** and the full-length cyclic rotations. No assertion is made about arbitrary prefixes, shorter cyclic factors, higher-order Abelian equivalence, or distinct rotations modulo equality. Other historical sources could conceivably contain an equivalent rotation classification; an independent audit and exhaustive historical-priority verification have not been performed.

## References
1. A. Parreau, M. Rigo, E. Rowland and É. Vandomme, *A new approach to the 2-regularity of the ℓ-Abelian complexity of 2-automatic sequences*, arXiv:1405.3532, initially public 2014-05-14, Electronic Journal of Combinatorics **22** (2015), P1.27. https://arxiv.org/html/1405.3532v2
2. X. Lü, J. Chen, Z. Wen and W. Wu, *On the Abelian complexity of the Rudin–Shapiro sequence*, arXiv:1606.06935, initially public 2016-06-22. https://arxiv.org/abs/1606.06935
3. J. Brillhart, P. Erdős and P. Morton, *On sums of Rudin–Shapiro coefficients II*, Pacific Journal of Mathematics **107** (1983), 39–69. https://msp.org/pjm/1983/107-1/pjm-v107-n1-p04-s.pdf
4. N. Rampersad and J. Shallit, *Rudin–Shapiro sums via automata theory and logic*, Theory of Computing Systems (2025). https://link.springer.com/article/10.1007/s00224-025-10214-1
