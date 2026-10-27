# An exact three-regime spectral-gap allocation for unequal barbell graphs

## Finding
Let \(p\ge q\ge2\) be integers. Join one designated vertex of \(K_p\) to one designated vertex of \(K_q\) by a single bridge. With nonnegative edge conductances of total sum \(B>0\), write \(\Lambda_{p,q}(B)\) for the largest possible second eigenvalue of the weighted Laplacian. Define
\[
N=p+q,\quad r=p-1,\quad t_0=\frac{2q-1}{r},\quad
 t_{\min}=\sqrt{\frac{p}{2r}},\quad
 t_*=\min\{1,\max\{t_{\min},t_0\}\}.
\]
The exact optimum is
\[
\boxed{\Lambda_{p,q}(B)=\frac{B}{D_*}},\qquad
D_*=p+4q-4-\frac{r^2}{N}(t_*-t_0)^2.
\]
Equivalently, it has three regimes:
\[
D_*=\begin{cases}
\frac{9pq}{p+q}-4,&p\le2q,\\
p+4q-4,&2q<p\ \text{and}\ p(p-1)\le2(2q-1)^2,\\
p+4q-4-\frac{\big(\sqrt{p(p-1)/2}-(2q-1)\big)^2}{p+q},&p(p-1)>2(2q-1)^2.
\end{cases}
\]
The optimum is unique, including at the boundaries. In the third regime precisely the edges between two non-bridge vertices of the **larger clique** receive positive conductance. These edges have zero optimal conductance in the first two regimes. Every edge between two non-bridge vertices of the smaller clique has zero optimal conductance in every regime.

For all regimes define \(\mu=((q+1)t_*+2q-1)/N\) and \(\lambda=B/D_*\). All individual optimal conductances are:
\[
\begin{aligned}
a&=\lambda\mu/t_*&&\text{(each larger-side spoke)},\\
b&=\lambda(t_*+2-\mu)&&\text{(each smaller-side spoke)},\\
h&=\lambda(p\mu-t_*)&&\text{(bridge)},\\
c&=\max\{0,\lambda(1-\mu/t_*)/r\}&&\text{(each larger-side internal non-spoke edge)},\\
d&=0&&\text{(each smaller-side internal non-spoke edge)}.
\end{aligned}
\]
Here \(c\ge0\) in every regime, and \(c>0\) exactly in the third regime; the formula gives \(c=0\) otherwise. When a class has no edges, its quoted weight is merely a harmless convention.

## Assumptions and scope
The host is the ordinary simple barbell obtained from exactly two complete graphs of orders \(p,q\) by a single inter-clique bridge, with no additional edges. All allowed conductances may vanish. The weighted Laplacian is \(L=\sum_{\{i,j\}}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T}\), and the objective is \(\lambda_2(L)\), not the discrete-time second-largest eigenvalue modulus or a sum of effective resistances. The total of the undirected edge conductances is exactly \(B\). Swapping the two cliques yields the symmetric equivalent statement, so \(p\ge q\) entails no loss. The cases \(q=2\), \(p=q\), and equality at both phase boundaries are included.

## Proof
Put \(r=p-1\), \(s=q-1\), \(N=p+q\). Call the two bridge endpoints \(H_L,H_R\), with \(r\) other vertices \(L_i\) and \(s\) other vertices \(R_j\). Fix a number \(t\in[t_{\min},1]\), where \(t_{\min}=\sqrt{p/(2r)}\). In Euclidean space of dimension at most \(r\), choose centered regular-simplex vectors \(y_1,\ldots,y_r\) satisfying
\[\sum_i y_i=0,\quad \lVert y_i\rVert^2=1-t^2,\quad
 \lVert y_i-y_j\rVert^2=\frac{2r(1-t^2)}{r-1}\quad(i\ne j),\]
with \(y_1=0\) if \(r=1\). Place the vertices at
\[
X_{L_i}=(0,y_i),\quad X_{H_L}=(t,0),\quad
X_{H_R}=(t+1,0),\quad X_{R_j}=(t+2,0),
\]
and translate all vertices by their common centroid. Every spoke and the bridge have squared Euclidean length exactly one. The edges between the \(L_i\) have squared length at most one by the definition of \(t_{\min}\); those between the \(R_j\) have zero length. Thus every edge of the host has squared length at most one.

The first-coordinate centroid is \(\mu(t)=((q+1)t+2q-1)/N\). The centered configuration has squared norm
\[
D(t)=\sum_v\lVert X_v-\overline X\rVert^2
=p+4q-4-\frac{r^2}{N}\left(t-\frac{2q-1}{r}\right)^2.
\]
For every admissible Laplacian \(L(w)\), the Rayleigh principle applied to each nonconstant coordinate of this centered configuration gives
\[
\lambda_2(L(w))D(t)\le
\sum_v X_v^{\mathsf T}L(w)X_v
=\sum_{\{i,j\}}w_{ij}\lVert X_i-X_j\rVert^2\le B.
\]
The concave quadratic \(D(t)\) is largest on \([t_{\min},1]\) at the clipped value \(t_*\). Hence \(\lambda_2\le B/D_*\) for every allocation. The inequalities \(t_0\ge1\iff p\le2q\) and \(t_0<t_{\min}\iff p(p-1)>2(2q-1)^2\) yield the three explicit regimes.

To attain the bound, use the conductances \(a,b,h,c,d\) stated above, with \(t=t_*\), \(\mu=\mu(t)\), \(\lambda=B/D_*\). The quantities \(a,b,h\) are strictly positive. The identity
\[
 t-\mu=\frac{r}{N}(t-t_0)
\]
shows \(c\ge0\): when \(t<1\), one has \(t\ge t_0\), and when \(t=1\), the definition using the maximum makes \(c=0\). Directly, \(c\) is positive exactly when \(t=t_{\min}>t_0\). The rate sum can be checked algebraically, or from the eigenvector and complementary-slackness identities below: \(\sum w_{ij}=\lambda D_*=B\).

The scalar centered first coordinate has four consecutive levels \(-\mu,t-\mu,t+1-\mu,t+2-\mu\); substitution into the individual vertex eigen-equations gives \(Lx=\lambda x\). Every coordinate of the simplex vectors is a left-leaf-contrast vector, with Laplacian eigenvalue \(a+rc=\lambda\) when \(t<1\); when \(t=1\), there are no nonzero simplex coordinates and the left-leaf-contrast eigenvalue satisfies \(a\ge\lambda\). The right-leaf-contrast eigenvalue is \(b\ge\lambda\) because \(t+2-\mu\ge1\).

It remains to check the other eigenvalues in the four-dimensional subspace of vectors constant on each vertex group. Its nonzero spectrum is that of
\[
Q=C^{1/2}\Delta M^{-1}\Delta^{\mathsf T}C^{1/2},\qquad
M=\operatorname{diag}(r,1,1,s),\quad C=\operatorname{diag}(ra,h,sb),
\]
where \(\Delta\) is the oriented incidence matrix of the four-vertex path in ascending-level orientation. This is an irreducible positive-definite tridiagonal matrix with strictly negative off-diagonal entries. The edge-gradient vector \(C^{1/2}\Delta x\) is strictly positive and is an eigenvector of \(Q\) with eigenvalue \(\lambda\), so by the Perron--Frobenius theorem applied to a sufficiently large scalar multiple of the identity minus \(Q\), \(\lambda\) is the **smallest** eigenvalue of \(Q\). All other quotient modes are therefore at least \(\lambda\). The full Laplacian consists of the quotient and the two leaf-contrast subspaces, so indeed \(\lambda_2(L)=\lambda\).

All edges with positive conductance have squared length one in the displayed embedding: the only delicate class is the larger-side leaf-leaf class, which has positive weight only when \(t=t_{\min}\), precisely when its squared length equals one. Therefore
\(\sum w_{ij}=\sum w_{ij}\lVert X_i-X_j\rVert^2=\lambda D_*=B\), verifying the budget and equality throughout the dual bound.

Finally, suppose another allocation attains the bound for this fixed dual embedding. Equality requires zero conductance on all embedding edges of length strictly less than one; hence all smaller-side non-spoke edges vanish, and so do the larger-side non-spoke edges when \(t>t_{\min}\). Equality of the Rayleigh step also requires every nonzero coordinate column of the centered embedding to be a \(\lambda\)-eigenvector. The scalar coordinate then determines individually the \(r+s\) spoke conductances and the bridge conductance as the displayed \(a,b,h\). When \(t<1\), the simplex coordinates span the entire left-leaf zero-sum subspace and force its full induced Laplacian to be \((\lambda-a)(I-\mathbf1\mathbf1^{\mathsf T}/r)\), which forces every left internal weight to equal \(c\). If \(t=1\), those edges already vanish by strict slackness. Thus every conductance is uniquely determined, including on the phase boundaries.

## Verification
The included `barbell_verification.py` builds the full weighted Laplacian for every integer pair \(2\le q\le p\le50\). Its 1225 cases check the rate sum, computed \(\lambda_2\), the explicit scalar Fiedler eigenvector, the dual norm, nonnegativity, and the simplex edge-length constraint. These are finite consistency checks; the proof above is what covers all integers \(p\ge q\ge2\) and all real \(B>0\).

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006) give the general budgeted continuous-time fastest-mixing formulation and its maximum-variance-unfolding dual, which is used here. Richter and Rocha's 2014 double-broom result covers the two-hub tree obtained by retaining only spokes and the bridge; its tree optimum yields the initial regimes but does **not** cover the third regime. In the third regime the complete barbell permits positive left internal weights and gives a strictly larger optimum than the tree, because \(D_*<p+4q-4\). Ghosh, Boyd and Saberi (2006) optimize a different objective, the total effective resistance, including a balanced-barbell example. Nabli and Oyallon's asynchronous barbell analysis concerns accelerated communication objectives, not the present budgeted \(\lambda_2\). Song and coauthors' 2024 paper concerns unweighted barbell algebraic connectivity in its accessible abstract; its full text was not available for comparison.

## Limitations
Nonnegative rather than strictly positive rates are essential: many allowed clique edges have zero rates at the optimum. The result applies to a *single* bridge between two complete cliques and a scalar total-rate budget, not multiple bridges, constrained edge-specific budgets, normalized random walks, or discrete-time SLEM. The displayed 2024 barbell article remains a residual bibliographic coverage risk because its full text was unavailable; novelty beyond the inspected literature is not independent certification. No claims about algorithms for general graphs or infinite-dimensional limits are made.

## References
1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, "The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem," *SIAM Review* 48 (2006), 681–699. DOI 10.1137/S0036144504443821. https://stanford.edu/~boyd/papers/pdf/fmmp.pdf
2. S. Richter, I. Rocha, "Absolute algebraic connectivity of double brooms," preprint dated 4 June 2014. https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf
3. A. Ghosh, S. Boyd, A. Saberi, "Minimizing Effective Resistance of a Graph," 2006. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
4. M. Nabli, E. Oyallon, "DADAO: Decoupled Accelerated Decentralized Asynchronous Optimization," *Journal of Machine Learning Research* 26 (2025). https://jmlr.org/papers/volume26/23-0748/23-0748.pdf
5. Song et al., "The algebraic connectivity of barbell graphs," *Discrete Mathematics*, 2024, DOI 10.1016/j.disc.2024.114027 (abstract inspected, full text not inspected).
