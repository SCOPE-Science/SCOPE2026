# Sharp shattering thresholds for fixed-dimensional faces of Boolean cubes

## Finding

Let \(d\ge k\ge3\) be integers and let \(Q_d=\{0,1\}^d\). Denote by \(\mathcal F_{d,k}\) the set system on the **vertices** of \(Q_d\) consisting of the vertex sets of all its \(k\)-dimensional coordinate faces. A face fixes exactly \(d-k\) coordinates and leaves the remaining \(k\) free. Queries are vertex-membership tests. The following statements hold.

**Sharp static threshold and complete maximum-support classification.** Every VC-shattered support has cardinality at most \(k\). A support of cardinality \(k\) is VC-shattered if and only if \(d\ge2k-2\) and, after permutation and independent complementations of coordinates, it is the set of the first \(k\) unit vectors \(\{e_1,\ldots,e_k\}\). Thus
\[
\operatorname{VCdim}(\mathcal F_{d,k})=k\quad\Longleftrightarrow\quad d\ge2k-2.
\]
The number of distinct shattered supports of cardinality \(k\) is exactly
\[
\begin{cases}
0,&d<2k-2,\\
2^d\binom dk,&d\ge2k-2.
\end{cases}
\]

**Sharp universal online ceiling and a stable-range equality.** For all \(d\ge k\ge3\),
\[
\operatorname{Ldim}(\mathcal F_{d,k})\le k+1.
\]
For every \(d\ge2k-1\), equality holds. Consequently, for every \(k\ge3\) and \(d\ge2k-1\),
\[
\operatorname{VCdim}(\mathcal F_{d,k})=k,
\qquad
\operatorname{Ldim}(\mathcal F_{d,k})=k+1.
\]
For the first nontrivial instance \(k=3\), the dimensions are \((3,3)\) at \(d=4\) and \((3,4)\) at \(d=5\): the latter is the first strict static/adaptive gap among three-dimensional faces. No exact Littlestone formula is asserted for the remaining interval \(k\le d<2k-1\).

## Assumptions and scope

A coordinate face is determined by a free-coordinate set \(K\subseteq[d]\), \(|K|=k\), and a fixed bit assignment on \([d]\setminus K\). Equivalently, the class is the set of Boolean conjunctions of **exactly** \(d-k\) distinct consistent signed literals, since each fixed cube coordinate imposes one positive or negative literal. This exact-width restriction matters: adjoining shorter or longer conjunctions changes the hypothesis class. The class contains exactly \(2^{d-k}\binom dk\) distinct hypotheses; it does not contain the empty set unless that set is itself a face (which never happens here). A support \(S\subseteq Q_d\) is VC-shattered if every \(T\subseteq S\) equals \(F\cap S\) for some \(F\in\mathcal F_{d,k}\). Its Littlestone dimension is the greatest depth of a complete adaptive binary vertex-query tree with a face consistent with every root-to-leaf label sequence. Every statement has integer quantifiers \(d\ge k\ge3\), with the stronger range restrictions stated explicitly.

## Proof

**Lemma 1: private coordinates.** Let \(S\) be a shattered support with \(|S|=m\ge3\). Since the all-positive trace exists, \(S\) lies in some \(k\)-face and hence varies in at most \(k\) coordinates. For any \(s\in S\), a face containing \(S\setminus\{s\}\) and excluding \(s\) must fix some coordinate on which all other points of \(S\) agree and \(s\) differs. Call it a private coordinate of \(s\). When \(m\ge3\), no coordinate can be private for two different points: the other points would force contradictory common values. The private coordinates are distinct, so \(m\le k\). In particular, the VC dimension is at most \(k\).

**Lemma 2: rigidity and the sharp ambient threshold.** Suppose a shattered support has \(k\) points. The proof above supplies \(k\) distinct private coordinates, and the all-positive face allows at most \(k\) varying coordinates; thus these are all the varying coordinates. Independent bit complementations and a coordinate permutation put the support into the form \(S=\{e_1,\ldots,e_k\}\), with remaining coordinates zero. To realize the trace consisting of \(e_1,e_2\) alone, a containing face must leave coordinates 1 and 2 free and must fix the remaining \(k-2\) private coordinates to zero. Its \(k\) free coordinates therefore require at least \(k-2\) coordinates outside the initial \(k\). Hence \(d-k\ge k-2\), or \(d\ge2k-2\). This argument also proves that **every** maximum shattered support has the claimed shape.

Conversely assume \(d\ge2k-2\) and take \(S=\{e_1,\ldots,e_k\}\). For any nonempty subset \(T\subseteq S\) of size \(t\ge2\), free the \(t\) coordinates indexed by \(T\), together with any \(k-t\) coordinates outside \([k]\), and fix all remaining coordinates to zero. This face meets \(S\) exactly in \(T\). For a singleton \(T=\{e_i\}\), fix coordinate \(i\) to one and free any \(k\) other coordinates; this is possible since \(d\ge k+1\), and its trace is \(T\). For the empty trace, fix one coordinate outside \([k]\) to one and free any \(k\) other coordinates. Thus \(S\) is shattered. Cube automorphisms preserve shattering, proving the full shape characterization. Its representation is unique for \(k\ge3\): each varying coordinate has a unique minority point, and its majority value determines the background bit. Choosing the \(k\) varying coordinates and the \(d\) background bits gives \(2^d\binom dk\) supports.

**Lemma 3: online upper bound.** Fix any first queried vertex \(x\). In the positive version space every face contains \(x\). Along any further all-positive sequence of internal nodes of a shattered tree, a new query \(y\) must strictly enlarge the set of coordinates varying over the already positively queried points: if it did not, \(y\) would lie in their smallest coordinate face and would belong to every remaining hypothesis, leaving an empty negative branch. This set of varying coordinates has size at most \(k\). Therefore the positive version space has Littlestone dimension at most \(k\). No root can have two children both supporting depth \(k+1\), so \(\operatorname{Ldim}(\mathcal F_{d,k})\le k+1\).

**Lemma 4: the online lower bound.** It suffices to treat \(d=2k-1\), since fixing additional ambient coordinates to zero embeds this instance into every larger dimension. Query the all-zero vertex. The positive version space consists of faces through zero, indexed by their free-coordinate \(k\)-subsets \(K\subseteq[2k-1]\). For such a face, querying the binary vector with ones on a coordinate set \(A\) returns positive exactly when \(A\subseteq K\). We construct a complete tree of depth \(k\) for this positive branch.

First query \(e_1\). In its positive child, \(1\in K\), and the remaining \(k-1\) positions of \(K\) form an arbitrary \((k-1)\)-subset of a \((2k-2)\)-set. Queries at any \(k-1\) distinct remaining unit vectors realize all \(2^{k-1}\) patterns, by padding the chosen indices outside the queried positions. In its negative child, \(1\notin K\). Let \(M\) be the complement of \(K\) among the remaining \(2k-2\) coordinates. Then \(|M|=t=k-2\ge1\), and membership of a query with ones on \(A\) means \(M\cap A=\varnothing\). Query the vector with ones in two selected remaining coordinates \(a,b\). In the positive child, \(M\) avoids \(a,b\), so it ranges over all \(t\)-subsets of the other \(2t\) coordinates; \(t\) singleton tests realize all depth-\(t\) binary patterns. In the negative child, restrict to the subclass with exactly one of \(a,b\) in \(M\) and \(t-1\) elements from the other \(2t\). A singleton test at \(a\), followed by \(t-1\) singleton tests outside \(\{a,b\}\), realizes every depth-\(t\) pattern. Both children therefore have depth \(t\), so the negative child of the first \(e_1\) query has depth \(t+1=k-1\). The positive child has depth \(k-1\) too. Hence the all-zero vertex's positive version space supports depth \(k\).

The negative version space contains, as a subfamily, all \(k\)-faces lying in the opposite coordinate facet with first bit one. That facet is a copy of \(Q_{2k-2}\), whose \(k\)-face family has VC dimension \(k\) by Lemma 2. Its fixed shattered support supplies a complete *nonadaptive* depth-\(k\) query tree in the negative branch. Both branches of the all-zero root therefore have depth \(k\), yielding a complete depth-\(k+1\) tree. This meets Lemma 3's upper bound.

For \(k=3\), \(d=3\) has a single full-cube face, hence online dimension zero. At \(d=4\) there are only \(2^{4-3}\binom43=8\) faces, so online dimension is at most three, and Lemma 2 gives VC dimension three. At \(d=5\), Lemmas 2 and 4 give dimensions three and four, respectively.

## Verification

The included `verify.py` independently builds every coordinate face as a vertex bit mask. It exhaustively enumerates all size-three supports for \((d,k)=(4,3)\) and \((5,3)\), obtaining exactly \(64\) and \(320\) shattered supports, as predicted by \(2^d\binom d3\). It tests the constructed unit-vector supports at additional parameter pairs, checks a full depth-four tree for \((5,3)\) against the separately stored `certificate.json`, and checks both root branches at representative larger parameters. The program verifies all certificate paths and terminal hypotheses directly from face membership. Finite experiments check boundaries, not universal quantifiers; the universal statements follow from the four lemmas.

Run from this directory with `python3 verify.py` (Python standard library only). The certificate is JSON and all paths and dependencies are relative to these two files.

## Relationship to prior work

The first publicly posted source used for this direction is Filmus–Hirsch–Kurz–Ihringer–Riazanov–Smal–Vinyals, *Irreducible Subcube Partitions*, arXiv:2212.14685 (first submission 2022-12-30). Its introduction and homogeneous-partition section study **disjoint partitions** into equal-codimension subcubes; they do not determine shattering under vertex membership for the full collection of all fixed-dimensional faces. Chepoi–Knauer–Philibert, *Two-dimensional partial cubes*, arXiv:1906.04492 (2019), studies the VC dimension of set families viewed as hypercube vertices and their isometric inclusion graphs. That primal set-family invariant is not the dual face-versus-vertex incidence system used here. Guingona–Kolesnikov–Nierwinski–Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (2021), proves equality for all nontrivial linear-combination zero sets; fixed-rank coordinate faces form a different, restricted conjunction family. Standard teaching treatments of conjunctions of up to a specified number of Boolean literals (for example, Mitchell, *Machine Learning*, Chapter 7) allow a variable number of literals; their usual VC-dimension estimate for that larger hypothesis class does not imply this fixed-width saturation threshold, maximal-support count, or exact adaptive depth. The results here use only the conventional definitions of VC and Littlestone dimension; none of these cited special results is needed in the proof.

## Limitations

The theorem does not provide exact Littlestone dimensions for every pair with \(k\le d<2k-1\), nor exact VC dimensions below the sharp saturation threshold, except the zero and small cases explicitly noted. The result does not concern arbitrary affine \(k\)-flats over finite fields, all-dimensional face families, or subcube partitions. The literature comparisons are limited to accessible records and materially inspected sources; particularly, a differently worded result about exact-width signed conjunctions or uniform Boolean terms is a residual priority risk. The proof and finite verification have not received an independent mathematical audit.

## References

1. Y. Filmus, E. A. Hirsch, S. Kurz, F. Ihringer, A. Riazanov, A. Smal, M. Vinyals, *Irreducible Subcube Partitions*, arXiv:2212.14685, first public submission 2022-12-30; *Electronic Journal of Combinatorics* 30(3), 2023, P3.29. https://arxiv.org/abs/2212.14685
2. V. Chepoi, K. Knauer, M. Philibert, *Two-dimensional partial cubes*, arXiv:1906.04492, first public submission 2019-06-11; *Electronic Journal of Combinatorics* 27(3), 2020, P3.29. https://arxiv.org/abs/1906.04492
3. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first public submission 2021-09-10. https://arxiv.org/abs/2109.04805
4. T. M. Mitchell, *Machine Learning*, Chapter 7 (1997), illustrative VC calculation for conjunctions of up to a varying number of literals; used only as background for the distinction from exact-width classes.
