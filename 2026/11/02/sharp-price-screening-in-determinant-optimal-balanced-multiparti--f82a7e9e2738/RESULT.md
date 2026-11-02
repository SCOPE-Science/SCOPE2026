# Sharp price screening in determinant-optimal balanced multipartite networks

## Finding

Fix integers \(r\ge3\) and \(m\ge2\). The vertices of the complete \(r\)-partite graph \(K_{m,\ldots,m}\) are divided into \(r\) parts of size \(m\), one part being distinguished. Every edge incident to the distinguished part has price \(P>0\) per unit conductance; every edge joining two different undistinguished parts has price \(Q>0\). Under the budget \(B>0\), maximize the weighted spanning-tree enumerator \(\mathcal T(w)=\sum_T\prod_{e\in T}w_e\) over **all independent nonnegative edge conductances** with \(\sum_e p_e w_e=B\).

There is a unique global optimizer. Its distinguished-to-ordinary edges all have conductance \(x>0\); its ordinary-to-ordinary edges all have conductance \(y\ge0\). The exact screening threshold is
\[
\Theta_{r,m}=\frac{2m(r-1)}{rm-1},\qquad
\boxed{\ y=0\ \Longleftrightarrow\ Q/P\ge\Theta_{r,m}.\ }
\]
In that regime, the unique optimum is the complete bipartite support \(K_{m,(r-1)m}\), with \(x=B/[m^2(r-1)P]\). For \(Q/P<\Theta_{r,m}\), define
\[
\begin{aligned}
A&=Qm(r-2)(r-1),\\
L&=2P(r-1)[m(r-1)-1]-Q[m(r^2-2)-2r+3],\\
C&=2Pm(r-1)-Q(rm-1)>0.
\end{aligned}
\]
Then all edges are retained and the optimal ratio and weights are
\[
t=\frac{y}{x}=\frac{L+\sqrt{L^2+4AC}}{2A}>0,\qquad
x=\frac{B}{m^2(r-1)[P+(r-2)Qt/2]},\qquad y=tx.
\]
For either regime, the exact optimal value is obtained by inserting these \(x,y\) into
\[
\boxed{\mathcal T(x,y)=(r-1)^{m-1}m^{rm-2}x^m
[x+(r-2)y]^{(r-1)(m-1)}[x+(r-1)y]^{r-2}.}
\]
The combinatorial tree-product identity is an input to the optimization, not an originality claim.

There is also an exact critical-window law. Fix \(r\ge3\), \(P>0\), and \(\gamma\in\mathbb R\), and take \(Q_m/P=2(r-1)/r+\gamma/m\) (positive for sufficiently large \(m\)). If \(t_m=y_m/x_m\) is optimal, then
\[
\boxed{\lim_{m\to\infty}m t_m=
\max\left\{0,\frac1{r-2}-\frac{r^2\gamma}{2(r-1)(r-2)}\right\}.}
\]
Thus the ordinary-to-ordinary conductances vanish across a genuine \(1/m\)-wide relative-price window.

## Assumptions and scope

The graph has \(rm\) labeled vertices and only edges between different parts; in particular, there are no edges internal to any part. The two cost classes contain \((r-1)m^2\) and \(\binom{r-1}{2}m^2\) edges, respectively. All individual conductances, including those in the same price class, are separate decision variables and may be zero. The budget is exactly spent, not bounded above. The objective is the **weighted sum of spanning-tree products**, not the weight of a single maximum or minimum spanning tree. No positive lower bound is imposed on each edge.

## Proof

**1. Existence, connectivity, and uniqueness without assuming class symmetry.** Removing one vertex produces a grounded weighted Laplacian \(L_0(w)=\sum_e w_e b_e b_e^{\mathsf T}\). By the weighted Matrix-Tree Theorem, \(\mathcal T(w)=\det L_0(w)\). The budget polytope is compact. Connected positive-weight choices exist and have \(\det L_0(w)>0\); disconnected choices have determinant zero and cannot optimize. On the convex set of positive-definite grounded Laplacians, \(\log\det\) is strictly concave. The map \(w\mapsto L_0(w)\) is injective for a simple graph: each off-diagonal entry identifies an edge not incident with the grounded vertex, and the remaining diagonal entries then identify the grounded-vertex edge weights. Therefore \(\log\det L_0(w)\) is strictly concave on the connected-support portion of the budget polytope, proving a unique maximizer, including boundary configurations. All permutations inside each part and all permutations of the ordinary parts preserve objective, prices and feasibility. Uniqueness forces invariance under their action, yielding exactly two conductance classes \(x,y\). Since \(x=0\) isolates the distinguished part, \(x>0\).

**2. Complete spectrum and tree product.** Decompose the vertex space orthogonally into internal zero-sum vectors in the distinguished part (dimension \(m-1\)), internal zero-sum vectors in ordinary parts (dimension \((r-1)(m-1)\)), part-constant vectors distinguishing ordinary parts (dimension \(r-2\)), the part-constant special-versus-ordinary contrast (dimension one), and constants (dimension one). The Laplacian eigenvalues on these spaces, in that order, are
\[
(r-1)mx,\quad m[x+(r-2)y],\quad m[x+(r-1)y],\quad rmx,\quad0.
\]
The nonzero eigenvalues have total multiplicity \(rm-1\). Their product divided by \(rm\) is precisely the displayed polynomial \(\mathcal T(x,y)\). This remains valid at \(y=0\), since \(x>0\).

**3. Exact price optimization and screening.** Write \(t=y/x\ge0\). The budget uniquely fixes
\[
x=\frac{B}{m^2(r-1)[P+(r-2)Qt/2]}.
\]
After substituting into the tree polynomial and discarding constants, its logarithm is
\[
F(t)=(r-1)(m-1)\log[1+(r-2)t]+(r-2)\log[1+(r-1)t]
-(rm-1)\log[2P+(r-2)Qt].
\]
A common-denominator calculation gives the **exact derivative identity**
\[
F'(t)=\frac{(r-2)[C+Lt-At^2]}{[1+(r-2)t][1+(r-1)t][2P+(r-2)Qt]},
\]
where \(A,L,C\) have the stated values and \(A>0\).

If \(Q/P<\Theta_{r,m}\), then \(C>0\). The concave quadratic \(C+Lt-At^2\) has exactly one positive root, since its two roots have opposite signs. Thus \(F\) increases and then decreases, so this root gives the unique optimum, with \(t>0\) as claimed.

If \(Q/P\ge\Theta_{r,m}\), then \(C\le0\). At the boundary price \(Q=2Pm(r-1)/(rm-1)\), the linear coefficient reduces to
\[
L=-\frac{2P(r-1)[m^2(r-2)+2m-1]}{rm-1}<0.
\]
The multiplier of \(-Q\) in \(L\), namely \(m(r^2-2)-2r+3\), is positive for all \(r\ge3,m\ge2\). Hence \(L<0\) throughout this regime, so \(F'(t)<0\) for every \(t>0\). The unique optimum is \(t=0\). The threshold equality is included; no third regime is hidden there.

**4. Critical-window calculation.** Write \(q_m=Q_m/P=2(r-1)/r+\gamma/m\), divide \(A,L,C\) by \(P\), and let \(m\) grow with \(r\) fixed. Then
\[
\frac{A}{Pm}\to\frac{2(r-1)^2(r-2)}r,
\qquad\frac{L}{Pm}\to-\frac{2(r-1)(r-2)}r,
\qquad\frac CP\to\frac{2(r-1)}r-r\gamma.
\]
If the last limit is positive, the unique positive quadratic root obeys \(t_m=O(m^{-1})\); multiplying its defining equation \(C+Lt_m-At_m^2=0\) by the appropriate powers of \(m\) proves the positive branch of the limit. If the last limit is negative, the exact screening criterion gives \(t_m=0\) eventually. At equality, \(C=O(m^{-1})\), \(L=-\Theta(m)\), and the positive root, when present, satisfies \(t_m=O(m^{-2})\). These cases give the displayed positive-part expression.

## Verification

Run `python3 verify.py` from the package directory (Python standard library only). The program constructs grounded Laplacians independently and evaluates exact rational determinants; compares them to the spectral tree product on small complete multipartite graphs, including the boundary \(y=0\); and tests the exact derivative-sign polynomial, screening boundaries and numerical positive-root identities across thousands of parameter choices. Its finite tests support, but do not replace, the full symbolic proof above.

For a readable test, \(r=3,m=2\) has the sharp price ratio \(Q/P=8/5\). At or above this ratio, every ordinary-to-ordinary edge is optimally deleted, leaving \(K_{2,4}\) with identical positive cross-edge conductances; at equal prices \(P=Q\), the optimum retains every edge with \(x=y\). In particular, at \(P=1,Q=2,B=8\), the optimum has \(x=1,y=0\) and weighted tree count \(32\), versus \(12\) for the feasible equal-conductance allocation \(x=y=1/2\).

## Relationship to prior work

The weighted Matrix-Tree Theorem and weighted multipartite enumerator formulas are established, including the degree-weighted complete-colorful-complex formulas of Aalipour et al. (2015). In particular, the tree-product identity here is an application of known spectral enumeration techniques and is **not** claimed as new. Khosoussi et al. (2016) give a broader graph-selection framework using log-determinant optimization and a continuous convex relaxation, with general numerical methods but without the stated exact continuous, price-dependent all-dimension solution. Martin and Reiner (2003) treat weighted tree-enumerator factorizations for Cartesian graph products and related families, not this priced multipartite design. The assessed new assertion is the globally unique unrestricted **conductance allocation**, its exact whole-edge-orbit screening threshold, its explicit quadratic positive regime, and its critical scaling—not generic concavity, determinant identities, or graph enumeration.

## Limitations

The result assumes equal part sizes, one distinguished part, precisely two positive linear edge-price classes, and the spanning-tree determinant criterion. It does not cover unequal part sizes, arbitrary independent prices, nonlinear costs, edge-count constraints, arbitrary reliability models, or finite-time dynamical mixing. Although the self-contained proof covers the full stated infinite parameter domain, independent mathematical validation has not been performed. Exhaustive historical priority is not certified; equivalent pricing results under another terminology remain possible.

## References

- G. Aalipour, A. M. Duval, W. Kook, K.-J. Lee, and J. L. Martin, *A weighted cellular matrix-tree theorem, with applications to complete colorful and cubical complexes*, arXiv:1510.00033, first publicly posted 2015-09-30, https://arxiv.org/abs/1510.00033 (especially Theorem 1.2 and Section 4).
- K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116, first publicly posted 2016-04-05, https://arxiv.org/abs/1604.01116 (especially Sections 2, 4.4 and 5).
- J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213, first publicly posted 2003-02-18, https://arxiv.org/abs/math/0302213 (especially Sections 1–3).
