# A sharp smoothness boundary for automorphism schemes of box-truncated polynomial algebras

## Finding
Let \(k\) be any field, let \(n\ge 2\) and \(m\ge 2\), and put
\[
 A_{n,m}=k[x_1,\ldots,x_n]/(x_1^m,\ldots,x_n^m),\qquad L=m^n.
\]
Let \(\mathbf{Aut}(A_{n,m})\) denote the affine group scheme representing algebra automorphisms after arbitrary base change.

**Smoothness dichotomy.** This group scheme is smooth over \(k\) if and only if either \(\operatorname{char}k=0\) or \(\operatorname{char}k=p>0\) with \(p\nmid m\). Its Zariski tangent dimension at the identity is exactly
\[
 \dim_k\operatorname{Lie}\mathbf{Aut}(A_{n,m})=
 \begin{cases}
 n(m-1)m^{n-1},&\operatorname{char}k\nmid m,\\
 nm^n,&\operatorname{char}k=p\mid m.
 \end{cases}
\]
Here \(\operatorname{char}k\nmid m\) includes characteristic zero.

**Explicit infinitesimal obstruction.** When \(p\mid m\) and \(p^e\) is the largest power of \(p\) dividing \(m\), the automorphism group scheme contains a closed subgroup \((\alpha_{p^e})^n\), embedded by independent infinitesimal translations \(x_i\mapsto x_i+a_i\) with \(a_i^{p^e}=0\).

**Prime-power enumeration.** If \(k=\mathbb F_q\) has characteristic \(p\) and \(m=p^e\), then every tuple of elements of the maximal ideal inducing an invertible linear map produces an automorphism. Consequently
\[
 \#\operatorname{Aut}_{\mathbb F_q}(A_{n,p^e})
 =\left(\prod_{j=0}^{n-1}(q^n-q^j)\right)
 q^{n(p^{en}-n-1)}.
\]
In this prime-power case the reduced automorphism group has dimension \(n(m^n-1)\), so its tangent-space excess inside the full group scheme is exactly \(n\).

## Assumptions and scope
The algebra is commutative and unital. Every exponent \(m\) is a common truncation exponent; no assumption of separability or perfectness is imposed on \(k\). Smoothness is scheme-theoretic, not merely smoothness of the reduced algebraic group. The finite-field enumeration requires that the exponent itself be a positive prime power equal to a power of the field characteristic.

## Proof
**1. Representability and tangent dimensions.** The algebra has the \(L=m^n\) monomial basis \(x_1^{a_1}\cdots x_n^{a_n}\) with \(0\le a_i<m\). Choosing \(n\) images \(f_i\in A_{n,m}\) defines an endomorphism precisely when \(f_i^m=0\) for all \(i\). Those endomorphisms inducing invertible matrices on the underlying \(L\)-dimensional vector space form an open subscheme, the automorphism group scheme. A tangent vector at the identity is a tuple \(h_i\in A_{n,m}\) with \((x_i+\varepsilon h_i)^m=0\) modulo \(\varepsilon^2\). The linearized relations are
\[
 m x_i^{m-1}h_i=0\qquad (1\le i\le n).
\]
If \(m\) is invertible in \(k\), multiplication by \(x_i^{m-1}\) retains precisely those monomial coefficients having \(x_i\)-exponent zero; it has rank \(m^{n-1}\). Therefore each \(h_i\) has \((m-1)m^{n-1}\) free coordinates. If \(p\mid m\), every relation linearizes to zero, and every one of the \(nm^n\) coordinates is tangent. This proves the dimension formula, without assuming that tangent vectors integrate to algebraic-group curves.

**2. Smoothness when \(m\) is invertible.** For each \(i\), allow an image \(f_i=x_i u_i\), where \(u_i\) is an arbitrary unit of \(A_{n,m}\). Such images automatically satisfy \(f_i^m=0\), and their linear matrix is diagonal with nonzero diagonal entries. They therefore define automorphisms: the induced cotangent-space map is invertible, and Nakayama's lemma (or induction through powers of the maximal ideal) gives surjectivity, hence bijectivity in finite dimension. The distinct elements \(x_i u_i\) fill the open subset where the coefficient of \(x_i\) is nonzero in the \((m-1)m^{n-1}\)-dimensional vector space \(x_i A_{n,m}\). These images form a smooth locally closed subvariety through the identity of dimension \(n(m-1)m^{n-1}\), equal to the full tangent dimension there. The local dimension of the automorphism scheme at the identity is bounded above by its tangent dimension and below by this subvariety's dimension. Equality makes the local ring regular, so the scheme is smooth at the identity after extending to an algebraic closure. Translation makes the full group scheme smooth; smoothness descends to \(k\).

**3. Failure when \(p\mid m\).** Over an algebraic closure, \(A_{n,m}\) is local with unique maximal ideal \(\mathfrak m=(x_1,\ldots,x_n)\). Every field-valued automorphism preserves this ideal. Thus each of the \(n\) coordinate images has zero constant coefficient, and the reduced underlying automorphism variety lies in an affine space of dimension \(n(L-1)\). Its local dimension is at most \(n(L-1)\). The tangent space at the identity nevertheless has dimension \(nL\). This strict difference proves nonregularity and nonsmoothness for every \(p\mid m\), irrespective of whether \(m\) is a prime power.

**4. Explicit translation subgroup.** Write \(m=p^e s\) with \(p\nmid s\). For elements \(a_i\) in any commutative base algebra satisfying \(a_i^{p^e}=0\), the substitution \(x_i\mapsto x_i+a_i\) respects the relations, since
\[
 (x_i+a_i)^m=(x_i^{p^e}+a_i^{p^e})^s=x_i^m=0.
\]
The inverse translation is \(x_i\mapsto x_i-a_i\). Coordinatewise translation embeds \((\alpha_{p^e})^n\) as a closed subgroup, its parameters recovered by the constant coefficients of the images.

**5. Prime-power count and exact tangent excess.** If \(m=p^e\), the Frobenius identity shows that every element of \(\mathfrak m\) has \(m\)-th power zero. Therefore every \(n\)-tuple from \(\mathfrak m\) satisfying the invertible cotangent-matrix condition is an automorphism. The linear coefficient matrix has \(\prod_{j=0}^{n-1}(q^n-q^j)\) choices; the \(n(L-1-n)\) higher-degree coefficients are independent. The same description geometrically exhibits the reduced group as an open subset of \(\mathbb A^{n(L-1)}\). Its dimension is \(n(L-1)\), exactly \(n\) smaller than the full group-scheme tangent dimension.

## Verification
The standalone script `verify.py` independently multiplies elements in the box-truncated quotient and exhaustively counts automorphisms in three small cases: \((n,m,q)=(2,2,2)\) gives \(24\), \((2,2,3)\) gives \(72\), and \((2,3,2)\) gives \(2048\). It also calculates the relation-Jacobian nullity in sixty triples \((n,m,p)\) and compares against the proved piecewise tangent formula. Its expected output is `VERIFY_OK aut_counts=3 tangent_cases=60`. These finite computations are checks, not proofs of arbitrary \(n,m\).

## Relationship to prior work
Díaz, Lucchini Arteche, and Manzano-Flores (arXiv:2609.13741, first posted 2026-09-12) study the automorphism group of zero-dimensional monomial algebras over algebraically closed characteristic-zero fields, particularly the reduced algebraic-group structure. The scheme-theoretic positive-characteristic smoothness boundary above is not a conclusion of their characteristic-zero hypotheses.

Ma (arXiv:2609.31711, first posted 2026-09-20) examines the height-one algebra \(k[x_1,\ldots,x_n]/(x_1^p,\ldots,x_n^p)\) and related Cartan-type group schemes, including a non-smooth full automorphism scheme and its smooth reduced coordinate subgroup. That prime-exponent case is prior work and is not claimed as new here. The contribution is the sharp if-and-only-if smoothness boundary for all common exponents \(m\) and all \(n\ge2\), together with the uniform tangent dimension and explicit exponent-dependent infinitesimal subgroup. A classical single-variable characteristic-two example \(k[x]/(x^2)\) and its non-smooth automorphism scheme also precede this result.

## Limitations
This does not classify the full reduced automorphism group for composite \(m\) divisible by its characteristic, nor compute the nilradical or infinitesimal length of the full group scheme. The prime-power counting formula is a supporting exact specialization, not a new general enumeration of all truncated-algebra automorphism groups. Prior related literature on smoothness of automorphism schemes of Artin complete intersections may contain an equivalent criterion not located in the inspected sources; absolute historical priority is not asserted.

## References
1. R. Díaz, G. Lucchini Arteche, G. Manzano-Flores, *The structure of automorphism groups of zero-dimensional monomial algebras*, arXiv:2609.13741 (2026), https://arxiv.org/abs/2609.13741.
2. C. Ma, *Extremal Derived Length in the Unipotent Radicals of Cartan-Type Automorphism Groups*, arXiv:2609.31711 (2026), Sections 2 and 5, https://arxiv.org/abs/2609.31711.
3. *Topics in group schemes and surfaces in positive characteristic*, Annali dell'Università di Ferrara (2024), Example 3.11, https://link.springer.com/article/10.1007/s11565-024-00514-8.
4. R. Díaz, Á. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (2024), https://arxiv.org/abs/2408.02197.
