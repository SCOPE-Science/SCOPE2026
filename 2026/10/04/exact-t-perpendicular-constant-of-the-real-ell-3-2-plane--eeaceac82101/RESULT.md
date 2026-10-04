# Exact \(T_{\perp}\) constant of the real \(\ell_3^2\) plane
## Finding
For the real Banach plane \(X=\ell_3^2\), define the Birkhoff--James orthogonality constant introduced by Ahmad, Xie and Li by
\[
T_{\perp}(X)=\sup\left\{\sqrt{\|x+y\|_3\,\|2x-y\|_3}:x,y\in S_X,\ x\perp_B y\right\}.
\]
Let \(u_*\) be the unique zero in \(0<u<1\) of
\[
Q(u)=729u^{17}+8289u^{16}+26784u^{15}+14904u^{14}-34128u^{13}-82944u^{12}-300448u^{11}+174168u^{10}-140086u^9+530922u^8+208224u^7+210728u^6+23864u^5-102168u^4-93792u^3-51128u^2-13707u-1331.
\]
Set
\[
r_* = \left(\frac{u_*(1+u_*)^2}{(1+u_*^2)^2}\right)^{1/3}.
\]
Then
\[
T_{\perp}(\ell_3^2)
=\left[\left(\frac{2}{1+u_*^2}+3r_*\right)
\left(\frac{7+9u_*^2}{1+u_*^2}+6r_*\right)\right]^{1/6}.
\]
The zero is isolated by \(0.7578975<u_*<0.7578976\), and therefore
\[
T_{\perp}(\ell_3^2)=1.96396141891920273469\ldots.
\]
The supremum is attained. If the coordinates of the first unit vector are ordered by magnitude, the maximizing coordinate ratio is \(t_*=u_*^{1/3}=0.91173822074151938717\ldots\).

## Assumptions and scope
The scalar field is real. The norm is \(\|(a,b)\|_3=(|a|^3+|b|^3)^{1/3}\). Birkhoff--James orthogonality is \(x\perp_B y\) when \(\|x+\lambda y\|_3\ge \|x\|_3\) for every real \(\lambda\). The statement concerns only the two-dimensional space \(\ell_3^2\).

## Proof
Because \(\ell_3^2\) is smooth, \(x\perp_B y\) is equivalent to the norming functional at \(x\) annihilating \(y\). Signed coordinate permutations are isometries. Hence, after applying such an isometry, every admissible pair can be written with
\[
x=\frac{(1,t)}{(1+t^3)^{1/3}},\qquad 0\le t\le1,
\]
and one of the two unit tangent directions
\[
y_+=\frac{(-t^2,1)}{(1+t^6)^{1/3}},\qquad y_-=-y_+.
\]
Indeed, the orthogonality equation is \(x_1|x_1|y_1+x_2|x_2|y_2=0\), so the one-dimensional tangent direction is proportional to \((-t^2,1)\).

Write \(u=t^3\) and
\[
c=\left(\frac{1+u}{1+u^2}\right)^{1/3},\qquad
r=tc^2=\left(\frac{u(1+u)^2}{(1+u^2)^2}\right)^{1/3}.
\]
Using the common denominator \((1+t^3)^{1/3}\), the positive orientation is \(y_+=(-ct^2,c)/(1+t^3)^{1/3}\). The sign of the only ambiguous coordinate in \(2x-y_+\) changes when \(2t=c\). In terms of \(u\), this transition is the unique root \(u_0\in(0,7/50)\) of
\[
8u^3+7u-1=0.
\]
For \(u\ge u_0\), direct expansion gives
\[
\|x+y_+\|_3^3=\frac{2}{1+u^2}+3r,
\]
and
\[
\|2x-y_+\|_3^3=\frac{7+9u^2}{1+u^2}+6r.
\]
Thus the sixth power of the objective is
\[
P_+(u)=\left(\frac{2}{1+u^2}+3r\right)
\left(\frac{7+9u^2}{1+u^2}+6r\right).
\]
To locate every stationary point without numerical optimization, differentiate before eliminating \(c\), subject to \(c^3(1+t^6)=1+t^3\). The resultant of the implicit derivative numerator with this cubic constraint has, for \(t>0\), the only potentially vanishing factor \(Q(t^3)\) displayed above. Exact Sturm counting gives exactly one zero of \(Q\) in \((0,1)\); it lies in \((0.7578975,0.7578976)\). The implicit derivative is positive at \(t=4/5\) and negative at \(t=19/20\), so this unique stationary point is the global maximum on the upper-sign branch \([u_0,1]\).

On the lower-sign branch \(0<u<u_0\), the corresponding resultant factor \(R_s(u)\) has no zero in \((0,7/50)\), while the actual derivative is positive at \(t=2/5\). Hence this branch is strictly increasing up to \(u_0\), so it cannot beat the unique upper-branch maximum.

It remains to treat \(y_-\). Its two relevant norm cubes have no sign transition for \(0<t<1\). The derivative resultant factor \(R_-(u)\) has exactly one zero in \((0,1)\); the actual derivative is negative at \(t=1/10\) and positive at \(t=1/5\). Therefore this unique stationary point is a minimum, and the maximum for the negative orientation occurs at an endpoint. Those endpoint values are \(18^{1/6}\) at \(t=0\) and \(56^{1/6}\) at \(t=1\). The positive branch already satisfies \(P_+(3/4)>56\), so its interior maximum strictly dominates both endpoints of the negative orientation.

Consequently the unique maximizing parameter is \(u_*\), and substitution into \(P_+(u)\) gives the stated exact formula for \(T_{\perp}(\ell_3^2)\).

## Verification
The standalone script `verify_tperp_l3.py` uses exact rational Sturm sequences for the three elimination polynomials, verifies the branch root counts and the isolating interval for \(u_*\), checks the signs of the actual implicit derivative at rational sample points, and recomputes the final value to high precision. Running `python3 verify_tperp_l3.py` returns `VERIFY_OK`. The Sturm computations are finite exact algebra; the decimal calculations only reconstruct and display the isolated algebraic value.

## Relationship to prior work
Ahmad, Xie and Li introduced \(T_{\perp}(X)\), proved the universal bounds \(\sqrt2\le T_{\perp}(X)\le\sqrt6\), computed the max-norm planar extremal case and the Hilbert-space value \(10^{1/4}\), and stated in their conclusion that values on further specific spaces remained to be investigated. Their paper does not give the value on \(\ell_3^2\). The exact computation above fills one of those concrete-space gaps and is not implied by the universal bounds or the Hilbert/max-norm cases.

A later paper on skew geometric constants by Ni, Liu and Zhou studies different two-parameter constants. Its inspected title, abstract, introduction and searchable full text do not supply this \(T_{\perp}(\ell_3^2)\) value.

## Limitations
No formula is claimed here for \(T_{\perp}(\ell_p^2)\) at general \(p\), nor for higher-dimensional \(\ell_3\). The exact answer is algebraic but is given through the unique root of a degree-seventeen polynomial rather than radicals. The originality search cannot exclude an unindexed source using substantially different notation; this residual risk is recorded in the review materials.

## References
1. A. Ahmad, H. Xie, Y. Li, “Some new geometric constants in Banach spaces,” *Advances in Fixed Point Theory* 12 (2022), Article 9. DOI: 10.28919/afpt/7588.
2. Q. Ni, Q. Liu, Y. Zhou, “Some aspects of new skew geometric constants in Banach spaces,” *Mathematical Inequalities & Applications* 28 (2025), 327–342. DOI: 10.7153/mia-2025-28-22.
