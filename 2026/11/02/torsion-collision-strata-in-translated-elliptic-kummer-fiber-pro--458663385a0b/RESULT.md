# Torsion-collision strata in translated elliptic Kummer fiber products

## Finding
Let \(E/\mathbb C\) be the elliptic curve \(y^2=x^3-1\), with identity \(O\), and let \(T=(0,i)\) be its point of order three. Fix an integer \(m\ge5\) with \(\gcd(m,6)=1\). For any integer \(r\ge2\), take pairwise distinct points \(Q_1,\ldots,Q_r\in E(\mathbb C)\), and let \(X_m\to E\) be the cyclic degree-\(m\) map from the smooth projective model of \(v^2=u^{3m}-1\), sending \((u,v)\) to \((u^m,v)\). Form the fiber product over \(E\) of its \(r\) translates: the \(j\)-th factor has generic equation \(u_j^m=x(P+Q_j)\), where \(P\in E\) is the base parameter. Denote this (possibly reducible or singular) fiber product by \(Y_{m,\boldsymbol Q}\).

Partition \(\{Q_1,\ldots,Q_r\}\) by cosets of \(H=\{O,T,-T\}\). Let \(c\) be the number of occupied cosets, and \(t\) the number of cosets containing all three of their points. Then **the normalization of \(Y_{m,\boldsymbol Q}\) is a disjoint union of exactly \(m^t\) smooth, connected curves**. Every component maps Galoisly to \(E\), with group \((\mathbb Z/m\mathbb Z)^{r-t}\) and degree \(m^{r-t}\), and has genus
\[
\boxed{\;1+\frac{3c}{2}\,m^{r-t-1}(m-1).\;}
\]
Its branch locus on \(E\) consists of precisely \(3c\) distinct points, all with inertia order \(m\). In particular, if no coset is full, the fiber product has just one irreducible component; a complete three-point torsion orbit produces exactly one multiplicative degree loss and a factor of \(m\) in the number of components. This is an exhaustive classification for the stated domain; no generic-position condition on the distinct \(Q_j\) is imposed.

## Assumptions and scope
All curves, function fields and normalizations are over \(\mathbb C\). The base elliptic curve has its usual chord-and-tangent group law. The integer \(m\ge5\) is odd and not divisible by three. The \(Q_j\) are pairwise distinct, although their differences may equal \(\pm T\). The theorem concerns the normalization of the fiber product, not the connectedness of the unnormalized scheme at intersections between components. It does not assert that the induced double-cover family in a moduli space has a unique global choice of square root.

## Proof
**1. Translation identity.** On \(E:y^2=x^3-1\), addition of \(T=(0,i)\) and \(-T=(0,-i)\) gives, as rational functions,
\[
x(P+T)=-\frac{2(1+iy)}{x^2},\qquad
x(P-T)=-\frac{2(1-iy)}{x^2}.
\]
Multiplying and using \(y^2+1=x^3\) yields
\[
\boxed{\ x(P)x(P+T)x(P-T)=4.\ }
\]
Translating \(P\) by an arbitrary \(Q\) yields the same identity for the three shifts \(Q,Q+T,Q-T\). Since \(\mathbb C\) contains all \(m\)-th roots of four, every complete orbit supplies a relation between the \(m\)-th-root covers.

**2. Exact number of independent Kummer classes.** In the function field \(K=\mathbb C(E)\), put \(f_Q(P)=x(P+Q)\). Its divisor is
\[
\operatorname{div}(f_Q)=[T-Q]+[-T-Q]-2[-Q].
\]
Within a fixed \(H\)-coset, the valuation columns for the three shifts, in a suitable ordering of its three support points, are
\[
D_0=(-2,1,1),\quad D_1=(1,-2,1),\quad D_2=(1,1,-2).
\]
The sum of these columns is zero, while the determinant of the minor formed by their first two columns and first two rows is \(3\). As \(3\) is a unit in \(\mathbb Z/m\mathbb Z\), the kernel for one or two columns is trivial, and that for all three columns is exactly the diagonal \(\{(a,a,a):a\in\mathbb Z/m\mathbb Z\}\).

Different cosets have disjoint support. Consequently, if \(\prod_j f_{Q_j}^{a_j}\) is an \(m\)-th power in \(K\), all exponent classes must be zero except possibly constant triples on completely occupied cosets. Conversely, the translation identity makes each of these diagonal triples an \(m\)-th-power relation. Thus the kernel of \((\mathbb Z/m\mathbb Z)^r\to K^*/K^{*m}\) consists of exactly \(t\) independent diagonal relations, and the span has order \(m^{r-t}\).

By Kummer theory, the compositum of all the cyclic extensions \(K(u_j)/K\), with \(u_j^m=f_{Q_j}\), is a Galois field extension of degree \(m^{r-t}\) and group \((\mathbb Z/m\mathbb Z)^{r-t}\). The original generic tensor-product algebra has total dimension \(m^r\), and it is reduced and finite étale over \(K\). Hence it has exactly \(m^t\) field factors, each isomorphic to this compositum. These factors are precisely the function fields of the irreducible components of the normalization.

**3. Branch locus and genus.** The branch support contributed by a coset \(Q+H\) is \(-Q+H\). Supports from different cosets do not intersect. Each occupied coset contributes exactly its three support points. At each such point at least one chosen \(f_{Q_j}\) has valuation \(1\) or \(-2\). Because \(m\) is odd, the local tame Kummer inertia has order exactly \(m\). There are no other branch points. On each connected component the Riemann--Hurwitz formula for the degree \(d=m^{r-t}\) cover of a genus-one curve therefore becomes
\[
2g-2=(3c)d\left(1-\frac1m\right),
\]
which is equivalent to the displayed genus formula. This completes the proof.

## Verification
The accompanying `verify.py` (Python 3 with SymPy) checks the exact addition-law identity modulo the Weierstrass equation, verifies the determinant-three valuation minor and the full modular kernels for \(m=5,7,11,13,17,19\), and checks inertia and genus computations for representative occupancy patterns. Invoke `python verify.py`; the expected terminal line is `VERIFY_OK: translation, valuation kernels, inertia, and genus examples`. The unlimited parameter claim follows from the proof and is **not** inferred from finite enumeration.

For \(m=5\), two shifts from different cosets give genus \(61\), whereas two shifts in the same coset give genus \(31\), both connected. A triple within one coset gives five components, each of genus \(31\). Four shifts occupying one full coset and one additional singleton give five components, each of genus \(301\), compared with genus \(3001\) for four shifts from distinct cosets. The reduced generic degree across components remains \(m^r\) in every case. In the separated case \(c=r\), \(t=0\), the formula reduces to \(1+\frac{3r}{2}m^{r-1}(m-1)\), reproducing the genus calculation under the original disjoint-branch hypothesis.

## Relationship to prior work
Stewart's 2026 construction uses the same translated cyclic covers \(X_m\to E\) to build complete families of curves in moduli, and computes the genus under the separation condition \(Q_j-Q_l\ne\pm T\) (Section 4.2). That hypothesis forces distinct branch supports and rules out all the collision patterns classified here. The present statement is the complementary **exact irreducible-component and genus classification on every excluded torsion-collision stratum** for \(\gcd(m,6)=1\); it does not claim novelty for Stewart's construction or the standard Kummer and Riemann--Hurwitz techniques.

Pagani's general theory concerns moduli and connectedness of abelian covers of elliptic curves, and Chen studies simply branched elliptic covers. They supply context but do not by their stated results identify the explicit three-term translation relation, the torsion-orbit occupancy data, or this formula for Stewart's specific translated fiber product. Full-text comparisons for some general antecedents remained incomplete; see the separate review for the residual priority risk.

## Limitations
The theorem excludes integers divisible by two or three; their local inertia and Kummer relations may have additional phenomena. It classifies the normalized fiber-product curves, not the degree of the ensuing moduli map, the uniqueness of each auxiliary double cover, or an isomorphism classification of different components. It makes no assertion about integral models or positive-characteristic specialization. The exact theorem is proved internally and has not received independent mathematical validation; historical priority remains provisional.

## References
- Chloe Stewart, *Complete Families of Curves in the Moduli Space of Genus g Curves*, arXiv:2606.03779, first submitted 2026-06-02, especially Sections 2--4, https://arxiv.org/abs/2606.03779 .
- Nicola Pagani, *Moduli of abelian covers of elliptic curves*, arXiv:1303.2991, first submitted 2013-03-12, https://arxiv.org/abs/1303.2991 .
- Dawei Chen, *Simply branched covers of an elliptic curve and the moduli space of curves*, arXiv:0806.0674, first submitted 2008-06-04, https://arxiv.org/abs/0806.0674 .
