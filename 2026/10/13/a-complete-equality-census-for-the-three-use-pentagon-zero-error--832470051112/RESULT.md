# A complete equality census for the three-use pentagon zero-error code
## Finding
For three independent uses of the pentagon confusability channel, equivalently the strong graph power \(C_5^{\boxtimes 3}\), the maximum zero-error code size is \(10\). Exactly \(391{,}600\) maximum codes of size \(10\) exist on the labeled alphabet \((\mathbb Z/5\mathbb Z)^3\), and exactly \(31{,}328\) contain any prescribed word. Under the natural channel-isometry group \(G=(D_{10})^3\rtimes S_3\) of order \(6000\), the maxima form exactly \(85\) orbits. Their stabilizer-order distribution is \(1^{53},2^{19},3^2,4^7,8^1,10^2,40^1\). The unique orbit with stabilizer order \(40\) has representative \(\{(0,0,0),(0,0,2),(1,2,0),(1,2,2),(2,4,0),(2,4,2),(3,1,0),(3,1,2),(4,3,0),(4,3,2)\}\).

The first number refines the classical equality \(\alpha(C_5^{\boxtimes 3})=10\) by determining the entire labeled equality set and its natural symmetry decomposition. Equivalently, these are all three-use zero-error block codes for a memoryless channel whose confusability graph is a pentagon.

## Assumptions and scope
Identify the five input symbols with \(\mathbb Z/5\mathbb Z\). Two distinct triples \(x,y\in(\mathbb Z/5\mathbb Z)^3\) are confusable precisely when, in every coordinate, their cyclic difference is \(0\), \(1\), or \(-1\). Thus a zero-error code is a set in which every pair differs by cyclic distance \(2\) in at least one coordinate. This is exactly an independent set of the strong power \(C_5^{\boxtimes 3}\).

The symmetry group used here is the explicit natural channel-isometry group \(G=(D_{10})^3\rtimes S_3\): independently in each coordinate one may translate or reflect the pentagon, and one may permute the three channel uses. No claim is made here about orbit structure under any larger abstract automorphism group.

## Proof
Fix the word \((0,0,0)\). Exactly \(98\) of the remaining \(124\) triples are nonconfusable with it, because its closed strong-product neighborhood has \(3^3=27\) vertices. Build the graph on those \(98\) candidates in which two candidates are adjacent when they are mutually nonconfusable. A zero-error code of size \(10\) containing \((0,0,0)\) is then a \(9\)-clique in this compatibility graph; a hypothetical code of size \(11\) containing the fixed word is a \(10\)-clique.

The bundled exact search enumerates every \(9\)-clique and finds \(31{,}328\), while an exhaustive \(10\)-clique search finds none. The recursion branches on a candidate vertex, intersects the remaining set with its compatibility neighborhood, and prunes only when a greedy proper coloring of the remaining graph proves that too few additional clique vertices are possible. Each branch removes its chosen vertex before continuing, so every clique is counted once. Every enumerated size-\(10\) code is then rechecked directly against the defining pairwise nonconfusability condition.

Translation is transitive on the \(125\) words. Double-counting incidences \((w,C)\) with \(w\in C\) therefore gives
\[
10N=125\cdot31{,}328,
\]
so the total number of maximum labeled codes is \(N=391{,}600\).

For symmetry classification, each maximum containing the origin is canonically normalized by trying each of its ten words as an anchor, each of the \(2^3\) independent coordinate reflections, and all \(3!\) coordinate permutations. This yields exactly \(85\) canonical representatives. For each representative the verifier then exhausts all \(6000\) elements of \(G\) and recomputes its stabilizer. The resulting orbit sizes sum to
\[
53\cdot6000+19\cdot3000+2\cdot2000+7\cdot1500+750+2\cdot600+150=391{,}600,
\]
independently matching the incidence count. There is one stabilizer-\(40\) orbit, represented by the set stated above.

## Verification
`verify.cpp` reconstructs the \(125\)-vertex object from the definition, performs both exhaustive clique searches, directly validates every maximum containing the fixed word, derives the \(85\) canonical classes, recomputes every stabilizer in \(G\), and compares the resulting table with `ORBITS.csv`. On the packaged data it reports:

`VERIFY_OK vertices=125 origin_candidates=98 origin_maxima=31328 maximum=10 labeled_maxima=391600 natural_group=6000 orbits=85 stabilizers=1x53,2x19,3x2,4x7,8x1,10x2,40x1 nodes9=262869 nodes10=22757 special_stabilizer=40`

A standard replay is `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify ORBITS.csv`.

## Relationship to prior work
Baumert, McEliece, Rodemich, Rumsey, Stanley, and Taylor introduced the toroidal packing formulation and proved the exact value \(\alpha(C_5^{\boxtimes 3})=10\); their Theorem 4 says an exhaustive search excludes sizes \(11\) and \(12\). Their paper also classifies a two-dimensional family of maximal packings, but the inspected text does not enumerate or classify all equality cases for the three-dimensional pentagon instance.

Badalyan and Mnatsakanyan later gave another proof of \(\alpha(C_5^{\boxtimes 3})=10\). Bohman, Holzman, and Natarajan developed complete maximum-independent-set classifications for certain other powers of odd cycles and later bounds for cubes of cycles \(C_{8n+5}\); those parameter families do not imply the three-use pentagon equality census here. Searches for the exact counts \(31{,}328\) and \(391{,}600\), for an \(85\)-orbit classification, and for aliases phrased as pentagon zero-error codes or maximum independent sets of \(C_5^{\boxtimes 3}\) located no implication-equivalent published result.

The zero-error communication formulation lies in information theory: modern literature on Shannon capacity explicitly treats confusability graphs and strong graph products as zero-error channel objects and includes MSC \(94A15\).

## Limitations
This is a finite equality classification for exactly three uses of the pentagon channel; it does not determine new Shannon-capacity values or classify arbitrary powers. The stated \(85\) orbits are for the explicit natural channel-isometry group \(G\), not for an unspecified larger group. The 1974 product-graph paper by Sonnemann and Krafft was identified as plausibly relevant, but a full lawful text was not available during this check after open-access attempts; its bibliographic abstract describes independence numbers of strong products and odd-cycle cubes but gives no equality census. An obscure unindexed historical equality classification therefore remains a residual originality risk.

## References
1. L. D. Baumert, R. J. McEliece, E. Rodemich, H. C. Rumsey Jr., R. Stanley, H. Taylor, *A Combinatorial Packing Problem*, SIAM-AMS Proceedings 4 (1971), 97-108. Scanned copy: https://oeis.org/A003012/a003012.pdf. The reported conference took place in New York beginning 25 March 1970.
2. V. S. Badalyan, A. A. Mnatsakanyan, *On the independence numbers of the powers of C5 graph*, Proceedings of the Yerevan State University, Physical and Mathematical Sciences 46(1) (2012), 38-42. DOI: 10.46991/PYSUA.2012.46.1.038.
3. T. Bohman, R. Holzman, V. Natarajan, *Maximum Independent Sets in Certain Powers of Odd Cycles*, Electronic Journal of Combinatorics 16 (2009), N26.
4. T. Bohman, R. Holzman, V. Natarajan, *On the Independence Numbers of the Cubes of Odd Cycles*, Electronic Journal of Combinatorics 20(3) (2013), P10. DOI: 10.37236/2598.
5. E. Sonnemann, O. Krafft, *Independence numbers of product graphs*, Journal of Combinatorial Theory, Series B 17(2) (1974), 133-142. DOI: 10.1016/0095-8956(74)90081-1.
