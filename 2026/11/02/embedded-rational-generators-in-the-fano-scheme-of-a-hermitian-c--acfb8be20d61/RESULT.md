# Embedded rational generators in the Fano scheme of a Hermitian cone

## Finding

Let \(p\) be any prime, \(e\ge1\), \(q=p^e\), and \(k\) an algebraically closed field of characteristic \(p\). Let
\[
X_q=V(X_0^{q+1}+X_1^{q+1}+X_2^{q+1})\subset\mathbf P^3_k
\]
be the projective cone with vertex \(v=[0:0:0:1]\) over the smooth Hermitian plane curve
\[
H_q=V(X_0^{q+1}+X_1^{q+1}+X_2^{q+1})\subset\mathbf P^2_k.
\]
Let \(F_q=F_1(X_q)\subset\operatorname{Gr}(2,4)\) be the **full scheme-theoretic Fano scheme** of projective lines, rather than its reduction. For \(P\in H_q(k)\), denote the cone generator joining \(v\) to \(P\) by \(L_P\).

The reduced Fano scheme is canonically \((F_q)_{\mathrm{red}}\cong H_q\). In the Grassmannian chart associated with \(P=[1:x:y]\), the complete defining equations are
\[
\mathcal O(F_q)|_{X_0\ne0}\cong
k[x,y,w]/\bigl(1+x^{q+1}+y^{q+1},\, (xy^{q^2}-yx^{q^2})w^q,\,w^{q+1}\bigr).
\]
Consequently, at every geometric closed point of \(F_q\) the completed local rings are precisely
\[
\widehat{\mathcal O}_{F_q,L_P}\cong
\begin{cases}
k[[t,w]]/(w^q),&P\notin H_q(\mathbf F_{q^2}),\\
k[[t,w]]/(tw^q,w^{q+1}),&P\in H_q(\mathbf F_{q^2}).
\end{cases}
\]
Here the standard subfield \(\mathbf F_{q^2}\subset k\) is fixed by the equation's coefficients. Thus the irreducible one-dimensional Fano scheme has generic multiplicity \(q\), and its **entire embedded associated-point locus** consists of exactly \(q^3+1\) points, namely the \(\mathbf F_{q^2}\)-rational generators. At each exceptional point the embedded finite-length submodule has length exactly \(1\), and its transverse zero-dimensional slice has length \(q+1\), rather than the generic length \(q\).

## Assumptions and scope

All schemes, completions, multiplicities and associated points are taken over the algebraically closed characteristic-\(p\) field \(k\). The rank-one cone has dimension \(2\) and its base has genus \(q(q-1)/2\). The theorem concerns the entire closed subscheme of \(\operatorname{Gr}(2,4)\) representing lines on this **singular** projective cone, not the Fano scheme of a smooth degree-\(q+1\) hypersurface or only the set of its generators. The parameter \(q\) is any prime power \(q\ge2\). The distinguished \(\mathbf F_{q^2}\)-points are geometric points fixed by \(q^2\)-Frobenius, not merely a field-of-definition convention.

## Proof

**1. Support and the Grassmannian neighborhood.** The plane curve \(H_q\) is smooth: its three partial derivatives are \(X_0^q,X_1^q,X_2^q\), which never vanish simultaneously on projective space. Hence it is integral and has no line component. If a projective line in \(X_q\) misses the vertex, projection from \(v\) induces an isomorphism of that line onto a projective line contained in \(H_q\), a contradiction. Thus each geometric line is one of the generators \(L_P\); the reduced Fano scheme is set-theoretically \(H_q\), and the maps taking a generator to its base point and vice versa are regular. The local calculation below proves the reduced scheme is actually \(H_q\).

Near \(L_{[1:x:y]}\), use the open Grassmannian chart with a line spanned by the vectors
\[
a=(1,x,y,0),\qquad b=(0,u,v,1).
\]
The restriction of the defining polynomial to \(sa+tb\), using \((r+s)^q=r^q+s^q\), is
\[
s^{q+1}(1+x^{q+1}+y^{q+1})
+s^qt(x^qu+y^qv)+st^q(xu^q+yv^q)
+t^{q+1}(u^{q+1}+v^{q+1}).
\]
These four coefficients generate the Fano ideal: a line is contained in the hypersurface exactly when this binary form vanishes identically, and these coefficient equations define the Hilbert/Fano subscheme on the Grassmannian.

On \(1+x^{q+1}+y^{q+1}=0\) the pair \((x,y)\) cannot be \((0,0)\). Thus, scheme-theoretically on this chart, the relation \(x^qu+y^qv=0\) is a split linear equation in \(u,v\), solved uniquely by
\[
u=y^qw,\qquad v=-x^qw
\]
for a free coordinate \(w\) locally (including the open cover where either \(x\) or \(y\) is invertible). The coefficient of \(st^q\) becomes \(P(x,y)w^q\), where \(P(x,y)=xy^{q^2}-yx^{q^2}\), and the last coefficient becomes
\[
(x^{q(q+1)}+y^{q(q+1)})w^{q+1}=
(x^{q+1}+y^{q+1})^qw^{q+1}=-w^{q+1}.
\]
Therefore the stated three-equation affine presentation is exact, not merely a tangent-space or truncated deformation calculation. Equivalent formulas hold on the other two projective base-coordinate charts. Its nilradical is \((w)\), so its reduction is the smooth plane curve \(H_q\), and there are no other scheme components.

**2. Exceptional zeros and their simplicity.** On \(H_q\), write \(P(x,y)=xy^{q^2}-yx^{q^2}\). Every \(\mathbf F_{q^2}\)-rational point has \(P=0\). Conversely, if \(P=0\), then \([x:y]\in\mathbf P^1(\mathbf F_{q^2})\); if \(y\ne0\), put \(r=x/y\in\mathbf F_{q^2}\). The curve equation becomes \(y^{q+1}=-1/(1+r^{q+1})\in\mathbf F_q^\times\) (the denominator cannot vanish). Hence \(y^{q^2-1}=(y^{q+1})^{q-1}=1\), and \(x,y\in\mathbf F_{q^2}\). If \(y=0\), then \(x^{q+1}=-1\) similarly implies \(x\in\mathbf F_{q^2}\). The symmetric coordinate charts cover points at infinity, proving that zeros of \(P\) are exactly the \(\mathbf F_{q^2}\)-rational points.

At any such point the tangent vector to the affine Hermitian curve can be chosen as \((dx,dy)=(y^q,-x^q)\). Because the derivatives of \(x^{q^2}\) and \(y^{q^2}\) vanish in characteristic \(p\),
\[
dP=y^{q^2}dx-x^{q^2}dy,
\qquad dP(y^q,-x^q)=y^{q+1}+x^{q+1}=-1.
\]
Thus every zero of \(P\) on \(H_q\) is simple. The same argument on each of the three coordinate charts gives a uniform simple zero at every distinguished point.

**3. Completed local rings and associated primes.** At a point where \(P\ne0\), it is a unit in the completed curve local ring \(k[[t]]\), and the Fano equations reduce to \(w^q=0\). At a zero of \(P\), take \(t=P\) as a local parameter (by Step 2), giving the exact local ideal \((tw^q,w^{q+1})\). This proves both displayed completed local-ring presentations, without requiring a finite computation.

The ordinary local ring \(k[[t,w]]/(w^q)\) has sole associated prime \((w)\), and generic length \(q\) over \(k((t))\). At a distinguished point the primary decomposition
\[
(tw^q,w^{q+1})=(w^q)\cap(t,w^{q+1})
\]
shows one minimal associated prime \((w)\) and an additional embedded prime \((t,w)\). The quotient of \((w^q)\) by \((tw^q,w^{q+1})\) is the one-dimensional \(k\)-vector space generated by \(w^q\), proving embedded length one. Modulo \(t\) the special transverse slice is \(k[[w]]/(w^{q+1})\), of length \(q+1\); away from such points it is \(k[[w]]/(w^q)\), of length \(q\).

**4. Count.** In \(\mathbf P^2(\mathbf F_{q^2})\), the Hermitian equation is the vanishing of a sum of three field norms from \(\mathbf F_{q^2}\) to \(\mathbf F_q\). On the affine chart \(X_0=1\), each nonzero norm value has exactly \(q+1\) preimages and zero has one; the number of affine solutions is
\[
2(q+1)+(q-2)(q+1)^2=q^3-q.
\]
There are \(q+1\) solutions on the line at infinity, since \((X_1/X_2)^{q+1}=-1\). In total \(\#H_q(\mathbf F_{q^2})=q^3+1\), and Step 3 gives precisely this many embedded points.

## Verification

The standalone Python 3 program `verify_fano.py` performs arithmetic in explicitly presented finite fields, verifies all projective Hermitian points and the exceptional Frobenius condition, checks the exact four coefficient identities for Grassmannian lines, and tests the nonvanishing differential expression. With \(q=2,3,4,5,7\) it finds respectively \(9,28,65,126,344\) special points over \(\mathbf F_{q^2}\), with no others there. Over the larger fields \(\mathbf F_{64}\) for \(q=2\) and \(\mathbf F_{729}\) for \(q=3\) it finds respectively \(72\) and \(864\) geometric points with \(P\ne0\), alongside \(9\) and \(28\) exceptional points. These exhaust only the specified finite fields. Their role is to check identities and boundary cases, not prove the general theorem, which follows from the four algebraic steps above.

Reproduction: `python3 verify_fano.py`; expected ending line `HERMITIAN_CONE_FANO_FIELDS_AND_COEFFICIENTS_OK`. The local-ring and associated-prime calculations are independently reproducible by substituting \(u=y^qw\), \(v=-x^qw\) in the four displayed coefficients and checking the elementary ideal intersection.

## Relationship to prior work

Raymond Cheng's 2022 dissertation *Geometry of q-bic Hypersurfaces*, Sections 2.7 and 3.8, develops the q-bic Fano-scheme formalism and explicitly considers cones over smooth q-bic plane curves. Cheng's 2023 preprint *q-bic hypersurfaces and their Fano schemes* gives general infinitesimal and smoothness criteria and studies smooth q-bic hypersurfaces and certain singular noncone situations. His 2024 preprint *q-bic threefolds and their surface of lines* gives further Fano geometry for threefolds. Those results motivate and situate the construction; the inspected relevant sections do not provide the two completed local rings, generic multiplicity \(q\), embedded-point classification or exact \(q^3+1\) count for the **singular cone surface** here. The statements are not corollaries of smooth-Fano theorems: every line on the present cone meets its singular vertex.

The elementary fact that a cone's set of lines is its family of generators is not claimed as new. Nor is the classical count of \(\mathbf F_{q^2}\)-points on the Hermitian curve. The contribution being assessed is the entire scheme-theoretic Fano structure, its uniform q-fold nilpotent thickening, and the arithmetic localization and lengths of its embedded associated points. A targeted comparison of related Fano schemes and their nonreduced structures has not identified these conclusions as an existing implication.

## Limitations

The result is for the specified projective cone and its marked embedding, not for every degenerate q-bic form, smooth q-bic hypersurfaces, or higher-dimensional cones. Counts concern geometric points and their embedded scheme structure, not automorphism orbits. They do not describe intersection-theoretic multiplicities under deformations of the ambient cone. The cited source inspections targeted relevant sections rather than claiming exhaustive page-by-page examination of all historical literature; an unindexed earlier local-ring calculation remains a priority risk. No independent external mathematical audit or validation has been performed.

## References

- R. Cheng, *Geometry of q-bic Hypersurfaces*, Columbia University dissertation, first publicly deposited 2022-04-13, DOI: 10.7916/4gba-xx11, https://doi.org/10.7916/4gba-xx11 ; relevant Sections 2.7 and 3.8.
- R. Cheng, *q-bic hypersurfaces and their Fano schemes*, arXiv:2307.06160, first posted 2023-07-12, https://arxiv.org/abs/2307.06160 ; especially the Fano-scheme equations and discussion of singular cases.
- R. Cheng, *q-bic threefolds and their surface of lines*, arXiv:2402.09884, first posted 2024-02-15, https://arxiv.org/abs/2402.09884 ; related Fano geometry and cones in the threefold setting.
