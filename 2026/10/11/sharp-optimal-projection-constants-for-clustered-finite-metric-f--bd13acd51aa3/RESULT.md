# Sharp optimal projection constants for clustered finite metric free spaces

## Finding
Let \(M=A_1\sqcup\cdots\sqcup A_k\) be a finite metric space with \(k\ge2\), \(|A_i|=m_i\ge1\), and at least one nonsingleton cluster. Distances within the \(i\)-th cluster are \(r_i\in(0,1]\), and distances between distinct clusters are \(1\). Put
\[w_i=r_i\left(1-\frac1{m_i}\right),\qquad w_{(1)}\ge w_{(2)}\]
for the two largest of these numbers. Let \(U\) be the subspace of the real Lipschitz-free space \(\mathcal F(M)\) spanned by differences of points in the same cluster. Its **relative projection constant**, optimized over every linear projection onto \(U\), is
\[\boxed{\lambda(U,\mathcal F(M))=\max\{1,w_{(1)}+w_{(2)}\}.}\]
A minimizing projection is obtained by subtracting the mean mass on each cluster. Its complementary projection onto the cluster-uniform subspace has norm exactly one. Thus this canonical direct-sum decomposition is bimonotone precisely when \(w_{(1)}+w_{(2)}\le1\).

For two clusters with the same size \(m\ge2\) and same within-cluster distance \(r\), the exact constant is \(\max\{1,2r(1-1/m)\}\). For \(m\ge3\), its threshold for one-complementability is \(r\le m/(2m-2)\). Taking \(r\) arbitrarily near \(1\) and \(m\) large gives optimal projection norms arbitrarily close to \(2\), while no finite instance reaches \(2\).

## Assumptions and scope
All scalars are real. The metric is defined by \(d(x,y)=r_i\) for distinct \(x,y\in A_i\) and \(d(x,y)=1\) for \(x\in A_i,y\in A_j,i\ne j\). Since \(0<r_i\le1\), the triangle inequality holds. Singleton clusters contribute \(w_i=0\). At least one nonsingleton cluster ensures that \(U\ne\{0\}\); at least two clusters ensure a nontrivial complementary range.

Identify \(\mathcal F(M)\) with signed real measures \(\mu\) of total mass zero, with the transportation/Kantorovich--Rubinstein norm
\[\|\mu\|=\sup\bigl\{\textstyle\sum_{x\in M}\mu(x)f(x):|f(x)-f(y)|\le d(x,y)\ \forall x,y\bigr\}.\]
Constants in \(f\) make no difference because \(\mu\) has zero total mass. Write \(e_x\) for the unit mass at \(x\), and \(\overline e_i=m_i^{-1}\sum_{z\in A_i}e_z\). The relative projection constant is
\[\lambda(U,\mathcal F(M))=\inf\{\|R\|:R^2=R,\ \operatorname{ran}R=U\}.\]

## Proof
**Step 1: the canonical splitting.** Define the cluster-averaging operator on mass-zero measures by
\[Q\mu=\sum_{i=1}^k\mu(A_i)\overline e_i,\qquad P\mu=\mu-Q\mu.\]
Clearly \(Q^2=Q\), \(P^2=P\), and \(\operatorname{ran}P=U\). Moreover the range \(V\) of \(Q\) consists precisely of cluster-uniform mass-zero measures, and \(\mathcal F(M)=U\oplus V\).

Let \(G=\prod_{i=1}^k\mathfrak S(A_i)\) act on signed measures by permutation of coordinates. Each permutation preserves the metric and induces a linear isometry \(T_g\) of the free space. The average \(|G|^{-1}\sum_{g\in G}T_g\) equals \(Q\), so \(\|Q\|\le1\). Because \(k\ge2\), \(V\ne\{0\}\), whence \(\|Q\|=1\).

**Step 2: exact norm of the complementary projection.** The unit ball of \(\mathcal F(M)\) is the convex hull of the normalized molecules \((e_x-e_y)/d(x,y)\) for distinct points. Hence \(\|P\|\) is the maximum norm of its values on these molecules. If \(x,y\in A_i\) are distinct, then \(Q(e_x-e_y)=0\), so \(P\) fixes the normalized molecule and the output norm equals \(1\).

For \(x\in A_i,y\in A_j\) with \(i\ne j\), the input molecule is \(e_x-e_y\), and
\[P(e_x-e_y)=(e_x-\overline e_i)-(e_y-\overline e_j).\]
For a point \(x\in A_i\), the decomposition
\[e_x-\overline e_i=\frac1{m_i}\sum_{z\in A_i\setminus\{x\}}(e_x-e_z)\]
proves \(\|e_x-\overline e_i\|\le r_i(1-1/m_i)=w_i\). The triangle inequality gives \(\|P(e_x-e_y)\|\le w_i+w_j\).

For the reverse inequality choose a potential \(f\) whose values are \(r_i\) at \(x\), zero at all other points of \(A_i\), zero at \(y\), \(r_j\) at all other points of \(A_j\), and zero outside these two clusters. Each within-cluster oscillation is at most its allowed radius; all values are in \([0,1]\), so cross-cluster differences are at most \(1\). Thus \(f\) is one-Lipschitz, and its pairing with the displayed output is exactly \(w_i+w_j\). Consequently
\[\|P(e_x-e_y)\|=w_i+w_j\quad(i\ne j).\]
As some within-cluster molecule exists, maximizing over all molecule types gives
\[\|P\|=\max\bigl\{1,\max_{i\ne j}(w_i+w_j)\bigr\}=\max\{1,w_{(1)}+w_{(2)}\}.\]

**Step 3: optimality among all projections.** The group representation leaves both \(U\) and \(V\) invariant. Every vector of \(V\) is fixed by \(G\). Conversely, the only \(G\)-fixed vector of \(U\) is zero: a mass-zero vector supported in each cluster with zero cluster sum and invariant under its full permutation group must vanish on that cluster.

Let \(R\) be any projection onto \(U\), with no symmetry assumption. Symmetrize it:
\[R_G=\frac1{|G|}\sum_{g\in G}T_gRT_g^{-1}.\]
Because \(U\) is invariant, \(R_G\) is again a projection onto \(U\), and \(\|R_G\|\le\|R\|\). It commutes with \(G\). For any \(v\in V\), its image \(R_Gv\in U\) is fixed by \(G\), so \(R_Gv=0\). On \(U\), \(R_G\) is the identity. It follows from \(\mathcal F(M)=U\oplus V\) that \(R_G=P\). Therefore \(\|R\|\ge\|P\|\) for every projection onto \(U\), proving the claimed exact relative projection constant and completing the theorem.

## Verification
All inequalities in the proof hold for arbitrary finite \(k\), positive cluster sizes, and radii \(0<r_i\le1\); no limiting or probabilistic argument is required. Exact-rational finite checks of \(263\) molecule/certificate cases across ten heterogeneous cluster configurations, including both sides of the bimonotonicity threshold, are supplied in `check_projection.py`. Run it with `python3 check_projection.py`. These checks verify the explicit upper decomposition and dual witnesses on those examples but are not used as a substitute for the general proof.

## Relationship to prior work
Cúth and Doucha, *Projections in Lipschitz-free spaces induced by group actions* (first public arXiv version 23 April 2021), establish general norm-one averaging projections onto invariant free-space subspaces. That explains the norm-one map \(Q\) but does not give the optimized norm of the complementary projection onto within-cluster fluctuations. In particular, existence of a contractive invariant-range projection does not imply contractivity of its complement: for two clusters of size \(3\), each with within-cluster distance \(1\), the minimum complementary projection norm is \(4/3\).

Dilworth, Kutzarova and Ostrovskii, *Lipschitz free spaces on finite metric spaces* (first public version 10 July 2018), prove large well-complemented finite-metric subspaces and employ averaging of projections in graph-related representations, but the compared results do not state this cluster-fluctuation subspace invariant or its sharp radius/cardinality threshold. The finding determines the minimum over **all** projections, not only the norm of a chosen group average.

## Limitations
The theorem concerns a specified family of finite, clustered equilateral metrics and the specified within-cluster fluctuation subspace. It neither computes absolute projection constants in arbitrary ambient superspaces nor claims a universal formula for nonhomogeneous within-cluster metrics. The source comparisons do not rule out an equivalent formulation in unindexed literature. Independent mathematical audit has not been performed.

## References
- S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first public 10 July 2018), https://arxiv.org/abs/1807.03814.
- M. Cúth, M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519 (first public 23 April 2021), https://arxiv.org/abs/2104.11519.
