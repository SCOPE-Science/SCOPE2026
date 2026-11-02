# A conditional-dependence path for consecutive rank comparisons

## Finding

**Theorem (exact conditional-dependence criterion).** Fix any integer \(n\ge3\). Let \(X_1,\ldots,X_n\) be independent, not necessarily identically distributed real random variables possessing probability densities, each strictly positive on the same nonempty open interval \(I\). For \(1\le k<n\), put
\[
D_k=\mathbf 1\{X_k>X_{k+1}\}.
\]
Select distinct indices \(1\le i<j<n\) and any set of observed indices \(S\subseteq\{1,\ldots,n-1\}\setminus\{i,j\}\). For every prescribed binary observation \(D_k=\varepsilon_k\) on \(S\), denoting that event by \(E\), the conditional covariance has the **complete sign classification**
\[
\operatorname{Cov}(D_i,D_j\mid E)
\begin{cases}
<0,&\{i+1,\ldots,j-1\}\subseteq S,\\
=0,&\{i+1,\ldots,j-1\}\not\subseteq S.
\end{cases}
\]
All such conditioning events have positive probability. In the equality case the two indicators are in fact conditionally independent. Thus, after conditioning on any subcollection of adjacent comparison bits, the remaining bits in increasing index order form a one-dependent process with **strictly negative pairwise covariance between its consecutive positions** and independence for nonconsecutive positions.

In particular, the result holds for the descent indicators of a uniformly random permutation. For \(n=4\), the first and third descents are independent without conditioning but have covariance \(-1/36\) conditional on either value of the middle descent.

## Assumptions and scope

The observations are independent and have Lebesgue densities \(p_k\), which need not be equal. There is a common nonempty open interval \(I\) on which each density can be chosen strictly positive almost everywhere; an everywhere-positive version may be used without loss for the arguments below. Ties have probability zero. The observation \(E\) consists solely of exact values of comparison bits distinct from \(i,j\), not arbitrary information about the underlying values. The empty interior index set in the adjacent case \(j=i+1\) is understood to be contained in \(S\).

## Proof

**1. Factor the observed constraints.** Set
\[
L=(X_1,\ldots,X_i),\quad
M=(X_{i+1},\ldots,X_j),\quad
R=(X_{j+1},\ldots,X_n).
\]
Since neither \(D_i\) nor \(D_j\) is observed, \(E=E_L\cap E_M\cap E_R\) is an intersection of conditions on these three disjoint independent blocks. They remain independent after conditioning on \(E\). Every finite up/down pattern is feasible with positive probability by selecting distinct ordered values in the common open interval \(I\).

Define
\[
f(t)=\Pr(X_i>t\mid E_L),\qquad
g(s)=\Pr(X_{j+1}<s\mid E_R).
\]
The conditional distributions of \(X_i\) and \(X_{j+1}\) have strictly positive densities on \(I\): choose all their block companions near distinct values in \(I\) satisfying the finite set of prescribed strict inequalities. Consequently \(f\) is nonincreasing and strictly decreasing on \(I\), while \(g\) is nondecreasing and strictly increasing on \(I\). With \(T=X_{i+1}\) and \(U=X_j\), conditional independence of the outer blocks yields
\[
\operatorname{Cov}(D_i,D_j\mid E)
=\operatorname{Cov}(f(T),g(U)\mid E_M).
\]

**2. An unobserved interior comparison gives independence.** If some \(k\) with \(i<k<j\) is absent from \(S\), the middle constraints split at the unconstrained comparison \(k\) into restrictions on disjoint underlying variable sets \((X_{i+1},\ldots,X_k)\) and \((X_{k+1},\ldots,X_j)\). These sets remain independent under \(E_M\), so \(T\) and \(U\) are conditionally independent. Moreover the entire collections of comparisons located strictly on opposite sides of that unconstrained edge are independent given the observed constraints. This proves the zero and independence assertions.

**3. Total positivity when every interior comparison is observed.** Let \(j\ge i+2\) and suppose all intermediate edges are in \(S\). For each middle edge define the order kernel
\[
K_k(x,y)=\begin{cases}
\mathbf 1\{x>y\},&\varepsilon_k=1,\\
\mathbf 1\{x<y\},&\varepsilon_k=0.
\end{cases}
\]
For ascending ordered pairs \(x_1<x_2\), \(y_1<y_2\), either kernel satisfies
\[
K_k(x_1,y_1)K_k(x_2,y_2)-K_k(x_1,y_2)K_k(x_2,y_1)\ge0.
\]
Multiplying a kernel by any nonnegative one-variable density preserves this total positivity of order two (TP2). Integrating a product of consecutive TP2 kernels preserves TP2 by the two-row continuous Cauchy--Binet identity: the determinant of a composed kernel is the integral, over \(z_1<z_2\), of the product of the determinants of its two factors. Hence the conditional joint density \(h(t,s)\) of \((T,U)\) under \(E_M\) satisfies
\[
h(t_1,s_1)h(t_2,s_2)-h(t_1,s_2)h(t_2,s_1)\ge0
\quad(t_1<t_2,\ s_1<s_2).
\]
This remains valid with arbitrary different middle densities.

**4. Strictness.** The preceding determinant is strictly positive on a positive-measure set with all endpoints inside \(I\). To see this, choose one small step \(\delta>0\), two copies \(c_k-\delta,c_k+\delta\) of each successive middle variable, and choose consecutive centers \(c_{k+1}=c_k+\delta\) for an observed ascent and \(c_{k+1}=c_k-\delta\) for an observed descent. Because the path is finite, all these values can be kept in \(I\). Each adjacent order-kernel determinant is then exactly one, and small perturbations retain the inequalities. The density factors are positive there, so repeated Cauchy--Binet integration makes the endpoint determinant positive for a positive-measure set of pairs \(t_1<t_2,s_1<s_2\) in \(I\).

For any TP2 density \(h\), direct symmetrization gives
\[
\operatorname{Cov}(f(T),g(U))
=\int_{t_1<t_2}\!\int_{s_1<s_2}
(f(t_1)-f(t_2))(g(s_1)-g(s_2))
\big[h(t_1,s_1)h(t_2,s_2)-h(t_1,s_2)h(t_2,s_1)\big]
\,ds_1\,ds_2\,dt_1\,dt_2.
\]
The first difference is strictly positive and the second strictly negative when the endpoints lie in \(I\); the density determinant is everywhere nonnegative and positive on a positive-measure subset of that region. Hence the covariance is strictly negative.

**5. The adjacent case.** If \(j=i+1\), then \(T=U=X_{i+1}\). The covariance of strictly oppositely monotone functions \(f(T),g(T)\) is strictly negative by the same two-independent-copies covariance identity; the conditional distribution of \(T\) has positive density on \(I\). The theorem follows.

For the uniform-permutation specialization, every full descent pattern has positive probability. The full-conditioning inequalities at each coordinate pair imply the negative lattice condition (log-submodularity) of its descent-set probability mass function by successively applying the elementary Boolean-lattice square inequalities. This last consequence should not be confused with the stronger real-stability property of the multiaffine generating polynomial.

## Verification

Run `python verify_conditional_comparisons.py` with Python 3 and only its standard library. It enumerates every permutation of lengths \(3\) through \(10\), forms exact descent-mask counts and tests **all** pairs of unobserved positions, every subset of other positions and every binary pattern on that subset. It checks that the exact contingency determinant is negative precisely when all intervening positions are conditioned, and otherwise zero. The program reports \(105796\) conditional sign checks, split into \(55152\) strict negatives and \(50644\) exact zeros; it also checks a six-assertion non-real-stability diagnostic.

At length \(5\), the descent-set multiaffine generating polynomial \(F\) evaluated at \((-3,-3,2,-3)\) has
\[
(F,\partial_2F,\partial_4F,\partial_2\partial_4F)=(76,16,-44,-9),
\qquad
(\partial_2F)(\partial_4F)-F\partial_2\partial_4F=-20.
\]
Thus the polynomial fails the necessary real-stability Rayleigh inequality. The proof above does not rely on real stability or a Hermitian determinantal representation. Finite checks corroborate the full analytical proof; they are not presented as proving the infinite-size statement.

## Relationship to prior work

Borodin, Diaconis and Fulman (2009), notably their Proposition 5.2 and Theorem 7.1, establish one-dependence and determinantal representations for (in particular) descents in random permutations. Unconditional one-dependence does not establish strict conditional anticorrelation after an arbitrary pattern of other descents has been fixed, nor the necessity-and-sufficiency condition on the intervening observed sites. Their determinantal kernel is not the Hermitian contraction hypothesis underlying general negative-association results for strongly Rayleigh measures.

Borcea, Brändén and Liggett (2008) prove conditional negative-association properties for strongly Rayleigh measures. The length-five explicit negative Rayleigh polynomial evaluation above shows that their stability hypothesis fails for the ordinary descent-set law, so that theorem is not a covering implication. Kahn and Neiman (2010) treat conditional negative association for competing-urn occupancy indicators and a graph-orientation counting inequality; these are different variables and hypotheses. Crane, DeSalvo and Elizalde (2016) exploit weak dissociation for consecutive permutation patterns under Mallows weights, not the complete exact conditional sign classification for potentially heterogeneous independent observations.

No claim is made to originate TP2 composition, the classical descent-set enumeration, the one-dependent marginal law, or negative-association theory. The particular all-conditioning criterion and its strictness for independent heterogeneous observations constitute the assessed result.

## Limitations

The statements are restricted to independent absolutely continuous underlying variables with a common interval of positive densities and to conditioning on adjacent comparison bits. They do not assert negative association of arbitrary increasing functions of the entire descent vector, nor an analogous result for Mallows-dependent underlying coordinates, discrete tied observations, or arbitrary permutation statistics. The historical literature search is not a proof of worldwide priority; analogous statements might be implicit in earlier total-positivity or permutation-distribution literature. Independent audit has not been performed.

## References

1. A. Borodin, P. Diaconis and J. Fulman, *On adding a list of numbers (and other one-dependent determinantal processes)*, arXiv:0904.3740v1, first public 23 April 2009, https://arxiv.org/abs/0904.3740.
2. J. Borcea, P. Brändén and T. M. Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340, https://arxiv.org/abs/0707.2340.
3. J. Kahn and M. Neiman, *Conditional negative association for competing urns*, arXiv:1001.0610v1, first public 5 January 2010, https://arxiv.org/abs/1001.0610.
4. H. Crane, S. DeSalvo and S. Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, arXiv:1609.01370v1, first public 6 September 2016, https://arxiv.org/abs/1609.01370.
