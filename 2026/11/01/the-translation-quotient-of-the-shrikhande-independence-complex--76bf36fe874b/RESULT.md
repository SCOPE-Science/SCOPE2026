# The translation quotient of the Shrikhande independence complex is a wedge of two spheres

## Finding
Let \(S\) be the Shrikhande graph on \(A=(\mathbb Z/4\mathbb Z)^2\), joining distinct points when their difference lies in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\). Let \(K=\operatorname{Ind}(S)\) be its ordinary simplicial independence complex. The group \(A\) acts on \(|K|\) by vertex translation. Its **ordinary topological quotient** satisfies
\[
\boxed{|K|/A\simeq S^2\vee S^2.}
\]
In particular, the orbit space is simply connected, \(\widetilde H_2(|K|/A;\mathbb Z)\cong\mathbb Z^2\), and all other reduced integral homology groups vanish. This is an assertion about the ordinary orbit space, not a homotopy quotient or Borel construction.

## Assumptions and scope
Use residue representatives \(0,1,2,3\); label \((i,j)\in A\) by \(4i+j\). A face of \(K\) is a set of vertices containing no edge of \(S\), including the empty face. All spaces are geometric realizations with their usual CW topology. Only the full order-sixteen translation group \(A\) is considered. The graph's adjacency difference set is the six-element set with the two signs coupled in \(\pm(1,1)\). No generalized strongly regular graph or other subgroup quotient is asserted.

## Proof
**Step 1: enumerate the original complex.** Directly testing all independent subsets of the sixteen vertices gives exactly \(16\) vertices, \(72\) edges, \(96\) triangles and \(16\) tetrahedra, with no five-vertex faces. The exhaustive enumeration and the graph's six-element difference set are implemented verbatim in `verify.py`.

**Step 2: a regular quotient cell structure.** Barycentrically subdivide \(K\). A simplex in \(\operatorname{sd}K\) is a strict chain \(F_0\subsetneq\cdots\subsetneq F_q\) of nonempty faces. Translation acts on these chains. A translation stabilizing a chain simplex setwise preserves the cardinality of every flag vertex, so it fixes each barycentric vertex and the whole simplex pointwise. Thus no simplex has a nontrivial internal identification, and the orbits of chains give a finite regular CW structure on \(|K|/A\). Enumerating each orbit by the lexicographically least translated chain gives the cell counts
\[
(c_0,c_1,c_2,c_3)=(17,62,72,24).
\]
The orbit-cell incidences come from deleting one chain entry, retaining its orientation sign; these are completely reconstructed in the verifier.

**Step 3: collapse away all three-cells.** The 24 pairs in `certificate.json`, keyed by zero-based indices in sorted canonical orbit-cell lists, each consist of a three-cell and a two-face appearing exactly once among the remaining three-cells. Each is a regular elementary CW collapse. The verifier reconstructs all face incidences before testing the pair sequence, checks the unique-coface condition at every stage, and confirms that no three-cell remains. The resulting connected two-dimensional CW complex \(Y\) has precisely \(17\) vertices, \(62\) edges and \(48\) two-cells; hence
\[
\chi(Y)=17-62+48=3.
\]

**Step 4: prove simple connectivity, not just trivial abelianized homology.** The 16 edge indices in `certificate.json` form a spanning tree of the one-skeleton. Collapse that tree for a presentation of \(\pi_1(Y)\). Each remaining edge is a generator and each surviving triangular two-cell supplies a relator involving its three oriented boundary edges. The certificate lists 46 consecutive pairs (triangle index, previously unknown edge index). For each pair, the other two edges of that triangle are already in the tree or earlier elimination list. Thus the triangular relator makes its third edge trivial. The verifier checks all 46 inductions and that every one of the 62 edges is accounted for. Consequently \(\pi_1(Y)=1\), not merely \(H_1(Y;\mathbb Z)=0\).

**Step 5: identify the homotopy type.** A connected, simply connected finite two-dimensional CW complex has free second homology, and \(\operatorname{rank}H_2(Y;\mathbb Z)=\chi(Y)-1=2\); no other positive-dimensional reduced homology can occur. By Hurewicz, two maps of spheres generate \(\pi_2(Y)\), giving a homology isomorphism \(S^2\vee S^2\to Y\). The homology form of Whitehead's theorem for simply connected CW complexes upgrades this to a homotopy equivalence. The 24 collapses preserve homotopy type, proving the boxed statement.

## Verification
Put the exact included `verify.py` and `certificate.json` in one directory and run `python3 verify.py` using Python 3's standard library. It exhaustively generates original independent subsets, all barycentric flags, all sixteen translations, canonical cell orbits, every codimension-one top-cell incidence, all certified free-face collapses, and the complete triangular-relator elimination. The output is included as `verification_output.txt`, ending in `VERIFY_OK`. These are exhaustive finite checks for the exact stated sixteen-vertex object, not numerical approximations or a claim about an infinite graph family.

## Relationship to prior work
Barmak's 2010 paper develops the topology of independence complexes, but does not determine this particular translation quotient. Earl, Vander Meulen and Van Tuyl's 2015 treatment concerns well-covered circulant graphs and their combinatorial topology, not this orbit-space calculation. An indexed earlier finding establishes \(\operatorname{Ind}(S)\simeq\bigvee^{23}S^2\) and its contrast with the \(4\times4\) rook graph. That nonequivariant equivalence does **not** imply the present statement: taking orbit spaces requires information about the particular group action, and does not preserve arbitrary nonequivariant homotopy equivalences. A separate indexed result computes an intrinsic graph Čech complex of the same graph, a different simplicial construction. The present claim concerns solely the ordinary quotient of the Shrikhande **independence** complex.

## Limitations
No equivariant homotopy equivalence, integral module identification, or classification of other subgroup orbit spaces is asserted. The result depends on an explicit finite certificate, whose canonical indexing and full independent-cell reconstruction are provided. The earlier nonequivariant homotopy calculation is not claimed as new. Unindexed equivalent literature cannot be excluded, and independent scientific audit is not asserted.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public July 2, 2010, https://arxiv.org/abs/1007.0418.
2. J. Earl, K. N. Vander Meulen and A. Van Tuyl, *Independence complexes of well-covered circulant graphs*, arXiv:1505.02837v1, first public May 11, 2015, https://arxiv.org/abs/1505.02837.
3. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, public mathematical record (2026), identifier `2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187`, https://github.com/Resultary/2026.
4. *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, public mathematical record (2026), identifier `2026/10/11/SCOPE-scale-two-ech-homotopy-distinguishes-the-shrikhande-and-rook-gra--5b6e4436155e`, https://github.com/Resultary/2026.
