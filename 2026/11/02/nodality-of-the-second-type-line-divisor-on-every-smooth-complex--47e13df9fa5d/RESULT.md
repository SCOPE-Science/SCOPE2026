# Nodality of the second-type line divisor on every smooth complex cubic threefold

## Finding

**Theorem.** Let \(X\subset\mathbf P^4_{\mathbf C}\) be any smooth cubic threefold, let \(F(X)\) be its smooth Fano surface of lines, and let \(M(X)\subset F(X)\) be the determinantal divisor parametrizing lines of the second type. Then every singularity of \(M(X)\) is an ordinary node. More precisely, for every triple line \(\ell\subset X\),
\[
\widehat{\mathcal O}_{M(X),[\ell]}\simeq\mathbf C[[U,V]]/(UV).
\]
There are no other singularities. The scheme of singular points, defined by \(\operatorname{Fitt}_1\Omega^1_{M(X)/\mathbf C}\), is therefore a reduced finite scheme supported exactly on the triple lines; each point has \(\delta=\tau=1\).

The notion of *triple line* means that the unique plane tangent to \(X\) along \(\ell\) cuts out exactly \(3\ell\). In particular, the assertion covers special cubic threefolds with reducible second-type divisors and is not confined to general members of moduli.

## Assumptions and scope

All schemes and formal completions are over \(\mathbf C\). The second-type curve is equipped with its standard determinantal divisor structure, namely the vanishing on the Fano surface of the determinant of the three binary quadratics obtained by restricting the transverse gradient of a cubic defining \(X\) to a moving line. This is the definition used in Bockondas–Boissière, equation (2), and fixes the potentially important scheme-theoretic convention.

A line is of the second type when its normal bundle in \(X\) is \(\mathcal O_{\mathbf P^1}(1)\oplus\mathcal O_{\mathbf P^1}(-1)\); equivalently it has a unique tangent plane along its length. Bockondas–Boissière prove that its determinant divisor is singular set-theoretically exactly at triple lines. The argument below strengthens this support classification to a formal analytic local-ring classification, including multiplicity.

## Proof

**1. Normalizing the pencil of normal quadratics.** Fix a triple line \(\ell\), choose homogeneous coordinates \([s:t:u:v:w]\) with \(\ell=\{u=v=w=0\}\) and its unique tritangent plane \(P=\{u=v=0\}\), and write the defining cubic as \(F\). Since \(P\cap X=3\ell\), its restriction to \(P\) is \(k w^3\) for some \(k\in\mathbf C^\times\). The linear terms transverse to \(\ell\) are \(u q_2(s,t)+v q_3(s,t)\), and the coefficient of \(w\) is zero.

The two quadratics \(q_2,q_3\) have no common zero on \(\mathbf P^1\): otherwise all partial derivatives of \(F\) vanish at the corresponding point of \(\ell\), contradicting smoothness of \(X\). They are linearly independent, because otherwise the transverse gradient would span at most one dimension and \(\ell\) would have at least two independent tangent-plane directions, contrary to uniqueness of \(P\). In fact the uniqueness is automatic from the two-dimensional span. Their projective pencil is thus a line in \(\mathbf P(\operatorname{Sym}^2\mathbf C^2)\) not tangent to the smooth conic of squares: a tangent line at \([h^2]\) is precisely the pencil of quadratics divisible by \(h\), which would have a base point. This line intersects the conic in two distinct squares of linearly independent linear forms. Changes of basis of \([s:t]\) and of the \((u,v)\)-plane therefore normalize the first-order terms to \(s^2u+t^2v\).

By homogeneity and the triple-plane restriction, in these adapted coordinates the cubic has the general form
\[
F=s^2u+t^2v+sQ_0(u,v,w)+tQ_1(u,v,w)+R_3(u,v,w),
\]
where \(Q_0,Q_1\) are arbitrary quadratic forms in the three normal variables **with zero \(w^2\)-coefficient**, and \(R_3(0,0,w)=kw^3\) with \(k\ne0\). These conditions do not restrict any other coefficients.

**2. The Fano-surface coordinates.** A line near \(\ell\) in the Grassmannian has equations
\[
u=a s+b t,\qquad v=c s+d t,\qquad w=e s+f t.
\]
Substitute these three expressions into \(F\). The four coefficients of \(s^3,s^2t,st^2,t^3\) vanish precisely on the Fano surface. Their Jacobian with respect to \((a,b,c,d)\) at the origin is the \(4\times4\) identity. Thus the formal implicit-function theorem identifies \(\widehat{\mathcal O}_{F(X),[\ell]}\) with \(\mathbf C[[e,f]]\), and expresses \(a,b,c,d\) uniquely as formal series in \(e,f\). Setting \(a=b=c=d=0\) in the four defining equations leaves the homogeneous cubic \(k(es+ft)^3\), with no terms of degree at most two in \((e,f)\). Consequently
\[
a,b,c,d\in(e,f)^3.
\]

**3. The universal quadratic jet of the second-type determinant.** For each moving line in the Fano surface, restrict the three transverse derivatives \(\partial_uF,\partial_vF,\partial_wF\) to it, and express the resulting quadratics in the coefficient basis \((s^2,st,t^2)\). The determinant of the resulting \(3\times3\) coefficient matrix is the local equation \(m(e,f)\) of \(M(X)\), by the published determinant construction. The preceding identities and the absence of pure \(w^2\)-terms in \(Q_0,Q_1\) give, in the \((e,f)\)-adic topology,
\[
\partial_uF|_{\ell_{e,f}}=s^2+O(e,f),\qquad
\partial_vF|_{\ell_{e,f}}=t^2+O(e,f),
\]
\[
\partial_wF|_{\ell_{e,f}}=3k(es+ft)^2+O((e,f)^3).
\]
Only the quadratic term of the last column contributes to the quadratic jet of the determinant. With the column order \((u,v,w)\) one obtains the *exact universal identity*
\[
\boxed{m(e,f)=-6kef+O((e,f)^3).}
\]
The Hessian determinant of this quadratic initial form is \(-36k^2\ne0\). Thus the divisor has an ordinary double point with two distinct tangents. Since the base field has characteristic zero, the formal Morse lemma (or explicit Hensel factorization followed by a formal change of parameters) identifies its completed local ring with \(\mathbf C[[U,V]]/(UV)\).

**4. Global completeness and the singular subscheme.** The support theorem of Bockondas–Boissière says that every singular point of \(M(X)\) is a triple line and conversely. The preceding computation applies at every such line, and shows all these points are nodes. At a node, the intrinsic first Fitting ideal of differentials is the Jacobian ideal \((U,V)\) inside \(\mathbf C[[U,V]]/(UV)\); its quotient is \(\mathbf C\). This proves that the singular subscheme is reduced of length equal to the number of triple lines and that each singularity has local \(\delta\)- and Tjurina invariants one.

As a numerical consequence, the known relation \(M(X)\sim2K_{F(X)}\) and \(K_{F(X)}^2=45\) give \(p_a(M(X))=136\). If \(M(X)\) has \(r\) irreducible components and \(N\) triple lines, the sum of the geometric genera of its normalized components is \(135+r-N\). This last formula does not assert irreducibility or the existence of a specified value of \(N\).

## Verification

Run `python3 verify_universal_jet.py` in an environment with SymPy. The verifier constructs the **most general** cubic in the normalized displayed form, with independent symbols for every coefficient of both \(Q_i\) and of \(R_3\). It checks (i) the Fano-equation Jacobian is exactly the identity; (ii) no term of degree below three survives when the four dependent Grassmannian variables are set to zero; (iii) the transverse-gradient determinant has quadratic jet exactly \(-6kef\); and (iv) the corresponding Hessian determinant is \(-36k^2\). It prints `UNIVERSAL_TRIPLE_LINE_QUADRATIC_JET_OK` on success.

This exact symbolic verification checks the pivotal universal polynomial identities, not just a finite collection of example threefolds. It does not replace the geometric basepoint-free pencil argument, the formal implicit-function theorem, the formal node classification, or the published singular-support theorem; those are given as mathematical arguments above.

## Relationship to prior work

Bockondas and Boissière, *Triple lines on a cubic threefold* (first publicly posted 2022-01-21, published 2023), prove that the singular support of the second-type line curve consists exactly of the triple lines (Theorem 1 / Theorem 6). They give the determinant construction used above in their equation (2). In Remark 9, page 755, they explicitly leave open whether these singularities are **always nodal**. The universal nondegenerate quadratic jet established here addresses precisely that missing local analytic conclusion, rather than re-proving their support theorem.

Lahoz, Naranjo, and Rojas describe the second-type divisor class and smoothness for general cubic threefolds; their nodality statement concerning a different auxiliary curve does not imply universal nodality of \(M(X)\). Bockondas and Bossoto (2023) analyze Eckardt points and special configurations of triple lines without supplying the above uniform local quadratic jet. Work on the locus of second-type lines of **cubic fourfolds** treats a different-dimensional space and does not subsume the present threefold statement.

## Limitations

The result is restricted to **smooth complex cubic threefolds** and to the standard determinant scheme structure on the second-type divisor. It does not classify all possible numbers or incidence patterns of triple lines, or assert that this divisor is irreducible. The normalized coordinate construction and formal Morse lemma specifically use characteristic zero; no statement is made for arbitrary positive characteristic. Independent external mathematical validation has not been performed. A possibility of an unindexed equivalent argument remains, despite comparison with the closest published statement and available sources.

## References

1. G. G. Bockondas and S. Boissière, *Triple lines on a cubic threefold*, arXiv:2201.08884 (first posted 2022-01-21); *Comptes Rendus Mathématique* 361 (2023), 747–755, DOI 10.5802/crmath.410. Theorem 6, equation (2), and Remark 9.
2. M. Lahoz, J. C. Naranjo, and A. Rojas, *Geometry of Prym semicanonical pencils and an application to cubic threefolds*, arXiv:2106.08683; *Mathematische Nachrichten* (2023), discussion of the second-type divisor and its class.
3. G. G. Bockondas and L. Bossoto, *Eckardt points on a cubic threefold*, arXiv:2309.08124 (2023).
4. J. P. Murre, *Algebraic equivalence modulo rational equivalence on a cubic threefold*, *Compositio Mathematica* 25 (1972), 161–206.
