# Sharp non-dominant mean-exceedance envelopes for six Bernoulli stakes

## Finding
Let \(B_1,\ldots,B_6\) be independent identically distributed Bernoulli\((p)\) variables, let \(w_i>0\), and suppose \(\sum_{i=1}^6w_i=1\). For every \(0<p\le 1/3\),
\[
\Pr\!\left(\sum_{i=1}^{6}w_i B_i\ge p\right)\ge p.
\]
This inequality is sharp over all positive weight vectors. Furthermore, among all **non-dominant** vectors satisfying \(\max_iw_i<p\), the class is nonempty precisely when \(p>1/6\), and the **attained exact minimum** is
\[
L(p)=\begin{cases}
\Pr(\operatorname{Bin}(6,p)\ge2),&1/6<p\le1/5,\\
\Pr(\operatorname{Bin}(5,p)\ge2),&1/5<p\le1/4,\\
\Pr(\operatorname{Bin}(4,p)\ge2),&1/4<p\le1/3.
\end{cases}
\]
In each interval \(L(p)>p\); consequently any equality case in the global inequality must have a weight at least \(p\). The interval endpoints are important: the new lower-tail branch begins **strictly above** its left endpoint.

## Assumptions and scope
All six trials have the *same* success probability \(p\), are independent, and all six weights are strictly positive and sum to one. The probability threshold is exactly the mean \(\mathbb E\sum_iw_i B_i=p\). The sharp subclass requires every individual weight strictly below the threshold. A vector with at least one weight \(\ge p\) is called dominant. The result does not concern general independent non-identically distributed trials, or a different threshold.

Write \(T_r(p)=\Pr(\operatorname{Bin}(r,p)\ge2)=1-(1-p)^r-rp(1-p)^{r-1}\). For a non-dominant weight vector, let \(N_k\) denote the number of \(k\)-subsets \(S\subseteq\{1,\ldots,6\}\) satisfying \(\sum_{i\in S}w_i\ge p\). Because every singleton fails and every subset of cardinality at least four succeeds (proved below),
\[
\Pr\!\left(\sum_iw_i B_i\ge p\right)=
N_2p^2(1-p)^4+N_3p^3(1-p)^3+\Pr(\operatorname{Bin}(6,p)\ge4).
\tag{1}
\]

## Proof
**1. Trivial and forced subsets.** If some \(w_i\ge p\), the event \(B_i=1\), of probability \(p\), ensures the target event. Hence the global lower bound is immediate in the dominant class. Suppose henceforth \(w_i<p\) for all \(i\). The inequality \(1=\sum_i w_i<6p\) forces \(p>1/6\). Every singleton fails. If a selected set has four or more indices, its complement has at most two, so its weight is greater than \(1-2p\ge p\), because \(p\le1/3\). This proves (1).

**2. Six-core phase: \(1/6<p\le1/5\).** A failed pair would have weight below \(p\), while its four remaining individual weights are each below \(p\); consequently \(1<5p\le1\), impossible. Every pair and therefore every triple succeeds. Thus \(N_2=15\), \(N_3=20\), and (1) equals \(T_6(p)\). All equal weights \(w_i=1/6\) attain this law.

**3. Five-core phase: \(1/5<p\le1/4\).** A failed triple together with its three remaining individual weights would have total less than \(4p\le1\), impossible; hence \(N_3=20\). Two *disjoint* failed pairs would have total weight less than \(2p\), while the two remaining singleton weights total less than \(2p\), again contradicting \(1=\sum_iw_i\) because \(4p\le1\). Thus the graph of failed pairs is intersecting. A pairwise-intersecting edge family on six vertices has at most five edges: if all edges share a vertex it has at most five, while otherwise any triangle contains all edges and gives at most three. Hence at least ten pairs succeed. Equation (1) yields
\[
\Pr\!\left(\sum_i w_iB_i\ge p\right)\ge
10p^2(1-p)^4+20p^3(1-p)^3+\Pr(\operatorname{Bin}(6,p)\ge4)=T_5(p).
\]
To attain the bound take \(w_1=\cdots=w_5=(1-\varepsilon)/5\), \(w_6=\varepsilon\), for \(\varepsilon>0\) small enough that \((1+4\varepsilon)/5<p\). Each heavy pair succeeds, and no heavy singleton with the sixth weight succeeds; therefore the target event occurs if and only if at least two of the first five trials succeed.

**4. Four-core phase: \(1/4<p\le1/3\).** Three pairwise-disjoint failed pairs would have total weight below \(3p\le1\), so every perfect matching of the complete graph on the six indices contains a successful pair. There are fifteen perfect matchings, and each edge belongs to exactly three. Counting incidences therefore gives \(3N_2\ge15\), or \(N_2\ge5\). If \(N_2=5\), each perfect matching contains exactly one successful pair. No two successful pairs can then be disjoint: any two disjoint edges extend to a perfect matching. Thus five successful edges form a star, centered at an index \(c\).

Any two distinct failed triples must have at least two indices in common. Indeed, disjoint failed triples would sum to less than \(2p\le1\); if the triples share exactly one index, their union has five elements whose weight is below \(2p\), and the sixth weight is below \(p\). Their total is then strictly below \(3p\le1\). A family of three-subsets of a six-element set having pairwise intersections of size at least two contains at most four triples. To see this, fix distinct triples \(\{a,b,c\}\) and \(\{a,b,d\}\). Every other triple either contains \(\{a,b\}\), of which there are four possibilities in total, or is one of \(\{a,c,d\}\) and \(\{b,c,d\}\). Once either exceptional triple occurs, no triple \(\{a,b,e\}\) with \(e\notin\{c,d\}\) can occur. Hence at most four triples fail, so \(N_3\ge16\).

If \(N_2\ge6\), equation (1) and the identity
\[
6p^2(1-p)^4+16p^3(1-p)^3+\Pr(\operatorname{Bin}(6,p)\ge4)=T_4(p)
\]
give the claimed bound. If \(N_2=5\), the successful-pair star forces all triples containing \(c\) to succeed. A failed triple avoiding \(c\) is impossible: the remaining two indices other than \(c\) form a failed pair (the only successful pairs include \(c\)), and \(w_c<p\); these three disjoint pieces would sum to less than \(3p\le1\). Thus \(N_3=20\) when \(N_2=5\). Its probability exceeds the preceding \(T_4(p)\) baseline by exactly
\[
p^2(1-p)^3(5p-1)>0.
\]
The \(T_4(p)\) bound holds in both cases. For attainment put \(w_1=\cdots=w_4=(1-2\varepsilon)/4\) and \(w_5=w_6=\varepsilon\), choosing \(\varepsilon>0\) so small that \((1+6\varepsilon)/4<p\) and \((1-2\varepsilon)/2\ge p\). The event then occurs precisely when at least two of the first four trials succeed, giving \(T_4(p)\).

**5. Strict improvement and global sharpness.** The polynomial identity
\[
T_4(p)-p=p(p-1)(3p^2-5p+1)>0\quad(1/4\le p\le1/3)
\]
holds since the quadratic is negative on this interval. Moreover \(T_5(1/6)-1/6=115/3888>0\), and \(\frac{d}{dp}(T_5(p)-p)=20p(1-p)^3-1>0\) throughout \([1/6,1/3]\), as follows by minimizing \(p(1-p)^3\) at the two endpoints of this interval. Since \(T_6(p)\ge T_5(p)\), every non-dominant phase satisfies \(L(p)>p\). Finally, for any \(p>0\) choose \(w_1=1-\delta\), \(w_2=\cdots=w_6=\delta/5\) with \(0<\delta<\min\{p,1-p\}\). The sum of the last five weights is less than \(p\) and the first weight is at least \(p\); hence the target event is exactly \(B_1=1\), with probability \(p\). This establishes sharpness of the global bound. \(\square\)

## Verification
The standalone `check.py`, using only the Python standard library and exact rational arithmetic, checks all fifteen perfect matchings and their edge incidences, confirms the maximum cardinality four of a pairwise 2-intersecting triple family, verifies the two binomial-polynomial identities and the positive deficit for the five-successful-pair case, and evaluates six explicit parameter/weight witnesses. It also evaluates a rational test grid. Run `python3 check.py` in a directory containing this file. These finite tests support the independently presented combinatorial proof; a finite grid is not a proof for arbitrary real weights or arbitrary \(p\).

## Relationship to prior work
Milojević and Sudakov, *On the Probability a Weighted Bernoulli Sum Exceeds Its Mean* (arXiv:2606.30287v1, June 2026), formulate the unrestricted-weight, arbitrary-summand bound as Conjecture 1 and establish a connection to the Manickam–Miklós–Singhi nonnegative-subset-sum conjecture. Their theorem yields a very-small-\(p\) range independently of the number of summands, not the six-stake parameter interval or its exact non-dominant envelope. The earlier question by Fernandez (2012) discusses reciprocal integer probabilities and counterexamples above the one-third boundary, but does not give these six-stake extremal branches. Fokkink, Meester and Pelekis, *Optimizing stakes in simultaneous bets* (arXiv:2002.06804v4), instead optimize the **maximum** exceedance probability at a prescribed threshold, which does not determine this **minimum**. The First Proof Second Batch discussion (arXiv:2606.18119v1) records individual rational-parameter partial cases but not these continuous-in-\(p\) exact six-weight minima. The related Samuels problem concerns a substantially larger class of independent nonnegative laws and has no known general six-variable solution; its statements do not imply the present explicit piecewise minimum without further work.

## Limitations
Only six iid Bernoulli trials are treated. The lower-envelope theorem is conditional on **all** weights being strictly smaller than the mean threshold; the unconstrained six-weight minimum is \(p\), attained in the dominant class. The theorem does not classify all minimizing weight vectors, or treat more than six trials, different thresholds, or heterogeneous success probabilities. No inference is made that an unsuccessful literature search proves priority. The exact six-weight proof is analytical; the finite checker supplies reproducibility checks, not infinite certification.

## References
1. A. Milojević and B. Sudakov, *On the Probability a Weighted Bernoulli Sum Exceeds Its Mean*, arXiv:2606.30287v1 (first posted 29 June 2026). https://arxiv.org/html/2606.30287v1
2. R. Fokkink, L. Meester and C. Pelekis, *Optimizing stakes in simultaneous bets*, arXiv:2002.06804v4 (2020); ALEA 20 (2023), 153–165. https://arxiv.org/html/2002.06804v4
3. A. Fernandez, *Convex Combinations of Low Probability Bernoulli Variables*, Mathematics Stack Exchange (26 December 2012). https://math.stackexchange.com/questions/265163/convex-combinations-of-low-probability-bernoulli-variables
4. M. Abouzaid, N. Srivastava, R. Ward and L. Williams, *First Proof Second Batch*, arXiv:2606.18119v1 (16 June 2026), Section 3.3 and associated discussion. https://arxiv.org/html/2606.18119v1
