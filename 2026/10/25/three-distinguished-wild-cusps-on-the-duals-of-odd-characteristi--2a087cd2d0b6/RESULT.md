# Three distinguished wild cusps on the duals of odd-characteristic Pellikaan curves

## Finding
Let \(q=p^e\), where \(p\) is an odd prime and \(e\ge1\), and let \(k\) be an algebraic closure of \(\mathbb F_q\). Consider the smooth Pellikaan curve
\[
C_q:\quad X^{q+1}Y+Y^{q+1}Z+Z^{q+1}X=0\subset\mathbb P^2_k.
\]
Let \(D_q=C_q^\vee\subset(\mathbb P^2_k)^\vee\) be its reduced projective dual. For the three coordinate vertices \(P_0=[0:0:1]\), \(P_1=[1:0:0]\), and \(P_2=[0:1:0]\), let \(T_i\in D_q\) denote their tangent lines regarded as points of the dual plane. Then the germ of \(D_q\) at each \(T_i\) is unibranch and singular, with multiplicity \(q\) and complete value semigroup
\[
\Gamma(D_q,T_i)=\langle q,(q+1)^2+1\rangle.
\]
Consequently its conductor and delta invariant are, respectively,
\[
c_i=(q-1)(q+1)^2,\qquad
\delta(D_q,T_i)=\frac{(q-1)(q+1)^2}{2}.
\]
In the usual smooth plane-filling Tallini model defined over \(\mathbb F_q\), the corresponding three singular dual points form one Frobenius orbit of length three. In contrast, in the displayed Pellikaan coordinates, the three are individually \(\mathbb F_q\)-rational.

## Assumptions and scope
The theorem holds for every odd prime power \(q\), over the algebraic closure, without a genericity assumption. A value semigroup is the set of valuations of nonzero elements of the completed local coordinate ring of a plane branch, calculated with the normalization's uniformizer. The delta invariant is the length of the normalization quotient. The word *unibranch* concerns the entire reduced dual germ at each displayed tangent, not merely a chosen formal parametrization. Nothing here classifies all singularities of the full dual curve.

## Proof
1. **Smoothness and the special tangents.** Write \(F=X^{q+1}Y+Y^{q+1}Z+Z^{q+1}X\). Since \(q=0\) in \(k\), its three partial derivatives are
\[
F_X=X^qY+Z^{q+1},\quad F_Y=Y^qZ+X^{q+1},\quad F_Z=Z^qX+Y^{q+1}.
\]
At any point where one coordinate vanishes, the equation and these partials show smoothness directly. If all coordinates are nonzero, multiplying the three hypothetical equations \(F_X=F_Y=F_Z=0\) gives \(A=-A\) for \(A=(XYZ)^{q+1}\ne0\), impossible because the characteristic is odd. The three coordinate vertices are smooth. The tangent at \(P_0=[0:0:1]\) is \(X=0\); its intersection divisor with \(C_q\) is \((q+1)P_0+P_2\), and \(P_2\) has tangent \(Z=0\), not \(X=0\). Thus this tangent line is tangent only at \(P_0\), and its image in the reduced dual has exactly one branch. The same argument works cyclically.

2. **Local parametrization and dual coordinates.** On \(Z=1\), let \(x=X/Z\), \(t=Y/Z\). The equation becomes
\[
x+t^{q+1}+x^{q+1}t=0.
\]
The partial derivative with respect to \(x\) is \(1+x^qt\), a unit at the origin, so the smooth local curve has a unique series \(x=x(t)\in k[[t]]\) with
\[
x(t)=-t^{q+1}+O(t^{(q+1)^2+1}).
\]
The Gauss map of \(C_q\) is \([F_X:F_Y:F_Z]\). In the affine dual chart \(F_X\ne0\) around the tangent \(X=0\), write \(u=F_Y/F_X\), \(v=F_Z/F_X\). On the curve, the original equation gives \(x+t^{q+1}=-x^{q+1}t\), whence
\[
u(t)=\frac{t^q+x(t)^{q+1}}{1+x(t)^qt},\qquad
v(t)=-\frac{x(t)^{q+1}t}{1+x(t)^qt}.
\]
Therefore
\[
\operatorname{ord}_t u=q,\qquad
\operatorname{ord}_t v=(q+1)^2+1=:M.
\]
The leading coefficients are nonzero; no characteristic-dependent cancellation is involved.

3. **The complete semigroup.** Since \(q\) is odd, \(\gcd(q,M)=\gcd(q,2)=1\). The parametrization \(k[[u(t),v(t)]]\hookrightarrow k[[t]]\) is primitive: the generated valuation group is \(\mathbb Z\), so its normalization has uniformizer \(t\). Every element of the numerical semigroup \(\langle q,M\rangle\) is realized as the initial value of a monomial in \(u,v\). Conversely, two distinct monomials \(u^av^b\) and \(u^{a'}v^{b'}\) cannot have equal valuation below \(qM\): the least positive relation is \(M q=q M\). Hence cancellations in a polynomial expression cannot introduce a new valuation below \(qM\). The conductor of the two-generator semigroup is \((q-1)(M-1)<qM\), and all integers at least this conductor already belong to \(\langle q,M\rangle\). Approximation by polynomials proves the same for arbitrary completed power series. Thus the value semigroup is exactly \(\langle q,M\rangle\). Its multiplicity is \(q\), conductor \((q-1)(M-1)\), and number of gaps \((q-1)(M-1)/2\), giving the claimed delta invariant. Cyclic coordinate symmetry handles the other two dual points.

4. **Frobenius for plane-filling models.** The canonical three special points of a Tallini curve over \(\mathbb F_q\) are the eigen/base points \(A_i=(\alpha_i:1:\alpha_i^2)\) associated with the three roots of an irreducible cubic over \(\mathbb F_q\) (Duran Cunha, Section 2). Frobenius permutes them transitively. Their tangents are distinct because they correspond under geometric projective equivalence to the distinct coordinate tangents above. The tangent construction is defined over \(\mathbb F_q\), so the corresponding three points of the dual form one Frobenius orbit of length three.

## Verification
The accompanying `verify_dual_cusps.py` uses exact truncated formal-series arithmetic in characteristics three, five, and seven, including the non-prime odd prime power nine. It checks the local curve equation, the Gauss coordinates' orders \(q\) and \(M\), and the numerical-semigroup gap formula for \(q\in\{3,5,7,9\}\). With SymPy installed it independently checks \(\det(\operatorname{Hess}F)=2(XYZ)^q\) in these characteristics. The script was executed on the packaged source and returned `VERIFY_OK`; these finite specializations corroborate but do not replace the uniform argument in the proof.

## Relationship to prior work
Tallini and Homma–Kim constructed and classified the smooth minimum-degree plane-filling curves. Duran Cunha proved geometric projective equivalence to the Pellikaan model, computed Weierstrass semigroups on the *original smooth curve*, and determined the special tangent-contact orders. None of these cited conclusions, as stated, determines the value semigroup of a singular **branch of the projective dual**, whose second generator is \((q+1)^2+1\), or its delta invariant. Komeda studies dual singularities for a different family of curves of degree \(q^2+q+1\) with inseparable Gauss map, rather than this degree-\(q+2\) Pellikaan curve with separable Gauss map. The present claim does not reassert known tangent orders or original-curve Weierstrass semigroups as new.

## Limitations
This computes three specified germs, not the full singular locus, bitangent incidence, or global singularity basket of \(D_q\). A previously unlocated account of these particular three dual germs could subsume the result. The characteristic-two case is excluded because the coprimality step fails. The Frobenius orbit assertion concerns the plane-filling Tallini equation over \(\mathbb F_q\), not the displayed Pellikaan equation over that field.

## References
1. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: Supplements to a work of Tallini*, arXiv:0903.1918, first posted 11 March 2009. https://arxiv.org/abs/0903.1918
2. G. Duran Cunha, *Curves containing all points of a finite projective Galois plane*, arXiv:1805.07345, Sections 2–4. https://arxiv.org/abs/1805.07345
3. K. Komeda, *Singularities of the dual curve of a certain plane curve in positive characteristic*, arXiv:2002.10691, especially the introduction and Section 5 (a different family). https://arxiv.org/abs/2002.10691
