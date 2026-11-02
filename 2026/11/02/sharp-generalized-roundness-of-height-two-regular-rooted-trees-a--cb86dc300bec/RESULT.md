# Sharp generalized roundness of height-two regular rooted trees and an inverse-square branching law

## Finding
Let \(T_{m,\ell}\) have a root, \(m\ge2\) children, and \(\ell\ge2\) private leaves attached to every child. All edges have length one, all \(1+m+m\ell\) vertices are included, and \(d\) is shortest-path distance. For \(1\le p\le2\), put
\[
 u=2^p,\quad v=3^p,\quad w=4^p,\quad
 a_m=(m-1)u-2m,\quad
 b_m=1+(m-1)v-m(1+u),\quad
 c_{m,\ell}=(\ell-1-2m\ell)u+(m-1)\ell w.
\]
The exact supremal negative-type exponent (equivalently, generalized roundness) \(\wp_{m,\ell}\) is the **unique** \(p\) in
\[
 1<p<\log_2\!\left(\frac{2m}{m-1}\right)
\]
such that
\[
 \boxed{a_m(p)c_{m,\ell}(p)=\ell\,b_m(p)^2.}
\]
The metric has strict \(p\)-negative type for \(0\le p<\wp_{m,\ell}\), non-strict negative type with precisely one zero-sum equality direction at \(p=\wp_{m,\ell}\), and no \(p\)-negative type above it. For \(0<p\le\wp_{m,\ell}\), the minimal Euclidean affine dimension of the metric \(d^{p/2}\) is
\[
 \begin{cases}
 m\ell+m,&0<p<\wp_{m,\ell},\\
 m\ell+m-1,&p=\wp_{m,\ell}.
 \end{cases}
\]
For the diagonal family of complete \(b\)-ary trees of depth two, the critical exponent satisfies the sharp limit
\[
 \boxed{\lim_{b\to\infty}b^2(\wp_{b,b}-1)=\frac1{5\log 2-3\log 3}=\frac1{\log(32/27)}.}
\]
In particular, \(\wp_{2,2}=1.527173088279971\ldots\) and \(\wp_{3,3}=1.297368465400303\ldots\).

## Assumptions and scope
The graph is a finite, unweighted, two-level, spherically symmetric tree, not the leaf-only metric, not a double-star, and not an infinite tree. Exponents are real. A finite metric has \(p\)-negative type when \(\sum_{x,y}\alpha_x\alpha_y d(x,y)^p\le0\) for all real coefficient vectors \(\alpha\) satisfying \(\sum_x\alpha_x=0\); strict negative type means strict inequality whenever \(\alpha\ne0\). At exponent zero, distinct-point distances are assigned power zero equal to one. Generalized roundness equals the supremal negative-type exponent. The critical root is taken in the stated open interval: other zeros of an unconstrained determinant, if present, are not critical exponents.

## Proof
Write \(Q_p(\alpha)=\sum_{x,y}\alpha_x\alpha_y d(x,y)^p\). A coefficient vector on the zero-sum hyperplane decomposes uniquely as follows. Within each sibling leaf class, its leaf coefficients have a zero-mean fluctuation; the common leaf means and their parent coefficients split into zero-sum fluctuations between the \(m\) branches and a two-dimensional radial component. In the radial component, put coefficient \(a\) on every child, \(h\) on every leaf and \(-m a-m\ell h\) on the root.

Set \(u=2^p\), \(v=3^p\), \(w=4^p\). On within-class fluctuations, \(Q_p=-u\sum\alpha_x^2\). Each of the \(m-1\) independent between-branch modes has quadratic-form matrix
\[
 S=\begin{pmatrix}-u&\ell(1-v)\\
 \ell(1-v)&\ell(\ell-1)u-\ell^2w\end{pmatrix}.
\]
On the radial component, the exact matrix is
\[
 P=m\begin{pmatrix}a_m&\ell b_m\\\ell b_m&\ell c_{m,\ell}\end{pmatrix}.
\]
These identities use the seven relevant vertex-pair types: root/child \(1\), root/leaf \(2\), different children \(2\), child/own leaf \(1\), child/other leaf \(3\), sibling leaves \(2\), and leaves of different branches \(4\). Direct expansion proves that the three invariant subspaces are mutually orthogonal for the bilinear form associated with \(Q_p\), and their dimensions sum to \(m+m\ell\), the dimension of the full zero-sum hyperplane.

The crucial comparison is the strictly positive definite matrix identity for every \(1<p<2\):
\[
 \frac Pm-S=m\begin{pmatrix}2^p-2&\ell(3^p-2^p-1)\\
 \ell(3^p-2^p-1)&\ell^2(4^p-2^{p+1})\end{pmatrix}\succ0.
\]
To prove this without assuming an unverified inequality, let \(f(x)=x^p\) and \(L_1=1,L_2=2\). The unscaled matrix on the right has entries
\[
 f(L_i+L_j)-f(L_i)-f(L_j)
 =p(p-1)\int_0^{L_i}\int_0^{L_j}(s+t)^{p-2}\,ds\,dt.
\]
For \(1<p<2\), the kernel is a strictly positive Gram kernel by
\[
 (s+t)^{p-2}=\frac1{\Gamma(2-p)}\int_0^\infty\lambda^{1-p}e^{-\lambda s}e^{-\lambda t}\,d\lambda.
\]
Indeed the two functions \(\lambda\mapsto\int_0^1e^{-\lambda s}ds\) and \(\lambda\mapsto\int_0^2e^{-\lambda s}ds\) are linearly independent in the corresponding weighted \(L^2\) space. Conjugating by \(\operatorname{diag}(1,\ell)\) and multiplying by \(m>0\) preserves strict positive definiteness.

At \(p=1\), \(P/m=S=\begin{psmallmatrix}-2&-2\ell\\-2\ell&-2\ell(\ell+1)\end{psmallmatrix}\), a negative definite matrix. The other fluctuation modes are also strictly negative. At \(p=2\), \(P\) is not negative semidefinite: if \(m\ge3\), its upper-left entry is \(2m(m-2)>0\); if \(m=2\), its lower-right entry is \(8\ell(\ell-1)>0\). Consequently the critical exponent lies strictly between one and two. By strict positive definiteness of \(P/m-S\), whenever \(P\preceq0\) in that interval, \(S\prec0\). Thus no nonradial direction can become critical first.

Let \(p_0=\log_2(2m/(m-1))\). The upper-left entry \(a_m\) of \(P/m\) is negative for \(1\le p<p_0\). Its determinant is \(\ell(a_m c_{m,\ell}-\ell b_m^2)\), so the first radial singularity in this interval is precisely the stated scalar root. Existence follows from negative definiteness at one and failure before \(p_0\). For \(m\ge3\), at \(p=p_0\), \(a_m=0\) and
\[
 b_m=\frac{2\cdot 3^{p_0}-4^{p_0}-2}{2^{p_0}-2}>0,
\]
because \(2-(4/3)^p-2\cdot3^{-p}\) is strictly concave and vanishes at both endpoints \(p=1,2\). For \(m=2\), \(p_0=2\), and \(P_{22}(2)>0\) while \(P_{11}<0\) immediately to its left, again forcing a singularity before \(p_0\). Every scalar root with \(p<p_0\) makes \(P\preceq0\), hence makes the full form negative semidefinite. The strict-downward-propagation theorem for negative type implies no second such root: if a later exponent had negative type, the earlier equality would have to be strict. The same theorem proves strict negative type below this unique root and failure of negative type above it.

At the endpoint, \(P\) has a one-dimensional kernel. A two-dimensional kernel would force \(P=0\). Since \(a_m<0\) at the endpoint this is impossible. The branch block is still negative definite, as are all within-class modes. The equality vectors are therefore radial, with \((a,h)\) proportional to \((-\ell b_m(\wp_{m,\ell}),a_m(\wp_{m,\ell}))\), and root coefficient determined by zero sum. Schoenberg's centered-Gram construction turns the nullity one into the stated exact Euclidean rank drop.

Finally, specialize to \(m=\ell=b\) and put \(F_b(p)=\det(P_{b,b}(p)/b)\). Direct differentiation at one gives
\[
 F_b(1)=4b,\qquad
 F_b'(1)=-4b(b-1)\bigl[b(5\log2-3\log3)+2\log2\bigr].
\]
For each fixed real \(c>0\), elementary Taylor expansion (with \(F_b''=O(b^4)\) uniformly for \(p\) within \(O(b^{-2})\) of one) yields
\[
 \frac{F_b(1+c/b^2)}b=4\bigl[1-c(5\log2-3\log3)\bigr]+O_c(b^{-1}).
\]
Since \(a_b(1+c/b^2)=-2+O_c(b^{-1})<0\), the sign of this determinant gives strict radial negative definiteness below the indicated scale and failure above it. The unique critical root is squeezed between \(1+c_-/b^2\) and \(1+c_+/b^2\) for arbitrary \(c_-<1/(5\log2-3\log3)<c_+\), proving the limit.

## Verification
The standalone script `verify_two_level_tree.py` independently builds all graph distances by breadth-first search, reconstructs the full zero-sum powered-distance form, and compares it with the three-block formula using exact integer and rational arithmetic. It checks 600 exact identities, 30 full-matrix critical inertia calculations and high-precision diagonal asymptotics. Reported output from running the embedded script:

```
EXACT_POWERED_DISTANCE_DECOMPOSITION_OK 600
CRITICAL_FULL_MATRIX_INERTIA_OK 30
ROOTED_BINARY_DEPTH_TWO_OK 1.527173088279971
INVERSE_SQUARE_BRANCHING_CONSTANT_OK 5.885848553716
ALL_TWO_LEVEL_TREE_CHECKS_OK
```

The analytic Laplace-kernel argument, strictness theorem and Taylor estimates—not the finite numerical checks—prove the universal claims.

## Relationship to prior work
Doust and Weston (2007/2008) established enhanced negative-type bounds for finite metric trees. Li and Weston (2009/2010) proved strict-downward propagation and non-strictness at finite supremal endpoints. Caffarelli, Doust and Weston (2010/2011 preprint) studied spherically symmetric trees and explicitly reported the depth-two binary numerical value \(1.5272\) in their Section 5; their results concern estimates and numerical calculations rather than the present uniform two-parameter evaluated formula and inverse-square law. Sánchez (2011) provided a general distance-matrix criterion for any finite metric, from which instances can in principle be evaluated, but that criterion does not itself identify the radial mode or simplify the present family uniformly. The binary numerical approximation is prior work, not a novel standalone assertion.

## Limitations
This theorem applies only to the unweighted complete two-level trees with at least two branches and at least two leaves per branch, counting all vertices. It does not classify arbitrary weighted or irregular trees, higher depths, leaf-only metrics, infinite trees or more general Banach embeddings. The literature comparison supports qualified originality for the explicit uniform reduction and asymptotic law, not a claim that the underlying general negative-type criterion is new. Independent validation has not been performed.

## References
- I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411, first posted 2007-05-03; Journal of Functional Analysis 254 (2008), 2336–2364. https://arxiv.org/abs/0705.0411
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, first posted 2009-01-06; Positivity 14 (2010), 529–545. https://arxiv.org/abs/0901.0695
- E. Caffarelli, I. Doust and A. Weston, *Metric trees of generalized roundness one*, arXiv:1008.3418, first posted 2010-08-20; Aequationes Mathematicae 83 (2012), 239–256. https://arxiv.org/abs/1008.3418
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first posted 2011-08-02. https://arxiv.org/abs/1108.0451
