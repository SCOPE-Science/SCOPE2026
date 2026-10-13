# Subalgebra and ideal Grassmannians of free class-two Zinbiel algebras

## Finding
Let \(K\) be any field, let \(V\) be an \(n\)-dimensional \(K\)-vector space with \(n\geq 1\), and give the nonunital algebra
\[
A_n(K)=V\oplus(V\otimes_K V),\qquad
(v,t)\circ(w,s)=(0,v\otimes w)
\]
its displayed bilinear product. This is the free nilpotent Zinbiel algebra of class two on \(n\) generators. Put \(T=V\otimes_KV\).

**Complete parametrization.** Each embedded linear subalgebra \(S\leq A_n(K)\) has a unique triple \((W,Z,f)\), where \(W\leq V\), \(Z\leq T\), and \(f:W\to T/Z\) is linear, subject to
\[
W\otimes W\ \subseteq\ Z.
\]
The corresponding subspace is the inverse graph
\[
S(W,Z,f)=\{(w,t):w\in W,\ t+Z=f(w)\}.
\]
It is a two-sided ideal if and only if the stronger condition
\[
(W\otimes V)+(V\otimes W)\ \subseteq\ Z
\]
holds. The maps \(f\) are unrestricted beyond linearity.

**Abstract types.** If \(\dim W=r\) and \(\dim Z=z\), then, as a nonunital Zinbiel algebra,
\[
S\ \cong\ A_r(K)\ \oplus\ K^{\,z-r^2},
\]
where the second factor has zero multiplication. Distinct pairs \((r,z)\) give nonisomorphic subalgebras, since \(\dim S=r+z\) and \(\dim S^2=r^2\). Thus the total numbers of distinct abstract subalgebra and ideal isomorphism types, respectively, are
\[
\sum_{r=0}^n(n^2-r^2+1)
\quad\text{and}\quad
\sum_{r=0}^n((n-r)^2+1).
\]
These are abstract types; they are **not** automorphism-orbit counts of embeddings.

**Complete joint finite-field spectra.** For any prime power \(q\), let \({a\brack b}_q\) denote the number of \(b\)-dimensional subspaces of \(\mathbb F_q^a\), with value zero outside \(0\leq b\leq a\). Over \(K=\mathbb F_q\), the numbers of subalgebras and two-sided ideals with \(\dim W=r\), \(\dim Z=z\), and hence total dimension \(r+z\), are exactly
\[
N_{n,q}^{\mathrm{sub}}(r,z)
={n\brack r}_q
 {n^2-r^2\brack z-r^2}_q q^{\,r(n^2-z)}
\]
and
\[
N_{n,q}^{\mathrm{ideal}}(r,z)
={n\brack r}_q
 {(n-r)^2\brack z-(2nr-r^2)}_q q^{\,r(n^2-z)}.
\]
These formulas are interpreted as zero when the Gaussian coefficient has inadmissible parameters. In particular, the complete dimension polynomials are the sums
\[
P_{n,q}^{\bullet}(X)=
\sum_{r=0}^n\sum_{z=0}^{n^2}
N_{n,q}^{\bullet}(r,z)X^{r+z},
\qquad \bullet\in\{\mathrm{sub},\mathrm{ideal}\}.
\]
For \(n=2\) and \(q=2\) they specialize to
\[
P_{2,2}^{\mathrm{sub}}(X)=1+15X+59X^2+99X^3+43X^4+3X^5+X^6,
\]
\[
P_{2,2}^{\mathrm{ideal}}(X)=1+15X+35X^2+15X^3+7X^4+3X^5+X^6.
\]
Thus the six-dimensional algebra has exactly \(221\) embedded subalgebras and \(77\) embedded two-sided ideals. It has \(10\) abstract subalgebra types and \(8\) abstract ideal types.

## Assumptions and scope
No restriction is imposed on the characteristic of \(K\). Products and subspaces are \(K\)-bilinear. The nilpotency class is two in the sense that all products involving three factors vanish, with any association. A subalgebra is a linear subspace closed under the product, not necessarily containing a unit (the algebra has no unit). An ideal means closed under multiplication with every ambient element on both sides. The counts over finite fields distinguish embedded subspaces, not chosen bases or abstract isomorphism types. The labels \((r,z)\) record quotient-image and degree-two-intersection dimensions.

## Proof
**1. Zinbiel structure and universal property.** Since \(T\) annihilates \(A_n(K)\) from both sides, any triple product vanishes. In particular the Zinbiel relation \((x\circ y)\circ z=x\circ(y\circ z)+x\circ(z\circ y)\) holds over every field. The only quadratic products of the chosen generators are the independent ordered tensors in \(V\otimes V\). Any map from the generator space into a class-two Zinbiel algebra extends uniquely to an algebra morphism by sending \(v\otimes w\) to the product of the corresponding images. Consequently the displayed algebra is the free class-two object.

**2. Graph parametrization.** Let \(\pi:A_n(K)\to V\) be the first-coordinate projection. Given a subspace \(S\), put \(W=\pi(S)\) and \(Z=S\cap T\). Each \(w\in W\) has some lift \((w,t)\in S\); its class \(t+Z\) is independent of the lift. This defines a unique linear map \(f:W\to T/Z\). Conversely the indicated inverse graph is a linear subspace with exactly this data. The product of two lifts of \(w,w'\in W\) equals \((0,w\otimes w')\); it lies in \(S\) precisely when \(w\otimes w'\in Z\). Bilinearity yields \(S\circ S\subseteq S\iff W\otimes W\subseteq Z\). Since the ambient first-coordinate projections range over all of \(V\), the analogous calculation for both products with ambient elements gives \(A_n(K)\circ S+S\circ A_n(K)\subseteq S\iff(V\otimes W)+(W\otimes V)\subseteq Z\).

**3. Dimension of tensor conditions.** Put \(r=\dim W\) and choose a vector-space complement \(U\) with \(V=W\oplus U\). The direct-sum decomposition
\[
T=(W\otimes W)\oplus(W\otimes U)\oplus(U\otimes W)\oplus(U\otimes U)
\]
shows \(\dim(W\otimes W)=r^2\), whereas
\[
\dim((W\otimes V)+(V\otimes W))
=n^2-(n-r)^2=2nr-r^2.
\]
There is no intersection correction left uncounted: the common part \(W\otimes W\) appears once.

**4. Finite-field enumeration without overcounting.** There are \({n\brack r}_q\) choices of \(W\). Fix one. If the required tensor subspace has dimension \(d\), choosing a \(z\)-dimensional \(Z\) containing it is equivalent to choosing a \((z-d)\)-subspace of an \((n^2-d)\)-space, giving \({n^2-d\brack z-d}_q\). Each such \(Z\) allows exactly \(q^{r(n^2-z)}\) linear maps \(W\to T/Z\). Step 2 proves these maps label distinct embedded subspaces and exhaust all of them. Substituting \(d=r^2\) or \(d=2nr-r^2\) gives both displayed formulas, including all boundary cases \(r=0\) and \(r=n\).

**5. Abstract algebra types.** Choose a linear section \(W\to S\) and a complement \(Z'\) of \(W\otimes W\) inside \(Z\). The section's ordered products form the independent tensor basis of \(W\otimes W\); their products with any element, and all products involving \(Z'\), vanish. Thus \(S\) is the direct sum of the free class-two algebra on \(W\) and the zero-product algebra \(Z'\). Since \(S^2=W\otimes W\), the invariants \((\dim S,\dim S^2)=(r+z,r^2)\) recover the pair \((r,z)\) uniquely. For subalgebras \(r^2\leq z\leq n^2\), and for ideals \(2nr-r^2\leq z\leq n^2\); counting these admissible integer pairs gives the two type-count sums.

**6. Extremal subalgebras.** A proper subalgebra must have \(W\neq V\), since \(W=V\) would force \(Z=T\), hence \(S=A_n(K)\). Every proper \(S\) lies in \(W\oplus T\), so all maximal proper subalgebras are exactly the inverse images of hyperplanes in \(V\). Their intersection is \(T\). Moreover if \(W\neq0\), then \(w\otimes w\neq0\) for nonzero \(w\), so \(S\) is not zero-product. Hence the abelian (zero-product) subalgebras are precisely the subspaces of \(T\).

## Verification
The embedded script `checker.py` independently enumerates every row-reduced-echelon subspace of \(A_n(\mathbb F_q)\) for \((n,q)=(1,2),(1,3),(2,2),(2,3)\). It tests multiplication closure and both-sided ideal closure directly against the multiplication table and compares the complete observed joint \((r,z)\) count with the Gaussian formulas. It reports respectively \(5,6,2825,56632\) ambient subspaces and concludes `VERIFY_OK`; the \((2,2)\) case yields \(221\) subalgebras and \(77\) ideals, and the \((2,3)\) case \(949\) and \(229\). This finite exhaustion verifies small cases, not the arbitrary-field statement; the latter is supplied by Steps 1–6. To reproduce, run `python3 checker.py` with Python 3.8 or newer (a recent Python is needed for modular inverses).

## Relationship to prior work
Ceballos and Towers (2022) study maximal abelian subalgebras and ideals of general Zinbiel algebras, proving codimension theorems and tabulating maximal dimensions in low dimensions. In contrast, the present result classifies **every** subalgebra and ideal of one natural, unrestricted-rank free class-two family, records their abstract types, and gives simultaneous finite-field \((r,z)\) multiplicities. Camacho and collaborators (2023) explain free Zinbiel structures and classify certain Zinbiel superalgebras, rather than these Grassmannians. Bauer and Schein (2022) treat ideal-zeta rationality for class-two nilpotent algebras over compact valuation rings; those general results do not explicitly give the present finite-field joint spectra or subalgebra types. These comparisons do not rule out an equivalent statement under terminology from truncated free associative algebras or abstract tensor-algebra incidence geometry.

## Limitations
No formula is claimed for automorphism-conjugacy orbits of embedded subalgebras, nor for other Zinbiel multiplication tensors with quadratic relations. The word “free” is relative to the class-two nilpotent variety, not the unrestricted free Zinbiel algebra. The finite-field coefficient formulas include all prime powers, but exhaustive computer enumeration was performed only for the stated prime-field cases. The classification of an embedded subalgebra and the abstract classification of its algebra structure are separate conclusions. No independent scientific audit has been performed.

## References
1. M. Ceballos and D. A. Towers, *Abelian subalgebras and ideals of maximal dimension in Zinbiel algebras*, arXiv:2202.03214v1 (first public version 7 February 2022); inspected public full text arXiv:2202.03214v2. https://arxiv.org/abs/2202.03214
2. L. M. Camacho, A. Fernández Ouaridi, I. Kaygorodov, and R. M. Navarro, *Zinbiel superalgebras*, arXiv:2304.00273. https://arxiv.org/abs/2304.00273
3. T. Bauer and M. M. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865. https://arxiv.org/abs/2202.10865
