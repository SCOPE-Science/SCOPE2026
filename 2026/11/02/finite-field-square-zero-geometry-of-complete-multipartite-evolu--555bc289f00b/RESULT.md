# Finite-field square-zero geometry of complete multipartite evolution algebras

## Finding
Let \(q\) be an odd prime power of characteristic \(p\), and let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph, with \(r\ge2\), every \(n_i\ge1\), and \(N=\sum_i n_i\). Let \(E_G\) be the evolution algebra with natural basis indexed by vertices, mixed products zero, and each basis square the sum of its graph-neighbors. Write \(X_G=\{x\in E_G:x^2=0\}\), and take the reduced structure when speaking of its algebraic variety.

Define \(a_i=q^{n_i-1}\). If \(n_i\) is even, put \(b_i=\chi((-1)^{n_i/2})q^{(n_i-2)/2}\); if \(n_i\) is odd, put \(c_i=\chi((-1)^{(n_i-1)/2})q^{(n_i-1)/2}\). Here \(\chi\) is the quadratic character on \(\mathbb F_q^\times\), and empty products are one. Set
\[
Z_0=\prod_{n_i\ \mathrm{even}}(a_i+(q-1)b_i)\prod_{n_i\ \mathrm{odd}}a_i.
\]
Then the complete square-zero point count is
\[
\#X_G(\mathbb F_q)=\begin{cases}
Z_0,&p\nmid(r-1),\\[3pt]
Z_0+\dfrac{q-1}{2}\left(\prod_{n_i\ \mathrm{even}}(a_i-b_i)\right)
\left[\prod_{n_i\ \mathrm{odd}}(a_i+c_i)+\prod_{n_i\ \mathrm{odd}}(a_i-c_i)\right],&p\mid(r-1).
\end{cases}
\]

When \(p\nmid(r-1)\), the reduced variety \(X_G\) is the product of the cones \(\sum_{j=1}^{n_i}x_{ij}^2=0\). It is equidimensional of dimension \(N-r\), and has exactly \(2^b\) geometric irreducible components, where \(b=\#\{i:n_i=2\}\). Its number of irreducible components over \(\mathbb F_q\) is \(2^b\) if \(\chi(-1)=1\) or \(b=0\), and \(2^{b-1}\) otherwise. The dimension of the \(\mathbb F_q\)-linear span of its rational points is
\[
\dim_{\mathbb F_q}\langle X_G(\mathbb F_q)\rangle
=\sum_{n_i\ge3}n_i+2b\,\mathbf1_{\chi(-1)=1}.
\]
When \(p\mid(r-1)\), the scheme of square-zero elements is a geometrically reduced equidimensional complete intersection of dimension \(N-r+1\), and its rational points linearly span all of \(E_G\). In particular, for \(G=K_{p+1}\) the square-zero locus is a union of \(2^p\) rational lines through zero and has \(1+2^p(q-1)\) rational points.

## Assumptions and scope
The base field is a finite field \(\mathbb F_q\) of **odd** characteristic. Graphs are nonempty complete multipartite simple graphs, with at least two nonempty parts; the displayed formulas include singleton parts and all extension fields. The algebra multiplication is nonassociative and commutative; \(x^2\) is one application of the algebra product, **not** an iteration of the evolution operator. Geometry refers to algebraic varieties over the indicated field or its algebraic closure, with reduced structure in the nonresonant case. The assertion about the scheme itself being reduced is made only in the resonant case.

## Proof
**1. Reduction to a scalar coupling.** For a vector \(x=(x_{ij})\), put \(Q_i(x)=\sum_{j=1}^{n_i}x_{ij}^2\), and \(S=\sum_iQ_i\). For every vertex in part \(i\), the coefficient of \(x^2\) is \(S-Q_i\). Hence \(x^2=0\) if and only if all \(Q_i=S\). Summing gives \((r-1)S=0\). If \(p\nmid(r-1)\), this means \(Q_i=0\) for all \(i\); if \(p\mid(r-1)\), this means precisely \(Q_1=\cdots=Q_r=t\), with unrestricted \(t\in\mathbb F_q\).

**2. The individual quadratic-fiber counts.** For any odd finite field, let \(T_n(t)=\#\{y\in\mathbb F_q^n:\sum y_j^2=t\}\). The classical diagonal-quadratic Gauss-sum computation gives, for \(n=2m\),
\[
T_{2m}(0)=q^{2m-1}+(q-1)\chi((-1)^m)q^{m-1},\qquad
T_{2m}(t)=q^{2m-1}-\chi((-1)^m)q^{m-1}\quad(t\ne0),
\]
and, for \(n=2m+1\),
\[
T_{2m+1}(0)=q^{2m},\qquad
T_{2m+1}(t)=q^{2m}+\chi((-1)^m)q^m\chi(t)\quad(t\ne0).
\]
For completeness, if \(\psi\) is a nontrivial additive character and \(g=\sum_{u\in\mathbb F_q}\psi(u^2)\), then additive-character orthogonality and \(\sum_{u\in\mathbb F_q}\psi(su^2)=\chi(s)g\) for \(s\ne0\) yield \(qT_n(t)=q^n+g^n\sum_{s\ne0}\chi(s)^n\psi(-st)\). The standard identity \(g^2=\chi(-1)q\), together with the quadratic-character sum, yields the displayed formulas, also for \(n=1\). The first case therefore contributes \(Z_0=\prod_iT_{n_i}(0)\). In the second case, the nonzero values of \(t\) split evenly into \((q-1)/2\) squares and nonsquares, giving the second summand and proving the count.

**3. Geometry away from resonance.** Over an algebraic closure of odd characteristic, a nonsingular sum-of-squares quadratic cone in one variable has reduced support a point, in two variables factors into two distinct lines, and in \(n\ge3\) variables is irreducible of dimension \(n-1\). Products of the resulting geometrically irreducible factors are geometrically irreducible. Each factor choice at the \(b\) two-dimensional parts therefore yields one component, of dimension \(N-r\). If \(\chi(-1)=1\), both lines of each binary factor descend individually to \(\mathbb F_q\); if \(\chi(-1)=-1\), Frobenius exchanges the two lines simultaneously in every two-dimensional part. With \(b>0\), its orbits on the \(2^b\) geometric components have size two. This proves both geometric and rational component numbers.

**4. Spans away from resonance.** A one-variable sum-of-squares zero cone has only zero. A two-variable cone has nonzero rational vectors precisely when \(-1\) is a square, and then its two distinct lines span the entire plane. A nondegenerate quadratic form in at least three variables is isotropic over a finite field of odd order. Its isotropic vectors span the entire underlying vector space: choose a hyperbolic pair \(u,v\) with \(Q(u)=Q(v)=0\) and polarization \(B_Q(u,v)=1\); for each \(w\in\langle u,v\rangle^\perp\), the vector \(w+u-Q(w)v\) is isotropic, so every \(w\) lies in the span of isotropic vectors. Varying one block while keeping all other blocks zero gives the direct-sum span formula.

**5. Geometry and spans at resonance.** Work first over an algebraic closure \(k\). The equations are \(Q_i=Q_r\) for \(1\le i<r\). Write \(t\) for their common value. Each ring \(k[x_{i1},\ldots,x_{in_i}]\), viewed as a module over \(k[t]\) via \(t\mapsto Q_i\), is torsion-free and therefore flat. Their tensor product over \(k[t]\) is flat, and its fibers are products of nonempty quadratic hypersurfaces, every fiber having pure dimension \(N-r\). Thus the total space has dimension \(N-r+1\), and its defining \(r-1\) equations have the expected codimension: it is a complete intersection. Over \(t\ne0\), each quadratic fiber is smooth (its gradient \(2x_i\) cannot vanish), so the total space is generically reduced. Flatness excludes components supported at \(t=0\); the complete intersection is Cohen–Macaulay and hence reduced by generic reducedness. All components have the same dimension. For the rational span, fix a block \(i\) and basis coordinate \(j\); the two points with coordinates \(+1\) and \(-1\), respectively, at \((i,j)\), and a single coordinate equal to \(1\) in every other part, both have every \(Q_l=1\). Their difference is \(2e_{ij}\), so every basis vector lies in the span. Finally, with every part a singleton and \(r=p+1\), all coordinates have equal square, so each vector is \(u(1,\pm1,\ldots,\pm1)\); its distinct sign choices produce \(2^p\) rational lines through the origin.

## Verification
Run the dependency-free Python 3 program `check_multipartite.py`. It enumerates all vectors in twenty-one finite-field examples; computes the algebra square from the actual complete-multipartite adjacency condition; checks the closed formulas; and independently Gaussian-eliminates the span of every rational square-zero locus. Tested fields include \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_9\) (with genuine extension-field arithmetic), and \(\mathbb F_{11}\). The checked examples include both characteristic-resonant and nonresonant parameters. The printed marker is `MULTIPARTITE_EVOLUTION_ABSOLUTE_NILPOTENTS_OK 21`. Finite enumeration corroborates, but does not prove, the all-parameter formulas or component claims.

## Relationship to prior work
The natural-basis evolution algebra and graph correspondence are classical; see Camacho–Gómez–Omirov–Turdibaev (2010), Elduque–Labra (2013), and Cabrera Casado–Siles Molina–Velasco (2016). Khudoyberdiyev–Omirov–Qaralleh, *Few remarks on evolution algebras* (arXiv:1307.0993v1, Proposition 4.1), proves a **qualitative** existence criterion over \(\mathbb C\) and describes absolute nilpotents in other families. Neither its statement nor its proof determines the finite-field point numbers, the characteristic-resonant dimension jump, rational/geometric component counts, or the spans of finite-field square-zero points in complete multipartite graphical algebras. The Gauss-sum formulas and properties of quadratic cones used above are classical, not presented as new. This is an explicit specialized synthesis, not an assertion that the underlying quadratic-form facts are novel. Publication-priority uncertainty remains for less accessible graph-evolution or quadratic-arrangement literature.

## Limitations
Only finite fields of odd characteristic and complete multipartite simple graphs are treated. The geometric description in the nonresonant case concerns the reduced locus; for singleton parts the scheme defined by square-zero equations can be nonreduced. Individual irreducible components in the resonant case are not classified, although the complete-intersection structure, dimension, point counts, and span are determined. This result does not address idempotents, higher power nilpotents, or dynamics of iterated squaring. The mathematical review is not an independent audit.

## References
1. A. Kh. Khudoyberdiyev, B. A. Omirov, I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993v1 (2013-07-03), especially Definition 2.3 and Proposition 4.1. https://arxiv.org/abs/1307.0993
2. L. M. Camacho, J. R. Gómez, B. A. Omirov, R. M. Turdibaev, *Some properties of evolution algebras*, arXiv:1004.1987v1 (2010-04-12). https://arxiv.org/abs/1004.1987
3. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (2013-12-17), especially Sections 2–4. https://arxiv.org/abs/1312.4685
4. Y. Cabrera Casado, M. Siles Molina, M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832v1 (2016-01-08), Sections 2–4. https://arxiv.org/abs/1601.01832
5. Classical finite-field quadratic-form count: additive-character orthogonality, one-dimensional Gauss sums, and \(g^2=\chi(-1)q\), as explicitly used in the proof above.
