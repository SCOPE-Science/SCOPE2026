# Complete inflection strata of a cyclic plane-curve pencil

## Finding

For every integer \(n\ge5\), the smooth members of the plane-curve pencil
\[
C_{n,t}:\quad Y^n=X^n+tX^{n-2}Z^2+Z^n\subset\mathbb P^2_{\mathbb C}
\]
have an explicit complete tangent-contact distribution. There is exactly one nonzero smooth parameter invariant at which the residual flex divisor acquires double points. The exceptional locus is determined uniformly for odd and even degrees, while the Fermat fiber has a different, fully concentrated inflection divisor.

Write \(g=\gcd(n,2)\), \(r=n/g\) and \(s=(n-2)/g\). Set
\[
S_n=\frac{(-n/2)^r}{((n-2)/2)^s},\qquad
K_n=\frac{(n(n-1)(n-3)/2)^r}{((n-2)(n-3)^2/2)^s}.
\]
These numbers are distinct and nonzero. The curve is smooth exactly when \(t^r\ne S_n\).

For each smooth \(t\ne0\), there are exactly \(n\) distinct points on \(Y=0\) with tangent contact \(n\), and exactly \(n\) distinct points on \(X=0\) with tangent contact \(n-2\). All remaining flexes have the following precise behavior:

* If \(t^r\ne K_n\), there are exactly \(n^2\) further points, all with tangent contact \(3\).
* If \(t^r=K_n\), there are exactly \(n(n-2g)\) further points of tangent contact \(3\), and exactly \(ng\) further points of tangent contact \(4\).

There are no other inflection points. At \(t=0\), the Fermat curve has precisely \(3n\) inflection points, all with tangent contact \(n\). The total inflection weight in every smooth fiber is \(3n(n-2)\), in agreement with the plane-curve flex formula.

The nonzero jumping parameters form the reduced equation \(t^r=K_n\) on the affine parameter line; in particular, there are exactly \(r\) such parameters. The geometric count of extra four-contact points in each exceptional fiber is \(ng\).

## Assumptions and scope

The ground field is \(\mathbb C\); thus Hessian intersection multiplicities equal tangent-contact excesses without positive-characteristic caveats. Tangent contact means the local intersection multiplicity of the curve with its unique projective tangent line. Its flex weight is contact order minus two. Every statement is about points of the displayed embedded smooth plane curve, not intrinsic Weierstrass points for an arbitrary linear series. The positive integer \(n\) is arbitrary subject to \(n\ge5\), and \(t\) is any complex number satisfying the stated smoothness condition.

For \(t\ne0\), define the binary form
\[
\begin{aligned}
H_{n,t}(X,Z)={}&2ntX^n-2(n-2)t^2X^{n-2}Z^2\\
&+n^2(n-1)X^2Z^{n-2}+n(n-2)(n-3)tZ^n.
\end{aligned}
\]
Its simple and double roots on the affine line \(Z=1\) give exactly the residual contact-three and contact-four points, respectively; each root lifts to exactly \(n\) points of \(C_{n,t}\). On the jumping locus the double roots satisfy
\[
X^n=\frac{(n-2)(n-3)^2}{2},\qquad
 tX^{n-2}=\frac{n(n-1)(n-3)}{2}.
\]
There are precisely \(g\) such roots of \(H_{n,t}(X,1)\).

## Proof

**Smoothness.** In the chart \(Z=1\), set \(f(x)=x^n+tx^{n-2}+1\). A singular point must have \(y=0\) and \(f(x)=f'(x)=0\). As \(f(0)=1\), one has \(x\ne0\). The derivative condition gives \(nx^2+(n-2)t=0\). Put \(u=tx^{n-2}\), \(v=x^n\); the two conditions are equivalent to
\[
u=-\frac n2,\qquad v=\frac{n-2}{2}.
\]
Since \(\gcd(r,s)=1\), the system \(x^n=v\), \(tx^{n-2}=u\) has a solution over \(\mathbb C\) exactly when \(t^r=u^r/v^s\). At \(Z=0\), the equation \(Y^n=X^n\) forces \(X,Y\ne0\), so no points at infinity are singular. This proves smoothness precisely for \(t^r\ne S_n\).

**Hessian factorization.** A direct differentiation of \(F=Y^n-X^n-tX^{n-2}Z^2-Z^n\) gives the exact identity
\[
\det(\partial_i\partial_jF)_{i,j\in\{X,Y,Z\}}
=n(n-1)^2Y^{n-2}X^{n-4}H_{n,t}(X,Z).
\]
For \(t\ne0\), \(H_{n,t}(0,1)=n(n-2)(n-3)t\ne0\) and \(H_{n,t}(1,0)=2nt\ne0\). Thus its \(n\) roots (with multiplicity) are finite and nonzero. Moreover, the exact affine identity \(nff''-(n-1)(f')^2=x^{n-4}H_{n,t}(x,1)\) shows that at a root of \(f\) the residual Hessian is a nonzero multiple of \(-(n-1)(f')^2\); smoothness makes this nonzero. Therefore no root of \(H_{n,t}\) lies over \(Y=0\), and each has precisely \(n\) distinct lifts to the curve.

**All multiple residual roots.** Write \(h(x)=H_{n,t}(x,1)\), and suppose \(t\ne0\), \(x\ne0\), \(h(x)=h'(x)=0\). Multiplying the first identity by \(x^{n-2}\), and the derivative identity by \(x^{n-1}/2\), yields the polynomial system
\[
\begin{aligned}
(2nu+n^2(n-1))v-2(n-2)u^2+n(n-2)(n-3)u&=0,\\
n^2(u+n-1)v-(n-2)^2u^2&=0.
\end{aligned}
\]
Eliminating \(v\) gives exactly
\[
n(n-2)u(n+2u)(-n^3+4n^2-3n+2u)=0.
\]
The factor \(u\) cannot vanish. The solution \(u=-n/2\) forces \(v=(n-2)/2\), i.e. the excluded singular parameter. The only remaining possibility is
\[
u_*=\frac{n(n-1)(n-3)}2,\qquad v_*=\frac{(n-2)(n-3)^2}2.
\]
The same coprimality argument as above shows that such a root exists precisely when \(t^r=K_n\). For a fixed such \(t\), the two power equations have exactly \(g\) solutions \(x\), because their exponent gcd is \(g\). Direct differentiation, evaluated using both power equations, gives
\[
h''(x)=2n^2(n-1)(n-2)^2\ne0.
\]
Hence these roots are exactly double, all other roots are simple, and there are precisely \(n-2g\) simple roots of \(h\). Finally \(|K_n/S_n|=((n-1)^n/(n-3)^{n-4})^{1/g}>1\) for \(n\ge5\), so the exceptional jump parameter is always smooth.

**Tangent-contact orders.** At the \(n\) smooth branch points \(y=0\), local inversion of \(f(x)=y^n\) gives \(x=x_0+c y^n+\cdots\) with \(c\ne0\), so the vertical tangent has contact exactly \(n\). At \(x=0\), one has \(y^n=1+tx^{n-2}+x^n\); since \(t\ne0\), the tangent has contact exactly \(n-2\). For every residual root \(x\ne0\), \(y\ne0\) and the local curve is the graph of an analytic function of \(x\). On a smooth plane curve in characteristic zero, the local Hessian intersection multiplicity is tangent contact minus two. As the other factors of the Hessian do not vanish at these points, simple roots of \(h\) yield contact three, and double roots yield contact four. There are no further Hessian intersections, so the classification is complete.

At \(t=0\), the Hessian is a nonzero constant times \(X^{n-2}Y^{n-2}Z^{n-2}\). Each coordinate line intersects the Fermat curve in \(n\) distinct points, and the tangent there has contact \(n\). Thus there are exactly \(3n\) inflection points, all with weight \(n-2\).

**Weight check.** In a generic nonzero smooth fiber the flex weights add to
\[
n(n-2)+n(n-4)+n^2=3n(n-2).
\]
At a jumping parameter they add to
\[
n(n-2)+n(n-4)+n(n-2g)+2ng=3n(n-2).
\]
The Fermat fiber has \(3n(n-2)\) by its coordinate-axis intersections. These checks agree with the Hessian intersection total but are not used as a substitute for the root-multiplicity argument.

## Verification

Run `python verify_flex.py` with SymPy installed. It checks the exact elimination identity symbolically for arbitrary formal \(n\), checks the full homogeneous Hessian identity for degrees \(5\) through \(10\), checks separation of the two parameter invariants and the nondegeneracy of the double roots in those degrees, verifies generic transversality in each sample, and independently factors the discriminant and resultant of the degree-five residual polynomial. Successful output ends with `VERIFY_OK`. The infinite-degree proof is the algebraic calculation above; the finite checks do not constitute its proof.

For the degree-five member, \(S_5=-3125/108\) and \(K_5=400000/27\). A generic nonzero smooth fiber has \(5\) branch flexes of contact five, \(5\) contact-three points at \(X=0\), and \(25\) further contact-three points. At each of the five nonzero jumping parameters, the last group becomes \(15\) contact-three and \(5\) contact-four points.

## Relationship to prior work

Badr and Harui (arXiv:2603.26180, first public version 2026-03-27) classify automorphism groups of smooth plane cyclic covers with a unique outer Galois point; their objects motivate studying explicit cyclic plane families, but their stated classification is not a flex-contact stratification. The present pencil is not asserted to have a unique outer Galois point in every fiber, especially at Fermat symmetry points.

Cotterill, Darago, Garay López, Han and Shaska (arXiv:2110.04813) develop general arithmetic-inflection methods for superelliptic curves, including ramification and off-ramification phenomena. Their general framework is relevant to deriving Hessian contact formulas, but no statement of the explicit smooth jump invariant \(K_n\) and complete contact counts for this pencil was found in the inspected material. Bertone and Weimann (arXiv:2502.02075) study flex loci of general hypersurfaces by intersection theory; those generic results are distinct from the exact exceptional parameter equation of this special smooth plane-curve family.

Related published classifications may encode the same invariant under changes of coordinates; therefore historical priority is provisional, not a proved absence of antecedents. General Hessian and flex-degree formulas are classical and not presented as novel.

## Limitations

This classifies the embedded plane flex divisor in characteristic zero, not all intrinsic Weierstrass points or higher linear-series ramification. It does not count abstract isomorphism classes of the parameter fibers, nor classify automorphism groups. It excludes the singular locus \(t^r=S_n\). A separate independent mathematical audit has not been performed. Historical-priority assessment remains qualified because alternative coordinate normalizations could disguise overlap.

## References

1. E. Badr and T. Harui, *Smooth plane curves with a unique outer Galois point and their automorphism groups*, arXiv:2603.26180 (first publicly submitted 2026-03-27), https://arxiv.org/abs/2603.26180.
2. E. Cotterill, I. Darago, C. Garay López, C. Han and T. Shaska, *Arithmetic inflection of superelliptic curves*, arXiv:2110.04813 (first publicly submitted 2021-10-10), https://arxiv.org/abs/2110.04813.
3. C. Bertone and M. Weimann, *Hyperflex loci of hypersurfaces*, arXiv:2502.02075 (first publicly submitted 2025-02-04), https://arxiv.org/abs/2502.02075.
