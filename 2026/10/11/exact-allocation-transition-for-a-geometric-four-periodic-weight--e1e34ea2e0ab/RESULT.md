# Exact allocation transition for a geometric four-periodic weighted shift

## Finding
Fix \(0<q<1\). On \(\ell_2(\mathbb N_0;\mathbb C)\), define the unilateral weighted shift \(T_{q,s,t}\) by \(T_{q,s,t}e_n=w_ne_{n+1}\), where, for every integer \(k\ge0\),
\[
(w_{4k},w_{4k+1},w_{4k+2},w_{4k+3})
=(q^{4k},s q^{4k+1},q^{4k+2},t q^{4k+3}).
\]
Put \(\mathcal R_q(c)=\inf\{w(T_{q,s,t}):s>0,\ t>0,\ s+t=c\}\) for \(c>0\), where \(w\) is the Hilbert-space numerical radius, and define the exact threshold
\[
c_*(q)=\frac{\sqrt{(1-q^4)(1-q^8)}}{q^3}.
\]
The infimum equals the minimum over the closed segment \(s,t\ge0\). If \(0<c\le c_*(q)\), then \(\mathcal R_q(c)=1/2\), attained on the closed segment **only** at \((s,t)=(0,c)\), and not attained for strictly positive \(s,t\). If \(c>c_*(q)\), the closed and open problems have the same **unique**, strictly positive minimizer \((s_c,t_c)\), and \(\mathcal R_q(c)>1/2\). The optimal value is strictly increasing, strictly convex, and real-analytic for \(c>c_*(q)\).

There is also a two-term large-budget law, including the first nontrivial shift of the optimizer:
\[
\begin{aligned}
s_c&=\frac{q^2}{1+q^2}\,c-\frac{1-q^2}{2(1+q^2)}+o(1),\\
t_c&=\frac{1}{1+q^2}\,c+\frac{1-q^2}{2(1+q^2)}+o(1),\\
\mathcal R_q(c)&=\frac{q^3}{2(1+q^2)}(c+1)+o(1)
\qquad(c\longrightarrow\infty).
\end{aligned}
\]
All assertions are for every fixed \(q\) strictly between zero and one; the remainder terms are not claimed uniform in \(q\) at the endpoints.

## Assumptions and scope
The scalar field is complex, the Hilbert space is \(\ell_2(\mathbb N_0)\), and numerical radius means \(w(T)=\sup_{\|x\|_2=1}|\langle Tx,x\rangle|\). The endpoint shifts with \(s=0\) or \(t=0\) are used only to understand the closure and the infimum of the original strictly positive problem. The weight sequence tends to zero geometrically, so the associated symmetric Jacobi operator is compact. No universal statement about other weight patterns, exponents, or arbitrary linear constraints is claimed.

## Proof
**1. Jacobi reduction.** The diagonal circle-unitary symmetry of a unilateral weighted shift gives
\[
w(T_{q,s,t})=\tfrac12\lambda_{\max}(S_{q,s,t}),\qquad S_{q,s,t}=T_{q,s,t}+T_{q,s,t}^*.
\]
Here the off-diagonal entries of \(S\) are the nonnegative weights \(w_n\). The largest eigenvalue is positive. Whenever \(s,t>0\), all off-diagonal entries are strictly positive; the compact Jacobi operator has a simple top eigenvalue and a corresponding strictly positive normalized eigenvector \(v\). This follows from the nonnegative top Rayleigh quotient, positivity propagation along the connected path, and the three-term eigenvector recurrence; simplicity also follows from that recurrence and the initial coordinate. The largest eigenvalue is real-analytic in \((s,t)\).

**2. The exact endpoint threshold.** At \(s=0\), the path splits into the edge of weight \(1\) on vertices \(0,1\), and mutually isolated four-vertex paths on vertices \(4k+2,\ldots,4k+5\), \(k\ge0\), with edge triples \(q^{4k}(q^2,tq^3,q^4)\). As \(q<1\), the top eigenvalue of all those latter blocks is that of the first four-vertex path \(B\). The characteristic polynomial of a four-vertex weighted path with edge weights \((a,b,d)\) is
\[
\det(\lambda I-B)=\lambda^4-(a^2+b^2+d^2)\lambda^2+a^2d^2.
\]
Its largest positive root is strictly increasing in \(b>0\), and equals \(1\) exactly when \(b^2=(1-a^2)(1-d^2)\). Taking \(a=q^2\), \(b=tq^3\), \(d=q^4\) yields \(t=c_*(q)\). Therefore
\[
w(T_{q,0,c})=\tfrac12 \quad\Longleftrightarrow\quad 0\le c\le c_*(q).
\]
For every \(s>0\), the leading three-vertex principal submatrix has edge weights \((1,sq)\), hence its largest eigenvalue is \(\sqrt{1+s^2q^2}>1\). Consequently \(w(T_{q,s,t})>1/2\) whenever \(s>0\). This proves the first phase and the nonattainment assertion.

**3. Uniqueness, interior attainment, and curvature.** Write \(S_{q,s,t}=S_0+sA+tB\), where \(S_0\) carries edges of even index, \(A\) edges of index \(4k+1\) with weight \(q^{4k+1}\), and \(B\) edges of index \(4k+3\) with weight \(q^{4k+3}\). (The symbol \(B\) here denotes the operator carrying the second modulated edge family, not the finite block in Step 2.) The largest-eigenvalue functional is convex in \((s,t)\). It is strictly convex on the positive quadrant: equality at two different parameters would supply a common positive top eigenvector \(v\) for both Jacobi operators. Their row at index \(0\) forces identical top eigenvalues, row \(1\) then forces identical \(s\), and row \(3\) forces identical \(t\), a contradiction. More strongly, for a nonzero parameter direction \(D\), the second-derivative spectral formula has strictly positive value: it could vanish only if \(Dv\) were proportional to \(v\); row \(0\) forces the proportionality constant zero and rows \(1,3\) force both direction coefficients zero. Thus the analytic Hessian is positive definite.

For \(c>c_*(q)\), at \((s,t)=(0,c)\), the simple top eigenvector is supported on the first nontrivial four-vertex block. Varying \(s\) from zero couples previously disconnected blocks, so the one-sided first derivative in \(s\) is zero; decreasing \(t\) has a strictly negative first derivative, since the positive top eigenvector has positive entries across the \(tq^3\) edge. Hence the value strictly falls when one moves into the segment. At the other endpoint \((c,0)\), the top eigenvector lives on vertices \(0,1,2,3\), whose later copies are scaled by \(q^4\); increasing \(t\) from zero gives zero first derivative, whereas decreasing \(s\) strictly lowers the top eigenvalue. Thus both endpoints are worse than nearby interior points. Convexity on the compact closed segment gives existence and interior attainment; strict convexity yields uniqueness. The positive-definite Hessian and the implicit function theorem imply real-analytic dependence of the minimizer on \(c>c_*(q)\), and the minimized value has positive second derivative (the positive Schur complement of the Hessian). Its first derivative is positive because the two partial derivatives at the interior optimum coincide and each is strictly positive by the positive-eigenvector formula. Finally, the strict lower bound \(w>1/2\) persists at every point of the closed segment for \(c>c_*(q)\).

**4. Exact large-budget asymptotics.** The operators \(A\) and \(B\) consist of disjoint two-vertex edges and satisfy \(\|A\|=q\), \(\|B\|=q^3\), while \(\|S_0\|=1\). Their supports are mutually disjoint, so, for \(0\le x\le1\),
\[
\lambda_{\max}(xA+(1-x)B)=\max\{qx,q^3(1-x)\}.
\]
The unique minimizing fraction is \(x_0=q^2/(1+q^2)\), with optimal leading eigenvalue \(a=q^3/(1+q^2)\). Write \(s=cx_0+y\), \(t=c(1-x_0)-y\). The choice \(y=0\) gives \(\lambda_{\max}(S)\le ca+1\). On the other hand, the principal two-vertex blocks give \(\lambda_{\max}(S)\ge\max\{sq,tq^3\}\). Thus at any optimal allocation \(y\) stays in the fixed bounded interval \([-q^{-3},q^{-1}]\).

At \(x=x_0\), the top eigenvalue \(a\) of \(x_0A+(1-x_0)B\) is exactly double, with normalized eigenvectors \(u=(e_1+e_2)/\sqrt2\) and \(v=(e_3+e_4)/\sqrt2\). Every other eigenvalue is at most \(q^4a<a\). The compression of \(S_0+y(A-B)\) to the span of \(u,v\) is the matrix
\[
M_y=\begin{pmatrix} qy&q^2/2\\ q^2/2&-q^3y\end{pmatrix}.
\]
The spectral gap of size \(\delta=a(1-q^4)>0\) controls the Schur complement onto its orthogonal complement. In detail, for \(|y|\le K\), put \(M=1+K(q+q^3)\); then \(\|S_0+y(A-B)\|\le M\), the complementary top spectral value is at most \(ca-c\delta+M\), and the full top eigenvalue is at least \(ca-M\). For \(c\delta>2M\), the Schur-complement correction is positive semidefinite and has norm at most \(M^2/(c\delta-2M)\). The compression supplies the matching lower bound, and thus the uniform \(O(c^{-1})\) estimate follows without relying on a finite-section limit. Uniformly for bounded \(y\),
\[
\lambda_{\max}(S_{q,cx_0+y,c(1-x_0)-y})=ca+\lambda_{\max}(M_y)+O(c^{-1}).
\]
The scalar function
\[
\lambda_{\max}(M_y)=\tfrac12\left(q(1-q^2)y+\sqrt{q^2(1+q^2)^2y^2+q^4}\right)
\]
is strictly convex, with its unique minimum attained at \(y_*=- (1-q^2)/(2(1+q^2))\), of value \(a\). Uniform convergence on a bounded set containing every optimal \(y\) yields \(y\to y_*\) and \(\lambda_{\max}(S)=a(c+1)+o(1)\). Dividing by \(2\) gives exactly the displayed asymptotics.

## Verification
The accompanying reproducibility script `verify_weighted_shift_budget.py` checks exact rational four-vertex characteristic identities and effective two-state eigenvalue equations. It also computes finite Jacobi truncations at several geometric ratios and verifies the predicted endpoint/interior behavior and large-budget leading and constant terms numerically. The infinite-dimensional theorem follows from the preceding analytic spectral and convexity arguments; no numerical enumeration is claimed to be an infinite proof.

## Relationship to prior work
Ghosh, Birbonshi and Ojha introduced the specific four-periodically modulated geometric shift in 2026, studied numerical-radius bounds, and represented its radius through a determinantal entire function. Their publicly indexed abstract and a detailed secondary description address evaluation for fixed positive \(s,t\), not optimization along a fixed \(s+t\) segment. The manuscript's full text was not obtainable through the available legal routes, so an unlocated result within it remains a stated originality risk. Chakraborty, Ojha and Birbonshi's 2022 primary paper gives determinantal polynomials for weighted shifts with eventually alternating nonzero weights; its principally different tail model and theorem statements do not yield the present compact geometric family or its exact budget threshold. Classical compact-self-adjoint perturbation and Perron eigenvalue principles are used explicitly as proof tools, not claimed as new independent discoveries.

## Limitations
The numerical-radius optimum has no positive-parameter minimizer in the lower-budget phase, even though the closure has an explicit one. The two-term expansion is for fixed \(q\) and \(c\to\infty\), without endpoint-uniform remainder. No explicit elementary formula for the full interior optimizer at finite \(c>c_*(q)\) is asserted. The full 2026 source manuscript was not inspected because the full preprint was not accessible through the available lawful sources. Accordingly, the originality assessment retains a meaningful risk of an unindexed or unpublished equivalent result, and independent scientific review has not occurred.

## References
1. A. Ghosh, R. Birbonshi and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486, first submitted 2026-08-18, https://arxiv.org/abs/2608.17486.
2. B. Chakraborty, S. Ojha and R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, Operators and Matrices **16** (2022), 1155–1174, DOI:10.7153/oam-2022-16-75, https://files.ele-math.com/articles/oam-16-75.pdf.
3. Q. F. Stout, *The numerical range of a weighted shift*, Proceedings of the American Mathematical Society **88** (1983), 495–502. (Background determinant method, as cited in Reference 2.)
