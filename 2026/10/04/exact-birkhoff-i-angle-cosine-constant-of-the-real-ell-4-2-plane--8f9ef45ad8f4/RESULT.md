# Exact Birkhoff i-angle cosine constant of the real \(\ell_4^2\) plane
## Finding
For the real Banach plane \(X=\ell_4^2\), define the Birkhoff i-angle cosine constant by
\[
C_B(X)=\sup\left\{\frac{\|x+y\|_4^2-\|x-y\|_4^2}{4}:x,y\in S_X,\ x\perp_B y\right\}.
\]
Then
\[
C_B(\ell_4^2)=\sqrt{\frac16-\frac{u_0^2}{2}}=0.2873902713995240563\ldots,
\]
where \(u_0\in(0,1)\) is the unique zero of
\[
9u^4+18u^3+3u^2-2=0.
\]
A maximizing Birkhoff-orthogonal pair is obtained from
\[
z=\frac{u_0^2}{1+3u_0^2},\qquad t=\frac{1-\sqrt{1-4z}}2,
\]
by
\[
x=(t^{1/4},(1-t)^{1/4}),\qquad
 y=c((1-t)^{3/4},-t^{3/4}),\qquad
 c=(t^3+(1-t)^3)^{-1/4}.
\]
Numerically,
\[
u_0=0.4100573095838545636\ldots,
\]
with one corresponding pair approximately
\[
x=(0.5983766859171193,0.9662818571477868),\qquad
y=(0.9992065344662093,-0.2372836323062247).
\]

## Assumptions and scope
The scalar field is real and \(X=\mathbb R^2\) carries the \(\ell_4\) norm.  Birkhoff orthogonality is \(x\perp_B y\) when \(\|x+\lambda y\|_4\ge \|x\|_4\) for every real \(\lambda\).  The constant is the one introduced by Du and Li from the cosine of the i-angle, specialized to unit vectors.  The result concerns this one canonical smooth two-dimensional space; it does not claim a formula for \(\ell_p^2\) for arbitrary \(p\).

## Proof
Write \(x=(a,b)\in S_X\).  Since \(\ell_4^2\) is smooth, its unique norming functional is proportional to \((a^3,b^3)\), so
\[
x\perp_B y\quad\Longleftrightarrow\quad a^3y_1+b^3y_2=0.
\]
Coordinate sign changes and interchange are linear isometries.  Hence, after these symmetries and possibly replacing \(y\) by \(-y\), it suffices to take \(a,b\ge0\) and
\[
y=c(b^3,-a^3),\qquad c=(a^{12}+b^{12})^{-1/4}.
\]
This vector has \(\|y\|_4=1\) and is Birkhoff orthogonal to \(x\).

Set
\[
u=\frac{a^2b^2}{\sqrt{a^{12}+b^{12}}}.
\]
Because \(a^4+b^4=1\), if \(A=a^4\), \(B=b^4\), and \(z=AB\), then
\[
u^2=\frac{z}{1-3z},\qquad 0\le z\le\frac14.
\]
Thus \(u\) runs through the entire interval \([0,1]\).

Let
\[
P=\|x+y\|_4^4,\qquad M=\|x-y\|_4^4.
\]
Expanding the two fourth powers and using \(a^4+b^4=1\) gives
\[
P+M=4(1+3u).
\]
The odd terms give
\[
|P-M|=8\sqrt{u(1-u^2)}.
\]
Consequently
\[
PM=4(1+2u+9u^2+4u^3).
\]
If \(F(u)\) denotes the nonnegative value of the i-angle cosine after orienting \(y\), then
\[
F(u)^2
 =\frac{(\sqrt P-\sqrt M)^2}{16}
 =\frac{1+3u-\sqrt{1+2u+9u^2+4u^3}}4.
\]
Differentiating on \((0,1)\),
\[
\frac{d}{du}F(u)^2
=\frac14\left(3-\frac{1+9u+6u^2}{\sqrt{1+2u+9u^2+4u^3}}\right).
\]
All quantities being compared are positive, so the critical-point equation can be squared without introducing a sign ambiguity.  A direct expansion gives
\[
(1+9u+6u^2)^2-9(1+2u+9u^2+4u^3)
=4(9u^4+18u^3+3u^2-2).
\]
The polynomial on the right is strictly increasing for \(u>0\), since its derivative is
\[
6u(6u^2+9u+1)>0,
\]
and its values at \(0\) and \(1\) have opposite signs.  Therefore there is exactly one root \(u_0\in(0,1)\); the derivative of \(F(u)^2\) is positive before \(u_0\) and negative after it.  Hence \(u_0\) is the unique global maximizer.

At the critical point,
\[
\sqrt{1+2u_0+9u_0^2+4u_0^3}=\frac{1+9u_0+6u_0^2}{3},
\]
so substitution simplifies the maximum to
\[
F(u_0)^2=\frac16-\frac{u_0^2}{2}.
\]
Taking the positive square root proves the formula.  Solving \(z=u_0^2/(1+3u_0^2)\) and \(t(1-t)=z\) gives the displayed maximizing pair.

## Verification
The bundled script `artifacts/verify.py` uses only the Python standard library.  It checks the polynomial identity in the stationary equation with exact rational arithmetic, isolates the unique root by bisection at high precision, reconstructs the displayed maximizing pair, verifies both unit norms and the Birkhoff equation numerically, and recomputes the objective.  A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Du and Li introduced \(C_B(X)\), proved general inequalities and the universal bound \(0\le C_B(X)\le3/4\), and gave exact upper-bound examples such as the square and an affine-regular hexagonal plane.  Their complete article does not provide an exact value for \(\ell_4^2\).  Ji and Wu's earlier invariant \(D(X)\) quantifies the discrepancy between Birkhoff and isosceles orthogonality and was computed for two-dimensional \(\ell_p\) spaces, but Du and Li relate \(C_B\) to \(D\) only by inequalities, so those computations do not imply the formula above.  A later skew-constant paper studies a different first-power norm-difference functional under Birkhoff orthogonality and likewise does not imply this exact i-angle value.

## Limitations
This is an exact computation for \(\ell_4^2\), not a general \(p\)-formula.  The literature comparison covered the defining full article, the closest discrepancy and skew-constant literature, targeted exact-formula searches, and a semantic published-results index; unindexed or differently named prior work remains a residual originality risk.  Independent audit has not been performed.

## References
1. D. Du and Y. Li, *Some Geometric Constants Related to the Sine Function and Cosine Function in Banach Spaces*, Vietnam Journal of Mathematics, published online 14 June 2024, DOI 10.1007/s10013-024-00696-w.
2. D. Ji and S. Wu, *Quantitative characterization of the difference between Birkhoff orthogonality and isosceles orthogonality*, Journal of Mathematical Analysis and Applications 323 (2006), 1–7, DOI 10.1016/j.jmaa.2005.10.004.
3. Y. Zhou, R. Ni, and B. Liu, *The skew constant and orthogonalities in Banach spaces*, Open Journal of Mathematical Sciences 8 (2024), DOI 10.30538/oms2024.0219.
