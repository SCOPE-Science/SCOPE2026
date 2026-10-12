# Antipodal-pair criterion and complete resolving polynomial of the dodecahedral graph

## Finding
Let \(D\) be the twenty-vertex dodecahedral graph, presented as the generalized Petersen graph \(P(10,2)\). Its ten antipodal pairs partition its vertex set. A set of vertices \(S\subseteq V(D)\) is a resolving set for the ordinary shortest-path metric **if and only if** it meets at least three of these ten pairs. Consequently its resolving polynomial, enumerating *all* resolving vertex subsets by their cardinality, is
\[
R_D(z)=\sum_{\substack{S\subseteq V(D)\\S\ \mathrm{resolves}\ D}}z^{|S|}
=\sum_{j=3}^{10}\binom{10}{j}(2z+z^2)^j
=(1+z)^{20}-1-10(2z+z^2)-45(2z+z^2)^2.
\]
In particular, \(\dim(D)=3\), and its \(960\) metric bases are **exactly** the sets that choose one vertex from each of three different antipodal pairs. The scalar metric dimension three was known previously; the characterization and full enumerator are the result asserted here.

## Assumptions and scope
Use indices in \(\mathbb Z/10\mathbb Z\). The graph has vertices
\(u_0,\ldots,u_9,v_0,\ldots,v_9\) and undirected edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for every \(i\). Write \(d\) for the shortest-path metric. A set \(S\) resolves the graph when the vectors \((d(x,s))_{s\in S}\) differ for all distinct vertices \(x,y\), equivalently when it is not contained in any of the equalizer sets
\(E(x,y)=\{s\in V(D):d(s,x)=d(s,y)\}\).

For \(r\in\mathbb Z/5\mathbb Z\), define \(U_r=\{u_r,u_{r+5}\}\), \(V_r=\{v_r,v_{r+5}\}\). These ten pairs form the antipodal partition; \(x\mapsto\bar x\) sends each vertex to the other vertex of its pair. The polynomial counts labeled vertex subsets, not subsets up to graph automorphisms, and uses ordinary (not edge, strong, local, or mixed) metric resolution.

## Proof
**Step 1: determine the distances.** Breadth-first search from \(u_0\) and \(v_0\), using only the defining edges, gives these complete rows, with target index \(j=0,1,\ldots,9\):

| Distance | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(d(u_0,u_j)\) | 0 | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
| \(d(u_0,v_j)=d(v_0,u_j)\) | 1 | 2 | 2 | 3 | 3 | 4 | 3 | 3 | 2 | 2 |
| \(d(v_0,v_j)\) | 0 | 3 | 1 | 4 | 2 | 5 | 2 | 4 | 1 | 3 |

Rotation by one index preserves every adjacency, so the rows determine all distances by shifting indices. Each row satisfies \(d(x,\bar y)=5-d(x,y)\); this proves that the ten named pairs are exactly the diameter-five antipodal pairs. It also implies that an equalizer set, if nonempty, is a union of whole antipodal pairs.

**Step 2: classify all equalizer sets.** The following exhaustive table comes from comparing the three distance rows. An entry \(A+B\) means the union of the two *whole* antipodal pairs; a dash marks the excluded coincident-vertex case \(x=y\), while \(\varnothing\) means the empty equalizer. Subscripts of \(U\) and \(V\) are modulo five.

| Pair of vertices | \(j=0\) | \(j=1\) | \(j=2\) | \(j=3\) | \(j=4\) | \(j=5\) |
|---|---|---|---|---|---|---|
| \(E(u_0,u_j)\) | — | \(V_2+V_4\) | \(U_1+V_1\) | \(V_1+V_2\) | \(U_2+V_2\) | \(\varnothing\) |
| \(E(v_0,v_j)\) | — | \(U_2+U_4\) | \(U_1+V_1\) | \(U_1+U_2\) | \(U_2+V_2\) | \(\varnothing\) |
| \(E(u_0,v_j)\) | \(U_2+U_3\) | \(U_1+U_2\) | \(V_0+V_3\) | \(U_2+V_4\) | \(U_2+V_3\) | \(V_1+V_4\) |

The dihedral graph automorphisms \(u_i\mapsto u_{i+a}\), \(v_i\mapsto v_{i+a}\) and \(u_i\mapsto u_{-i}\), \(v_i\mapsto v_{-i}\) reduce every unordered pair of distinct vertices to one of these cases. For same-type pairs the index gap can be taken in \(\{1,2,3,4,5\}\), and for mixed pairs reflection reduces it to \(\{0,1,2,3,4,5\}\). Hence every equalizer is either empty or the union of **exactly two** antipodal pairs.

Moreover, *every unordered choice of two antipodal pairs* occurs as such an equalizer. To see this without a separate forty-five-case table, apply the induced rotations and reflections modulo five to these seven examples from the table: \(U_1+U_2\), \(U_2+U_4\), \(V_1+V_2\), \(V_2+V_4\), \(U_1+V_1\), \(U_2+V_3\), and \(U_2+V_4\). They represent respectively the same-type separations one and two, and the mixed-type separations zero, one, and two. Those are all dihedral orbits on unordered pairs of the ten antipodal classes.

**Step 3: characterize resolving sets.** If \(S\) meets three or more antipodal pairs, it is not contained in any \(E(x,y)\), since each equalizer is either empty or supported on two pairs. Thus every two vertices are distinguished by some sensor in \(S\). Conversely, if \(S\) meets at most two antipodal pairs, choose two different classes whose union contains \(S\) (possible even for \(S=\varnothing\)). By Step 2 there exist distinct vertices \(x,y\) with this union equal to \(E(x,y)\). Hence all sensors in \(S\) assign equal distances to \(x\) and \(y\), so \(S\) does not resolve. This proves the equivalence for *every* vertex subset.

**Step 4: enumerate.** For each antipodal pair, selecting one of its two vertices contributes \(2z\), selecting both contributes \(z^2\), and selecting neither contributes one. The theorem requires at least three occupied pairs, giving the first polynomial formula. Subtracting the cases of zero, one, and two occupied pairs from \((1+2z+z^2)^{10}=(1+z)^{20}\) gives the other. The first nonzero coefficient is \([z^3]R_D(z)=\binom{10}{3}2^3=960\), and the description of all minimum sets follows immediately.

## Verification
The standalone standard-library program `verify.py` constructs the defining graph, recomputes all twenty shortest-path distance rows, checks the displayed rows and antipodal complement identity, and exhaustively checks all \(190\) vertex-pair equalizers. Ten are empty and \(180\) comprise exactly two complete antipodal pairs; all \(45\) pairs of antipodal classes occur. It then compares direct distance signatures with the characterization on each of the \(6196\) subsets of cardinality at most four. Finally, it enumerates all \(2^{20}=1,048,576\) subsets and verifies the full coefficient formula, with \(436\) nonresolving sets and \(1,048,140\) resolving sets.

Reproduce from the accompanying file with `python3 verify.py`. The unrestricted statement is about one *fixed finite graph*: the complete distance table and equalizer classification are a proof, not a generalization from finite examples to an infinite family.

## Relationship to prior work
Javaid, Rahim, and Ali proved the previously known scalar result \(\dim(P(n,2))=3\) for \(n\ge5\); this includes the twenty-vertex graph here. Shao, Sheikholeslami, Wu, and Liu (2018) explicitly credit that theorem and analyze other generalized Petersen parameter families. Raza and Ji (2020) study the *mixed* metric dimension of \(P(n,2)\), which distinguishes both vertices and edges and therefore is a different invariant. These inspected results do not themselves supply the criterion for **all** ordinary resolving sets, or the exact polynomial and count \(960\). Previous graph-polynomial results for other families are not extended merely by renaming their parameters: the equalizer structure of the antipodal dodecahedron is the essential new argument.

## Limitations
The theorem concerns only the dodecahedral graph \(P(10,2)\); it does not state a formula for all generalized Petersen graphs or for edge, strong, mixed, or fault-tolerant metric resolution. The original 2008 Javaid–Rahim–Ali full text was not accessible during the priority comparison; its accessible abstract and subsequent paper's explicit statement credit the known scalar dimension, but the possibility of an older unnoticed equivalent full-resolving-set classification cannot be excluded. The full enumeration has received a self-review only; no independent mathematical audit or priority certification has been performed.

## References
1. I. Javaid, M. T. Rahim, and K. Ali, “Families of regular graphs with constant metric dimension,” *Utilitas Mathematica* **75** (2008), 21–33. Volume listing published 2008-05-09: https://utilitasmathematica.com/index.php/Index/issue/view/27 ; article record: https://utilitasmathematica.com/index.php/Index/article/view/566 .
2. Z. Shao, S. M. Sheikholeslami, P. Wu, and J.-B. Liu, “The Metric Dimension of Some Generalized Petersen Graphs,” *Discrete Dynamics in Nature and Society* (2018), article 4531958, https://doi.org/10.1155/2018/4531958 .
3. H. R. Hassan Raza and Y. Ji, “Computing the Mixed Metric Dimension of a Generalized Petersen Graph P(n, 2),” *Frontiers in Physics* **8** (2020), article 211, https://doi.org/10.3389/fphy.2020.00211 .
