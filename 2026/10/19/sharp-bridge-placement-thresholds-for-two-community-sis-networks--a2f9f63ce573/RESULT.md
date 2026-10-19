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
For a sequence with \(k/n\to\theta\in(0,1]\), the two **excess spectral radii** and the finely rescaled threshold separation obey
\[
\lambda_M-(n-1)\longrightarrow\theta,\quad
\lambda_S-(n-1)\longrightarrow
\frac{\theta}{2}\bigl(\theta+\sqrt{\theta^2+4}\bigr),
\]
\[
n^2\left(\frac1{\lambda_M}-\frac1{\lambda_S}\right)
\longrightarrow\frac{\theta}{2}\bigl(\theta+\sqrt{\theta^2+4}-2\bigr)>0.
\]

For the explicitly specified **deterministic SIS probability recurrence** below, this threshold is also the exact disease-free versus positive-endemic boundary, including extinction at equality. For example, when \(n=4\), \(k=3\), the same spreading/recovery probabilities \((\beta,d)=(13/125,2/5)\) yield extinction for matching bridges and global convergence to a unique positive endemic equilibrium for star bridges, from every nonzero initial infection-probability vector. Thus identical community threshold sets and bridge budgets can predict opposite long-term behavior when bridge placement differs.

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

**1. Global minimum and equality case.** Set \(\lambda=\lambda(B)>n-1\), \(h=\lambda-n+1>0\), and let \((x,y)\gg0\) be a Perron eigenvector. Write \(X=\sum_i x_i\), \(Y=\sum_j y_j\), and \(r_i=\sum_jB_{ij}\), \(s_j=\sum_iB_{ij}\). The eigenvector equations are
\[
(\lambda+1)x_i=X+(By)_i,\quad
(\lambda+1)y_j=Y+(B^{\mathsf T}x)_j.
\]
Summing gives \(hX=\sum_j s_jy_j\) and \(hY=\sum_i r_ix_i\). Since every occupied row of \(B\) has integer degree at least one,
\[
(\lambda+1)hY=kX+\sum_i r_i(By)_i
\ge kX+\sum_i(By)_i=(k+h)X,
\]
so \(\lambda hY\ge kX\). Interchanging the two sides gives \(\lambda hX\ge kY\), hence \(\lambda(\lambda-n+1)\ge k\). The positive root is the displayed \(\lambda_M\). Equality requires every occupied row and column degree to equal one; this means precisely a matching. Conversely, for a matching its automorphism-symmetric Perron vector, or its two-class equitable quotient, gives \(\lambda_M(\lambda_M-n+1)=k\). In particular this proof covers \(k=n\), when the matching graph is regular of degree \(n\).

**2. Global maximum and equality case.** Fix \(z>n-1\) and put
\[
R(z)=(zI_n-C)^{-1}=aI_n+b\mathbf1\mathbf1^{\mathsf T},\quad
a=\frac1{z+1},\quad b=\frac1{(z+1)(z-n+1)}.
\]
Both \(a,b\) are positive. By the Schur complement, \(zI_{2n}-A_B\) is positive semidefinite exactly when \(\|R(z)^{1/2}BR(z)^{1/2}\|_2\le1\). For every \(B\),
\[
\begin{aligned}
\|R^{1/2}BR^{1/2}\|_2^2
&\le\operatorname{tr}(RBRB^{\mathsf T})\\
&=a^2k+ab\left(\sum_i r_i^2+\sum_j s_j^2\right)+b^2k^2\\
&\le a^2k+ab(k^2+k)+b^2k^2.
\end{aligned}
\]
The last inequality counts intersecting pairs of distinct bridge edges: two distinct edges in a simple bipartite graph share at most one endpoint, giving \(\sum r_i^2+\sum s_j^2\le2k+2\binom{k}{2}=k^2+k\). For \(k>1\), equality requires all bridge edges to have one common endpoint: pairwise-intersecting edges in a bipartite graph form a star. For a star, \(B\) has rank one, so the first trace inequality is also equality. Thus the rightmost expression is the **exact** squared singular norm for a star.

The star's rank-one bridge operator has squared singular norm
\[
\left\|R(z)^{1/2}B_SR(z)^{1/2}\right\|_2^2
=\frac{k(z-n+2)(z-n+1+k)}{(z+1)^2(z-n+1)^2}.
\]
It is strictly decreasing from infinity to zero as \(z\) increases over \((n-1,\infty)\) (equivalently, the resolvent is entrywise decreasing and strictly positive). Hence the unique value where it equals one is exactly \(\lambda_S\). At \(z=\lambda_S\) the trace bound above is at most one for every \(B\), so the Schur complement gives \(\lambda(B)\le\lambda_S\). Strict inequality holds for nonstar patterns when \(k>1\). The equality class and the complete sharp interval follow.

**3. Large-community window.** Put \(h_M=\lambda_M-n+1\), \(h_S=\lambda_S-n+1\). From \(\lambda_M h_M=k\) and \(k/n\to\theta\), we obtain \(h_M\to\theta\). Writing the star equation as
\[
(n+h_S)^2h_S^2=k(h_S+1)(h_S+k)
\]
shows that \(0<h_S<2\) for all \(1\le k\le n\): the left minus right side is negative at zero and positive at two, and the resolvent root is unique. Every subsequential limit therefore solves \(h^2=\theta^2(h+1)\). Its unique positive solution is \(\theta(\theta+\sqrt{\theta^2+4})/2\). Expanding the two reciprocals, whose denominators are \(n+O(1)\), proves the claimed limit for \(n^2(1/\lambda_M-1/\lambda_S)\).

**4. Exact deterministic SIS consequence.** The map \(F:[0,1]^{2n}\to[0,1]^{2n}\) is continuous and coordinatewise increasing, and its derivative at zero is \(L=(1-d)I+\beta A_B\). For all \(p\ge0\), the union bound gives \(F(p)\le Lp\), so when \(\beta\lambda(B)<d\), every orbit converges exponentially to zero. At equality, let \(w\gg0\) be a left Perron vector of \(A_B\). Then \(w^{\mathsf T}F(p)\le w^{\mathsf T}p\), and the inequality is strict whenever \(p\gg0\), because the factor \(1-(1-d)p_i\) produces a strictly positive loss \((1-d)p_i[1-\prod_j(1-\beta A_{ij}p_j)]\). Every nonzero orbit is strictly positive after finitely many steps by graph connectivity, persistence of positivity because \(d<1\), and \(\beta>0\). Compactness and the strict Lyapunov decrease force its only accumulation point to be zero.

When \(\beta\lambda(B)>d\), there is \(\varepsilon>0\) such that \(F(\varepsilon w)>\varepsilon w\) componentwise, from differentiability and the linear Perron multiplier \(1-d+\beta\lambda(B)>1\). Monotone iteration from \(\varepsilon w\) is increasing, iteration from the all-ones vector is decreasing, and their limits bound a positive equilibrium. For \(p\gg0\) and \(0<t<1\), writing \(q_i(p)=1-\prod_j(1-\beta A_{ij}p_j)\), concavity of \(q_i(tp)\) as a function of \(t\) implies \(q_i(tp)\ge t q_i(p)\). Therefore
\[
F_i(tp)-tF_i(p)\ge t(1-d)(1-t)p_iq_i(p)>0.
\]
This strict radial subhomogeneity, monotonicity, and a minimum-ratio comparison give uniqueness of the strictly positive equilibrium: distinct positive equilibria would violate the displayed strict inequality at a coordinate attaining the smaller componentwise ratio. Every nonzero orbit eventually becomes strictly positive, then lies between an iterated positive subsolution and the all-ones supersolution, and consequently converges to that unique equilibrium.

Finally, for \(n=4,k=3\), the matching root obeys \(\lambda_M^2-3\lambda_M-3=0\); at \(z=50/13\), \(z^2-3z-3=43/169>0\), so \(\lambda_M<50/13\). The star polynomial from step 2 equals \(-128151/28561<0\) at the same \(z\), so \(\lambda_S>50/13\). With \(\beta/d=13/50\), matching bridges lie below their global threshold, while star bridges lie above it, proving the claimed opposite dynamical outcomes.

## Verification

Run `python checker.py` with Python 3 and NumPy installed. The checker directly builds every relevant \(2n\)-vertex adjacency matrix for all cross-edge subsets with \(2\le n\le4\), plus seeded larger samples, and independently compares numerical eigenvalues with both sharp formulas and equality patterns. It also tests the degree-square combinatorial bound and the asymptotic formula at larger sizes. A representative execution passed 5,421 configurations and nine limit checks. The exact rational comparison at \(z=50/13\) is reconstructed in step 4; numerical model iterations corroborate, but do not establish, the nonlinear classification.

## Relationship to prior work

Hoang and Nguyen (2026) study the discrete-time SIS approximation and define local community spectral threshold sets, proving the general direction of the local-versus-global inequality. The present fixed-budget *optimization over bridge placement* gives both sharp possible global thresholds, unique extremizers, and explicit epidemic outcomes inaccessible from that community threshold set alone. That source's Theorem 1 does not imply either extremizer or its equality condition.

The work on fastest-mixing Markov chains by Olesker-Taylor and Zanetti (2024) uses two n-cliques joined by a matching or a single gateway star as examples for **random-walk mixing and conductance**. Those quantities are not the unnormalized adjacency spectral radius or the deterministic SIS threshold studied here. Recent spectral clique-supersaturation work (2026) likewise compares stars and matchings inserted inside Turán parts, rather than cross edges between two already complete communities. The general use of spectral radii in SIS models, Schur complements, and Perron theory is established background, not claimed as new.

## Limitations

The construction assumes exactly two equally sized complete communities, a simple unweighted undirected contact network, a cross-edge budget no larger than the community size, homogeneous infection and recovery, and the specified deterministic probability map. It does not optimize unequal communities, weighted/directed bridges, finite stochastic extinction times, or observed epidemiological processes. No claim of exhaustive novelty across unindexed literature is made. The sharp extremal inequality is proven mathematically; the epidemic interpretation applies to the displayed deterministic approximation and not to guaranteed persistence in a finite-state SIS Markov chain.

## References

1. Hoang Phi Dung and Nguyen Hong Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048, first submitted 2026-07-15. Full-text reading: https://academ.us/article/2607.14048/ .
2. *Geometric bounds on the fastest mixing Markov chain*, *Probability Theory and Related Fields* (2024), DOI:10.1007/s00440-023-01257-x. Full text: https://link.springer.com/article/10.1007/s00440-023-01257-x .
3. *Strict spectral supersaturation for cliques: extremal graphs and sharp thresholds*, arXiv:2610.03337, 2026-10-02, https://arxiv.org/html/2610.03337v1 .
4. D. Chakrabarti et al., *Epidemic thresholds in real networks*, *ACM Transactions on Information and System Security* 10(4), 2008, DOI:10.1145/1284680.1284681 .
