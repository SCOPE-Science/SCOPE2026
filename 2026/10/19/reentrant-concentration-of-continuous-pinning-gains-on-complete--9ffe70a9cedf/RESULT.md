# Continuous pinning on complete bipartite networks: the exact support phase diagram

## Finding and scope

Let \(K_{p,q}\) be a unit-weight complete bipartite graph with integers \(p\ge q\ge2\) and ordinary combinatorial Laplacian \(L\). For any \(B>0\), minimize
\[
 J(g)=\operatorname{tr}[(L+\operatorname{diag}(g))^{-1}],\qquad g_v\ge0,\qquad \sum_v g_v=B.
\]
The optimum is unique even with independently adjustable vertex gains. At the optimum all \(p\) vertices of the first part have a common gain \(x>0\), and all \(q\) vertices of the second part have a common gain \(y\ge0\). Set
\[
 H_{p,q}(z)=z^3+2(q+1)z^2+(p+q^2+4q-p^2)z+2q^2.
\]
The optimum has \(y=0\) and \(x=B/p\) if and only if \(H_{p,q}(B/p)\le0\). Otherwise it is the unique interior solution of the budget and marginal equations given below.

Define \(R_q(z)=z^2+2(q+1)z+q^2+4q+2q^2/z\) for \(z>0\), and let \(u_q>0\) solve \(u_q^3+(q+1)u_q^2=q^2\). If \(p^2-p>R_q(u_q)\), the cubic has exactly two positive roots \(z_-<z_+\) and only the \(p\)-vertex part is pinned precisely on \([pz_-,pz_+]\). Both parts are pinned at lower and higher budgets. In the algebraic equality case the sole concentration budget is \(pu_q\), and when \(p^2-p<R_q(u_q)\) both parts are always pinned. For example, \(H_{8,3}(z)=z^3+8z^2-35z+18\) takes the signs \(+,-,+\) at \(z=1/4,1,4\), giving both–one–both support at budgets \(2,8,32\).

The gains are additive, continuously divisible, and have no per-vertex cap or leader-count restriction. The objective is the trace of the inverse pinned Laplacian, proportional to stationary total variance under isotropic additive noise: the drift \(-(L+\operatorname{diag}g)X\) and noise \(\sigma\,dW\) give total variance \(\sigma^2J(g)/2\).

## Proof

**Existence, strict convexity, symmetry.** The matrix \(M=L+\operatorname{diag}g\) is positive definite throughout the compact feasible simplex: a vector in the nullspace of the quadratic form would be constant by connectivity and must vanish since at least one gain is positive. With \(S=M^{-1}\), the second derivative in a nonzero diagonal direction \(D\) is \(2\operatorname{tr}(SDSDS)=2\operatorname{tr}(S(S^{1/2}DS^{1/2})^2)>0\). Thus the unique minimum is invariant under independent within-part permutations, proving the asserted partwise constancy without restricting the original gain choices.

**Trace and marginal equations.** Write \(a=q+x\), \(b=p+y\), \(\Delta=ab-pq=px+qy+xy\). The zero-sum vectors within the two parts yield eigenvalues \(a\) and \(b\) of multiplicities \(p-1\) and \(q-1\); the orthonormal part-constant basis gives the block with diagonal \(a,b\) and both off-diagonal entries \(-\sqrt{pq}\). Inverting this last block gives
\[
 J(x,y)=\frac{p-1}{a}+\frac{q-1}{b}+\frac{a+b}{\Delta}.
\]
Put \(F_A=-\partial_x J/p\), \(F_B=-\partial_y J/q\). Differentiating gives
\[
 F_A=\frac{p-1}{pa^2}+\frac{b^2+pq}{p\Delta^2},\qquad
 F_B=\frac{q-1}{qb^2}+\frac{a^2+pq}{q\Delta^2}.
\]
Along \(f(y)=J((B-qy)/p,y)\) the derivative is \(q(F_A-F_B)\). With \(z=B/p\), substitution gives
\[
 f'(0)=\frac q{p^2}\left[\frac{p(p-1)}{(z+q)^2}-1-\frac2z\right]
      =-\frac{q H_{p,q}(z)}{p^2 z(z+q)^2}.
\]
The other endpoint is checked by interchanging the parts. For \(w=B/q\), the derivative along increasing \(x\), with \(dy/dx=-p/q\), at \(x=0\) is
\[
 \frac{p}{q^2}\left[\frac{q(q-1)}{(w+p)^2}-1-\frac2w\right]<0,
\]
since \(q(q-1)<p^2\). Thus moving inward from \(x=0\) reduces the objective. Equivalently \(f'(B/q)>0\) in the increasing-\(y\) coordinate used for \(f\). Strict convexity now gives the unique minimizer at \(y=0\) when \(f'(0)\ge0\), including equality. If \(f'(0)<0\), the minimizer is interior and its unique marginal equation is \(F_A=F_B\) on \(px+qy=B\); it can be solved by bisection.

**Classification.** For \(z>0\), \(H_{p,q}(z)=z(R_q(z)-(p^2-p))\). The function \(R_q\) diverges at both ends of the positive half-line, \(R_q''(z)=2+4q^2/z^3>0\), and \(R_q'(u_q)=0\) gives the stated equation for its unique minimizer. Comparison with the horizontal level \(p^2-p\) yields two simple positive intersections, one double intersection, or no intersection, respectively. The support condition includes both endpoints of the two-root interval.

## Examples and reproduction

For \((p,q)=(6,2)\), \(H=z^3+6z^2-18z+8\), the transition budgets are approximately \(3.34679965326\) and \(10.3824948581\), and budgets \(1,5,20\) exhibit the both–one–both sequence. The accompanying `verify.py` compares trace and marginal calculations with direct numerical inversion and checks this two-vertex-part example. Those finite checks are corroboration, not the general proof given above.

## Relationship to prior work and limitations

Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* (arXiv:1407.1569), use a common gain on a selected leader set rather than arbitrary additive gains sharing a total budget. Shafi, Arcak and El Ghaoui, *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints* (DOI 10.1109/ALLERTON.2010.5707021), use spectral constraints and a different node-weighted Laplacian. Inverse-trace convexity and the marginal test are not claimed as novel. The Resultary two-hub study `3040bc2335f8` gives exactly the \(q=2\) support law, \(p(p-1)z\ge(z+2)^3\), including the \(K_{6,2}\) example. The additional scope is the exact support phase diagram across arbitrary part sizes, including \(q\ge3\). The related clique-grounding result `0b9d2b9aa8a6` concerns a clique joined to an independent set, not two independent parts. No claim is made for general weighted or directed graphs, heterogeneous noise, or other optimization objectives.
