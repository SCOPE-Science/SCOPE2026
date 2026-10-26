# Sharp majority partitions and minimum \(q\)-cores in \(K_3\square K_q\square K_q\)

## Finding
For every integer \(q\ge4\), let \(G_q=K_3\square K_q\square K_q\). Its majority C-chromatic number, the largest number of nonempty colour classes in a vertex partition such that every vertex shares its colour with at least half of its neighbours, is exactly
\[
\overline\chi_{\ge}(G_q)=\left\lfloor\frac{3q}{2}\right\rfloor.
\]
More strongly, every nonempty vertex subset \(S\subseteq V(G_q)\) with \(\delta(G_q[S])\ge q\) has \(|S|\ge2q\). Equality holds **exactly** for coordinate rectangles in which one \(q\)-sized coordinate ranges over all its values, one other coordinate ranges over two values, and the remaining coordinate is fixed. There are exactly \(3q(q+1)\) such minimum-cardinality subsets.

## Assumptions and scope
All graphs are finite and simple. Vertices of \(G_q\) are triples \((x,y,z)\in[3]\times[q]\times[q]\), with adjacency when exactly one coordinate differs. Each vertex has degree \(2q\). A *majority C-colouring* is an arbitrary vertex colouring (not necessarily proper) in which every vertex has at least \(q\) neighbours of its own colour; colours used must have nonempty classes. Thus a colour class is precisely a nonempty induced subgraph of minimum degree at least \(q\). A *coordinate rectangle of type \(q\times2\times1\)* has one unrestricted coordinate of cardinality \(q\), another of cardinality two, and the last fixed. For \(q\ge4\), the unrestricted coordinate must be either the second or third coordinate.

## Proof
**Lemma (minimum dense cores).** Let \(q\ge4\) and \(\varnothing\ne S\subseteq V(G_q)\) satisfy \(\delta(G_q[S])\ge q\). Then \(|S|\ge2q\), with equality precisely for the rectangles described above.

Fix any \(v\in S\). Write \(A=N(v)\cap S\) and \(B=S\setminus(\{v\}\cup A)\), and \(k=|A|\ge q\). The neighbours of \(v\) lie on three coordinate cliques. Let \(a,b,c\) be the numbers belonging to \(A\) in these respective cliques, so \(0\le a\le2\), \(0\le b,c\le q-1\), and \(a+b+c=k\). A selected neighbour of \(v\) in a coordinate clique containing \(a_i\) selected neighbours has exactly \(a_i\) neighbours in \(\{v\}\cup A\). Indeed, these are \(v\) and the other \(a_i-1\) members of that clique; neighbours from other coordinate cliques of \(v\) differ from it in two coordinates and are not adjacent. Each such neighbour therefore needs at least \(q-a_i\) further neighbours in \(B\). Summing over \(A\) yields at least
\[
qk-a^2-b^2-c^2
\]
incidences between \(A\) and \(B\). Every vertex in \(B\) has at most two neighbours in \(A\): if its distance from \(v\) is exactly two there are precisely two candidate intermediate neighbours, and if its distance is three there are none. Consequently
\[
2|B|\ge qk-a^2-b^2-c^2.\tag{1}
\]

If \(k\ge2q-1\), then \(|S|\ge1+k\ge2q\). Equality is impossible in this case: equality would require \(k=2q-1\) and \(B=\varnothing\), but any selected neighbour of \(v\) has at most \(q-1\) neighbours within \(\{v\}\cup A\), contradicting the minimum-degree hypothesis.

Now assume \(q\le k\le2q-2\). Put \(r=k-q+1\), so \(1\le r\le q-1\). Since each of \(a,b,c\) is at most \(q-1\), convexity of the square function, or moving units from a smaller positive entry to a larger non-full entry, gives
\[
a^2+b^2+c^2\le(q-1)^2+r^2.\tag{2}
\]
This follows by maximizing the sum of three squares under the relaxed bounds \(0\le a,b,c\le q-1\) and their fixed sum \(k\); its maximal vector up to permutation is \((q-1,r,0)\). Equations (1)--(2) imply
\[
2|B|\ge(q-1)+r(q-r),
\]
and therefore
\[
|S|=1+k+|B|\ge2q+\frac{r(q+2-r)-(q+1)}2\ge2q.\tag{3}
\]
For \(1\le r\le q-1\) and \(q\ge4\), the quadratic \(r(q+2-r)\) takes its minimum \(q+1\) uniquely at \(r=1\): it is concave, its endpoint values are \(q+1\) and \(3(q-1)>q+1\). Thus equality in (3) forces \(r=1\), \(k=q\), and equality in (2), hence the directional populations of \(A\) are \((q-1,1,0)\) up to permutation. The full direction must be a \(q\)-sized coordinate, since the first direction has only two neighbours.

In this equality case \(|B|=q-1\), and (1) requires each vertex of \(B\) to meet exactly two members of \(A\). Write \(A\) as the \(q-1\) other points of a full coordinate line through \(v\), together with one point \(u\) on a perpendicular line through \(v\). The *only* vertices outside \(\{v\}\cup A\) adjacent to two members of \(A\) are the \(q-1\) cross-intersections obtained by changing both the full-line coordinate and the coordinate leading from \(v\) to \(u\). Hence \(B\) must consist of exactly these cross-intersections and \(S\) is the prescribed \(q\times2\times1\) rectangle. Conversely every such rectangle induces \(K_q\square K_2\), so every selected vertex has precisely \((q-1)+1=q\) selected neighbours. This proves the lemma.

**Census of minimum cores.** Choose which of the two \(q\)-sized coordinates is unrestricted. If the pair is chosen in the three-valued coordinate, there are \(2\binom32q=6q\) choices. If the pair is chosen in the other \(q\)-valued coordinate, there are \(2\binom q2\cdot3=3q(q-1)\) choices. For \(q\ge4\) these are all different, giving \(6q+3q(q-1)=3q(q+1)\).

**Upper bound on colours.** Every nonempty colour class has at least \(2q\) vertices by the lemma. Since \(|V(G_q)|=3q^2\), the number of colours is at most \(\lfloor3q^2/(2q)\rfloor=\lfloor3q/2\rfloor\).

**Sharp colour partition.** Regard the first two coordinates as a \(3\times q\) array; keep all values of the third coordinate together in each colour class. If \(q\) is even, pair the entries of each of the three rows into \(q/2\) adjacent pairs. This gives \(3q/2\) colours. If \(q\) is odd, pair the first \(q-1\) entries within each of the three rows, and place the three remaining entries of the same final column in one additional colour. This gives \(3(q-1)/2+1=\lfloor3q/2\rfloor\) colours. After lifting by the full third coordinate, every two-entry base block induces \(K_2\square K_q\) and has internal degree \(q\), while the one three-entry base block (when present) induces \(K_3\square K_q\) and has internal degree \(q+1\). Thus every vertex meets the majority requirement and the upper bound is attained. This proves the theorem.

## Verification
The accompanying standalone `verify.py` constructs and directly checks the colour partitions and all coordinate rectangles for every \(4\le q\le14\). It checks the local three-direction inequality for every permitted directional occupancy throughout the same range. An independent exhaustive enumeration of all \(397593\) vertex subsets of sizes one through six in the ternary three-cube confirms the boundary behaviour, including its \(54\) minimum cores; that balanced case is **not** claimed as new. Running `python verify.py` prints `VERIFY_OK` on success. These finite checks do not replace the all-\(q\) combinatorial proof above.

## Relationship to prior work
Bujtás, Dettlaff, Furmańczyk, Laskowska and Tuza [1, Proposition 14 and Open problem 2] derive general lower bounds for Cartesian products and explicitly ask for exact majority C-chromatic numbers of imbalanced three- and four-dimensional Hamming graphs. In this family their Proposition 14 yields a lower bound of three, whereas the present value grows as \(3q/2\). Lu [2, Theorem 1] solves balanced odd-dimensional Hamming graphs, not the unequal-factor family here; its concluding discussion explicitly asks for comparable results for unequal orders. The **size inequality** \(|S|\ge2q\) also follows from Lu [2, Lemma 4] by embedding \(G_q\) into the balanced three-cube \(K_q^{\square3}\): applying that lemma at threshold \(q=(q-1)+1\) gives \(f_q(q)=2q\). That previously available bound alone supplies the upper bound on colours, but neither the attaining imbalanced partition nor the complete equality classification and its census. The direct incidence proof here provides the latter rigid equality information. The 2012 alliance-partition literature [3] treats a related parameter and general regular-graph bounds; an equivalent special case under alliance terminology cannot be excluded solely from abstract-level access.

## Limitations
The exact formula and the minimum-core classification require \(q\ge4\) and the specific factor orders \((3,q,q)\). They do not solve the open problem for arbitrary imbalanced Hamming graphs. In particular, no uniqueness of the maximum whole-graph colour partition is asserted. Historical priority under the terminology of defensive-alliance partitions is a residual risk; independent mathematical validation and priority assessment have not been performed.

## References
[1] C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska and Z. Tuza, *Majority C-coloring in Cartesian products*, arXiv:2608.27669 (initial posting 2026-08-27; subsequent version 2026-09-17). https://arxiv.org/html/2608.27669v2

[2] ZeHua Lu, *Exact majority C-colourings of balanced Hamming graphs and grids*, arXiv:2609.31674 (initial posting 2026-09-16). https://arxiv.org/pdf/2609.31674

[3] *Alliance Partition Number in Graphs*, Ars Combinatoria 103 (2012), 519–529. https://combinatorialpress.com/ars-articles/volume-103-ars-articles/alliance-partition-number-in-graphs/

[4] C. Bujtás, M. Dettlaff, H. Furmańczyk and A. Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752 (2026-04-22). https://arxiv.org/abs/2604.20752
