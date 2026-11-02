# Two winding sectors in the optimal recolouring graph of the Grötzsch graph

## Finding

Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, and let \(\mathcal R_4(G)\) be the graph of all proper vertex colourings with **named** colours \(0,1,2,3\), adjacent precisely when one vertex changes colour and propriety is retained. There are exactly \(12{,}480\) such colourings, and the complete recolouring graph has exactly **two connected components, each of order \(6{,}240\)**. These are the two level sets of the explicit signed winding invariant defined below.

The complete graph has \(45{,}240\) edges, degree enumerator
\[
D(t)=480t^{5}+2640t^{6}+3840t^{7}+4320t^{8}+1200t^{9},
\]
and each component has radius \(15\), diameter \(17\), and \(22{,}620\) edges. In each component the numbers of vertices of eccentricities \(15,16,17\) are respectively \(1{,}080,5{,}100,60\). The minimum number of named colours for which all proper colourings of \(G\) are connected by single-vertex recolouring is exactly **five**.

## Assumptions and scope

Use indices in \(\mathbb Z/5\mathbb Z\). The vertices are originals \(v_i\), their shadows \(s_i\), and an apex \(z\). The edges are \(v_iv_{i+1}\), \(s_iv_{i-1}\), \(s_iv_{i+1}\), and \(zs_i\) for every \(i\); there are no others. This is Mycielski's construction on the pentagon. A colouring is a function from these eleven vertices to the **fixed four-element palette**, not a colour partition modulo permutations. A move changes the value at exactly one vertex.

For a proper colouring \(c\), set \(a=c(z)\). Define a three-colouring \(r(c)\) of the original pentagon by
\[
r_i(c)=\begin{cases}c(v_i),&c(v_i)\ne a,\\c(s_i),&c(v_i)=a.\end{cases}
\]
All its values lie among the three colours different from \(a\). Let \(q_a\) rank these three colours in increasing numerical order as \(0,1,2\), and put \(h_i=q_a(r_i(c))\). Let \(\varepsilon_i=1\) if \(h_{i+1}-h_i\equiv1\pmod3\), and \(\varepsilon_i=-1\) otherwise. Then
\[
\boxed{\Omega(c)=(-1)^a\,\frac{1}{3}\sum_{i=0}^{4}\varepsilon_i\in\{-1,+1\}.}
\]
This quantity is the **signed winding**. The choice of sorted named colours, and the factor \((-1)^a\), are part of the normalization; without them the statement of the invariant at apex recolourings is not the one claimed.

## Proof

**Optimality of four colours.** The pentagon has chromatic number three. A proper three-colouring of its Mycielskian would assign some colour \(a\) to the apex, and no shadow could receive \(a\). Replacing the colour of every original vertex coloured \(a\) with the colour of its own shadow yields a proper two-colouring of the original pentagon: the shadow sees both of the original's neighbours. This is impossible. Extending a three-colouring of the pentagon by copying it to the shadows and giving the apex a fourth colour proves \(\chi(G)=4\).

**Well-defined signed winding.** The three-colouring \(r(c)\) is proper on the original pentagon. Adjacent originals cannot both have colour \(a\), and a shadow is adjacent to both neighbours of its original; this establishes properness in all cases. Every difference \(h_{i+1}-h_i\) has residue \(1\) or \(-1\) modulo three. The sum of five such signed differences is an odd multiple of three, necessarily \(3\) or \(-3\); hence \(\Omega(c)\) belongs to the stated two-element set.

**Invariance under recolouring.** If a move does not recolour \(z\), the three-colouring \(h\) changes at most one position. In any proper three-colouring of a cycle, a legal single-position change requires that its two neighbours share a colour; the two altered directed edge contributions therefore sum to zero both before and after. Thus the winding does not change. For an apex move, the two old/new apex colours are absent from all five shadows. The finite case lemma is that the signed winding formula has the same value on the two resulting proper colourings. The complete lemma is checked in both standalone programs, which test **every** legal apex move; in fact, for each unordered pair of apex colours and each winding sign there are exactly \(190\) such undirected moves. This is a finite exhaustive lemma, not an appeal to sampled examples.

**Exhaustive connectivity and metric certificate.** The attached programs give two separate complete enumerations. The recursive vertex-colouring search extends every legal partial assignment; the second program instead enumerates the \(240\) proper four-colour assignments of the original pentagon and forms all admissible independent shadow choices for each apex colour. Both yield precisely \(12{,}480\) distinct states. Legal moves are formed by a neighbour-colour test in the first implementation and, independently, by grouping states that agree at ten of the eleven positions in the second. The resulting edge set has \(45{,}240\) undirected edges, and both BFS and disjoint-set union give exactly two components of size \(6{,}240\). Each component has constant \(\Omega\), with \(6{,}240\) colourings of each sign, so these are **exactly** the two invariant classes. For each fixed apex colour, its \(3{,}120\) colourings split into two connected induced subgraphs of size \(1{,}560\), one per sign; each pair of different apex colours has \(190\) cross-edges within each sign. This supplies a more refined finite connectivity witness.

The degree counts follow by examining every legal one-vertex move. The radius, diameter and eccentricity distributions are determined by BFS from one representative of each orbit under the colour-permutation group \(S_4\) and the dihedral symmetry \(D_5\) of the pentagon. Both programs independently construct this quotient, with \(56\) orbits, of which \(48\) have size \(240\) and \(8\) have size \(120\). Each group element preserves the recolouring metric, so checking all orbit representatives proves the bounds for **all** \(12{,}480\) vertices. The total eccentricity counts are \(2{,}160,10{,}200,120\) at distances \(15,16,17\); an odd palette permutation interchanges the two equal components, giving the per-component figures.

**Five-colour threshold.** The graph is three-degenerate. For example, successively delete vertices in the order \(s_0,v_1,s_2,v_0,v_4,v_3,s_4,v_2,s_1,s_3,z\); each has at most three neighbours remaining. In a \(d\)-degenerate graph every pair of proper named \(k\)-colourings is connected whenever \(k\ge d+2\): inductively reconfigure after deleting a vertex of degree at most \(d\), recolouring that vertex to an available spare colour whenever it blocks a step. This established bound gives connectivity for every \(k\ge5\). Four colours are not connected by the preceding result, and three colours do not suffice, proving the sharp threshold.

## Verification

Run `python3 verify_coloring_recursive.py` and `python3 verify_coloring_independent.py` from the same extracted directory. They use only the Python standard library. Both were executed from the final package paths and passed all assertions. Their counted universes are exhaustive: the first assigns every possible colour to each vertex subject to prior-edge constraints; the second lists every proper outer-cycle word and every permitted apex/shadow assignment. One forms edges from recolouring constraints; the other forms all pairs at Hamming distance exactly one. Each computes all connected components and exact eccentricities using graph automorphism orbits, with no randomness or heuristics. The software is a finite proof certificate; it makes **no** claim about the colouring dynamics of larger Mycielski graphs.

## Relationship to prior work

Mycielski's classical construction and the 4-chromaticity of \(\mu(C_5)\) are established; neither is new. Cereceda, van den Heuvel and Johnson studied the recolouring graph, proved the general degeneracy-plus-two connectivity theorem, and established winding invariance for *three*-colourings of an arbitrary cycle. The present signed-winding formula is a lift from the inner three-colouring to **four** named colours on the Mycielski graph and, crucially, also handles recolouring of the apex. The general theorem implies five-colour connectivity but not the number or structure of four-colour components. Brewster and Noel studied more general homomorphism and circular-colouring mixing; the Brewster–McGuinness–Moore–Noel dichotomy concerns computational complexity for input graphs; neither statement implies this exact finite configuration graph. Brewster and Moore's later cycle-wind characterization explicitly assumes a circular-colouring ratio **strictly below four** and therefore does not determine this four-colour case. Mohar, Simonyi and Tardos studied chromatic constraints on quadrangulations, not this reconfiguration graph. The previously known total count \(12{,}480\) is not claimed as original. The new claim is the explicit two-sector optimal-colouring reconfiguration structure, including its exact connectivity and metric data.

## Limitations

This is an exhaustive finite theorem for the **one** eleven-vertex Grötzsch graph, with named colours and one-vertex moves. It is not an infinite-family connectivity result, an asymptotic mixing-time theorem, or a proof of rapid sampling; in fact reducibility into two components rules out irreducibility for the usual four-colour single-site chain. The exact diameter statement concerns shortest recolouring paths **within** a component; no finite path connects different signs. The signed-winding apex-transition case and the component/metric census use the supplied independently executable finite enumeration. Historical priority remains qualified: an equivalent specific calculation could exist under graph-homomorphism complex or projective-quadrangulation terminology. Independent scholarly audit has not been performed.

## References

1. L. Cereceda, J. van den Heuvel, M. Johnson, *Connectedness of the Graph of Vertex-Colourings*, LSE-CDAM-2005-11 (July 2005), especially Theorem 3 and Lemma 4; public report: https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf .
2. B. Mohar, G. Simonyi, G. Tardos, *Local chromatic number of quadrangulations of surfaces*, arXiv:1010.0133 (first arXiv public date 2010-10-01), https://arxiv.org/abs/1010.0133 .
3. R. C. Brewster, J. A. Noel, *Mixing Homomorphisms, Recolourings, and Extending Circular Precolourings*, arXiv:1412.3493 (first arXiv public date 2014-12-10), https://arxiv.org/abs/1412.3493 .
4. R. C. Brewster, S. McGuinness, B. Moore, J. A. Noel, *A Dichotomy Theorem for Circular Colouring Reconfiguration*, arXiv:1508.05573 (2015-08-23), https://arxiv.org/abs/1508.05573 .
5. R. C. Brewster, B. Moore, *Characterizing Circular Colouring Mixing for \(p/q<4\)*, arXiv:2008.12185 (2020-08-27), https://arxiv.org/abs/2008.12185 .
