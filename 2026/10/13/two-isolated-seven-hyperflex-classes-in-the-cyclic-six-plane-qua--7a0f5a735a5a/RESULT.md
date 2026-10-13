# Two isolated seven-hyperflex classes in the cyclic-six plane-quartic family

## Finding
Let \(r\in\mathbb C\setminus\{0,2,-2\}\), and let \(C_r\) be the smooth plane quartic
\[
 C_r:\quad F_r(X,Y,Z)=X^3Z+Y^4+rY^2Z^2+Z^4=0.
\]
This is the canonical cyclic-six genus-three family of Ohashi--Kudo--Harashita [1]. Its complete flex profile has a sharp dichotomy:

* If \(11r^4-1080r^2+3888\ne0\), it has exactly **one hyperflex** (at \([1:0:0]\)) and **22 ordinary flexes**.
* If \(11r^4-1080r^2+3888=0\), it has exactly **seven hyperflexes** and **ten ordinary flexes**. The additional six hyperflexes form a single orbit under \((X:Y:Z)\mapsto(\zeta_3X:-Y:Z)\).

The exceptional values of the complete isomorphism parameter \(u=r^2\) are exactly
\[
 u=\frac{540+288\sqrt3}{11},\qquad u=\frac{540-288\sqrt3}{11}.
\]
Thus exactly **two** complex isomorphism classes in the full-automorphism-\(C_6\) family have seven hyperflexes. The assertion counts distinct geometric flex points, not merely Hessian intersection multiplicity.

## Assumptions and scope
All curves and geometric points are considered over \(\mathbb C\). A flex is a point of contact of order at least three between a smooth quartic and its tangent; a hyperflex has tangent contact order four. An ordinary flex has order three. By the classical Hessian criterion [2, Section 2], for a smooth plane quartic a flex contributes intersection multiplicity one at an ordinary flex and two at a hyperflex to the curve--Hessian intersection cycle. The total intersection degree is \(4\cdot6=24\). The parameters \(r=0\) and \(r=\pm2\) are excluded: the former has a larger automorphism group, while the latter are singular [1, Theorem A]. No statement about positive-characteristic fibers is made.

## Proof
**1. Exact Hessian reduction.** Put \(x=X/Z\), \(y=Y/Z\) in \(Z\ne0\), set \(t=y^2\), and define
\[
 g_r(t)=t^2+rt+1,\qquad P_r(t)=2t^3+5rt^2+(18-r^2)t+3r.
\]
The affine equation of \(C_r\) is \(x^3+g_r(y^2)=0\). Direct differentiation of \(F_r\) gives the homogeneous Hessian determinant
\[
 H_r=-18X\bigl(4r^2Y^2Z^3+rX^3Z^2-8rY^4Z-8rZ^5+6X^3Y^2-48Y^2Z^3\bigr).
\]
On the affine curve, substitution \(x^3=-g_r(y^2)\) yields the exact congruence
\[
 H_r(x,y,1)\equiv54xP_r(y^2)\pmod{x^3+g_r(y^2)}.
\]
In particular, the affine flexes have either \(x=0\) or \(P_r(y^2)=0\).

**2. Four ordinary flexes on \(x=0\).** The equation \(g_r(y^2)=0\) has four distinct nonzero solutions for \(y\), since \(r^2\ne4\) and \(g_r(0)=1\). The partial derivative \(\partial F_r/\partial y=2y(2y^2+r)\) is nonzero there, hence \(x\) is a local uniformizer. The parenthesized Hessian factor above, reduced modulo \(g_r(y^2)\) and evaluated at \(x=0\), equals \(12y^2(r^2-4)\), which is nonzero. Thus \(H_r\) has a simple zero on \(C_r\) at each of these four points, giving four ordinary flexes.

**3. All remaining affine flexes form six-point orbits.** Exact resultant and constant-term calculations give
\[
 \operatorname{Res}_t(P_r,g_r)=16(r^2-4)^2\ne0,\qquad P_r(0)=3r\ne0.
\]
For each root \(t_0\) of \(P_r\), the equations \(y^2=t_0\), \(x^3=-g_r(t_0)\) consequently have precisely six distinct solutions. Since \(\partial F_r/\partial x=3x^2\ne0\), \(y\) is a local uniformizer, and so is \(t=y^2\) since \(y\ne0\). In the local ring the Hessian is a unit times \(P_r(t)\). Its intersection multiplicity therefore equals the multiplicity of \(t_0\) as a root of \(P_r\). These six solutions constitute a full orbit under the indicated order-six automorphism.

**4. Precisely two exceptional isomorphism classes.** Direct discriminant expansion gives
\[
 \operatorname{disc}_t(P_r)=3(r^2-4)(11r^4-1080r^2+3888).
\]
Since \(r^2\ne4\), the cubic has three simple roots unless \(Q(r)=11r^4-1080r^2+3888=0\). On this exceptional locus it has exactly one double root and one simple root: a triple root would require \(P_r(t)=2(t+5r/6)^3\), forcing simultaneously \(r^2=108/31\) and \(r^2=324/125\), which is impossible. Thus the exceptional root contributes six hyperflexes, and the simple root six ordinary flexes. Otherwise all 18 points coming from three roots are ordinary flexes. The quadratic equation in \(u=r^2\) has two distinct roots displayed in the finding, both nonzero and unequal to four. Theorem A of [1] states that \(r^2\) is a complete isomorphism invariant for these \(C_6\) quartics, so they define two and only two exceptional complex isomorphism classes.

**5. The unique point at infinity.** On \(Z=0\) the quartic equation reduces to \(Y^4=0\), so the only geometric point there is \(O=[1:0:0]\). It is smooth because \(F_Z(O)=1\), its tangent is \(Z=0\), and that line meets the quartic with contact order four. Thus \(O\) is always a hyperflex. There are no other points to examine. The profiles are respectively \(22\) ordinary flexes plus one hyperflex, and \(10\) ordinary flexes plus seven hyperflexes; both give the required weighted total \(24\).

## Verification
The standalone `verify.py` is an exact SymPy checker over the rational polynomial ring in the parameters and coordinates. It computes the full Hessian from the defining quartic, reduces it modulo the affine curve equation, verifies the resultant and discriminant identities, verifies the simple Hessian vanishing at the four points on \(x=0\), rules out triple roots, and checks the distinct exceptional squared parameters. Execute `python verify.py` with Python 3 and SymPy installed. A successful run prints `VERIFY_OK` with the identities checked. No finite sample is used to infer a universal statement.

## Relationship to prior work
Ohashi--Kudo--Harashita [1, Theorem A and Section 2.1] establish the quartic normal form, smoothness conditions, cyclic-six automorphism, and the complete isomorphism invariant \(r^2\); they do not determine the flex strata. Girard--Kohel [2, Sections 2, 4, and 5], building on Vermeulen, describe the Hessian/Weierstrass approach and broader quartic moduli strata with seven or more hyperflexes; their general classification is not a parameter-level computation of this specific cyclic-six locus. Hu [3] gives a modular-form equation for the existence of a hyperflex, whereas every curve in this family already has the permanent hyperflex \(O\). The present contribution is the complete **additional-hyperflex** parameter equation, orbit decomposition, and exact two-point intersection on the cyclic-six moduli line, not the general Hessian criterion or the known normal form.

## Limitations
This is a characteristic-zero theorem for the specified smooth canonical family. It does not classify bitangents away from hyperflex lines, special fibers at excluded parameters, or arbitrary quartics in Vermeulen's larger strata. The connection with broader moduli descriptions may permit an independent derivation of the exceptional values; no claim of independent priority certification is made. Additional unpublished or unindexed literature could contain an equivalent specialization. Independent mathematical audit has not been performed.

## References
[1] R. Ohashi, M. Kudo, S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777 (first public 2021-11-18), https://arxiv.org/html/2111.09777v3, Theorem A and Section 2.1.

[2] M. Girard, D. R. Kohel, *Classification of genus 3 curves in special strata of the moduli space*, arXiv:math/0603555 (2006), https://arxiv.org/html/math/0603555v1, Sections 2, 4, 5.

[3] X. Hu, *The Locus of Plane Quartics with A Hyperflex*, arXiv:1509.07689 (2015), https://arxiv.org/html/1509.07689v3, introduction and Section 2.
