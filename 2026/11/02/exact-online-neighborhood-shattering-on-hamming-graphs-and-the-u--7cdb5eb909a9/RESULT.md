# Exact online neighborhood shattering on Hamming graphs and the unique VC gap

## Finding

Let \(d\ge1\) and \(q\ge2\) be integers. The Hamming graph \(H(d,q)\) has vertex set \([q]^d\), with adjacency defined by Hamming distance exactly one. Let \(\mathcal N_{d,q}=\{N(v):v\in[q]^d\}\) be its Boolean open-neighborhood concept class, queried by vertices. Then

\[
\operatorname{Ldim}(\mathcal N_{d,q})=
\begin{cases}
1,&d=1\text{ or }(d,q)=(2,2),\\
2,&(d,q)=(3,2),\\
3,&\text{otherwise}.
\end{cases}
\]

Every induced subgraph of any Hamming graph has open-neighborhood Littlestone dimension at most three. Comparing this theorem with the established all-parameter VC classification of Adler, Benediktsson, and Macpherson, the *only* full Hamming graph \(H(d,q)\) whose open-neighborhood concept class has strictly larger Littlestone dimension than VC dimension is \(H(2,3)\), with

\[
\operatorname{VCdim}(\mathcal N_{2,3})=2<3=\operatorname{Ldim}(\mathcal N_{2,3}).
\]

The VC classification itself is prior work and is not claimed as a new result.

## Assumptions and scope

The alphabet \([q]\) is any fixed \(q\)-element set; neither primality nor a field structure is required. Concepts are **open** neighborhoods: for a query word \(x\) and a concept center \(c\), the answer is one exactly when \(x\) and \(c\) differ in precisely one coordinate. An adaptive shattering tree of depth \(r\) is a complete binary tree whose internal nodes carry query words and whose every root-to-leaf sequence of prescribed answers is realized by some center. Repeatedly labeling a node by the same query cannot supply two nonempty branches after that query has been answered. Empty depth has dimension zero by convention. Only the graph's open-neighborhood concept family is studied; balls of larger radius are excluded.

## Proof

**Pairwise positive-intersection lemma.** Fix distinct query words \(x,y\). A center adjacent to both can exist only if their Hamming distance is one or two. If it is one, the common centers are the \(q-2\) other words on the unique coordinate line through \(x,y\). If it is two, the common centers are the two words obtained by changing one of those two differing coordinates to agree with the opposite query. If the distance is at least three, there is no common center. These statements follow by considering the coordinate in which a proposed center differs from each query.

For the first case, take any further query \(z\). Restricted to the common-center coordinate line, a distance-one neighborhood has either all but at most one common center, or at most one common center. Indeed, if \(z\) is on the line it is adjacent to every point of the line except itself, whereas a word off that line is adjacent to at most one point on the line. In the distance-two case there are only two candidate centers. Therefore, in *every* case, the concept class restricted to centers positive on two distinct queries has Littlestone dimension at most one: no query can divide those surviving centers into two groups each of size at least two.

**Universal upper bound.** A complete adaptive tree of depth four would have a root query \(x\), then (on its positive branch) some query \(y\) with a positive branch supporting a complete depth-two tree. Because that second query must genuinely split the surviving centers, \(y\ne x\). But the positive-positive candidate class is of Littlestone dimension at most one, contradicting the required depth two. Thus \(\operatorname{Ldim}\le3\) for every Hamming graph. Restricting centers and queries to vertices of an induced subgraph cannot increase Littlestone dimension, yielding the induced-subgraph statement.

**Sharp lower bounds.** `TREES.json` supplies fully explicit depth-three adaptive trees with center witnesses in \(H(2,3)\) and \(H(4,2)\). It also supplies a depth-two tree in \(H(3,2)\), and depth-one trees for \(H(1,2)\) and \(H(2,2)\). Every certificate contains exactly one witness for every leaf, with an independently checked distance-one answer at every internal node. Fixing additional coordinates and enlarging the alphabet embeds \(H(2,3)\) into every \(H(d,q)\) with \(d\ge2,q\ge3\), and embeds \(H(4,2)\) into every \(H(d,2)\) with \(d\ge4\). The full neighborhood incidence of either smaller graph occurs as a submatrix of that of the larger graph, so their adaptive lower bounds persist.

**Exceptional upper bounds.** For \(d=1\), each negative response to a query uniquely identifies its center, preventing a depth-two tree, while two distinct centers give a depth-one tree. In \(H(2,2)\) each positive query has only two possible centers, whereas a depth-two tree would require at least four centers in each root-answer branch. In \(H(3,2)\) each positive query has exactly three possible centers, whereas depth three would require four in each branch. The supplied smaller trees match these respective upper bounds. This establishes the displayed formula.

**Comparison with VC dimension.** Adler–Benediktsson–Macpherson, Theorem 4.7, establishes VC dimension three exactly when \(d\ge3,q\ge3\), or \(d\ge2,q\ge4\), or \(d\ge4,q\ge2\); its proof also excludes VC dimension three for \(H(2,3)\) and \(H(3,2)\). The small remaining VC dimensions are one for \(d=1\) and \(H(2,2)\), and two for \(H(2,3)\) and \(H(3,2)\). The displayed online formula therefore shows the sole strict difference is \(H(2,3)\). These static facts are cited, not reassigned as new discoveries.

## Verification

From this directory run `python3 verify_hamming.py`. It reads `TREES.json`, checks all internal query vectors and every leaf witness against an independent distance-one evaluator, tests an exhaustive finite recurrence for adaptive shattering on twenty parameter pairs, and enumerates static shattering on eleven parameter pairs. It additionally checks the two-positive-intersection obstruction in five small representative Hamming graphs. The recorded output is in `VERIFY_OUTPUT.txt`.

The finite tests corroborate the unrestricted mathematical upper bound and the complete explicit small-graph witness trees; they do not substitute for the proof for arbitrary \(d,q\).

## Relationship to prior work

The central focal source, Adler, Benediktsson, and Macpherson's 2020 preprint (published 2022), studies the **same edge relation and open-neighborhood family**. Its Theorems 4.6–4.7 give the exact static VC upper bound and the parameter ranges attaining three, and its Lemmas 4.1–4.5 describe the relevant local neighborhood geometry. It does not state or prove a Littlestone-dimension formula. Our positive-positive adaptive obstruction and the depth-three tree on \(H(2,3)\) add information not implied by the static bounds; in particular, the published statement \(\operatorname{VCdim}(H(2,3))=2\) cannot establish the online value three. Generic work on zero-set families of all linear combinations studies a different, unrestricted algebraic concept class and cannot supply this sparse distance-one classification directly.

## Limitations

The classification applies to the full Cartesian Hamming graph, with a universal *upper bound* only for its induced subgraphs. No exact dimension for each arbitrary induced subgraph, arbitrary code-restricted center set, closed neighborhood, or larger-radius sphere is claimed. A search of accessible papers and research records did not reveal the same exact adaptive classification; this is not a proof of historical uniqueness, and independent scientific validation is not claimed.

## References

1. Isolde Adler, Bjarki Geir Benediktsson, and Dugald Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, initially public 2020-07-31; accepted-version full text at https://eprints.whiterose.ac.uk/id/eprint/178584/1/Adler_Benediktsson_Macpherson.pdf; published in *Discrete Applied Mathematics* 312 (2022), 29–44, DOI:10.1016/j.dam.2021.09.017. Relevant material: Section 4, Lemmas 4.1–4.5, Theorems 4.6–4.8.
2. Vincent Guingona, Alexei Kolesnikov, Julie Nierwinski, and Richard Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (2021). This concerns full classes of nontrivial linear-combination zero sets, not Hamming distance-one neighborhood families.
