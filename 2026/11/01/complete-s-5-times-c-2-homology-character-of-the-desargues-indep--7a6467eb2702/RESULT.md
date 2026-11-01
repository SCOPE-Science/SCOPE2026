# Complete \(S_5\times C_2\) homology character of the Desargues independence complex

## Finding
Let \(D\) be the twenty-vertex Desargues graph, equivalently the bipartite Kneser graph \(H(5,2)\), and set \(X=\operatorname{Ind}(D)\). Its full graph automorphism group is \(G\cong S_5\times C_2\). Let \(\varepsilon\) denote the nontrivial rational character of \(C_2\), let \(\operatorname{sgn}_5\) be the sign representation of \(S_5\), and let \(P_5=\mathbb Q^{\{1,2,3,4,5\}}\) be its natural point-permutation module. Then
\[
\boxed{\widetilde H_4(X;\mathbb Q)\cong \operatorname{sgn}_5\boxtimes\varepsilon,\qquad
\widetilde H_5(X;\mathbb Q)\cong P_5\boxtimes\varepsilon.}
\]
All other reduced rational homology groups vanish. In particular, the central involution interchanging the bipartition acts as minus the identity on **both** nonzero homology groups. The reduced rational homology of the ordinary full-symmetry quotient \(|X|/G\) vanishes in every degree.

Equivalently, for \(g=(\pi,\delta)\in S_5\times C_2\), with \(\delta\in\{0,1\}\), the two nonzero characters are
\[
\chi_4(g)=(-1)^\delta\operatorname{sgn}(\pi),\qquad
\chi_5(g)=(-1)^\delta\#\{i\in\{1,\ldots,5\}:\pi(i)=i\}.
\]
This is an equivariant refinement, not a new claim about the nonequivariant homotopy type.

## Assumptions and scope
The vertex set is \(\{(A,b):A\in\binom{\{1,2,3,4,5\}}2,\ b\in\{0,1\}\}\). Distinct vertices \((A,b)\), \((B,c)\) are adjacent exactly when \(b\ne c\) and \(A\cap B=\varnothing\). An independent face is any subset containing no adjacent pair. The symmetric group permutes the underlying five symbols simultaneously in both layers, and the central \(C_2\) exchanges the layers.

This action is the full automorphism group: any graph automorphism preserves or exchanges the two bipartition classes because the graph is connected. On one class, two vertices have a common neighbor exactly when the corresponding two-subsets intersect. Therefore an automorphism preserving that class induces an automorphism of the triangular graph \(T(5)\), whose five maximal cliques of size four are the stars of individual symbols. It is induced by a unique element of \(S_5\). The neighborhoods in the opposite class are distinct, so that permutation uniquely determines the action there. Layer exchange supplies the other coset. Thus \(\operatorname{Aut}(D)=S_5\times C_2\) with \(240\) elements.

## Proof
**1. Exact finite chain bound.** Enumerating every independent subset produces the full face vector by dimensions zero through nine:
\[
(20,160,660,1510,1924,1320,480,115,20,2).
\]
There are exactly \(6211\) nonempty faces. With the empty face in degree minus one, bit-exact Gaussian elimination over \(\mathbb F_2\) gives the augmented boundary ranks \(\operatorname{rank}(\partial_k)\), in degrees zero through nine:
\[
(1,19,141,519,991,932,383,97,18,2).
\]
The resulting reduced \(\mathbb F_2\)-Betti numbers are \(1\) in degree four and \(5\) in degree five, and zero otherwise. The universal coefficient theorem implies, for rational reduced homology, that it is zero outside degrees four and five and that
\[
\dim_{\mathbb Q}\widetilde H_4(X;\mathbb Q)\le1,\qquad
\dim_{\mathbb Q}\widetilde H_5(X;\mathbb Q)\le5.
\]
These inequalities do not assume the absence of integral torsion.

**2. Exact equivariant Lefschetz character.** Orient each nonempty simplex by increasing vertex index. For every automorphism \(g\), a simplex contributes to the trace on its chain group precisely if it is setwise fixed; its contribution is the parity of the induced permutation of its oriented vertices. Hence the reduced Lefschetz character is exactly
\[
L(g)=\sum_{k=0}^9(-1)^k\operatorname{tr}(g\mid C_k(X;\mathbb Q))-1.
\]
Complete enumeration for the seven cycle types of \(S_5\) gives the following signed traces, displayed for no layer swap and layer swap respectively:

| Cycle type of \(\pi\) | \(L(\pi,0)\) | \(L(\pi,1)\) |
|:---|---:|---:|
| \(1^5\) | \(-4\) | \(4\) |
| \(2\,1^3\) | \(-4\) | \(4\) |
| \(2^2\,1\) | \(0\) | \(0\) |
| \(3\,1^2\) | \(-1\) | \(1\) |
| \(3\,2\) | \(-1\) | \(1\) |
| \(4\,1\) | \(-2\) | \(2\) |
| \(5\) | \(1\) | \(-1\) |

Consequently, for all \(240\) automorphisms,
\[
L(\pi,\delta)=(-1)^\delta\big(\operatorname{sgn}(\pi)-\#\operatorname{Fix}(\pi)\big).
\]
The attached program independently checks all \(240\) graph automorphism maps and all traces, not only the seven rows.

**3. Isolate the actual homology modules.** By Hopf's trace formula and Step 1, the rational virtual character satisfies
\[
[\widetilde H_4]-[\widetilde H_5]=[\operatorname{sgn}_5\boxtimes\varepsilon]-[P_5\boxtimes\varepsilon].
\]
Over \(\mathbb Q\), the \(S_5\)-permutation module decomposes as \(P_5\cong\mathbf1\oplus V_4\), where \(V_4\) is the irreducible four-dimensional standard module. Neither summand is \(\operatorname{sgn}_5\). Therefore the coefficient of the irreducible \(\operatorname{sgn}_5\boxtimes\varepsilon\) in this virtual character is \(+1\). Nonnegative multiplicities of actual finite-group representations force it to occur in \(\widetilde H_4\). The upper bound of one dimension from Step 1 forces \(\widetilde H_4=\operatorname{sgn}_5\boxtimes\varepsilon\). Substitution identifies \(\widetilde H_5=P_5\boxtimes\varepsilon\). No assumption on possible integral torsion was used.

**4. Symmetry quotient.** Both nonzero rational modules are anti-invariant under layer exchange. After barycentric subdivision, the finite-group action is simplicial without inversions; with rational coefficients, chains of the ordinary quotient identify with coinvariants, and finite-group averaging identifies their homology with invariants. All reduced invariant homology therefore vanishes, proving the quotient statement.

## Verification
Run `python3 verify.py` using Python's standard library alone. The program reconstructs the graph from pair-disjointness, enumerates all \(6211\) independent faces, recomputes the augmented mod-two boundary ranks by exact bit-column elimination, verifies \(240\) distinct automorphism maps and their edge preservation, and directly evaluates the signed fixed-simplex Lefschetz trace of **each** automorphism. It checks all displayed equalities by assertions and ends with `VERIFY_OK`. The included `verify_output.txt` records the exact output. This finite exhaustive calculation is the proof of the required finite boundary ranks and Lefschetz character; the rational module identification is the independent representation-theoretic deduction in Step 3.

## Relationship to prior work
Mütze and Su (public preprint March 31, 2015) study Hamilton cycles in bipartite Kneser graphs, including \(H(5,2)\), but not their independence-complex homology actions. Kumar, Singh, and Verma (2021) study graded Betti numbers and regularity of *edge ideals* of bipartite Kneser graphs; those invariants are not a calculation of the graded \(S_5\times C_2\) representation on the reduced homology of the entire independence complex. Two published 2026 calculations of \(\operatorname{Ind}(D)\) give the nonequivariant homotopy type \(S^4\vee\bigvee^5 S^5\), and their face vectors agree with the independent enumeration here; neither gives either automorphism module. An older study by Nilakantan and Shukla of cyclic-interval regular bipartite graphs concerns a different graph family and supplies nonequivariant homotopy formulas. Carnero Bravo (2026) uses the Kronecker double cover as an input in formulas for generalized Mycielskian independence complexes, without this particular equivariant computation. No published statement covering the two graded modules was found in the targeted literature and research-record searches.

## Limitations
The finding concerns this single canonical graph, not all bipartite Kneser graphs. It determines rational group representations and rational quotient homology; it does **not** determine the integral \(G\)-lattices, any possible integral torsion, or the homotopy type of the quotient. Exact finite code checks support the mathematical proof but do not amount to independent expert validation. Publication-priority searches cannot exclude an unindexed equivalent result under a different formulation.

## References
1. T. Mütze and P. Su, *Bipartite Kneser graphs are Hamiltonian*, arXiv:1503.09175, first public March 31, 2015, https://arxiv.org/abs/1503.09175.
2. A. Kumar, P. Singh, and R. Verma, *Certain Homological Invariants of Bipartite Kneser Graphs*, arXiv:2105.06144, first public May 13, 2021, https://arxiv.org/abs/2105.06144.
3. *The Desargues independence complex is \(S^4\vee\bigvee^5 S^5\)*, published research record, October 11, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563.
4. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, first public January 19, 2026, https://arxiv.org/abs/2601.13432.
5. *Independence complex of the Desargues graph is \(S^4\vee\bigvee^5 S^5\)*, published research record, October 4, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-independence-complex-of-the-desargues-graph-is-s-4-vee-bigvee-5--f3b1cf10aadb.
6. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789, first public September 14, 2017, https://arxiv.org/abs/1709.04789.
