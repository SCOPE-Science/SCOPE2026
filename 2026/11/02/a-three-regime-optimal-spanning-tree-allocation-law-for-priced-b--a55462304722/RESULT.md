# A three-regime optimal spanning-tree allocation law for priced Boolean cubes

## Finding
For every integer \(d\ge3\), set \(m=d-1\). On the Boolean hypercube \(Q_d\), give each edge in one designated coordinate direction price \(P>0\) per unit conductance and each edge in all other directions price \(Q>0\). For a budget \(B>0\), let every edge conductance \(w_e\ge0\) be independently adjustable subject to \(\sum_e p_e w_e\le B\), and maximize the weighted spanning-tree enumerator
\[
\tau(w)=\sum_{T\text{ spanning tree of }Q_d}\prod_{e\in T}w_e.
\]
There is a **unique global optimum**, and it has one conductance \(x_d>0\) on every distinguished-direction edge and a second conductance \(y_d>0\) on every remaining edge. Put \(t_d=x_d/y_d\). It is the unique positive solution of
\[
\left(Pt+mQ\right)\sum_{k=0}^{m}\frac{\binom{m}{k}}{t+k}
=P(2^{m+1}-1).\tag{1}
\]
The exact conductances are
\[
y_d=\frac{B}{2^m(Pt_d+mQ)},\qquad x_d=t_dy_d.\tag{2}
\]
For fixed prices as \(d\to\infty\), these have a sharp three-regime ratio law:
\[
\boxed{\begin{aligned}
P>Q:&\quad\lim_{d\to\infty}\frac{2^d t_d}{d-1}=\frac{Q}{P-Q},\\
P=Q:&\quad t_d=1\quad\text{for every }d,\\
P<Q:&\quad\lim_{d\to\infty}\frac{t_d}{d-1}=\frac{Q}{P}-1.
\end{aligned}}\tag{3}
\]
Thus an expensive coordinate is optimally retained at an exponentially small *relative* conductance, whereas a cheap distinguished coordinate acquires a relative conductance linear in dimension. The asymptotic limits concern fixed positive \(P,Q,B\); the ratio does not depend on \(B\).

## Assumptions and scope
The graph is the simple undirected \(d\)-cube with vertex set \(\{0,1\}^d\), where adjacent vertices differ in exactly one coordinate. A conductance is a nonnegative real variable on each individual edge. Every coordinate direction has \(2^{d-1}=2^m\) edges. The cost is linear, with no upper bound on any individual edge conductance. The objective is the **weighted sum of tree products**, not the maximum weight of a single spanning tree, and not the minimization of total effective resistance. All assertions of uniqueness are for the full, independently weighted edge problem, not just the symmetric two-variable restriction.

## Proof
**1. Existence, saturation and strict uniqueness.** Delete one row and column from the weighted graph Laplacian to obtain its reduced matrix \(L_*(w)\). The weighted matrix-tree theorem gives \(\tau(w)=\det L_*(w)\). The compact budget simplex contains an all-positive assignment and hence has an optimizer with positive determinant. Every positive-determinant assignment has connected support; its reduced Laplacian is positive definite. Scaling all weights up strictly increases \(\tau\), because it is homogeneous of degree \(2^d-1\). Thus every optimum saturates the budget. On the set of connected-support assignments, \(\log\det L_*(w)\) is strictly concave in \(w\): \(\log\det\) is strictly concave on positive definite matrices, and the affine map \(w\mapsto L_*(w)\) is injective. To see injectivity, each edge not incident to the deleted vertex is uniquely determined by its corresponding off-diagonal reduced-Laplacian entry (the cube is simple); the remaining root-incident edge weights are then uniquely determined by the diagonal entries. Therefore two distinct positive-determinant feasible weight vectors have a strict log-determinant improvement at their midpoint. In particular the maximizer is unique even when some initially allowed weights are zero.

**2. Reduction to two uniform classes.** Flipping coordinate bits and permuting the \(m\) ordinary coordinates preserves both the graph and the two-price cost, and acts transitively on the edges of each price class. Uniqueness forces the optimizer to be invariant under this group, hence to have a distinguished weight \(x\) and ordinary weight \(y\). If \(x=0\) the graph splits into two \((d-1)\)-cubes; if \(y=0\), it consists of disconnected matching edges. Both have zero tree enumerator, unlike an all-positive assignment, so \(x,y>0\). The saturated budget reads \(2^m(Px+mQy)=B\).

**3. Exact scalar equation.** Each coordinate edge Laplacian has eigenvalues \(0\) and \(2\) times its weight. The tensor-product Walsh eigenbasis therefore gives the full nonzero spectrum: \(2ky\) for \(1\le k\le m\), with multiplicity \(\binom{m}{k}\), and \(2(x+ky)\) for \(0\le k\le m\), with multiplicity \(\binom{m}{k}\). The weighted matrix-tree theorem gives
\[
\tau(x,y)=\frac{2^{2^d-1}}{2^d}\,y^{2^d-1}
\left(\prod_{k=1}^{m}k^{\binom{m}{k}}\right)
\left(\prod_{k=0}^{m}(t+k)^{\binom{m}{k}}\right),\quad t=x/y.\tag{4}
\]
Inserting \(y=B/[2^m(Pt+mQ)]\), taking logs and differentiating with respect to \(t\) yields
\[
\frac{d}{dt}\log\tau
=\sum_{k=0}^{m}\frac{\binom{m}{k}}{t+k}
-\frac{(2^{m+1}-1)P}{Pt+mQ}.\tag{5}
\]
The derivative is positive near \(t=0\), because the \(k=0\) summand diverges as \(1/t\). It is negative for sufficiently large \(t\), since its first term is asymptotic to \(2^m/t\) and its second to \((2^{m+1}-1)/t\). The strictly concave objective along the affine budget segment, with \(t\) a strictly increasing coordinate along that segment, has exactly one stationary maximizer. This proves (1), (2), and uniqueness of the root. If \(P=Q\), coordinate-exchange symmetry of the entire cube gives \(x=y\) and hence \(t=1\) exactly.

**4. Linear regime for the cheap coordinate.** Let \(K_m\sim\mathrm{Bin}(m,1/2)\) and \(S_m(t)=\sum_{k=0}^m\binom{m}{k}/(t+k)=2^m\mathbb E[(t+K_m)^{-1}]\). For each fixed \(c>0\), the law of large numbers and bounded convergence yield
\[
\frac{mS_m(cm)}{2^m}\longrightarrow\frac1{c+1/2}.
\]
For \(F_m(t)=(Pt+mQ)S_m(t)-P(2^{m+1}-1)\), it follows that
\[
\frac{F_m(cm)}{2^m}\longrightarrow
\frac{Pc+Q}{c+1/2}-2P
=\frac{Q-P-Pc}{c+1/2}.\tag{6}
\]
When \(P<Q\), this limiting sign changes precisely at \(c_*=Q/P-1>0\). Because \(F_m\) has exactly one positive root and its sign is positive before that root and negative afterward, applying (6) at any two constants straddling \(c_*\) gives \(t_d/m\to c_*\).

**5. Exponential regime for the expensive coordinate.** Suppose \(P>Q\). For each fixed \(a>0\), binomial concentration, with the exponentially small event \(K_m=0\) handled separately, gives \(mS_m(a)/2^m\to2\). Consequently
\[
\frac{F_m(a)}{2^m}\longrightarrow\frac{2Q}{1}-2P=2(Q-P)<0.\tag{7}
\]
Thus the unique root \(t_d\) lies below every fixed \(a>0\) for all sufficiently large dimensions, so \(t_d\to0\). Define \(H_m(t)=\sum_{k=1}^{m}\binom{m}{k}/(t+k)\). Binomial concentration also gives
\[
\frac{mH_m(t_d)}{2^m}\longrightarrow2,
\]
because \(t_d\to0\), and on \(k\ge1\) the difference between \((t_d+k)^{-1}\) and \(k^{-1}\) is bounded by \(t_d/k^2\). Split the equation (1) into the \(k=0\) term and the remainder:
\[
P+\frac{mQ}{t_d}
=P(2^{m+1}-1)-(Pt_d+mQ)H_m(t_d).\tag{8}
\]
After division by \(2^{m+1}\), the right side tends to \(P-Q>0\) and the first constant on the left vanishes. Therefore \(mQ/(2^{m+1}t_d)\to P-Q\), equivalently \(2^{m+1}t_d/m\to Q/(P-Q)\). Since \(d=m+1\), this is the first limit in (3). Every asymptotic statement follows from exact finite-dimensional optimality and elementary binomial concentration, not from finite numerical extrapolation.

## Verification
The included dependency-free script `verify.py` independently constructs reduced weighted Laplacians, evaluates exact integer determinants using fraction-free elimination, compares them with formula (4) for cubes of dimensions two through four, checks the exact equal-price binomial identity through dimension 41, locates roots for many dimension/price pairs and checks derivative signs and representative large-dimensional scaling. Run `python3 verify.py` from a directory containing that file. It completed with **566 assertions/grouped checks passed**. The numerical checks are finite witnesses only; equations (6)–(8) and strict concavity provide the all-dimensional proof.

## Relationship to prior work
Martin and Reiner (2003) already gave weighted spanning-tree factorizations for products of complete graphs; Bernardi (2012) further developed the weighted hypercube and rooted-forest enumerations. Formula (4) is an established spectral specialization, **not an independent novelty claim**. Khosoussi and collaborators (2016) analyze tree-connectivity and optimize selection of edges of predetermined weights under combinatorial constraints. The new statement here concerns optimizing every real conductance of a fixed hypercube under per-unit class prices, proving the unique optimum and the exact exponential-versus-linear price asymptotics. Related optimal-conductance problems with cactus support and effective-resistance rather than tree-entropy objectives are not equivalent; in particular an effective-resistance objective has a different expensive-coordinate scaling. This statement is not intended as a claim of exhaustive priority over all possible specialists' formulations.

## Limitations
The result assumes a single distinguished coordinate price and a shared price across all other directions, the unnormalized weighted tree enumerator, and a linear conductance budget. It does not characterize arbitrary per-edge price patterns, control-energy performance, robustness, or numerical conditioning of very small optimal conductances. The exact ratio is implicitly specified by a unique scalar root rather than an elementary closed expression. Related unpublished or unlocated D-optimal design literature might formulate the same optimum.

## References
1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, first public preprint 18 February 2003, https://arxiv.org/abs/math/0302213 .
2. O. Bernardi, *On the spanning trees of the hypercube and other products of graphs*, first public preprint 4 July 2012, https://arxiv.org/abs/1207.0896 .
3. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the weighted number of spanning trees: Near-\(t\)-optimal graphs*, first public preprint 5 April 2016, https://arxiv.org/abs/1604.01116 .
