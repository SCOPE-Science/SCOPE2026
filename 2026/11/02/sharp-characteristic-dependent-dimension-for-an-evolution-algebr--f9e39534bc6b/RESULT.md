# Sharp characteristic-dependent dimension for an evolution algebra with infinitely many natural bases and no nontrivial automorphisms

## Finding

Let \(K\) be any infinite field. Let \(d(K)\) be the least positive integer for which a nondegenerate finite-dimensional evolution \(K\)-algebra \(E\) has the following two properties: its ordinary group \(\operatorname{Aut}_K(E)\) has only the identity element, yet there are infinitely many natural bases of \(E\) up to permutation and independent nonzero rescaling of basis vectors. Then
\[
d(K)=\begin{cases}2,&\operatorname{char}(K)=2,\\3,&\operatorname{char}(K)\ne2.\end{cases}
\]
In particular, an evolution algebra can have an infinite set of inequivalent natural bases while its entire ordinary automorphism group is finite (indeed trivial), answering the finite-automorphism part of Question 14 in [1]. The least possible dimension is determined exactly, including its dependence on characteristic.

## Assumptions and scope

An evolution algebra is a commutative, possibly nonassociative \(K\)-algebra admitting a *natural basis* \(e_1,\ldots,e_n\) with \(e_i e_j=0\) for distinct indices. It is *nondegenerate* if every \(e_i^2\ne0\), equivalently if its annihilator is zero. A natural-basis class identifies bases obtained by permutation and multiplying each basis vector by an arbitrary element of \(K^\times\). The automorphism group is the group of invertible \(K\)-linear maps preserving multiplication; no group-scheme or base-extension assertion is made. The field is required to be infinite. All constructions and lower bounds below work without assuming algebraic closure or perfection of \(K\).

## Proof

**Characteristic two, dimension two.** On \(K e_1\oplus K e_2\), define \(e_1^2=e_2^2=e_1\), \(e_1e_2=0\). This algebra is nondegenerate. For an automorphism \(T\), the equality \(T(e_1)=T(e_1^2)=T(e_1)^2\) forces \(T(e_1)=c e_1\) with \(c=c^2\). Invertibility forces \(c=1\). Now \(T(e_1)T(e_2)=0\) forces \(T(e_2)=d e_2\), and \(T(e_2)^2=T(e_1)\) forces \(d^2=1\). In characteristic two this implies \(d=1\). Thus \(T=1\).

For each \(a\in K\), put
\[
f_1(a)=a e_1+(1+a)e_2,\qquad f_2(a)=(1+a)e_1+a e_2.
\]
The coefficient matrix has determinant \(a^2-(1+a)^2=1\) in characteristic two. Their product is zero and each squares to \(e_1\), so they are a natural basis. Each \(f_i(a)\) has coordinate sum one. If two such bases are equivalent by scalings and permutations, comparing coordinate sums makes every scalar one, and comparing coordinates gives only the two possibilities \(b=a\) and \(b=1+a\). Each class therefore contains at most two parameters. Since \(K\) is infinite, infinitely many classes exist. Dimension one has just one natural-basis class for any algebra, yielding the minimality of two.

**Uniform dimension-three example.** Over an arbitrary field \(K\), set
\[
e_1^2=e_2^2=u:=e_1+e_3,\qquad e_3^2=v:=e_2+e_3,\qquad e_ie_j=0\ (i\ne j).
\]
The three squares are nonzero, so \(E\) is nondegenerate, while \(\dim E^2=2\). In coordinates,
\[
(x_1,x_2,x_3)(y_1,y_2,y_3)=(x_1y_1+x_2y_2)u+x_3y_3v.
\]
Suppose \(T\) is an automorphism and write \(x=T(e_1)\), \(y=T(e_2)\), \(z=T(e_3)\). Because \(x y=0\) and \(u,v\) are linearly independent, \(x_3y_3=0\). As \(x^2=y^2\), we have \(x_3^2=y_3^2\); a field has no nonzero element with square zero, so \(x_3=y_3=0\). Invertibility makes \(x,y\) a basis of \(U=\operatorname{span}(e_1,e_2)\). The equalities \(xz=yz=0\) then imply \(z=c e_3\), for some \(c\ne0\). Preservation of \(e_1^2=u=e_1+e_3\) gives
\[
x+c e_3=T(u)=x^2=(x_1^2+x_2^2)(e_1+e_3).
\]
The second coordinate comparison shows \(x_2=0\), and the first and third give \(x=\lambda e_1\) and \(c=\lambda\), where \(\lambda\ne0\) and \(\lambda=\lambda^2\). Therefore \(\lambda=c=1\). Finally,
\[
T(v)=T(e_2+e_3)=y+e_3=T(e_3^2)=e_3^2=e_2+e_3,
\]
so \(y=e_2\). Thus \(T=1\), **over every field**.

Assume now \(\operatorname{char}(K)\ne2\). For every \(t\in K\) such that \(1+t^2\ne0\), set
\[
c_t=\frac{1-t^2}{1+t^2},\qquad s_t=\frac{2t}{1+t^2},\qquad
f_1(t)=c_te_1+s_te_2,\quad f_2(t)=-s_te_1+c_te_2,\quad f_3(t)=e_3.
\]
Since \(c_t^2+s_t^2=1\), these three vectors form an orthogonal natural basis: the two-dimensional block has determinant one, its mixed product vanishes, and neither block multiplies nontrivially with \(e_3\). The rational map \(t\mapsto(c_t:s_t)\) is nonconstant and has finite fibers (in fact at most two). A given unordered pair of projective lines \(\{Kf_1(t),Kf_2(t)\}\) therefore arises from only finitely many parameters. Moreover, the other basis line \(Ke_3\) is distinguished by having nonzero third coordinate. Since an infinite field has infinitely many \(t\) with \(1+t^2\ne0\), the natural-basis classes are infinite. This proves \(d(K)\le3\) in odd characteristic and characteristic zero.

**Dimension-two lower bound outside characteristic two.** Let \(K\) be infinite of characteristic different from two and \(E\) a nondegenerate two-dimensional evolution algebra. If \(E\) is perfect, the independent-square argument makes every natural basis monomial relative to a fixed natural basis, hence there is only one natural-basis class. Otherwise \(\dim E^2=1\). Choose a nonzero \(u\in E^2\). Multiplication is expressible as \(xy=B(x,y)u\), where \(B\) is a nondegenerate symmetric bilinear form: its matrix is diagonal with nonzero diagonal entries in a nondegenerate natural basis. Any invertible linear operator \(T\) satisfying \(T(u)=c u\) and \(B(Tx,Ty)=cB(x,y)\) is an algebra automorphism.

If \(B(u,u)\ne0\), orthogonal reflection in the line \(Ku\), namely \(T(x)=2B(x,u)u/B(u,u)-x\), preserves \(B\), fixes \(u\), and acts by minus the identity on the nonzero orthogonal complement. It is a nonidentity automorphism. If \(B(u,u)=0\), pick \(w\) with \(B(u,w)=1\), and replace it by \(w'=w-B(w,w)u/2\); then \(B(w',w')=0\). In the hyperbolic basis \((u,w')\), choose \(c\in K^\times\setminus\{1\}\) and put \(T(u)=c u\), \(T(w')=w'\). The transformation is invertible, has \(T(u)=cu\), and obeys \(B(Tx,Ty)=cB(x,y)\) because both basis vectors are isotropic. It is again a nonidentity automorphism. Thus **no nondegenerate two-dimensional evolution algebra in characteristic different from two has both infinite natural-basis classes and trivial automorphism group**. Along with the one-dimensional observation and three-dimensional example, this completes the claimed sharp dimension formula. \(\square\)

## Verification

The accompanying `verify_natural_basis.py` uses only Python's standard library. For the characteristic-two two-dimensional example it enumerates all \(6\) invertible \(2\times2\) matrices over \(\mathbb F_2\) and finds only the identity as an automorphism. For the three-dimensional example it enumerates all \(168\) invertible \(3\times3\) matrices over \(\mathbb F_2\) and all \(11{,}232\) over \(\mathbb F_3\), again finding only the identity in each case. Exact rational arithmetic verifies \(23\) distinct parameter choices of the rotation basis; direct polynomial coefficient checks modulo two verify the characteristic-two basis identities. The output concludes `VERIFY_OK` and is provided verbatim in `verification_output.txt`. These finite verifications corroborate but do not establish the all-field results, which follow from the proof.

## Relationship to prior work

[1, Question 14] explicitly asks whether a nondegenerate evolution algebra may have infinitely many inequivalent natural bases while its automorphism group is finite. The survey's Proposition 14 constructs an algebra with infinitely many natural bases but an infinite orthogonal symmetry group, so it does not settle the finite-automorphism question. [2, Corollary 2.13] supplies a general natural-family description and [3] classifies nondegenerate evolution algebras through dimension three. Those descriptions provide context; the present theorem specifies explicit automorphism-rigid examples and a sharp characteristic-dependent minimal dimension. A related published research record titled *A single symmetry jump in the \(E_\lambda\) evolution-algebra family* describes automorphism rigidity for a different family but does not assert infinitely many natural bases, the characteristic-two example, or the minimality statement. Existing structural classifications may imply pieces by additional argument, but a fully equivalent statement was not found in the inspected materials.

## Limitations

Only ordinary \(K\)-rational automorphism groups are classified, not automorphism group schemes. Natural bases are identified only by permutation and independent nonzero scaling, not by arbitrary algebra automorphisms. The infinite-field hypothesis is essential to the conclusion of infinitely many bases. The theorem does not classify every evolution algebra with these features, nor the entire natural-basis moduli space. Historical priority cannot be established conclusively from a finite literature search, especially when earlier general classification papers might implicitly contain examples.

## References

[1] I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, publicly posted 15 October 2026, especially Question 14, Proposition 14, and Section 1.1. https://arxiv.org/html/2610.22248v1

[2] N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1, 25 June 2020, especially Corollary 2.13. https://arxiv.org/abs/2006.14460

[3] A. J. Calderón Martín, A. Fernández Ouaridi, I. Kaygorodov, *Non-degenerate evolution algebras*, arXiv:2303.00862v1, 1 March 2023, especially its dimension-two and dimension-three classification. https://arxiv.org/abs/2303.00862
