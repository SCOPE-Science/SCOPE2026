# Characteristic-two automorphisms of star evolution algebras: a symplectic parity dichotomy

## Finding
Let \(k=\mathbb F_q\) with \(q=2^f\), \(f\ge1\), and let \(m\ge2\). On the vector space \(E_m=ka\oplus W\), with \(W=k^m\), standard dot product \(B(u,v)=\sum_{i=1}^m u_iv_i\), and \(s=(1,\ldots,1)\), define the commutative evolution-algebra multiplication
\[
 (\alpha a+u)(\beta a+v)=B(u,v)a+\alpha\beta s.
\]
Equivalently, the natural basis satisfies \(a^2=\sum_i b_i\), \(b_i^2=a\), and mixed products are zero; this is the unweighted star-graph evolution algebra.

**Theorem.** Every algebra automorphism has the unique form
\[
 G_{c,U}(\alpha a+u)=c\alpha a+c^2Uu,
 \qquad c^3=1,\quad U^tU=I_m.
\]
Consequently \(\operatorname{Aut}_k(E_m)\cong\mu_3(k)\times O(I_m,k)\), where \(\mu_3(k)=\{c\in k^\times:c^3=1\}\). The parity of the number of leaves determines the orthogonal group:
\[
 O(I_{2r+1},k)\cong\operatorname{Sp}_{2r}(k),\qquad
 O(I_{2r+2},k)\cong (\mathbb F_2)^{f(2r+1)}\rtimes\operatorname{Sp}_{2r}(k).
\]
The first formula includes \(r\ge1\), the second \(r\ge0\). In the semidirect product, the precise conjugation action is given below in the coordinates \((u,\beta)\mapsto(Vu,\beta)\), with the nonstandard additive group law also stated explicitly.

In particular, with \(\displaystyle S_r(q)=q^{r^2}\prod_{j=1}^{r}(q^{2j}-1)\), \(S_0(q)=1\), and \(d=\gcd(3,q-1)\), the exact orders are
\[
 |\operatorname{Aut}(E_{2r+1})|=dS_r(q),\qquad
 |\operatorname{Aut}(E_{2r+2})|=d q^{2r+1}S_r(q).
\]
Thus there is a sharp parity transition between symplectic automorphism groups and groups possessing a nontrivial normal elementary abelian subgroup.

## Assumptions and scope
The field is finite of characteristic two, \(q=2^f\), and \(m\ge2\). The algebra is generally nonassociative and nonperfect: \(E_m^2=ka+ks\) has dimension two. The group is the group of ordinary \(k\)-linear multiplicative bijections, not the automorphism group of the underlying abstract graph. The normal-form argument also works for perfect fields of characteristic two; finite-field orders require \(q=2^f\).

## Proof
**1. A forced block decomposition.** Let \(G\) be an invertible linear algebra homomorphism. Write
\[
 G(\alpha a+u)=(c\alpha+\ell(u))a+\alpha v+Tu,
\]
where \(c\in k\), \(v\in W\), \(\ell\in W^*\), and \(T\in\operatorname{End}(W)\). Comparing \(G(uw)\) with \(G(u)G(w)\) for arbitrary \(u,w\in W\), where \(uw=B(u,w)a\), gives
\[
 B(Tu,Tw)=cB(u,w),\qquad
 \ell(u)\ell(w)s=B(u,w)v.
\]
As \(B\) is nondegenerate and \(s\ne0\), the second equality implies \(v=\delta s\) and \(\ell\otimes\ell=\delta B\). Because \(m\ge2\), the bilinear form on the right has rank \(m\) if \(\delta\ne0\), while the left has rank at most one. Hence \(\delta=0\), so \(v=0\), \(\ell=0\). Thus \(G\) is block diagonal. Its invertibility forces \(c\ne0\) and \(T\) invertible. Comparing \(G(a^2)\) and \(G(a)^2\) yields
\[
 T^tT=cI_m,\qquad Ts=c^2s.
\]
The vanishing mixed products are then automatically preserved.

**2. The characteristic-two scalar constraint.** The vector \(s\) is characteristic for the dot product: for all \(u\in W\),
\[
 B(u,u)=B(u,s)^2.
\]
Because \(Ts=c^2s\) and \(B(Tu,Ts)=cB(u,s)\), one has \(B(Tu,s)=c^{-1}B(u,s)\). Squaring and comparing with \(B(Tu,Tu)=cB(u,u)\) forces \(c^{-2}=c\) (choose \(u\) with \(B(u,u)\ne0\)), hence \(c^3=1\). Put \(U=c^{-2}T\). From \(c^3=1\), one obtains \(U^tU=I_m\) and \(Us=s\). Conversely any \(c^3=1\) and any orthogonal \(U\) fix \(s\) and define an automorphism by the displayed formula. Uniqueness and componentwise group multiplication give the direct product.

**3. Odd number of leaves.** If \(m=2r+1\), then \(B(s,s)=1\). The orthogonal complement \(H=s^\perp\) has dimension \(2r\), is nondegenerate, and is alternating because \(B(h,h)=B(h,s)^2=0\) for \(h\in H\). Every orthogonal transformation fixes \(s\), since \(B(Uu,Uu)=B(u,u)\) and the square map is injective, so it restricts to a symplectic transformation on \(H\). Conversely every symplectic transformation of \(H\) extends uniquely by fixing \(s\). This proves \(O(I_{2r+1})\cong\operatorname{Sp}_{2r}\).

**4. Even number of leaves.** If \(m=2r+2\), then \(B(s,s)=0\). Choose \(t=e_1\), so \(B(t,s)=B(t,t)=1\). Let \(H=\langle s,t\rangle^\perp\); it is a nondegenerate alternating subspace of dimension \(2r\). Every orthogonal transformation is uniquely represented by \(V\in\operatorname{Sp}(H)\), \(u\in H\), and \(\beta\in k\), via
\[
 U(s)=s,\qquad U(t)=t+u+\beta s,\qquad
 U(h)=Vh+B(u,Vh)s\quad(h\in H).
\]
These formulas preserve all pairings on the basis decomposition \(W=ks\oplus kt\oplus H\), and hence give every orthogonal transformation: fixing \(s\) forces \(U(t)\) to have coefficient one along \(t\); preserving pairings uniquely determines the other terms, while the induced map on the symplectic quotient is \(V\). At \(V=I\), the composition law is
\[
 (u,\beta)(u',\beta')=(u+u',\beta+\beta'+B(u,u')).
\]
Because \(B\) is alternating in characteristic two, this kernel is abelian of exponent two, of cardinality \(q^{2r+1}\). The section \(V\mapsto U_{0,0,V}\) proves that the extension splits. Conjugation by the section sends \((u,\beta)\) to \((Vu,\beta)\), giving the claimed semidirect product.

**5. Group orders.** A symplectic basis can be constructed successively by choosing any nonzero first vector, a partner pairing to one, and descending to its orthogonal complement. This yields the standard factorization \(S_r(q)=q^{r^2}\prod_{j=1}^r(q^{2j}-1)\). The multiplicative group \(\mathbb F_q^\times\) is cyclic of order \(q-1\), giving \(|\mu_3(k)|=\gcd(3,q-1)\). Multiplying proves both formulas.

## Verification
Run `python3 verify.py` with Python 3 and the standard library; expected output is in `checks.txt`. The program performs independent full enumeration of invertible multiplicative matrices in the full \((m+1)\)-dimensional ambient endomorphism space for \((m,q)=(2,2),(3,2),(2,4)\), with exact counts \(2,6,12\). Independently it enumerates full orthogonal matrix spaces for \((m,q)=(2,2),(3,2),(4,2),(2,4),(3,4)\), giving \(2,6,48,4,60\), respectively. Every candidate is checked against the original multiplication, not solely the normal form. A separate scalar-family check covers additional values. These are finite examples, not a proof of the all-parameter theorem.

## Relationship to prior work
Elduque and Labra introduced structural graph methods for evolution algebras and gave finite-automorphism results for perfect evolution algebras (2013 preprint). Star-graph evolution algebras here satisfy \(\dim E_m^2=2<m+1\), so those perfect-algebra theorems do not determine their automorphism groups. Existing odd-characteristic star-family automorphism classifications rely on orthogonal-group methods but do not cover the characteristic-two characteristic-vector identity used in the present proof. The isomorphisms and finite-field orders of symplectic and orthogonal groups themselves are standard and are not claimed as new. The asserted contribution is the full characteristic-two star-evolution-algebra automorphism identification, including its even/odd unipotent-versus-reductive dichotomy.

## Limitations
The result assumes \(m\ge2\), characteristic two and an unweighted star with the specified algebra multiplication. It does not classify automorphisms of arbitrary graph evolution algebras, weighted stars, or arbitrary characteristics. All finite tests have bounded dimension/field size and cannot establish infinite-parameter correctness; the preceding direct algebraic proof supplies that implication. Unidentified earlier specialized automorphism classifications may affect historical priority; independent mathematical audit has not been performed.

## References
1. Alberto Elduque and Alicia Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1, first public 2013-12-17, https://arxiv.org/abs/1312.4685.
2. Paula Cadavid, Mary Luz Rodiño Montoya and Pablo M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516, 2017, https://arxiv.org/abs/1710.10516.
3. Keith Conrad, *Finite fields* (standard facts on cyclic multiplicative groups); for the classical symplectic-group order, see any standard finite classical groups text. Neither classical fact is asserted to be original.
