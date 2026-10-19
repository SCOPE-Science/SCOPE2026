# Generic nonreducedness of the three-dimensional exterior-algebra representation scheme

## Finding
Let \(k\) be any field, and let \(\Lambda=k\langle u,v\rangle/(u^2,v^2,uv+vu)\), the exterior algebra on two generators. Let \(\mathscr R_3\) denote the affine **representation scheme** cut out by the entries of \(X^2\), \(Y^2\), and \(XY+YX\) in the polynomial ring of two generic \(3\times3\) matrices. The claims below distinguish this possibly nonreduced scheme from its reduced geometric support.

**Geometric and infinitesimal theorem.** Over an algebraic closure of \(k\), every closed representation point satisfies \(XY=YX=0\). The reduced support of \(\mathscr R_3\) has two distinct irreducible components, both of dimension \(6\), each containing a dense conjugacy orbit. One is the closure of the orbit represented by \((E_{12},E_{13})\); the other is the closure of the orbit represented by \((E_{13},E_{23})\). Their intersection is irreducible of dimension \(5\) and consists of zero together with the proportional pairs of square-zero rank-one matrices. The scheme \(\mathscr R_3\), unlike its reduced support, has Zariski tangent dimension **\(8\)** at every point of both dense orbits, and therefore is **generically nonreduced along both components**, in every characteristic. The tangent dimension is \(10\) on the nonzero proportional-pair stratum and \(18\) at the origin.

**Arithmetic theorem.** For any finite field \(\mathbb F_q\), the number of labeled three-dimensional representations is exactly
\[
\#\mathscr R_3(\mathbb F_q)=2q^6+q^5-q^3-q^2,
\]
and simultaneous conjugacy has exactly \(q+4\) orbits. Their isomorphism types comprise the zero representation; \(q+1\) projective slopes of nonzero proportional rank-one pairs; and two generic types (common image of dimension one or common kernel of dimension two). This includes characteristic two.

The enumeration and reduced two-component decomposition are included as structural context; the distinctive scheme-theoretic contribution is the **two-component generic tangent excess and explicit nilpotent coordinate functions**, not merely a new description of previously studied radical-square-zero module varieties.

## Assumptions and scope
\(\Lambda\) is a unital associative algebra and representations are unital algebra homomorphisms into \(M_3(k)\). \(E_{ij}\) denotes the matrix unit with a single nonzero entry at row \(i\), column \(j\). The reduced-component statements concern the base change to an algebraic closure. Tangent dimensions are for the scheme defined by the three displayed matrix relations (not the reduced representation variety). The point and orbit formulas hold for every finite field of every characteristic; no smoothness or separability hypothesis is assumed for \(k\). The component count is topological; scheme-theoretic primary multiplicities are not determined.

## Proof
**1. Products vanish at field-valued points.** If \(A\in M_3(K)\) and \(A^2=0\) over any field \(K\), then \(\operatorname{rank}A\le1\). Suppose \(X^2=Y^2=XY+YX=0\) and \(XY\ne0\). The relation forces \(YX=-XY\ne0\). Both \(X\) and \(Y\) have rank one. Since \(\operatorname{im}(XY)\subseteq\operatorname{im}X\) and \(\operatorname{im}(YX)\subseteq\operatorname{im}Y\), their one-dimensional images coincide. Similarly \(\ker Y\subseteq\ker(XY)=\ker(YX)\supseteq\ker X\), and every space here has dimension two, hence the kernels coincide. Two rank-one endomorphisms with identical image and kernel are scalar multiples; their square-zero property then implies \(XY=0\), a contradiction. Thus \(XY=YX=0\) for all field-valued points, including characteristic two.

**2. The reduced components.** Let \(V=K^3\). If \(X,Y\) are not both zero, their image lines either coincide or are distinct. In the first case there is a line \(W\subset V\) containing both images and killed by both maps. In the second case their images span a plane \(K_0\); all products vanish, so \(K_0\subseteq\ker X\cap\ker Y\), forcing \(K_0=\ker X=\ker Y\). Hence the reduced support is the union of the following proper incidence images:
\[
\begin{aligned}
 C_{\mathrm{im}}&=\{(X,Y):\exists W\in\mathbb P(V),\ X(V)+Y(V)\subseteq W,\ X(W)=Y(W)=0\},\\
 C_{\mathrm{ker}}&=\{(X,Y):\exists K_0\in\operatorname{Gr}(2,V),\ X(K_0)=Y(K_0)=0,\ X(V)+Y(V)\subseteq K_0\}.
\end{aligned}
\]
The first incidence space is a rank-four vector bundle \(\operatorname{Hom}(V/W,W)^{\oplus2}\) over \(\mathbb P^2\), and the second is a rank-four vector bundle \(\operatorname{Hom}(V/K_0,K_0)^{\oplus2}\) over the dual \(\mathbb P^2\). Each is irreducible of dimension six, and each proper image has dimension six because a generic independent pair determines \(W\) or \(K_0\) uniquely. Independent covectors (respectively, independent image vectors) form a single dense \(\operatorname{GL}_3(K)\)-orbit, represented by \((E_{12},E_{13})\) and \((E_{13},E_{23})\). They differ by the dimension of their total image, so neither component contains the other. The intersection consists precisely of proportional rank-one square-zero pairs, including zero: a nonzero such pair is determined by a rank-one square-zero line in \(\mathbb P(\operatorname{End}V)\) (dimension three) and a nonzero vector on the corresponding two-dimensional coefficient line modulo common scaling (dimension two); equivalently, the rank-one square-zero orbit has dimension four plus one projective slope, giving dimension five. Irreducibility follows by the parameter space of a square-zero rank-one map and an arbitrary pair of coefficients.

**3. Tangent dimensions.** For \(X,Y\) satisfying the equations, a tangent vector is a pair \((P,Q)\in M_3(K)^2\) obeying
\[
 XP+PX=0,\qquad YQ+QY=0,\qquad XQ+QX+PY+YP=0.
\]
At \((E_{12},E_{13})\), linear elimination gives ten independent conditions on the eighteen entries: \(p_{21}=p_{23}=p_{31}=q_{21}=q_{31}=q_{32}=0\), together with \(p_{11}+p_{22}=0\), \(q_{11}+q_{33}=0\), \(p_{32}+q_{11}+q_{22}=0\), and \(p_{11}+p_{33}+q_{23}=0\). Their coefficient matrix has a unit minor of size ten, so this rank is characteristic-independent. Transposing and permuting basis vectors carries this computation to \((E_{13},E_{23})\), giving tangent dimension eight there too. For \((E_{12},0)\), the first and mixed tangent equations each impose four independent conditions, giving dimension ten. At \((0,0)\), all relations have degree two, giving dimension eighteen. By simultaneous conjugacy, these values hold on the indicated orbits.

Both reduced components have dimension six and dense orbits of smooth points in their reduced structure. Over an algebraically closed (hence perfect) field, a generically reduced finite-type scheme would be smooth on a dense open subset of each generically reduced component. But the full scheme has tangent dimension eight at every point of both dense orbits; hence it cannot be generically reduced along either component.

The extra scheme structure can be seen without a tangent-space argument. Put \(R=K[\varepsilon]/(\varepsilon^2)\) and
\[
 X_{\varepsilon}=E_{12}+\varepsilon E_{32},\qquad Y_{\varepsilon}=E_{13}-\varepsilon E_{22}.
\]
Then \(X_{\varepsilon}^2=Y_{\varepsilon}^2=X_{\varepsilon}Y_{\varepsilon}+Y_{\varepsilon}X_{\varepsilon}=0\), whereas \(X_{\varepsilon}Y_{\varepsilon}=-\varepsilon E_{12}\ne0\). Thus entries of \(XY\) vanish at every geometric point but need not vanish as functions on the representation scheme: they are genuine nilpotents in its coordinate ring. This witness works in characteristic two as well (where minus equals plus).

**4. Finite-field orbit and point counts.** Write \(L=q^2+q+1\) and \(G=|\operatorname{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\). The common-image and common-kernel independent-pair strata each contain exactly \(LG\) rational points. The nonzero proportional-pair stratum has \(L(q^2-1)(q+1)\) rational points: \(L(q^2-1)\) square-zero rank-one maps, multiplied by the \(q+1\) projective slopes. Including the zero pair, the count is
\[
 1+2LG+L(q^2-1)(q+1)=2q^6+q^5-q^3-q^2.
\]
The two independent strata are single \(\operatorname{GL}_3(\mathbb F_q)\)-orbits, as a basis adapted to the common line/plane and two independent linear forms/vectors puts them in the two displayed normal forms. Nonzero proportional pairs have precisely the \(q+1\) invariant slopes, one orbit per slope; zero is a separate orbit. Thus the orbit count is \(2+(q+1)+1=q+4\).

## Verification
`verify.py` is a standard-library-only Python 3 program. Run `python3 verify.py` in the directory containing this document and the program. It directly enumerates all \(3\times3\) square-zero matrices over \(\mathbb F_2\) and \(\mathbb F_3\), selects all anticommuting pairs, confirms both products vanish, computes the entire orbit partition via elementary-generator conjugations and checks tangent ranks for the four normal forms. The output is:

```
q=2: square-zero matrices=22, points=148, orbits=6, sizes=[1,21,21,21,42,42], tangent profiles=(8,8,10,18), quotient tangent profiles=(6,6,9,18)
q=3: square-zero matrices=105, points=1665, orbits=7, sizes=[1,104,104,104,104,624,624], tangent profiles=(8,8,10,18), quotient tangent profiles=(6,6,9,18)
VERIFY_OK
```

The quotient comparison refers to adding the equations \(XY=YX=0\) and illustrates the difference between a reduced-geometry model and the exterior presentation. The proof above, not these finite tests, establishes the theorems for arbitrary fields.

## Relationship to prior work
Bleher, Chinburg and Huisgen-Zimmermann (2014, Theorem 3.12 and Corollary 3.13) determine irreducible components of **reduced module varieties** of algebras with radical square zero. Since every three-dimensional exterior representation has \(XY=YX=0\) at field-valued points, their theory already controls the two-component reduced support; that classification is *not* asserted as an independent novelty. An earlier rank-one anticommuting square-zero matrix obstruction already implies the field-point product vanishing in dimension three; this too is not claimed as novel. Huisgen-Zimmermann (2014) develops a broader reduced-component framework for local truncated path algebras. Morrison (1980) develops representation **schemes** and tangent-space formalism, and includes a different radical-square-zero algebra example. The additional calculation here is that the exterior-algebra relation scheme is generically nonreduced along both dense six-dimensional components with uniform excess two, demonstrated by its explicit tangent equations and by a nonzero square-zero coordinate function. The arithmetic orbit formula refines the labeled-point geometry. No inspected primary theorem furnished these combined dimension-three scheme and rational-orbit conclusions; unlocated more specialized literature remains possible.

## Limitations
The theorem describes the reduced support, tangent dimensions at each geometric orbit type, an explicit nilpotent element of the coordinate ring, and rational point/orbit counts. It does **not** compute the generic primary multiplicities, embedded associated primes, a full scheme-theoretic primary decomposition, or deformation-obstruction spaces in higher order. The program exhausts only the two indicated finite fields; no claim of exhaustive computational verification for arbitrary characteristic or field size is made. Novelty remains subject to independent specialist literature review.

## References
1. F. M. Bleher, T. Chinburg and B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045v1, first public 2014-07-11, especially Theorem 3.12 and Corollary 3.13. https://arxiv.org/pdf/1407.3045
2. B. Huisgen-Zimmermann, *Irreducible components of varieties of representations I. The local case*, arXiv:1410.3166v1, first public 2014-10-12, especially the introductory geometric-component framework. https://arxiv.org/pdf/1410.3166
3. K. Morrison, *The scheme of finite-dimensional representations of an algebra*, Pacific Journal of Mathematics **91** (1980), 199–218, especially the tangent-space formalism and the radical-square-zero example; this is background rather than the dated research seed.
