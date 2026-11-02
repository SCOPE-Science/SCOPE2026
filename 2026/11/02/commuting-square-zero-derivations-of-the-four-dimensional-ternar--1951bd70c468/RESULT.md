# Commuting square-zero derivations of a four-dimensional ternary Lie algebra: exact ranks and component geometry

## Finding
Let \(q\) be an odd prime power and \(m\ge1\). Equip \(V=\mathbb F_q^4\) with the standard symmetric form and the ternary Filippov bracket uniquely specified by \(\langle[u,v,w],z\rangle=\det(u,v,w,z)\). For each \(i\), let \(D_i:V\to V\) be a derivation satisfying \(D_i^2=0\), and require \(D_iD_j=D_jD_i\) for all \(i,j\). The following assertions classify their compatible tuples, their ranks, and their reduced parameter-space components.

Every nonzero square-zero derivation has rank exactly \(2\). Write \(\mathcal C_m(q)\) for the set of ordered compatible tuples and set
\[
F_{m,q}(T_1,\ldots,T_m)=\sum_{(D_1,\ldots,D_m)\in\mathcal C_m(q)}\prod_{i=1}^m T_i^{\operatorname{rank}(D_i)}.
\]
Then
\[
\boxed{\displaystyle F_{m,q}=1+2(q+1)\biggl[\prod_{i=1}^{m}(1+(q-1)T_i^2)-1\biggr]+(q+1)^2\biggl[\prod_{i=1}^{m}(1+2(q-1)T_i^2)-2\prod_{i=1}^{m}(1+(q-1)T_i^2)+1\biggr].}
\]
Equivalently, for every nonempty support \(S\subseteq\{1,\ldots,m\}\) of cardinality \(s\), the coefficient of \(\prod_{i\in S}T_i^2\) (and of no other variables) equals
\[
\boxed{(q-1)^s\left[2(q+1)+(2^s-2)(q+1)^2\right].}
\]
The empty support has coefficient \(1\), and all other rank patterns have coefficient zero. In particular,
\[
\boxed{\#\mathcal C_m(q)=(q+1)^2(2q-1)^m-2q(q+1)q^m+q^2.}
\]
For \(m=1\), the reduced affine solution variety has exactly two irreducible components, each of dimension \(2\). For every \(m\ge2\), it has exactly \(2^m\) geometrically irreducible components, all defined over \(\mathbb F_q\): precisely two have dimension \(m+1\), while the other \(2^m-2\) have dimension \(m+2\). Hence it is non-equidimensional for every \(m\ge2\).

## Assumptions and scope
A derivation of the ternary algebra is an \(\mathbb F_q\)-linear map \(D\) obeying \(D[u,v,w]=[Du,v,w]+[u,Dv,w]+[u,v,Dw]\) for all inputs. Square-zero means the ordinary composition \(D^2\) is the zero endomorphism. Commutation refers to ordinary composition, not ternary multiplication. The standard form on \(\mathbb F_q^4\) has Gram matrix \(I_4\); the alternating bracket is the four-dimensional volume dual. All formulas cover every odd prime power, including characteristic \(3\), without an algebraically closed ground-field assumption. The component assertions concern the reduced affine algebraic variety, not the full potentially nonreduced defining scheme. We make no claim about characteristic \(2\) or arbitrary ternary Lie algebras.

## Proof
**1. Exact derivation algebra.** By the four-variable determinant differentiation identity,
\[
\sum_{j=1}^{3}\det(u_1,\ldots,Du_j,\ldots,u_3,z)=\operatorname{tr}(D)\det(u_1,u_2,u_3,z)-\det(u_1,u_2,u_3,Dz).
\]
The derivation identity is therefore equivalent to \(D+D^{\mathsf T}=\operatorname{tr}(D)I_4\). Taking traces gives \(2\operatorname{tr}(D)=4\operatorname{tr}(D)\), so \(\operatorname{tr}(D)=0\) in odd characteristic, and precisely \(D^{\mathsf T}=-D\). Thus \(\operatorname{Der}(V)=\mathfrak{so}_4(\mathbb F_q)\).

**2. Two tensor-factor ideals.** A nondegenerate four-dimensional quadratic space of determinant square over an odd finite field is split. The Gram determinant of \(I_4\) is \(1\), so the space is isometric to \(U\otimes W\), where \(U\) and \(W\) are symplectic planes with symmetric tensor-product form \(\omega_U\otimes\omega_W\). The six-dimensional space of skew endomorphisms is exactly the image of the injective map
\[
\mathfrak{sl}(U)\oplus\mathfrak{sl}(W)\longrightarrow\mathfrak{so}(U\otimes W),\qquad (A,B)\longmapsto A\otimes I_W+I_U\otimes B.
\]
Injectivity follows by partial trace, since \(2\) is invertible and the two matrices have trace zero; equality of dimensions gives surjectivity. The two summands are commuting Lie ideals.

**3. Square-zero rigidity and rank.** Cayley--Hamilton gives \(A^2=aI_U\) and \(B^2=bI_W\) for traceless two-by-two matrices. Thus, for the displayed derivation,
\[
D^2=(a+b)I_{U\otimes W}+2A\otimes B.
\]
Taking the partial trace over \(W\) forces \(a+b=0\); hence \(A\otimes B=0\), so either \(A=0\) or \(B=0\). In the remaining factor the square-zero condition reads \(A^2=0\) or \(B^2=0\). A nonzero such two-by-two matrix has rank one, so the corresponding four-dimensional tensor endomorphism has rank \(2\). This proves that the square-zero locus is exactly the union of two nilpotent quadratic cones in distinct ideals, meeting at zero.

**4. Commutation in a single ideal.** A traceless two-by-two square-zero matrix has coordinates \(\bigl(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\bigr)\) satisfying \(a^2+bc=0\). Its projectivization is a split smooth conic with \(q+1\) rational points, each representing a line with \(q-1\) nonzero matrices; hence its full square-zero cone has \(q^2\) rational points. If \(A\ne0\) is nilpotent, its centralizer in \(\mathfrak{sl}_2\) equals \(\mathbb F_q A\) (put \(A\) in rank-one Jordan form and solve the commutator equations). Therefore all nonzero entries in a commuting tuple drawn from the same ideal lie on one common nilpotent line. Entries drawn from opposite ideals automatically commute.

**5. Count each rank support without multiplicity.** For a prescribed nonempty support of size \(s\), choosing one of two pure ideals gives \(2(q+1)(q-1)^s\) tuples, because the nilpotent line is chosen in \(q+1\) ways and each active coordinate receives a nonzero scalar. For a nonconstant assignment of the \(s\) active coordinates to the two ideals, there are \(2^s-2\) assignments; each admits \((q+1)^2(q-1)^s\) tuples. Since the two ideals intersect only at zero, these types are disjoint and exhaustive. This yields the coefficient formula, the product-form generating polynomial, and after setting all \(T_i=1\), the displayed total.

**6. Geometry and dimensions.** For \(r\ge1\), the variety of commuting nilpotent \(r\)-tuples in one \(\mathfrak{sl}_2\) factor is the affine cone parametrized by a projective nilpotent line and \(r\) scalar coordinates. It is geometrically irreducible of dimension \(r+1\) (it is the affine cone over the Segre product of the split nilpotent conic and \(\mathbb P^{r-1}\)). For each of the \(2^m\) assignments of all \(m\) coordinate positions to the two ideals, the corresponding closed compatible-tuple locus is the product of one or two such irreducible varieties (a missing ideal contributes a point). Its dimension is \(m+1\) in the two monochromatic assignments and \(m+2\) in the mixed assignments. Each locus has a dense subset on which every assigned coordinate is nonzero and hence cannot lie in the locus of any different assignment. No locus is contained in another; their union is the complete solution locus, establishing the claimed irreducible-component census for its reduced variety.

## Verification
A standalone arithmetic checker (`CHECK.py`) constructs all six-parameter skew matrices in dimension four and checks square-zero identities, the original ternary derivation identity on all basis triples, ranks, pairwise commutation, and every coefficient of the rank polynomial. It performs exhaustive compatible-pair checks for \(q=3,5,7\), compatible-triple checks for \(q=3,5\), and an independent tensor-model square-zero/pair check over the genuine extension field \(\mathbb F_9\). Exact recorded output is in `CHECK_OUTPUT.txt`; execute `python CHECK.py` in a Python 3 environment. In particular, the commuting pair counts are \(193,1441,5377,14401\) for \(q=3,5,7,9\), respectively. These finite tests do not substitute for the proof valid for all odd prime powers and all tuple lengths.

## Relationship to prior work
The canonical four-dimensional metric ternary Lie algebra and derivations of metric Lie 3-algebras are classical objects; see Papadopoulos (2008) and de Medeiros--Figueroa-O'Farrill--Méndez-Escobar (2008). The split orthogonal Lie algebra, nilpotent cone in \(\mathfrak{sl}_2\), and one-dimensional centralizers of nonzero nilpotents are standard ingredients, not claimed as new. Panyushev's 1999 work treats general nilpotent pairs in semisimple Lie algebras and their characteristics; Fulman--Guralnick (2016) enumerates commuting and nilpotent pairs in classical matrix Lie algebras. These sources do not explicitly establish this simultaneous endomorphism-square-zero constraint, its all-arity rank polynomial, or the \(2^m\)-component non-equidimensional locus for ternary derivations. Historical priority is provisional; a stronger result specialized from a general orthogonal commuting-tuple classification remains possible.

## Limitations
Characteristic two is excluded. The classification is for this particular four-dimensional volume-form ternary Lie algebra and its full coefficient-linear derivation algebra. It does not cover arbitrary 3-Lie algebras, arbitrary nilpotent (rather than square-zero) derivations, conjugacy classes of tuples, or nonreduced scheme structure. The affine component formula is for reduced varieties only. Mathematical review beyond the present proof and exhaustive publication-priority verification have not been performed.

## References
1. G. Papadopoulos, *M2-branes, 3-Lie Algebras and Plücker relations*, arXiv:0804.2662 (first posted 2008-04-16), https://arxiv.org/abs/0804.2662.
2. P. de Medeiros, J. Figueroa-O'Farrill, E. Méndez-Escobar, *Metric Lie 3-algebras in Bagger-Lambert theory*, arXiv:0806.3242 (first posted 2008-06-19), https://arxiv.org/abs/0806.3242.
3. D. I. Panyushev, *Nilpotent pairs in semisimple Lie algebras and their characteristics*, arXiv:math/9906049 (first posted 1999-06-08), https://arxiv.org/abs/math/9906049.
4. J. Fulman, R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (first posted 2016-11-16), https://arxiv.org/abs/1611.05499.
