# Integral homotopy type of the Pappus graph matching complex

## Finding
For the Pappus graph \(P\), the ordinary matching complex \(\mathcal M(P)\), whose simplices are sets of pairwise disjoint graph edges, is homotopy equivalent to a wedge of forty five-dimensional spheres:
\[
\mathcal M(P)\simeq\bigvee^{40}S^5.
\]
In particular \(\widetilde H_5(\mathcal M(P);\mathbb Z)\cong\mathbb Z^{40}\), and \(\widetilde H_i(\mathcal M(P);\mathbb Z)=0\) for every \(i\ne5\). This is an integral homotopy statement, not merely a computation over a field.

## Assumptions and scope
Take the labeled graph \(P\) with vertex set \(\{0,1,\ldots,17\}\). Include the eighteen cycle edges \(\{i,i+1\pmod {18}\}\), together with the distinct edges \(\{i,i+s_i\pmod {18}\}\) defined by the length-eighteen LCF sequence \([5,7,-7,7,-7,-5]^3\). Sort all graph edges lexicographically to index the twenty-seven vertices of \(\mathcal M(P)\) from zero through twenty-six. Faces are exactly the nonempty subsets of these edge indices having pairwise disjoint graph endpoints. Use ordinary simplicial homotopy and integral cellular boundaries, with no metric parameter or augmented empty face in the matching poset.

The Pappus graph is the cubic symmetric eighteen-vertex Levi graph of the Pappus \((9_3)\)-configuration; the LCF description fixes the graph independently of nomenclature. The complex here is the *ordinary* matching complex; it is not the perfect-matching subcomplex or the complex of acyclic vertex-edge vector fields.

## Proof
**Exhaustive face construction.** Enumerate allowed subsets recursively in strictly increasing edge-index order. On inserting graph edge \(e\), forbid all later edges incident to an endpoint of \(e\). This recursion is a bijection with all matchings, including the empty matching counted only for bookkeeping. The counts for matching cardinalities \(0\) through \(9\) are
\[
(1,27,297,1719,5643,10557,10737,5319,1026,42).
\]
Thus there are \(35{,}367\) nonempty faces, and dimension eight.

**A complete acyclic matching.** On the finite face poset of these nonempty simplices, perform an element-toggle matching stagewise in the graph-edge index order

`[7,13,17,26,25,12,21,2,8,20,22,15,23,10,19,3,9,16,24,5,4,1,6,0,11,18,14]`.

At stage \(p\), visit faces in the fixed recursive enumeration order and pair each still-unpaired face \(\sigma\) lacking \(p\) to \(\sigma\cup\{p\}\) whenever that upper face is present and still unpaired. Remove both from subsequent stages. This gives precisely \(17{,}660\) matched pairs. The \(47\) unmatched simplices consist of one vertex, forty-three five-simplices and three six-simplices. Reverse each matched covering incidence of the ordinary face-poset Hasse graph, retaining all other covering incidences downward. An exhaustive topological sort visits all \(35{,}367\) vertices of this directed graph and all \(191{,}349\) directed incidences, proving it acyclic. The acyclic matching therefore yields a CW complex with one zero-cell, forty-three five-cells and three six-cells, and no cells in intermediate degrees.

**Integral attaching degrees.** Orient each simplex by the increasing ordering of its edge indices. The integral cellular differential from critical six-cells to critical five-cells can be obtained by signed gradient-path elimination. In detail, a critical five-cell contributes its own basis vector, while a five-cell matched downward to dimension four contributes zero. If a five-cell \(\sigma\) is matched upward to a six-cell \(\tau\), solve the integral boundary equation \(\partial\tau=0\) for \(\sigma\): replace it by the negative sum over the other five-faces of \(\tau\), each coefficient multiplied by the quotient of the corresponding boundary incidence and the \(\sigma\)-incidence. The latter is \(\pm1\); no division beyond unit incidence is needed. Gradient acyclicity makes the recursion finite. Applying it to each oriented face of every critical six-cell gives an integer matrix with forty-three ordered critical-five-cell rows and three ordered critical-six-cell columns. The complete nonzero column dictionaries, using zero-based row indices, are:

```
column_0 = {3:1, 7:1, 10:1, 15:1, 21:1, 23:-1, 30:-1}
column_1 = {2:-1, 3:1, 13:-1, 14:1, 16:1, 26:-1, 28:1, 31:-1, 37:1, 38:1}
column_2 = {15:1, 19:-1, 23:-1, 24:1, 27:-1}
```

Rows \(30,13,27\), in that order, form the three-by-three minor \(-I_3\). Hence the integral boundary has rank three and primitive image with three unit Smith invariant factors. The five-skeleton is a wedge of forty-three copies of \(S^5\), since it has a single zero-cell and no cells of dimensions one through four. For a wedge of five-spheres, each map \(S^5\to\bigvee^{43}S^5\) is completely determined by its vector of integer degrees, because \(\pi_5(\bigvee^{43}S^5)\cong\mathbb Z^{43}\). A unimodular basis change sends the three independent attaching vectors to three coordinate vectors; the three degree-one attaching cells cancel corresponding five-cells up to homotopy. The result is \(\bigvee^{40}S^5\), as claimed.

## Verification
Run `python3 verify_pappus_integral.py` with Python 3.9 or later. It reconstructs the LCF graph and all simplices, generates all matching pairs, checks the directed Hasse graph by topological sorting, expands signed integral gradient paths, and checks every entry of the reported matrix and the unimodular minor. The expected terminal prefix is `VERIFY_OK` with `faces_nonempty=35367`, `matched_pairs=17660`, `critical=1x0+43x5+3x6`, and `directed_incidences=191349`.

Run `python3 verify_pappus_mod2.py` separately. This implements a different matching enumeration and exact bitset Gaussian elimination of every simplicial boundary over \(\mathbb F_2\). Its independently recovered augmented boundary ranks for dimensions \(0\) through \(8\) are \((1,26,271,1448,4195,6362,4335,984,42)\), with reduced degree-five Betti number forty and all others zero. The mod-two computation corroborates, but by itself does **not** establish, the integral wedge decomposition.

## Relationship to prior work
Kozlov's work on combinatorial simple-homotopy methods (arXiv:math/0503613, first public version March 28, 2005, primary MSC \(57Q10\)) supplies the archive-era methodological setting, not this Pappus-specific result. Donovan and Scoville's matching-complex analysis covers structured families including paths, cycles and Dutch windmill graphs; its matching-complex results do not imply the stated result for this Pappus graph. Bayer, Goeckner and Jelić Milutinović analyze matching complexes that are homology manifolds. The present complex is nonpure: it has maximal matchings of sizes six, seven, eight and nine, precluding direct application of a pure homology-manifold classification. Results concerning perfect-matching complexes of honeycomb graphs have a different face condition: here non-perfect maximal matchings occur.

A separately published exact computation on the **same ordinary Pappus matching complex** finds reduced mod-two homology of rank forty in degree five, with zero other reduced mod-two ranks. That result explicitly does not determine integral homology, torsion or homotopy type. The new assertion is the strictly stronger integral homotopy classification, established by the primitive signed Morse boundary. Results for the Heawood, Desargues and Möbius–Kantor matching complexes involve different graph complexes and do not logically imply this one.

## Limitations
Only this fixed eighteen-vertex Pappus graph and its ordinary matching complex are treated; no all-parameter family theorem is asserted. The proof is finite exhaustive discrete Morse reduction plus a topological attaching-map argument; the attached programs are fully inspectable computational witnesses, not a replacement for defining the construction. The stated classification does not address the homotopy type of the perfect-matching subcomplex. A complete global bibliographic uniqueness claim cannot follow from indexed searches: an equivalent calculation could exist in unindexed or differently titled literature.

## References
1. Dmitry N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613 (initial public version 2005-03-28), primary MSC 57Q10. https://arxiv.org/abs/math/0503613
2. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex of discrete Morse functions*, arXiv:2207.13780 (2022). https://arxiv.org/abs/2207.13780
3. Margaret Bayer, Bennet Goeckner and Marija Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328 (2019). https://arxiv.org/abs/1906.03328
4. Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (2022). https://arxiv.org/abs/2209.02803
5. *Mod-2 homology of the Pappus matching complex*, previously published exact finite calculation. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-pappus-matching-complex--a28326a5f491
6. *Pappus Graph*, Wolfram MathWorld, for graph naming and LCF graph description. https://mathworld.wolfram.com/PappusGraph.html
