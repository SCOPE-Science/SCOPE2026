# Complete census of ternary length-four MDS symbol-pair codes

## Finding
For ternary length-four symbol-pair codes with minimum pair-distance \(4\), the Singleton maximum size is \(9\), and there are exactly \(8{,}784\) labeled maximum codes. Under the natural isometry subgroup \(G=(S_3)^4\rtimes D_8\), acting by independent symbol permutations in each coordinate and by dihedral symmetries of the cyclic coordinate order, the maxima split into exactly \(11\) orbits of sizes \(36,72,144,324,432,648,648,1296,1296,1296,2592\). Exactly \(252\) maximum codes are affine two-flats in \(\mathbb F_3^4\); they are precisely the three orbits of sizes \(36,72,144\), so the other \(8{,}532\) maxima are non-affine.

An explicit non-affine maximum code is
\[
\{{0000,0101,0202,1010,1122,1221,2020,2112,2211\}}.
\]
It contains \(0000\), but \(1122+1221=2010\) in \(\mathbb F_3^4\) and \(2010\) is not a codeword, so this witness is not linear and hence is not affine.

## Assumptions and scope
The alphabet is \(\mathbb F_3=\{{0,1,2\}}\). For \(x,y\in\mathbb F_3^4\), indices are cyclic modulo \(4\), and the symbol-pair distance is
\[
d_p(x,y)=\left|\left\{{i\in\mathbb Z/4\mathbb Z:(x_i,x_{{i+1}})\ne(y_i,y_{{i+1}})\right\}}\right|.
\]
A code is any subset \(C\subseteq\mathbb F_3^4\), without a linearity assumption. “Labeled” means that coordinate positions and alphabet symbols are fixed. The stated orbit calculation is only for the explicitly defined subgroup \(G=(S_3)^4\rtimes D_8\); no claim is made that this subgroup is the full isometry group of the pair metric.

## Proof
If two codewords of a code with minimum pair-distance \(4\) agreed in their first two coordinates, then their differences could occur only in the last two coordinates. Such differences can affect at most the three cyclic adjacent pairs \((1,2),(2,3),(3,0)\), so their pair-distance would be at most \(3\). Therefore projection onto the first two coordinates is injective, and every such code has at most \(3^2=9\) codewords. This is the \((n,d,q)=(4,4,3)\) instance of the symbol-pair Singleton bound.

The supplied verifier independently builds all \(3^4=81\) words and joins two vertices exactly when their pair-distance is \(4\). It then performs an exhaustive Bron–Kerbosch enumeration of all maximal cliques. The resulting maximal-clique histogram is \(1{,}296\) of size \(6\), \(28{,}512\) of size \(7\), and \(8{,}784\) of size \(9\), with no other maximal sizes. Hence the maximum code size is \(9\), and there are exactly \(8{,}784\) labeled maximum codes.

For each maximum code \(C\), the verifier translates by one codeword and tests closure under addition in \(\mathbb F_3^4\). A translated set of nine elements that is closed under addition is a subgroup of the additive group \(\mathbb F_3^4\), hence a two-dimensional \(\mathbb F_3\)-subspace. This gives exactly \(252\) affine two-flats among the maxima.

Finally, the verifier generates the action of independent copies of \(S_3\) on the four coordinates together with a rotation and a reflection of the four-cycle. Exhaustive orbit traversal on the \(8{,}784\) maxima gives orbit sizes \(36,72,144,324,432,648,648,1296,1296,1296,2592\). The affine maxima are exactly the three complete orbits of sizes \(36,72,144\).

## Verification
Running `python3 verify.py` from the supplied directory reconstructs the domain, distance graph, complete maximal-clique census, affine test, group action, orbit decomposition, and the explicit non-affine witness. The recorded output is:

`VERIFY_OK vertices=81 edges=2268 maximal_cliques=38592 histogram=6:1296,7:28512,9:8784 maximum=9 labeled_maxima=8784 affine_maxima=252 orbits=11 orbit_sizes=36,72,144,324,432,648,648,1296,1296,1296,2592 affine_orbits=36,72,144`

The computation is exhaustive over the finite domain; it is not a timeout-based lower bound or a partial enumeration.

## Relationship to prior work
Chee, Ji, Kiah, Wang, and Yin introduced the MDS symbol-pair framework used here, proved the Singleton bound, and established existence of MDS symbol-pair codes for the relevant distance-four regime. Ding, Ge, Jun Zhang, Tao Zhang, and Yiwei Zhang subsequently emphasized linear MDS symbol-pair constructions and tabulated the known distance-four existence family. Those results imply the known optimum size \(9\) for this parameter set but do not imply the number of labeled maximizers, the affine/non-affine split, or the stated orbit decomposition.

Targeted searches for the exact parameter, the aliases “MDS \((4,4)_3\) symbol-pair code” and “ternary length-four pair-distance-four code,” the numbers \(8{,}784\) and \(252\), affine classifications, and orbit classifications did not locate an implication-equivalent census. The closest indexed result found concerned different binary cyclic symbol-pair families rather than this finite ternary all-code classification.

## Limitations
The classification is only for ternary length \(4\) and minimum pair-distance \(4\). The orbit statement is with respect to the stated natural subgroup \(G\), not a claimed full isometry group. Although the most directly relevant construction/existence sources and targeted exact-claim searches were checked, an obscure or unindexed finite census could still exist; this is the residual originality risk.

## References
1. Y. M. Chee, L. Ji, H. M. Kiah, C. Wang, and J. Yin, “Maximum Distance Separable Codes for Symbol-Pair Read Channels,” arXiv:1211.1728, first public version 2012-11-07.
2. B. Ding, G. Ge, J. Zhang, T. Zhang, and Y. Zhang, “New Constructions of MDS Symbol-Pair Codes,” arXiv:1605.08859, first public version 2016-05-28.
