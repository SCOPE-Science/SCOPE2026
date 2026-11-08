# A four-vertex stability threshold for affine projection on \(K_{m,n,1}\)

## Finding

Let \(m,n\ge 2\) be integers. Make each edge of the complete tripartite graph \(G=K_{m,n,1}\) a unit interval with arclength measure, and let \(P\) be the real \(L^2(G)\)-orthogonal projector onto globally continuous, edgewise-affine functions. Write \(p=\min(m,n)\), \(q=\max(m,n)\), and
\[
D=(p+q+1)(pq+p+q),\quad
u=\frac{p^2+pq-p+q+1}{(p+1)D},\quad
v=\nu+\frac3{p+1},\quad
x=\frac{2p+2q-1}{D},\quad
y=\frac{2q+2-p}{D},
\]
where all four quantities \(\nu,v,x,y\) are positive. Define \(\Phi(a,b)=(a^2+b^2)/(2(a+b))\) for positive \(a,b\). Then the *sharp*, attained operator norm is
\[
\boxed{\|P\|_{L^\infty\to L^\infty}
=p\Phi(v,x)+p(q-1)\Phi(\nu,x)+\Phi(v,y)
+(q-1)\Phi(\nu,y)+\frac p2(x+y).}
\]
The only norming evaluation points are the vertices in the part(s) of size \(q\). The singleton vertex and every edge-interior point are strictly nonnorming. The amplification crosses two at a universal discrete threshold:
\[
\boxed{\|P\|<2\quad\text{if }q\le3,\qquad
\|P\|>2\quad\text{if }q\ge4.}
\]
For every fixed \(p\ge2\), one has \(\lim_{q\to\infty}\|P\|=7/3\).

## Assumptions and scope

The graph is finite, simple, has exactly three independent vertex classes of sizes \(p,q,1\), and has all cross-class edges of unit length. It carries non-normalized arclength measure and no vertex atoms. Every edge is one affine element; no derivative matching is imposed. The domain and codomain are real \(L^\infty(G)\). The named theorem is for \(p,q\ge2\), with \(p\le q\). The boundary where a nonsingleton class has size one belongs to a previously studied complete-split family and is not claimed new.

## Proof

For each graph vertex \(j\), let \(\phi_j\) be its continuous nodal hat function. The mass/Gram matrix is \(M_{jj}=\deg(j)/3\), \(M_{ij}=1/6\) for adjacent distinct vertices, and zero otherwise. It is positive definite because the hats are linearly independent. Its inverse gives the reproducing kernel at a point \(z\): \(K_z(t)=\sum_{i,j}\phi_i(z)(M^{-1})_{ij}\phi_j(t)\). Therefore the evaluation norm is \(E(z)=\int_G|K_z(t)|\,dt\), and \(\|P\|=\max_zE(z)\).

For the three class-constant subspace (in the ordered classes of sizes \(p,q,1\)), the mass operator has matrix
\[
Q=\begin{pmatrix}
(q+1)/3&q/6&1/6\\
p/6&(p+1)/3&1/6\\
p/6&q/6&(p+q)/3
\end{pmatrix}.
\]
On zero-sum fluctuations of the two nonsingleton classes the eigenvalues are \((q+1)/3\) and \((p+1)/3\). Inverting these three invariant summands gives, in the row of a distinguished vertex \(b\) in the size-\(q\) part, the coefficients \(v\) at \(b\), \(\nu\) at each other size-\(q\) vertex, \(-x\) at each of the \(p\) vertices of the other nonsingleton part, and \(-y\) at the singleton. Direct substitution into the three-class inverse together with the fluctuation terms verifies these expressions.

On an edge, the kernel linearly interpolates its endpoint values. For \(a,b>0\), \(\int_0^1|a(1-t)-bt|\,dt=\Phi(a,b)\); same-sign endpoints integrate to their absolute arithmetic mean. The edges split into five groups: \(p\) edges from \(b\) to the size-\(p\) class, \(p(q-1)\) edges from the other size-\(q\) vertices to that class, one edge from \(b\) to the singleton, \(q-1\) others to the singleton, and \(p\) edges between the size-\(p\) class and singleton. Integrating gives precisely the boxed formula.

It remains to prove that this largest-part row dominates all other evaluation rows. Denote the other nonsingleton-part row norm by \(E_A\), the singleton row norm by \(E_C\), and the displayed larger-part row norm by \(E_B\). All row coefficients are obtained by the displayed block inversion. Their signs are fixed except the cross coefficient between the smaller part and the singleton, whose sign changes at \(q=2p+2\). Use the same two elementary absolute-linear integration identities to obtain rational expressions for \(E_A,E_B,E_C\) in two regions: \(p\le q\le 2p+2\) and \(q\ge2p+2\).

Here is an *exact algebraic positivity certificate* rather than a numerical sampling argument. In the first region substitute \(p=1+h,q=1+h+k\) (\(h,k\ge0\)). Clearing the explicit positive denominators gives \(E_B-E_A=kA(h,k)/D_A(h,k)\) and \(E_B-E_C=(h+k)C(h,k)/D_C(h,k)\), where all nonzero coefficients of the four polynomials \(A,C,D_A,D_C\) are strictly positive. In the second region substitute \(p=1+h,q=4+2h+k\); after clearing the positive denominators, both differences are quotients of polynomials with strictly positive nonzero coefficients (no vanishing factor). The supplied exact symbolic checker constructs these identities directly from the three-by-three inverse and verifies every coefficient, without substituting bounded numerical parameter ranges. Consequently \(E_B\ge E_A\), with equality exactly when \(p=q\); for \(p,q\ge2\), \(E_B>E_C\).

For a point interior to an edge \([a,b]\), the kernel is \((1-t)K_a+tK_b\), so \(E((1-t)a+tb)\le(1-t)E(a)+tE(b)\). Except when \(p=q\), at least one endpoint lies outside the norming size-\(q\) part, giving strict inequality. If \(p=q\), the only edges with both endpoints norming join the two nonsingleton parts; their two endpoint kernels have opposite signs on a positive-length interval near that edge's endpoint because the corresponding inverse Gram entry is strictly negative. Hence the \(L^1\) triangle inequality is strict for every interior point on those edges. This proves the complete norming-location classification.

For the sharp threshold, when \(q\le3\), the three possibilities \((p,q)=(2,2),(2,3),(3,3)\) give, respectively, \(157069/82250\), \(386261/195130\), and \(2013509/1014741\), each below two. For \(q\ge4\), the same symbolic certificate proves \(E_B-2>0\): if \(p\ge4\), substitute \(p=4+h,q=4+h+k\); if \(p\in\{2,3\}\), substitute \(q=4+k\). In each case the exact rational numerator and denominator have strictly positive nonzero polynomial coefficients. Finally, taking the ordinary rational-function limit in the displayed formula as \(q\to\infty\) with \(p\) fixed yields \(7/3\).

For completeness, all norm-attaining unit-bounded inputs have an explicit description: choose a norming vertex \(b\), take \(f=\pm\operatorname{sgn}K_b\) almost everywhere, and optionally change it on null sets. Necessity follows from equality in the integral triangle inequality at a norming evaluation vertex. On each edge, the required sign changes occur exactly at the zero of the linear interpolant of the corresponding coefficient pair; the five edge groups above give every such pair.

## Verification

Run `python verify_tripartite_affine_projection.py` with SymPy installed (see `requirements.txt`). It performs exact symbolic inversion, constructs both competing-row sign-region formulas, verifies positive-coefficient certificates for the four strict comparisons and all threshold regimes, and independently inverts dense rational Gram matrices on 28 small parameter pairs to integrate every edge kernel exactly. The coefficient certificates are universal polynomial identities; the 28 finite matrices are separate consistency checks, not proofs of the infinite assertion.

## Relationship to prior work

Passenbrunner's 2011 full text computes endpoint projection norms for periodic degree-one splines on a circle using inverse Gram matrices, not for the stated tripartite metric networks. Oswald's 2006 full text constructs unbounded norms on two-dimensional simplicial triangulations, not the one-dimensional metric-graph family considered here. Both supply mathematical motivation, not novelty certificates. Earlier available graph-projection results treat complete bipartite networks (including higher-degree vertex evaluation), balanced multipartite networks, complete-split networks, and a general bound below three. None of those statements implies the present sharp formula and size-four threshold for graphs with two nonsingleton independent parts and one singleton. The existing complete-split boundary cases are deliberately excluded. A related 2006 weighted finite-element study by Boman was available only through its abstract; any unindexed equivalent result remains a residual originality risk.

## Limitations

Only real continuous edgewise-affine \(L^2\) projection, unit edges, uniform arclength, and exactly three parts of sizes \(p,q,1\) with \(p,q\ge2\) are covered. This does not classify other unbalanced multipartite graphs, variable edge lengths, vertex atoms, or higher-degree splines. The algebraic certificates depend on exact symbolic manipulation (SymPy) and have not undergone independent external review. The earlier finite-graph variants are used only for mathematical comparison, not to claim any exhaustive literature novelty.

## References

1. Peter Oswald, *A counterexample concerning the L2-projector onto linear spline spaces*, arXiv:math/0611573, first posted 2006-11-19, https://arxiv.org/abs/math/0611573 (full original text inspected).
2. Markus Passenbrunner, *The Lebesgue Constant for the Periodic Franklin System*, arXiv:1103.1950, first posted 2011-03-10, https://arxiv.org/abs/1103.1950 (full original text inspected).
3. Mats Boman, *Estimates for the L2-Projection onto Continuous Finite Element Spaces in a Weighted Lp-Norm*, BIT Numerical Mathematics 46 (2006), 249–260, doi:10.1007/s10543-006-0062-3 (abstract only; unexamined full-text risk).
