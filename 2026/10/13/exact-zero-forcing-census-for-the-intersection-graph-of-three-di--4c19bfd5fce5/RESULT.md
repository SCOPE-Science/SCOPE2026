# Exact zero forcing census for the intersection graph of three-dimensional ternary space

## Finding

Let \(V=\mathbb F_3^3\) and let \(\mathcal G(V)\) be the graph on the nonzero proper linear subspaces of \(V\), with distinct subspaces adjacent exactly when their intersection is nonzero. The complete zero forcing polynomial \(\mathcal Z(\mathcal G(V);u)=\sum_{S\text{ zero forcing}}u^{|S|}\) is
\[
\begin{aligned}
&1246986u^{13}+3599154u^{14}+4874220u^{15}+4326426u^{16}\\
&+2872233u^{17}+1515501u^{18}+651950u^{19}+229801u^{20}\\
&+65767u^{21}+14950u^{22}+2600u^{23}+325u^{24}+26u^{25}+u^{26}.
\end{aligned}
\]
In particular, the standard zero forcing number, real symmetric maximum nullity, and real symmetric minimum rank are all \(13\). There are exactly \(1{,}246{,}986\) minimum zero forcing sets. Under the natural \(\operatorname{PGL}(3,3)\)-action, these sets form \(254\) orbits, with orbit-size histogram
\[
234^1,\qquad936^9,\qquad1404^2,\qquad2808^{44},\qquad5616^{198}.
\]
Of the minimum sets, \(556{,}686\) contain six one-dimensional subspaces and \(690{,}300\) contain seven. These assertions concern this specific \(26\)-vertex graph, not an arbitrary field or dimension.

## Definitions and normalization

A zero forcing process colors a vertex black when it is the only remaining white neighbor of an already black vertex. A set is zero forcing if some sequence of these moves colors the whole graph. The maximum nullity \(M(G)\) maximizes the kernel dimension over real symmetric matrices whose off-diagonal nonzero entries are precisely the edges of \(G\), with arbitrary diagonal entries. The minimum rank is \(|V(G)|-M(G)\).

The thirteen one-dimensional subspaces are the points of the projective plane \(\operatorname{PG}(2,3)\), and the thirteen two-dimensional subspaces are its lines. The point vertices form an independent set, the line vertices form a clique, and a point is adjacent to a line exactly on projective incidence. Normalize every nonzero vector over \(\mathbb F_3\) by scaling its first nonzero coordinate to \(1\). In lexicographic order, the thirteen representatives are
\[
(0,0,1),(0,1,0),(0,1,1),(0,1,2),(1,0,0),(1,0,1),(1,0,2),
(1,1,0),(1,1,1),(1,1,2),(1,2,0),(1,2,1),(1,2,2).
\]
Vertices \(0,\ldots,12\) are the corresponding points; vertices \(13+j\), \(0\le j<13\), are the projective lines whose normalized defining normals are the same representatives in the same order.

## Exact minimum-size proof

Let \(B\) be the \(13\times13\) point-line incidence matrix in this ordering. Each point is on four lines, each line contains four points, and any two distinct points lie on exactly one common line. Hence
\[
BB^{\mathsf T}=B^{\mathsf T}B=3I+J.
\]
The real symmetric matrix
\[
C=\begin{pmatrix}I&B\\ B^{\mathsf T}&B^{\mathsf T}B\end{pmatrix}
=\begin{pmatrix}I\\ B^{\mathsf T}\end{pmatrix}
\begin{pmatrix}I&B\end{pmatrix}
\]
has rank exactly \(13\), because its upper-left block is \(I\). Its off-diagonal support is exactly the graph: zero between distinct point vertices, equal to incidence between points and lines, and nonzero between every two distinct line vertices (as \(B^{\mathsf T}B=3I+J\)). Thus \(M(\mathcal G(V))\ge13\). The standard inequality \(M(G)\le Z(G)\) yields \(Z(\mathcal G(V))\ge13\).

Conversely, the set of thirteen vertices
\[
\{0,1,2,3,4,5,8,13,14,15,17,18,20\}
\]
is zero forcing. One legal chronological sequence, verified directly against the incidence graph after every move, is
\[
0\to23,\ 1\to19,\ 4\to16,\ 8\to21,\ 3\to25,\ 5\to22,\ 2\to24,
\]
\[
14\to6,\ 16\to12,\ 18\to9,\ 15\to11,\ 20\to10,\ 13\to7.
\]
Consequently \(Z\le13\), proving \(Z=M=\operatorname{mr}=13\).

## Complete finite enumerations

The accompanying `enumerate.cpp` examines **each** of the \(2^{26}=67{,}108{,}864\) vertex subsets. For any initial black bit mask, it repeatedly finds a black vertex with exactly one white neighbor; the mask is zero forcing if and only if this closure reaches all 26 vertices. Enumerating all initial masks produces the coefficients displayed above, with no omitted cardinalities. Their **correct sum is**
\[
\sum_{k=13}^{26}[u^k]\mathcal Z(\mathcal G(V);u)=19{,}399{,}940.
\]
This is the number of *zero forcing* subsets, **not** the number of all subsets. Therefore the number of nonforcing subsets is exactly
\[
67{,}108{,}864-19{,}399{,}940=47{,}708{,}924.
\]

For the orbit census, the four explicit invertible \(3\times3\) matrices in `verify.py` induce automorphisms on projective points and, via inverse transpose, projective lines. Their generated action has order \(5616=|\operatorname{PGL}(3,3)|\). The enumerator applies their induced permutations to **every** one of the \(1{,}246{,}986\) minimum black sets and takes orbit closures. Exactly \(254\) orbits are found, with histogram as above. Both the orbit-weight identity
\[
234+9\cdot936+2\cdot1404+44\cdot2808+198\cdot5616=1{,}246{,}986
\]
and the point-occupancy identity \(556{,}686+690{,}300=1{,}246{,}986\) hold. The orbit statement is for the specified projective group, not an assertion that this is the full graph automorphism group.

The included `verify.py` reconstructs incidence directly over \(\mathbb F_3\), checks \(BB^{\mathsf T}=3I+J\), exact rational rank and off-diagonal support of \(C\), the legal forcing sequence, and the order of the generated projective group. The `enumerate.cpp` routine supplies the complete polynomial and orbit partition by finite exhaustive enumeration. The symbolic incidence argument establishes the exact minimum size without relying on exhaustive search; the complete polynomial and orbit census are finite statements for which complete enumeration is a proof.

## Relation to existing work and limits

The intersection graph of nontrivial submodules is a previously studied object (Akbari–Tavallaee–Khalashi Ghezelahmad; Yaraneri), including the specific nonzero-proper vertex convention. Jafari Rad and Jafari study the subspace-intersection graph of finite vector spaces, with clique, chromatic, domination and independence parameters. The general inequality \(M(G)\le Z(G)\) and the concept of a zero forcing polynomial are established prior work. The present result evaluates a natural exact finite case and classifies its projective symmetry orbits; it does not assert a formula for arbitrary field order or dimension. Reproducible finite enumeration is essential to the full coefficient and orbit statements, whereas the minimum-size equality has an additional exact linear-algebraic certificate.

The 2012 journal source on intersection graphs has a publication-month record but no precisely established first-public calendar day here; no such day is inferred. Work on graph invariants under alternative projective-incidence terminology may provide unindexed overlap.

## References

1. S. Akbari, H. A. Tavallaee, S. Khalashi Ghezelahmad, “Intersection Graph of Submodules of a Module,” *Journal of Algebra and Its Applications* **11** (2012), 1250019. DOI:10.1142/S0219498811005452.
2. E. Yaraneri, “Intersection Graph of a Module,” *Journal of Algebra and Its Applications* **12** (2013), 1250218; arXiv:1208.1897. DOI:10.1142/S0219498812502180.
3. N. Jafari Rad and S. H. Jafari, “A Note on the Intersection Graph of Subspaces of a Vector Space,” *Ars Combinatoria* **125** (2016), 401–407.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and Its Applications* **428** (2008), 1628–1648. DOI:10.1016/j.laa.2007.10.009.
5. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* **258** (2019), 35–48; arXiv:1801.08910.
