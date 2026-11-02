# Positive association of lucky cars and preference richness in random parking functions

## Finding

Choose uniformly from all classical parking functions of length \(n\), with \(n\ge2\). Write \(L_i\) for the indicator that car \(i\) parks in its first-choice place, \(L=\sum_{i=1}^{n}L_i\), and \(M\) for the number of distinct first-choice places in the preference list. For **every pair of strictly increasing real functions** \(f,g\) on \(\{1,\ldots,n\}\),

\[
\operatorname{Cov}(f(L),g(M))>0.
\]

This is a positive-association assertion for the full distributions, not just an assertion about two first moments. In addition, let \(N=n+1\) and \(q=n/N\). Each car has the exact covariance profile

\[
\operatorname{Cov}(L_i,M)=\frac{N-i+1}{N}\,(1-q^{i-1})q^{n-i},\quad 1\le i\le n.
\]

Hence the first car has zero covariance, all later cars have strictly positive covariance, and the aggregate has the closed form

\[
\boxed{\operatorname{Cov}(L,M)=n+2-\frac{5n+7}{2}\left(\frac{n}{n+1}\right)^n.}
\]

In particular,

\[
\frac{\operatorname{Cov}(L,M)}n\longrightarrow1-\frac5{2e},\qquad
\operatorname{Corr}(L,M)\longrightarrow
\frac{1-5/(2e)}{\sqrt{(e^{-1}-2e^{-2})/6}}
\approx0.6308785600.
\]

The location of the largest individual-car covariance is asymptotically nonuniform: if \(i_n\) maximizes \(\operatorname{Cov}(L_i,M)\), then \(i_n/n\longrightarrow W(1)\approx0.56714329\), where \(W(1)e^{W(1)}=1\).

## Assumptions and scope

A classical parking function is a vector \((a_1,\ldots,a_n)\in\{1,\ldots,n\}^n\) for which all cars can park, in arrival order, each taking the first unoccupied space at or after its requested space. The probability measure is uniform over the \((n+1)^{n-1}\) successful vectors. A car is *lucky* if its eventual parking space equals its preference; *preference richness* is the number of distinct values among its first-choice places. No assumption of exchangeability in the arrival order is made. In the expressions above, \(f,g\) need only be strictly increasing on the finite support. The quantitative results also hold for \(n=1\) where defined, except that the strict covariance is then zero.

## Proof

**1. Uniform circular representation and exact joint transitions.** Place \(n\) cars at \(N=n+1\) cyclic spots; independently choose each preferred spot uniformly from \(\{1,\ldots,N\}\). Every sequence leaves precisely one spot vacant. Rotate the labels to put the vacant spot at \(N\). This is a \(N\)-to-one map onto classical parking functions (one circular shift for each vacant-spot label), and the rotation preserves both the lucky-car indicators and the number of distinct preferred spots. Thus circular i.i.d. preferences exactly represent their joint law under uniform classical parking functions.

Let \(M_i\) denote the number of distinct preferences among the first \(i\) cars, with \(M_0=0\). After \(i-1\) arrivals, exactly \(i-1\) spots are occupied, and **every previously requested spot is occupied**. Among the occupied spots, \(M_{i-1}=m\) were requested before and \(i-1-m\) never were. There are \(N-i+1\) vacant spots. Conditional on the complete past (and hence also on \(M_{i-1}=m\)), the only possible triples \((L_i,M_i-M_{i-1},\text{probability})\) are

\[
\begin{array}{c|c|c}
L_i& M_i-M_{i-1}&\Pr\\ \hline
1&1&(N-i+1)/N\\
0&1&(i-1-m)/N\\
0&0&m/N.
\end{array}
\]

All coefficients are nonnegative on reachable states and sum to one. Consequently the joint generating polynomials \(F_i(u,v)=\mathbb E[u^{\sum_{j\le i}L_j}v^{M_i}]\) obey the complete recursion

\[
F_0(u,v)=1,\qquad
F_i(u,v)=\frac{(N-i+1)uv+(i-1)v}{N}F_{i-1}(u,v)
+\frac{v(1-v)}N\frac{\partial F_{i-1}}{\partial v}(u,v).
\]

The first transition probability, \(p_i=(N-i+1)/N\), does not depend on the past. Therefore \(L_1,\ldots,L_n\) are **independent**, with \(L_1=1\) and \(L_i\sim\operatorname{Bernoulli}(p_i)\).

**2. Strict increasing-transform association.** Fix any complete lucky vector \(\ell\), with \(\ell_1=1\). When \(\ell_i=1\), the richness transition is deterministically \(m\mapsto m+1\). When \(\ell_i=0\) and \(i\ge2\), conditional on preceding richness \(m\), the transition is \(m\mapsto m+1\) with probability \((i-1-m)/(i-1)\), and otherwise \(m\mapsto m\). This kernel is stochastically nondecreasing in \(m\); replacing \(\ell_i=0\) by \(\ell_i=1\) also increases its output in stochastic order. An inductive monotone coupling proves that \(H_g(\ell)=\mathbb E[g(M)\mid(L_1,\ldots,L_n)=\ell]\) is nondecreasing in every coordinate whenever \(g\) is nondecreasing.

For strictly increasing \(g\), this increase is strict in the **last** lucky coordinate: if that coordinate is unlucky, its conditional richness increment is zero with probability \(m/(n-1)>0\) (the preceding richness \(m\ge1\)); if lucky, its increment is one. The independent Bernoulli vector \((L_2,\ldots,L_n)\) is associated (the elementary product-measure covariance inequality). For strictly increasing \(f\), the function \(\ell\mapsto f(\sum\ell_i)\) is strictly increasing in its last coordinate. Using the conditional-covariance decomposition, product association gives a nonnegative contribution from other coordinates, and the last coordinate gives a strictly positive one. Hence \(\operatorname{Cov}(f(L),g(M))>0\) for all \(n\ge2\).

**3. The exact local and aggregate covariance.** Set \(q=1-1/N\). In the circular model, \(\mathbb E[M_i]=N(1-q^i)\). Since a lucky preference must be new, \(L_i=1\) forces \(M_i=M_{i-1}+1\). Furthermore, \(L_i\) is independent of the past. Hence

\[
\operatorname{Cov}(L_i,M_i)=p_i(1-q^{i-1}).
\]

After time \(i\), each unseen preference value appears in the remaining \(n-i\) draws with probability \(1-q^{n-i}\), giving

\[
\mathbb E[M\mid\mathcal F_i]=N(1-q^{n-i})+q^{n-i}M_i.
\]

Since future choices are independent of \(L_i\), the tower property gives \(\operatorname{Cov}(L_i,M)=p_i(1-q^{i-1})q^{n-i}\). Summing over all cars and simplifying the two geometric sums produces the boxed aggregate formula. Its strict positivity also follows directly because the \(i\ge2\) summands are positive.

**4. Asymptotics and maximal-influence location.** Standard occupancy calculations from the circular representation give

\[
\operatorname{Var}(L)=\frac{n(n-1)(n+4)}{6(n+1)^2},
\]

\[
\operatorname{Var}(M)=Nq^n(1-q^n)+N(N-1)\left[\left(1-\frac2N\right)^n-q^{2n}\right].
\]

Thus \(\operatorname{Var}(L)/n\to1/6\), \(\operatorname{Var}(M)/n\to e^{-1}-2e^{-2}\), and \(\operatorname{Cov}(L,M)/n\to1-5/(2e)\), which proves the correlation limit. If \(i/n\to t\in[0,1]\), the exact local covariance converges uniformly on the grid to \(\phi(t)=e^{-1}(1-t)(e^t-1)\). Since \(\phi'(t)=e^{-1}(1-te^t)\), its unique maximizer solves \(te^t=1\), establishing the claimed limit for **every** maximizing sequence \(i_n\).

## Verification

The accompanying standalone Python script `verify.py` uses only the standard library. It exhaustively enumerates all classical parking functions for \(1\le n\le7\), compares their complete bivariate count table with the independent circular-state recurrence, checks the moments and each individual lucky-car covariance in exact rational arithmetic, checks the conditional richness laws for every feasible lucky pattern and their stochastic ordering, and checks multiple increasing-transform covariances. It also checks the asymptotic coefficients numerically for large values of \(n\). Running `python3 verify.py` returned **PASS: 3048 assertions; enumerated 280392 parking functions**. These finite checks corroborate but do **not** replace the preceding general proof.

## Relationship to prior work

Gessel and Seo (2005) proved the marginal lucky-car enumerator using a product formula. Shin (2008) developed a parking-function/forest correspondence recording lucky cars. Diaconis and Hicks (2016) analyzed the individual distribution of lucky cars and the marginal distribution of the number of distinct preferences in random parking functions. Butler and collaborators (2024) and Harris and Martinez (2024) investigated refined lucky-car/lucky-spot laws. The **marginals** do not determine a joint distribution or an increasing-transform covariance law; the present claim is the joint richness/luck Markov transition, its strict association, its individual-car covariance profile, and its correlation limit, **not** rederivation of known marginal enumerators.

## Limitations

This result concerns only the uniform classical parking-function model with \(n\) cars and \(n\) linear spaces. It does not establish positive association between arbitrary subsets of favorite-value occupancy indicators, a multivariate central limit theorem, or the result under nonuniform preferences. Independent mathematical auditing and exhaustive historical-priority certification have not been performed. Older multivariate parking-function enumerations could implicitly contain a reformulation of some of these results.

## References

1. I. M. Gessel and S. Seo, *A refinement of Cayley's formula for trees*, arXiv:math/0507497, posted 2005-07-24, especially Section 10. https://arxiv.org/abs/math/0507497
2. H. Shin, *A New Bijection Between Forests and Parking Functions*, arXiv:0810.0427, posted 2008-10-02. https://arxiv.org/abs/0810.0427
3. P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821, posted 2016-11-29, especially Sections 3 and 4. https://arxiv.org/abs/1611.09821
4. S. Butler, K. Hadaway, V. Lenius, P. Martens and M. Moats, *Lucky cars and lucky spots in parking functions*, arXiv:2412.07873, posted 2024-12-10. https://arxiv.org/abs/2412.07873
5. P. E. Harris and J. C. Martinez, *Parking functions with a fixed set of lucky cars*, arXiv:2410.08057, posted 2024-10-10. https://arxiv.org/abs/2410.08057
6. FindStat statistic St000135, *Number of lucky cars of a parking function* (known marginal enumeration). https://www.findstat.org/StatisticsDatabase/St000135/
