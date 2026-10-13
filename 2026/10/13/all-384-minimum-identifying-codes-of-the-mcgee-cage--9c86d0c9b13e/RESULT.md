# All \(384\) minimum identifying codes of the McGee cage

## Finding

Let \(H\) be the McGee graph, the unique \(24\)-vertex cubic graph of girth \(7\), represented by the LCF chord pattern \([12,7,-7]^8\) on a Hamiltonian cycle. For a vertex set \(C\subseteq V(H)\), its **closed-neighborhood signature** at \(v\) is \(I_C(v)=C\cap N_H[v]\). An identifying code is a set \(C\) such that the \(24\) signatures are nonempty and pairwise different.

The smallest identifying codes have size \(11\), and there are exactly \(384\) of them. Under the complete automorphism group of \(H\), of order \(32\), they form precisely \(13\) orbits: two orbits of size \(16\) and eleven of size \(32\). The thirteen representatives below generate **every** minimum code by automorphisms. In particular, the optimal-code configurations are not a single symmetry class.

## Assumptions and scope

Label vertices \(0,1,\ldots,23\) modulo \(24\). Join \(i\) to \(i+1\) modulo \(24\), and also join \(i\) to \(i+s_i\) modulo \(24\), where \(s_i=12\) for \(i\equiv0\pmod3\), \(s_i=7\) for \(i\equiv1\pmod3\), and \(s_i=-7\) for \(i\equiv2\pmod3\). Duplicate undirected edges are included only once. This is the customary LCF presentation, with \(12\equiv-12\pmod{24}\). The resulting graph has \(36\) edges, degree \(3\) at each vertex, and girth \(7\).

A subset is represented by a \(24\)-bit nonnegative integer \(m\): vertex \(i\) belongs to the subset precisely when bit \(i\) of \(m\) is set. The statement concerns ordinary radius-one identifying codes (single-vertex identification), not the stronger identification of all vertex sets of sizes up to three.

## Proof

**Analytic lower bound.** Write \(k=|C|\). Since the graph is cubic, each selected vertex belongs to exactly four closed neighborhoods, and thus \(\sum_{v\in V(H)}|I_C(v)|=4k\). Pairwise distinct nonempty signatures can include at most \(k\) singleton signatures: a singleton can be only one of the \(k\) possible selected vertices. Consequently, at least \(24-k\) signatures have cardinality at least two, giving \(4k\ge k+2(24-k)=48-k\). Therefore \(5k\ge48\), so \(k\ge10\).

**Complete finite step.** The standalone C++ source `verify.cpp` loops over each of the \(\binom{24}{10}=1{,}961{,}256\) masks of weight \(10\) and each of the \(\binom{24}{11}=2{,}496{,}144\) masks of weight \(11\). These masks are uniquely enumerated by the increasing integers from zero through \(2^{24}-1\), restricted by their bit counts. For each mask the code applies two exact equivalent tests:

1. Directly form all \(24\) intersections \(C\cap N_H[v]\), and reject if any is empty or any two are identical.
2. Check that \(C\) intersects each of the \(24\) closed-neighborhood sets \(N_H[v]\) and each of the \(\binom{24}{2}=276\) symmetric differences \(N_H[u]\mathbin{\triangle}N_H[v]\). Nonempty intersections with these \(300\) sets are exactly the conditions of identification and distinction.

Both tests agree on **every** tested mask, giving zero codes of cardinality \(10\) and precisely \(384\) codes of cardinality \(11\). Together with the analytic lower bound, this proves both minimality and the complete count. This is a fully exhausted finite domain, not inference from a prefix of an enumeration.

**Automorphism classification.** The Python verifier independently constructs the same \(24\)-vertex LCF graph and exhaustively enumerates the edge-preserving bijections of its vertex set using exact graph-isomorphism backtracking. There are \(32\). Their vertex orbits are
\[
A=\{0,3,6,9,12,15,18,21\},\qquad B=V(H)\setminus A.
\]
Each of the \(384\) optimum masks is transformed by each of these \(32\) bijections. Their disjoint code orbits are precisely those in the table. Columns show the decimal mask of a representative, its code-orbit size, its number of selected vertices in \(A\), and its number of edges induced by the selected vertices. The representative together with the full graph automorphism group specifies every member of its orbit exactly.

| Representative mask | Orbit size | \(|C\cap A|\) | Edges in \(H[C]\) |
| ---: | ---: | ---: | ---: |
| 1919283 | 16 | 2 | 6 |
| 1462891 | 16 | 6 | 5 |
| 1140085 | 32 | 2 | 4 |
| 1664369 | 32 | 2 | 5 |
| 1403187 | 32 | 2 | 6 |
| 1402169 | 32 | 3 | 4 |
| 1134197 | 32 | 3 | 5 |
| 1395507 | 32 | 3 | 5 |
| 1395303 | 32 | 4 | 4 |
| 600041 | 32 | 4 | 5 |
| 697203 | 32 | 4 | 5 |
| 1219301 | 32 | 5 | 4 |
| 1225331 | 32 | 5 | 6 |

The code orbits are pairwise disjoint and their cardinalities sum to \(2\cdot16+11\cdot32=384\). The verifier checks these integer representatives and invariants exactly, rather than assuming that the invariants alone separate all orbits. Thus the table is an exhaustive classification up to symmetry.

## Verification

With Python at least version \(3.10\), a C++17 compiler, and the version of NetworkX described in `requirements.txt`, execute `python3 verify.py` in this directory. The script compiles the standalone `verify.cpp`, replays both exhaustive predicates on the complete size-\(10\) and size-\(11\) layers, checks all \(384\) successful masks in an independently constructed graph, enumerates every graph automorphism, and checks every orbit and representative. Its expected final output begins with `VERIFY_OK` and includes `gamma_ID=11`, `optimum_codes=384`, `automorphisms=32`, and `orbits=13`.

The finite proof consists of the explicit lower bound together with the exhaustive exact search of the only two possible smaller-or-optimum cardinalities. No randomized tests, floating-point approximations, unexamined larger graph orders, or unverified external certificates are used.

## Relationship to prior work

McGee introduced the \(24\)-vertex cubic girth-seven graph, and Biggs surveyed the extremal cage construction problem. Laihonen studied the existence of stronger \((1,\le\ell)\)-identifying codes in regular graphs of high girth; that existence question is different from the exact minimum cardinality and classification of ordinary identifying codes. The published geometric description of the McGee graph's \(32\)-element symmetry group and its \(8+16\) vertex-orbit split is also prior knowledge. The present result determines the exact optimum-code multiplicity and all symmetry classes, which are not entailed by those statements.

## Limitations

This is an exact finite theorem for the McGee graph, not a claimed formula for all cubic cages or all cubic girth-seven graphs. The exhaustive part covers exactly the two relevant cardinality layers after a proven lower bound, and the orbit classification uses exact finite graph automorphism enumeration. An earlier, unindexed enumeration of the same optimal configurations remains a priority risk. The complete text of Laihonen's paper was not accessible for direct comparison, although its accessible abstract concerns a stronger existence problem; this is a literature-access limitation, not an omitted condition of the mathematical proof.

## References

1. W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin **3** (1960), 149–152, DOI: 10.4153/CMB-1960-018-1.
2. N. Biggs, *Constructions for cubic graphs with large girth*, Electronic Journal of Combinatorics **5** (1998), A1, DOI: 10.37236/1386. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v5i1a1/pdf/.
3. T. Laihonen, *On cages admitting identifying codes*, European Journal of Combinatorics **29** (2008), 737–741, DOI: 10.1016/j.ejc.2007.02.016.
4. J. C. Baez, *McGee Graph*, AMS Visual Insight, 15 September 2015: https://blogs.ams.org/visualinsight/2015/09/15/mcgee-graph/.
5. E. W. Weisstein, *McGee Graph*, MathWorld: https://mathworld.wolfram.com/McGeeGraph.html.
