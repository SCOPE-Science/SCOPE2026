# A sharp five-weight gap for Bernoulli mean crossings

## Finding

**Theorem (five-weight mean crossing and sharp light-stake gap).** Let \(1\le m\le5\), let \(w_1,\ldots,w_m\ge0\) satisfy \(\sum_{i=1}^{m}w_i=1\), and let \(B_1,\ldots,B_m\) be independent \(\operatorname{Bernoulli}(p)\) variables with a common parameter \(0\le p\le1/3\). Set \(X=\sum_{i=1}^{m}w_iB_i\), so \(\mathbb E X=p\). Then

\[
\Pr(X\ge p)\ge p.
\]

More precisely, in the **light-stake regime** \(0<p\le1/3\) and \(\max_i w_i<p\),

\[
\Pr(X\ge p)-p>\frac{3}{256}.
\]

The constant \(3/256\) is the **sharp, unattained infimum** of this excess over all such light-stake choices with at most five weights. The baseline \(\Pr(X\ge p)\ge p\) is also sharp and attained for strictly positive five-weight vectors. In particular, a counterexample to the mean-crossing inequality in this parameter range requires at least six nonzero weights.

## Assumptions and scope

The weights are deterministic, nonnegative, and normalized to sum to one. The Bernoulli variables are independent and identically distributed, with success probability equal to the comparison threshold. The event includes equality. The bound concerns \(m\le5\) and \(p\in[0,1/3]\) only; the light-stake statement requires strict \(\max_iw_i<p\).

Padding the vector by zeros reduces the proof to five weights. When \(p=0\), \(X=0\) almost surely and the first inequality is immediate. Hence assume \(p>0\).

## Proof

If some \(w_i\ge p\), the event \(\{B_i=1\}\) implies \(X\ge p\). Its probability is \(p\), proving the first inequality in this case.

Suppose henceforth that \(w_i<p\) for all five indices. Because the weights sum to one, \(1<5p\), hence \(p>1/5\). Moreover, **every subset of at least three indices is winning**: for a triple, the sum of its weights exceeds \(1-2p\ge p\), since the two omitted weights are each smaller than \(p\). Supersets are also winning.

Write \(e\) for the number of pairs \(\{i,j\}\) satisfying \(w_i+w_j\ge p\). Because the sampling bits are independent and equiprobable,

\[
\Pr(X\ge p)\ge \Pr(\operatorname{Bin}(5,p)\ge3)+e\,p^2(1-p)^3.
\tag{1}
\]

First suppose \(1/5<p\le1/4\). If one pair had total weight less than \(p\), the other three weights would each be less than \(p\), so the total of all five weights would be strictly smaller than \(4p\le1\), a contradiction. Thus every pair is winning, and

\[
\Pr(X\ge p)\ge\Pr(\operatorname{Bin}(5,p)\ge2)
\ge\Pr(\operatorname{Bin}(5,1/5)\ge2)=\frac{821}{3125}.
\]

The monotonicity used here follows by coupling five Bernoulli variables with common uniform random variables. Consequently,

\[
\Pr(X\ge p)-p\ge \frac{821}{3125}-\frac14
=\frac{159}{12500}>\frac{3}{256}.
\tag{2}
\]

Now suppose \(1/4<p\le1/3\), and sort the weights so that \(w_1\le w_2\le w_3\le w_4\le w_5\). **At least six pairs are winning.** If \(w_2+w_3\ge p\), all six pairs among indices \(2,3,4,5\) are winning. Otherwise \(w_2+w_3<p\). Then \(w_2+w_4\ge p\); indeed, if the opposite held, \(w_1+w_3\le w_2+w_4<p\) as well, and \((w_1+w_3)+(w_2+w_4)+w_5<3p\le1\), a contradiction. This establishes the five winning pairs \(\{2,4\},\{2,5\},\{3,4\},\{3,5\},\{4,5\}\). In addition \(w_1+w_5\ge p\), because otherwise \((w_1+w_5)+(w_2+w_3)+w_4<3p\le1\). Thus \(e\ge6\) in all cases.

Substitution in (1) gives

\[
\Pr(X\ge p)-p\ge F(p)
:=\Pr(\operatorname{Bin}(5,p)\ge3)+6p^2(1-p)^3-p
=p(p-1)(3p^2-5p+1).
\tag{3}
\]

Direct differentiation yields \(F'(p)=12p(1-p)^2-1\). On \([1/4,1/3]\), the bounds \(p\ge1/4\) and \(1-p\ge2/3\) give \(F'(p)\ge1/3>0\). Hence

\[
F(p)>F(1/4)=\frac{3}{256},
\]

proving the claimed strict gap, and therefore the basic bound, for every light-stake choice.

To prove **sharpness of the light-stake constant**, let \(0<\varepsilon\le1/12\), choose

\[
p_\varepsilon=\frac14+\varepsilon,\qquad
(w_1,w_2,w_3,w_4,w_5)
=\left(\varepsilon,\frac{1-\varepsilon}{4},\frac{1-\varepsilon}{4},\frac{1-\varepsilon}{4},\frac{1-\varepsilon}{4}\right).
\]

Every weight is strictly smaller than \(p_\varepsilon\). One large weight together with the small weight has total \((1+3\varepsilon)/4<p_\varepsilon\), while any two of the four large weights total \((1-\varepsilon)/2\ge p_\varepsilon\). Thus \(X\ge p_\varepsilon\) holds **exactly when at least two of the four large-weight Bernoulli variables equal one**. Therefore

\[
\Pr(X\ge p_\varepsilon)-p_\varepsilon
=\Pr(\operatorname{Bin}(4,p_\varepsilon)\ge2)-p_\varepsilon
\longrightarrow\frac{67}{256}-\frac14=\frac3{256}
\quad(\varepsilon\downarrow0).
\]

The strict bound already proved shows that this infimum is not attained. Finally, for any fixed \(0<p\le1/3\), selecting sufficiently small \(\varepsilon>0\) and weights \((1-4\varepsilon,\varepsilon,\varepsilon,\varepsilon,\varepsilon)\) makes the event \(X\ge p\) coincide with \(B_1=1\). This attains the baseline probability \(p\), even with every weight positive. \(\square\)

## Verification

The accompanying standard-library Python program `verify.py` checks the exact identities \(\Pr(\operatorname{Bin}(4,1/4)\ge2)=67/256\), \(\Pr(\operatorname{Bin}(5,1/5)\ge2)=821/3125\), and the polynomial identity in (3), all with rational arithmetic. It also enumerates **103746** rational five-weight/parameter combinations, of which **1865** have \(\max_i w_i<p\), and verifies the inequalities, pair counts, and triple counts. Exact rational checks of the extremizing family confirm the event characterization for several positive parameters. Reproduce with `python3 verify.py` from the extracted package directory. These finite checks supplement, and do not replace, the analytical proof for the full continuum of weights and probabilities.

## Relationship to prior work

Milojević and Sudakov (2026) conjectured \(\Pr(X\ge\mathbb EX)\ge p\) for arbitrary numbers of positive weights and \(p\le1/3\). They proved it for a very small uniform range of \(p\) and recalled the earlier results at reciprocal integers. The present theorem handles **all \(p\in[0,1/3]\) for at most five weights**, and supplies an additional exact, sharp stability gap when no weight alone reaches the threshold; it does not address six or more weights.

Fokkink, Meester and Pelekis (2020) optimized the *upper* probability \(\Pr(\sum w_iB_i\ge t)\) over weights in selected parameter regions; that is a different extremal direction. Ling's solution (2026) of Samuels' conjecture determines an extremal probability for sums **above their mean threshold**, involving \(\lambda>\sum\mathbb E X_i\), and gives an upper-tail supremum, not the present lower bound at the mean. The later exposition of Feige's inequality by Milojević and Sudakov (2026) likewise concerns a threshold strictly above the expectation. These results motivate comparison but do not state the five-weight gap established here.

## Limitations

No inference is claimed for six or more nonzero weights, nonidentical Bernoulli parameters, dependent bits, or comparison thresholds different from the common mean. The constant \(3/256\) is sharp only as a **uniform light-stake gap over the indicated range**; it is not an exact weight-specific minimum at each fixed \(p\). Sharpness is obtained by a limiting family of strictly positive weights and is not an attained light-stake equality. The full unrestricted conjecture remains outside the scope of this theorem. The literature comparison is extensive but cannot exclude all unindexed or earlier equivalent statements; independent priority examination has not been performed.

## References

1. A. Milojević and B. Sudakov, *On the Probability a Weighted Bernoulli Sum Exceeds Its Mean*, arXiv:2606.30287v1 (first submitted 2026-06-29), https://arxiv.org/abs/2606.30287.
2. R. Fokkink, L. Meester and C. Pelekis, *Optimizing Stakes in Simultaneous Bets*, arXiv:2002.06804 (2020), https://arxiv.org/abs/2002.06804.
3. Z. Ling, *On Samuels' Conjecture*, arXiv:2608.18392 (2026), https://arxiv.org/abs/2608.18392.
4. A. Milojević and B. Sudakov, *Perfect Matchings in Hypergraphs and Feige's Inequality*, arXiv:2610.10380 (2026), https://arxiv.org/abs/2610.10380.
5. N. Alon, Y. Emek, M. Feldman and M. Tennenholtz, *Adversarial Leakage in Games*, SIAM J. Discrete Math. 27 (2013), 363–385, DOI:10.1137/110858021. The reciprocal-parameter inequality is cited through Reference 1.
6. A. Fernandez, *Convex Combinations of Low Probability Bernoulli Variables*, Mathematics Stack Exchange question 265163 (2012), https://math.stackexchange.com/questions/265163/convex-combinations-of-low-probability-bernoulli-variables.
