# Characteristic-three collapse and exact zeta strata of a genus-four \(C_6\) hyperelliptic pencil

## Finding
Let \(K=\mathbb F_q\), \(q=3^r\), \(r\ge1\), and let \(a,b\in K\). Consider the natural complete even-degree hyperelliptic model
\[
X_{a,b}:\quad Y^2=X^{10}+X^7+aX^4+bX.
\]
Its compactification is taken in the standard degree-ten double cover of \(\mathbf P^1\), with two smooth \(K\)-rational points over infinity. Put \(c^3=a\), \(d^3=b\) (unique elements of \(K\)), and \(h(X)=X^3+X^2+cX+d\). Let \(D=a^2-a^3\). The following classification is exact, including all boundary parameters.

1. If \(b\ne0\) and \(b\ne D\), \(X_{a,b}\) is geometrically integral, has precisely three cusp singularities analytically of the form \(v^2=u^3\), and its smooth normalization is the elliptic curve \(E_{c,d}:V^2=Xh(X)\). The normalization is supersingular if and only if \(a=0\), and ordinary otherwise. For every \(m\ge1\), \(\#X_{a,b}(\mathbb F_{q^m})=\#E_{c,d}(\mathbb F_{q^m})\).
2. If \(a\notin\{0,1\}\) and \(b\in\{0,D\}\), the curve is geometrically integral with rational normalization and exactly one two-branched singularity, of local form \(v^2=u^4\) when \(b=0\), or \(v^2=u^6\) when \(b=D\). In the first case it also has two \(v^2=u^3\) cusps; in the second, one such cusp. Writing \(\chi_q\) for the quadratic character on \(K^\times\), its zeta function is
\[
Z(X_{a,b}/K,T)=\frac{1-\chi_q(a)T}{(1-T)(1-qT)}.
\]
3. If \((a,b)=(0,0)\), the only singularities are \(v^2=u^7\) and \(v^2=u^3\); the normalization is rational and \(Z(X_{0,0}/K,T)=((1-T)(1-qT))^{-1}\).
4. If \((a,b)=(1,0)\), the equation factors into two rational graph components meeting at two \(K\)-rational points (local forms \(v^2=u^4\) and \(v^2=u^6\)); its zeta function is \(Z(X_{1,0}/K,T)=(1-qT)^{-2}\).

For all parameters, the zeta function of \(X_{a,b}\) equals that of the (possibly singular or reducible) quartic double cover \(V^2=Xh(X)\). For the smooth elliptic stratum this is the usual elliptic zeta function with numerator \(1-t_qT+qT^2\), where \(t_q=q+1-\#E_{c,d}(K)\).

In particular, among the \(q^2\) literal pairs \((a,b)\in K^2\), exactly \(q^2-3q+3\) have ordinary elliptic normalization, \(q-1\) have supersingular elliptic normalization, \(2(q-2)\) are integral with rational normalization and a two-branched singularity, one has rational cuspidal normalization, and one is reducible.

## Assumptions and scope
The ground field has characteristic three and is finite; the geometric descriptions hold after base change to any algebraic closure of characteristic three. All enumerations count literal coefficient pairs, not isomorphism classes. A statement about the supersingularity of an elliptic *normalization* is not a statement about a Jacobian of a singular genus-four model. The projective curve is the degree-ten double cover with weighted homogenization \(Y^2=X^{10}+X^7Z^3+aX^4Z^6+bXZ^9\) in weights \((1,5,1)\). In characteristic three the usual two points \([1:\pm1:0]\) are distinct and nonsingular.

## Proof
**Frobenius factor and point-count identity.** Since \(K\) is perfect of characteristic three,
\[
X^{10}+X^7+aX^4+bX=X(X^3+X^2+cX+d)^3=Xh(X)^3.
\]
The finite map from \(V^2=Xh(X)\) to \(Y^2=Xh(X)^3\) is \((X,V)\mapsto(X,h(X)V)\). It is birational on every irreducible component, and induces a bijection on geometric closed points: if \(h(x)\ne0\) its inverse is \(V=Y/h(x)\), whereas at a root of \(h\) both curves have the single point with second coordinate zero. The two points over infinity correspond individually, because \(h\) is monic of degree three. This correspondence is defined over \(K\) and commutes with Frobenius; in particular it gives equal numbers of points over *every* finite extension. Equivalently, for any finite extension \(L/K\), \(\chi_L(Xh^3)=\chi_L(Xh)\) pointwise, including zeros, and both models have two rational points over infinity. Thus their zeta functions coincide, even in reducible cases.

**Discriminant and all singularities.** The derivative of \(h\) is \(h'(X)=c-X\); its only possible repeated root is \(X=c\), and
\[
h(c)=c^3-c^2+d.
\]
Consequently \(h\) is separable if and only if \(d\ne c^2-c^3\), equivalently \(b\ne a^2-a^3\). Also \(h(0)=d\), so the root at zero of \(Xh^3\) merges with a root of \(h\) exactly when \(b=0\). If \(b\ne0,D\), the four roots of \(Xh\) are distinct and the original polynomial has valuations \((1,3,3,3)\). Hence there are exactly three ordinary unibranch cusps with local equations \(v^2=u^3\), each with \(\delta=1\); the normalization has genus \(4-3=1\). If \(a\notin\{0,1\}\) and \(b=D\), then \(h=(X-c)^2(X-c+1)\), \(c\notin\{0,1\}\), and \(Xh^3\) has multiplicities \((1,6,3)\), giving the indicated \(v^2=u^6\) and \(v^2=u^3\) singularities with \(\delta=3+1=4\). If \(b=0\), then \(h=X(X^2+X+c)\). When \(c\notin\{0,1\}\) the quadratic is separable and nonzero at zero, giving multiplicities \((4,3,3)\) and \(\delta=2+1+1=4\). At \(c=0\), \(h=X^2(X+1)\) gives multiplicities \((7,3)\). At \(c=1\), \(h=X(X-1)^2\), so \(Xh^3=X^4(X-1)^6\) is a square and the curve splits into two rational components. The unit factors at each singular point admit square roots in the completed local ring over the algebraic closure, proving all displayed local analytic equations. No other finite singularities occur, and the points at infinity are smooth.

**Rational and elliptic zeta strata.** When \(b\ne0,D\), the quartic \(V^2=Xh(X)\) is a smooth genus-one double cover with two rational points at infinity. Replacing \(X\) by \(1/t\) and \(V\) by \(W/t^2\) gives the cubic \(W^2=1+t+ct^2+dt^3\). In characteristic three the Cartier/Hasse invariant of this Weierstrass cubic is proportional to its quadratic coefficient \(c\), so its elliptic normalization is supersingular exactly when \(c=0\), equivalently \(a=0\). This also follows directly from the coefficient-of-\(t^{p-1}\) Cartier formula at \(p=3\).

When \(a\notin\{0,1\},b=0\), the quartic is \(V^2=X^2(X^2+X+c)\); after dividing \(V\) by \(X\), its normalization is the rational conic \(W^2=X^2+X+c\). Its unique node lies over \(X=0\), with normalization preimages satisfying \(W^2=c\). When \(a\notin\{0,1\},b=D\), the quartic is \(V^2=X(X-c)^2(X-c+1)\), and dividing \(V\) by \(X-c\) yields the rational conic \(W^2=X(X-c+1)\). Its unique node lies over \(X=c\), again with normalization preimages satisfying \(W^2=c\). Both conics are split (the first has two rational points at infinity; the second has a rational point at \(X=0\)), hence have \(q^m+1\) points over every \(\mathbb F_{q^m}\). For each extension, the singular node contributes one point in place of \(1+\chi_{q^m}(c)\) normalization preimages, yielding
\[
\#X_{a,b}(\mathbb F_{q^m})=q^m+1-\chi_q(c)^m=q^m+1-\chi_q(a)^m,
\]
since \(a=c^3\). Exponentiating these point counts proves the claimed nodal zeta function. At \((0,0)\) the quartic \(V^2=X^3(X+1)\) is unibranch-cuspidal with split rational normalization, hence has \(q^m+1\) points. At \((1,0)\) it is \(V^2=X^2(X-1)^2\), the union of two copies of \(\mathbf P^1\) meeting at \(X=0,1\), hence has \(2q^m\) points. The formulas for their zeta functions follow.

**Parameter counts.** In the coefficient plane the potentially special locus is the union of the line \(b=0\) and the curve \(b=a^2-a^3\). They intersect in precisely \((0,0),(1,0)\) over every \(\mathbb F_{3^r}\). Thus their union has \(2q-2\) coefficient pairs, of which \(2(q-2)\) are in the nodal (rational-normalization) case, one is cuspidal, and one reducible. The smooth-normalization complement has \(q^2-2q+2\) pairs, of which exactly \(q-1\) satisfy \(a=0,b\ne0\); the remaining \(q^2-3q+3\) have ordinary elliptic normalization. This exhausts all parameters.

## Verification
Run `python3 verify_char3.py` without external dependencies. It constructs polynomial-basis fields of sizes \(3,9,27,81\). It tests the two distinct affine point-count expressions, the closed singular-stratum formulas, and exhaustive parameter frequencies over fields of sizes \(3,9,27\), with \(500\) coefficient pairs additionally checked over the field of size \(81\). The reproduced terminal marker is `CHAR3_C6_FIBER_ZETA_CLASSIFICATION_PASS`. These are finite cross-checks; the proof above handles every extension and every coefficient pair over all characteristic-three finite fields.

## Relationship to prior work
Kudo, Nakagawa, and Takagi introduced the genus-four family \(Y^2=X^{10}+X^7+aX^4+bX\) and analyzed its superspecial smooth members and their automorphisms, using primes at least seven in the automorphism-classification appendix. They do not provide the characteristic-three singular-fiber stratification or its zeta functions. Standard facts about the Cartier operator and the Hasse invariant of elliptic curves are used here as prior tools, not new claims. Results for the same family in other small characteristics do not determine these characteristic-three special fibers.

## Limitations
These models are singular in characteristic three, so their smooth normalizations have genus at most one, rather than genus four; no superspecial genus-four curve or singular-curve Jacobian is asserted. The result counts coefficient pairs, not distinct isomorphism classes. The local equations \(v^2=u^m\) are the precise meanings of the displayed singularity types, avoiding ambiguity of ADE terminology in small characteristic. Equivalent presentations in older literature on characteristic-three degenerations or inseparable reductions are a residual originality risk.

## References
- M. Kudo, T. Nakagawa, T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing* \(\mathbb Z_6\), arXiv:2210.14822 (first public 2022-10-26), https://arxiv.org/html/2210.14822v1, especially Introduction, Sections 2.2 and 3, and Appendix A.
- N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic* \(p>2\), Journal of Algebra 52 (1978), 378–410 (Cartier coefficient formula, as cited in Kudo–Nakagawa–Takagi).
