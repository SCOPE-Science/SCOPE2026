# Total domination of finite-module intersection graphs has a complete length-and-type classification

## Finding

Let \(R\) be a commutative ring with identity and let \(M\) be a finite \(R\)-module of composition length \(\ell\ge 2\). For the intersection graph \(\Gamma(M)\) whose vertices are the nonzero proper submodules and whose edges join pairs with nonzero intersection, a total dominating set exists exactly when \(\ell\ge3\). When \(\ell\ge3\), if \(M\) is homogeneous semisimple, equivalently \(M\cong (R/\mathfrak m)^\ell\) for a maximal ideal \(\mathfrak m\), then \(\gamma_t(\Gamma(M))=|R/\mathfrak m|+1\); in every other case \(\gamma_t(\Gamma(M))=2\).

Thus total domination differs from the ordinary domination classification in exactly one structural place: nonsemisimple finite modules have ordinary domination number one, while their total domination number is two as soon as the composition length is at least three. Homogeneous semisimple modules retain the finite-field value \(q+1\), and mixed semisimple modules retain the value two.

## Assumptions and scope

The ring \(R\) is commutative with identity, and \(M\) is a finite nonzero \(R\)-module. Write \(\ell=\ell_R(M)\) for its composition length. The graph \(\Gamma(M)\) has as vertices all nonzero proper submodules of \(M\); distinct vertices \(A,B\) are adjacent when \(A\cap B\ne0\). A total dominating set is a set \(D\) of vertices such that every vertex, including every member of \(D\), has a neighbor in \(D\).

The statement begins at \(\ell\ge2\), where \(\Gamma(M)\) is nonempty. For \(\ell=1\), the graph has no vertices and is outside the stated convention.

## Proof

Assume first that \(\ell=2\). If \(M\) is not semisimple, it has a unique simple submodule: two distinct simple submodules would have direct sum of length two and hence equal \(M\). Every nonzero proper submodule has length one, so \(\Gamma(M)\) is a single isolated vertex. If \(M\) is semisimple and its two simple summands are nonisomorphic, those two summands are the only nonzero proper submodules and have zero intersection. If instead \(M\cong S^2\) is homogeneous semisimple, its nonzero proper submodules are the one-dimensional subspaces over the field \(\operatorname{End}_R(S)\), and distinct such subspaces intersect trivially. In every length-two case there is an isolated vertex, so no total dominating set exists.

Now assume \(\ell\ge3\).

If \(M\) is not semisimple, its socle \(\operatorname{Soc}(M)\) is nonzero and proper. Every nonzero submodule of the finite-length module \(M\) contains a simple submodule, hence meets \(\operatorname{Soc}(M)\) nontrivially. Therefore the socle is a universal vertex of \(\Gamma(M)\). There is another nonzero proper submodule: if the socle has length at least two, choose a simple submodule inside it; if the socle is simple, a composition series supplies a length-two proper submodule containing it. Pairing that vertex with the socle gives a total dominating set of size two. Since a total dominating set in a loopless graph cannot have size one,
\[
\gamma_t(\Gamma(M))=2.
\]

Suppose next that \(M\) is semisimple but not homogeneous. Decompose it into nonzero isotypic components
\[
M=C_1\oplus\cdots\oplus C_r,\qquad r\ge2.
\]
Submodules split componentwise because distinct simple isomorphism types have distinct annihilator maximal ideals. If \(r=2\), one component, say \(C_1\), has length at least two. Choose \(0<A<C_1\) and put
\[
D_1=C_1,\qquad D_2=A\oplus C_2.
\]
They are adjacent because their intersection is \(A\). Every nonzero submodule with a nonzero \(C_1\)-component meets \(D_1\); one with zero \(C_1\)-component meets \(D_2\). Thus \(\{D_1,D_2\}\) is a total dominating set. If \(r\ge3\), take
\[
D_1=C_1\oplus\cdots\oplus C_{r-1},\qquad
D_2=C_2\oplus\cdots\oplus C_r.
\]
Their intersection contains \(C_2\), and every nonzero componentwise submodule meets at least one of them. Again \(\gamma_t=2\).

Finally suppose \(M\) is homogeneous semisimple. Then for a maximal ideal \(\mathfrak m\),
\[
M\cong (R/\mathfrak m)^\ell,
\]
so \(M\) is an \(\ell\)-dimensional vector space over the finite field \(F=R/\mathfrak m\), of order \(q=|F|\). The ordinary domination number of its subspace-intersection graph is \(q+1\), so every total dominating set has at least \(q+1\) vertices. Choose a codimension-two subspace \(W\). The \(q+1\) hyperplanes containing \(W\) cover \(M\). Hence every nonzero proper subspace meets one of them. Because \(\ell\ge3\), \(W\ne0\), so any two of these hyperplanes already meet in at least \(W\); consequently each selected hyperplane also has a selected neighbor. They form a total dominating set, proving
\[
\gamma_t(\Gamma(M))=q+1.
\]
This completes all cases.

## Verification

The proof is structural and does not use computation. The accompanying `verify.py` independently enumerates small subspace lattices and mixed examples, constructs the intersection graphs, and exhaustively searches for minimum total dominating sets. It checks the homogeneous cases \(\mathbb F_2^2\), \(\mathbb F_2^3\), \(\mathbb F_2^4\), and \(\mathbb F_3^3\), the uniserial modules \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/8\mathbb Z\), and two mixed semisimple \(\mathbb Z\)-modules. Its exact output is:

```text
VERIFY_OK
F_2^2: subspaces=5, vertices=3, gamma_t=None
F_2^3: subspaces=16, vertices=14, gamma_t=3
F_2^4: subspaces=67, vertices=65, gamma_t=3
F_3^3: subspaces=28, vertices=26, gamma_t=4
Z/4Z: total_domination=undefined (isolated vertex)
Z/8Z: gamma_t=2
C2^2 (+) C3: gamma_t=2
C2 (+) C3 (+) C5: gamma_t=2
```

The finite computations are checks of boundary cases only; the theorem for arbitrary finite \(M\) follows from the socle, isotypic-decomposition, and hyperplane arguments above.

## Relationship to prior work

Jafari and Jafari Rad (2011) define exactly the nonzero-proper-submodule intersection graph used here and classify its ordinary domination number for Artinian modules. They prove that a nonsemisimple Artinian module has ordinary domination number one, quote the \(q+1\) value for finite vector spaces, obtain \(q+1\) for homogeneous finite semisimple modules, and obtain two for semisimple modules with more than one annihilator type. Their article is classified under module theory as well as graph domination.

The preceding vector-space paper of Jafari Rad and Jafari proves the ordinary value \(\gamma(G(V))=q+1\) by covering a finite vector space with the \(q+1\) hyperplanes through a codimension-two subspace. The same hyperplanes become a total dominating set exactly from dimension three onward because their common codimension-two subspace is then nonzero.

Akbari, Tavallaee, and Khalashi Ghezelahmad (2012), and Yaraneri (2012/2013), study the structure and ordinary domination of submodule intersection graphs more broadly. Targeted searches for total domination, total dominating sets, the socle formulation, and the \(q+1\) total-domination formula found no source stating the classification above.

## Limitations

The theorem uses the convention that vertices are nonzero proper submodules. Some later papers use a graph including the zero submodule, which is automatically isolated and therefore cannot have a total dominating set under the standard definition. The result is restricted to finite modules over commutative rings; the same proof suggests cardinal analogues in some finite-length infinite modules, but no such extension is claimed here.

The originality conclusion is limited by bibliographic coverage: no matching result appeared in the targeted database and web searches, but an unindexed source could exist.

## References

1. N. Jafari Rad and S. H. Jafari, “Results on the intersection graphs of subspaces of a vector space,” arXiv:1105.0803, first posted 2011-05-04.
2. S. H. Jafari and N. Jafari Rad, “Domination in the intersection graphs of rings and modules,” *Italian Journal of Pure and Applied Mathematics* 28 (2011), 17–20; published 2011-07-19.
3. S. Akbari, H. A. Tavallaee, and S. Khalashi Ghezelahmad, “Intersection graph of submodules of a module,” *Journal of Algebra and Its Applications* 11 (2012), 1250019. DOI: 10.1142/S0219498811005452.
4. E. Yaraneri, “Intersection graph of a module,” arXiv:1208.1897 (2012); *Journal of Algebra and Its Applications* 12 (2013), 1250218. DOI: 10.1142/S0219498812502180.
