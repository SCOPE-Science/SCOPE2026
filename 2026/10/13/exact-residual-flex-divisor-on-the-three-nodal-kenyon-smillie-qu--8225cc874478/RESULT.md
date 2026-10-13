# Exact residual flex divisor on the three-nodal Kenyon–Smillie quartic
## Finding
Let \(C_1\subset\mathbb P^2_{\mathbb Q}\) be the singular Kenyon–Smillie quartic at \(t=1\), in the coordinates used by Lax. Lax determines the three nodes, the fixed hyperflex \(H=[0:-1:1]\), the fixed flex \(P_0=[0:0:1]\), and gives only three-decimal approximations for the remaining three smooth weight-one Weierstrass points.

Those three residual points form one reduced irreducible degree-three divisor over \(\mathbb Q\). Explicitly, if \(\alpha\) runs over the roots of
\[
q(T)=106T^3+3T^2-6T-2,
\]
then the residual flexes are exactly
\[
R_\alpha=\left[\alpha:-\frac{106\alpha^2+23\alpha+3}{19}:1\right].
\]
The cubic \(q\) is irreducible over \(\mathbb Q\), has discriminant
\[
\operatorname{disc}(q)=-1026^2,
\]
and therefore has Galois group \(\mathrm S_3\). In particular, the residual divisor is one Galois orbit, consisting of one real flex and one complex-conjugate pair.

Writing
\[
n(T)=T^3-3T+1,
\qquad
N_a=[a:1-a-a^2:1]\quad(n(a)=0),
\]
the complete canonical Weierstrass zero-cycle on \(C_1\) is
\[
W(C_1)=6\sum_{n(a)=0}N_a+2H+P_0+\sum_{q(\alpha)=0}R_\alpha.
\]
Thus the exact residual cubic replaces the numerical approximations in the published computation without changing its weight distribution \(6+6+6+2+1+1+1+1=24\).

## Assumptions and scope
The ground field for the exact equations is \(\mathbb Q\), with geometric points taken over \(\mathbb C\). The quartic is the \(t=1\) member of the family \(F(X,Y,Z,t)=X^4+tG(X,Y,Z)\) in arXiv:2105.11604, originally derived in arXiv:1601.02783. The claim concerns only this singular fiber and its canonical Weierstrass/flex divisor. It does not assert a corresponding exact formula for the other singular fiber or for smooth members of the family.

## Proof
At \(t=1\), the homogeneous quartic is
\[
\begin{aligned}
F_1={}&2X^4-3X^3Y+6X^3Z-3X^2Y^2-6X^2YZ+6X^2Z^2\\
&+4XY^3-6XY^2Z-6XYZ^2+XZ^3+3Y^4+3Y^3Z.
\end{aligned}
\]
Let \(f(x,y)=F_1(x,y,1)\). Let \(h(x,y)\) be the determinant of the homogeneous Hessian matrix of \(F_1\), dehomogenized at \(Z=1\) and divided by the harmless constant \(162\). Exact elimination gives
\[
\operatorname{Res}_y(f,h)
=729x^3(x^3-3x+1)^6(106x^3+3x^2-6x-2).
\]
There is no common zero of \(F_1\) and its Hessian on \(Z=0\): after setting \(Y=1\), the corresponding resultant in \(X\) equals \(77274\), while \([1:0:0]\notin C_1\). Hence the displayed affine resultant accounts for the full degree \(4\cdot6=24\) Hessian intersection.

The singular ideal \((f,f_x,f_y)\) gives the known three nodes with \(x\)-coordinates satisfying \(n(x)=x^3-3x+1=0\) and with \(y=1-x-x^2\). The factor \(n(x)^6\) therefore matches the three weight-six singular Weierstrass points already identified in the source.

For the residual factor \(q(x)=106x^3+3x^2-6x-2\), a lexicographic Gröbner basis of \((f,h,q)\) is
\[
106x^2+23x+19y+3,\qquad q(x).
\]
Thus every residual Hessian intersection has the claimed coordinate, and conversely every root of \(q\) produces such a point. The polynomial \(q\) is squarefree, is coprime to \(x(x^3-3x+1)\), and therefore these three points are distinct from the nodes and the two \(x=0\) flexes.

The two points over \(x=0\) are exact independently of the resultant. At \(P_0=(0,0)\), the tangent is \(x=0\) and
\[
f(0,y)=3y^3(y+1),
\]
so \(P_0\) has tangent contact order three and hence weight one. At \(H=(0,-1)\), the tangent is \(x+y+1=0\) and
\[
f(u,-1-u)=u^4,
\]
so \(H\) is a hyperflex of weight two.

Finally, reducing \(q\) modulo \(5\) gives a cubic with no root in \(\mathbb F_5\), hence \(q\) is irreducible over \(\mathbb Q\). Direct discriminant calculation gives \(\operatorname{disc}(q)=-1026^2\). An irreducible cubic with nonsquare discriminant has Galois group \(\mathrm S_3\), and the negative discriminant gives one real root and one complex-conjugate pair.

## Verification
The accompanying `verify.py` reconstructs \(F_1\), forms its Hessian symbolically, proves the exact resultant factorization, checks that there is no Hessian intersection at infinity, recomputes the residual Gröbner basis, verifies both tangent-contact calculations, and checks the irreducibility/squarefreeness/discriminant statements. It uses exact rational polynomial arithmetic in SymPy and prints `VERIFY_OK` when all assertions pass.

The numerical values of the three roots reproduce the three approximate smooth weight-one points reported in arXiv:2105.11604v2: one point near \((0.325,-1.140)\) and one complex-conjugate pair near \((-0.177\pm0.164i,0.032\pm0.125i)\).

## Relationship to prior work
Lax, arXiv:2105.11604v2, determines the full weight distribution on \(C_1\), but the final three smooth weight-one points are presented only numerically to three decimal places. The exact cubic equation and the linear coordinate relation above are not stated there. Costantini–Kappes, arXiv:1601.02783, supply the universal family and its special-fiber geometry but do not give this flex divisor. Lax–Widland, DOI:10.4153/CMB-1987-041-7, classify possible Weierstrass-weight patterns on rational nodal genus-three curves; that general result does not determine the coordinates or arithmetic of the residual flexes on this specific Teichmüller cusp fiber.

## Limitations
This is a curve-specific exactification of a canonical divisor, not a new general theorem about rational nodal quartics or Teichmüller curves. The Galois statement concerns the residual cubic factor over \(\mathbb Q\); it does not describe monodromy of the full family. The originality comparison found no indexed exact formula for these three flexes, but an unindexed private computation or unpublished note could in principle contain the same elimination.

## References
1. R. F. Lax, *Limit Weierstrass Points on the Kenyon-Smillie Family of Plane Quartics*, arXiv:2105.11604v2 (first public version 2021-05-25).
2. M. Costantini and A. Kappes, *The equation of the Kenyon-Smillie (2,3,4)-Teichmüller curve*, arXiv:1601.02783v1; Journal of Modern Dynamics 11 (2017), 17–41.
3. R. F. Lax and C. Widland, *Weierstrass Points on Rational Nodal Curves of Genus 3*, Canadian Mathematical Bulletin 30 (1987), 286–294, DOI:10.4153/CMB-1987-041-7.
