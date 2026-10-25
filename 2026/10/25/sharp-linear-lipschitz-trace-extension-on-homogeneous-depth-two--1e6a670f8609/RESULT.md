# Sharp linear Lipschitz trace extension on homogeneous depth-two trees

## Finding
For all integers \(m,k\ge2\), the minimum norm of a **real-linear simultaneous extension operator** from the leaves of the unit-edge homogeneous depth-two tree to all its vertices is
\[
\boxed{\Lambda_{m,k}=\frac{4(2mk-k-1)}{m(3k+1)}}.
\]
This is an actual minimum over every linear right inverse, not merely over symmetric or positive extension operators. It is achieved by an explicit positive, tree-automorphism-equivariant operator. Moreover,
\[
\Lambda_{m,k}>2\quad\Longleftrightarrow\quad (m-2)(k-1)>4,
\]
with equality at the parameter boundary. The constants are strictly increasing in either parameter and have the sharp, unattained two-parameter supremum \(8/3\).

## Assumptions and scope
Let \(T_{m,k}\) have one root \(r\), vertices \(b_i\) for \(1\le i\le m\), and leaves \(x_{i,j}\) for \(1\le j\le k\), with precisely the edges \(rb_i\) and \(b_ix_{i,j}\), each of length \(1\). Let \(L=\{x_{i,j}\}\), equipped with the restriction of the shortest-path metric on the full tree: distinct leaves in one branch are distance \(2\), and leaves in different branches are distance \(4\). All scalars are real. The spaces \(\operatorname{Lip}(L)/\mathbb R\) and \(\operatorname{Lip}(V(T_{m,k}))/\mathbb R\) carry their Lipschitz seminorms as norms. A right inverse \(E\) is linear on functions modulo constants and satisfies \((Ef)|_L=f\pmod{\mathbb R}\). The norm in the codomain equals the largest absolute difference across a unit tree edge. The infimum of \(\|E\|\) over all such operators is denoted \(\Lambda_{m,k}\).

Write \(\mu_i(f)=k^{-1}\sum_{j=1}^k f(x_{i,j})\) and \(\mu_0(f)=m^{-1}\sum_{i=1}^m\mu_i(f)\). Put
\[
\alpha_* = \frac{2mk-k-1}{(m-1)(3k+1)}.
\]
The claimed optimal extension is
\[
Ef(x_{i,j})=f(x_{i,j}),\qquad Ef(r)=\mu_0(f),\qquad
Ef(b_i)=\alpha_*\mu_i(f)+(1-\alpha_*)\mu_0(f).
\]
Since \(0<\alpha_*<1\) for \(m,k\ge2\), its coefficients are nonnegative and sum to one.

## Proof
**1. Reduction to symmetric extensions.** A right inverse can be represented so that its leaf outputs equal the prescribed leaf inputs exactly: correcting by an input-dependent constant does not alter its Lipschitz norm. Every tree automorphism acts isometrically on both Lipschitz spaces and preserves leaf restriction. Averaging any right inverse over the finite group \(S_k^m\rtimes S_m\) leaves the right-inverse property intact and cannot increase its norm. An equivariant linear rule at the root has equal coefficients on all leaves; constants are preserved, hence its output is \(\mu_0(f)\). Each equivariant branch rule has one common coefficient on its own \(k\) leaves and one on all other \((m-1)k\) leaves. Consequently every equivariant right inverse is, for some \(\alpha\in\mathbb R\),
\[
Ef(b_i)=\alpha\mu_i(f)+(1-\alpha)\mu_0(f).
\]
No positivity assumption is imposed in this reduction.

**2. Exact dual norm for leaf measures.** Given real coefficients \(w_{i,j}\) with \(\sum_{i,j}w_{i,j}=0\), the Lipschitz dual norm of the functional \(f\mapsto\sum w_{i,j}f(x_{i,j})\) on the leaf metric is
\[
\|w\|_{\mathrm{KR}}=\sum_{i,j}|w_{i,j}|+\sum_{i=1}^m\left|\sum_{j=1}^kw_{i,j}\right|.
\tag{1}
\]
Indeed, on a tree one may telescope potentials across edges, obtaining the upper bound by the absolute total descendant mass at each edge. Choosing every edge increment independently to have sign matching that mass attains the upper bound on the full tree. Its restriction to leaves is \(1\)-Lipschitz, so equality holds on the leaf metric as well. Thus (1) is exact for every real signed leaf measure of mass zero.

**3. Every symmetric extension has a uniform lower bound.** The root-to-branch edge functional equals \(\alpha(\mu_i-\mu_0)\). Applying (1) gives its exact norm
\[
A|\alpha|,\qquad A=\frac{4(m-1)}m.
\tag{2}
\]
For a branch-to-leaf edge \(b_ix_{i,a}\), rewrite the branch rule as
\[
Ef(b_i)=\beta\mu_i(f)+(1-\beta)\mu_{\neg i}(f),\qquad
\beta=\frac{1+(m-1)\alpha}{m},
\]
where \(\mu_{\neg i}\) averages all leaves outside branch \(i\). Consider the leaf function equal to \(2\) at \(x_{i,a}\), to \(0\) at the other leaves of branch \(i\), and to \(-2\) at all leaves outside that branch. This function is \(1\)-Lipschitz for the specified leaf distances. The difference between its values at \(x_{i,a}\) and the branch rule is exactly
\[
4-2\left(1+\frac1k\right)\beta
=4-\frac{2(k+1)}{mk}\bigl(1+(m-1)\alpha\bigr).
\tag{3}
\]
The witness remains legitimate for every real \(\alpha\), even when the branch coefficients have negative entries. Therefore every equivariant extension, and hence every extension, satisfies
\[
\|E\|\ge
\max\left\{A\alpha,
4-\frac{2(k+1)}{mk}\bigl(1+(m-1)\alpha\bigr)\right\}.
\tag{4}
\]
The first affine expression strictly increases with \(\alpha\), the second strictly decreases. Their unique intersection is
\[
\alpha=\alpha_* =\frac{2mk-k-1}{(m-1)(3k+1)},
\]
and the minimum of the two-line maximum is
\[
A\alpha_* =\frac{4(2mk-k-1)}{m(3k+1)}.
\tag{5}
\]

**4. The lower bound is attained on every tree edge.** For \(\alpha=\alpha_*\), direct simplification yields \(0<\alpha_*<1\), so \(0<\beta<1\), and the branch rule is a positive probability measure on the leaves. Applying (1) to the branch-to-leaf edge signed measure \(\delta_{i,a}-\beta\mu_i-(1-\beta)\mu_{\neg i}\) gives
\[
\begin{aligned}
\|\delta_{i,a}-\beta\mu_i-(1-\beta)\mu_{\neg i}\|_{\mathrm{KR}}
&=2\left(1-\frac\beta k\right)+2(1-\beta)\\
&=4-2\left(1+\frac1k\right)\beta.
\end{aligned}
\tag{6}
\]
Equation (2) gives \(A\alpha_*\) on every root-to-branch edge. At \(\alpha_*\), equations (3), (5), and (6) make **both** edge types attain the common value \(\Lambda_{m,k}\), proving the stated norm and global optimality.

**5. Phase boundary and limiting sharpness.** Simplifying \(\Lambda_{m,k}-2\) yields
\[
\Lambda_{m,k}-2
=\frac{2\bigl((m-2)(k-1)-4\bigr)}{m(3k+1)}.
\]
Moreover,
\[
\Lambda_{m,k}=\frac{4}{3k+1}\left(2k-\frac{k+1}{m}\right).
\]
For fixed \(k\), this strictly increases with \(m\), and for fixed \(m\), differentiation of the corresponding positive-real parameter expression in \(k\) gives a positive derivative. Taking \(m,k\to\infty\) yields \(8/3\), while every finite parameter pair has smaller norm.

## Verification
The self-contained standard-library script `verify.py` uses exact rational arithmetic to reconstruct the tree-edge dual norms from signed masses and verify the stated optimal extension, dual Lipschitz witnesses, and phase boundary. Executing `python verify.py 8 8` checks all \(49\) pairs with \(2\le m,k\le8\) and all \(1470\) corresponding edge functionals. It reports exact values \(10/7\), \(8/5\), \(12/7\), \(28/15\), and \(2\) for representative parameter pairs. Separately, unconstrained finite-dimensional linear programming across representative pairs numerically corroborated optimality without imposing symmetry. Finite computations are supplemental; the proof above covers the entire infinite family.

## Relationship to prior work
Fefferman and Klartag, *Linear extension operators for Sobolev spaces on radially-symmetric binary trees* (2023, arXiv:2301.13792v1), establish uniform Sobolev extension bounds for the range \(1<p<\infty\) on weighted binary trees. Their concluding discussion specifically separates the endpoint \(p=\infty\) as an open direction; neither that theorem nor the present height-two calculation settles the general endpoint question. Bruè, Di Marino, and Stra (2018, arXiv:1801.07533v1) develop general Lipschitz extension operators through random projections. Their general estimates do not state the present sharp two-parameter constant or its optimality among all simultaneous linear extensions. General one-point metric-star formulas also do not imply the many-branch, all-internal-vertices optimization here.

## Limitations
The result concerns real scalars, unit edges, a homogeneous depth-two rooted tree, and the **scalar Lipschitz** endpoint with the induced leaf metric. It does not determine sharp extension norms for deeper or weighted trees, arbitrary metric subsets, complex scalars, Banach-valued Lipschitz functions, or finite Sobolev exponents. Global originality cannot be certified by finite literature searches, and relevant unindexed explicit finite-tree formulas may exist. The analytical result has undergone self-review only; independent mathematical audit has not been performed.

## References
1. C. Fefferman and B. Klartag, *Linear extension operators for Sobolev spaces on radially-symmetric binary trees*, arXiv:2301.13792v1, first public 2023-01-31, especially the endpoint discussion in the final remarks.
2. E. Bruè, S. Di Marino, and F. Stra, *Linear Lipschitz and C¹ extension operators through random projection*, arXiv:1801.07533v1, first public 2018-01-23.
