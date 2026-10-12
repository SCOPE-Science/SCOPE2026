# Polygon-imbalance law for optimal spectral gaps of arbitrarily priced stars

## Finding

**Theorem (full positive-price star classification).** Consider a star with a hub and \(m\ge2\) leaves, with a freely chosen nonnegative symmetric transition rate \(w_i\) on the edge to leaf \(i\). Every unit of rate on that edge costs \(c_i>0\), with one shared budget \(\sum_{i=1}^{m}c_iw_i=1\). Let \(L(w)\) be the combinatorial weighted Laplacian and write its eigenvalues in nondecreasing order, so \(\lambda_2(L(w))\) is the algebraic connectivity.

Set
\[
 n=m+1,\quad d_i=\sqrt{c_i},\quad S=\sum_{i=1}^mc_i,\quad
 \delta=\left(2\max_i d_i-\sum_{i=1}^m d_i\right)_+,
 \qquad \Lambda=\frac{1}{S-\delta^2/n}.
\]
Here \((z)_+=\max\{z,0\}\). For **every** \(m\ge2\) and **every** positive real price vector,
\[
 \boxed{\max_{w_i\ge0,\ \sum c_iw_i=1}\lambda_2(L(w))=\Lambda.}
\]
The maximizer is **unique** and all optimal edge rates are strictly positive. They have the following complete classification.

If \(\delta=0\), equivalently \(2\max_i\sqrt{c_i}\le\sum_i\sqrt{c_i}\), the unique optimal rates are \(w_i^*=1/S\) for every leaf, despite possibly unequal prices. The spectral gap has multiplicity \(m-1\).

If \(\delta>0\), exactly one index \(j\) has the largest \(d_j\), and the unique optimal rates are
\[
 \boxed{w_j^*=\Lambda\left(1-\frac{\delta}{nd_j}\right),\qquad
 w_i^*=\Lambda\left(1+\frac{\delta}{nd_i}\right)\quad(i\ne j).}
\]
In this regime the spectral gap is simple. Its eigenvector has hub coordinate zero before centering and leaf differences \(d_j\) at \(j\), and \(-d_i\) at every other leaf. The rule is invariant under simultaneous rescaling of all prices, with the optimal gap rescaled inversely.

For instance, the distinct prices \((16,9,4)\) satisfy the geometric triangle inequality for their square roots, so all three optimal rates are \(1/29\). For prices \((25,4,1)\), the imbalance is \(\delta=2\), and the unique optimum has gap \(1/29\), with leaf rates \((9/290,5/116,3/58)\); the uniform-rate choice gives only \(1/30\).

## Assumptions and scope

The Laplacian has entries \(L_{00}=\sum_i w_i\), \(L_{0i}=L_{i0}=-w_i\), \(L_{ii}=w_i\), with zero entries between distinct leaves. Eigenvalues use the **combinatorial**, not normalized, Laplacian. Thus the symmetric continuous-time generator is \(-L\), whose equilibrium is uniform on all \(n\) vertices. There are no additional edge-rate caps or restrictions beyond nonnegativity and the stated positive linear budget. The theorem includes the degenerate polygon boundary and the two-leaf star. When \(m=2\), the gap is always simple, even at the boundary; when \(m\ge3\), the multiplicity drops from \(m-1\) to one on entering the strict-imbalance regime.

## Proof

Write \(P=I-\mathbf1\mathbf1^{\mathsf T}/n\). For every vector \(y\), the spectral variational principle gives \(y^{\mathsf T}L(w)y\ge\lambda_2(L(w))\,y^{\mathsf T}Py\). The same inequality summed over vector-valued configurations is valid column by column.

**1. A uniform sharp upper bound.** Select vectors \(u_1,\ldots,u_m\in\mathbb R^2\) of respective lengths \(d_i\), placing the hub at \(u_0=0\), so that \(\|\sum_i u_i\|=\delta\). Such a configuration exists by the elementary polygon-closing criterion: the given segments close exactly if the largest does not exceed the sum of the rest, and otherwise the minimal resultant is the excess of the largest over the rest, attained collinearly. This statement remains valid for two segments. Their total squared centered norm is
\[
 Q=\sum_{i=0}^m\|u_i-\overline u\|^2
 =\sum_{i=1}^m d_i^2-\frac1n\left\|\sum_{i=1}^m u_i\right\|^2
 =S-\frac{\delta^2}{n}>0.
\]
For any admissible rates, summing the quadratic-form inequality across the two coordinate directions yields
\[
 1=\sum_i c_iw_i=\sum_iw_i\|u_i-u_0\|^2
 \ge\lambda_2(L(w))Q.
\]
Hence \(\lambda_2(L(w))\le1/Q=\Lambda\), with no assumption about whether any rate vanishes.

**2. Closed-polygon regime.** Suppose \(\delta=0\). Put \(w_i=1/S\). The star Laplacian is then a scalar multiple of the unweighted star Laplacian, with exact eigenvalues \(0\), \(1/S\) repeated \(m-1\) times, and \(n/S\). It achieves the upper bound. Uniqueness follows from equality in the above spectral inequality: each nonzero coordinate column of the centered polygon configuration lies in the eigenspace for \(\lambda_2=1/S\). At leaf \(i\), the associated vector equation reads \(w_i u_i=\Lambda(u_i-\overline u)=\Lambda u_i\), since the polygon mean is zero. Every \(u_i\) is nonzero, so \(w_i=\Lambda\), independently of the polygon's dimension or degeneracy. This also handles equality in the polygon inequality.

**3. Strict-imbalance regime and feasibility.** Suppose \(\delta>0\), and let \(j\) be the unique index with \(d_j>\sum_{i\ne j}d_i\). Write \(B=\sum_{i\ne j}d_i=d_j-\delta>0\). Place the leaf coordinates on a common line, with \(u_j=d_j\) and \(u_i=-d_i\) for \(i\ne j\), and hub coordinate zero. Their mean is \(\delta/n\). Set the rates as in the theorem. They are positive because \(0<\delta<d_j\). Directly,
\[
 \sum_{i=1}^m c_iw_i^*
 =\Lambda\left[S+\frac{\delta}{n}\left(\sum_{i\ne j}d_i-d_j\right)\right]
 =\Lambda\left(S-\frac{\delta^2}{n}\right)=1.
\]
The centered collinear vector is an eigenvector with eigenvalue \(\Lambda\): for each leaf \(i\), the equation \(w_i^*u_i=\Lambda(u_i-\delta/n)\) is immediate, and the hub equation follows by summing all rows of the Laplacian.

**4. Exact matrix lower certificate.** It remains to prove that this eigenvalue is the *smallest positive* eigenvalue, rather than a higher mode. Given any real vertex vector \(y\), subtract the hub value and denote the resulting leaf coordinates by \(z_i=y_i-y_0\). Let \(T=\sum_{i\ne j}z_i\). Then
\[
 \begin{aligned}
 &y^{\mathsf T}(L(w^*)-\Lambda P)y\\
 &\quad=\frac{\Lambda}{n}\left[\delta\left(\sum_{i\ne j}\frac{z_i^2}{d_i}-\frac{T^2}{B}\right)
 +\frac{B}{d_j}\left(z_j+\frac{d_jT}{B}\right)^2\right]\ge0.
 \end{aligned}
\]
The first parenthesis is nonnegative by weighted Cauchy--Schwarz; the second term is a square. Equality among the leaf differences requires \(z_i=\tau d_i\) for all \(i\ne j\) and \(z_j=-\tau d_j\), leaving precisely one nonconstant eigendirection. Therefore \(L(w^*)\succeq\Lambda P\), and the constructed eigenvalue is exactly \(\lambda_2\) and is simple.

**5. Uniqueness in the strict-imbalance regime.** Any other optimal rate vector must saturate the upper certificate of step 1 using the fixed collinear configuration. Thus its centered configuration vector is an eigenvector with eigenvalue \(\Lambda\). The leaf equations \(w_i u_i=\Lambda(u_i-\delta/n)\) then uniquely force each rate to equal the displayed \(w_i^*\), because \(u_i\ne0\). This proves all assertions.

## Verification

The standalone standard-library checker `verify_star.py` runs exact rational tests for every ordered vector of integer edge lengths in \(\{1,2,3,4\}^m\), with \(2\le m\le5\) (1,360 cases). It verifies budgets, rate positivity, optimal-eigenvector equations and 77,488 exact rational specializations of the closed-form positive-semidefinite identity in step 4. Run `python3 verify_star.py`; successful output begins `VERIFY_OK`. Finite computations check algebra but do not replace the proof for all positive real prices and unbounded numbers of leaves.

## Relationship to prior work

The general semidefinite-programming and maximum-variance-embedding equivalence for maximizing weighted Laplacian algebraic connectivity subject to arbitrary linear edge costs is established by Sun--Boyd--Xiao--Diaconis (2006). The uniformly priced star and its high-dimensional and low-dimensional optimal embeddings are explicitly treated by Göring--Helmberg--Wappler (2005 preprint, Example 6). Farhadi--Louis--Singh--Tetali (2022 revision) studies variance embedding on trees and a distinct star \(\lambda_\infty\) problem. The present theorem concerns the complete **arbitrary positive edge-price** spectral-gap optimizer and its exact geometric regime boundary; it neither proposes the general SDP/embedding duality as new nor claims a new result for uniform prices alone.

## Limitations

Only symmetric continuous-time rates, one shared *linear* price budget, and star topology are covered. This says nothing about discrete-time stochastic-matrix optimization, fixed edge capacities, arbitrary vertex stationary masses, or general trees. Spectral simplicity at strict imbalance does not imply robustness under rate uncertainty. The full text of Fiedler's 1990 historical tree paper could not be inspected; a differently worded prior specialization of the arbitrary-price conclusion cannot be excluded by searches alone.

## References

1. F. Göring, C. Helmberg, M. Wappler, *Embedded in the Shadow of the Separator*, preprint first available September 2, 2005, https://optimization-online.org/2005/09/1202/ ; journal version, SIAM J. Optimization 19 (2008), 472--501, DOI 10.1137/050639430.
2. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681--699, published online November 2, 2006, DOI 10.1137/S0036144504443821; lawful author PDF https://stanford.edu/~boyd/papers/pdf/fmmp.pdf.
3. M. Farhadi, A. Louis, M. Singh, P. Tetali, *Maximum Variance Embedding: Measuring and Optimizing Connectivity of a Graph Metric*, arXiv:2003.05582v3, https://arxiv.org/abs/2003.05582.
4. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85--106, DOI 10.1080/03081089008817967 (abstract consulted; full text not inspected).
