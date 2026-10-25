# Directed-forest topology and affine homology of the seven-vertex quadratic-residue tournament

## Finding
Let \(T_7\) be the tournament on \(\mathbb Z/7\mathbb Z\) with an arc \(u\to v\) exactly when \(v-u\in\{1,2,4\}\pmod 7\). Let \(K=\operatorname{DT}(T_7)\) be the complex of directed forests: its vertices are the \(21\) arcs of \(T_7\), and its faces are sets of arcs having indegree at most one at each original graph vertex and containing no directed cycle.

There is an integral homotopy equivalence
\[
K\simeq\bigvee^{512}S^5.
\]
The affine group \(G=\{u\mapsto au+b:a\in\{1,2,4\},\ b\in\mathbb Z/7\mathbb Z\}\cong C_7\rtimes C_3\) acts by permuting the arcs. The rational \(G\)-character on \(\widetilde H_5(K;\mathbb Q)\) is \((512,1,-1)\) on, respectively, the identity, each nonidentity translation, and each element of order three. More precisely,
\[
\widetilde H_5(K;\mathbb Q)\cong24\mathbf 1\oplus25W_2\oplus73W_6,
\]
where \(W_2\) is the inflated cyclotomic \(\mathbb Q[C_3]\)-module \(\mathbb Q(\zeta_3)\), and \(W_6=\mathbb Q(\zeta_7)\) has \(C_7\) acting by multiplication by seventh roots of unity and \(C_3\) acting through \(\zeta_7\mapsto\zeta_7^2\). Thus the full affine-invariant subspace is \(24\)-dimensional. In particular \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^{512}\), and all other reduced integral homology groups vanish.

## Assumptions and scope
The underlying undirected graph is complete. Each of its \(21\) pairs has just one specified orientation; in particular, this is not the fully bidirected complete graph. A directed forest means a disjoint union of rooted trees with edges directed outward from each root, equivalently an acyclic arc set with indegree at most one at every vertex. Empty-face conventions are standard for a simplicial complex. Equivariant statements concern the stated \(21\)-element affine subgroup and rational, not integral, representation theory.

## Proof
**Exhaustiveness.** Order the arcs lexicographically, and assign each possible incoming arc a bit. For each of the seven potential heads there are four options: no incoming arc or any of its three incoming arcs. The Cartesian product of these options consists of exactly \(4^7=16384\) descriptions and covers *every* arc set having indegree at most one, exactly once. Reject a description if iterating parent pointers from any vertex encounters a repeated vertex before reaching a root. For such a functional digraph this happens exactly when there is a directed cycle. Exhaustive enumeration gives \(10648\) faces including the empty face and the nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(21,189,931,2646,4116,2744).
\]
The \(2744\) spanning directed trees provide an independent count: the incoming-arc Laplacian has any principal root cofactor \(392\), as computed by exact rational elimination in `verify.py`; vertex transitivity gives \(7\cdot392=2744\) trees.

**Acyclic discrete-Morse certificate.** Let \(F\) be the enumerated set of bit-mask faces. Initialize an alive set containing all faces. For arc indices \(i=0,\ldots,20\), in that order, visit the currently alive masks in increasing \((\text{number of set bits},\text{numeric mask})\) order. Whenever both \(\sigma\) and \(\sigma\cup\{i\}\) are alive and \(i\notin\sigma\), pair them and remove both. This deterministically gives \(5068\) pairs on the poset including the empty face. Discard the empty-face pair and treat its formerly paired vertex as critical. The ordinary face poset therefore has \(5067\) pairs and exactly one critical vertex and \(512\) critical five-simplices.

To prove acyclicity, direct every codimension-one face incidence from the larger face to the smaller, except reverse matched incidences. The actual program constructs every such arrow between nonempty simplices and exhaustively topologically sorts the resulting finite directed Hasse graph. It finds \(50799\) incidences and visits all \(10647\) nonempty faces before exhausting the queue, so **no directed cycle exists**. This supplies the required acyclic matching, not merely a proposed matching or a homology computation. By discrete Morse theory, \(K\) is homotopy equivalent to a CW complex with one zero-cell and \(512\) five-cells only. Every five-cell attaches to the zero-skeleton, which is a point, hence that CW complex is \(\bigvee^{512}S^5\).

**Affine character.** For each \(g:u\mapsto au+b\), the action on arcs is \((u,v)\mapsto(au+b,av+b)\). For each \(g\)-fixed face \(\sigma\), compute its signed action on the oriented simplex (the sign of the induced permutation of its arc vertices), multiply by \((-1)^{\dim\sigma}\), and sum over all nonempty faces. Subtract one for the augmented/reduced Lefschetz number. Because reduced homology occurs only in degree five, the resulting character is \(1-\sum_{\sigma\ne\varnothing,g\sigma=\sigma}(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma)\).

For the identity the alternating nonempty-face sum is \(-511\), yielding trace \(512\). A nontrivial translation acts in seven-cycles on arcs, but faces contain at most six arcs, so it fixes no nonempty face; its trace is \(1\). For an order-three affine element, conjugation reduces to \(u\mapsto2u\) or \(u\mapsto4u\). The fixed faces consist of four three-arc faces and two six-arc faces; the sign of the arc permutation is positive on each. Their signed alternating sum is \(4-2=2\), giving trace \(-1\). The complete program checks all \(21\) group elements, not only representatives.

The three rational irreducible character rows on these types are \((1,1,1)\) for \(\mathbf1\), \((2,2,-1)\) for \(W_2\), and \((6,-1,0)\) for \(W_6\). This follows from their concrete cyclotomic constructions: translations have the trace of multiplication by \(\zeta_7^b\) on \(\mathbb Q(\zeta_7)\), namely \(-1\) for \(b\ne0\), and order-three field automorphisms permute two triples of its six monomial basis elements. Rational Maschke semisimplicity and the normal \(C_7\) subgroup show these are the exhaustive irreducible rational types. Solving the three character equations gives multiplicities \(24,25,73\), all nonnegative integers. Only the first type has \(G\)-fixed vectors.

## Verification
The complete executable `verify.py` independently regenerates all directed-forest faces from the incoming-arc choices; reconstructs and topologically checks every Morse arrow; performs an exact Laplacian-minor calculation; and checks oriented simplex traces for all \(21\) affine elements. Its output is:

```
f_vector=21,189,931,2646,4116,2744; total_nonempty=10647
matrix_tree_cofactor=392; spanning_out_trees=2744
morse_pairs=5067; critical=one_0_cell,512_5_cells
nonempty_hasse_incidences=50799; topological_sort=10647
affine_group_order=21; character=(512,1,-1); irreps=(24,25,73)
VERIFY_OK
```

Execute `python3 verify.py` using Python \(3\) with standard-library dependencies only. All integers are recomputed from the explicit graph, not imported from tables.

## Relationship to prior work
Kozlov's original directed-tree-complex framework [1] and his later accessible paper [2] study directed forests, particularly bidirected paths and trees. Engström [3, Section 2] gives the identical directed-forest face convention and shellability results for directed acyclic graphs, while Jojić [4] proves shellability for digraphs with complete sources and analyzes bidirected and essentially tree-like classes. The Paley tournament has directed triangles and every vertex has outdegree three (rather than a complete source's six); those results do not by themselves imply this homotopy or its affine character. Björner and Welker [5] study all *acyclic arc sets* without the indegree-one restriction, a different simplicial complex. Published calculations of directed **flag** and **neighborhood** complexes of tournaments concern different face conditions and therefore do not determine \(\operatorname{DT}(T_7)\).

A particularly close later study is Courtney's *The Directed Forest Complex of Cayley Graphs* [6], whose abstract covers the general Cayley setting. Its full thesis was unavailable for material comparison; it is therefore a genuine residual originality risk rather than evidence of noncoverage. No priority or exhaustive-literature claim is made.

## Limitations
The result is for exactly this seven-vertex tournament and its specified affine symmetry group. It does not classify all tournaments, all Cayley directed-forest complexes, or integral \(G\)-lattices, nor does it follow merely from the face vector. The homotopy certificate is a finite exhaustive proof; it does not provide a symbolic all-order formula. Relevant material unavailable in full, especially [1] and [6], may contain overlapping calculations and merits independent review. No independent scientific audit has been performed.

## References
[1] D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory A **88** (1999), 112–122, DOI: 10.1006/JCTA.1999.2984 (bibliographic metadata; complete text unavailable for this comparison).

[2] D. N. Kozlov, *Directed trees in a string, real polynomials with triple roots, and chain mails*, arXiv:math/0210045, publicly posted October 3, 2002; https://arxiv.org/abs/math/0210045 (full text inspected).

[3] A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148, posted August 8, 2005; https://arxiv.org/abs/math/0508148 (full text inspected).

[4] D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475, posted September 21, 2011; https://arxiv.org/abs/1109.4475 (full text inspected).

[5] A. Björner and V. Welker, *Complexes of Directed Graphs*, SIAM Journal on Discrete Mathematics **12** (1999), 413–424, DOI: 10.1137/S0895480198338724 (abstract and bibliographic description inspected).

[6] K. Courtney, *The Directed Forest Complex of Cayley Graphs*, Boise State University M.S. thesis (May 2020), DOI: 10.18122/td/1684/boisestate; https://scholarworks.boisestate.edu/td/1684/ (abstract and limited opening preview only; full text unavailable).
