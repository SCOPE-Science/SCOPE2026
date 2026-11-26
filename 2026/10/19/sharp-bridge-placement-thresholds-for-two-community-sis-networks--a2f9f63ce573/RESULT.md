# Sharp bridge-placement thresholds for two-community SIS networks

## Finding

Fix integers \(n\ge2\) and \(1\le k\le n\). Consider two disjoint complete contact communities with \(n\) vertices each and exactly \(k\) distinct, undirected, unweighted intercommunity contacts, with no other edges. Let \(A_B\) be the resulting \(2n\)-vertex adjacency matrix and \(\lambda(B)=\rho(A_B)\). Among **all** choices of the \(k\) cross-community edges, the smallest spectral radius is attained exactly when the cross edges form a matching, and the largest is attained exactly when all cross edges share one endpoint (a star). When \(k=1\) the two descriptions coincide; for \(k>1\) both extremizers are unique up to relabeling the vertices and exchanging communities.

Writing \(\lambda_M\) and \(\lambda_S\) for these sharp bounds,
\[
\lambda_M=\frac{n-1+\sqrt{(n-1)^2+4k}}{2},\qquad
\lambda_M\le\lambda(B)\le\lambda_S,
\]
where \(\lambda_S\) is the unique real root strictly greater than \(n-1\) of
\[
[(\lambda+1)(\lambda-n+1)]^2
=k(\lambda-n+2)(\lambda-n+1+k).
\]
Every community separately has the same local spectral SIS threshold \(1/(n-1)\), independently of bridge placement, but the exact global spectral thresholds satisfy
\[
\frac1{\lambda_S}\le\frac1{\lambda(B)}\le\frac1{\lambda_M}<\frac1{n-1}.
\]
For a sequence with \(k/n\to\theta\in(0,1]\) as \(n\to\infty\), the two **excess spectral radii** and the finely rescaled threshold separation obey
\[
\lambda_M-(n-1)\longrightarrow\theta,\quad
\lambda_S-(n-1)\longrightarrow
\frac{\theta}{2}\bigl(\theta+\sqrt{\theta^2+4}\bigr),
\]
\[
n^2\left(\frac1{\lambda_M}-\frac1{\lambda_S}\right)
\longrightarrow\frac{\theta}{2}\bigl(\theta+\sqrt{\theta^2+4}-2\bigr)>0.
\]

For the explicitly specified **deterministic SIS probability recurrence** below, the spectral threshold is the exact boundary between convergence to zero and convergence to a unique strictly positive equilibrium from nonzero data, with convergence to zero at equality. The graph example \(n=4,k=3\) has \(\lambda_M<50/13<\lambda_S\). Thus, even with identical local thresholds and bridge counts, the two graphs can lie on opposite sides of the deterministic recurrence's threshold at the same model ratio.

## Assumptions and scope

Let \(B\in\{0,1\}^{n\times n}\) contain exactly \(k\) ones. Set \(C=\mathbf1\mathbf1^{\mathsf T}-I_n\) and
\[
A_B=\begin{pmatrix}C&B\\B^{\mathsf T}&C\end{pmatrix}.
\]
This is a simple connected graph because \(k\ge1\). Graph eigenvalues are those of the symmetric adjacency matrix, not transition-matrix or Laplacian eigenvalues. The comparison fixes both complete internal communities and the cross-edge count; rewiring internal contacts is excluded.

For the nonlinear application, take \(0<d<1\) and \(0<\beta<1\), and define for every \(p\in[0,1]^{2n}\)
\[
F_i(p)=1-[1-(1-d)p_i]\prod_{j=1}^{2n}(1-\beta (A_B)_{ij}p_j).
\]
This is a deterministic nonlinear probability approximation, not the full finite-state stochastic SIS Markov chain. The latter has eventual extinction in every finite network without exogenous infection. We define a strictly positive equilibrium to mean all \(2n\) coordinates lie in \((0,1)\). The *spectral threshold* is the critical ratio \(\beta/d=1/\lambda(B)\).

## Proof

**1. Global minimum and equality case.** The Rayleigh quotient of the all-ones vector is \(n-1+k/n\), so \(\lambda=\lambda(B)>n-1\). Put \(h=\lambda-n+1>0\) and let \((x,y)\gg0\) be a Perron eigenvector. Write \(X=\sum_i x_i\), \(Y=\sum_j y_j\), and \(r_i=\sum_jB_{ij}\), \(s_j=\sum_iB_{ij}\). The eigenvector equations are
\[
(\lambda+1)x_i=X+(By)_i,\qquad
(\lambda+1)y_j=Y+(B^{\mathsf T}x)_j.
\]
Summing gives \(hX=\sum_j s_jy_j\) and \(hY=\sum_i r_ix_i\). Multiplying the first eigenvector equation by \(r_i\) and summing yields
\[
(\lambda+1)hY=kX+\sum_i r_i(By)_i
\ge kX+\sum_i(By)_i=(k+h)X,
\]
since \((By)_i\) vanishes on unoccupied rows and \(r_i\ge1\) on occupied rows. Similarly \((\lambda+1)hX\ge(k+h)Y\) using the column degrees. Multiply these two inequalities and cancel \(XY>0\) to obtain \(((\lambda+1)h)^2\ge(k+h)^2\). Taking positive square roots gives \(\lambda h\ge k\). The positive root of \(\lambda(\lambda-n+1)=k\) is the displayed \(\lambda_M\).

Equality holds exactly when both row and column estimates are equalities. The Perron vector is strictly positive, so these equalities hold precisely when every occupied row and column has degree one, that is, when the cross edges form a matching. This also covers \(k=n\), when the matching graph is regular of degree \(n\).

**2. Global maximum and equality case.** Fix \(z>n-1\) and put
\[
R(z)=(zI_n-C)^{-1}=aI_n+b\mathbf1\mathbf1^{\mathsf T},\quad
a=\frac1{z+1},\quad b=\frac1{(z+1)(z-n+1)}.
\]
Both \(a,b\) are positive. By a block congruence and the Schur complement, \(zI_{2n}-A_B\) is positive semidefinite exactly when \(\|R(z)^{1/2}BR(z)^{1/2}\|_2\le1\), and it is positive definite exactly when this norm is strictly less than one. For every \(B\),
\[
\begin{aligned}
\|R^{1/2}BR^{1/2}\|_2^2
&\le\operatorname{tr}(RBRB^{\mathsf T})\\
&=a^2k+ab\left(\sum_i r_i^2+\sum_j s_j^2\right)+b^2k^2\\
&\le a^2k+ab(k^2+k)+b^2k^2.
\end{aligned}
\]
The last inequality counts intersecting pairs of distinct bridge edges: two distinct edges in a simple bipartite graph share at most one endpoint, giving \(\sum r_i^2+\sum s_j^2\le2k+2\binom{k}{2}=k^2+k\). For \(k>1\), equality requires all bridge edges to have one common endpoint: if two edges have a common endpoint, any edge meeting both must contain that endpoint, since their two other endpoints are on the same side. For a star, \(B\) has rank one, so the first trace inequality is also equality. Thus the rightmost expression is the exact squared operator norm for a star:
\[
\left\|R(z)^{1/2}B_SR(z)^{1/2}\right\|_2^2
=\frac{k(z-n+2)(z-n+1+k)}{(z+1)^2(z-n+1)^2}.
\]
The terms \(a,b\) are positive and strictly decreasing in \(z\). The expression decreases strictly from infinity to zero as \(z\) increases over \((n-1,\infty)\). Its unique crossing of one is \(\lambda_S\) by the Schur complement. At \(z=\lambda_S\) the squared-norm bound is at most one for every \(B\) and strictly less than one for each nonstar pattern. This proves the sharp maximum and its equality class.

**3. Large-community window.** Put \(h_M=\lambda_M-n+1\), \(h_S=\lambda_S-n+1\). The equation \((n-1+h_M)h_M=k\) implies \(0<h_M\le1\), and then \(h_M\to\theta\). The star equation is
\[
(n+h_S)^2h_S^2=k(h_S+1)(h_S+k).
\]
Here \(0<h_S<2\): the left minus right side is negative at zero and positive at two because \(4(n+2)^2-3k(k+2)>0\) for \(k\le n\). The root is unique. Dividing by \(n^2\) shows that every subsequential limit satisfies \(h^2=\theta^2(h+1)\) with \(h\ge0\), so \(h_S\to\theta(\theta+\sqrt{\theta^2+4})/2\). The scaled reciprocal difference is \(n^2(h_S-h_M)/(\lambda_M\lambda_S)\), which tends to the claimed limit because both eigenvalues are \(n+O(1)\).

**4. Exact deterministic SIS consequence.** On \([0,1]^{2n}\), the map \(F\) is continuous and coordinatewise increasing, and its derivative at zero is \(L=(1-d)I+\beta A_B\). Write \(q_i(p)=1-\prod_j(1-\beta A_{ij}p_j)\), with \(A=A_B\). The union bound on this cube gives \(q_i(p)\le\beta(Ap)_i\). Hence \(F(p)\le Lp\), so every orbit converges exponentially to zero when \(\beta\lambda(B)<d\). Every nonzero orbit is strictly positive after finitely many steps since coordinates already positive stay positive and positivity reaches neighbors at each step. The image of the cube has all coordinates strictly below one because \(0<d,\beta<1\).

At equality \(\beta\lambda(B)=d\), let \(w\gg0\) be a Perron vector of the symmetric adjacency matrix. Then \(w^{\mathsf T}F(p)\le w^{\mathsf T}p\). If \(p\gg0\), the loss term \((1-d)p_iq_i(p)>0\) in \(F_i(p)=(1-d)p_i+q_i(p)-(1-d)p_iq_i(p)\) gives strict decrease. If a nonzero limit point \(p_*\) existed, continuity would make all its forward iterates limit points with the same limiting value of \(w^{\mathsf T}p\). A strictly positive iterate of \(p_*\) would violate this constancy. Hence zero is the only limit point and the orbit converges to zero.

When \(\beta\lambda(B)>d\), differentiability and the Perron multiplier \(1-d+\beta\lambda(B)>1\) give \(F(\varepsilon w)>\varepsilon w\) for small positive \(\varepsilon\). Monotone iteration from \(\varepsilon w\) increases and from the all-ones vector decreases. By continuity both limits are strictly positive fixed points. For \(p\gg0\) and \(0<t<1\), the function \(t\mapsto q_i(tp)\) is concave on \([0,1]\): its second derivative is a sum of nonpositive terms obtained by differentiating two different factors in the product with a minus sign. As \(q_i(0)=0\), we have \(q_i(tp)\ge t q_i(p)\). It follows that
\[
F_i(tp)-tF_i(p)\ge t(1-d)(1-t)p_iq_i(p)>0.
\]
If there were distinct positive fixed points \(p,r\), interchange them if necessary so that \(t=\min_i r_i/p_i<1\). Then \(r\ge tp\) with equality in some coordinate, but \(r=F(r)\ge F(tp)>tF(p)=tp\), a contradiction. Every nonzero orbit eventually lies above some sufficiently small positive subsolution \(\varepsilon w\) and below the all-ones vector. Both monotone bounds converge to the same fixed point, so the orbit converges to it.

For the finite graph example \(n=4,k=3\), at \(z=50/13\) the matching polynomial \(z^2-3z-3\) equals \(43/169>0\), so \(\lambda_M<z\). The star polynomial, left minus right of the displayed equation for \(\lambda_S\), equals \(-128151/28561<0\), so \(z<\lambda_S\). This puts the common model ratio \(1/z\) strictly between the reciprocal radii.

## Verification

Run `python checker.py` with Python 3 and NumPy installed. The checker directly builds every relevant \(2n\)-vertex adjacency matrix for all cross-edge subsets with \(2\le n\le4\), plus seeded larger samples, and independently compares numerical eigenvalues with both sharp formulas and equality patterns. It also tests the degree-square combinatorial bound and the asymptotic formula at larger sizes. A representative execution recorded 5,421 configurations and nine limit checks. These are finite corroborations of the spectral statements, not proofs for arbitrary sizes. The exact rational comparison and the nonlinear classification follow from the analytic proof rather than from the supplied checker.

## Relationship to prior work

Hoang and Nguyen (2026) study the discrete-time SIS approximation and define local community spectral threshold sets, proving the general direction of the local-versus-global inequality. The fixed-budget optimization over bridge placement here gives both sharp bounds and equality classes; those conclusions do not follow from their local-versus-global inequality. The use of the spectral threshold in the deterministic model is background, not a claim of a new SIS threshold.

Olesker-Taylor and Zanetti (2024) consider two cliques connected by a matching in the setting of fastest Markov-chain mixing; that objective is not the unnormalized adjacency spectral radius. The spectral clique-supersaturation work (2026) compares stars and matchings inserted inside Turán parts under a clique-count constraint, rather than cross edges between two already complete communities with a fixed edge budget. Schur complements and Perron theory are established background.

## Limitations

The construction assumes exactly two equally sized complete communities, a simple unweighted undirected abstract contact network, a cross-edge count no larger than the community size, homogeneous parameters, and the specified deterministic probability map. It does not optimize unequal communities or weighted or directed bridges, and it does not address finite stochastic extinction times or observed epidemiological processes. The sharp extremal inequality concerns adjacency matrices; the deterministic classification does not imply persistence in a finite-state SIS Markov chain. Historical priority beyond the compared statements is not certified.

## References

1. Hoang Phi Dung and Nguyen Hong Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048, https://arxiv.org/abs/2607.14048 .
2. S. Olesker-Taylor and L. Zanetti, *Geometric bounds on the fastest mixing Markov chain*, *Probability Theory and Related Fields* (2024), DOI:10.1007/s00440-023-01257-x .
3. *Strict spectral supersaturation for cliques: extremal graphs and sharp thresholds*, arXiv:2610.03337, https://arxiv.org/html/2610.03337v1 .
4. D. Chakrabarti et al., *Epidemic thresholds in real networks*, *ACM Transactions on Information and System Security* 10(4), 2008, DOI:10.1145/1284680.1284681 .
