# Two-component geometry and compatible families of modular cyclic-four Rota–Baxter operators

## Finding
Let \(k\) be any field of characteristic two and let \(A=k[C_4]\). For a generator \(g\) of \(C_4\), put \(t=g-1\), identifying \(A\cong k[t]/(t^4)\). A \(k\)-linear map \(P:A\to A\) is a weight-zero Rota–Baxter operator if and only if it has the following **unique** form:
\[
\begin{aligned}
P(1)&=a t^2+b t^3,\\
P(t)&=c t^2+d t^3,\\
P(t^2)&=f t^3,\\
P(t^3)&=0,
\end{aligned}
\qquad a,b,c,d,f\in k,\quad cf=0.
\]
Thus the **reduced** operator variety is the union of exactly two affine four-spaces, \(\{c=0\}\) and \(\{f=0\}\), meeting in an affine three-space. Every operator satisfies \(P^3=0\), and \(P^2\ne0\) holds exactly when \(af\ne0\).

An ordered family \((P_1,\ldots,P_m)\), \(m\ge1\), is called *linearly compatible* if each \(k\)-linear combination \(\sum_i\lambda_iP_i\) is again a weight-zero Rota–Baxter operator. Such a family is linearly compatible **if and only if** all its members lie in one and the same one of the two affine-four-space components. Consequently the reduced compatible-family variety has exactly two irreducible components \(\mathbb A_k^{4m}\), meeting in \(\mathbb A_k^{3m}\). These two four-dimensional operator spaces are exactly the maximal vector spaces consisting entirely of weight-zero Rota–Baxter operators.

For \(k=\mathbb F_q\), \(q\) a power of two, the complete number of linearly compatible ordered families is
\[
\boxed{\mathcal C_m(q)=2q^{4m}-q^{3m}.}
\]
The joint linear-rank generating polynomial is
\[
\boxed{\Phi_m(z_1,\ldots,z_m)=2\prod_{i=1}^mF_q(z_i)-\prod_{i=1}^mG_q(z_i),}
\]
where
\[
\begin{aligned}
F_q(z)&=1+(q^3+q^2-q-1)z+q(q-1)^2(q+1)z^2,\\
G_q(z)&=1+(2q^2-q-1)z+q(q-1)^2z^2.
\end{aligned}
\]
In particular, the individual rank counts are \(1\) at rank zero, \(2q^3-q-1\) at rank one, and \(q(q-1)^2(2q+1)\) at rank two. The number with operator nilpotency index exactly three is \(q^2(q-1)^2\).

## Assumptions and scope
The field is arbitrary of characteristic \(2\) for the normal form, reduced geometry, maximal compatible linear spaces, and compatibility criterion. Finite-field formulas assume \(q=2^e\), \(e\ge1\). The operator is an arbitrary \(k\)-linear map, not necessarily an algebra homomorphism. It satisfies the weight-zero identity
\[
P(x)P(y)=P\bigl(P(x)y+xP(y)\bigr)\quad(x,y\in A).
\]
Rank always means \(k\)-linear rank of \(P:A\to A\). Compatibility concerns linear combinations of operators, not commutation under composition. Geometric statements concern underlying reduced varieties; no statement is made about the nonreduced operator scheme.

## Proof
**1. The group-algebra model.** In characteristic two the binomial identity gives \((g-1)^4=g^4-1=0\). The elements \(1,t,t^2,t^3\) are linearly independent because their changes of basis to \(1,g,g^2,g^3\) are triangular with diagonal units. Hence \(A\cong k[t]/(t^4)\).

**2. Square-zero outputs.** Taking \(x=y\) in the Rota–Baxter identity gives \(P(x)^2=P(2xP(x))=0\). For an element \(u=u_0+u_1t+u_2t^2+u_3t^3\), we have \(u^2=u_0^2+u_1^2t^2\). Since \(k\) is a field, \(u^2=0\) implies \(u_0=u_1=0\). Thus every output belongs to the square-zero ideal \((t^2)\), so products of any two outputs vanish. Initially write
\[
P(1)=at^2+bt^3,\quad P(t)=ct^2+dt^3,\quad
P(t^2)=et^2+ft^3,\quad P(t^3)=ht^2+jt^3.
\]

**3. Forced vanishings and the single equation.** Apply the identity to the basis pairs \((t,t^3)\), \((1,t^3)\), \((1,t^2)\), in that order. Since the left sides vanish, the first gives \(P(tP(t^3))=P(ht^3)=h^2t^2+hjt^3=0\), forcing \(h=0\). The second gives \(P(P(t^3))=P(jt^3)=j^2t^3=0\), forcing \(j=0\). The third gives \(P(P(t^2))=P(et^2+ft^3)=e^2t^2+eft^3=0\), forcing \(e=0\). The pair \((1,t)\) now gives
\[
0=P\bigl(P(t)+tP(1)\bigr)
=P\bigl(ct^2+(d+a)t^3\bigr)=cf\,t^3,
\]
so \(cf=0\). Conversely, for the stated normal form with \(cf=0\), both sides of the identity vanish on all ten unordered pairs of basis vectors: diagonal pairs vanish because the characteristic is two; \((1,t)\) is the displayed equation; \((1,t^2)\), \((1,t^3)\), \((t,t^2)\), \((t,t^3)\), and \((t^2,t^3)\) vanish because \(P(t^3)=0\), \(P(t^2)\in kt^3\), and products beyond degree three vanish. Bilinearity establishes the identity for all inputs. This proves necessity, sufficiency, and uniqueness.

**4. Geometry, nilpotency and compatibility.** The polynomial \(cf\) defines two coordinate hyperplanes in the five-dimensional normal-form parameter space. Its reduced zero set consists of two affine four-spaces intersecting in an affine three-space. The only possibly nonzero value of \(P^2\) on the basis is \(P^2(1)=af\,t^3\); indeed \(P^2(t)=cf\,t^3=0\), and \(P^2(t^2)=P^2(t^3)=0\). Consequently \(P^3=0\) and the criterion for index three is exactly \(af\ne0\).

For compatible operators with coefficients \((c_i,f_i)\), one has \(c_if_i=0\) for every \(i\). If some \(c_i\ne0\), then \(f_i=0\), and compatibility of \(P_i+P_j\) forces \(c_if_j+c_jf_i=c_if_j=0\) for every \(j\); thus all \(f_j=0\). If no \(c_i\) is nonzero, all \(c_j=0\). Conversely, either common condition makes every linear combination an operator. This also proves that precisely the two coordinate four-spaces are maximal linear compatible spaces, and proves the two-component description for every tuple length.

**5. Rank enumeration.** In the basis of the two-dimensional image ideal \((t^2)\), the nonzero rows of the matrix of \(P\) are
\[
\begin{pmatrix}a&c&0&0\\ b&d&f&0\end{pmatrix}.
\]
On the component \(f=0\), rank is the rank of the arbitrary \(2\times2\) matrix with columns \((a,b)^T,(c,d)^T\). Its rank-zero, rank-one, rank-two counts are respectively \(1\), \(q^3+q^2-q-1\), and \(q(q-1)^2(q+1)\). On \(c=0\), the columns are \((a,b)^T,(0,d)^T,(0,f)^T\); rank two occurs exactly when \(a\ne0\) and \((d,f)\ne(0,0)\), giving the identical three counts. On the intersection \(c=f=0\), the rank counts are \(1\), \(2q^2-q-1\), and \(q(q-1)^2\). Inclusion-exclusion over the two components in each of the \(m\) positions proves the claimed joint polynomial. Setting every rank variable to one yields \(2q^{4m}-q^{3m}\). For index three, choose \(a\ne0\), \(f\ne0\), \(c=0\), and arbitrary \(b,d\), giving \(q^2(q-1)^2\).

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The checker constructs arithmetic and the original multiplication table, tests the original Rota–Baxter identity for all ordered basis pairs, and computes ranks by finite-field elimination. Over \(\mathbb F_2\) it examines every one of the \(2^{16}=65536\) linear maps, without assuming the normal form. It finds 24 operators, with rank counts \((1,13,10)\), and 4 of nilpotency index three. It also directly checks all ordered compatible pairs and triples, finding respectively 448 and 7680. Over \(\mathbb F_4\), it independently tests all \(4^8=65536\) maps with images in the mathematically forced square-zero ideal; exactly 448 satisfy the original identity, with ranks \((1,123,324)\) and 144 of index three. The extension-field arithmetic uses the irreducible binary polynomial \(z^2+z+1\). See `verification_output.txt` for the recorded exact output. Finite computations support, but do not replace, the proof over all characteristic-two fields.

## Relationship to prior work
Guo, Rosenkranz and Zheng, arXiv:1407.5306v1 (20 July 2014), develop weight-zero Rota–Baxter operators on untruncated polynomial algebras, focusing on monomial and injective operators and characteristic-zero hypotheses. Their methods and the Rota–Baxter identity are antecedents, but their theorems do not provide the full characteristic-two, length-four quotient classification.

Zheng, Guo and Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three* (2019), provide general coefficient equations and classifications for orders two and three. The generic coefficient identity is known; solving it for the modular cyclic group algebra of order four, together with the compatibility and rank enumerators, is the additional contribution here.

An earlier rank-one Rota–Baxter classification for truncated polynomial algebras already determines the rank-one count \(2q^3-q-1\) for this specific algebra. That count is **not** asserted as new. An earlier result on square-zero-radical local algebras already exhibits index-three operators in characteristic two, but that algebra family has radical square zero and does not determine the present rank-two strata or all-arity compatibility. A previously established unit-value result for modular truncated polynomial algebras supplies a broader constraint on \(P(1)\), not the full operator classification. Finally, the distinct four-dimensional exterior algebra \(k[x,y]/(x^2,y^2)\) is not isomorphic to the one-generator algebra used here: their cotangent dimensions are two and one, respectively.

Farooq, arXiv:2605.15670v1 (15 May 2026), treats square-zero-radical quotients over characteristic-zero fields; neither the algebra length nor the characteristic matches this theorem. Publication priority remains provisional because a more general unpublished or unlocated classification might imply part of the result.

## Limitations
This theorem concerns the modular cyclic group algebra of order four in characteristic two, weight zero only. It does not classify Rota–Baxter operators of nonzero weight, cyclic group algebras of higher order, or the full potentially nonreduced operator scheme. It does not determine conjugacy orbits under the algebra automorphism group. The rank-one specialization and existence of index-three phenomena in other algebras are established prior facts; the assessed new contribution concerns the complete rank-two/full-operator geometry, explicit index-three locus here, and every length of linearly compatible families. Independent mathematical review has not been performed, and exhaustive historical publication priority has not been established.

## References
1. L. Guo, M. Rosenkranz and S. Zheng, *Rota-Baxter operators on the polynomial algebras, integration and averaging operators*, arXiv:1407.5306v1, public 2014-07-20; Pacific Journal of Mathematics 275 (2015), 481–507. https://arxiv.org/abs/1407.5306
2. S. Zheng, L. Guo and M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra 47 (2019), 3094–3116, DOI:10.1080/00927872.2018.1552278. https://pmc.ncbi.nlm.nih.gov/articles/PMC7083595/
3. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1, public 2026-05-15. https://arxiv.org/abs/2605.15670
