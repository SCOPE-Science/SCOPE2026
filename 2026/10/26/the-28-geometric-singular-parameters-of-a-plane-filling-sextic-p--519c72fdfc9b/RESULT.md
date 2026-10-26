# The 28 geometric singular parameters of a plane-filling sextic pencil in characteristic three

## Finding
Let \(k=\mathbb F_3\), let \(\overline k\) be its algebraic closure, and let \(\lambda\in\overline k\) be **finite**. Consider the plane sextic
\[
C_\lambda:\quad X^2(X^3Y-XY^3)+Y^2(Y^3Z-YZ^3)+(Z^2+\lambda X^2)(Z^3X-ZX^3)=0.
\]
This is the \(q=3\) specialization of the Asgarli–Ghioca degree-\(q+3\) pencil. Write
\[
\begin{aligned}
Q_7(T)&=T^7+T^6+T^4-T^3-1,\\
Q_{19}(T)&=T^{19}-T^{18}-T^{16}-T^{15}+T^{14}-T^{11}
+T^9-T^8-T^7-T^5+T^3+T^2+1.
\end{aligned}
\]
Both polynomials are irreducible over \(k\). The precise **reduced geometric singular-parameter locus** of the finite pencil is
\[
\boxed{\{\lambda:C_\lambda\text{ is singular over }\overline k\}
=V\bigl(T(T-1)Q_7(T)Q_{19}(T)\bigr).}
\]
Thus exactly \(28=1+1+7+19\) finite geometric parameters are singular. Every member has at most one geometric singular point. At \(\lambda=0\) this is an ordinary unibranch cusp of \(\delta=1\); at the other \(27\) parameters it is an ordinary node. All finite fibers are geometrically integral. Their normalizations have genus \(9\) at singular parameters and genus \(10\) otherwise. This statement concerns parameters over the entire algebraic closure, not just the three \(k\)-rational parameters.

## Assumptions and scope
The field is exactly \(\mathbb F_3\), the sextic has the displayed fixed coordinates, and \(\lambda\) ranges over all finite elements of \(\overline{\mathbb F}_3\). The member at the parameter \(\lambda=\infty\) of the projective pencil is *excluded*: it is a reducible product, not one of the finite sextics classified here. All singularity assertions are geometric. The roots of \(Q_7\) and \(Q_{19}\) each form one Galois orbit of degrees \(7\) and \(19\), respectively.

## Proof
**1. Exhaustion of the geometric singularities.** Write \(F_\lambda\) for the homogeneous defining polynomial. On \(X=0\), its derivatives in the \(X\)- and \(Z\)-directions include respectively \(Z^5\) and \(Y^5\), so no point there is singular. On the chart \(X=1\), put \(u=Y/X\), \(v=Z/X\). The affine equation becomes
\[
f_\lambda(u,v)=u-\lambda v+u^5v+v^5+\lambda v^3-u^3-u^3v^3-v^3.
\]
In characteristic three its two partial derivatives are
\[
\partial_u f_\lambda=1-u^4v,\qquad
\partial_v f_\lambda=-\lambda+u^5-v^4.
\]
Consequently a singular point has \(u\ne0\) and must satisfy
\[
\boxed{v=u^{-4},\qquad \lambda=u^5-u^{-16}.}
\]
It also has to satisfy the **equation** \(f_\lambda=0\), since the degree six is divisible by the characteristic and vanishing of all derivatives alone is insufficient. Direct substitution gives the exact identity
\[
\begin{aligned}
 u^{28} f_{u^5-u^{-16}}(u,u^{-4})
 &= -u^{31}+u^{29}+u^{21}-u^{19}-u^{16}+2u^8-1\\
 &=-(u-1)^3(u+1)^2 P_7(u)P_{19}(u),
\end{aligned}
\]
where
\[
\begin{aligned}
P_7(U)&=U^7+U^5+U^4-U^3-1,\\
P_{19}(U)&=U^{19}+U^{18}+U^{17}-U^{15}-U^{11}-U^8
 +U^7-U^5-U^3+U+1.
\end{aligned}
\]
All identities here are in \(\mathbb F_3\), so \(2=-1\). Conversely, every nonzero root of the displayed product gives a singular point of the corresponding fiber by the two derivative identities. Neither \(P_7\) nor \(P_{19}\) has zero as a root.

**2. Exactly 28 parameters, not merely 28 points in a parameterization.** Each of \(P_7,P_{19}\) is irreducible in \(\mathbb F_3[U]\). An exact certificate is the pair of Frobenius-congruence tests \(U^{3^n}\equiv U\pmod {P_n}\) and \(\gcd(P_n,U^3-U)=1\) for \(n=7,19\); these are sufficient since both degrees are prime. Define \(\lambda(U)=U^5-U^{-16}\) in each quotient field. Direct quotient-ring arithmetic gives \(Q_n(\lambda(U))\equiv0\pmod{P_n}\), while \(\lambda(U)^3-\lambda(U)\not\equiv0\pmod {P_n}\). As \(n\) is prime, \(\lambda(U)\) has exact degree \(n\) over \(\mathbb F_3\). Thus Frobenius carries the \(n\) roots of \(P_n\) bijectively onto the distinct \(n\) roots of \(Q_n\). The parameter orbits of degrees seven and nineteen cannot overlap with each other or with the rational values. The remaining roots \(u=1,-1\) give \(\lambda=0,1\), respectively. Hence the displayed reduced polynomial has exactly 28 distinct roots and every singular fiber has exactly one singular point.

**3. Local type.** At the singular point with \(u\ne0\), the affine Hessian determinant is
\[
\det\begin{pmatrix}f_{uu}&f_{uv}\\f_{vu}&f_{vv}\end{pmatrix}
=u^3v^4-u^8=-\lambda u^3.
\]
This is nonzero whenever \(\lambda\ne0\), giving an ordinary node because the characteristic is not two. At \(\lambda=0\), the singular point is \((u,v)=(1,1)\). Set \(U=u-1\), \(V=v-1\), \(W=U+V\). The quadratic term is exactly \(W^2\), and on its double tangent the defining function satisfies
\[
 f_0(1-V,1+V)=V^3-V^5.
\]
Since the characteristic is not two, Weierstrass preparation and completing the square preserve the leading \(V^3\) term. This is one unibranch singularity with coprime characteristic exponents \((2,3)\), hence an ordinary cusp of \(\delta=1\).

**4. Irreducibility and genus.** Every fiber has no singularity or just one ordinary node or cusp. A nonreduced component would produce a positive-dimensional singular locus. Two distinct components of a degree-six plane curve have Bézout intersection number at least five, whereas the unique singularity has at most two local branches, with local interbranch intersection number one for a node and no distinct branches for a cusp. Thus no fiber is geometrically reducible. The plane sextic arithmetic genus is \((6-1)(6-2)/2=10\), and the normalization genus decreases by precisely one at any of the 28 singular parameters.

## Verification
Run `python3 verify.py` in the same directory. It uses only the Python standard library and exact polynomials over \(\mathbb F_3\). It checks the elimination polynomial factorization, irreducibility of the degree-seven and degree-nineteen auxiliary and parameter polynomials using finite-field Frobenius tests, the two minimal-polynomial congruences, nonrationality of the corresponding parameter orbits, and a direct check of all thirteen \(\mathbb F_3\)-rational projective points in each of the three rational fibers. Successful output ends with `VERIFY_OK`. For an independently organized computer-algebra recheck of the polynomial identities and local Hessian, run `python3 check_symbolic.py` with SymPy installed; success ends with `SYMBOLIC_VERIFY_OK`.

The symbolic elimination and local-analytic steps of the proof cover all geometric points over the algebraic closure. The finite rational-point loops are independent checks only; they are not substituted for the geometric proof.

## Relationship to prior work
Asgarli and Ghioca introduced this exact \(q+3\) plane-filling pencil and established a rational-point smoothness criterion, and they reported computer verification of their geometric smoothness conjecture for odd prime powers below 200, including \(q=3\). Their paper does **not** claim this complete geometric singular-parameter polynomial, the two nonrational degree-seven and degree-nineteen orbits, or the one-cusp/twenty-seven-node degeneration profile. Rational singularities at \(\lambda=0,1\) are consistent with the established rational criteria and are not themselves claimed as a new result. The new scope is the complete reduced discriminant over an algebraic parameter, including singular fibers not defined over \(\mathbb F_3\).

## Limitations
No assertion is made for \(q\ne3\), for the projective pencil member \(\lambda=\infty\), or about the multiplicity structure of the scheme-theoretic discriminant. The displayed degree-28 polynomial cuts out the **reduced** singular-parameter set. Geometric irreducibility and normalization genera are proved for the finite fibers only. The finding has not undergone independent external audit; literature novelty is subject to possible unindexed results.

## References
1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, first posted 2023-07-06, especially Equation (1), Theorem 1.2, Conjecture 1.5, and Section 3. https://arxiv.org/html/2307.03072v1
2. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, Linear Algebra and its Applications 438 (2013), 969–985 (background cited in reference 1).
