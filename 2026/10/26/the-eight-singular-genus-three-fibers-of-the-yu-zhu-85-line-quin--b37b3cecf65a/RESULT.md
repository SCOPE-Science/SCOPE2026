# The eight singular genus-three fibers of the Yu–Zhu 85-line quintic pencil

## Finding
For every \(t\in\mathbb C\setminus\{0,1\}\), the residual-quartic pencil on the Yu–Zhu quintic \(X_t\) has **exactly eight singular fibers**: five four-line stars and three pairs of smooth conics tangent at two points. The five four-line fibers lie over \(r=0,\infty\) and \(r^3=t\), while the three two-conic fibers lie over \(r^3=1\). Each four-line fiber has one ordinary quadruple point; each conic-pair fiber has two \(A_3\) tacnodes. All other fibers are smooth plane quartics of genus three. Every singular fiber is reduced.

Their topological Euler characteristics are, respectively, \(5\) and \(2\), and the total space has \(e(X_t)=55\). Thus the total singular-fiber defect relative to a smooth genus-three fiber is \(5\cdot9+3\cdot6=63\).

## Assumptions and scope
Work over \(\mathbb C\). Write coordinates on \(\mathbb P^3\) as \([u:v:a:b]\) and fix \(t\ne0,1\). Let
\[
X_t=V\bigl((a-b)(u^4-3v^4)-6(a+b)u^2v^2+ab(b^3-ta^3)\bigr).
\]
The source proves \(X_t\) is smooth for these parameters and has exactly \(85\) lines. Let \(L=V(a,b)\subset X_t\). Planes containing \(L\), parametrized by \([a:b]\in\mathbb P^1\), cut the hyperplane divisor as \(L+Q\), with \(Q\) a residual plane quartic. The family of residual divisors is \(|H-L|\), where \(H\) is the hyperplane class. The claim classifies this specified fibration, **not** all genus-three pencils on \(X_t\).

## Proof
**1. The fibration is defined everywhere.** Off \(L\), the unique plane through \(L\) and a point determines the parameter. On \(L\), the residual quartic in the plane \(a=rb\) restricts to the binary form
\[
f_r(u,v)=(r-1)(u^4-3v^4)-6(r+1)u^2v^2.
\]
If a point of \(L\) belonged to all residual divisors, the coefficients of \(r\) and of the constant term of \(f_r\) would vanish there, forcing simultaneously \(u^2v^2=0\) and \(u^4-3v^4=0\), impossible for \([u:v]\in\mathbb P^1\). Therefore \(|H-L|\) is base-point-free and defines a morphism \(\pi_t:X_t\to\mathbb P^1\). Its generic fiber is a smooth plane quartic, hence has genus \(3\). For completeness, the source's smoothness assertion follows from the partial derivatives: on \(L\) these two coefficients cannot vanish simultaneously; on \(V(u,v)\) the derivatives in \(a,b\) have no common zero for \(t\ne0\); when exactly one of \(u,v\) is zero, a singularity would force \(a=b\) and then \(t=1\); when both are nonzero, the two derivatives in \(u,v\) force \(u^4=-3v^4\) and \(a^2+ab+b^2=0\), where the degree-five equation would again force \(t=1\).

**2. A single explicit quartic controls every fiber.** On the finite base chart \(b\ne0\), write \(a=rb\). After removing the factor \(b\) defining \(L\), the residual fiber in the plane \([u:v:b]\in\mathbb P^2\) has equation
\[
Q_{r,t}=A u^4+B u^2v^2+C v^4+c b^4=0,
\quad A=r-1,\ B=-6(r+1),\ C=-3(r-1),\ c=r(1-tr^3).
\]
The fiber over \(r=\infty\) is \(u^4-6u^2v^2-3v^4=0\). This is the four-line case described below.

**3. Exhaustive singular-fiber criterion.** If \(c\ne0\), the derivative \(\partial Q/\partial b=4cb^3\) forces every singular point to have \(b=0\). Such a singular point is exactly a repeated root of the homogeneous binary quartic \(f_r\). Its discriminant on the affine chart \(v=1\) is
\[
\operatorname{Disc}_u(f_r(u,1))=-110592(r-1)^2(r^2+r+1)^2.
\]
The condition therefore is \(r=1\) or \(r^2+r+1=0\), precisely the three roots of \(r^3=1\). Because \(t\ne1\), these parameters do have \(c\ne0\). If \(c=0\), then \(r=0\) or \(r^3=t\). At each of these four values \(f_r\) has four distinct projective roots: its leading and constant coefficients are nonzero and its biquadratic discriminant is \(B^2-4AC=48(r^2+r+1)\ne0\). The fifth value \(r=\infty\) likewise gives a quartic with four distinct roots. No other singular fibers exist. Since \(t\notin\{0,1\}\), the eight base parameters are distinct.

**4. The five line-star fibers.** Whenever \(c=0\), the equation \(Q_{r,t}=f_r(u,v)\) factors into four distinct linear forms over \(\mathbb C\), independent of \(b\). In its plane these are four distinct lines meeting at \([u:v:b]=[0:0:1]\). This point is their unique singular point and is an ordinary quadruple point, with four distinct tangent directions. The same argument applies at \(r=\infty\).

**5. The three conic-pair fibers and their analytic types.** At \(r=1\), one has \(f_1=-12u^2v^2\). Consequently \(Q_{1,t}\) is a difference of two squares after choosing square roots of nonzero constants, and it splits into the two smooth conics \(uv=\pm\gamma b^2\), where \(\gamma\ne0\). They meet exactly at \([1:0:0]\) and \([0:1:0]\), with contact order two at each point.

For a primitive cube root \(r\ne1\), the identity
\[
(r-1)f_r=\bigl((r-1)u^2-3(r+1)v^2\bigr)^2-12(r^2+r+1)v^4
\]
reduces to a square because \(r^2+r+1=0\). Here \(c=r(1-t)\ne0\), so \(Q_{r,t}\) again factors into two conics of the form \(q(u,v)\pm\gamma b^2=0\), with \(q\) a nondegenerate diagonal quadratic form having two distinct zeros on \(\mathbb P^1\). Each conic is smooth and the two intersections lie at those zeros with \(b=0\). Locally \(q\) is a coordinate transverse to the root, and the union has equation \(q^2-\gamma^2 b^4=0\): the \(A_3\) plane-curve tacnode. There are exactly two such points per fiber.

**6. Euler characteristic as a global consistency check.** A smooth genus-three fiber has \(e=-4\). Four rational lines sharing just one point have \(e=4\cdot2-3=5\). Two smooth conics meeting at two distinct points have \(e=2\cdot2-2=2\). Therefore, using additivity of Euler characteristic in a proper fibration with finitely many singular fibers,
\[
e(X_t)=2(-4)+5(5+4)+3(2+4)=55.
\]
Independently, adjunction for a smooth quintic surface gives \(c_2(TX_t)=11H^2\), and since \(H^2=5\), its Euler characteristic is \(55\).

## Verification
The accompanying `verify_genus3_fibers.py` performs exact symbolic checks of the binary-quartic discriminant, square identities, limiting binary quartics and independent Euler-characteristic calculation. Its successful output records the 5+3 classification and \(e(X_t)=55\). These calculations verify polynomial identities; the algebraic argument above supplies the exhaustive all-parameter classification, smoothness reasoning and local analytic interpretation.

## Relationship to prior work
Yu and Zhu [1] construct the pencil of quintic surfaces with 85 lines, give its equation (3.1), prove smoothness, and count the 20 lines meeting \(L\) by identifying five completely split residual quartic planes. They also compute the singular fibers of a **different elliptic fibration**, obtained from the quotient \(X_{-1/8}/C_4\), as \(5I_0^*+I_4+2I_1\). The present claim instead gives a complete classification of the **unquotiented genus-three residual-quartic fibration for every smooth parameter**, including three conic-pair fibers and all its local plane-curve singularities. The source's elliptic quotient fiber labels do not identify the components or tacnodal singularities of the original plane-quartic fibers. An independently published published-finding corpus computation of the 85-line incidence graph concerns the line-incidence spectrum, not singular plane-quartic fibers. Standard plane-curve discriminant methods and Euler-characteristic formulas are background tools, not claimed as new.

## Limitations
The conclusion is over \(\mathbb C\) for \(t\ne0,1\). It does not classify stable reductions, monodromy representations, all other fibrations on the surface, or the induced elliptic quotient's singular fibers beyond the cited source. Direct consequences of the explicit source equation may have been independently observed but not found in the searched records; publication priority requires external verification. No independent scientific audit has been performed.

## References
[1] X. Yu and Z. Zhu, *A smooth quintic surface with 85 lines and Picard number 43*, arXiv:2609.26862v1, submitted 2026-09-22, https://arxiv.org/abs/2609.26862 (Theorem 1.1, §3.1, §3.2, §4).

[2] C. Hilario and K.-O. Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity*, arXiv:2306.08579 (characteristic-two rational quartic fibrations, a different setting).
