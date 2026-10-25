# Wild cusps and normalization genera of Klein plane curves

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic, let \(m\ge 2\), and put
\[
C_m=V(x^m y+y^m z+z^m x)\subset\mathbb P^2_k,
\qquad N=m^2-m+1.
\]
The curve is geometrically integral in every characteristic. In characteristic zero, or characteristic \(p>0\) with \(p\nmid N\), it is smooth of genus \(m(m-1)/2\). If \(p\mid N\), write \(N=p^a h\) with \(a\ge1\) and \(p\nmid h\). Then the entire singular support consists of exactly \(h\) distinct points, all on the dense torus, and **every completed plane-curve germ** is analytically isomorphic to
\[
k[[X,Y]]/(X^2+Y^{p^a}).
\]
Each point is a unibranch cusp with delta invariant \((p^a-1)/2\), and the intrinsic Tjurina/Jacobian singular algebra has length \(p^a\). Thus the singular scheme has total length \(N\), while the normalization \(\widetilde C_m\) has geometric genus
\[
\boxed{g(\widetilde C_m)=\frac{h-1}{2}=\frac{N/p^a-1}{2}.}
\]
The conclusions include characteristics dividing the projective degree \(m+1\): this happens in the exceptional case \(p=3\) with \(m\equiv2\pmod3\).

For the classical quartic \(m=3\), reduction in characteristic seven produces a single \((2,7)\) cusp and rational normalization. For \(m=8\), characteristic three yields nineteen \((2,3)\) cusps and genus nine, whereas characteristic nineteen yields three \((2,19)\) cusps and genus one. The higher wild exponent \(m=31\), \(p=7\) has \(N=931=49\cdot19\), so there are nineteen \((2,49)\) cusps and the normalization has genus nine.

## Assumptions and scope
An integral plane curve is a reduced, irreducible closed subscheme of \(\mathbb P^2_k\). The singular scheme here is the subscheme locally defined by the plane equation and its first partial derivatives; the completed local algebra of its structure sheaf is the Tjurina algebra. The asserted isomorphism of completed curve germs is noncanonical and takes place over \(k\). In characteristic \(p>0\), \(p^a\) denotes the exact highest power of \(p\) dividing \(N\). No separability hypothesis on the projection to the chosen torus coordinate is assumed.

## Proof
**1. Torus chart and boundary.** The curve meets a coordinate line only at two coordinate vertices; for example, on \(x=0\) its equation is \(y^m z=0\). All three vertices are smooth, because a cyclically chosen partial derivative equals one on the corresponding unit-coordinate chart. On the torus \(xyz\ne0\), set \(x=1\), \(y=u\), \(z=v\), and introduce the invertible Laurent coordinate \(s=u^{m-1}v\). Direct substitution gives
\[
F(1,u,v)=u\left(1+s+s^m u^{-N}\right),
\qquad N=m^2-m+1.
\]
Thus the torus portion of the plane curve is given, in coordinates \((s,u)\in(k^*)^2\), by
\[
f(s,u)=1+s+s^m u^{-N}=0.
\]
The coordinate change is an isomorphism of algebraic tori: its inverse is \(v=s u^{-(m-1)}\).

**2. Geometric integrality.** The same torus curve has function-field equation
\[
u^N=-\frac{s^m}{1+s}.
\]
The right-hand rational function has valuation exactly \(m\) at \(s=0\), and \(\gcd(m,N)=1\). Any root in an algebraic extension of the complete discrete valuation field \(k((s))\) has valuation \(m/N\), whose reduced denominator is \(N\). The ramification index, hence the extension degree, is therefore divisible by \(N\); as the defining polynomial has degree \(N\), it is irreducible over \(k((s))\), including in inseparable characteristic. Consequently it is irreducible over \(k(s)\). Since the homogeneous equation is divisible by none of \(x,y,z\), its projective closure is geometrically integral.

**3. Entire singular support.** Differentiating the Laurent equation yields
\[
f_s=1+m s^{m-1}u^{-N},\qquad
f_u=-N s^m u^{-N-1}.
\]
If \(\operatorname{char}k=0\), or \(p\nmid N\), the second derivative is invertible on the torus, so the entire curve is smooth. Suppose \(p\mid N\). Because \(N\equiv1\) for \(m\equiv0,1\pmod p\), both \(m\) and \(m-1\) are units; because \(N\) is odd, \(p\) is odd. The second derivative now vanishes identically. Simultaneously solving \(f=0=f_s\) gives precisely
\[
s=s_0:=-\frac{m}{m-1},
\qquad u^N=-m s_0^{m-1}.
\]
The constant on the right is nonzero. Write \(N=p^a h\) with \(p\nmid h\); over an algebraically closed field the equation for \(u\) has exactly \(h\) distinct roots. No coordinate-boundary singularities exist by step 1.

**4. Exact completed germ.** At any of these points set \(q=p^a\) and introduce \(w=u^{-h}\). Since \(p\nmid h\), the derivative of \(w\) with respect to \(u\) is a unit; hence \((s,w)\) are formal local coordinates. With \(w_0\) the value at the point and \(Y=w-w_0\), Frobenius gives \(w^q=w_0^q+Y^q\), and therefore the local equation, multiplied by the unit \(s^{-m}\), becomes
\[
Y^q+s^{-m}\phi(s)=0,
\qquad\phi(s)=1+s+w_0^q s^m.
\]
The singularity equations say \(\phi(s_0)=\phi'(s_0)=0\), while
\[
\phi''(s_0)=m(m-1)w_0^q s_0^{m-2}\ne0.
\]
Because \(p\ne2\), the zero of \(\phi\) at \(s_0\) has exact order two. Hence \(s^{-m}\phi(s)=(s-s_0)^2 H(s)\) for a formal unit \(H\). Over algebraically closed \(k\) of odd characteristic, the unit has a formal square root. Setting \(X=(s-s_0)\sqrt{H(s)}\) gives exactly the completed equation \(X^2+Y^q=0\), without terms of higher order.

**5. Singular-scheme length and genus.** Since \(q=p^a\) is odd, \(X^2+Y^q\) is analytically unibranch, with normalization parameter \(X=t^q\), \(Y=-t^2\) after a harmless constant scaling. Its semigroup \(\langle2,q\rangle\) has \((q-1)/2\) gaps, proving that the local delta invariant is \((q-1)/2\). Its two partial derivatives are \(2X\) and zero, so the completed Tjurina algebra is
\[
k[[X,Y]]/(X^2+Y^q,2X,0)\cong k[[Y]]/(Y^q),
\]
of length \(q\). Summing over \(h\) points gives total Jacobian singular-scheme length \(hq=N\). The plane arithmetic genus is \(m(m-1)/2\); the normalization genus therefore is
\[
\frac{m(m-1)}2-h\frac{q-1}2
=\frac{m(m-1)-N+h}{2}
=\frac{h-1}{2},
\]
as asserted.

## Verification
The standalone file `verify_klein_reduction.py` uses integer arithmetic and finite-field computations. Executing `python verify_klein_reduction.py` gives the marker `VERIFY_OK`. It checks all prime divisors of \(N\) for \(2\le m\le45\), including the higher-exponent case \((m,p,q)=(31,7,49)\). For small fields it directly enumerates torus points and checks the full homogeneous Jacobian equations. It also verifies the exact local double-root coefficient and the arithmetic genus identity. The checker does not prove the infinite family; steps 1–5 above do.

## Relationship to prior work
González-Aguilera and Liendo introduced the cyclic Klein hypersurface in arbitrary dimension (2011 preprint, Example 3.5), proving smoothness over the complex numbers and using a recurrence involving the geometric-series factor. Harui (2013) studied the automorphism group of smooth complex Klein plane curves and records the integer \(m^2-m+1\) in their cyclic symmetry. Those results do not provide modular singular completed local rings or the normalization-genus law.

The previously obtained higher-dimensional cyclic-hypersurface isogeny calculation treats at least four variables and gives finite singular schemes and Tjurina lengths. Its hypotheses exclude dimension-one hypersurfaces, and its normality and Hessian conclusions do not imply a genus calculation or identify the wild plane-cusp analytic type. Dolgachev (2024, Section 4.2) explicitly notes that the classical Klein quartic is not smooth in characteristic seven. That instance of bad reduction is **known**, not claimed as a new discovery; the contribution here is the uniform singularity-type, length, and normalization-genus classification for all degrees and exceptional characteristics.

## Limitations
The result concerns the named plane model and its normalization, not a regular or stable model over a mixed-characteristic discrete valuation ring. It does not calculate the automorphism group after reduction or all ramification filtrations. The formal analytic equation is established over an algebraically closed base field; no descent to the prime field is claimed. Equivalent formulas could exist in unidentified literature on Delsarte curves, inseparable Kummer covers or loop-type invertible polynomials. The finite checks are corroboration, not a substitute for the proof.

## References
1. V. González-Aguilera and A. Liendo, *On the order of an automorphism of a smooth hypersurface*, arXiv:1102.3443, first public version 16 February 2011, especially Example 3.5. https://arxiv.org/abs/1102.3443
2. T. Harui, *Automorphism groups of smooth plane curves*, arXiv:1306.5842, first public version 25 June 2013, Sections 2–3. https://arxiv.org/abs/1306.5842
3. I. Dolgachev, *Automorphisms of del Pezzo surfaces in odd characteristic*, J. Lond. Math. Soc. (2024), DOI:10.1112/jlms.12905, Section 4.2. https://doi.org/10.1112/jlms.12905
