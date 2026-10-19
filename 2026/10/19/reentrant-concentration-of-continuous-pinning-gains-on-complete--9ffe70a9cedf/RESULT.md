# Reentrant concentration of continuous pinning gains on complete bipartite networks

## Finding

For every pair of integers \(p\ge q\ge2\), consider the unit-weight complete bipartite graph \(K_{p,q}\). Allocate arbitrary nonnegative feedback gains \(g_v\) to its vertices under \(\sum_vg_v=B>0\), and minimize
\[
 J(g)=\operatorname{tr}\bigl[(L_{K_{p,q}}+\operatorname{diag}(g))^{-1}\bigr].
\]
The optimizer is globally unique, even when all vertex gains are individually adjustable. It allocates a common gain \(x>0\) to each of the \(p\) vertices in the larger part and a common gain \(y\ge0\) to each of the \(q\) vertices in the smaller part. Define
\[
 H_{p,q}(z)=z^3+2(q+1)z^2+(p+q^2+4q-p^2)z+2q^2.
\]
**Exact support test:** the optimizer has \(y=0\) (and \(x=B/p\)) if and only if \(H_{p,q}(B/p)\le0\). Otherwise, it has \(x,y>0\) and is uniquely specified by the budget constraint and the explicit marginal-value equation below.

There is a complete algebraic classification of *reentrant concentration*. Put
\[
 R_q(u)=u^2+2(q+1)u+q^2+4q+2q^2/u,\qquad u>0,
\]
and let \(u_q>0\) be the unique root of \(u_q^3+(q+1)u_q^2=q^2\). When \(p^2-p>R_q(u_q)\), there are exactly two simple positive roots \(z_-<z_+\) of \(H_{p,q}\). Gains are strictly positive in *both* parts at low and high budgets, but every vertex in the smaller part receives zero gain precisely for
\[
 pz_-\le B\le pz_+.
\]
If equality \(p^2-p=R_q(u_q)\) holds, concentration occurs only at \(B=pu_q\). If \(p^2-p<R_q(u_q)\), both parts always receive positive gains. In particular, for \(K_{6,2}\), concentration holds exactly between two budgets approximately \(3.34679965326\) and \(10.3824948581\). Thus at budgets \(B=1,5,20\) the unique optima respectively pin both parts, the six-vertex part only, and both parts again.

## Assumptions and scope

The graph has \(p\ge q\ge2\) labelled vertices in each respective part, unit conductance on every cross edge and none within a part. Gains \(g_v\ge0\) are continuously divisible, have unit cost, and satisfy the exact budget \(B>0\); there is no per-node upper bound and no integer leader-count constraint. The Laplacian is the ordinary combinatorial Laplacian. Since the graph is connected and \(\sum_vg_v>0\), its pinned Laplacian is positive definite. The objective is inverse trace, not the second Laplacian eigenvalue, sum of effective resistances, or combinatorial leader count. For independent unit-intensity additive Brownian noise in \(dX=-(L+\operatorname{diag}g)X\,dt+\sigma dW\), stationary total variance equals \(\sigma^2J(g)/2\). There is no claim for heterogeneous edge weights, heterogeneous noise, directed networks, or nonlinear feedback.

## Proof

**1. Existence and unrestricted uniqueness.** Put \(M(g)=L+\operatorname{diag}(g)\). For \(B>0\) the feasible simplex is compact and \(M(g)\succ0\). With \(S=M(g)^{-1}\), the second directional derivative of inverse trace in direction \(D=\operatorname{diag}(h)\) is
\[
 \frac{d^2}{dt^2}\operatorname{tr}(M+tD)^{-1}\bigg|_{t=0}=2\operatorname{tr}(SDSDS)>0
\]
for every nonzero real diagonal \(D\), since it is a positive-weighted trace of the square of the nonzero symmetric matrix \(S^{1/2}DS^{1/2}\). Hence \(J\) is strictly convex and admits a unique minimizer. Permuting vertices independently within each part preserves both constraints and objective; uniqueness forces the optimizer to be constant within each part. This is a consequence of unrestricted optimization, not a symmetry assumption.

**2. Exact trace.** Write the partwise gains as \(x,y\) with \(px+qy=B\), and put
\[
 a=q+x,\quad b=p+y,\quad \Delta=ab-pq=px+qy+xy>0.
\]
The subspaces of vectors summing to zero separately in the parts contribute eigenvalues \(a\) (multiplicity \(p-1\)) and \(b\) (multiplicity \(q-1\)). On normalized part-constant vectors the remaining symmetric block is
\[
 \begin{pmatrix}a&-\sqrt{pq}\\-\sqrt{pq}&b\end{pmatrix}.
\]
Consequently
\[
 J(x,y)=\frac{p-1}{a}+\frac{q-1}{b}+\frac{a+b}{\Delta}.
\]
This formula also determines the exact minimum after the unique optimizer is specified.

**3. The larger part is always pinned.** At the face \(x=0\) write \(y=B/q\). Along the feasible direction increasing \(x\) with \(dy/dx=-p/q\), direct differentiation gives
\[
 \left.\frac{dJ}{dx}\right|_{x=0}=-\frac{pN}{Bq^2(B+pq)^2},
\]
where
\[
 \begin{aligned}
 N={}&B^3+2B^2pq+2B^2q+Bq^2(p^2-q^2)\\
 &+4Bpq^2+Bq^3+2p^2q^3>0.
 \end{aligned}
\]
All terms are nonnegative and some are strictly positive for \(p\ge q\ge2\), so \(x=0\) cannot be optimal.

**4. The exact KKT threshold.** At the opposite face \(y=0\), put \(x=B/p=z\). Differentiate along increasing \(y\) with \(dx/dy=-q/p\). Direct algebra yields
\[
 \left.\frac{dJ}{dy}\right|_{y=0}=-\frac{qH_{p,q}(z)}{p^2z(z+q)^2}.
\]
The one-variable restriction \(y\mapsto J((B-qy)/p,y)\) is strictly convex on \([0,B/q]\), with strictly negative derivative at its upper endpoint by step 3. It follows that its unique minimum is at \(y=0\) exactly when the derivative there is nonnegative, i.e. \(H_{p,q}(B/p)\le0\). Otherwise it is interior.

For the interior case define the per-budget-unit marginal gains
\[
 F_A=\frac{p-1}{p a^2}+\frac{b^2+pq}{p\Delta^2},\qquad
 F_B=\frac{q-1}{q b^2}+\frac{a^2+pq}{q\Delta^2}.
\]
The unique optimizer \((x,y)\) is the positive solution to \(px+qy=B\) and \(F_A=F_B\). Indeed \(\partial J/\partial x=-pF_A\) and \(\partial J/\partial y=-qF_B\); strict convexity gives existence and uniqueness. Bisection on \(y\in(0,B/q)\) using \(F_A-F_B\) computes it with arbitrary desired precision.

**5. Number of support transitions.** For \(z>0\) rearrangement of the cubic gives
\[
 H_{p,q}(z)<0\quad\Longleftrightarrow\quad p^2-p>R_q(z).
\]
Now \(R_q''(z)=2+4q^2/z^3>0\), and \(R_q\) diverges as \(z\to0^+\) and \(z\to\infty\). Its derivative vanishes at the unique \(u_q>0\) specified above. Horizontal-level geometry therefore gives zero, one double, or two simple positive roots according as \(p^2-p\) is below, equal to, or above \(R_q(u_q)\). This proves all phase boundaries, including equality. Since \(H_{p,q}(z)>0\) for sufficiently small or large positive \(z\), the two-root case produces a genuine *both–one–both* sequence with increasing budget. For \((p,q)=(6,2)\),
\[
 H_{6,2}(z)=z^3+6z^2-18z+8.
\]
Its signs at \(z=1/6,5/6,20/6\) are respectively positive, negative and positive; the two roots give the quoted switch budgets. Because the function is strictly convex along the allocation constraint, there are no other optima or asymmetric competitors.

## Verification

Run the standalone Python 3 standard-library program `verify.py` from the same extracted package. It independently assembles pinned Laplacian matrices, inverts them by Gauss–Jordan elimination, checks the trace decomposition, gain budgets, analytic marginal identities, rational sign certificates and numerous asymmetric alternatives. It reports **2,302 finite checks passed** and computes the two approximate \(K_{6,2}\) budgets. A finite test is not a proof of the all-parameter statement; the proof above supplies the infinite-family argument. The program is an ordinary reproducibility check, not formal or independent validation.

## Relationship to prior work

Fitch and Leonard (arXiv:1407.1569, first public 7 July 2014) investigate selection of a prescribed number of leaders in noisy networks. Their Section II fixes one common positive measurement gain on a chosen set and zero gains elsewhere; their special-graph and appendix results solve fixed-leader-set problems, not the continuously divided global budget here. Their linear stochastic model supplies the motivation and inverse-trace performance interpretation. Shafi, Arcak and El Ghaoui (2010) optimize node- and edge-weighted Laplacian *spectral constraints*, using a generalized node-weighted Laplacian, rather than additive diagonal feedback with a trace-inverse objective. General inverse-trace convexity and KKT principles are classical; they do not themselves state the graph-specific cubic support test or double-transition phase diagram.

## Limitations

The classification is specific to unit-weight complete bipartite graphs, continuously divisible unit-priced gains, equal isotropic noise and inverse-trace loss. Roots generally require algebraic/numerical evaluation. The phenomenon is compatible with but not inferred from generic strict-convexity theory. The claim is not that earlier general convex optimization methods are novel. Related A-optimal experimental-design formulations or unindexed specialized consensus papers could contain an equivalent statement; this residual originality risk is not eliminated by database searches. No independent scientific audit has been performed.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07, https://arxiv.org/abs/1407.1569 ; full preprint https://arxiv.org/pdf/1407.1569 .
2. S. Y. Shafi, M. Arcak, and L. El Ghaoui, *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints*, 48th Allerton Conference (2010), doi:10.1109/ALLERTON.2010.5707021; lawful author full text https://people.eecs.berkeley.edu/~elghaoui/Pubs/SAE_Allerton_2010.pdf .
