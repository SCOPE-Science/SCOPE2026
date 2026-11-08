# A characteristic-two \((2,3)\) tangential complete intersection for the degree-six del Pezzo surface

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Let \(X\subset\mathbb P^6_k\) be the anticanonical model of the smooth degree-six toric del Pezzo surface, realized as the closure of
\[
(x,y)\longmapsto[Z:A:A':B:B':C:C']=[1:x:x^{-1}:y:y^{-1}:xy:(xy)^{-1}]
\]
for \((x,y)\in(k^\times)^2\). The **reduced tangential variety**, the closure of the union of embedded tangent planes, is the integral projective fourfold
\[
\boxed{\tau(X)=V\bigl(Z^2+AA'+BB'+CC',\;ABC'+A'B'C\bigr)\subset\mathbb P^6_k.}
\]
The displayed ideal is the full prime homogeneous ideal of \(\tau(X)\); it is a complete intersection of degrees \(2\) and \(3\), with projective degree \(6\). The natural tangent-plane incidence map to \(\tau(X)\) is generically finite and **purely inseparable of degree \(2\)**. Thus its geometric generic fiber consists of one point of scheme length \(2\), not two distinct tangent centers.

## Assumptions and scope
The field is algebraically closed of characteristic \(2\), and the surface is the smooth projective toric surface associated with the anticanonical lattice hexagon \(\{(0,0),\pm(1,0),\pm(0,1),\pm(1,1)\}\). This is the blow-up of \(\mathbb P^2\) at its three torus-fixed points. The assertion is about the reduced tangential image and generic incidence extension, not the possibly nonreduced scheme-theoretic image of an arbitrary integral model or every special incidence fiber.

## Proof
**Tangent parametrization.** On the dense torus, differentiate the monomial vector using logarithmic derivatives \(x\partial_x\) and \(y\partial_y\). In characteristic \(2\), the derivatives of inverse monomials have the same sign as those of positive monomials. In the open chart \(Z=1\), an arbitrary point in the tangent plane therefore has the form
\[
\begin{aligned}
 A&=(1+a)x,&A'&=(1+a)/x,\\
 B&=(1+b)y,&B'&=(1+b)/y,\\
 C&=(1+a+b)xy,&C'&=(1+a+b)/(xy),
\end{aligned}
\]
for \(x,y\in k^\times\) and \(a,b\in k\). Setting \(s=1+a\), \(t=1+b\), we have \(1+a+b=1+s+t\), and hence
\[
Z^2+AA'+BB'+CC'=1+s^2+t^2+(1+s+t)^2=0,
\]
\[
ABC'+A'B'C=st(1+s+t)+st(1+s+t)=0.
\]
Thus the tangent image is contained in the displayed complete intersection \(Y\).

**Integrality and degree of the complete intersection.** Work in \(Z=1\) with \(A,A',B,B'\) invertible. The cubic equation uniquely gives \(C'=A'B'C/(AB)\), and the quadric becomes
\[
C^2=\frac{AB}{A'B'}\bigl(1+AA'+BB'\bigr).
\]
The rational function on the right is not a square in \(F=k(A,A',B,B')\): its formal derivative with respect to \(A\) equals \(B/(A'B')+B^2/A'\ne0\). Therefore this open locus is integral of dimension \(4\) (a purely inseparable quadratic extension of \(F\)). No four-dimensional irreducible component of \(Y\) can lie in a coordinate hyperplane: when any of \(A,A',B,B',C,C'\) vanishes, the cubic becomes a nonzero product of three other coordinates, and so another coordinate must vanish; the restricted quadric is still nonzero because it contains \(Z^2\). Such a locus has dimension at most \(3\). When \(Z=0\), the quadric \(AA'+BB'+CC'\) is irreducible of rank \(6\), and the cubic does not vanish identically upon it (for example take \(A=A'=B=C=C'=1,\;B'=0\)); hence this intersection has dimension \(3\). The projective complete intersection \(Y\) is Cohen--Macaulay and unmixed, with one generically reduced irreducible component; it is therefore reduced and integral. Its degree is \(2\cdot3=6\), and its homogeneous ideal is the displayed prime ideal.

**Image equals the complete intersection.** In the parametrization, \(A,A',B,B'\) are algebraically independent: adjoining \(x\) and \(y\), which satisfy \(x^2=A/A'\) and \(y^2=B/B'\), recovers the four independent parameters \(x,y,a,b\). Hence the tangent image has dimension \(4\). Its closure is the whole integral fourfold \(Y\).

**Pure inseparability and exact degree.** Let \(K=k(x,y,a,b)\) be the tangent-incidence function field, and let \(F=k(A,A',B,B')\). Using \(x^2=A/A'\) and \(y^2=B/B'\), the independent square classes of \(A/A'\) and \(B/B'\) give \([K:F]=4\), purely inseparable. Also
\[
C=Ay+Bx+xy,
\qquad C^2=\frac{AB}{A'B'}(1+AA'+BB').
\]
The nonsquare calculation above gives \([F(C):F]=2\). The cubic equation expresses \(C'\) rationally in \(F(C)\), so the image function field is \(L=F(C)\). Consequently \([K:L]=2\). Moreover, \(y=(C+Bx)/(A+x)\) in \(K\), and \(a=A/x+1\), \(b=B/y+1\); hence \(K=L(x)\), with \(x^2=A/A'\in L\). This proves that the degree-two extension is purely inseparable.

**Independent intersection-theoretic check.** Write \(H=-K_X\). Since \(X\) is the blow-up of \(\mathbb P^2\) at three points, \(H^2=6\), \(K_XH=-6\), and \(c_2(X)=6\). From the jet exact sequence \(0\to\Omega_X^1\otimes H\to J_1(H)\to H\to0\), one finds \(c_1(J_1(H))=2H\), \(c_2(J_1(H))=12\), and thus \(\int_X s_2(J_1(H))=24-12=12\). This equals \(\deg(\tau(X))\) times the generic tangent-incidence degree, namely \(6\cdot2=12\), in agreement with the function-field proof.

## Verification
A standalone Python checker using exact polynomial arithmetic and the finite field with four elements verifies both defining identities under the tangent parametrization, verifies that the square root on the dense coordinate chart is nontrivial by a formal derivative, and checks the jet-bundle characteristic numbers. It also enumerates **all 63** points on the dense coordinate torus of the affine \(Z=1\) chart over \(\mathbb F_4\) satisfying the quadric and cubic, and confirms that each is attained by the tangent parametrization. Run `python check_toric_tangent_char2.py`. The expected final output line is `ALL_CHECKS_PASSED`. These exact checks support the proof but do not replace its arbitrary-field arguments.

## Relationship to prior work
Oeding and Raicu (2011 preprint) determine equations for tangential varieties of Segre--Veronese varieties over characteristic zero; their target family and characteristic assumptions differ. Furukawa and Ito (2014 preprint) determine combinatorial Gauss maps of projective toric varieties in arbitrary characteristic; the Gauss map into a Grassmannian is distinct from the tangent-plane incidence map into \(\mathbb P^6\). Neither inspected primary treatment states the above prime \((2,3)\) ideal or its degree-two purely inseparable tangent incidence for the anticanonical degree-six del Pezzo surface. This is a best-knowledge comparison rather than a proof of historical priority.

## Limitations
The description concerns the reduced tangential image over algebraically closed characteristic-two fields. It does not classify singularities of the fourfold, all special tangent-plane incidence fibers, or the scheme-theoretic specializations from other characteristics. Originality remains subject to specialized older literature or tables not located in the checked searches. No independent scientific audit is represented.

## References
- L. Oeding and C. Raicu, *Tangential varieties of Segre--Veronese varieties*, original arXiv posting 2011-11-26, arXiv:1111.6202v1, https://arxiv.org/abs/1111.6202.
- K. Furukawa and A. Ito, *Gauss maps of toric varieties*, original arXiv posting 2014-03-04, arXiv:1403.0793v1, https://arxiv.org/abs/1403.0793.
