# Exact \(H_3\) constant of the real \(\ell_3^2\) plane
## Finding
For the real Banach plane \(X=\ell_3^2\), let
\[
H_3(X)=\sup\left\{\frac{(1+\lambda^3)^{1/3}}{\|x+\lambda y\|_3}:x,y\in S_X,\ x\perp_I y,\ \lambda\ge0\right\},
\]
where \(x\perp_I y\) means \(\|x+y\|_3=\|x-y\|_3\). Let \(t_*\in(0,1)\) be the unique root of
\[
t^4+6t^3+4t^2+2t-1=0.
\]
Then
\[
H_3(\ell_3^2)=\left(\frac{(1+t_*^3)^2}{8t_*^3+(1-t_*^2)^3}\right)^{1/3}
=1.0290679924451534009\ldots.
\]
The supremum is attained. If
\[
b=(1+t_*^3)^{-1/3},\qquad a=t_*b,
\]
then one maximizing configuration is
\[
x=(a,b),\qquad y=(b,-a),\qquad \lambda=t_*.
\]

## Assumptions and scope
All scalars are real. The norm is \(\|(u,v)\|_3=(|u|^3+|v|^3)^{1/3}\). The constant is exactly the Baronti–Bertella \(p\)-isosceles constant specialized to \(p=3\); it is not the classical isosceles constant and not a Birkhoff–James orthogonality constant. The statement concerns only the plane \(\ell_3^2\).

## Proof
First classify the isosceles-orthogonal unit pairs. For nonnegative \(u,v\), write
\[
\Phi(u,v)=|u+v|^3-|u-v|^3.
\]
For positive arguments, \(\Phi\) is symmetric and strictly increasing in each argument. After coordinate sign changes, an isosceles-orthogonal unit pair can be written as
\[
x=(a,b),\qquad y=(c,-d),\qquad a,b,c,d\ge0,
\]
with \(a^3+b^3=c^3+d^3=1\). The condition \(\|x+y\|_3=\|x-y\|_3\) becomes
\[
\Phi(a,c)=\Phi(b,d).
\]
If \(c>b\), equality of the two unit-cube sums forces \(a>d\); symmetry and strict monotonicity then give \(\Phi(a,c)=\Phi(c,a)>\Phi(b,d)\), a contradiction. The case \(c<b\) is symmetric. Hence \(c=b\) and \(d=a\). Boundary zero cases follow directly. Swapping the two vectors if necessary and applying the same signed-coordinate isometry therefore reduces every pair to
\[
x=(a,b),\qquad y=(b,-a),\qquad 0\le a\le b,
\qquad a^3+b^3=1.
\]
Put \(r=a/b\in[0,1]\), so \(b=(1+r^3)^{-1/3}\).

The symmetry reduction for the source constant permits \(0\le\lambda\le1\) provided both ordered branches are considered. For the branch \(x+\lambda y\), cubing the ratio gives
\[
F(r,\lambda)=
\frac{(1+\lambda^3)(1+r^3)}{(r+\lambda)^3+(1-r\lambda)^3}.
\]
For the reversed branch \(y+\lambda x\), cubing gives
\[
G(r,\lambda)=
\frac{(1+\lambda^3)(1+r^3)}{(1+r\lambda)^3+|\lambda-r|^3}.
\]
The latter never exceeds \(1\). Indeed, when \(\lambda\ge r\), denominator minus numerator equals
\[
r\bigl(3\lambda^2r-3\lambda^2+3\lambda r+3\lambda-2r^2\bigr).
\]
As a function of \(r\in[0,\lambda]\), the bracket is concave, and its endpoint values are \(3\lambda(1-\lambda)\) and \(\lambda(3\lambda^2-2\lambda+3)\), both nonnegative. When \(r\ge\lambda\), the analogous difference is
\[
\lambda\bigl(-2\lambda^2+3\lambda r^2+3\lambda r-3r^2+3r\bigr),
\]
which is concave in \(\lambda\in[0,r]\) and has nonnegative endpoint values \(3r(1-r)\) and \(r(3r^2-2r+3)\). Thus only \(F\) can improve on the trivial value \(1\).

The function \(F\) is symmetric in \(r\) and \(\lambda\). Clearing its positive denominators, the two interior stationarity equations are
\[
\begin{aligned}
A(r,\lambda)={}&2\lambda^2r^2+\lambda r^4+2\lambda r^3-2\lambda r-\lambda+r^4-2r^3-2r+1=0,\\
B(r,\lambda)={}&\lambda^4r+\lambda^4+2\lambda^3r-2\lambda^3+2\lambda^2r^2-2\lambda r-2\lambda-r+1=0.
\end{aligned}
\]
Eliminating \(\lambda\) gives the exact factorization
\[
\operatorname{Res}_{\lambda}(A,B)
=2(r-1)(r^2+1)^4 q_4(r)q_6(r),
\]
where
\[
q_4(r)=r^4+6r^3+4r^2+2r-1
\]
and
\[
q_6(r)=r^6-4r^5+5r^4-8r^3+7r^2-4r-1.
\]
The polynomial \(q_4\) is strictly increasing on \([0,1]\), changes sign between \(1/4\) and \(3/10\), and therefore has a unique root \(t_*\) there. The polynomial \(-q_6\) is strictly positive on \([0,1]\): in the degree-six Bernstein basis its coefficients are
\[
1,\quad \frac53,\quad \frac{28}{15},\quad 2,\quad \frac{32}{15},\quad \frac83,\quad 4.
\]
Applying the same symmetric elimination in the other variable shows that the unique interior critical point is \((r,\lambda)=(t_*,t_*)\).

On the boundary, \(F(r,0)=1\), and
\[
\frac{d}{dr}F(r,1)=
\frac{3r(r-1)(r^2+r+2)}{(3r^2+1)^2}\le0,
\]
so the boundary maximum is \(1\); symmetry handles the remaining edges. At the diagonal point,
\[
(1+r^3)^2-\bigl(8r^3+(1-r^2)^3\bigr)
=r^2(2r^4-3r^2-6r+3).
\]
The last factor is decreasing on \([0,3/10]\) and equals \(4731/5000>0\) at \(r=3/10\), so \(F(t_*,t_*)>1\). Therefore this unique interior point is the global maximizer. Substituting \(r=\lambda=t_*\) yields
\[
H_3(\ell_3^2)^3=F(t_*,t_*)
=\frac{(1+t_*^3)^2}{8t_*^3+(1-t_*^2)^3},
\]
which proves the formula and the displayed attaining vectors.

## Verification
Run `python3 verify_h3_l3.py`. The standalone checker uses only the Python standard library. It reconstructs the crucial resultant identity by exact Sylvester determinants at enough integer values to certify the polynomial identity from its degree bound, verifies the positive Bernstein expansion of \(-q_6\), checks the root bracket and boundary inequalities with exact rational arithmetic, and reconstructs the final algebraic value at high precision. A successful replay prints `VERIFY_OK`. The decimal reconstruction is supplementary; the global maximum is established by the exact argument above.

## Relationship to prior work
Baronti and Bertella introduced \(H_p\), proved universal bounds, computed the Hilbert-space and \(\ell_\infty^2\) cases, and studied equality versus uniform non-squareness. Their accepted manuscript does not state the value of \(H_3\) on \(\ell_3^2\). The exact computation above supplies a classical smooth non-Hilbert benchmark in which the optimizer is genuinely interior and algebraic.

Public comparison records were also checked for the same invariant, same space, equivalent formulations, and stronger statements. A record on \(H_4\) gives a uniformly non-square hexagonal counterexample to an equality conjecture, not an \(H_3(\ell_3^2)\) value. Other close records compute a Birkhoff-orthogonal \(T_\perp\) constant and a Dragomir-symmetry constant on \(\ell_3^2\), or a generalized James constant on \(\ell_p\); those are different functionals and do not imply the formula here.

## Limitations
No formula is claimed for \(H_p(\ell_q^2)\) at general exponents, for higher-dimensional \(\ell_3\), or for complex scalars. The originality assessment is based on the inspected primary source, targeted public-database searches, and statement-level implication comparisons; an unindexed source using substantially different notation remains a residual risk.

## References
1. M. Baronti and V. Bertella, “A Generalization of the Isosceles Constant in Banach Spaces,” *Mediterranean Journal of Mathematics* 21 (2024), Article 113, DOI: 10.1007/s00009-024-02654-9. Earliest public online date verified here: 2024-05-04.
2. Accepted manuscript repository record, University of Genoa, handle 11567/1182495.
