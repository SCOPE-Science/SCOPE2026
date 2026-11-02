# One commuting graph across quadratic cyclic division and matrix algebras over finite fields

## Finding
Let \(q\ge2\) be any prime power, \(F=\mathbb F_q\), \(K=\mathbb F_{q^2}\), and \(\sigma(x)=x^q\). For every \(a\in K^\times\), form the four-dimensional \(F\)-algebra \(S_a=K\oplus Kt\), with multiplication
\[
(u+vt)(x+yt)=(ux+a v\sigma(y))+(uy+v\sigma(x))t.
\]
For \(a\in F^\times\), the algebra is associative and isomorphic to \(M_2(F)\). For \(a\in K\setminus F\), it is a proper nonassociative division algebra. **Nevertheless the commuting graph on noncentral elements is independent of \(a\)** and is
\[
\Gamma(S_a)\cong \bigsqcup_{j=1}^{q^2+q+1} K_{q^2-q}.
\]
Here adjacent distinct elements commute under the displayed multiplication, and central means commuting with every element, not membership in all associativity nuclei. The commuting probability for independent uniform elements is exactly
\[
\Pr(XY=YX)=\frac{q^6+q^5-q^3}{q^8}=q^{-2}+q^{-3}-q^{-5}.
\]
For each noncentral \(z\), its *elementwise commutant* is the two-dimensional \(F\)-linear space \(C(z)=F+Fz\), of cardinality \(q^2\). For every proper algebra \(a\notin F\), the commutant of each \(z=u+vt\) with \(v\ne0\) is **not a subalgebra**, despite being a clique in the commuting graph. In contrast, every element commutant in the associative split-matrix algebra is a subalgebra. Thus a proper nonassociative division algebra and a matrix ring have identical commuting graphs although their centralizer-closure behavior distinguishes them.

## Assumptions and scope
The parameter \(q\) ranges over all prime powers, including even characteristic; \(K/F\) is the unique quadratic finite-field extension, and \(a\) is any nonzero element of \(K\). The multiplication is the Petit right-remainder multiplication for the skew polynomial \(t^2-a\); no associativity is assumed. We use the graph on \(S_a\setminus Z_c(S_a)\), where \(Z_c(S_a)=\{x:xy=yx\text{ for all }y\in S_a\}\). This 'commutative center' is not an assertion about associativity nuclei. A commutant \(C(z)\) is defined solely by pairwise commutation.

## Proof
Put \(z=u+vt\) and \(w=x+yt\). Direct subtraction using the displayed multiplication gives
\[
zw-wz=a\bigl(v\sigma(y)-y\sigma(v)\bigr)+\bigl(y(u-\sigma(u))+v(\sigma(x)-x)\bigr)t.\tag{1}
\]
If \(v=0\) and \(u\in F\), (1) vanishes for all \(w\). Conversely, if \(v=0\) and \(u\notin F\), (1) vanishes precisely when \(y=0\), so \(C(z)=K=F+Fz\), because \(1,u\) form a basis of \(K/F\) as an \(F\)-vector space.

If \(v\ne0\), since \(a\ne0\), the scalar component in (1) vanishes exactly when \(\sigma(y/v)=y/v\), equivalently \(y=cv\) for some \(c\in F\). Substitution into the \(t\)-component yields \(\sigma(x-cu)=x-cu\), hence \(x=cu+f\) with \(f\in F\). Consequently
\[
C(u+vt)=\{f+c(u+vt):f,c\in F\}=F+F(u+vt).
\]
This proves that the commutative center is precisely \(F\), and each noncentral commutant has \(q^2\) elements. Two noncentral elements commute if and only if they determine the same one-dimensional line modulo \(F\): if \(w\in C(z)\setminus F\), then \(F+Fw=F+Fz\); the converse is immediate. The quotient \(S_a/F\) has dimension three over \(F\), with \((q^3-1)/(q-1)=q^2+q+1\) lines. Each line lifts to \(q(q-1)=q^2-q\) noncentral elements. This proves the disjoint-clique graph formula.

There are \(q\) central elements and \(q^4-q\) noncentral elements. Summing all centralizer sizes therefore gives the number of ordered commuting pairs
\[
q\cdot q^4+(q^4-q)q^2=q^6+q^5-q^3,
\]
which proves the probability formula.

For \(a\in F^\times\), the norm map \(N_{K/F}:K^\times\to F^\times\) is surjective. Choose \(b\in K^\times\) with \(b\sigma(b)=a\). The linear endomorphisms on \(K\) given by left multiplication by elements of \(K\) and \(t:z\mapsto b\sigma(z)\) satisfy \(t^2=a\) and \(tx=\sigma(x)t\). They give an injective map of \(S_a\) into \(\operatorname{End}_F(K)\), both of dimension four, hence an algebra isomorphism \(S_a\cong M_2(F)\).

For \(a\notin F\), associativity fails since \((tt)t=at\) but \(t(tt)=\sigma(a)t\); moreover, the standard degree-two skew-polynomial irreducibility criterion (Nevins–Pumplün, Theorem 2.1) applies: \(a\notin N_{K/F}(K)\subset F\), so \(S_a\) is a division algebra (no nonzero zero divisors). For any \(z=u+vt\) with \(v\ne0\), expansion gives
\[
z^2=\operatorname{Tr}_{K/F}(u)z+\bigl(aN_{K/F}(v)-N_{K/F}(u)\bigr).
\]
The final scalar lies in \(K\setminus F\), because \(N(v)\in F^\times\) and \(a\notin F\). If \(z^2\) belonged to \(F+Fz\), subtracting the displayed trace multiple would force this scalar into \((F+Fz)\cap K=F\), a contradiction. Hence \(C(z)\) is not multiplication-closed. In an associative algebra the commutant of an element is always a subalgebra, proving the contrast.

## Verification
The accompanying standalone Python checker implements arithmetic in \(\mathbb F_{q^2}\), builds all algebra elements, and independently evaluates every ordered product and all elementwise commutants for \(q=2,3,4,5\). In each field it checks one parameter \(a\in F^\times\) and one parameter \(a\in K\setminus F\), including characteristic two and an extension base field \(\mathbb F_4\). It verifies each commutant against the proposed \(F+Fz\) set, its size, the center, total commuting-pair count and failure of multiplicative closure in the proper case. It reports `VERIFY_OK`. These finite computations corroborate, and do not replace, the proof valid for every prime power.

## Relationship to prior work
Nevins and Pumplün, *A parametrization of nonassociative Petit algebras* (arXiv:2610.30921v1, public 22 October 2026), §2.1–2.4, establish the skew-quotient framework, degree-two irreducibility, and isomorphism/parameter questions. The abstract, introductory reduction, defining formulas, division criterion, and isomorphism sections were examined. They do not calculate the elementwise commuting relation, its graph, its probability, or closure of commutants. Commuting graphs and graph spectra of **associative** finite rings are studied by Fasfous, Nath, and Sharafdini (2020), a distinct category. The matrix-algebra clique structure is elementary; neither that fact nor the division-algebra construction alone implies the simultaneous graph-invariance and failure-of-closure result. Nearby indexed mathematical claims on Nagy–Zhou presemifields or Kronecker path algebras concern other multiplications and do not entail the formula here. Historical completeness cannot be certified: an earlier specialized result on finite semifield commutants might imply part of the theorem.

## Limitations
This result concerns quadratic cyclic Petit algebras with nonzero parameter and does not assert such invariance for higher-degree extensions, the zero-parameter algebra, or arbitrary nonassociative semifields. It does not classify all isomorphisms; different algebras sharing a commuting graph need not be isomorphic or isotopic. The finite checker is not a universal certificate or independent mathematical audit.

## References
1. Monica Nevins and Susanne Pumplün, *A parametrization of nonassociative Petit algebras* (2026), arXiv:2610.30921v1, §§1–2, Theorem 2.1.
2. W. N. T. Fasfous, R. K. Nath and R. Sharafdini, *Various spectra and energies of commuting graphs of finite rings*, Hacettepe J. Math. Stat. 49 (2020), 1915–1925, DOI:10.15672/hujms.540309.
