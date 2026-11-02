# The complete \(2\)-packing polynomial and eight optimal orbits of \(K(3r-3,r)\)

## Finding
For every integer \(r\ge11\), put \(n=3r-3\) and let \(K(n,r)\) be the Kneser graph of all \(r\)-subsets of \([n]\), with adjacency meaning disjointness. A \(2\)-packing is a vertex family whose members have mutually disjoint closed graph neighborhoods. Write
\[
\mathcal P_r(z)=\sum_{S\text{ a }2\text{-packing of }K(n,r)}z^{|S|}.
\]
The **complete enumerator**, not just its degree, is
\[
\boxed{\mathcal P_r(z)=1+\binom nr z+B_rz^2+C_rz^3},
\]
where
\[
B_r=\tfrac12\binom nr\left[r\binom{2r-3}{r-1}+\binom r2\binom{2r-3}{r-2}\right]
\]
and \(C_r=\sum_{(k,t)\in\mathcal I} E_{r;k,t}\), with
\[
\mathcal I=\{(0,0),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1),(3,2)\}.
\]
For each \((k,t)\in\mathcal I\), choose any ordering \((p_{12},p_{13},p_{23})\) of \(k\) copies of \(2\) and \(3-k\) copies of \(1\). Set
\[
a=r-p_{12}-p_{13}+t,\quad b=r-p_{12}-p_{23}+t,\quad c=r-p_{13}-p_{23}+t,\quad h=k-t.
\]
Then
\[
\boxed{E_{r;k,t}=\frac{n!\binom3k}{6\,t!\,h!\,(p_{12}-t)!\,(p_{13}-t)!\,(p_{23}-t)!\,a!\,b!\,c!}.}
\]
The formula is independent of the chosen ordering of the \(p\)'s. The eight positive integers \(E_{r;k,t}\) are exactly the eight orbit sizes of maximum \(2\)-packings under permutations of \([n]\): \(k\) is the number of the three pairwise intersections of size two, and \(t\) is the triple-intersection size. In particular, every maximum packing has three vertices, there are exactly eight isomorphism types under the natural coordinate-permutation action, and the total number of maximum packings is \(C_r\). For \(r=11\), \(C_{11}=9,693,705,696,717,042,000\).

## Assumptions and scope
All sets are distinct subsets of the labeled ground set \([n]\); packings are unordered collections. The polynomial counts labeled packings once each. \(K(n,r)\) is the ordinary simple undirected Kneser graph. The stated original enumerative contribution is for every \(r\ge11\); its ingredients also give computations for smaller indices, but the threshold avoids parameter ranges included in earlier finite coding-theory classification studies. No claim is made that the already known formula \(\rho_2(K(3r-3,r))=3\) is new.

## Proof
**1. The exact pair condition.** Two distinct \(r\)-subsets \(A,B\) cannot occur together in a \(2\)-packing if they are disjoint, since then they are adjacent. If \(|A\cap B|\ge3\), their union has size at most \(2r-3\), hence its complement in \([3r-3]\) contains an \(r\)-subset disjoint from both. Thus they have a common neighbor, and are forbidden. Conversely, if \(1\le|A\cap B|\le2\), they are not adjacent and their union's complement has size \(r-3+|A\cap B|\le r-1\), so no common neighbor exists. Therefore distinct members of a \(2\)-packing are characterized by \(1\le|A\cap B|\le2\). This recovers the condition of Brešar--Cornet--Dravec--Henning, Observation 4.1.

**2. There are at most three members.** For any four \(r\)-sets meeting in at most two points pairwise, let \(d_x\) be the number containing coordinate \(x\). Since \(d_x-1\le\binom{d_x}2\) for positive integer \(d_x\), their union size is at least \(4r-\sum_{i<j}|A_i\cap A_j|\ge4r-12\). But \(4r-12>3r-3=n\) when \(r\ge10\), a contradiction. Three feasible blocks exist: allocate a separate common coordinate to each of their three pairs and \(r-2\) private coordinates to each block, using exactly \(3+3(r-2)=3r-3\) coordinates. Thus the maximum packing size is three; this fact was already established in Proposition 4.2 of the cited Kneser paper.

**3. Coefficients of degrees one and two.** There are \(\binom nr\) individual vertices. Fixing \(A\), the number of eligible \(B\) with intersection size \(j\in\{1,2\}\) is \(\binom rj\binom{n-r}{r-j}\). Divide ordered pairs by two. This gives \(B_r\).

**4. Venn atoms for the triple enumerator.** Fix an *ordered* triple \((A_1,A_2,A_3)\) with pairwise intersection sizes \(p_{12},p_{13},p_{23}\in\{1,2\}\) and triple intersection size \(t\). The three pair-only Venn atoms have sizes \(p_{ij}-t\); the three private atoms have sizes \(a,b,c\) as displayed; and the exterior atom has size
\[
h=n-(|A_1\cup A_2\cup A_3|)=p_{12}+p_{13}+p_{23}-t-3=k-t.
\]
All atom sizes are nonnegative precisely for the eight indicated choices of \((k,t)\) (the private atom sizes are positive for \(r\ge11\)). Choosing which labeled coordinates belong to each of the eight atoms gives the multinomial number \(n!/[t!h!\prod_{i<j}(p_{ij}-t)!\,a!b!c!]\). There are \(\binom3k\) ways to place the two-valued intersections among the three labeled pairs. Every unordered packing has exactly \(3!\) orders, giving \(E_{r;k,t}\) and \(C_r\).

**5. Exactly eight permutation orbits.** Permutations of the ground coordinates preserve all Venn atom sizes and hence the unordered pair-intersection multiset and triple-intersection size \((k,t)\). Conversely, any two ordered triples with identical Venn atom cardinalities are mapped to one another by a permutation of \([n]\), and reordering the three blocks accounts for the placement of the \(k\) doubled intersections. Thus the eight feasible \((k,t)\) are exactly the eight orbits, of the sizes just computed. This proves the polynomial and classification for every \(r\ge11\).

## Verification
The accompanying standalone `verify.py` evaluates the Venn-multinomial formula using arbitrary-precision integers, compares it against an independently derived anchored-two-block count for every \(4\le r\le25\), and directly enumerates all admissible two- and three-block families from the \(126\) vertices of \(K(9,4)\). The direct check returns \(6,300\) pairs and \(163,800\) triples, subdivided into the eight predicted patterns, agreeing exactly with the algebraic enumerator. The \(r=11\) output is \(9,693,705,696,717,042,000\). The program terminates with `VERIFY_OK`. These computations check finite instances; the infinite theorem follows from the Venn-atom and four-block arguments.

## Relationship to prior work
Brešar, Cornet, Dravec, and Henning introduced the stated diagonal in their study of Kneser \(2\)-packings. Their Observation 4.1 gives the same pairwise intersection criterion, and Proposition 4.2 already proves that the maximum size is \(3\) for \(r\ge10\). These results are inputs, not new conclusions. Neither result evaluates the entire packing polynomial or enumerates the maximum families and their eight coordinate-permutation orbits. Earlier coding-theory literature studies length-\(n\), weight-\(r\) binary codes with minimum distance \(2r-4\), which correspond to the *upper* intersection requirement \(|A_i\cap A_j|\le2\); the Kneser packing additionally requires positive pairwise intersection. Östergård's 2010 optimal-code classification explicitly covers only specified smaller-length ranges (in particular, \(n\le28\) at distance \(18\)), while the present theorem starts at \(n=30\). Smith--Hughes--Perkins (2006) tabulate maximum cardinalities and constructions for longer constant-weight codes; those tables are not cardinality-distribution enumerators and do not imply the eight-orbit count. The standard bound/code data are not claimed as new.

## Limitations
The enumerator concerns only the diagonal \(n=3r-3\) and \(r\ge11\), and does not classify maximum packings on other diagonals. The eight orbits refer to permutations of the labeled ground coordinates; no classification under other notions of code equivalence is claimed. Earlier unpublished or unindexed counting results using binary codes or Venn profiles could overlap. A full historical priority guarantee is not provided. An independently performed mathematical audit is not asserted.

## References
1. B. Brešar, M. G. Cornet, T. Dravec, and M. A. Henning, *k-Domination invariants on Kneser graphs*, arXiv:2312.15464, first posted 2023-12-24; see Observation 4.1 and Proposition 4.2. https://arxiv.org/abs/2312.15464
2. M. G. Cornet and P. Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603 (2023). https://arxiv.org/abs/2308.15603
3. P. R. J. Östergård, *Classification of Binary Constant Weight Codes*, IEEE Transactions on Information Theory 56 (2010), 3779–3785. https://doi.org/10.1109/TIT.2010.2050922
4. D. H. Smith, L. A. Hughes, and S. Perkins, *A New Table of Constant Weight Codes of Length Greater than 28*, Electronic Journal of Combinatorics 13 (2006), #A2. https://doi.org/10.37236/1162
5. A. E. Brouwer, *Bounds for binary constant weight codes*, online tables. https://aeb.win.tue.nl/codes/Andw.html
