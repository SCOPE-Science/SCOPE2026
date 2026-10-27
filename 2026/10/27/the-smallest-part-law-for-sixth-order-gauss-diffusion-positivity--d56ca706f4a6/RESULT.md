# The smallest-part law for sixth-order Gauss diffusion positivity on complete multipartite graphs

## Finding

Consider any connected unweighted complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), where \(r\ge2\), every part size \(n_i\) is a positive integer, and \(N=\sum_i n_i\). Let \(L\) be the combinatorial Laplacian and let \(T(h)\) be the *completed* three-stage, sixth-order Gauss–Legendre Runge–Kutta step for \(y'=-Ly\):
\[
T(h)=P(hL)Q(hL)^{-1},\quad P(z)=120-60z+12z^2-z^3,\quad Q(z)=120+60z+12z^2+z^3.
\]
Put \(R(z)=P(z)/Q(z)\), \(m_* = \min_i n_i\), and, for each integer \(1\le m<N\), define
\[
F_{N,m}(h)=\frac1N+\left(\frac1m-\frac1N\right)R(Nh)+\left(1-\frac1m\right)R((N-m)h).
\]
If \(N\ge3\), every \(F_{N,m}\) decreases strictly from \(1\) at \(h=0\) to \(2/N-1<0\) as \(h\to\infty\), so it has one and only one positive root \(H_{N,m}\). The exact entrywise positivity criterion is
\[
\boxed{T(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad 0\le h\le H_{N,m_*}.}
\]
For every \(h>0\), *all off-diagonal entries* are strictly positive. The first zeros at \(H_{N,m_*}\) occur precisely on the diagonals of vertices belonging to smallest parts; those entries remain strictly negative for all larger \(h\). Thus the sharp threshold depends on the total order and the smallest part size alone, not on the rest of the partition. For fixed \(N\), \(H_{N,m}\) increases strictly with \(m\). In the degenerate case \(N=2\), the graph is \(K_2\) and \(T(h)\) is entrywise positive for all finite \(h>0\). For every graph in the family and every \(h\ge0\), \(T(h)\) is symmetric, doubly stochastic, and satisfies \(\|T(h)\|_{2\to2}=1\), whether or not its diagonal is nonnegative.

## Assumptions and scope

All graphs are finite, simple, connected, unweighted and undirected. Parts are nonempty, with at least two parts. The Laplacian has diagonal vertex degrees and off-diagonal \(-1\) on edges. Nonnegativity concerns the *completed* one-step matrix, not internal Runge–Kutta stages or nonlinear equations. The result covers all real timesteps \(h\ge0\), not just small-step behavior. No sign claim is made for arbitrary weighted or directed graphs or for non-complete-multipartite graphs.

## Proof

**1. Exact projectors.** Let \(E\) be the orthogonal projector onto vectors constant on each part, so that its block for a part of size \(m\) is \(J_m/m\). Let \(J\) denote the all-ones matrix. The orthogonal Laplacian eigenspaces are: constants with projector \(J/N\) and eigenvalue \(0\); part-constant vectors orthogonal to constants with projector \(E-J/N\) and eigenvalue \(N\); and within-part fluctuations for part \(i\), with projector \(I_{n_i}-J_{n_i}/n_i\) and eigenvalue \(N-n_i\). These are pairwise orthogonal and sum to the identity. All positive eigenvalues are in \(\{N,N-n_1,\ldots,N-n_r\}\).

Consequently, for a vertex \(u\) in a part of size \(m\), the diagonal entry is exactly \(F_{N,m}(h)\). For distinct vertices \(u,v\) in different parts,
\[
T(h)_{uv}=\frac{1-R(Nh)}{N}=h\,g(Nh),\qquad g(z)=\frac{1-R(z)}z=\frac{2(z^2+60)}{z^3+12z^2+60z+120}.
\]
For distinct vertices \(u,v\) in the same part of size \(m\),
\[
T(h)_{uv}=\frac{1-R(Nh)}{N}+\frac{R(Nh)-R((N-m)h)}m
=\frac{(N-m)h}{m}\bigl(g((N-m)h)-g(Nh)\bigr).
\]
These identities hold also for singleton parts, in which the last entry type is absent.

**2. Scalar sign certificates.** For every \(z\ge0\), \(Q(z)>0\). Direct differentiation gives the identities
\[
R'(z)=-\frac{24\big((z^2-15)^2+375\big)}{Q(z)^2}<0,
\qquad
g'(z)=-\frac{2(z^4+120z^2+1200z+3600)}{Q(z)^2}<0.
\]
Also \(1-R(z)=2z(z^2+60)/Q(z)>0\) for \(z>0\), and \(1+R(z)=24(z^2+10)/Q(z)>0\) for finite \(z\ge0\). Therefore \(-1<R(z)<1\) for \(z>0\). Both displayed off-diagonal entries are strictly positive for every \(h>0\), since \(0<N-m<N\) and \(g\) is strictly decreasing. Symmetry and preservation of constants follow from the spectral functional calculus; the eigenvalue \(1\) on constants together with \(|R(z)|<1\) for positive \(z\) yields exactly \(\|T(h)\|_{2\to2}=1\) for all \(h\ge0\).

**3. Unique diagonal crossing.** The three nonnegative coefficients in \(F_{N,m}\) are spectral weights summing to one:
\[
\mu_m=\frac1N\delta_0+\frac{N-m}{Nm}\delta_N+\frac{m-1}{m}\delta_{N-m}.
\]
For every \(1\le m<N\), at least the coefficient of \(R(Nh)\) is positive. Since \(R'\) is strictly negative, \(F_{N,m}(h)\) strictly decreases in \(h\). It starts at \(1\) and, as \(R(z)\to-1\) for \(z\to\infty\), tends to \(2/N-1\). If \(N\ge3\), there is exactly one positive crossing; if \(N=2\), the only possible part size is one and \(F_{2,1}(h)=(1+R(2h))/2>0\) for finite \(h\).

**4. The smallest-part law.** Fix \(N\) and let \(1\le m_1<m_2<N\). The distributions \(\mu_{m_1}\) and \(\mu_{m_2}\) give the same mass \(1/N\) to zero. Their remaining masses lie at \(N-m_j\) and \(N\). The lower nonzero support point \(N-m_1\) is larger than \(N-m_2\), while the mass at \(N\), equal to \((N-m)/(Nm)\), is strictly larger for \(m_1\). Comparing upper tails on the three intervals divided by \(N-m_2\), \(N-m_1\), and \(N\) proves that \(\mu_{m_1}\) strictly first-order stochastically dominates \(\mu_{m_2}\). Because \(z\mapsto R(hz)\) decreases strictly for each \(h>0\),
\[
F_{N,m_1}(h)<F_{N,m_2}(h)\qquad (h>0).
\]
The earliest diagonal zero therefore occurs exactly in the parts of minimum size, and their diagonal entries are strictly negative thereafter. This proves all assertions.

**5. Same-order structural witness.** At six vertices and timestep \(h=4\), the graph \(K_{2,2,2}\) has diagonal entry \(-66473/957799<0\), while \(K_{3,3}\) has diagonal entry \(1999/166291>0\). All off-diagonal entries in both graphs are positive. Thus equal graph order does not alone determine the positivity boundary; the smallest part does.

## Verification

The accompanying `verify.py` symbolically checks the displayed rational and derivative identities with SymPy, constructs the independent rational matrix quotient on 87 complete multipartite graphs of orders two through nine, checks 14,925 exact transition-entry identities at three rational timesteps per graph, verifies symmetry, stochastic row sums and strict positivity of all off-diagonal entries, and checks smallest-part ordering. Execute `python verify.py` with the version requirement in `requirements.txt`. All matrix comparisons are exact rational equalities and cannot establish the infinite-family theorem; the analytical projector and scalar-sign proof above does.

## Relationship to prior work

Gottlieb, Shu and Tadmor developed and analyzed strong-stability-preserving high-order time discretizations, including limitations for implicit schemes. Conde, Gottlieb, Grant and Shadid studied high-linear-order implicit SSP methods. Blanes, Iserles and Macnamara investigated positivity for graph-Laplacian dynamics and explicitly identified positivity of higher-order diagonal Padé approximations as a challenge. These works address general methods or different positivity constructions; the present claim gives exact completed-step signs on a specific all-size graph family, not a universal SSP property. Sixth-order Gauss–Legendre is the diagonal \([3/3]\) Padé stability map, and its graph-specific finite positivity horizon should not be conflated with A-stability or with fourth-order \([2/2]\) results.

## Limitations

No claim is made that a negative diagonal implies a large solution error: this is a structural nonnegativity test rather than an accuracy bound. Intermediate-stage positivity is not established. The result does not cover weighted edges, general graph Laplacians, nonlinear models, or changes of time integrator. The literature comparison can miss unindexed specialized statements; the work has not undergone independent mathematical review.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43(1) (2001), 89–112, DOI: 10.1137/S003614450036757X. Public full text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download (first electronically published 2001-02-02, printed in the source).
2. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242 (first submitted 2021-02-16), https://arxiv.org/html/2102.08242v2.
3. S. Conde, S. Gottlieb, Z. J. Grant and J. N. Shadid, *Implicit and Implicit-Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order*, arXiv:1702.04621 (first submitted 2017-02-15), https://arxiv.org/abs/1702.04621.
4. C. Song and S. Eisenträger, *High-order implicit time integration scheme based on Padé expansions*, arXiv:2103.12282 (first submitted 2021-03-23), https://arxiv.org/abs/2103.12282. Discusses high-order Padé time integration but not the graph-specific positivity classification.
