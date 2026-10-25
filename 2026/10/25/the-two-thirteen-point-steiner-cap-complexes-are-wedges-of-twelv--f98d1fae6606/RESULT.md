# The two thirteen-point Steiner cap complexes are wedges of twelve and seventeen four-spheres

## Finding

Let \(T\) be one of the two nonisomorphic Steiner triple systems of order thirteen. Its **cap complex** is the abstract simplicial complex
\[
K(T)=\{\sigma\subseteq\{0,\ldots,12\}:B\nsubseteq\sigma\text{ for every triple }B\in T\}.
\]
For the cyclic system \(C\) and its Pasch-switched companion \(N\), respectively, there are integral homotopy equivalences
\[
\boxed{K(C)\simeq\bigvee^{12}S^4,\qquad K(N)\simeq\bigvee^{17}S^4.}
\]
These are the complete classification of the homotopy types for the two isomorphism classes of order-thirteen Steiner triple systems. Both complexes have facets in dimensions four and five, despite having homotopy concentrated in dimension four. If \(p(T)\) is the number of Pasch configurations, their sphere multiplicities satisfy \(\operatorname{rank}\widetilde H_4(K(T);\mathbb Z)=25-p(T)\) for these two systems only, with \(p(C)=13\) and \(p(N)=8\).

The cyclic thirteen-point translation group acts on \(\widetilde H_4(K(C);\mathbb Q)\) by the twelve-dimensional augmentation representation: the trace is twelve at the identity and minus one at each nonidentity translation. Equivalently, it is the rational cyclotomic representation \(\mathbb Q(\zeta_{13})\).

## Assumptions and scope

Let the points be the residues modulo thirteen. The blocks of \(C\) are all thirteen translates of each of the triples \(\{0,1,4\}\) and \(\{0,2,7\}\). Set
\[
\begin{aligned}
P_-&=\big\{\{0,1,4\},\{0,2,7\},\{1,7,9\},\{2,4,9\}\big\},\\
P_+&=\big\{\{0,1,7\},\{0,2,4\},\{1,4,9\},\{2,7,9\}\big\}.
\end{aligned}
\]
Define \(N=(C\setminus P_-)\cup P_+\). Each of \(C,N\) has twenty-six blocks, and each of the seventy-eight unordered pairs of points belongs to exactly one block. The two different Pasch counts certify that the systems are nonisomorphic; the classical two-isomorphism-class fact is recorded in the cited design literature. The forbidden triples are blocks, not collinear triples of the thirteen-point projective plane of order three: those are different simplicial complexes.

Write \(f_i\) for the number of \(i\)-simplices. Exact enumeration gives
\[
(f_0,f_1,f_2,f_3,f_4,f_5)(K(C))=(13,78,260,455,312,39),
\]
\[
(f_0,f_1,f_2,f_3,f_4,f_5)(K(N))=(13,78,260,455,312,34).
\]
There are no faces of greater dimension. The facet multiplicities in dimensions four and five are \((117,39)\) for \(C\), and \((132,34)\) for \(N\).

## Proof

**Finite exact face certificates.** Represent \(\sigma\) by the integer bitmask \(m(\sigma)=\sum_{v\in\sigma}2^v\). Construct every candidate \(m\) in the inclusive range \(0\leq m<2^{13}\); it is a face precisely when none of the twenty-six block masks \(b\) satisfies \(m\mathbin{\&}b=b\). This gives respectively \(1157\) and \(1152\) nonempty faces, and reconstructs the preceding face and facet counts. Direct enumeration of unordered quadruples of blocks with exactly six distinct points, each of multiplicity two, gives respectively thirteen and eight Pasch configurations.

**Acyclic matchings.** On the face poset with the empty simplex removed, use the following deterministic vertex orders:

\[
\begin{aligned}
\omega_C&=(11,1,2,10,0,8,5,4,7,12,3,9,6),\\
\omega_N&=(4,0,9,2,3,11,5,7,1,10,6,8,12).
\end{aligned}
\]

In this order, at each vertex \(v\), traverse the remaining faces in increasing order of cardinality and then increasing bitmask. If a face \(\sigma\) does not contain \(v\) and both \(\sigma\) and \(\sigma\cup\{v\}\) remain unmatched, pair and remove them. This uniquely determines \(568\) pairs for \(C\) and \(565\) for \(N\). For each codimension-one incidence, orient its arrow upward when matched and downward when unmatched. Kahn topological sorting exhausts all nonempty faces: all \(1157\) vertices and \(4550\) incidence arrows for \(C\), and all \(1152\) vertices and \(4520\) arrows for \(N\). Hence the matchings are acyclic.

The remaining critical cells are one vertex, four cells in dimension three and sixteen in dimension four for \(C\), and one vertex, two cells in dimension three and nineteen in dimension four for \(N\). There are no other critical cells.

**Integral attaching maps.** Use the increasing-vertex orientation on each simplex and the standard signed simplicial boundary. For each paired dimension-three face \(\alpha\subset\beta\) with dimension-four coface \(\beta\), substitute the relation \(\partial\beta=0\) to eliminate \(\alpha\); the coefficient of \(\alpha\) in \(\partial\beta\) is \(\pm1\). Because the gradient relation is acyclic, this signed reduction terminates and yields the integral Morse boundary between the critical four- and three-cells. With critical cells ordered by increasing bitmask, the following square submatrix for \(C\) is selected by zero-based four-cell column indices \((0,1,2,5)\):
\[
\begin{pmatrix}
-1&0&-1&0\\
0&0&-1&0\\
1&-1&0&-2\\
0&-1&0&-1
\end{pmatrix},\qquad\det=1.
\]
For \(N\), zero-based columns \((0,1)\) give the identity matrix of order two. Therefore the respective integral Morse boundary matrices \(\mathbb Z^{16}\to\mathbb Z^4\) and \(\mathbb Z^{19}\to\mathbb Z^2\) are split surjections, with free kernels of ranks twelve and seventeen. There are no critical dimensions one, two or five. The integral reduced homology is therefore free in degree four of those ranks and zero in every other degree.

**From integral homology to homotopy.** The connected Morse CW models consist of one vertex, three-cells and four-cells. Hence they are simply connected and have trivial second homotopy. The surjectivity just proved gives zero third homology; the first nonzero Hurewicz theorem implies their third homotopy groups also vanish. They are therefore three-connected, with \(\pi_4\cong H_4\) integrally. Represent an integral basis of \(H_4\) by maps of four-spheres; their wedge maps to the respective complex and induces an isomorphism on all integral homology groups. The simply connected homology version of Whitehead's theorem gives the claimed homotopy equivalences.

**Cyclic character.** The order-thirteen translation action preserves the blocks of \(C\), hence acts simplicially. Every nonidentity translation is a single thirteen-cycle on vertices; its only invariant subsets are the empty and full set, but the full set is not a face. Thus there are no nonempty invariant simplices, and its reduced Lefschetz number is minus one. Since the only nonzero reduced rational homology is in even degree four, the trace is minus one for every nonidentity translation; the identity trace is twelve. This is precisely the rational augmentation character.

## Verification

`verify.py` uses only Python 3 standard-library modules. It independently reconstructs all twenty-six blocks of both designs, checks uniqueness of unordered pairs, enumerates every subset, computes all facets and Pasch counts, checks every matching pair and every incidence arrow, and performs a complete topological sort. It computes the signed discrete-Morse boundary by recursive gradient-path substitution and verifies the stated unimodular minors. As a separate chain-level check, mod-two simplicial boundary ranks in degrees one through five are \((12,66,194,261,39)\) for \(C\) and \((12,66,194,261,34)\) for \(N\). The cyclic action is verified by enumerating all translation-fixed face sets. The actual executable and its recorded output are supplied together with this result; executing `python3 verify.py` produces `VERIFY_OK` on success.

## Relationship to prior work

Forbes, Grannell and Griggs (2004) introduced the independent-point-set enumeration problem in Steiner triple systems and gave closed formulas for the numbers of independent sets of cardinality up to eight. Their results supply enumerative background, not an integral homotopy classification or a symmetry module. Grannell, Griggs and Rosa (2000) explicitly describe the two order-thirteen systems and a Pasch switch. Forbes, Grannell and Griggs (2005) further study enumerative identities. Huggan, Huntemann and Stevens (2021/2022) study the Nofil impartial game on exactly this class of legal block-avoiding subsets and compute nim-values for both order-thirteen systems; their game-theoretic conclusions do not determine the homotopy type of the underlying face complex. The present finite Morse certificates add a complete homotopy classification for both systems; neither face-count formulas nor known matroid-independence shellability imply it. In particular, a block-free set for a Steiner triple system is a hypergraph-independent set, not a rank-three matroid-independent set.

Related publicly indexed findings for the thirteen-point projective-plane cap complex, affine-plane cap complexes and design-incidence neighborhood complexes have different forbidden triples, vertex sets or defining face conditions, and do not imply this classification.

## Limitations

This theorem concerns only the two isomorphism classes of Steiner triple systems of order thirteen, not all Steiner triple systems or arbitrary hypergraphs. The formula involving Pasch counts has only been established for these two cases. The statement about rational symmetry is restricted to the cyclic design's translation subgroup, not its full automorphism group. The classification is supported by exhaustive reproducible finite calculations; it has not undergone independent mathematical auditing. Although full-text primary material and relevant mathematical indexes were compared, unindexed prior equivalent coverage remains possible.

## References

- A. D. Forbes, M. J. Grannell, T. S. Griggs, *Independent Sets in Steiner Triple Systems*, Ars Combinatoria **72** (2004), 161–169. Publisher: https://combinatorialpress.com/ars-articles/volume-072-ars-articles/independent-sets-in-steiner-triple-systems/ . Full article: https://combinatorialpress.com/article/ars/Volume%20072/volume-72-paper-16.pdf .
- M. J. Grannell, T. S. Griggs, A. Rosa, *Three-line chromatic indices of Steiner triple systems*, Australasian Journal of Combinatorics **21** (2000), 67–84. https://ajc.maths.uq.edu.au/pdf/21/ocr-ajc-v21-p67.pdf .
- A. D. Forbes, M. J. Grannell, T. S. Griggs, *On independent sets*, Mathematica Slovaca **55** (2005), 375–377. https://dml.cz/handle/10338.dmlcz/132953 .
- M. A. Huggan, S. Huntemann, B. Stevens, *The combinatorial game Nofil played on Steiner triple systems*, Journal of Combinatorial Designs **30** (2022), 19–47. Open 2021 preprint https://arxiv.org/abs/2103.13501 .
