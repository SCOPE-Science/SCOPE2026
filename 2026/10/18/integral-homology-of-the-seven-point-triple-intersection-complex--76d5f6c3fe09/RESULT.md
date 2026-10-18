# Integral homology of the seven-point triple-intersection complex

## Finding
Let \(V=\binom{[7]}3\) be the set of thirty-five triples from seven points. Let \(X\) be the abstract simplicial complex on \(V\) whose faces are the families \(\mathcal F\subseteq V\) in which every two distinct triples intersect. Equivalently, \(X=\operatorname{Ind}(\operatorname{KG}(7,3))\), using the convention that \(\operatorname{KG}(7,3)\) joins disjoint triples. In the alternative notation of Feng and Wang, this is \(\operatorname{Ind}(\operatorname{KG}(3,1))\).

Its complete reduced integral homology is
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{29},& j=6,\\
\mathbb Z^{7},& j=9,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular **there is no torsion of any prime order**. This is an integral homology statement, not a claimed homotopy equivalence to a wedge of spheres.

## Assumptions and scope
The vertex set consists of **all** three-element subsets of \(\{0,1,2,3,4,5,6\}\), ordered lexicographically. A family is a face exactly when its members are pairwise intersecting; the empty family is included to compute *reduced* chains. Orient each positive-dimensional simplex by increasing index order. The assertion is over \(\mathbb Z\) and includes all homological degrees. The largest face has fifteen vertices (simplicial dimension fourteen). No statement is made for other seven-point graph complexes or for \(\operatorname{KG}(n,k)\) at parameters other than triples on seven points.

An equivalent metric definition is the inclusive Vietoris--Rips complex of these thirty-five length-seven binary vectors of Hamming weight three at symmetric-difference distance four: distinct triples intersect if and only if their symmetric difference has size at most four.

## Proof
**Exhaustive face model.** Encode each triple \(T\) by its seven-bit incidence mask and a family \(\mathcal F\) by a thirty-five-bit mask. For each vertex \(i\) define a thirty-five-bit forbidden-neighbor mask recording triples disjoint from the \(i\)-th triple. The recursive generation enumerates, once each, all increasing-index compatible families; the condition for adjoining \(i\) is that its forbidden-neighbor mask has zero intersection with the current family mask. The augmented face counts by cardinality zero through fifteen are
\[
(1,35,525,4445,23555,81942,191170,300855,317730,221865,100296,29295,5950,910,105,7),
\]
whose sum is \(1,278,686\). The source file `kg73_morse.cpp` gives the complete implementation, including the exact ordering and incidence coefficients.

**Acyclic elementary matching.** Starting with all faces unmatched, visit each vertex \(v\) in lexicographic order; for each currently unmatched face \(L\) not containing \(v\), pair \(L\) to \(U=L\cup\{v\}\) when \(U\) is a face and both are still unmatched. This produces \(639,293\) face pairs. For every matched lower face \(L\), draw an arrow to each other matched lower facet of its matched upper face \(U\). A complete Kahn topological ordering visits all \(639,293\) such faces across exactly \(501,581\) arrows; hence no closed gradient path exists. The resulting unmatched simplex counts by **cardinality** are \(45\) in size seven, \(27\) in size eight, \(16\) in size nine, and \(12\) in size ten, with no other critical simplices. The empty simplex is matched, so the reduced Morse complex applies.

**Exact integral Morse boundaries.** In the oriented simplicial chain complex, every matched incidence \([U:L]\) is a unit \(\pm1\). Eliminate matched face pairs by integral row/column operations, or equivalently use the recursive chain projection
\[
P(L)=-[U:L]^{-1}\sum_{\substack{B\subset U,\,|B|=|L|\\B\ne L}}[U:B]P(B)
\]
for each matched lower face, with critical lower faces projecting to their basis vectors and matched upper faces projecting to zero. Acyclicity makes these recursions terminate; hence they compute the differentials of an integral chain complex chain-homotopy equivalent to the original reduced simplicial complex.

The only nonempty differential matrices in the reduced Morse chain complex are the integer matrices \(d_7,d_8,d_9\), respectively of sizes \(45\times27\), \(27\times16\), and \(16\times12\). Their integer ranks are \(16,11,5\). More strongly, unimodular integer row and column operations reduce each to a diagonal matrix with all nonzero diagonal entries \(1\): their Smith forms are \(\operatorname{diag}(1^{16},0)\), \(\operatorname{diag}(1^{11},0)\), and \(\operatorname{diag}(1^{5},0)\), with the rectangular zero portions understood. The actual signed matrices are recorded in `matrices_forward.txt`; `verify.py` independently reconstructs explicit unit-pivot integer reductions and checks \(d_7d_8=d_8d_9=0\).

Because the chain groups are free and all images of these differentials are primitive sublattices, their homology has no torsion. The free ranks are \(45-16=29\) in degree six, \(27-16-11=0\) in degree seven, \(16-11-5=0\) in degree eight and \(12-5=7\) in degree nine. All other Morse chain groups vanish. This proves the theorem over \(\mathbb Z\).

## Verification
The complete package contains `kg73_morse.cpp`, `verify.py`, `matrices_forward.txt`, and `matrices_reverse.txt`. In a directory containing those four files, with Python 3 and a C++17 compiler `g++` installed, run `python3 verify.py`. The verifier compiles the source, re-enumerates **all** compatible families, checks the full gradient acyclicity DAG, reproduces both frozen signed-matrix certificates byte-for-byte, checks exact chain compositions, and computes unit-pivot integer reductions for every Morse differential.

The reverse vertex order is an independent acyclic matching on the same faces: \(639,283\) pairs, \(540,642\) gradient arrows, critical cardinalities \((60,41,11,8)\) in sizes seven through ten, and integer boundary ranks \((31,10,1)\), again with only unit Smith factors. Both constructions give exactly the same integral homology. The final verifier emits `INTEGRAL_HOMOLOGY_VERIFIED` only when both passes succeed.

## Relationship to prior work
Feng and Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs* (2024), introduced the triple-subset families and reported the free-rank pattern for this small parameter in computations, together with homology generators and propagation results. Their published tabulations over \(\mathbb F_2\) do not rule out torsion at odd primes. Feng, *The rational homology of independence complexes of Kneser graphs on triples* (2026), established rational homology ranks in all parameters and separately asked whether integral homology of these complexes is always torsion-free. The present self-contained integer calculation supplies a complete answer **for the first positive parameter only**; it neither reproves the general rational formula nor answers the family-wide integral question. In particular its novelty is the all-prime integral conclusion, not the previously known Betti numbers.

The alternative metric model is consistent with the finite-metric Vietoris--Rips literature, but the present scale is four in the symmetric-difference metric. Results for other metric scales, ordinary graph-metric Rips complexes, or stable Schrijver subgraphs do not imply the exact integer Smith factors computed here.

## Limitations
The result makes no assertion that \(X\) has the homotopy type \(\bigvee^{29}S^6\vee\bigvee^7S^9\); nontrivial attaching maps are not excluded by integral homology alone. No classification for \(\operatorname{KG}(3,k)\) with \(k>1\) is claimed. The proof is a finite, fully executable exact-arithmetic computation whose stated conclusion depends on running or independently reviewing the supplied source and signed matrices. An independent mathematical audit has not been conducted.

## References
1. Ziqin Feng and Guanghui Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566 (first posted 2024-04-16). https://arxiv.org/abs/2404.10566
2. Ziqin Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394 (first posted 2026-10-12). https://arxiv.org/abs/2610.17394
3. *On Vietoris--Rips Complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664 (2023), for related finite-metric constructions. https://arxiv.org/abs/2302.14664
