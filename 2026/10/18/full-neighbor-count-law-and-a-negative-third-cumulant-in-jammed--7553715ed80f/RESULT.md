# Full neighbor-count law and a negative third cumulant in jammed tree adsorption

## Finding

Consider nearest-neighbor-exclusion random sequential adsorption (blocking RSA) on the infinite \(\Delta\)-regular tree, \(\Delta\ge2\): each vertex independently attempts adsorption once at a uniform time in \([0,1]\), succeeding only if none of its neighbors is already occupied. For a fixed vertex \(o\), let \(X_\Delta\) count its occupied neighbors at the final jammed configuration. Define
\[
u_\Delta(t)=\begin{cases}e^{-t},&\Delta=2,\\ (1+(\Delta-2)t)^{-1/(\Delta-2)},&\Delta>2,\end{cases}\qquad a_\Delta=u_\Delta(1).
\]
Then the **complete coordination probability-generating polynomial** is
\[
\Phi_\Delta(z)=\mathbb E[z^{X_\Delta}]
=[a_\Delta+(1-a_\Delta)z]^\Delta
+\int_0^1\{u_\Delta(t)^\Delta-[a_\Delta+(u_\Delta(t)-a_\Delta)z]^\Delta\}\,dt.
\]
For every integer \(1\le k\le\Delta\),
\[
\mathbb P(X_\Delta=k)=\binom\Delta k a_\Delta^{\Delta-k}
\left((1-a_\Delta)^k-\int_0^1[u_\Delta(t)-a_\Delta]^kdt\right),
\qquad \mathbb P(X_\Delta=0)=\frac{1-a_\Delta^2}{2}.
\]
All integrals are elementary (see the proof). In particular, for \(\Delta=3\),
\[
\Phi_3(z)=\frac38+\left(\frac34-\frac34\log2\right)z
+\left(\frac32\log2-\frac34\right)z^2
+\left(\frac58-\frac34\log2\right)z^3.
\]

Write \(Y_i\) for the terminal occupation indicator of the \(i\)-th neighbor of \(o\). For any **three distinct** neighbors (hence \(\Delta\ge3\)), their pair covariance and mixed third cumulant obey the strict *opposite-sign* laws
\[
\operatorname{Cov}(Y_1,Y_2)=\frac{1-a_\Delta^4}{4}+a_\Delta^2\log a_\Delta>0,
\]
\[
\begin{aligned}
\kappa_3(Y_1,Y_2,Y_3)
&=\mathbb E[Y_1Y_2Y_3]-3\mathbb E[Y_1Y_2]\mathbb E[Y_1]+2\mathbb E[Y_1]^3\\
&=-\frac{a_\Delta^2}{4}\left[a_\Delta^4+8a_\Delta-9-6(1+a_\Delta^2)\log a_\Delta\right]<0.
\end{aligned}
\]
Finally, the vacancy of the entire neighbor star is asymptotically more likely than an independent-site approximation even as the marginal density vanishes:
\[
\mathbb P(X_\Delta=0)\sim\frac{\log\Delta}{\Delta},\qquad
\frac{\mathbb P(X_\Delta=0)}{(1-\mathbb E[Y_1])^\Delta}\sim\log\Delta
\qquad(\Delta\to\infty).
\]
The marginal occupation probability and pair covariance have classical antecedents; the asserted new content is their extension to the **complete star law, strict negative three-neighbor cumulant, and logarithmically enhanced empty-star event**.

## Assumptions and scope

The graph is the countably infinite, simple, locally finite, unweighted \(\Delta\)-regular tree. Attempts are independent, one per vertex, uniform on \([0,1]\). This is distributionally identical to ordering the first arrivals of independent rate-one exponential clocks over infinite physical time, by the strictly increasing transformation \(t\mapsto1-e^{-t}\). A successful attempt occupies only its own vertex and permanently excludes its nearest neighbors. All expectations are over the attempt times. The model concerns the jammed infinite-volume random independent set, not equilibrium lattice gases or a finite-depth Cayley-tree limit with a macroscopic boundary. The count \(X_\Delta\) is bounded between zero and \(\Delta\).

The infinite-volume evolution is well defined: any dependency chain affecting one vertex must follow a strictly decreasing sequence of arrival times along a self-avoiding path. The expected number of such paths of length \(h\) is at most \(\Delta(\Delta-1)^{h-1}/(h+1)!\). The sum over \(h\) is finite, so almost surely only a finite causal neighborhood determines a fixed vertex's state.

## Proof

**1. Independent cavity branches.** Remove \(o\), leaving \(\Delta\) independent rooted trees. On any one, let \(U\) denote the time when its root becomes occupied in the isolated-branch adsorption (set \(U=\infty\) if it never does). Write \(u(t)=\mathbb P(U>t)\). For the branch root to become occupied at time \(t\), it must attempt then and all \(\Delta-1\) child-branch roots must still be empty. Their independence gives
\[
u'(t)=-u(t)^{\Delta-1},\qquad u(0)=1.
\]
The unique solution is exactly \(u_\Delta(t)\) in the finding. Each branch root has probability \(a=u(1)\) of never becoming occupied by the final time. The \(\Delta\) cavity occupation times \(U_1,\dots,U_\Delta\) are independent.

**2. Root-time dichotomy and the full law.** Let \(T\) be the independent uniform root attempt time. If \(T<\min_i U_i\), the root succeeds and forces all its neighbors to remain unoccupied, so \(X_\Delta=0\). Otherwise an earlier cavity occupation permanently blocks \(o\); then \(o\) never affects any branch and the final neighbors are exactly \(\mathbf1_{U_i\le1}\). Without intervention their generating polynomial is \([a+(1-a)z]^\Delta\). The intervention occurs with probability density \(u(t)^\Delta\,dt\) at root time \(t\), and on that event the unperturbed joint contribution to the generating polynomial is \([a+(u(t)-a)z]^\Delta\,dt\), because \(\mathbb P(t<U\le1)=u(t)-a\). Replacing it by one gives the asserted formula. Coefficient extraction yields the \(k\ge1\) formula. The root succeeds with probability
\[
\int_0^1u(t)^\Delta dt=\int_a^1s\,ds=\frac{1-a^2}{2},
\]
using \(ds=-s^{\Delta-1}dt\). Since the configuration is maximal, \(X_\Delta=0\) occurs precisely when \(o\) is occupied, proving the \(k=0\) identity. For explicit quadrature-free coefficients, define \(J_j=\int_0^1u(t)^jdt\). Direct substitution gives
\[
J_j=\begin{cases}
(1-a^{j-\Delta+2})/(j-\Delta+2),&j\ne\Delta-2,\\
-\log a,&j=\Delta-2.
\end{cases}
\]
Expanding the integrand in powers of \(u\) expresses all coefficients using these finite elementary terms. Direct integration at \(\Delta=3\), \(a=1/2\), yields the displayed cubic polynomial.

**3. Joint moments and cumulants.** For \(1\le k\le\Delta\) distinct neighbors, the same root-time dichotomy gives
\[
m_k:=\mathbb E\prod_{i=1}^kY_i
=(1-a)^k-\int_0^1(u(t)-a)^ku(t)^{\Delta-k}dt
=(1-a)^k-\int_a^1(s-a)^ks^{1-k}\,ds.
\]
At \(k=1,2,3\), this becomes, exactly,
\[
m_1=(1-a^2)/2,\quad
m_2=(1-a^2)/2+a^2\log a,\quad
m_3=1/2+3a^2/2-2a^3+3a^2\log a.
\]
Substitution into \(m_2-m_1^2\) and \(m_3-3m_2m_1+2m_1^3\) produces the displayed covariance and cumulant.

For the covariance, let \(s=-\log a>0\). Its value is \(e^{-2s}(\sinh(2s)/2-s)>0\) by strict convexity of \(\sinh\) or its positive-power series. For the third cumulant, write
\[
F(a)=a^4+8a-9-6(1+a^2)\log a,
\qquad t=(1-a)/(1+a)\in(0,1).
\]
The strict bound \(-\log a=2\operatorname{artanh}t>2(t+t^3/3)\) implies the exact positive rational lower bound
\[
F(a)>\frac{(1-a)^4(a^3+7a^2+9a+7)}{(1+a)^3}>0
\qquad(0<a<1).
\]
Thus the third cumulant is strictly negative for every \(\Delta\ge3\), even while pair covariances are strictly positive.

**4. Large-degree nonfactorization.** For \(\Delta>2\),
\[
a=(\Delta-1)^{-1/(\Delta-2)}
=\exp\left(-\frac{\log(\Delta-1)}{\Delta-2}\right).
\]
Therefore \(p=m_1=(1-a^2)/2\sim(\log\Delta)/\Delta\) and \(\Delta p=\log\Delta+o(1)\). For \(\Delta\) independent Bernoulli variables of marginal \(p\), the empty-star probability is \((1-p)^\Delta\sim\Delta^{-1}\), whereas the exact empty-star probability is \(p\sim(\log\Delta)/\Delta\). Taking their ratio proves the logarithmic enhancement. It is a relative rare-event effect, not an assertion of nonvanishing covariance at infinite degree.

## Verification

The accompanying `verification.py` recomputes the moment and cumulant identities symbolically, verifies the positivity-bound factorization, independently integrates the degree-three generating polynomial exactly, checks normalization and moments by high-resolution quadrature for degrees \(2,3,4,5,8,16\), and compares against seeded greedy adsorption simulations of finite rooted trees in degrees \(3\) and \(4\). It additionally checks large-degree asymptotic ratios. Run `python verification.py` with the version recorded in `requirements.txt`. The finite-tree simulations concern finite boundary approximations and do **not** prove the infinite-tree theorem; the full proof is analytical above.

## Relationship to prior work

Penrose and Sudbury (2005), Theorems 12–13 and related derivations, already obtain occupation probabilities and pair correlations for blocking RSA on Bethe lattices and prove parity-sensitive positive association. In particular the one-site formula and the pair-covariance positivity are prior results, not stand-alone novelty claims here. Dehling, Fleurke and Külske (2008) independently derive the occupation probability for general iid random-degree trees, recovering the regular case. Their inspected article addresses the marginal density, not the joint full-star law. Classical RSA overviews motivate higher-order jammed morphology. The additional complete neighbor-count distribution, explicit negative distinct-triplet cumulant, and logarithmic high-degree empty-star enhancement are not statements found in the inspected full texts.

Gouet and Sudbury (2008) analyze finite Cayley-tree processes and correlations, which may provide related specialized implications, but the complete paper was not available for full comparison. Sudbury's Bethe-lattice emptiness paper and Fan–Percus's multisite-correlation article likewise warrant continued bibliographic checking. The derivation above stands independently of any novelty claim and does not purport to rule out all equivalent older formulations.

## Limitations

The exact formulas require a regular infinite tree and one independent single-site attempt per vertex. They do not extend without new analysis to cycles, variable coordination, equilibrium hard-core gases, adsorbing dimers, or correlated arrival clocks. The negative third cumulant concerns *distinct neighbors of the same center*, not arbitrary triples of graph vertices. The ratio asymptotic is a large-degree statement, not a nonzero limiting correlation. Some older primary literature could not be fully inspected; originality remains subject to independent bibliographic review. No independent scientific audit has been performed.

## References

1. M. D. Penrose and A. Sudbury, "Exact and approximate results for deposition and annihilation processes on graphs," *Annals of Applied Probability* **15** (2005), 853–889; arXiv:math/0503519v1 (first public 2005-03-24), https://arxiv.org/abs/math/0503519.
2. H. G. Dehling, S. R. Fleurke and C. Külske, "Parking on a random tree," *Journal of Statistical Physics* **133** (2008), 151–157; arXiv:0711.4061, https://arxiv.org/abs/0711.4061.
3. R. Gouet and A. Sudbury, "Blocking and dimer processes on the Cayley tree," *Journal of Statistical Physics* **130** (2008), 935–955, doi:10.1007/s10955-007-9451-5.
4. A. Sudbury, "Emptiness probabilities in random sequential adsorption on the Bethe lattice," *Modern Physics Letters B* (2008), doi:10.1142/S0217984908017485.
5. J. C. Fan and J. K. Percus, "Asymptotic coverage in random sequential adsorption on a lattice," *Physical Review A* **44** (1991), 5099, doi:10.1103/PhysRevA.44.5099.
6. A. Cadilhe, N. A. M. Araújo and V. Privman, "Random sequential adsorption: from continuum to lattice and pre-patterned substrates," arXiv:cond-mat/0611413v1 (2006), https://arxiv.org/abs/cond-mat/0611413.
