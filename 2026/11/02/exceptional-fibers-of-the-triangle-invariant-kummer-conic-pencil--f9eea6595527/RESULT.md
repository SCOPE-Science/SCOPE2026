# Exceptional fibers of the triangle-invariant Kummer-conic pencil

## Finding
Let \(k\) be an algebraically closed field of characteristic \(p>0\), let \(q=p^e\) with \(e\ge1\), and set \(n=q-1\). Consider the degree-\(2n\) pencil
\[
 C_{[\lambda:\mu]}:\quad
 \lambda(X^n+Y^n+Z^n)^2+\mu\bigl((XY)^n+(YZ)^n+(ZX)^n\bigr)=0
 \quad\subset\mathbb P^2_k.
\]
For finite \(\lambda\), write \(C_\lambda=C_{[\lambda:1]}\). **All its geometric fibers are classified as follows.**

1. **The Cremona fiber \(\lambda=0\).** The curve is geometrically irreducible, and its normalization is the Fermat curve of degree \(n\), with genus \((n-1)(n-2)/2\). If \(n>1\), the only singularities are the three coordinate vertices, each an ordinary \(n\)-fold point of delta invariant \(n(n-1)/2\). For \(n=1\), it is a smooth conic.
2. **The split-conic fiber \(\lambda=-1/3\), if \(p\ne3\).** The reduced curve consists of two distinct smooth degree-\(n\) Fermat-type curves. They meet transversely in exactly \(n^2\) ordinary nodes, all in the coordinate torus.
3. **The tangent-conic fiber \(\lambda=-1/4\), if \(p\ne2\).** Since \(n\) is even, put \(d=n/2\). The reduced curve consists of four distinct smooth Fermat-type components of degree \(d\). Its singular locus comprises exactly \(3n=6d\) points on the coordinate axes. Exactly two components pass through each such point; their smooth branches have intersection multiplicity \(d\). Equivalently the local analytic type is \(A_{n-1}\), given by \(v^2-u^n=0\) after a local change of coordinates.
4. **All other finite parameters.** The fiber is smooth and geometrically irreducible of degree \(2n\), hence has genus \((2n-1)(2n-2)/2\).
5. **The pencil member at infinity.** The scheme \(C_{[1:0]}\) is the nonreduced double of the smooth degree-\(n\) Fermat curve.

The listed finite exceptional parameters are pairwise distinct whenever they exist, and there are no additional singular or reducible fibers. Every geometric singular point in cases 1–3 is \(\mathbb F_q\)-rational. In characteristic two only cases 1 and 2 occur among exceptional finite members; in characteristic three only cases 1 and 3 occur.

## Assumptions and scope
All geometric claims are over \(k=\overline{\mathbb F}_p\) or an arbitrary algebraically closed field of the indicated characteristic. The exponent \(n=q-1\) is always prime to \(p\). A Fermat-type curve means a curve \(aX^m+bY^m+cZ^m=0\) with three nonzero coefficients and \(p\nmid m\); it is smooth and irreducible. The node description is for the reduced fibers. At the exceptional four-component fiber, \(A_{n-1}\) is the two-branch plane-curve singularity of contact order \(n/2\); the analytic equation is valid in odd characteristic because \(2n\) is invertible. No claim is made about stable reduction or arithmetic monodromy of this pencil.

## Proof
### 1. A tame power map reduces the problem to conics
Set \(U=X^n\), \(V=Y^n\), \(W=Z^n\). The finite separable map
\[
 \pi_n:\mathbb P^2_k\longrightarrow\mathbb P^2_k,
 \qquad [X:Y:Z]\longmapsto[X^n:Y^n:Z^n]
\]
is étale on the coordinate torus and ramified only on the three coordinate axes. Each finite member is the pullback of
\[
 Q_\lambda:\quad \lambda(U+V+W)^2+UV+VW+WU=0.
\]
At a coordinate vertex of the \((U,V,W)\)-plane the conic equation has value \(\lambda\), so \(Q_\lambda\) avoids all three vertices whenever \(\lambda\ne0\).

For \(p\ne2\), the symmetric matrix of this conic has diagonal entries \(\lambda\), off-diagonal entries \(\lambda+1/2\), and determinant \((3\lambda+1)/4\). Thus it is singular precisely for \(\lambda=-1/3\) when \(p\ne3\). For \(p=2\), its partial derivatives are \(V+W,U+W,U+V\), which have common zero \([1:1:1]\); this lies on \(Q_\lambda\) precisely when \(\lambda=1=-1/3\). Consequently the same split-conic condition \(\lambda=-1/3\), defined whenever \(p\ne3\), covers characteristic two as well. In characteristic three the conic never degenerates.

On the axis \(U=0\), the conic becomes
\[
 \lambda(V+W)^2+VW=0.
\]
For \(p\ne2\), its binary discriminant is \(4\lambda+1\). Hence, when \(\lambda\ne0\), it meets each coordinate axis transversely except when \(\lambda=-1/4\), where it has a unique tangency on each axis. In characteristic two its mixed coefficient is one, so it always meets each axis transversely away from vertices. If the conic is smooth, avoids vertices, and meets the three coordinate axes transversely, its pullback is smooth: this is immediate on the torus by étaleness, and on an axis from the nonvanishing derivative along that axis. A smooth positive-degree plane curve is geometrically irreducible by Bézout, proving case 4.

### 2. The zero fiber is a Cremona transform of Fermat
At \(\lambda=0\), the defining form is
\[
 (XY)^n+(YZ)^n+(ZX)^n
 =\bigl(U^n+V^n+W^n\bigr)\big|_{[U:V:W]=[YZ:ZX:XY]}.
\]
The standard quadratic Cremona map \([X:Y:Z]\dashrightarrow[YZ:ZX:XY]\) is an involutive isomorphism on the torus. Fermat's smooth degree-\(n\) curve meets the torus in a dense irreducible open set, so its strict inverse image is irreducible. No coordinate line is a component of the displayed form. This proves irreducibility and the stated normalization.

At \([1:0:0]\) the local equation is \(y^n+z^n+y^nz^n=0\). For \(n>1\), its tangent cone \(y^n+z^n\) has \(n\) distinct linear factors because \(p\nmid n\); thus this is an ordinary \(n\)-fold point with delta invariant \(n(n-1)/2\). The same argument applies at the other two vertices. No other singularities occur because the conic is smooth and the inverse power map is étale on the torus. For \(n=1\), the equation is a smooth conic. Its normalization genus follows from Fermat's degree and smoothness (and agrees with the plane genus formula after subtracting three delta invariants).

### 3. The rank-two conic splits into two Fermat curves
Suppose \(p\ne3\) and \(\lambda=-1/3\). Choose a primitive cube root of unity \(\omega\in k\). The elementary identity
\[
 -3Q_{-1/3}=(U+\omega V+\omega^2W)(U+\omega^2V+\omega W)
\]
holds in every such characteristic, including \(p=2\). Pullback gives two smooth Fermat-type degree-\(n\) components, with no common component. The two conic lines intersect only at \([U:V:W]=[1:1:1]\), a torus point. Its inverse image is the \(n^2\)-point set \(\{[1:\zeta:\eta]:\zeta^n=\eta^n=1\}\). Since \(\pi_n\) is étale there, the two components meet transversely at each point, giving exactly \(n^2\) nodes. Because \(n=q-1\), \(\mu_n=\mathbb F_q^\times\), so all these points are \(\mathbb F_q\)-rational.

### 4. The tritangent conic yields four Fermat components
Suppose \(p\ne2\), \(\lambda=-1/4\), and \(d=n/2\). Put \(A=X^d\), \(B=Y^d\), \(C=Z^d\). The Heron identity gives the exact factorization
\[
 C_{-1/4}:\qquad
 \frac14(A+B+C)(A+B-C)(A-B+C)(-A+B+C)=0.
\]
All four factors are distinct smooth degree-\(d\) Fermat-type forms; \(p\nmid d\). For each of the six pairs, the two linear equations in \(A,B,C\) imply that one of \(A,B,C\) is zero and the remaining two are equal or opposite. Hence the pair intersects on a coordinate axis in precisely \(d\) distinct points, and no point lies on three factors. After using one component equation as a local coordinate, the other has leading term a nonzero multiple of the \(d\)-th power of the transverse axis coordinate; each component is smooth there. Hence their intersection multiplicity is exactly \(d\). There are six pairs, giving \(6d=3n\) singular support points, each with precisely two smooth branches and contact order \(d\). For example, at an intersection of \(A+B+C=0\) and \(A+B-C=0\), one has \(Z=0\). Since \(d\) is invertible and \(XY\ne0\), \(v=A+B\) is a formal local coordinate, and the union has equation \((v+C)(v-C)=v^2-Z^{2d}=0\). The other five pairs are symmetric. Thus the local analytic type is exactly \(A_{n-1}\). The points are the axis points with equal \(n\)-th powers of the other two coordinates, so they belong to \(\mathbb P^2(\mathbb F_q)\).

### 5. Exhaustion and the infinite member
The conic analysis shows that the only possible singular finite parameters are the vertex condition \(\lambda=0\), the conic-rank condition \(3\lambda+1=0\) (when meaningful), and the axis-tangency condition \(4\lambda+1=0\) (when meaningful). Cases 2–4 describe all singularities at these parameters and prove that no other finite fibers are singular. The member at \([1:0]\) is by definition \((X^n+Y^n+Z^n)^2=0\), the double Fermat curve. This completes the classification.

## Verification
The included standalone script `verify_triangle_pencil.py` (Python 3 with SymPy) confirms the conic determinant and binary discriminant, the two exact factorization identities, and the arithmetic-genus conservation identities. It then enumerates singular rational supports in \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_9,\mathbb F_{25}\) for the listed special and generic parameters. The symbolic identities apply in every characteristic after the stated exclusions; finite tests are auxiliary checks, not proofs that a geometric singular locus has been exhausted.

## Relationship to prior work
Borges, Korchmáros and Speziali introduced the \(\Delta_q\)-invariant pencil with this precise equation in their 2022 preprint, Section 4.7 and Theorem 4.22, in the course of classifying plane curves with large linear automorphism groups. Their preprint identifies the pencil, but its discussion does not give the above singular-fiber stratification, Fermat/Cremona normalizations, and contact-order classification. Its stated nonsingularity of all finite pencil members is incompatible with the displayed exact exceptional factorizations; this is a comparison with the publicly accessible 2022 preprint, not an assertion about any changes in the 2024 journal version. General knowledge of Fermat curves and abelian Kummer covers explains the tools but does not by itself specify the exceptional parameters and all local singularity types of this fixed pencil.

## Limitations
The classification is geometric over algebraically closed fields. It concerns the particular coefficient-marked plane model, not every curve with a triangle-preserving automorphism group. Only the singular support and local analytic types of the reduced fibers are asserted; no claim about the full relative discriminant scheme or stable reduction is made. The 2024 journal version of the motivating article was not available for complete text comparison; it could contain additional treatment. Possible equivalents in unindexed literature are a priority risk. No independent audit has been performed.

## References
1. H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1, first public 2022-02-11, especially Section 4.7, Theorem 4.22, https://arxiv.org/html/2202.05765v1 . Journal version: *Finite Fields and Their Applications* **96** (2024), article 102402, https://doi.org/10.1016/j.ffa.2024.102402 .
2. W. de Paula Ferreira, P. Speziali, *Optimal plane curves of degree \(q-1\) over a finite field*, arXiv:2211.14288 (2022), https://arxiv.org/abs/2211.14288 . Its degree-\(q-1\) extremal-point classification is distinct from the degree-\(2(q-1)\) pencil classified here.
3. K. Karagiannis, *Representations on canonical models of generalized Fermat curves and their syzygies*, *Quarterly Journal of Mathematics* **76** (2025), 95–107, https://doi.org/10.1093/qmath/haae064 . The discussion of tame abelian covers and ordinary Fermat curves supplies background, not the claimed exceptional-fiber result.
