# Universal half-mass transition in endpoint Poisson response of path-attached graphs

## Finding
Let \(H\) be any finite connected simple graph with \(m\ge2\) vertices, distinguished vertex \(o\), and unnormalized combinatorial Laplacian spectral gap \(\gamma=\lambda_2(L_H)>0\). Attach a unit-edge path \(1,\ldots,p\), \(p\ge1\), to \(o\) by the edge \(o1\). Write \(N=m+p\), let \(L\) be the resulting unnormalized graph Laplacian, and define the sharp *tip response*
\[
\mathcal T(H,p)=\sup\left\{\left|(L^\dagger f)(p)\right|:\; f\in\mathbb R^N,\ \|f\|_{\ell^\infty}\le1,\ \sum_{v}f(v)=0\right\}.
\]
All vertices are counted with unit mass. The following two-part statement holds.

**Universal continuum profile.** For every such \(H,p\), putting \(\lambda=m/N\),
\[
\left|\frac{\mathcal T(H,p)}{N^2}-\Phi(\lambda)\right|
\le\frac1N+\frac{m(m+\sqrt m)}{\gamma N^3},
\qquad
\Phi(\lambda)=
\begin{cases}
\displaystyle\frac18-\frac{\lambda^3}{3},&0\le\lambda\le\frac12,\\
\displaystyle\frac{(1-\lambda)^2(1+2\lambda)}6,&\frac12\le\lambda\le1.
\end{cases}
\]
In particular, for any sequence of heads with \(\inf\gamma>0\), as \(N\to\infty\) the normalized sharp response converges uniformly to \(\Phi(m/N)\). The profile is continuously differentiable, but not twice differentiable, at \(\lambda=1/2\): its one-sided second derivatives are \(-1\) and \(0\). Below that threshold the limiting optimum saturates the forcing bound on the entire head and on each side of a switch along the path. Above it the path forcing saturates positively, while only the *mean* negative forcing on the head is needed to balance the source.

**Exact finite clique specialization.** If \(H=K_m\), then for every \(m\ge2,p\ge1\),
\[
\mathcal T(K_m,p)=\min_{c\in\mathbb R}\left[(m-1)\left|c+\frac1N\right|+|c|+\sum_{k=1}^p\left|\frac{mk+k(k-1)/2}{N}-c\right|\right].
\]
This is an exact finite expression, evaluated by taking any median of the displayed multiset of \(N\) coefficients. If \(p\to\infty\) and \(m/p\to0\), then \(\mathcal T(K_m,p)/p^2\to1/8\); if \(p\to\infty\) and \(m/p\to\infty\), then \(\mathcal T(K_m,p)/p^2\to1/2\). Thus a large clique at the end of an otherwise long path multiplies the leading *tip* bounded-source amplification by four, relative to a negligible head.

## Assumptions and scope
The path vertices are numbered from the head to the tip; \(1\) has an edge to \(o\), and consecutive path vertices are joined by unit edges. The graph is finite, connected, undirected and unweighted. \(L^\dagger\) is the Moore--Penrose inverse, uniquely characterized by \(Lu=f\) and \(\sum_vu(v)=0\) for mean-zero \(f\). The expression \(\mathcal T\) concerns evaluation at the distinguished path tip, **not** the maximum over all output vertices. The forcing space in this theorem is real; no extension to other norms is claimed.

Only the universal limit along a family of heads requires a uniform gap bound. The exact formula and finite bound hold for each connected head with its actual positive gap. If \(m/N\to\lambda\), the profile holds provided \(\gamma^{-1}m(m+\sqrt m)=o(N^3)\); a uniform positive gap is a transparent sufficient condition.

## Proof
**1. Exact reduction to the path and one head potential.** Put \(F=\sum_{x\in H}f(x)=-\sum_{k=1}^p f(k)\), and set
\[
\eta=f|_H-F\mathbf1_{\{o\}},\qquad v=L_H^\dagger\eta,\qquad\sum_{x\in H}v(x)=0.
\]
Summing the Poisson equation over the vertices of \(H\), the current across the bridge is \(u(o)-u(1)=F\). Consequently, the restriction of \(u=L^\dagger f\) to the head is \(u|_H=a\mathbf1_H+v\) for some \(a\in\mathbb R\). On the path, the last-vertex equation and backwards summation yield the exact increments
\[
u(j)-u(j-1)=\sum_{k=j}^p f(k),\qquad j=1,\ldots,p,
\]
where \(u(0)=u(o)\). Therefore
\[
u(j)=a+v(o)+\sum_{k=1}^p\min(j,k)f(k).
\]
Imposing \(\sum_vu(v)=0\), with \(A_k=\sum_{j=1}^p\min(j,k)=kp-k(k-1)/2\), gives
\[
a=-\frac{p\,v(o)+\sum_{k=1}^p A_kf(k)}{N}.
\]
At the tip we obtain the exact identity
\[
\boxed{u(p)=\sum_{k=1}^p b_k f(k)+\frac mN v(o),\qquad
b_k=\frac{mk+k(k-1)/2}{N}.}
\]
This identity holds for every permissible forcing, with no asymptotic approximation.

**2. Uniform spectral-gap error.** Since \(\eta\) is orthogonal to constants, the spectral theorem on the head gives
\[
|v(o)|\le\|v\|_2\le\frac{\|\eta\|_2}{\gamma}
\le\frac{\sqrt m+m}{\gamma}.
\]
Write \(\mathcal T_0(m,p)\) for the sharp value obtained by omitting the \(v(o)\) term from the boxed identity while retaining **all** constraints on \(f\). Then
\[
|\mathcal T(H,p)-\mathcal T_0(m,p)|\le\frac mN\frac{m+\sqrt m}{\gamma}.
\]
A head forcing with \(m\) components bounded by one can balance precisely those path forcings whose sum is between \(-m\) and \(m\). Equivalently, write the coefficient list as \(m\) zeros followed by \(b_1,\ldots,b_p\). Finite-dimensional linear-programming duality for the cube intersected with the zero-sum hyperplane yields
\[
\boxed{\mathcal T_0(m,p)=\min_{c\in\mathbb R}\left(m|c|+\sum_{k=1}^p|b_k-c|\right).}
\]
For completeness, this dual identity follows from the minimax equality
\[
\sup_{\substack{|f_i|\le1\\\sum_i f_i=0}}\sum_i d_i f_i
=\inf_{c\in\mathbb R}\sup_{|f_i|\le1}\sum_i(d_i-c)f_i
=\inf_c\sum_i|d_i-c|.
\]
A minimizer is a median of the coefficients. At median ties, the sign choices at equal coefficients can be adjusted to give zero total forcing, so the supremum is attained.

**3. Uniform Riemann limit.** Set \(x_k=k/N\) and \(\lambda=m/N\). The normalized coefficients satisfy
\[
\frac{b_k}{N}=B_\lambda(x_k)-\frac{x_k}{2N},\qquad
B_\lambda(x)=\lambda x+\frac{x^2}{2},\quad 0\le x\le1-\lambda.
\]
The function \(B_\lambda\) is nondecreasing and has Lipschitz constant at most one on this interval. With \(c=Nd\), the median formula divided by \(N^2\) differs, uniformly in \(d\in\mathbb R\), by at most \(1/N\) from
\[
\lambda|d|+\int_0^{1-\lambda}|B_\lambda(x)-d|\,dx.
\]
Indeed, replacing each \(b_k/N\) by \(B_\lambda(x_k)\) costs at most \(1/(2N)\) in the normalized sum, and the right-endpoint Riemann-sum error is at most \(1/(2N)\). Taking infima preserves the bound.

The measure whose median is sought has an atom of mass \(\lambda\) at zero and uniform continuous mass on \([0,1-\lambda]\) mapped through the strictly increasing function \(B_\lambda\). If \(\lambda<1/2\), its median occurs at \(x_*=1/2-\lambda\), whereas if \(\lambda\ge1/2\), the median is zero. Thus
\[
\Phi(\lambda)=
\begin{cases}
\displaystyle\int_0^{1-\lambda}B_\lambda(x)\,dx-2\int_0^{1/2-\lambda}B_\lambda(x)\,dx,&\lambda<1/2,\\
\displaystyle\int_0^{1-\lambda}B_\lambda(x)\,dx,&\lambda\ge1/2.
\end{cases}
\]
Elementary integration gives the displayed piecewise cubic. Differentiating on each open branch shows the one-sided second derivatives at one half are distinct. The median also describes the limiting optimizing forcing: when \(\lambda<1/2\), negative signs on the head and on the initial path interval of length \(1/2-\lambda\) balance positive signs thereafter; when \(\lambda>1/2\), all path sites can be positive and a head average \(-(1-\lambda)/\lambda\) balances them. Combining with Step 2 proves the uniform bound and the claimed limit.

**4. Finite clique identity and factor four.** For \(H=K_m\), \(L_H=mI-J\), so \(v(o)=-(1/m)\sum_{x\in H\setminus\{o\}}f(x)\). The exact identity in Step 1 becomes the linear functional with coefficients \(-1/N\) at each of the \(m-1\) other clique vertices, \(0\) at the root, and \(b_k\) on path vertex \(k\). The same median duality proves the exact finite formula.

Furthermore, \(|\mathcal T(K_m,p)-\mathcal T_0(m,p)|<1\) because \(|v(o)|\le(m-1)/m\). If \(m\ge p\), zero is a median of the ideal coefficient list and hence
\[
\mathcal T_0(m,p)=\sum_{k=1}^p b_k
=\frac{p(p+1)}{2N}\left(m+\frac{p-1}{3}\right).
\]
For \(p\to\infty\) with \(m/p\to\infty\), division by \(p^2\) yields \(1/2\). When \(m/p\to0\), the uniform profile gives \(\mathcal T(K_m,p)/p^2\to\Phi(0)=1/8\). The ratio is four.

## Verification
The included standard-library Python program `verify.py` reconstructs the exact Moore--Penrose pseudoinverse as \((L+J/N)^{-1}-J/N\), tests the finite clique median identity against all computed Green rows, independently enumerates zero-sum cube vertices in small dimensions, tests the bridge reduction for multiple nonclique heads, verifies the spectral-gap comparison against known elementary eigenvalues, and checks the continuum Riemann bound and the two limiting regimes. On the final reviewed source it reports 2,271 comparisons passed. The proof above, not the finite checks, establishes the universal assertions.

## Relationship to prior work
Classical graph electrical potential identities and cut-edge hitting-time formulas appear in Palacios, Gómez and Del Río (2014). Beveridge (2015) establishes a general hitting-time representation of discrete Green functions for random walks, with examples including paths and trees. Jonasson (2000) explains why clique-and-path lollipop graphs are natural extremal random-walk geometries. Those general identities and extremal commute-time results are not the present sharp *bounded mean-zero source to pendant-value* optimization, and do not in the examined material yield its piecewise cubic universality for arbitrary uniformly gapped heads. The new point is the optimization of the exact path coefficients under a global balance constraint, the atom-induced median switch, and the quantitative spectral-gap reduction. Spectral characterization of signed lollipop graphs (Belardo and Petecki, 2015) studies a different invariant.

## Limitations
This is a point-evaluation norm at the path tip only. It does not identify the maximizing row of the entire pseudoinverse matrix for arbitrary heads. For heads with spectral gap tending to zero faster than the hypothesis permits, the remainder estimate may be large and universality is not asserted. Exact formulas for all finite nonclique heads would require their full head Green operator. Historical priority remains conditional on the inspected sources: earlier equivalent Green-function/median formulations might exist, especially in literature under endpoint resolvent bounds and optimal balanced forcing.

## References
1. J. Jonasson, *Lollipop graphs are extremal for commute times*, Random Structures & Algorithms **16** (2000), 131--142; first published 2000-02-02. DOI: 10.1002/(SICI)1098-2418(200003)16:2<131::AID-RSA1>3.0.CO;2-3.
2. J. L. Palacios, E. Gómez and M. Del Río, *Hitting Times of Walks on Graphs through Voltages*, Journal of Probability (2014), article 852481, first published 2014-05-20. DOI: 10.1155/2014/852481.
3. A. Beveridge, *A Hitting Time Formula for the Discrete Green's Function*, arXiv:1505.06989v1, posted 2015-05-26; later in Combinatorics, Probability and Computing **25** (2016), 362--379. DOI: 10.1017/S0963548315000152.
4. F. Belardo and P. Petecki, *Spectral characterizations of signed lollipop graphs*, Linear Algebra and its Applications **480** (2015), 144--167. DOI: 10.1016/j.laa.2015.04.022.
