# The \(S_5\times C_2\) homology character of the Desargues independence complex

## Finding

Let \(D=H(5,2)\) be the twenty-vertex Desargues graph, with vertices the two-element and three-element subsets of \([5]\), adjacent exactly when one is contained in the other. Let \(X=\operatorname{Ind}(D)\) be its ordinary independence complex, and let \(G=\operatorname{Aut}(D)\cong S_5\times C_2\). Write \(c\) for the central complement involution, \(\varepsilon(c)=-1\), and \(\mathrm{Perm}_5\) for the natural five-point permutation representation of \(S_5\). Then

\[
\widetilde H_4(X;\mathbb Z)\cong\operatorname{sgn}_{S_5}\boxtimes\varepsilon,
\qquad
\widetilde H_5(X;\mathbb Q)\cong\mathrm{Perm}_5\boxtimes\varepsilon.
\]

The other reduced integral homology groups vanish, while \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^5\) as an abelian group. Thus the full rational fifth-homology character is

\[
\chi_5(p,c^s)=(-1)^s\#\{i\in[5]:p(i)=i\},
\]

and the integral fourth-homology character is

\[
\chi_4(p,c^s)=(-1)^s\operatorname{sgn}(p)
\qquad(p\in S_5,\ s\in\{0,1\}).
\]

In particular, the central complement acts as minus the identity on **both** positive-degree integral homology groups, and no positive-degree rational homology class is fixed by the full automorphism group. The four-dimensional standard representation and the trivial line occur once each in fifth homology when restricted to \(S_5\). The statement does **not** identify the integral fifth-homology lattice as an integral permutation module.

## Assumptions and scope

Use vertices numbered \(0,\ldots,9\) for lexicographically ordered two-subsets and \(10,\ldots,19\) for lexicographically ordered three-subsets. An independent face is a set of vertices containing no inclusion edge. Every simplex is oriented by increasing vertex number, and augmented simplicial chains include the empty face in degree \(-1\). The action of \((p,c^s)\) first applies \(p\) to the underlying five symbols and then, if \(s=1\), replaces each subset by its complement. All integral assertions refer to ordinary integral singular or simplicial homology; the asserted five-dimensional module is over \(\mathbb Q\).

The stated group is the full automorphism group: the two bipartite sides are connected by a graph, so an automorphism preserves the sides or exchanges them. On the two-subset side, distance-two adjacency is exactly intersection in one symbol, giving the triangular graph \(T(5)\). Its five maximal four-cliques are the stars of the five original symbols, forcing each side-preserving automorphism to come from \(S_5\). The three-subset vertices are determined by their three neighbors, while complementation exchanges the two sides. Hence the full group is precisely \(S_5\times\langle c\rangle\) of order \(240\).

## Proof

**1. Exact integral homology.** The exhaustive face vector, including the empty simplex first, is

\[
(1,20,160,660,1510,1924,1320,480,115,20,2).
\]

There are \(6{,}211\) nonempty faces. On these, process vertex labels \(0,1,\ldots,19\) in order. At each stage, pair every still-unmatched face \(\sigma\) omitting the current label \(v\) with \(\sigma\cup\{v\}\) if both are still unmatched and the union is independent. The deterministic matching has \(3{,}102\) pairs and seven critical faces: one vertex, one four-simplex and five five-simplices. Direct the \(30{,}360\) nonempty face-cover incidences upward for a matched cover and downward otherwise. An exhaustive topological sort visits all \(6{,}211\) faces, proving acyclicity.

For each matched pair \(\sigma\subset\tau\), the incidence \([\tau:\sigma]\) equals \(+1\) or \(-1\). Integral unit-pivot elimination along the acyclic matching gives a Morse complex with exactly these seven cells. Its only potentially nonzero boundary is from the five critical five-cells to the critical four-cell; the signed gradient-path recursion yields the **zero** row \((0,0,0,0,0)\). Thus the reduced integral homology is \(\mathbb Z\) in degree four, \(\mathbb Z^5\) in degree five, and zero elsewhere. The attached verifier reconstructs the complete face poset, matching, acyclicity, and every signed integer Morse coefficient, not merely ranks over a field.

**2. A signed Lefschetz calculation.** For any simplicial automorphism \(g\), let \(\widetilde L(g)\) denote the alternating trace on the augmented chain groups, equal to the alternating trace on reduced homology. A fixed oriented simplex contributes its permutation sign multiplied by \((-1)^{\dim\sigma}\); the empty simplex contributes \(-1\).

There is an independent orbit formulation. Decompose the twenty vertices into \(g\)-orbits; remove any orbit containing an internal graph edge and join two remaining orbits when their union contains a graph edge. If \(P_g(t)\) is the independence polynomial of this conflict graph, then

\[
\widetilde L(g)=-P_g(-1).
\]

Indeed, a \(g\)-invariant independent face is a union of compatible vertex-orbits; if it contains \(r\) orbits, its signed Lefschetz contribution is \((-1)^{r-1}\), including the empty face at \(r=0\). Direct fixed-simplex summation and the orbit-graph method agree on **all 240 elements**. The seven conjugacy classes of \(S_5\), their sizes, and the two trace values are:

| Cycle type of \(p\) | Size in each half | \(\widetilde L(p,1)\) | \(\widetilde L(p,c)\) |
|---|---:|---:|---:|
| \(1^5\) | 1 | −4 | 4 |
| \(2,1^3\) | 10 | −4 | 4 |
| \(2^2,1\) | 15 | 0 | 0 |
| \(3,1^2\) | 20 | −1 | 1 |
| \(3,2\) | 20 | −1 | 1 |
| \(4,1\) | 30 | −2 | 2 |
| \(5\) | 24 | 1 | −1 |

Consequently the full reduced Lefschetz character is

\[
\widetilde L(p,c^s)=(-1)^s\bigl(\operatorname{sgn}(p)-\#\operatorname{Fix}_{[5]}(p)\bigr).
\]

**3. The one-dimensional character is forced.** By Step 1, the fourth-homology character is one-dimensional, hence of the form \(\lambda(p,c^s)=\operatorname{sgn}(p)^a(-1)^{bs}\), with \(a,b\in\{0,1\}\). Let \(\chi_5\) be the fifth-homology character. The Lefschetz identity gives \(\chi_5=\lambda-\widetilde L\).

If \(a=0\), every transposition of \(S_5\) has trace \(5\) on the five-dimensional \(H_5\), hence acts as the identity (its eigenvalues are \(\pm1\)). Because transpositions generate \(S_5\), every three-cycle would also have trace \(5\). But the Lefschetz formula gives trace \(2\) on a three-cycle, a contradiction. Thus \(a=1\).

If \(b=0\), a transposition multiplied by \(c\) has \(H_5\)-trace \(-5\), so it acts as minus the identity. Products of such elements for any two transpositions then act as the identity; in particular a three-cycle would have trace \(5\), again contradicting the calculated trace \(2\). Thus \(b=1\).

It follows that \(\lambda=\operatorname{sgn}\boxtimes\varepsilon\), and subtracting the Lefschetz character gives precisely \(\chi_5(p,c^s)=(-1)^s\#\operatorname{Fix}_{[5]}(p)\). Semisimplicity of rational representations of finite groups and equality of characters give the asserted rational module. The fourth-homology lattice is a rank-one integral module, so its sign character determines it integrally. The central involution has trace \(-5\) on the rational fifth homology and order two; it must act as \(-I\) rationally and hence also on its free integral lattice.

## Verification

With Python 3 (standard library only), run:

```text
python3 verification/verify_desargues_character.py
```

It prints `DESARGUES_EQUIVARIANT_HOMOLOGY_OK`. The script independently rebuilds the graph and all faces; verifies the \(30\) incidence edges, matching and full directed-face-poset acyclicity; checks all five integral Morse differentials; enumerates the full \(240\)-element action and verifies adjacency preservation; and computes every signed Lefschetz trace by **two structurally different exact methods**. No floating-point approximation, sampling, or unverifiable external log is used.

## Relationship to prior work

Barmak's 2010 star-cluster theorem proves that independence complexes of triangle-free graphs have suspension homotopy type [1, Theorem 3.4]. It does not determine the integral symmetry action here. Previously published exact Desargues calculations [2–4] identify the nonequivariant homotopy type \(S^4\vee\bigvee^5S^5\); that fact is credited, not claimed as new. Their inspected main results do not specify either of the two natural homology characters. Tsukuda's incidence-graph/Alexander-dual reduction [5] is a plausible general structural comparison; an accessible abstract does not provide this particular five-point representation, while the full paper was unavailable for material examination. Kumar–Singh–Verma [6] compute edge-ideal syzygy invariants of bipartite Kneser graphs, which do not directly provide the equivariant topological homology module. The classical full automorphism group is also independently documented in [7].

The novelty asserted here is **only** the complete degree-four integral character and degree-five rational character under all \(240\) automorphisms, together with their representation-theoretic consequences. The nonequivariant wedge decomposition, the underlying graph, and the existence of its symmetries are not new assertions.

## Limitations

The theorem treats exactly the indicated finite graph and does not classify an infinite family. The fifth-homology lattice is determined as an abelian group and as a rational \(G\)-module, but not up to integral \(G\)-module isomorphism. Bibliographic searching cannot establish absolute novelty; in particular an unavailable general incidence-graph text or unindexed equivalent calculation remains a residual overlap risk. The finite proof establishes the claimed case without extrapolating to larger graphs. Independent scientific audit has not been performed.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, submitted 2010-07-02, Theorem 3.4. https://arxiv.org/html/1007.0418v1
2. *The Desargues graph independence complex is \(S^4\vee\bigvee^5S^5\)*, publicly indexed full scientific text, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-graph-independence-complex-is-s-4-vee-bigvee-5-s-5--ca55f3b9deba
3. *The Desargues independence complex is \(S^4\vee\bigvee^5S^5\)*, publicly indexed full scientific text, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563
4. *Independence complex of the Desargues graph is \(S^4\vee\bigvee^5S^5\)*, publicly indexed full scientific text, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-independence-complex-of-the-desargues-graph-is-s-4-vee-bigvee-5--f3b1cf10aadb
5. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46. https://doi.org/10.55016/ojs/cdm.v12i1.62277
6. A. Kumar, P. Singh, R. Verma, *Certain Homological Invariants of Bipartite Kneser Graphs*, arXiv:2105.06144v1, 2021-05-13. https://arxiv.org/abs/2105.06144
7. M. Randić, *Symmetry properties of graphs of interest in chemistry. II. Desargues–Levi graph*, International Journal of Quantum Chemistry 15 (1979). https://doi.org/10.1002/qua.560150610
