# Sharp retractional basis constants of finite Hamming boxes

## Finding
Let \(n\ge1\) and let \(q_1,\ldots,q_n\ge2\) be integers. Give
\[
H=\prod_{i=1}^{n}\{0,\ldots,q_i-1\}
\]
the Hamming metric \(d(x,y)=|\{i:x_i\ne y_i\}|\) and basepoint \(0\). Define \(\kappa(H)\) to be the infimum of \(\max_{1\le m\le |H|}\operatorname{Lip}(r_m)\) over enumerations \(H=\{v_1,\ldots,v_{|H|}\}\), with \(v_1=0\), and retractions \(r_m:H\to\{v_1,\ldots,v_m\}\) satisfying \(r_mr_l=r_{\min(m,l)}\). Then
\[
\boxed{\kappa(H)=\begin{cases}
1,&n=1\text{ or }(n=2,\ q_1=q_2=2),\\
2,&\text{otherwise}.
\end{cases}}
\]
The explicit minimizing retractions with bound \(2\) yield a Schauder basis with basis constant at most \(2\) for the **real** Lipschitz-free space \(\mathcal F(H)\), through the canonical linearizations. The exact minimum here concerns *retractional* bases, not all possible linear Schauder bases.

## Assumptions and scope
All alphabets are finite, each has a distinguished zero and at least one other letter, and coordinates are indexed by \(1,\ldots,n\). The graph of pairs at Hamming distance one is the Cartesian product of complete graphs; its shortest-path metric is \(d\). A retraction is required to fix every vertex of its image. The Lipschitz constant of a constant retraction is zero; since the last map is the identity and \(|H|\ge2\), always \(\kappa(H)\ge1\). The classification quantifies over **all** orders and compatible retractions, not merely those constructed below.

## Proof
**Step 1: A compatible family with constant at most two.** For a vertex \(x\), let \(S(x)=\{i:x_i\ne0\}\), and write the elements of \(S(x)\) increasingly. Order all vertices first by \(|S(x)|\), then lexicographically by their lists \(S(x)\), then lexicographically by the tuple of their nonzero letters in increasing coordinate order. Thus vertices in the same support stratum are ordered by their letter tuples. Let \(p(x)\) set to zero the last (largest-index) nonzero coordinate of \(x\ne0\). Repeated application of \(p\) leads to the origin, and each proper ancestor precedes its descendant.

For any initial segment \(V_m\) of this order, define \(r_m(x)\) to be the first vertex of \(V_m\) encountered in \(x,p(x),p^2(x),\ldots,0\). Every initial segment is closed under taking ancestors; therefore \(r_m\) fixes \(V_m\), has image exactly \(V_m\), and \(r_mr_l=r_{\min(m,l)}\).

For \(m=1\), the map is constant. For \(m\ge2\), choose the unique layer \(k\ge1\) such that all vertices of support size less than \(k\) have entered \(V_m\), and the currently entering layer has size \(k\). For integer \(j\ge0\), let \(\pi_j(x)\) retain just the first \(j\) nonzero coordinates of \(x\), or all of them if fewer than \(j\), setting the rest to zero. Then
\[
r_m(x)=\begin{cases}
\pi_k(x),&\pi_k(x)\in V_m,\\
\pi_{k-1}(x),&\pi_k(x)\notin V_m.
\end{cases}
\]
This includes the final full layer, for which every vertex is fixed.

Since the Hamming metric is the path metric of the unit-edge graph, it suffices to prove \(d(r_m(x),r_m(y))\le2\) when \(d(x,y)=1\). If \(x,y\) have the same support, they differ only in one nonzero letter, and their \(\pi_j\)-images differ in at most one position. Each retraction chooses its \(k\)- or \((k-1)\)-projection; a mixed choice can add at most one changed/deleted coordinate, so the images differ in at most two positions.

Otherwise, after exchanging vertices, write \(S(y)=S(x)\cup\{i\}\), where all shared nonzero letters agree. If \(|S(x)|\le k-2\), both vertices already belong to \(V_m\). If \(|S(x)|=k-1\), \(x\) is fixed and \(r_m(y)\) is either \(y\) or \(\pi_{k-1}(y)\), each within distance two of \(x\). Now suppose \(|S(x)|\ge k\). If \(i\) comes after the \(k\)-th element of \(S(x)\), both relevant projections of \(x\) and \(y\) agree, hence so do their images. Otherwise \(\pi_k(y)\) replaces the largest retained coordinate of \(\pi_k(x)\) by the new coordinate \(i\); therefore \(\pi_k(y)\) precedes \(\pi_k(x)\) by the support-lexicographic order. Either both \(k\)-projections lie in \(V_m\) (output distance two), or neither does (the two \((k-1)\)-projections differ in at most two coordinates), or only \(\pi_k(y)\) does. In the last case \(r_m(x)=\pi_{k-1}(x)\) and \(r_m(y)=\pi_k(y)\), which differ in the single inserted coordinate \(i\). The reverse mixed case is impossible because of the ordering. Thus every \(r_m\) is \(2\)-Lipschitz, uniformly in \(n\) and all alphabet sizes.

**Step 2: A sharp obstruction from the penultimate retraction.** Consider any enumeration, and let \(v\) be its last vertex. The next-to-last retraction fixes \(H\setminus\{v\}\) and sends \(v\) to some \(u\ne v\). If it had Lipschitz constant strictly less than two, the integer-valued Hamming metric would force \(d(u,w)\le1\) for **every** neighbor \(w\) of \(v\). This is impossible outside the stated exceptions:

- If \(u\) differs from \(v\) in just one coordinate and \(n\ge2\), change another coordinate of \(v\) to obtain a neighbor \(w\) with \(d(u,w)=2\).
- If \(u\) differs in at least two coordinates and \(n\ge3\), either change a coordinate not among these differences (if exactly two coordinates differ), or change one of the differing coordinates (if at least three differ). The resulting neighbor \(w\) has \(d(u,w)\ge2\).
- If \(n=2\), \(u\) differs from \(v\) in both coordinates, and some \(q_i\ge3\), change that coordinate of \(v\) to a third letter distinct from both its original value and the corresponding letter of \(u\). The resulting neighbor \(w\) has \(d(u,w)=2\).

Consequently \(\kappa(H)\ge2\) whenever \(n\ge3\) or \(n=2\) with a nonbinary factor. Combined with Step 1, this gives equality.

**Step 3: The two exceptional families.** If \(n=1\), the metric is equilateral. Enumerate its vertices starting at zero and send every vertex outside the current prefix to zero. These retractions commute and are all \(1\)-Lipschitz (or constant).

For the binary square, take the order \((0,0),(1,0),(0,1),(1,1)\). Let \(r_1\) be constant zero, let \(r_2\) fix the first two vertices and map both others to zero, let \(r_3\) fix the first three vertices and map \((1,1)\) to zero, and let \(r_4\) be the identity. Every map is nonexpansive on each unit edge, and the maps commute in the requisite nested way. Hence \(\kappa(H)=1\) in both exceptional cases.

**Step 4: The free-space consequence.** With basepoint zero, every \(r_m\) fixes zero and therefore induces a bounded linear operator \(\widehat r_m\) on \(\mathcal F(H)\) of norm \(\operatorname{Lip}(r_m)\). Its range is the span of the point masses on \(V_m\setminus\{0\}\); ranges increase by one dimension, the operators commute as \(\widehat r_m\widehat r_l=\widehat r_{\min(m,l)}\), and the last operator is the identity. Thus they are the partial-sum projections of an ordered linear basis, with norm at most two, or at most one in the two exceptional families. This proves the stated consequence without identifying the least basis constant among unrestricted linear bases.

## Verification
A standalone checker `VERIFY.py` constructs every prefix map from its ancestor rule, enumerates Hamming graph edges, checks all commuting identities and retraction identities, and checks the maximum edge Lipschitz ratio in heterogeneous boxes. Its supplied test families include dimensions one through five and alphabet tuples such as \((2,3,3,3)\). The checker also validates the separate nonexpansive chain on the binary square. These finite calculations support, but do not replace, Steps 1–3, which quantify over arbitrarily large finite boxes.

## Relationship to prior work
Hájek–Medina (2021, arXiv:2112.03095) define commuting retractional bases and obtain dimension-independent basis constants on nets and FDD grids. Their constructions are more general but do not provide the exact minimum for arbitrary finite Hamming boxes or identify its binary-square exception. In the earlier paper by Novotný (2019, arXiv:1905.13188), graph-circle lower obstructions and the failure of unconditional retractional bases for Euclidean nets concern different metric spaces and different conclusions. The present lower bound is an exact **penultimate-stage obstruction** specialized to the complete Cartesian graph metric; the upper bound is a uniform support-lexicographic ancestor construction.

## Limitations
The optimal constant is proved only within commuting **point-retractional** bases of finite full Cartesian products of equilateral alphabets. It does not assert the same optimal constant for all Schauder bases of their free spaces, for arbitrary subsets, other graph metrics, or infinite products. Finite checker runs cannot establish the all-dimensions theorem. The literature comparison is a best-knowledge comparison, not a proof that no unpublished or unindexed equivalent result exists; further independent assessment is warranted.

## References
1. P. Hájek and R. Medina, *Schauder bases in Lipschitz free spaces over nets in Banach spaces*, arXiv:2112.03095, first submitted 6 December 2021, https://arxiv.org/abs/2112.03095.
2. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, first submitted 30 May 2019, https://arxiv.org/abs/1905.13188.
