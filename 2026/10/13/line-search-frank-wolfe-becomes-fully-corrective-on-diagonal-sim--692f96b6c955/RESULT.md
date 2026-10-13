# Line-search Frank–Wolfe becomes fully corrective on diagonal simplex quadratics
## Finding
Let
\[
\Delta_m=\{x\in\mathbb R^m:x_i\ge0,\ \sum_{i=1}^m x_i=1\}
\]
and
\[
f(x)=\frac12\sum_{i=1}^m a_i x_i^2,
\qquad a_i>0.
\]
For every nonempty support \(S\subseteq\{1,\ldots,m\}\), define
\[
Z_S=\sum_{i\in S}a_i^{-1}
\]
and the unique minimizer of \(f\) on the face supported by \(S\) by
\[
x_i^S=
\begin{cases}
a_i^{-1}/Z_S,&i\in S,\\
0,&i\notin S.
\end{cases}
\]

Run classical Frank–Wolfe with an exact vertex linear-minimization oracle and exact line search. If the current iterate is \(x^S\) and \(S\) is not the full support, then every vertex selected by the oracle is an unseen vertex \(e_j\) with \(j\notin S\), and the exact line-search parameter is
\[
\gamma_j=\frac{a_j^{-1}}{Z_S+a_j^{-1}}
=\frac{1}{1+a_j Z_S}.
\]
The resulting iterate is exactly
\[
(1-\gamma_j)x^S+\gamma_j e_j=x^{S\cup\{j\}}.
\]
Thus, on this family, ordinary one-dimensional line-search Frank–Wolfe produces exactly the same iterates as a fully corrective method on the growing active set. Starting from any vertex, it reaches the global minimizer
\[
x_i^\star=\frac{a_i^{-1}}{\sum_{\ell=1}^m a_\ell^{-1}}
\]
in exactly \(m-1\) nonstationary iterations, independently of how ties among unseen vertices are broken. More generally, a face-minimizer start \(x^S\) terminates after exactly \(m-|S|\) nonstationary iterations.

Along this trajectory,
\[
f(x^S)=\frac{1}{2Z_S},
\qquad
g_{\mathrm{FW}}(x^S)=\frac{1}{Z_S}
\]
for every incomplete support \(S\), where \(g_{\mathrm{FW}}\) is the standard Frank–Wolfe duality gap.

## Assumptions and scope
The theorem uses exact arithmetic, positive diagonal coefficients \(a_i>0\), the probability simplex in the same coordinate basis as the diagonal Hessian, an exact line search, and the standard vertex form of the simplex linear-minimization oracle. When several unseen vertices tie, any tied vertex may be selected.

The vertex-oracle assumption matters. At an incomplete face minimizer, every unseen vertex has the same minimal linearized value, so a linear oracle allowed to return an arbitrary convex combination of tied minimizers need not follow the stated one-vertex enlargement path.

## Proof
Fix a nonempty support \(S\). Minimizing \(f\) on its face under \(\sum_{i\in S}x_i=1\) gives the Lagrange equations
\[
a_i x_i=\lambda
\qquad(i\in S).
\]
After normalization,
\[
\lambda=Z_S^{-1},
\qquad
x_i=x_i^S.
\]
Strict convexity on the face makes this minimizer unique.

At \(x^S\), the gradient coordinates are therefore
\[
(\nabla f(x^S))_i=
\begin{cases}
Z_S^{-1},&i\in S,\\
0,&i\notin S.
\end{cases}
\]
If \(S\) is incomplete, a vertex linear-minimization oracle must choose \(e_j\) with \(j\notin S\).

Along the Frank–Wolfe segment to that vertex,
\[
y(\gamma)=(1-\gamma)x^S+\gamma e_j,
\qquad 0\le\gamma\le1,
\]
the supports are disjoint between the old face and the newly selected coordinate, so
\[
f(y(\gamma))
=\frac{(1-\gamma)^2}{2Z_S}
+\frac{a_j\gamma^2}{2}.
\]
The derivative vanishes exactly at
\[
-\frac{1-\gamma}{Z_S}+a_j\gamma=0,
\]
which gives
\[
\gamma=\frac{1}{1+a_jZ_S}
=\frac{a_j^{-1}}{Z_S+a_j^{-1}}.
\]
Substitution yields, for \(i\in S\),
\[
y_i=\frac{a_i^{-1}}{Z_S+a_j^{-1}},
\]
and
\[
y_j=\frac{a_j^{-1}}{Z_S+a_j^{-1}}.
\]
Hence \(y=x^{S\cup\{j\}}\). Induction proves the trajectory identity and finite-termination count.

Finally,
\[
f(x^S)=\frac12\sum_{i\in S}a_i\frac{a_i^{-2}}{Z_S^2}
=\frac{1}{2Z_S}.
\]
For an unseen oracle vertex \(e_j\), the Frank–Wolfe gap is
\[
\langle x^S-e_j,\nabla f(x^S)\rangle
=\frac{1}{Z_S}.
\]
At full support all gradient coordinates are equal, so the gap is zero.

## Verification
For the exact example
\[
(a_1,a_2,a_3,a_4)=(1,2,3,6),
\]
start from \(e_1\) and let the oracle add \(e_2,e_3,e_4\). Exact line search gives
\[
\gamma_1=\frac13,
\qquad
x^{(1)}=\left(\frac23,\frac13,0,0\right),
\]
\[
\gamma_2=\frac{2}{11},
\qquad
x^{(2)}=\left(\frac6{11},\frac3{11},\frac2{11},0\right),
\]
and
\[
\gamma_3=\frac1{12},
\qquad
x^{(3)}=\left(\frac12,\frac14,\frac16,\frac1{12}\right)=x^\star.
\]
The objective values are respectively \(1/2,1/3,3/11,1/4\).

The accompanying exact-rational checker reconstructs this example and exhaustively checks the one-step identity for dimensions \(2\) through \(5\), every positive integer diagonal with entries in \(\{1,2,3,4\}\), every nonempty proper support, and every unseen vertex choice. These finite checks corroborate the algebra; they are not used as a proof of the all-dimensional theorem.

## Relationship to prior work
Jaggi's Frank–Wolfe survey presents exact line search and the fully corrective update as distinct algorithmic variants: line search minimizes only on the current segment, whereas the fully corrective variant re-optimizes over all previously selected atoms. The same paper uses the unit simplex with the unweighted squared Euclidean norm as a canonical sparsity example. The statement proved here identifies a special weighted quadratic geometry in which those two variants coincide iterate-for-iterate from every face minimizer, and it gives the exact inverse-curvature trajectory, objective values, gaps, and finite-termination count.

Clarkson's earlier simplex Frank–Wolfe treatment likewise describes a greedy line-search method and, separately, a harder-working current-face re-optimization. The inspected material does not state that the two operations become identical for arbitrary positive diagonal quadratics.

Lan and Zhou's conditional-gradient work provides a standard convex-programming classification for conditional-gradient methods and explicitly uses exact line search in a conditional-gradient subroutine. It supplies classification and method context, not the diagonal-simplex equivalence above.

## Limitations
The theorem does not extend automatically to dense positive-definite Hessians, to a diagonal Hessian expressed in coordinates not aligned with the simplex vertices, to arbitrary starting points that are not face minimizers, to inexact line search, or to an oracle that returns a nonvertex convex combination of tied minimizers. No claim is made about floating-point finite termination.

The literature comparison was targeted to Frank–Wolfe/conditional-gradient line search, fully corrective variants, simplex squared-norm examples, finite termination, and separable diagonal quadratics. Older resource-allocation or separable-quadratic literature could contain an equivalent observation under different terminology.

## References
1. Martin Jaggi, “Revisiting Frank-Wolfe: Projection-Free Sparse Convex Optimization,” Proceedings of Machine Learning Research 28(1), 427–435, 2013, PMLR:v28:jaggi13.
2. Kenneth L. Clarkson, “Coresets, Sparse Greedy Approximation, and the Frank-Wolfe Algorithm,” ACM Transactions on Algorithms 6(4), 2010; author manuscript dated July 22, 2008, DOI:10.1145/1824777.1824783.
3. Guanghui Lan and Yi Zhou, “Conditional Gradient Sliding for Convex Optimization,” Optimization Online, October 17, 2014, OptimizationOnline:4605.
