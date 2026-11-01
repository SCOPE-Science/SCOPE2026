# Torsion-free integral homology for the first nontrivial triple Kneser independence complex

## Finding
Let \(\operatorname{KG}(7,3)\) denote the Kneser graph on the thirty-five triples of \([7]=\{1,\dots,7\}\), with two triples adjacent when they are disjoint. Put \(K=\operatorname{Ind}(\operatorname{KG}(7,3))\). Then
\[
\widetilde H_i(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{29},&i=6,\\
\mathbb Z^7,&i=9,\\
0,&i\notin\{6,9\}.
\end{cases}
\]
In particular, the integral groups are torsion-free. In the alternate parameter convention of Feng and Wang, the same object is \(\operatorname{Ind}(\operatorname{KG}(3,1))\). It is also the inclusive Vietoris--Rips complex of the seven-element, constant-weight-three binary layer at symmetric-difference threshold four.

## Assumptions and scope
All complexes are abstract finite simplicial complexes. The empty face is included for augmented chain calculations; ordinary nonempty faces give the geometric realization. A face of \(K\) is a family of triples that are pairwise intersecting. Reduced homology is taken over \(\mathbb Z\). The statement is for the fixed seven-element ground set only. It makes no claim of a wedge-of-spheres homotopy type, simple homotopy type, a general formula for larger ground sets, or equivariant homology.

## Proof
Order the thirty-five triples by their seven-bit numerical masks and encode any family by a thirty-five-bit integer. A recursive exact enumeration appends only triples intersecting every already selected triple. The procedure visits each face exactly once: at each recursion it chooses the least remaining eligible vertex, removes that vertex from the available list, and recursively restricts eligibility to triples meeting it. It finds \(1,278,686\) faces including the empty face and \(1,278,685\) nonempty faces. For family size zero through fifteen, the complete face counts are
\[
(1,35,525,4445,23555,81942,191170,300855,317730,221865,100296,29295,5950,910,105,7).
\]
Consequently the reduced Euler characteristic is \(22\).

On this augmented face poset construct a discrete-Morse matching by scanning the ordered graph vertices. At step \(v\), among the faces still unmatched, pair every available face omitting \(v\) with its coface obtained by adjoining \(v\), whenever both remain unmatched. The completed matching contains \(639,283\) pairs. The only unmatched cells have dimensions six, seven, eight, and nine, with multiplicities \(60,41,11,8\). Acyclicity is *checked exhaustively* as follows: for each matched upper simplex, inspect every facet other than its paired lower simplex, follow its matching upward when possible, and confirm by depth-first search that the resulting directed graph on all \(639,283\) matched upper simplices has no directed cycle. This is the absence of closed gradient paths, including paths involving the empty face. Hence elementary algebraic Morse cancellation over \(\mathbb Z\) gives a chain-homotopy-equivalent reduced complex of critical cells.

Orient each simplex by increasing vertex order. Eliminate each matched pair with its signed simplicial incidence coefficient, always \(\pm1\). Gradient-path substitution computes the three potentially nonzero integral Morse differentials
\[
\partial_7:\mathbb Z^{41}\longrightarrow\mathbb Z^{60},\qquad
\partial_8:\mathbb Z^{11}\longrightarrow\mathbb Z^{41},\qquad
\partial_9:\mathbb Z^8\longrightarrow\mathbb Z^{11}.
\]
The exact integer matrices appear in `boundary7.txt`, `boundary8.txt`, and `boundary9.txt`; the standalone generator constructs every entry directly from the full face poset. Both compositions \(\partial_7\partial_8\) and \(\partial_8\partial_9\) are zero. Exact Smith normal forms contain respectively \(31\), \(10\), and \(1\) nonzero diagonal factors, *all equal to one*. Thus the reduced integral homology has ranks \(60-31=29\) in degree six, \(41-31-10=0\) in degree seven, \(11-10-1=0\) in degree eight, and \(8-1=7\) in degree nine; other degrees have no Morse cells. Since every differential image is primitive in its target lattice, no homology torsion is possible.

A second complete reduction toggling the thirty-five vertices in reverse order gives \(639,293\) matched pairs and critical multiplicities \(45,27,16,12\). Its integral boundary maps have Smith forms with respectively \(16\), \(11\), and \(5\) unit factors and all remaining entries zero, yielding the same integral groups. The reverse matrices are also included. The two reductions have different critical-chain sizes and provide an additional consistency check.

## Verification
Compile and run `verify_kg73.cpp` using a C++17 compiler, first with no arguments, then with the flag `--reverse`. Each run reconstructs all faces, the matching, all gradient-path transitions, and the complete signed Morse differentials. After both runs, execute `verify_integral.py` using Python 3 with SymPy installed to check every integer matrix entry's dimensions, the chain conditions, and the exact Smith normal forms. `verification_output.txt` records the reproduced output. The complete face-poset matching acyclicity is verified computationally rather than inferred from a sample. The highest simplex has dimension fourteen, so the calculation covers *every* simplicial face and degree.

## Relationship to prior work
Feng and Wang (arXiv:2404.10566v1, first submitted April 16, 2024) already listed the rank values \(29\) and \(7\) in their Table 1 for their parameter \(k=1\) and investigated cross-polytopal cycles and related questions. Thus **the rational ranks are not new**. Feng (arXiv:2610.17394v1, first submitted October 12, 2026) proved the complete rational Betti-number formula for all \(k\) and explicitly asked in Section 7 whether the corresponding integral groups are torsion-free; his proof is over \(\mathbb Q\). The new calculation resolves precisely the smallest nontrivial \(k=1\) integral torsion question, not the all-parameter conjecture. Their rank and rational-homology theorems do not exclude odd-primary torsion; mod-two calculations of an auxiliary complex likewise do not establish torsion-freeness for the present integral complex. Barmak's earlier wedge classification for two-subset Kneser independence complexes concerns a distinct family.

## Limitations
The argument is an exhaustive finite, reproducible chain computation for one specified object; it does not produce a conceptual all-parameter proof. An exact homology calculation alone does not identify higher homotopy attaching maps or prove a sphere-wedge decomposition. No assertion about larger ground sets or integer torsion in those cases is made. A complete independent literature audit may discover an equivalent previous computation; the surveyed sources did not establish this integral case.

## References
1. Ziqin Feng and Guanghui Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1, submitted 2024-04-16, Table 1 and Section 7. https://arxiv.org/abs/2404.10566
2. Ziqin Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394v1, submitted 2026-10-12, Sections 5--7. https://arxiv.org/abs/2610.17394
