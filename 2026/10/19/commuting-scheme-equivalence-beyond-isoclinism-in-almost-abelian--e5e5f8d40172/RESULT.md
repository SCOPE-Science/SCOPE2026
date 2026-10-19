# Commuting-scheme equivalence beyond isoclinism in almost-abelian Lie algebras

## Finding
Let \(k\) be any field, let \(V\) be a \(d\)-dimensional vector space, and let \(D:V\to V\) have rank \(r\ge2\). Form the almost-abelian Lie algebra \(L_D=kh\ltimes_D V\), with \([h,v]=Dv\) and \([V,V]=0\). Put \(c=d-r\). For each \(s\ge2\), the scheme of ordered pairwise-commuting \(s\)-tuples in \(L_D\) depends, up to **linear scheme isomorphism**, only on \((d,r,s)\), not on the similarity type of \(D\). More precisely, it is the affine scheme with coordinates \(a_i\), \(y_{ji}\) and \(z_{\ell i}\), for \(1\le i\le s\), \(1\le j\le r\), \(1\le\ell\le c\), and equations
\[
 a_i y_{j h}-a_h y_{j i}=0\qquad(1\le i<h\le s,\ 1\le j\le r).
\]
Its **reduced geometric support** has exactly two irreducible components: the linear subspace \(a_1=\cdots=a_s=0\), of dimension \(ds\), and the rank-at-most-one locus of the \((r+1)\times s\) matrix with first row \((a_i)\) and remaining rows \((y_{ji})\), times affine \(cs\)-space, of dimension \(cs+r+s\). Their intersection is the rank-at-most-one locus of the \(r\times s\) matrix \((y_{ji})\), times affine \(cs\)-space, of dimension \(cs+r+s-1\). The support is equidimensional exactly when \(r=s=2\).

For \(k=\mathbb F_q\), let \(N_s\) count pairwise-commuting ordered \(s\)-tuples, and let \(R_s(t)\) enumerate the ranks of their **joint-adjoint maps** for all ordered tuples (not just commuting tuples), where \(\Psi_{\boldsymbol x}:L_D\to L_D^s\) sends \(b\) to \(([x_1,b],\ldots,[x_s,b])\). Then
\[
 N_s=q^{ds}+q^{cs+r}(q^s-1),
\]
\[
 R_s(t)=q^{cs}\left[1+(q^{rs}-1)t+(q^s-1)q^r t^r+(q^s-1)(q^{rs}-q^r)t^{r+1}\right].
\]
In particular the entire family of geometric commuting schemes, finite-field commuting counts, and joint-centralizer rank frequencies fails to determine Lie-algebra isomorphism or even nilpotency class. Over **every** field, the two five-dimensional nilpotent algebras with \(D\) of Jordan types \((3,1)\) and \((2,2)\) have all these same invariants, although their nilpotency classes are respectively three and two; they are not isoclinic. Five is the smallest dimension in which this same-rank nilpotent almost-abelian example can occur.

## Assumptions and scope
Every displayed geometric statement refers to the support of the reduced base change to an algebraic closure. We **do not** assert that the original scheme is reduced. The asserted scheme equivalence is exact, not merely pointwise. The rank enumerator assumes a finite field and \(r,s\ge2\); it counts all \(q^{(d+1)s}\) tuples. A nilpotent \(D\) is required only for the final five-dimensional example, not for the general theorem. The formulas hold in characteristic two.

## Proof
1. Write \(x_i=a_i h+v_i\). Bilinearity and \([V,V]=0\) give
\[
 [x_i,x_h]=a_iDv_h-a_hDv_i.
\]
Choose a linear splitting \(V=U\oplus\ker D\). The map \(D|_U:U\to\operatorname{im}D\) is an isomorphism. Use coordinates \(y_i=Dv_i\in k^r\) and \(z_i\in k^c\) for the kernel component. All defining commutator polynomials are exactly the displayed equations; the \(z_i\) are free. If \(D_1,D_2\) have the same rank, there are invertible maps \(R,S\) satisfying \(D_2R=SD_1\). Consequently the linear map \((a,v)\mapsto(a,Rv)\) carries **each** commutator equation for \(D_1\) to an invertible linear combination (via \(S\)) of those for \(D_2\). This proves an isomorphism of the defining ideals and affine schemes for every tuple length.

2. With \(A=(a_i)\) and \(Y=(y_{ji})\), if \(A=0\) the equations impose no condition on \(Y\). If \(A\ne0\), select an index \(i\) with \(a_i\ne0\). The equations imply \(y_{jh}=(a_h/a_i)y_{ji}\) for all \(h,j\), so the stacked matrix \([A;Y]\) has rank at most one. Conversely either condition implies the commutator equations. These are two irreducible closed sets over an algebraic closure: one is affine linear, the other is the image closure of the outer-product parametrization \((u,v)\mapsto uv^\mathsf T\). Both are maximal, since \(r,s\ge2\) allows \(A=0\) with \(Y\) of rank two, and the rank-one locus also has points with \(A\ne0\). The affine rank-one \(m\times s\) determinantal locus has dimension \(m+s-1\), by its dense nonzero outer-product parametrization modulo the one-dimensional scaling. The intersection and all dimensions follow. Equality \(ds=cs+r+s\) reduces to \((r-1)s=r\), whose only integer solution for \(r,s\ge2\) is \(r=s=2\).

3. Over \(\mathbb F_q\), when \(A=0\) there are \(q^{rs}\) choices for \(Y\). For each of the \(q^s-1\) nonzero \(A\), the equations say \(Y=uA\) with an arbitrary column \(u\in\mathbb F_q^r\), giving \(q^r\) choices. Multiply by \(q^{cs}\) choices for free kernel coordinates to obtain \(N_s\). This proves the formula over every extension field as well. In particular the Hasse–Weil zeta function of the reduced commuting variety over \(\mathbb F_q\) is
\[
 Z_s(T)=\frac{1-q^{cs+r}T}{(1-q^{ds}T)(1-q^{cs+r+s}T)}.
\]

4. For any ordered tuple \(\boldsymbol x\), the joint-adjoint map factors through the domain \(k\oplus\operatorname{im}D\) and has the form
\[
 (b,u)\longmapsto (a_i u-b y_i)_{i=1}^s.
\]
If \(A=0\) its rank is zero exactly when \(Y=0\), and one otherwise. If \(A\ne0\), the \(u\)-part is injective of rank \(r\); the extra \(b\)-column belongs to its image exactly when \(Y=u_0A\) for some \(u_0\in k^r\). Otherwise the rank is \(r+1\). The respective counts before the free-kernel factor are \(1\), \(q^{rs}-1\), \((q^s-1)q^r\), and \((q^s-1)(q^{rs}-q^r)\). This proves \(R_s(t)\), whose coefficients sum to \(q^{(d+1)s}\).

5. In dimension five choose \(d=4,r=2\) and write \(D_{31}\) for the nilpotent matrix with a Jordan block of size three and a zero block; write \(D_{22}\) for two size-two nilpotent blocks. Both have rank two, so Steps 1–4 give equal schemes and enumerators. However \(D_{31}^2\ne0\), \(D_{31}^3=0\), while \(D_{22}^2=0\). The descending central series satisfies \(\gamma_{j+1}(L_D)=D^jV\), so the two nilpotency classes are three and two. Furthermore \(Z(L_D)=\ker D\) for \(r>0\), and \(L_{D_{31}}/Z(L_{D_{31}})\) is nonabelian whereas \(L_{D_{22}}/Z(L_{D_{22}})\) is abelian. Hence the algebras are neither isomorphic nor isoclinic, since isoclinism requires an isomorphism between the central quotients. For \(d\le3\), the nilpotent partitions of \(d\) have pairwise different ranks (number of nonzero Jordan superdiagonal entries), so no lower-dimensional same-rank nilpotent almost-abelian pair exists.

## Verification
The standalone `verify.py` constructs Lie brackets directly from two distinct four-by-four nilpotent matrices and from the three-by-three nilpotent Jordan block, computes actual joint-adjoint matrices and finite-field ranks, and independently enumerates all commuting tuples. Its exhaustive results cover the two five-dimensional algebras over \(\mathbb F_2\) for tuple lengths two and three and over \(\mathbb F_3\) for length two, plus the four-dimensional example over \(\mathbb F_3\) for length two. For \(\mathbb F_2\), the five-dimensional pair has rank-frequency vector \((16,240,192,576)\) at length two and \((64,4032,1792,26880)\) at length three; the respective commuting-tuple counts are \(448\) and \(5888\). For \(\mathbb F_3\), their length-two rank counts are \((81,6480,5832,46656)\), with \(12393\) commuting pairs. These experiments check instances; the infinite family and geometric assertions are proved algebraically above.

## Relationship to prior work
Richardson (1979) established irreducibility of the commuting **pair** variety of reductive Lie algebras and noted reducible solvable cases, not the present classification. Goodwin–Röhrle (arXiv:1209.1289v1, September 2012), §3.5, identified two components for the pair commuting variety of the \(B_2\) Borel nilradical, a four-dimensional filiform instance in suitable characteristic. Its pair-component statement is prior art, not a new claim here. The present statement concerns **all** almost-abelian Lie algebras of arbitrary dimension and rank, **all** tuple lengths, an exact scheme-level linear equivalence and joint-centralizer rank polynomials, including the nonisoclinic class-two/class-three collision. Salemkar–Mirzaei (2010) develop Lie isoclinism; the exhibited pair has nonisomorphic central quotients, making a deduction from its isoclinism inapplicable. No claim of absolute priority from a search alone is made.

## Limitations
This does not classify Lie-isomorphism types, schemes of arbitrary Lie algebras, or their nonreduced scheme structure. The reducible pair-variety phenomenon itself is known in related cases. Only the specific universal rank-only theorem, formulas, and nonisoclinic collision are submitted. A specialized prior publication giving an equivalent all-arity result may exist; independent review remains unperformed.

## References
- R. W. Richardson, *Commuting varieties of semisimple Lie algebras and algebraic groups*, Compositio Mathematica 38 (1979), 311–327; https://www.numdam.org/item/CM_1979__38_3_311_0/.
- S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289v1, first posted 2012-09-06; https://arxiv.org/abs/1209.1289.
- A. R. Salemkar and F. Mirzaei, *Characterizing n-isoclinism classes of Lie algebras*, Communications in Algebra 38 (2010), 3392–3403, https://doi.org/10.1080/00927870903117535 (online 2010-09-30).
