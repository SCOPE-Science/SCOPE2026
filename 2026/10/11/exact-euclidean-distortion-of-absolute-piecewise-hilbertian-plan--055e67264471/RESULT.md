# Exact Euclidean distortion of absolute piecewise-Hilbertian planes
## Finding
For every \(a,c>0\) and \(0\le b\le\sqrt{ac}\), let \(N_{a,b,c}(x,y)=\sqrt{a x^2+2b|xy|+c y^2}\) on \(\mathbb R^2\). Then \(N_{a,b,c}\) is a norm and its Euclidean Banach--Mazur distance satisfies \[d_{\mathrm{BM}}((\mathbb R^2,N_{a,b,c}),\ell_2^2)^2=1+\frac{b}{\sqrt{ac}}.\] An optimal Euclidean pullback is \(H_{a,c}(x,y)=\sqrt{a x^2+c y^2}\), up to positive scale.

Equivalently, after the linear normalization \(u=\sqrt{a}x\), \(v=\sqrt{c}y\), the family is the one-parameter absolute norm
\[
N_r(u,v)=\sqrt{u^2+2r|uv|+v^2},\qquad 0\le r\le1,
\]
where \(r=b/\sqrt{ac}\), and its squared Euclidean Banach--Mazur distance is exactly \(1+r\).

## Assumptions and scope
The scalars are real. The parameters satisfy \(a,c>0\) and \(0\le b\le\sqrt{ac}\). For \(b<\sqrt{ac}\), define
\[
q_\pm(x,y)=a x^2\pm2bxy+c y^2.
\]
Both quadratic forms are positive definite and
\[
N_{a,b,c}=\max\{\sqrt{q_+},\sqrt{q_-}\}.
\]
Thus the norm is the maximum of two Hilbert norms. At \(b=\sqrt{ac}\), the same formula becomes \(N_{a,b,c}(x,y)=\sqrt{a}|x|+\sqrt{c}|y|\), so the endpoint is a weighted \(\ell_1^2\) norm. The claim concerns only the exact distance to a Hilbert plane and one optimal pullback; it does not assert uniqueness of the optimal pullback.

## Proof
Let \(Q\) be an arbitrary positive-definite real symmetric matrix and write \(H_Q(z)^2=z^TQz\). Put
\[
m_Q=\inf_{z\ne0}\frac{N_{a,b,c}(z)^2}{H_Q(z)^2},\qquad
M_Q=\sup_{z\ne0}\frac{N_{a,b,c}(z)^2}{H_Q(z)^2}.
\]
Then the squared distortion supplied by \(H_Q\) is \(M_Q/m_Q\), and the squared Banach--Mazur distance is the infimum of this ratio over all positive-definite \(Q\).

The norm is invariant under the four independent coordinate sign changes. If
\[
m_QH_Q(z)^2\le N_{a,b,c}(z)^2\le M_QH_Q(z)^2,
\]
apply the inequality to every sign change and average the four quadratic forms. The off-diagonal entries cancel, giving a positive diagonal form \(\overline Q=\operatorname{diag}(u,v)\) with exactly the same admissible constants \(m_Q,M_Q\). Hence no nondiagonal form can improve the infimum, and it suffices to optimize over \(u,v>0\).

For \(H(x,y)^2=u x^2+v y^2\), absolute symmetry allows restriction to \(x,y\ge0\). Set
\[
A=\frac au,\qquad C=\frac cv,\qquad r=\frac b{\sqrt{ac}},\qquad
t=\frac{y\sqrt v}{x\sqrt u}\ge0.
\]
For \(x\ne0\),
\[
\frac{N_{a,b,c}(x,y)^2}{H(x,y)^2}
=
\frac{A+2r\sqrt{AC}t+Ct^2}{1+t^2}.
\]
This is the Rayleigh quotient, on the nonnegative quadrant, of
\[
S=\begin{pmatrix}A&r\sqrt{AC}\\r\sqrt{AC}&C\end{pmatrix}.
\]
Its maximum on that quadrant is the Perron eigenvalue
\[
\lambda_+=\frac{A+C+\sqrt{(A-C)^2+4r^2AC}}2,
\]
while its minimum is \(\min\{A,C\}\) because the other eigenvector has opposite signs when \(r>0\), so the minimum occurs on a coordinate axis; the statement is immediate also for \(r=0\).

Scale by \(m=\min\{A,C\}\) and put \(z=\max\{A,C\}/m\ge1\). Every diagonal pullback therefore has squared distortion
\[
D_r(z)=\frac{z+1+\sqrt{(z-1)^2+4r^2z}}2.
\]
We claim \(D_r(z)\ge1+r\). This is equivalent to
\[
\sqrt{(z-1)^2+4r^2z}\ge2r-(z-1).
\]
If the right side is nonpositive there is nothing to prove. Otherwise both sides are nonnegative and squaring is legitimate; the difference of their squares is
\[
4r(r+1)(z-1)\ge0.
\]
Thus every Hilbert pullback has squared distortion at least \(1+r\).

Now take \(u=a\) and \(v=c\). Then
\[
\frac{N_{a,b,c}(x,y)^2}{a x^2+c y^2}
=1+\frac{2b|xy|}{a x^2+c y^2}.
\]
The weighted arithmetic--geometric mean inequality gives \(2\sqrt{ac}|xy|\le a x^2+c y^2\), so this ratio ranges from \(1\) on the coordinate axes to \(1+r\) when \(\sqrt{a}|x|=\sqrt{c}|y|\). Hence \(H_{a,c}\) attains squared distortion \(1+r\), matching the lower bound.

## Verification
The proof covers every parameter in the closed range. At \(b=0\), the norm is already Hilbertian and the formula gives distance \(1\). At \(b=\sqrt{ac}\), the norm is linearly isometric to \(\ell_1^2\) and the formula gives squared distance \(2\), the standard planar endpoint. For the two-dimensional Cesàro norm
\[
\|(x,y)\|^2=|x|^2+\left(\frac{|x|+|y|}2\right)^2,
\]
one has \(a=5/4\), \(b=1/4\), and \(c=1/4\), so the theorem gives \(d_{\mathrm{BM}}^2=1+1/\sqrt5\), consistent with the known special case.

No finite experiment is used as proof. The decisive steps are the exact sign-averaging reduction, the closed Rayleigh-quotient extremum, and the global one-variable inequality for \(D_r\).

## Relationship to prior work
Z. Zuo's 2012 paper *The Ptolemy constant of absolute normalized norms on R^2* develops the absolute-normalized-plane framework and computes the Ptolemy constant of the two-dimensional Cesàro space. Its Example 2.10 contains the same Cesàro plane that appears as the parameter choice \(a=5/4\), \(b=1/4\), \(c=1/4\) above. The inspected full text does not state an exact Euclidean Banach--Mazur distance theorem for the full quadratic-absolute family.

Searches under absolute-normalized norms, piecewise quadratic norms, maxima of Hilbert norms, optimal ellipses, and the canonical form \(\sqrt{u^2+2r|uv|+v^2}\) located exact-distance results for several other planar families and the isolated Cesàro special case, but not this all-parameter formula. The present statement therefore packages the isolated example into a complete intrinsic law governed only by the normalized coupling \(r=b/\sqrt{ac}\).

## Limitations
The originality search cannot exclude an equivalent theorem hidden under older convex-body or ellipsoid-approximation terminology. The argument is specific to real dimension two and to a single absolute quadratic coupling; it does not directly cover higher-dimensional maxima of quadratic forms or arbitrary absolute normalized norms. No independent audit has been performed.

## References
1. Z. Zuo, *The Ptolemy constant of absolute normalized norms on R^2*, Journal of Inequalities and Applications 2012, Article 107, DOI: 10.1186/1029-242X-2012-107.
