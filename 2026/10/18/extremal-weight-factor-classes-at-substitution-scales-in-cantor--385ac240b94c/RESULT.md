# Extremal-weight factor classes at substitution scales in Cantor-like words

## Finding

For every integer \(q\ge3\), let \(c_q\) be the infinite binary fixed point beginning with \(1\) of the substitution
\[
\sigma_q(1)=10^{q-2}1,\qquad \sigma_q(0)=0^q.
\]
For every integer \(k\ge0\), put \(L=q^k\), \(W=\sigma_q^k(1)\), and \(T=2^k\). Write \(\mathcal F_q(n)\) for the set of distinct contiguous length-\(n\) factors of \(c_q\), and \(\mathcal E_q(n)\) for those having the largest number of \(1\)s.

At the substitution length, \(\mathcal E_q(L)=\{W\}\) and its maximal number of \(1\)s is \(T\). At twice that length, the maximal number is again \(T\), and the complete extremal class is
\[
\mathcal E_q(2L)=
\big\{0^jW0^{L-j}:0\le j\le L\big\}
\ \cup\ 
\begin{cases}
\big\{W[r:L]0^LW[0:r]:1\le r<L\big\},&q=3,\\
\varnothing,&q\ge4.
\end{cases}
\]
The union is disjoint. Consequently,
\[
|\mathcal E_q(2q^k)|=
\begin{cases}2q^k,&q=3,\\q^k+1,&q\ge4.\end{cases}
\]
Here \(W[a:b]\) means positions \(a,a+1,\ldots,b-1\) using zero-based indices.

A complete classification of **all** length-\(2L\) factors, proved below, additionally yields
\[
|\mathcal F_q(2L)|=
\begin{cases}4L-1,&q=3,\\3L,&q\ge4.\end{cases}
\]
Thus the proportion of distinct length-\(2q^k\) factors belonging to the maximum-one-count class tends, as \(k\to\infty\), to \(1/2\) for the ordinary Cantor word but to \(1/3\) for every fixed \(q\ge4\). The total factor-count values agree with the previously established Cantor-like factor-complexity formulas; the classification of the maximum-weight class is the result of interest.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Factors are *contiguous* finite words, and words are counted once regardless of their number of occurrences. Integers \(q\ge3\), \(k\ge0\) are unrestricted. No claim is made for intermediate lengths other than \(q^k\) and \(2q^k\). Notation \(0^j\) denotes \(j\) copies of symbol \(0\), with \(0^0\) empty.

## Proof

**1. Substitution-scale block structure.** Fix \(q,k\) and set \(L=q^k\), \(W=\sigma_q^k(1)\). Since \(\sigma_q\) is uniform of length \(q\), the fixed point can be partitioned into consecutive aligned blocks of length \(L\), one block per symbol of \(c_q\). An upper-level \(1\) produces \(W\); an upper-level \(0\) produces \(0^L\). Each \(W\) begins and ends with \(1\) and contains exactly \(T=2^k\) ones. Therefore every proper prefix or suffix of \(W\) has strictly fewer than \(T\) ones. Every run of zeros strictly inside \(W\) has length less than \(L\).

The word \(c_q\) has no adjacent \(1\)s: the substitution has no adjacent \(1\)s inside either image and each \(1\)-image has its first and last \(1\) separated, while adjacent images do not create \(11\) because any two consecutive source symbols cannot both be \(1\). More directly, its \(1\)s occur exactly at positions whose base-\(q\) digits all belong to \(\{0,q-1\}\). For \(q\ge4\), occurrences of \(1\) are separated by at least two zeros, so \(101\) cannot occur. For \(q=3\), both \(101\) and \(010\) occur. For every \(q\ge3\), the patterns \(000\), \(100\), \(001\), and \(010\) all occur: arbitrarily long zero runs occur, and \(1\)s are isolated with zeros on both sides.

**2. Length \(L\).** Every length-\(L\) factor either equals an aligned block or straddles exactly two adjacent blocks. An aligned \(W\) has \(T\) ones; any aligned zero block has none. A straddling factor cannot encounter two \(W\)-blocks because the upper sequence has no adjacent \(1\)s. Thus it contains at most a proper prefix or suffix of one \(W\), hence strictly fewer than \(T\) ones. This proves \(\mathcal E_q(L)=\{W\}\).

**3. Full length-\(2L\) factor classification.** For convenience introduce five sets:
\[
\begin{aligned}
\mathcal Z&=\{0^{2L}\},\\
\mathcal A&=\{0^jW0^{L-j}:0\le j\le L\},\\
\mathcal B&=\{W[r:L]0^{L+r}:1\le r<L\},\\
\mathcal C&=\{0^{2L-r}W[0:r]:1\le r<L\},\\
\mathcal D&=\{W[r:L]0^LW[0:r]:1\le r<L\}.
\end{aligned}
\]
At a block boundary, a length-\(2L\) factor spans two adjacent upper-level symbols. Since those symbols cannot both be \(1\), it lies in \(\mathcal Z\cup\mathcal A\). Otherwise its start has a unique offset \(r\), with \(1\le r<L\), within a block. Such a factor consists of the last \(L-r\) symbols of a block \(X\), the entire next block \(Y\), and the first \(r\) symbols of the following block \(Z\). Each of \(X,Y,Z\) is \(W\) or \(0^L\), and adjacent \(W\)-blocks are prohibited. If \(Y=W\), both neighbors are zero blocks and the factor lies in \(\mathcal A\). If \(Y=0^L\), the factor lies in \(\mathcal Z\), \(\mathcal B\), \(\mathcal C\), or \(\mathcal D\) according as neither, only \(X\), only \(Z\), or both outer blocks are \(W\). The last case is possible exactly when \(101\) occurs at the upper level, that is, for \(q=3\).

Conversely, the occurrences of upper patterns \(000,010,100,001\), and for \(q=3\) also \(101\), ensure that every word displayed in these families is an actual factor. Hence
\[
\mathcal F_q(2L)=
\begin{cases}
\mathcal Z\cup\mathcal A\cup\mathcal B\cup\mathcal C\cup\mathcal D,&q=3,\\
\mathcal Z\cup\mathcal A\cup\mathcal B\cup\mathcal C,&q\ge4.
\end{cases}
\]
These families are disjoint: \(\mathcal Z\) is the only zero word; words of \(\mathcal B\) have all their \(1\)s strictly in the first length-\(L\) half, whereas those of \(\mathcal C\) have all their \(1\)s strictly in the second half; words of \(\mathcal D\) have \(1\)s in both halves, with an internal zero run of length \(L\) flanked by \(1\)s. No \(\mathcal A\)-word has such an internal run, because it has just one full \(W\) and any zeros outside \(W\) are terminal. The words of \(\mathcal A\) are distinguished by their first \(1\) position \(j\); those of \(\mathcal B\) by the length \(L+r\) of their terminal zero run; and those of \(\mathcal C\) by the position \(2L-r\) of their first \(1\). Words of \(\mathcal D\) are distinguished by the start position of their internal length-\(L\) zero run, since the interiors of both proper \(W\)-pieces contain no zero run that long. Thus their sizes are respectively \(1,L+1,L-1,L-1,L-1\), with \(\mathcal D\) present only when \(q=3\). Summing proves the stated total factor counts.

**4. Extremal one-count class.** Each \(\mathcal A\)-word has exactly \(T\) ones. Each \(\mathcal D\)-word also has exactly \(T\), since \(W[r:L]\) and \(W[0:r]\) partition the positions of \(W\). A \(\mathcal B\)- or \(\mathcal C\)-word has strictly fewer than \(T\), because its only nonzero block piece is a proper prefix or suffix of \(W\). The zero word has none. Therefore \(\mathcal A\), together with \(\mathcal D\) exactly when \(q=3\), is the entire maximizing class. This proves all formulas and proportions. \(\square\)

## Verification

The standalone script `verify.py` constructs the fixed points by substitution and independently by the criterion that a positive position has symbol \(1\) exactly when every base-\(q\) digit is \(0\) or \(q-1\). For every \(3\le q\le8\) and \(0\le k\le3\), it enumerates all observed factors of the two target lengths in a substitution prefix, compares the complete length-\(2q^k\) factor set with the five-family classification, verifies maxima and complete extremal sets, and checks both cardinality formulas. It returns `VERIFY_OK cases=24`. The infinite proof is the block argument, not this finite test.

## Relationship to prior work

Lü, Chen, Guo and Wen study the same Cantor-like substitutions and prove total factor-complexity formulas and permutation complexity formulas (first publicly available online December 29, 2015). Their total factor counts are consistent with the present length-\(2q^k\) enumeration. Counting *all* factors does not specify which individual factors lie in a given Parikh (one-count) fiber. In particular, those numerical totals do not imply the explicit maximizing set or its sharp dependence on \(q\).

Chen, Lü and Wu subsequently establish that the ordinary Cantor word's maximum one-count over length-\(n\) factors equals its prefix count (Lemma 2 of their March 2017 preprint). That already covers the maximum value for \(q=3\), and is not claimed here as new. It does not enumerate the distinct maximizers and does not treat the parameter-wide multiplicity dichotomy. The present result is the classification and cardinality of the extreme Parikh fiber, with an elementary full-factor decomposition at the indicated scales.

## Limitations

Only lengths \(q^k\) and \(2q^k\) are classified; no formula for all intermediate lengths is claimed. The limiting fractions count distinct factors rather than occurrences. The total complexity counts alone were known, and the maximum one-count in the ordinary Cantor word was known: the proposed contribution is the complete extremal-factor fiber and its cross-parameter transition. Despite targeted literature comparisons, an equivalent specialized classification in other sources cannot be excluded without broader independent review.

## References

1. X.-T. Lü, J. Chen, Y.-J. Guo, and Z.-X. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science **616** (2016), 100–110, DOI: 10.1016/j.tcs.2015.12.022. Available online December 29, 2015. Section 3 treats factor complexity.
2. J. Chen, X.-T. Lü, and W. Wu, *On the \(k\)-abelian complexity of the Cantor sequence*, arXiv:1703.04063 (first version March 12, 2017), especially Lemma 2 and Corollary 1 for ordinary-Cantor maximum one-counts.
