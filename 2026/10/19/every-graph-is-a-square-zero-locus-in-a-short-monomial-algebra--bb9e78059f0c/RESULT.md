# Every graph is a square-zero locus in a short monomial algebra

## Finding

For every finite simple graph \(G=([n],E)\), every field \(k\), and \(m=|E|\), there is an explicitly presented \((1+n+m)\)-dimensional associative local monomial \(k\)-algebra \(A_G\) with radical \(J\) satisfying \(J^3=0\), such that the **scheme of square-zero elements in the radical** has an isomorphism
\[
Z_G:=\{a\in J:a^2=0\}\;\cong\;
\mathbb A_k^m\times\operatorname{Spec}\frac{k[t_1,\ldots,t_n]}{(t_it_j:\{i,j\}\in E)}.
\]
This isomorphism holds in every characteristic and the displayed scheme is reduced. The reduced scheme underlying square-zero elements of the *whole* algebra is also \(Z_G\).

Consequently, if \(I_G(u)=\sum_{S\subseteq[n],\ S\text{ independent}}u^{|S|}\) is the independence polynomial, then
\[
[Z_G]=\mathbb L^m I_G(\mathbb L-1),\qquad
|Z_G(\mathbb F_q)|=q^m I_G(q-1)
\]
for every finite field \(\mathbb F_q\), where \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring of varieties. Its graded affine coordinate ring has Hilbert series
\[
H_{Z_G}(t)=\frac{1}{(1-t)^m}I_G\!\left(\frac{t}{1-t}\right),
\]
using degree one for all coordinates. Its irreducible components are precisely the coordinate linear subspaces indexed by maximal independent sets \(S\); their dimensions are \(m+|S|\). Thus \(\dim Z_G=m+\alpha(G)\), with \(\alpha(G)\) the independence number.

As a computational consequence, exact counting of square-zero elements is \(\#\mathrm P\)-hard under polynomial-time Turing reductions even for finite-dimensional local monomial algebras over \(\mathbb F_2\) with cube-zero radical. The classification and complexity assertion are consequences of this one universal realization, not separate conjectures.

The noncommutativity of this construction is essential in characteristic two: over any algebraically closed field of characteristic two, the reduced square-zero locus of a finite-dimensional **commutative** associative algebra is a linear subspace. In contrast, if the graph has an edge, the displayed radical square-zero scheme has at least two irreducible components.

## Assumptions and scope

Choose and retain an ordering \(1<\cdots<n\) of the vertices of \(G\). Set \(A_G\) to be the \(k\)-vector space with basis
\[
1,\quad x_1,\ldots,x_n,\quad z_{ij}\quad (\{i,j\}\in E,\ i<j).
\]
Declare \(1\) a two-sided identity. Among products of nonunit basis vectors, set \(x_ix_j=z_{ij}\) for ordered edges \(i<j\), and set *all other* such products to zero (including all products containing a \(z_{ij}\)). This is the associative monomial quotient of the free unital algebra in \(x_1,\ldots,x_n\) obtained by killing all words of length at least three and all length-two words except \(x_ix_j\) for an edge with \(i<j\). These choices do not assert orientation-independent algebra isomorphism; the conclusions about \(Z_G\) depend only on the underlying graph.

The algebra is allowed to be noncommutative, and no characteristic restriction is imposed. The square-zero scheme in \(J\) is defined by the coefficient equations of \(a^2=0\), rather than by merely counting rational points. For \(m=0\) the radical has square zero and all formulas still apply.

## Proof

**Associativity and locality.** Any triple product involving three nonunit basis vectors vanishes, regardless of bracketing. Products involving the identity have the required identity law. Therefore multiplication is associative. The subspace \(J=\langle x_i,z_{ij}\rangle\) is a two-sided ideal with \(J^2=\langle z_{ij}\rangle\) and \(J^3=0\). Because \(A_G/J\cong k\) is a field and \(J\) is nilpotent, \(J\) is exactly the Jacobson radical and \(A_G\) is local.

**Exact equations.** Write an arbitrary radical element uniquely as
\[
a=\sum_{i=1}^n c_i x_i+\sum_{\{i,j\}\in E,\,i<j}d_{ij}z_{ij}.
\]
Then by the multiplication table,
\[
a^2=\sum_{\{i,j\}\in E,\,i<j}c_ic_jz_{ij}.
\]
The \(z_{ij}\) are linearly independent. Thus the polynomial ideal of equations is exactly \((c_ic_j:\{i,j\}\in E)\), with each \(d_{ij}\) arbitrary. This proves the displayed scheme isomorphism, even in characteristic two. The edge ideal is radical: a monomial belongs to it precisely when its support contains both ends of some edge; taking any positive power does not change this support condition. Hence the radical square-zero scheme is reduced.

To compare with the full algebra, write \(b=\lambda 1+a\), with \(a\in J\). The scalar coordinate of \(b^2\) is \(\lambda^2\), so the full square-zero ideal contains \(\lambda^2\). Its radical contains \(\lambda\), and reducing modulo \(\lambda\) leaves exactly the radical edge ideal above. Therefore the reduction of the full square-zero scheme is \(Z_G\); the unreduced full scheme is not claimed to be reduced.

**Why characteristic two requires noncommutativity.** Let \(K\) be an algebraically closed field of characteristic two and let \(B\) be any finite-dimensional commutative associative \(K\)-algebra, with basis \(e_1,\ldots,e_N\). For \(b=\sum_i t_i e_i\), commutativity implies \(b^2=\sum_i t_i^2 e_i^2\). In each basis coordinate, the defining quadratic equation is \(\sum_i a_i t_i^2=0\). Each \(a_i\) is a square in \(K\); consequently this polynomial is the square of the linear form \(\sum_i \sqrt{a_i}t_i\). Taking the radical of the square-zero equation ideal therefore yields an ideal generated by linear forms; the reduced locus is a vector subspace. If \(G\) contains an edge \(\{i,j\}\), there exist maximal independent sets extending \(\{i\}\) and \(\{j\}\), respectively, which must be distinct. Thus the radical square-zero scheme constructed for \(G\) is reducible and cannot equal the reduced square-zero locus of a commutative algebra over \(K\). This is a boundary statement concerning reduced square-zero geometry, not a classification of commutative algebra structures.

**Components and enumerators.** Set \(I(E)=(c_ic_j:\{i,j\}\in E)\). The minimal primes of this squarefree monomial ideal are \((c_i:i\notin S)\) with \(S\) a maximal independent set. Indeed, any point satisfying all edge equations has support an independent set and hence belongs to the coordinate subspace of a maximal independent set. Distinct maximal independent sets give incomparable coordinate primes; each subspace has dimension \(m+|S|\).

For a finite field, stratify according to the exact support \(S=\{i:c_i\ne0\}\). This support can be any independent set. On the stratum for \(S\), there are \((q-1)^{|S|}\) choices of the \(c_i\)'s and \(q^m\) independent choices of \(d_{ij}\). This proves the finite-field formula. The same disjoint locally-closed support stratification has class \(\mathbb L^m(\mathbb L-1)^{|S|}\), proving the Grothendieck-class formula. Finally, coordinate monomials whose support is exactly an independent \(S\) contribute \((t/(1-t))^{|S|}\) to the graded Hilbert series, and the \(m\) free coordinates contribute \((1-t)^{-m}\).

**Counting complexity.** Constructing the multiplication table of \(A_G\) from \(G\) requires polynomial time, with dimension \(1+n+m\). Over \(\mathbb F_2\), the formula becomes \(|Z_G(\mathbb F_2)|=2^m I_G(1)\). Thus an oracle for counting square-zero elements of such algebras yields the number of independent vertex sets of any input graph by one oracle call followed by exact division by \(2^m\). Counting independent sets is \(\#\mathrm P\)-hard (already for bipartite graphs, via counting vertex covers); this proves the asserted polynomial-time Turing hardness. Square-zero verification for an explicitly given element is polynomial in the table size, but no parsimonious reduction or stronger hardness notion is claimed.

## Verification

The self-contained standard-library checker `verify.py` constructs the basis multiplication table, checks associativity on every ordered basis triple, directly enumerates all elements over prime fields, and compares the square-zero counts against independently enumerated independent-set supports. It verifies **every graph with at most four labeled vertices over \(\mathbb F_2\)** (76 graph instances) and six further graph instances over \(\mathbb F_3\), for 82 tested graph/field instances. It also checks the two maximal independent-set sizes for the path on three vertices. Running `python3 verify.py` emits `VERIFY_OK graph_instances 82 P3_components [1, 2]`. These finite tests corroborate but do not replace the all-graphs proof.

For the path \(1-2-3\), the independence polynomial is \(1+3u+u^2\) and \(m=2\). The two irreducible components have dimensions three and four; the rational-point count is \(q^2(q^2+q-1)\), giving 20 at \(q=2\) and 99 at \(q=3\).

## Relationship to prior work

The monomial-basis perspective is classical; Bell and Pekcagliyan study finitely presented *prime* monomial algebras and primitivity (arXiv:0712.0815v1), whereas these examples are nonprime local algebras with cube-zero radical. Morey and Villarreal survey graph edge ideals, their independent-set Stanley–Reisner complexes, and their commutative-algebra invariants (arXiv:1012.5329); that prior theory supplies the component and Hilbert-series interpretation **once** the edge ideal arises, but does not itself identify edge ideals as radical square-zero equations of the displayed local associative algebras. Chudnovsky and Seymour study independence polynomials and their roots, not algebra-element square-zero loci. Rickard's two-generator example of a local algebra detected by its square-zero elements illustrates a small special case of coefficient-product equations, but does not provide arbitrary-graph realization. These established ingredients are not claimed as independently new.

The contribution assessed here is the characteristic-uniform realization linking arbitrary finite graphs to square-zero schemes of short monomial associative algebras, together with its uniform component, enumerative, and complexity consequences. The relevant previous two-generator observations and the classical edge-ideal results are explicitly included in the comparison rather than relabeled as new.

## Limitations

The construction gives labeled algebra elements, not conjugacy classes, algebra isomorphism types, or a classification of all short local algebras. The orientation chosen to define \(A_G\) need not produce isomorphic algebras for different choices. The reduction of the full-algebra square-zero scheme is identified; the full scheme may be nonreduced. The counting hardness is under polynomial-time Turing reductions only. No claim is made that the conceptual bridge has absolute priority over all unlocated literature. Independent external validation has not been performed.

## References

1. J. P. Bell and P. Pekcagliyan, *Primitivity of finitely presented monomial algebras*, arXiv:0712.0815v1 (publicly posted 2007-12-05), especially Section 1 and Theorem 1.2. https://arxiv.org/html/0712.0815v1
2. S. Morey and R. H. Villarreal, *Edge ideals: algebraic and combinatorial properties*, arXiv:1012.5329 (initial posting 2010-12-24), especially Sections 1–2. https://arxiv.org/html/1012.5329v3
3. M. Chudnovsky and P. Seymour, *The Roots of the Independence Polynomial of a Clawfree Graph*, preprint marked 2004, revised 2006, especially Section 1. https://web.math.princeton.edu/~mchudnov/roots.pdf
4. J. Rickard, answer on small associative algebras and their square-zero elements, MathOverflow question 171995, 2014-06-17. https://mathoverflow.net/questions/171995/
5. J. S. Provan and M. O. Ball, *The Complexity of Counting Cuts and of Computing the Probability that a Graph is Connected*, SIAM J. Comput. **12** (1983), 777–788; #P-completeness of counting vertex covers in bipartite graphs. https://doi.org/10.1137/0212053
