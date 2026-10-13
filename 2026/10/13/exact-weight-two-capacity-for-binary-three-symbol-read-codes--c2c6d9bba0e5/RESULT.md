# Exact weight-two capacity for binary three-symbol read codes

## Finding

For every integer \(n\ge 6\), let \(A_{3,2}(n,6)\) be the maximum cardinality of a set of binary length-\(n\) words, **each of Hamming weight exactly two**, whose minimum cyclic three-symbol read distance is at least six. Set \(m=\lfloor n/3\rfloor\). Then

\[
A_{3,2}(n,6)=
\begin{cases}
\dfrac{m(3m-1)}{2},& n=3m,\\[3pt]
\left\lfloor\dfrac{nm}{2}\right\rfloor,&n\equiv1,2\pmod3.
\end{cases}
\]

In particular, when \(n=3m\), the unrounded degree bound \(3m^2/2\) exceeds the optimum by \(m/2\); equivalently, the integer degree bound exceeds it by \(\lfloor m/2\rfloor\) edges. At the other lengths, the integer degree bound is attained. The proof supplies explicit optimum codes for every \(n\ge6\).

## Assumptions and scope

Coordinates are \(\mathbb Z/n\mathbb Z\), with all subscripts cyclic. For a word \(x\), its three-read vector is \(\pi_3(x)=((x_i,x_{i+1},x_{i+2}))_{i\in\mathbb Z/n\mathbb Z}\). For words \(x,y\), define \(d_3(x,y)\) as the number of positions where the corresponding triples differ. A code is any set (not necessarily linear) of distinct binary words, each with exactly two ones, and \(d_3(x,y)\ge6\) for all distinct members. The assumption \(n\ge6\) is necessary for the displayed all-length formula and for a six-unit read distance to be possible.

For vertices \(a,b\in\mathbb Z/n\mathbb Z\), let their cyclic separation be \(\delta_n(a,b)=\min\{(a-b)\bmod n,(b-a)\bmod n\}\).

## Proof

**1. Reduction to a locally separated graph.** Identify a binary word with ones at \(i,j\) with the unordered edge \(\{i,j\}\) on the vertex set \(\mathbb Z/n\mathbb Z\). Let \(H\) be the graph of all selected edges. If two distinct selected edges are disjoint, their binary words differ at four coordinates. Every set \(S\) of four coordinates satisfies
\[
\left|S\cup(S-1)\cup(S-2)\right|\ge\min\{n,|S|+2\}=6
\]
for \(n\ge6\): on a cycle, adjoining a one-position shift enlarges every nonempty proper set by at least one until all vertices are covered. Thus these two words automatically have three-read distance at least six.

If two distinct edges share endpoint \(v\), write them \(\{v,a\}\) and \(\{v,b\}\). The two words differ only at \(a,b\), each of which affects precisely three cyclic read windows. Those two sets of windows are disjoint exactly when \(\delta_n(a,b)\ge3\). Consequently the code condition is **equivalent** to
\[
\delta_n(a,b)\ge3\quad\text{for every vertex }v\text{ and all distinct }a,b\in N_H(v).
\tag{1}
\]
Equivalently, \(N_H(v)\) is independent in the square \(C_n^2\) of the cyclic graph; the code is an independent set in the two-token graph \(F_2(C_n^2)\).

**2. General upper bound.** A set of cyclically separated points satisfying (1) has size at most \(m=\lfloor n/3\rfloor\), because its successive cyclic gaps are each at least three. Hence \(\deg_H(v)\le m\) for every vertex. By the handshake identity,
\[
|E(H)|\le\left\lfloor\frac{nm}{2}\right\rfloor.
\tag{2}
\]

**3. Strict bound when \(n=3m\).** Each cyclically separated set of exactly \(m\) vertices then has all successive gaps exactly three, so it is one of the three residue classes \(R_0,R_1,R_2\) modulo three. Suppose \(H\) had a degree-\(m\) vertex in every residue class, and select \(v_i\in R_i\), for \(i=0,1,2\). For each \(i\), the whole neighborhood of \(v_i\) is one class \(R_{f(i)}\). Since no vertex is adjacent to itself, \(f(i)\ne i\). If \(f(i)=j\), the vertex \(v_j\) is a neighbor of \(v_i\), hence symmetry forces \(f(j)=i\). Thus \(f(f(i))=i\) for all three labels. A fixed-point-free involution cannot act on three elements, a contradiction.

Therefore degree \(m\) occurs in at most two residue classes, and all \(m\) vertices of at least one residue class have degree at most \(m-1\). It follows that
\[
2|E(H)|\le 3m^2-m,
\qquad |E(H)|\le\frac{m(3m-1)}2.
\tag{3}
\]

**4. Attainment at multiples of three.** Join every vertex of \(R_0\) to every vertex of \(R_1\), and join every two vertices within \(R_2\); include no other edges. This is the disjoint union \(K_{m,m}\sqcup K_m\). Every neighborhood lies in one residue class, so its vertices are separated by three. The number of edges is
\[
m^2+\binom m2=\frac{m(3m-1)}2,
\]
which attains (3).

**5. Attainment for the other residues.** Write \(m=2h\) or \(m=2h+1\). Let the basic undirected circulant graph have all edges of cyclic displacements
\[
\pm(3j-1),\qquad 1\le j\le h.
\tag{4}
\]
The basic graph is \(2h\)-regular. The displacements around any neighborhood are separated by at least three: within each positive or negative part they have gaps three, the gap across zero is four, and the middle gap between the two extreme parts is \(n-2(3h-1)\), which is at least three in all cases below.

If \(m=2h\) is even, the possible lengths outside the previous case are \(n=6h+1\) and \(n=6h+2\). The basic circulant itself is \(m\)-regular, with \(nm/2\) edges, meeting (2).

If \(m=2h+1\) is odd and \(n=6h+4\), add all \(n/2\) antipodal edges (cyclic displacement \(n/2=3h+2\)) to (4). The added neighbor is separated by at least three from the previous neighbors; this yields an \(m\)-regular graph attaining (2).

If \(m=2h+1\) is odd and \(n=6h+5\), let \(d=(n-1)/2=3h+2\). Since \(n\) is odd, \(\gcd(d,n)=1\), so the step-\(d\) edges form an odd Hamiltonian cycle. Add a maximum matching of \((n-1)/2\) edges from this cycle to the basic graph. Each vertex receives at most one new neighbor, at displacement \(+d\) or \(-d\), which is separated by at least three from the basic displacements in (4). Thus (1) continues to hold. The edge count is
\[
nh+\frac{n-1}{2}=\left\lfloor\frac{nm}{2}\right\rfloor,
\]
attaining (2). All possibilities \(n\ge6\) are covered. \(\square\)

## Verification

Run `python3 verify.py` with Python 3.8 or later and no third-party packages. It constructs the extremal graph and checks its edge cardinality and cyclic neighborhood separation for every length from 6 through 180. For lengths through 24 it independently computes every pairwise three-read distance by inspecting all cyclic windows, rather than relying on the graph reduction. An exhaustive independent maximum-independent-set search on the direct read-distance conflict graph confirms the optimum at each length 6 through 11. The expected output terminates in `VERIFY_OK`. These finite checks test the construction and reductions but do not constitute the all-length proof given above.

For orientation, the optimum values for lengths 6 through 14 are \(5,7,8,12,15,16,22,26,28\), respectively.

## Relationship to prior work

The b-symbol read metric and its basic Hamming-distance comparisons were developed by Yaakobi, Bruck, and Siegel [1]; their construction theorems address cyclic linear codes, interleaving, and minimum read distance, not the maximum size of the Hamming-weight-two layer. The Plotkin-like constructions of Yang, Li, and Feng [2] and the unrestricted linear MDS constructions of Ding, Zhang, and Ge [3] likewise do not impose this fixed-weight-two requirement. In particular, the linear MDS family with \(b=3\) and minimum read distance six in [3] provides no code-size optimum after restricting each word to two ones.

The two-token-graph equivalence is a natural reformulation. De Alba, Carballosa, Leaños, and Rivera [4, Theorem 1.3] determine \(\alpha(F_2(C_n))\), where the base graph is the **ordinary cycle**; here the base graph is its **square**, and the divisible-by-three degree deficit is different. Their general token-graph upper inequality recovers at most the coarse degree bound (2), not the sharp divisible-by-three formula and matching constructions. Verma, Patanker, and Singh [5] provide general three-symbol code-size bounds and bounds for prescribed *b-symbol weight*, which is distinct from prescribing the binary Hamming weight two. The exact piecewise formula above was not located in these inspected sources.

## Limitations

The result applies only to binary words with exactly two ones, cyclic read windows of length three, read distance at least six, and \(n\ge6\). It does not cover other weights, longer read windows, or a different minimum distance. The all-length proof is self-contained; finite computations are checks only. Publication novelty is subject to the possibility of an unindexed equivalent theorem in either the coding or token-graph literature; absence from searched records alone is not a uniqueness certificate. No independent validation is claimed.

## References

1. E. Yaakobi, J. Bruck, P. H. Siegel, “Constructions and Decoding of Cyclic Codes over b-Symbol Read Channels,” *IEEE Transactions on Information Theory* 62 (2016), 1541–1551. DOI: 10.1109/TIT.2016.2522434. Author-posted PDF: https://yaakobi.net.technion.ac.il/files/2016/04/21_Symbol_Pair_IT16.pdf . Earliest verified public date: 2016-01-27.
2. M. Yang, J. Li, K. Feng, “Construction of Cyclic and Constacyclic Codes for b-symbol Read Channels Meeting the Plotkin-like Bound,” arXiv:1607.02677 (2016-07-10), https://arxiv.org/abs/1607.02677 .
3. B. Ding, T. Zhang, G. Ge, “Maximum Distance Separable Codes for b-Symbol Read Channels,” arXiv:1609.09236 (2016-09-29), https://arxiv.org/abs/1609.09236 .
4. H. de Alba, W. Carballosa, J. Leaños, L. M. Rivera, “Independence and Matching Numbers of Some Token Graphs,” arXiv:1606.06370 (2016-06-21), https://arxiv.org/abs/1606.06370 .
5. G. K. Verma, N. Patanker, A. K. Singh, “Code Size Constraints in b-Symbol Read Channels: A Bound Analysis,” arXiv:2504.10088 (2025-04-14), https://arxiv.org/abs/2504.10088 .
