# Exact edge-triangle profile of finite-field total dot product graphs

## Finding

Let \(q\) be a prime power, let \(n\ge3\), and write \(V=\mathbb F_q^n\). The total dot product graph \(TD(\mathbb F_q,n)\) has vertex set \(V\setminus\{0\}\), with distinct vertices adjacent exactly when their standard dot product is zero.

For an edge \(xy\), set
\[
r=\dim\langle x,y\rangle\in\{1,2\},
\qquad
\varepsilon(v)=\begin{cases}1,&v\cdot v=0,\\0,&v\cdot v\ne0.\end{cases}
\]
Then
\[
|N(x)\cap N(y)|=q^{\,n-r}-1-\varepsilon(x)-\varepsilon(y).
\]
Consequently an independent adjacent pair has \(q^{n-2}-1\), \(q^{n-2}-2\), or \(q^{n-2}-3\) common neighbors according as zero, one, or two endpoints are isotropic. A dependent edge consists of distinct scalar multiples of an isotropic vector and has \(q^{n-1}-3\) common neighbors.

This gives two sharp structural consequences. First, for every \(n\ge3\), edge triangle multiplicity is not constant: there are adjacent anisotropic-anisotropic pairs with \(q^{n-2}-1\) common neighbors and adjacent isotropic-anisotropic pairs with \(q^{n-2}-2\). Second, every edge lies in a triangle except exactly six edges of \(TD(\mathbb F_2,3)\), namely its isotropic-anisotropic edges.

In dimension three there are no independent orthogonal isotropic pairs. The three edge classes therefore have sizes
\[
E_{AA}=\frac{q(q-1)^2(q^2-1)}2,
\qquad
E_{IA}=q(q-1)(q^2-1),
\qquad
E_{II}^{\mathrm{dep}}=\frac{(q^2-1)(q-2)}2,
\]
and respective common-neighbor counts \(q-1\), \(q-2\), and \(q^2-3\). Hence
\[
\#\{\text{triangles in }TD(\mathbb F_q,3)\}
=
\frac{(q-1)(q+1)(q^2-3)(q^2-2)}6.
\]

## Assumptions and scope

The coefficient ring is a finite field \(\mathbb F_q\), and the bilinear form is the standard nondegenerate symmetric form
\[
B(x,y)=x\cdot y=\sum_{i=1}^n x_i y_i.
\]
A nonzero vector is called isotropic when \(B(v,v)=0\). Common neighbors are graph vertices distinct from both endpoints. The theorem concerns \(n\ge3\); dimension two has a separate component decomposition depending on isotropy and is not included in the all-dimensional boundary statement.

The phrase “edge triangle multiplicity” means the number of triangles containing a fixed edge, equivalently the number of common neighbors of its endpoints. No assertion about a graph-theoretic convention for “edge-regular” is needed.

## Proof

Let \(x\) and \(y\) be adjacent distinct nonzero vectors and set \(W=\langle x,y\rangle\). A vector \(z\) is adjacent to both endpoints exactly when
\[
B(z,x)=B(z,y)=0,
\]
so before excluding forbidden vertices the common-neighbor candidates are the nonzero vectors of \(W^\perp\). Since \(B\) is nondegenerate,
\[
\dim W^\perp=n-\dim W=n-r,
\]
and therefore \(W^\perp\setminus\{0\}\) contains \(q^{n-r}-1\) vectors.

Because \(B(x,y)=0\), the endpoint \(x\) belongs to \(W^\perp\) exactly when \(B(x,x)=0\); similarly for \(y\). Common neighbors must be distinct from the endpoints, so deleting exactly those isotropic endpoints gives
\[
|N(x)\cap N(y)|=q^{n-r}-1-\varepsilon(x)-\varepsilon(y).
\]
This proves the local formula. If \(r=1\), then \(y=cx\) for some \(c\in\mathbb F_q^\times\setminus\{1\}\), and adjacency gives \(cB(x,x)=0\), so both endpoints are isotropic and the value becomes \(q^{n-1}-3\). If \(r=2\), the three displayed independent-pair values follow immediately.

There is always an anisotropic-anisotropic edge: the standard basis vectors \(e_1\) and \(e_2\) are orthogonal and satisfy \(B(e_i,e_i)=1\). There is also an isotropic-anisotropic edge. In characteristic two, take \(x=e_1+e_2\) and \(y=e_3\). In odd characteristic, a nondegenerate quadratic form in at least three variables over a finite field has a nonzero isotropic vector \(x\). The hyperplane \(x^\perp\) cannot consist entirely of isotropic vectors: otherwise polarization would make \(B\) vanish identically on \(x^\perp\), forcing \(x^\perp\subseteq(x^\perp)^\perp=\langle x\rangle\), impossible because \(\dim x^\perp=n-1\ge2\). Hence some \(y\in x^\perp\) is anisotropic. These two edge types differ by one common neighbor, so edge triangle multiplicity is never constant.

For the triangle-coverage boundary, a dependent edge can occur only when \(q>2\), and then \(q^{n-1}-3>0\). For an independent edge in dimension at least four, even the smallest possible value satisfies
\[
q^{n-2}-3\ge2^2-3=1.
\]
It remains to consider \(n=3\). Independent orthogonal isotropic vectors cannot exist: if \(x,y\) were such a pair, then the two-dimensional space \(\langle x,y\rangle\) would satisfy \(B|_{\langle x,y\rangle}=0\), so it would lie in its one-dimensional orthogonal complement, contradicting nondegeneracy. Thus the independent edge types in dimension three are only anisotropic-anisotropic and isotropic-anisotropic, with \(q-1\) and \(q-2\) common neighbors. These are positive when \(q>2\). When \(q=2\), dependent edges do not exist and the isotropic-anisotropic edges have zero common neighbors. There are \(q^2-1=3\) nonzero isotropic vectors in \(\mathbb F_2^3\), and each has \(q^2-q=2\) anisotropic neighbors, giving exactly six such edges.

For the dimension-three enumeration, the number of nonzero isotropic vectors is \(q^2-1\). In characteristic two this is immediate from
\[
B(x,x)=(x_1+x_2+x_3)^2,
\]
whose zero set is a two-dimensional linear hyperplane. In odd characteristic it is the standard count for a nondegenerate ternary quadratic form; equivalently its projective zero locus is a nonsingular conic with \(q+1\) rational points, each representing \(q-1\) nonzero vectors.

An isotropic vertex has degree \(q^2-2\). Its only isotropic neighbors are its \(q-2\) other nonzero scalar multiples, because independent orthogonal isotropic pairs do not exist. Hence it has \(q^2-q\) anisotropic neighbors. It follows that
\[
E_{IA}=(q^2-1)(q^2-q)=q(q-1)(q^2-1).
\]
The \(q+1\) isotropic projective lines each induce a clique on \(q-1\) vectors, so
\[
E_{II}^{\mathrm{dep}}=(q+1)\binom{q-1}{2}=\frac{(q^2-1)(q-2)}2.
\]
There are \(q^3-q^2=q^2(q-1)\) anisotropic vertices, each of degree \(q^2-1\). Summing degrees over anisotropic vertices gives
\[
q^2(q-1)(q^2-1)=2E_{AA}+E_{IA},
\]
which yields
\[
E_{AA}=\frac{q(q-1)^2(q^2-1)}2.
\]
Finally every triangle contributes once to the common-neighbor count of each of its three edges, so
\[
3T=E_{AA}(q-1)+E_{IA}(q-2)+E_{II}^{\mathrm{dep}}(q^2-3).
\]
Substitution and factorization give
\[
T=\frac{(q-1)(q+1)(q^2-3)(q^2-2)}6.
\]

## Verification

The proof is symbolic and applies to every prime power. The accompanying verifier reconstructs the graphs directly for \((q,n)=(2,3),(2,4),(3,3),(3,4),(4,3),(5,3),(7,3)\). It checks every edge against the formula by explicit neighborhood intersection. For dimension three it also checks the three edge-class counts and the triangle formula. The \(q=4\) case is computed in an explicit model of \(\mathbb F_4\), so the tests are not restricted to prime fields.

The verifier returns `VERIFY_OK`. These finite checks are reproducibility tests; they are not used as proof of the general statement.

## Relationship to prior work

Badawi introduced the total dot product graph and proved connectivity, diameter, and girth results. In particular, for dimension at least three the source establishes girth three, which guarantees that some triangle exists, but it does not enumerate common neighbors of an edge or determine which edges lie in triangles.

Mollahajiaghaei subsequently determined finite-field vertex degrees, regularity behavior, graph-isomorphism rigidity, ordinary domination, and several global invariants. The finite-field degree theorem distinguishes isotropic from anisotropic vertices, but vertex degrees alone do not determine intersections of two neighborhoods. Inspection of the full arXiv text found no common-neighbor, triangle-multiplicity, or strongly-regular analysis.

Abdulla and Badawi later gave a detailed component decomposition in the two-dimensional finite-field case, outside the range of the all-dimensional theorem here. Saleh and Megahed studied unit/congruence dot product graphs and domination rather than edge-local triangle multiplicities.

In dimension three, projectivizing the orthogonality relation produces an orthogonal polarity graph, a standard object in finite geometry. That literature is therefore a genuine alias risk for the rank-three quotient. The present statement is not a claim of novelty for polarity graphs themselves: its main content is the exact unprojectivized common-neighbor formula in every dimension, including the scalar-dependent edge class, together with the unique \((q,n)=(2,3)\) edge-triangle defect. The rank-three counts are recorded as an explicit consequence of that formula.

## Limitations

The result uses a field and a nondegenerate standard bilinear form. It does not cover dot product graphs over general finite commutative rings, where orthogonal solution sets need not have dimensions determined only by the span rank.

The rank-three edge enumeration uses the standard count of isotropic vectors for a nondegenerate ternary quadratic form. The verifier checks representative prime and nonprime fields, but finite computation is not a substitute for that general count.

Finite-geometry literature contains many projectivized orthogonality and polarity graphs under different terminology. Searches and direct source inspection did not locate the all-dimensional unprojectivized formula stated here, but terminology mismatch remains the principal residual literature risk.

## References

1. A. Badawi, “On the Dot Product Graph of a Commutative Ring,” *Communications in Algebra* 43 (2015), 43–50. DOI: 10.1080/00927872.2014.897188. Published online 1 August 2014.
2. M. Mollahajiaghaei, “Properties of the Dot Product Graph of a Commutative Ring,” arXiv:1601.05034 (2016).
3. M. Abdulla and A. Badawi, “On the Dot Product Graph of a Commutative Ring II,” *International Electronic Journal of Algebra* 28 (2020), 61–74. DOI: 10.24330/ieja.768135.
4. D. Saleh and N. Megahed, “Dot product graphs and domination number,” *Journal of the Egyptian Mathematical Society* 28 (2020), Article 31. DOI: 10.1186/s42787-020-00092-6.
