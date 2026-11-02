# The characteristic-two residual of the Asgarli–Ghioca tangent-filling equation

## Finding

For an integer \(r\geq3\), set \(q=2^r\), \(t=q/2=2^{r-1}\), and work over \(k=\overline{\mathbb F}_2\). In the homogeneous coordinate ring \(\mathbb F_2[X,Y,Z]\) put
\[
F_q=X^{q-1}+Y^{q-1}+Z^{q-1}+(X+Y+Z)^{q-1},\qquad
B=(X+Y)(Y+Z)(Z+X).
\]
The polynomial \(B\) divides \(F_q\); write \(H_q=F_q/B\), a homogeneous form of degree \(d=q-4\), and \(C_q=V(H_q)\subset\mathbb P^2_{\mathbb F_q}\).

**Theorem.** The curve \(C_q\) is geometrically integral. Its geometric singular locus consists of exactly
\[
(t-2)(t-4)
\]
ordinary unibranch cusps (each of multiplicity two and \(\delta=1\)), and no other singularities. These cusps are exactly the points \([X:Y:Z]\in\mathbb P^2(\mathbb F_t)\) for which \(X,Y,Z,X+Y+Z\) are nonzero and \(X,Y,Z\) are pairwise distinct. In particular there are none at \(q=8\), \(24\) at \(q=16\), and \(168\) at \(q=32\).

Each of the three lines in \(B\) is tangent to \(C_q\) at exactly \(t-2\) distinct smooth \(\mathbb F_t\)-points, each with intersection multiplicity precisely two; those lines have no other intersections with \(C_q\). The normalization has genus
\[
g(\widetilde C_q)=t^2-5t+7.
\]
The complete rational point count is
\[
\#C_q(\mathbb F_q)=(q-2)(q-4),
\]
and every \(\mathbb F_q\)-point of \(C_q\) is smooth. Its shortfall from the usual plane-curve point bound \(q(d-1)+1\) is exactly \(q-7\).

## Assumptions and scope

Every geometric statement is over the algebraic closure \(k\), except that the cusp coordinates and line contacts are over \(\mathbb F_t\), a subfield of \(k\) **not** generally contained in \(\mathbb F_q\). In fact \(\gcd(r,r-1)=1\), so \(\mathbb F_q\cap\mathbb F_t=\mathbb F_2\). The \(\mathbb F_q\)-point formula refers to the original defining field \(\mathbb F_q\). An ordinary unibranch cusp means a plane branch whose strict transform becomes smooth after a single blow-up and has intersection multiplicity two with its exceptional divisor; equivalently, its initial tangent term is a square of a line and its degree-three term does not vanish identically in that tangent direction.

## Proof

### Divisibility and intersections with the three lines

On \(X=Y\), the four terms of \(F_q\) cancel pairwise in characteristic two; the same holds on \(Y=Z\) and \(Z=X\). Since the three linear factors are distinct, their product \(B\) divides \(F_q\).

Put \(m=q-1=2t-1\). At a point \([a:a:b]\), with \(a+b\ne0\), differentiation transverse to \(X=Y\) gives
\[
H_q(a,a,b)=\frac{F_{q,X}(a,a,b)}{B_X(a,a,b)}
=\left(\frac{a^{t-1}+b^{t-1}}{a+b}\right)^2.
\]
Thus, on \(X=Y\), the roots away from \([1:1:1]\) are exactly \([a:a:b]\) with \(a,b\ne0\), \(a/b\in\mathbb F_t^\times\setminus\{1\}\); there are \(t-2\) roots, each of restriction multiplicity two. At the triple intersection, write \(X=1+u,Y=1+v,Z=1\). The initial nonzero homogeneous term of \(F_q\) is \(uv(u+v)=B\), so \(H_q(1,1,1)=1\).

At a root \([a:a:b]\) just found, choose the transverse parameter \(u=X-a\) with \(Y=a,Z=b\). The coefficient of \(u^2\) in \(F_q(a+u,a,b)\) is \(a^{-1}+b^{-1}\ne0\), because \(a,b\in\mathbb F_t^\times\), and its linear coefficient vanishes. Meanwhile \(B(a+u,a,b)=u(a+b)^2+O(u^2)\). Therefore the coefficient of \(u\) in the local equation \(H_q\) is
\[
\frac{a^{-1}+b^{-1}}{(a+b)^2}=\frac1{ab(a+b)}\ne0.
\]
The point is smooth, and the line has exactly second-order contact. Symmetry proves the same statement for all three lines. Bézout is also saturated: \(2(t-2)=d\) on each line. There are no singularities of \(C_q\) on \(B=0\).

### Complete geometric singular support away from \(B\)

Put \(s=X+Y+Z\). In characteristic two, since \(q-2=2(t-1)\),
\[
(F_{q,X},F_{q,Y},F_{q,Z})
=(X^{2(t-1)}+s^{2(t-1)},Y^{2(t-1)}+s^{2(t-1)},Z^{2(t-1)}+s^{2(t-1)}).
\]
On \(B\ne0\), the equations \(H_q=H_{q,X}=H_{q,Y}=H_{q,Z}=0\) are equivalent to the vanishing of all three derivatives of \(F_q\): the identity \(F_q=B H_q\), with \(B\ne0\), gives one direction, and homogeneous Euler gives the other, because \(\deg F_q=q-1\) is odd. Vanishing derivatives forces \(s\ne0\). Scale to \(s=1\). Squaring is injective on \(k\); hence \(X^{t-1}=Y^{t-1}=Z^{t-1}=1\), or \(X,Y,Z\in\mathbb F_t^\times\), together with \(X+Y+Z=1\). Conversely, these equations imply all derivatives vanish and \(F_q=0\). The condition \(B\ne0\) requires the three coordinates to be pairwise distinct.

For a field with \(t\) elements of characteristic two, the number of ordered nonzero triples with sum one is \(t^2-3t+3\). The three pairwise-equality loci have union of size \(3(t-1)-2=3t-5\). Subtraction gives precisely \((t-2)(t-4)\) geometric singular points.

### Local cusp type and geometric integrality

At such a point in the chart \(Z=1\), write it \((a,b)\), set \(s=a+b+1\), and put \(A=a^{-1}\), \(D=b^{-1}\), \(S=s^{-1}\). All \(a,b,1,s\) are nonzero; \(a,b,1\) are pairwise distinct. Since \(B\) is a local unit, the singularity type of \(H_q=0\) is that of \(F_q=0\). With \(u=X-a\), \(v=Y-b\), the quadratic and cubic terms are
\[
F_2=(A+S)u^2+(D+S)v^2,\qquad
F_3=A^2u^3+D^2v^3+S^2(u+v)^3.
\]
Indeed \(m=2^r-1\) has every binary digit equal to one, so its binomial coefficients through degree three are all odd; the displayed inverses follow from \(a,b,s\in\mathbb F_t^\times\).

The unique tangent direction can be represented by \((u,v)=(\sqrt{D+S},\sqrt{A+S})\). A direct characteristic-two polynomial identity yields
\[
F_3(\sqrt{D+S},\sqrt{A+S})^2
=(A+D)(A+S)(D+S)(AD+AS+DS)^2.
\]
The first three factors are nonzero by distinctness, and
\[
AD+AS+DS=\frac{s+a+b}{abs}=\frac1{abs}\ne0.
\]
Thus the cubic term along the doubled tangent is nonzero. After a linear change of coordinates and one blow-up the strict transform is smooth and meets the exceptional line with multiplicity two; it has a single branch with delta invariant one (the ordinary cusp type in characteristic two).

The singular locus is finite, so \(H_q\) is reduced (a repeated geometric component would force a positive-dimensional Jacobian singular locus). If its reduced support had two or more irreducible components, Bézout would force two distinct components to intersect at a multibranch singularity. Every singularity just classified is unibranch, so that is impossible. Hence \(H_q\) is geometrically irreducible and reduced.

The arithmetic genus is \((d-1)(d-2)/2\), and each of the \((t-2)(t-4)\) cusps contributes exactly one to the genus defect. Since \(d=2t-4\),
\[
g=(2t-5)(2t-6)/2-(t-2)(t-4)=t^2-5t+7.
\]

### Rational points over \(\mathbb F_q\)

The line intersections above are \(\mathbb F_t\)-points with a coordinate ratio in \(\mathbb F_t^\times\setminus\{1\}\). As \(\gcd(t-1,q-1)=1\), none is \(\mathbb F_q\)-rational. Thus \(C_q(\mathbb F_q)\cap V(B)=\varnothing\).

For a rational projective point outside \(B\), each nonzero member of \(X,Y,Z,s\) has \((q-1)\)st power equal to one. Hence \(F_q=0\) is equivalent to having an even number of these four entries nonzero. Because \(s=X+Y+Z\) and \(X,Y,Z\) are pairwise distinct, this happens precisely when all four are nonzero. Normalize \(s=1\). Counting ordered nonzero, pairwise distinct \(X,Y,Z\in\mathbb F_q\) with sum one yields \((q-2)(q-4)\), by the same inclusion–exclusion calculation as above. Finally, no such triple lies in \(\mathbb F_t^\times\), since \(\mathbb F_q\cap\mathbb F_t=\mathbb F_2\); thus each rational point is smooth. The bound comparison uses \(d=q-4\):
\[
q(d-1)+1-(q-2)(q-4)=q-7.
\]

## Verification

The accompanying standalone Python verifier constructs \(H_q\) by **exact** division of polynomials over \(\mathbb F_2\), checks \(F_q=B H_q\), and evaluates the partial derivatives on the complete projective point sets over \(\mathbb F_t\), for \(q=8,16,32\). Independently, it enumerates all \(\mathbb F_q\)-rational curve points and all contact points on each of the three lines. It also verifies the universal characteristic-two polynomial identity governing the cusp cubic term. Its exact outputs are \(24,168,840\) rational points; \(0,24,168\) candidate cusp supports; and \(2,6,14\) smooth tangencies per line. This finite arithmetic evidence checks the derivation but is not presented as proof for all \(r\); that proof is above. To replay: run `python verify_residual.py` with Python 3 and no nonstandard packages.

## Relationship to prior work

Asgarli and Ghioca, *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, first public version 2023-02-26), introduce the equation \(F_q=0\) for odd characteristic greater than three. Their Remark 1.4 observes that in characteristic two it contains the three lines \(X=Y\), \(Y=Z\), \(Z=X\); their subsequent irreducibility and tangent-filling analysis assumes the stated odd-characteristic hypothesis. The present theorem instead studies the reduced residual factor after removing those lines and determines its irreducibility, complete geometric cusp basket, genus, and exact original-field point count. The precise residual conclusions are not supplied by that remark. An earlier equivalent treatment outside the inspected literature is possible.

## Limitations

No tangent-filling property is asserted for the residual curve. There is no claim about its zeta function over all extension fields or the conductor of its normalization. The classification is for the specific family \(r\ge3\), in geometric characteristic two, and the exact rational point count is over its defining field \(\mathbb F_q\). The genus and singularity classification have mathematical proofs above, not independent external review. Historical originality is assessed from accessible literature and research records only.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, initial public posting 2023-02-26, Remark 1.4 and Section 3; *Bull. Aust. Math. Soc.* 109 (2024), 301–315, https://doi.org/10.1017/S0004972723000382.
2. Classical plane-curve genus formula, Bézout theorem, and standard point bounds for plane curves over finite fields; these are used in their customary forms.
