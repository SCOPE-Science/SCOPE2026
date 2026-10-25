# Six four-nodal and thirty-six one-nodal fibers in a degree-one del Pezzo pencil

## Finding
Consider over \(\mathbb C\) the weighted hypersurface
\[
X_0=\{w^2=z^3+(x_2^4+x_0^3x_2+x_0^3x_1)z+(x_1^6+x_0^5x_1+x_0^6)\}\subset\mathbb P(1,1,1,2,3).
\]
It is a smooth degree-one del Pezzo Fano threefold. The rational pencil \([x_0:x_1]\) has base a smooth elliptic curve; after blowing up this base, its degree-one del Pezzo surface fibers have **exactly six singular members with four ordinary double points each and thirty-six other singular members with one ordinary double point each**, with no further singular fibers. All singularities are type \(A_1\). The same singular-fiber passport holds on a nonempty Zariski-open subset of the binary-sextic family of smooth hypersurfaces
\[
w^2=z^3+a_2(x_0,x_1,x_2)z^2+a_4(x_0,x_1,x_2)z+h_6(x_0,x_1),
\]
where \(a_2,a_4\) are ternary forms of degrees two and four, and \(h_6\) is a binary sextic. Massarenti's unirationality theorem applies to the smooth members of the relevant family [1]. In particular, the six four-nodal fibers account for twenty-four of the sixty vanishing cycles counted with local Milnor number.

## Assumptions and scope
The ground field is \(\mathbb C\). Weighted projective coordinates have respective weights \((1,1,1,2,3)\) for \((x_0,x_1,x_2,z,w)\). A fiber means the strict transform of a hyperplane section \(\lambda x_0+\mu x_1=0\) after blowing up the smooth base curve. An ordinary double point is a hypersurface surface singularity with a nondegenerate quadratic term. Fibers are counted over geometric points of \(\mathbb P^1_{\mathbb C}\), not with an arbitrary scheme-theoretic discriminant multiplicity. The generic assertion concerns a nonempty Zariski-open subset, not every degenerate choice of coefficients.

## Proof
**1. Affine pencil and its base.** On \(x_0\ne0\) put \(t=x_1/x_0\) and \(s=x_2/x_0\). The fiber equation becomes
\[
f_t(s,z,w)=w^2-z^3-(s^4+s+t)z-h(t)=0,\qquad h(t)=t^6+t+1.
\]
The base is \(x_0=x_1=0\), a weighted Weierstrass cubic \(w^2=z^3+x_2^4z\), with smooth affine form \(w^2=z^3+z\). It is a smooth elliptic curve. The defining hypersurface meets the smooth locus of the weighted ambient space, and \(dx_0,dx_1\) are independent along the base because its equation has nonzero derivative in one of the transverse \((x_2,z,w)\) directions. Thus every pencil member is smooth along the base, and the blowup introduces no extra fiber singularities.

**2. The six four-node fibers.** Differentiating \(f_t\) gives \(f_w=2w\), \(f_z=-3z^2-(s^4+s+t)\), and \(f_s=-(4s^3+1)z\). On \(z=0\), the singular-point equations are exactly
\[w=0,\qquad h(t)=0,\qquad s^4+s+t=0.\]
The roots of \(h\) are distinct, and for each root \(t\) the quartic has four distinct roots. Indeed, a multiple root of that quartic obeys \(s^3=-1/4\) and \(256t^3=27\); the polynomials \(h(t)\) and \(256t^3-27\) are coprime. In coordinates centered at such a point, the quadratic part is \(w^2-(4s^3+1)(s-s_0)z\), which is nondegenerate. Thus every one of these six fibers has four \(A_1\) points.

**3. The remaining discriminant.** At a singular point with \(z\ne0\), the same derivative equations require \(w=0\), \(s^3=-1/4\), and \(3z^2=-(s^4+s+t)\); substituting into the equation gives \(z^3=h(t)/2\). When \(h(t)\ne0\), eliminating \(z\) is equivalent to
\[4(t+3s/4)^3+27h(t)^2=0,\qquad s^3=-1/4.\]
The converse holds: if these two equations hold and \(h(t)\ne0\), setting \(a=t+3s/4\) and \(z=-3h(t)/(2a)\) gives the unique singular point over this \((t,s)\).

Set \(T=4s\), so \(T^3=-16\), and put \(Q(t)=256t^3+1728h(t)^2-27\). Multiplying the first elimination equation by \(64\) produces
\[Q(t)+144t^2T+27tT^2=0.\]
Its norm in \(\mathbb C(t)[T]/(T^3+16)\) is
\[
F(t)=Q(t)^3+186624Q(t)t^3-47775744t^6+5038848t^3.
\]
To see this without a black-box resultant, multiplication by \(a+bT+cT^2\) on the basis \((1,T,T^2)\) has matrix
\[
\begin{pmatrix}a&-16c&-16b\\b&a&-16c\\c&b&a\end{pmatrix},
\]
whose determinant is \(a^3+48abc-16b^3+256c^3\). Substituting \((a,b,c)=(Q,144t^2,27t)\) yields \(F\). In particular \(\deg F=36\) and its leading coefficient is \(1728^3\).

Exact reductions modulo \(5\) give
\[
\gcd(F,F')=\gcd(F,h)=\gcd(h,h')=\gcd(h,256t^3-27)=1.
\]
These are identities in \(\mathbb F_5[t]\), verified by the included standalone checker. Since \(F\) has the same degree over \(\mathbb F_5\), these certificates prove squarefreeness and coprimality over \(\mathbb Q\) and hence over \(\mathbb C\). Thus the other thirty-six parameters are distinct, avoid the six roots of \(h\), and yield one singular point apiece. At any of these, \(z\ne0\) and \(s\ne0\); the Hessian diagonal entries in the \((s,z,w)\) directions are \(-12s^2z,-6z,2\), hence the point is an \(A_1\) singularity.

**4. Infinity and smooth total space.** The fiber at \([x_0:x_1]=[0:1]\), in the chart \(x_1=1\), is \(w^2=z^3+s^4z+1\). Its affine derivative equations have no solution on the surface: \(s^3z=0\) and \(3z^2+s^4=0\) imply \(s=z=0\), contradicted by the constant term. It is also smooth along the base by step 1. Thus there are no additional singular members. The two isolated singular points of the ambient weighted projective space are not on \(X_0\). Along each four-node member the derivative of the total equation with respect to \(t\) is \(-h'(t)\ne0\). Along each one-node member, the simple root of the discriminant makes the deformation transverse (equivalently, the critical value has a simple zero), so the total hypersurface is smooth there as well. Therefore \(X_0\) is smooth everywhere. Each surface fiber is a degree-one del Pezzo hypersurface in \(\mathbb P(1,2,3)\), possibly with rational double points.

**5. Nonempty open family.** In the displayed binary-sextic family, every simple zero of \(h_6\) forces four nodes at the four distinct zeros of the quartic \(a_4\) along its corresponding line; this persists in the parameter family. The thirty-six additional nodes are simple zeros of the residual discriminant for the witness \(X_0\), so they also persist separately under sufficiently small algebraic deformations. Smoothness of the total space, distinctness of roots and transversality are Zariski-open conditions. Properness rules out additional singular fibers appearing from nowhere in a sufficiently small open neighborhood. The exhibited \(X_0\) proves that neighborhood nonempty.

## Verification
Run `python3 verify.py` without external packages. It checks the displayed norm/determinant identity coefficient by coefficient over the integers, the exact degree and leading coefficient of \(F\), and all four modular coprimality identities. Successful output is `VERIFY_OK: degree 36; exact cubic norm; four coprimality certificates modulo 5`. These finite polynomial certificates suffice here because the discriminant has been derived exactly for the entire complex family of pencil parameters, rather than sampled over finite fields. As an independent consistency check, adjunction gives \(c_3(TX_0)=-38H^3\), and \(\int_{X_0}H^3=1\), hence \(e(X_0)=-38\); blowing up an elliptic curve does not change Euler characteristic. A smooth degree-one del Pezzo surface has Euler characteristic \(11\), and \(2\cdot11-6\cdot4-36=-38\), agreeing with the complete singularity census.

## Relationship to prior work
Massarenti [1], first publicly available on 2026-08-23, constructs a smooth unirational family of degree-one del Pezzo Fano threefolds of the displayed type and studies its birational geometry. The contribution here is the explicit **singular-fiber passport of its natural pencil**, including the six simultaneously four-nodal fibers and the squarefree degree-thirty-six residual discriminant. The general principle that singular fibers contribute Milnor numbers to Euler characteristic is classical; it does not force the partition \(6\times4+36\times1\). Related general studies of del Pezzo varieties [2] do not furnish the specific calculation.

## Limitations
The theorem concerns the stated 28-parameter coefficient presentation (before taking weighted coordinate equivalences), not the full moduli space of degree-one del Pezzo threefolds. It determines singular points and fiber counts, not the full monodromy representation or isomorphism classes of singular fibers. The modular certificates prove the required polynomial facts in characteristic zero; no assertion about reduction of the original geometry to characteristic five is made. Literature priority is subject to the possibility of an equivalent earlier unindexed discriminant computation. Independent review has not been performed.

## References
[1] Alex Massarenti, *Unirational Fano threefolds*, arXiv:2608.22333v1 (public 2026-08-23), https://arxiv.org/abs/2608.22333.

[2] Alexander Kuznetsov and Yuri Prokhorov, *On higher-dimensional del Pezzo varieties* (2023), background on del Pezzo geometry and discriminant loci.
