# Exact negative type and an inverse-branching law for once-subdivided metric stars

## Finding
For each integer \(q\ge 3\), let \(T_q\) have central vertex \(o\), intermediate vertices \(a_1,\ldots,a_q\), and terminal vertices \(b_1,\ldots,b_q\), with unit edges \(oa_i\) and \(a_ib_i\). Let \(d\) be the graph shortest-path metric on **all** \(2q+1\) vertices, including the intermediate vertices and hub. Then the exact supremal negative-type exponent (equivalently, generalized roundness) is the unique \(\wp_q\in (1,\log_2(2q/(q-1)))\) for which
\[
q\bigl(1+2^{\wp_q/2}\bigr)^2
=1+(q-1)\bigl(3^{\wp_q}+2^{3\wp_q/2}\bigr).
\]
For \(0\le p<\wp_q\), \((T_q,d)\) has strict \(p\)-negative type; at \(p=\wp_q\) it has non-strict \(p\)-negative type; and for all \(p>\wp_q\) it fails \(p\)-negative type. The zero-sum equality space at \(p=\wp_q\) is one-dimensional. Consequently, the least affine Euclidean embedding dimension of the metric \(d^{p/2}\) is exactly \(2q\) when \(0<p<\wp_q\), and \(2q-1\) when \(p=\wp_q\).

These exponents strictly decrease with \(q\), and
\[
\wp_q=1+\frac{C}{q}+O(q^{-2}),\qquad
C=\frac{2+2\sqrt2}{3\log 3+(2\sqrt2-2)\log2}
=1.247636634\ldots.
\]
In particular, **subdividing each spoke strictly lowers** the maximal negative-type exponent of the unit \(q\)-leaf star when \(q\ge3\). For the exceptional \(q=2\) case, \(T_2\) is a five-vertex path; its exponent equals \(2\), and \(d\) embeds in a line at that endpoint.

## Assumptions and scope
All graph edges have length one, and all vertices of \(T_q\) are included in the metric space. The nonzero distances are \(d(o,a_i)=1\), \(d(o,b_i)=2\), \(d(a_i,a_j)=2\), \(d(a_i,b_i)=1\), \(d(a_i,b_j)=3\) for \(i\ne j\), and \(d(b_i,b_j)=4\) for \(i\ne j\). For an exponent \(p\ge0\), the metric has \(p\)-negative type precisely when
\[
\sum_{x,y\in T_q}\eta_x\eta_y d(x,y)^p\le0
\quad\text{for every real }(\eta_x)\text{ with }\sum_x\eta_x=0,
\]
with \(d(x,x)^p=0\). Strict negative type means the displayed inequality is strict for each nonzero such vector. The exponent of generalized roundness agrees with the supremal negative-type exponent; the latter is used for the proof.

## Proof
**Step 1: exact zero-sum decomposition.** Fix \(p>0\); write \(x=2^p\), \(y=3^p\), and \(t=2^{p/2}\), so \(x=t^2\). Every zero-sum vector is uniquely expressible as coefficients \(\eta_{a_i}=u+\alpha_i\), \(\eta_{b_i}=v+\beta_i\), \(\eta_o=-q(u+v)\), with \(\sum_i\alpha_i=\sum_i\beta_i=0\). Directly expanding the displayed distance list gives
\[
Q_p(\eta)=-q\bigl(Au^2+2C_0uv+xAv^2\bigr)
-\sum_{i=1}^{q}\bigl(x\alpha_i^2+2(y-1)\alpha_i\beta_i+x^2\beta_i^2\bigr),
\]
where \(A=2q-(q-1)x\) and \(C_0=q(1+x)-1-(q-1)y\). In particular, this is an identity for every real coefficient vector, not merely for symmetric test vectors.

**Step 2: the fluctuation block.** For every \(0<p<2\), the matrix
\[
\begin{pmatrix}x&y-1\\y-1&x^2\end{pmatrix}
\]
is positive definite. Indeed, \(x>0\) and \((y-1)^2<x^3\): since \(p/2\in(0,1)\), strict subadditivity gives \(3^p=(1+8)^{p/2}<1+8^{p/2}=1+x^{3/2}\). Thus the only possible non-strictness before \(p=2\) occurs in the two-dimensional symmetric block \(M=\bigl(\begin{smallmatrix}A&C_0\\C_0&xA\end{smallmatrix}\bigr)\).

**Step 3: the first singular symmetric block.** Put \(p_A=\log_2(2q/(q-1))\), so \(A>0\) for \(p<p_A\). For \(q\ge3\), one has \(1<p_A<2\). Factor its determinant as
\[
\det M=(tA+C_0)(tA-C_0)=F_q(p)G_q(p),
\]
where
\[
F_q(p)=q(1+t)^2-1-(q-1)(y+t^3),\qquad
G_q(p)=tA-C_0.
\]
For \(p\ge1\), set \(B(p)=(1+t)^2\) and \(E(p)=y+t^3\). We have
\[
E'(p)=3^p\log3+\tfrac32t^3\log2>
\tfrac32 t(1+t)\log2=\tfrac32 B'(p).
\]
Indeed, \(t^3\ge t^2\) and \(3^p\log3>\tfrac32t\log2\) for all \(p\ge1\). Consequently, for every \(q\ge3\),
\[
F_q'(p)=qB'(p)-(q-1)E'(p)<0\quad(p\ge1).
\]
At \(p=1\), \(F_q(1)=2+2\sqrt2>0\). At \(p=p_A\), \(A=0\) and
\[
F_q(p_A)=C_0(p_A)=\frac{x^2+2-2y}{x-2}<0.
\]
For the last sign, let \(g(p)=2\cdot3^p-4^p-2\). On \(1<p<2\), \(g(1)=g(2)=0\) and \(g''(p)<0\): since \(3^5<4^4\), \(\log3/\log4<4/5\) and hence \(2(3/4)^p(\log3/\log4)^2<24/25<1\) for \(p\ge1\). Strict concavity yields \(g(p)>0\). Therefore \(F_q\) has a unique zero \(\wp_q\) in \((1,p_A)\).

We must exclude an earlier zero of \(G_q\). This can be done uniformly. Fix \(1<p<2\) and regard \(q\) temporarily as a real parameter. The function \(H(p)=E(p)-B(p)\) is positive since \(H(1)=0\) and \(H'=E'-B'>0\). Thus \(F_q(p)\ge0\) is equivalent to \(0\le q\le Q(p)\), where
\[
Q(p)=\frac{E(p)-1}{E(p)-B(p)}.
\]
Let \(q_A(p)=x/(x-2)\), the real parameter where \(A=0\). The inequality \(g(p)>0\) yields \(F_{q_A(p)}(p)= -g(p)/(x-2)<0\), so \(Q(p)<q_A(p)\). Hence \(A(Q(p),p)>0\). The function \(q\mapsto G_q(p)\) is affine and positive at both endpoints of \([0,Q(p)]\):
\[
G_0(p)=1+t^3-y>0,
\qquad G_{Q(p)}(p)=2tA(Q(p),p)>0.
\]
The first inequality is again strict subadditivity. It follows that \(G_q(p)>0\) whenever \(1<p<2\) and \(F_q(p)\ge0\). At \(p=1\) the blocks are directly positive definite. Thus \(M\) is positive definite for \(1\le p<\wp_q\), and at \(p=\wp_q\) it is positive semidefinite of rank one. Combining the symmetric and fluctuation blocks proves strict negative type on \([1,\wp_q)\) and non-strict negative type at the endpoint. Li--Weston's strictness theorem extends strictness from \(1\) to \(0\le p<1\); their same theorem implies that no exponent above a non-strict negative-type endpoint can have negative type.

**Step 4: the equality space and Euclidean dimensions.** At \(p=\wp_q\), one has \(C_0=-tA\), with \(A>0\). The radial matrix is therefore
\[
M=A\begin{pmatrix}1&-t\\-t&t^2\end{pmatrix},
\]
whose null space is spanned by \((u,v)=(t,1)\). The fluctuation block is strictly positive at the endpoint, so the **entire** zero-sum equality space is spanned by the vector
\[
\eta_o=-q(t+1),\quad \eta_{a_i}=t,\quad \eta_{b_i}=1\quad (1\le i\le q).
\]
The coefficients sum to zero. Schoenberg's Euclidean distance criterion identifies the Gram matrix of the squared distances \(d^p\) as \(-\tfrac12 J(d(v,w)^p)_{v,w}J\), where \(J\) is orthogonal projection onto the zero-sum space. Its positive rank is \(2q\) under strict negative type and \(2q-1\) at the endpoint. These are the claimed minimum affine Euclidean embedding dimensions for \(d^{p/2}\).

**Step 5: monotonicity and asymptotics.** For fixed \(p>1\), \(E(p)>B(p)\), so \(F_q(p)=(E(p)-1)-q(E(p)-B(p))\) decreases strictly with \(q\). Consequently its root \(\wp_q\) decreases strictly. The root tends to \(1\). The implicit function theorem applied to \(B(p)-E(p)+(E(p)-1)/q=0\) at \((p,1/q)=(1,0)\), where \((E-B)'(1)=3\log3+(2\sqrt2-2)\log2>0\), gives
\[
\wp_q=1+\frac{2+2\sqrt2}{\bigl(3\log3+(2\sqrt2-2)\log2\bigr)q}+O(q^{-2}).
\]
The strict inequality \(\wp_q<p_A\) compares this family with the exact original \(q\)-leaf star exponent established by Doust--Weston. If \(q=2\), the graph is a five-vertex unit path on a Euclidean line. Its ordinary metric has strict \(p\)-negative type for \(0\le p<2\); it has non-strict \(2\)-negative type and has no higher negative type, with Euclidean dimension one at \(p=2\).

## Verification
The accompanying standalone `verify_subdivided_star.py` builds the tree by graph edges and breadth-first search, then tests the exact quadratic identity using `fractions.Fraction` on \(q=2,\ldots,8\) and exponents \(1,2,3\). It separately computes centered Gram matrices and numerical inertias for \(3\le q\le16\), checks the root interval and endpoint rank, and reports large-\(q\) asymptotic diagnostics. These finite tests independently corroborate the decomposition and signs. They are not used as proofs of the universal inequalities above.

## Relationship to prior work
Doust--Weston, *Enhanced negative type for finite metric trees* (arXiv:0705.0411), Theorem 5.6, computes the exponent of the **unsubdivided** star; its other results yield general finite-tree bounds rather than the present all-vertex depth-two classification. Li--Weston, *Strict p-negative type of a metric space* (arXiv:0901.0695), Theorem 5.4, supplies the strictness implication used here. Caffarelli--Doust--Weston, *Metric trees of generalized roundness one* (arXiv:1008.3418), Theorem 2.1, derives degree-dependent upper bounds for trees of radius at least three, not the present exact radius-two case. Sánchez, *On the supremal p-negative type of a finite metric space* (arXiv:1108.0451), develops a general determinant method without evaluating this depth-two star family. Levy-Moore--Nichols--Weston, *Comparing the generalized roundness of metric spaces* (arXiv:1608.03699), treats comparison methods and infinite-tree phenomena. The claim here is the explicit exact exponent, equality space, dimension transition, monotonicity, and asymptotics for all \(q\ge3\), not a claim to have introduced negative-type theory or the general determinant method.

## Limitations
The classification is only for unit edge lengths on equal-depth, once-subdivided stars with **all vertices present**. It does not classify unequal arm depths, weighted edges, deeper spherically symmetric trees, or the metric restricted to leaves. The originality assessment depends on inspected accessible primary sources and targeted searching; it does not prove no unindexed equivalent argument exists. Independent scientific validation has not been performed.

## References
1. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, first available May 3, 2007, https://arxiv.org/abs/0705.0411, especially Theorem 5.6.
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, first available January 6, 2009, https://arxiv.org/abs/0901.0695, especially Theorem 5.4.
3. E. Caffarelli, I. Doust and A. Weston, *Metric trees of generalized roundness one*, first available August 20, 2010, https://arxiv.org/abs/1008.3418, especially Section 2.
4. S. Sánchez, *On the supremal p-negative type of a finite metric space*, first available August 2, 2011, https://arxiv.org/abs/1108.0451.
5. L. Levy-Moore, M. Nichols and A. Weston, *Comparing the generalized roundness of metric spaces*, first available August 12, 2016, https://arxiv.org/abs/1608.03699.
