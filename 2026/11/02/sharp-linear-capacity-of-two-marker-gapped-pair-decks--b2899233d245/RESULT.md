# Sharp linear capacity of two-marker gapped pair decks

## Finding

Fix an integer separation parameter \(s\ge 2\). For a binary word \(w=w_1\cdots w_n\) with exactly two ones, its **\(s\)-gapped pair deck** is the four-component vector \(\mathcal D_s(w)=(N_{00},N_{01},N_{10},N_{11})\), where \(N_{ab}\) counts ordered pairs of positions \(1\le p<q\le n\) with \(q-p\ge s\) and \((w_p,w_q)=(a,b)\). Let \(C_s(n)\) be the number of distinct such decks as \(w\) ranges over all binary words of length \(n\) with exactly two ones.

**Theorem.** For \(s=2\) and \(n\ge5\),
\[
C_2(n)=5n-15.
\]
For all \(s\ge3\) and \(n\ge3s-1\),
\[
C_s(n)=(2s+2)n-3s^2-2s-3.
\]
The onset is sharp: for every \(s\ge3\), the value at \(n=3s-2\) is **one larger** than the evaluation of the displayed linear polynomial. Likewise \(C_2(4)=6\), one larger than \(5\cdot4-15\).

Consequently, in these ranges, \(C_s(n)\) is exactly the largest zero-error code size among weight-two length-\(n\) binary words observed only through their \(s\)-gapped pair decks. No assertion is made about lengths below the displayed ranges beyond the stated immediate boundary.

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\); word orientation and positions are fixed, and reversal is not identified. The two ones occupy distinct integer positions \(1\le i<j\le n\). Both the multiplicities and the ordering of letters in a two-letter subsequence are observed; pairs with index separation less than \(s\) are excluded. The weight-two promise is part of the decoding model. The total admissible-pair count is \(T=(n-s)(n-s+1)/2\) when \(n\ge s\). All claims are exact integer equalities, not asymptotic estimates or statements about unweighted subsequence *sets*.

## Proof

**1. Reduce the deck to two coordinate sums and a spacing bit.** For a position \(p\), define
\[
L(p)=\max(p-s,0),\qquad R(p)=\max(n-s+1-p,0).
\]
These count, respectively, positions at least \(s\) earlier and positions at least \(s\) later than \(p\). Set
\[
X=L(i)+L(j),\quad Y=R(i)+R(j),\quad h=\mathbf1_{\{j-i\ge s\}}.
\]
Counting the admissible pairs before and after the two ones, and subtracting the possible \(11\) pair once, gives
\[
(N_{00},N_{01},N_{10},N_{11})=(T-X-Y+h,\ X-h,\ Y-h,\ h).
\]
The deck is therefore equivalent to the triple \((X,Y,h)\): it determines \(h\), then \(X=N_{01}+h\) and \(Y=N_{10}+h\). In particular, different values of \((X+Y,h,X)\) specify different decks.

**2. Decompose the position curve.** Put \(t=n-2s+1\). For the principal range \(s\ge3\), \(n\ge3s-1\), we have \(t\ge s\). The complete position set breaks into three disjoint zones:
\[
\begin{array}{c|c|c}
\text{zone}&p&(L(p),R(p))\\\hline
\text{left}&s-a,\ 1\le a\le s-1&(0,t+a)\\
\text{middle}&s+u,\ 0\le u\le t&(u,t-u)\\
\text{right}&s+t+b,\ 1\le b\le s-1&(t+b,0).
\end{array}
\]
Every pair of distinct positions belongs to one of the six types \(LL,LM,LR,MM,MR,RR\), ordered from left to right. Define the nonnegative **excess** \(\delta=X+Y-2t\). A middle position contributes zero excess; a left or right position contributes its boundary distance \(a\) or \(b\). We count distinct pairs \((X,h)\) separately at each fixed excess \(\delta\); different excesses cannot collide.

**3. The zero-excess slice.** Here both positions lie in the middle zone, with parameters \(0\le u<v\le t\), \(X=u+v\), and \(h=\mathbf1_{\{v-u\ge s\}}\). When \(h=0\), the separations \(1\) and \(2\), both available because \(s\ge3\), yield every odd and every even integer from \(1\) through \(2t-1\), respectively. No other \(X\) occurs. Thus there are \(2t-1\) zero-excess decks with \(h=0\).

When \(h=1\), sums range from \(s\) to \(2t-s\). Separation exactly \(s\) supplies one parity of sums; separation \(s+1\), when available, supplies the other parity. For \(t=s\) the interval is the singleton \(\{s\}\). Hence **every** integer in this interval occurs, giving \(2t-2s+1\) decks with \(h=1\). The zero-excess contribution is therefore \(4t-2s\).

**4. The low positive-excess slices.** Fix \(1\le\delta\le s-1\). The \(LM\) pairs have left parameter \(a=\delta\) and give \(X=0,1,\ldots,t\). The \(MR\) pairs have right parameter \(b=\delta\) and give \(X=t+\delta,\ldots,2t+\delta\). The \(LR\) pairs with \(a+b=\delta\) fill the missing values \(X=t+1,\ldots,t+\delta-1\). Thus every integer \(0\le X\le 2t+\delta\) occurs. For each such \(X\), its zone type is determined, except that \(LL\) or \(RR\) can repeat the corresponding extreme values. These extreme repetitions have \(h=0\), just as the \(LM\) or \(MR\) representatives: in all cases the two positions are separated by less than \(s\). Thus no value of \(X\) occurs with both values of \(h\) at this excess. There are exactly \(2t+\delta+1\) decks at excess \(\delta\).

**5. The high-excess slices.** When \(s\le\delta\le2s-2\), no pair uses a middle position. Each \(LR\) pair is uniquely determined by \((a,b)\in\{1,\ldots,s-1\}^2\), contributes \(X=t+b\), and has \(h=1\) because \(j-i=t+a+b\ge s\). Across all these high-excess slices, there are \(s(s-1)/2\) such pairs, since \(a+b\ge s\). Each gives a different \((\delta,X)\).

A pair of distinct left-zone positions \((LL)\) or distinct right-zone positions \((RR)\) has \(h=0\) and occurs in a high-excess slice exactly when \(s\le\delta\le2s-3\). Each such excess has both an \(LL\) representative, contributing \(X=0\), and an \(RR\) representative, contributing \(X=2t+\delta\). Neither overlaps an \(LR\) value \(X=t+b\). Thus the additional high-excess contribution is \(2(s-2)\).

**6. Sum the slices.** The total is
\[
\begin{aligned}
C_s(n)&=(4t-2s)+\sum_{\delta=1}^{s-1}(2t+\delta+1)
 +\frac{s(s-1)}2+2(s-2)\\
&=(2s+2)t+s^2-5\\
&=(2s+2)n-3s^2-2s-3.
\end{aligned}
\]
No pair type is omitted, all counted parameter values are realized by actual positions, and the deck coordinates separate the listed cases.

**7. Sharpness of the onset.** At \(n=3s-2\) and \(s\ge3\), \(t=s-1\). The arguments for positive excesses remain valid. In the zero-excess slice the \(h=0\) sums still fill \(1,\ldots,2t-1\), but there is no pair at spacing at least \(s\). Thus that slice has \(2t-1\) decks instead of the formal continuation \(4t-2s=2t-2\), giving an excess of one.

**8. Separation two.** When \(s=2\) and \(n\ge5\), write \(t=n-3\ge2\). The zero-excess slice has \(t\) decks with \(h=0\) (only odd sums from adjacent middle positions) and \(2t-3\) with \(h=1\) (all sums \(2,\ldots,2t-2\)), hence \(3t-3\) total. Excess one contributes \(2t+2\); excess two consists of the one \(LR\) pair. Thus \(C_2(n)=5t=5n-15\). At \(n=4\), the zero-excess slice has one deck instead of the formal value zero, whence \(C_2(4)=6\).

**9. Coding consequence.** A zero-error code cannot contain two words having the same deck. Conversely, choose one arbitrary representative for each realizable deck; those representatives form a zero-error code. Therefore the optimum code cardinality is exactly \(C_s(n)\).

## Verification

The accompanying `verify_gapped_weight2.py` independently enumerates every admissible index pair for short lengths and compares literal four-count decks with the analytic coordinate formula. It then enumerates all pairs of marker positions and checks the claimed capacity and sharp boundary. A completed run reported `VERIFY_OK gap_values=2..18 cases=748 literal_pair_observations=14535 position_pairs=540294 theorem_instances=442 sharp_boundary_instances=17`. The literal pair-reading loop is executed for lengths at most \(19\); larger lengths use the independently defined coordinate formula. This finite experiment is a consistency check, not an exhaustive proof for arbitrary lengths.

## Relationship to prior work

Golm, Nahvi, Gabrys and Milenkovic introduced gap-constrained subsequence decks and investigated the shortest length at which collisions are possible, emphasizing multilevel decks and broad word families. Their accessible abstract and indexed preliminary passages describe a different reconstruction threshold problem, not this all-\(s\) capacity formula restricted to exactly two ones. Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao studied cardinalities of ordinary, *ungapped* \(k\)-decks; their accessible full text gives exact ordinary \(2\)-deck counts and a trellis approach. Its observations range over all index pairs instead of pairs separated by at least \(s\), so its formulas do not imply the result above without a new spacing analysis.

## Limitations

The theorem concerns precisely two ones, ordered binary pairs, and a known length and minimum spacing. It does not enumerate decks at arbitrary weights, does not recover individual word multiplicities, and does not give a closed formula for every short transient length. Finite tests do not independently establish the infinite theorem. Full text of the most directly relevant gapped-deck paper could not be inspected completely from available access; the novelty comparison therefore carries residual literature risk. An independently conducted mathematical review has not been performed.

## References

1. R. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, *The Gapped k-Deck Problem*, arXiv:2201.12671, first public 2022-01-29; DOI: 10.1109/ISIT50566.2022.9834537. https://arxiv.org/abs/2201.12671
2. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, early access 2021-08-30, *Advances in Mathematics of Communications* 17 (2023), 960-978, DOI: 10.3934/amc.2021032. https://www.researchgate.net/publication/354441361_On_the_number_of_distinct_k_-decks_Enumeration_and_bounds
