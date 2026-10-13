# The six perfect cyclic-Kendall codes in \(S_5\) are affine cosets
## Finding
Equip \(S_5\) with the cyclic Kendall \(\tau\)-metric: an elementary error swaps the entries in two cyclically adjacent positions, so in addition to the four usual adjacent swaps, positions \(1\) and \(5\) may be swapped. A perfect single-error-correcting code is a set whose closed radius-one balls are pairwise disjoint and cover all \(120\) permutations.

There are exactly six such perfect codes. Regard each permutation as a bijection of \(\mathbb Z/5\mathbb Z\), with ordinary function composition, and set
\[
A=\{x\mapsto ax+b: a\in(\mathbb Z/5\mathbb Z)^\times,\ b\in\mathbb Z/5\mathbb Z\}=\operatorname{AGL}(1,5).
\]
Then \(|A|=20\), and the six perfect cyclic-Kendall codes are exactly the six left cosets \(gA\) in \(S_5\). Hence the complete equality class is one orbit under left multiplication by \(S_5\); the stabilizer of \(A\) is precisely \(A\), of order \(20\).

## Assumptions and scope
Permutations are stored in one-line notation. The cyclic Kendall graph has one vertex for each permutation and an undirected edge for each swap of entries in adjacent positions on the five-cycle. Thus every closed radius-one ball has exactly six vertices: its center and five one-swap neighbors. “Perfect” means exact radius-one packing and covering in this graph, not merely minimum distance at least three in the ordinary Kendall metric.

The group statement uses standard composition \((p\circ q)(i)=p(q(i))\). With that convention, \(gA=\{g\circ a:a\in A\}\) denotes a left coset. Other conventional choices for representing permutations can turn the same geometric family into right cosets; the classification itself is invariant under that notational change.

## Proof
Each radius-one ball contains six permutations. Therefore a perfect code must have exactly \(120/6=20\) centers. Perfect codes are consequently identical to exact covers of the \(120\)-element permutation set by the \(120\) radius-one balls.

The accompanying verifier constructs all \(120\) balls directly from the five cyclic adjacent swaps. It then performs exhaustive exact-cover search. At each search node it chooses an uncovered permutation contained in the fewest still-compatible balls, branches over every ball containing that permutation, and removes every ball intersecting the chosen one. Because every branch fixes one required cover block and every discarded block is incompatible with that choice, this is a complete finite enumeration of all exact covers. The search visits \(254\) nodes and returns exactly six covers, each with \(20\) centers.

Independently of that enumeration, the verifier constructs
\[
A=\{x\mapsto ax+b:a\in\{1,2,3,4\},\ b\in\mathbb Z/5\mathbb Z\}
\]
and checks closure under composition, so \(A\) is a subgroup of \(S_5\) of order \(20\). It forms all left cosets \(gA\) and obtains exactly six distinct sets. A set comparison then verifies that these six cosets are exactly the six exact-cover solutions. For each one, the verifier separately unions its twenty radius-one balls, checks that no two intersect, and checks that the union is all of \(S_5\).

Finally, left multiplication by any element of \(S_5\) sends one left coset of \(A\) to another. The verifier checks that the orbit of \(A\) under all \(120\) left multipliers is exactly the six-code set and that its stabilizer is exactly \(A\). This proves the claimed orbit and stabilizer statements.

## Verification
The packaged `verification/verify.py` uses only the Python standard library. A replay gives

`VERIFY_OK vertices=120 ball_size=6 exact_cover_nodes=254 perfect_codes=6 code_size=20 affine_cosets=6 left_orbit=1 stabilizer=20 census_sha256=89d75eb3fe7b76ae2723a55ba872eb3cdd98efb1ef1ac2ca6b363844ec16f7d8`

The census hash is computed from a canonical JSON serialization of all six codes, after sorting the one-line permutations within each code and sorting the six resulting lists. The proof does not infer an infinite statement from this computation: its quantified domain is precisely the finite set \(S_5\).

## Relationship to prior work
Buzaglo and Etzion introduced the cyclic Kendall variant while studying perfect permutation codes. Their 2013 preprint gives a perfect twenty-word code in \(S_5\). In their displayed array, the first row is an affine map over \(\mathbb Z/5\mathbb Z\), and the remaining rows are its cyclic shifts, so that construction is exactly one of the affine cosets above. The same paper explicitly asks whether more perfect codes exist for the cyclic Kendall metric. The complete six-code classification resolves that question for the first displayed case \(S_5\).

The later Buzaglo--Etzion paper on bounds for permutation codes studies the ordinary Kendall metric. Its definitions, bounds, and small-parameter results do not imply which ordinary distance-three codes are exact covers for the cyclic metric. A previous exhaustive ordinary-Kendall equality census at the same order likewise classifies a strictly broader ambient family; it does not determine the cyclic exact-cover subclass or the affine-coset characterization proved here.

Semantic searches using the terms “cyclic Kendall”, “perfect permutation code”, “cyclic adjacent transposition”, “efficient dominating set”, and “Cayley graph” found no published classification that implies the six-code statement. The closest returned records concern different permutation-intersection properties or different code metrics and therefore do not dominate this claim.

## Limitations
The result is only for the cyclic Kendall metric on \(S_5\). It does not classify perfect cyclic-Kendall codes in larger symmetric groups and does not assert their existence there. The exhaustive enumeration certifies all perfect radius-one codes for this finite graph; it is not a general existence theorem. Priority risk remains for obscure literature using a graph-theoretic synonym rather than permutation-code terminology, although searches included the efficient-domination and Cayley-graph formulations.

## References
1. S. Buzaglo and T. Etzion, *Perfect Permutation Codes with the Kendall's \(\tau\)-Metric*, arXiv:1310.5515v1, first public version 2013-10-21; later published in the 2014 IEEE International Symposium on Information Theory, DOI 10.1109/ISIT.2014.6875262.
2. S. Buzaglo and T. Etzion, *Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric*, IEEE Transactions on Information Theory 61 (2015), DOI 10.1109/TIT.2015.2424701.
