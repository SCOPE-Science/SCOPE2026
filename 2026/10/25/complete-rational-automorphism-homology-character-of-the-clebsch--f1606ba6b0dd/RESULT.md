# Complete rational automorphism-homology character of the Clebsch independence complex

## Finding
Let \(N=\mathbb F_2^5/\langle(1,1,1,1,1)\rangle\). Let \(C\) be the Cayley graph of \(N\) with the five distinct generators represented by the coordinate unit vectors, and put \(X=\operatorname{Ind}(C)\). This is the degree-five, sixteen-vertex Clebsch graph (also called the folded five-cube or Greenwood–Gleason graph); its complement is the degree-ten graph sometimes given the same name. The entire automorphism group is \(G=N\rtimes S_5\), of order \(1920\).

Let \(P=\mathbb Q^5\) carry the coordinate-permutation representation of \(S_5\), inflated to \(G\) with trivial \(N\)-action, and let \(P_0=\ker(P\xrightarrow{\sum}\mathbb Q)\). For \(i=1,\ldots,5\), define the nontrivial character
\[
\lambda_i([a])=(-1)^{\sum_{j\ne i}a_j}\qquad(a\in\mathbb F_2^5).
\]
The exponent changes by four upon replacing \(a\) by \(a+(1,1,1,1,1)\), so the character is well defined on \(N\). Let \(M\) be the rational five-dimensional \(G\)-representation with basis \(b_1,\ldots,b_5\), where for \((t,p)\in N\rtimes S_5\),
\[
(t,p)b_i=\lambda_{p(i)}(t)b_{p(i)}.
\]
Write \(\operatorname{sgn}\) for the sign character of \(S_5\), inflated to \(G\).

**The complete graded rational automorphism-homology module is**
\[
\boxed{\widetilde H_3(X;\mathbb Q)\cong_{\mathbb Q[G]}\operatorname{sgn}\otimes(P_0\oplus M),\qquad
\widetilde H_k(X;\mathbb Q)=0\ (k\ne3).}
\]
Equivalently, for every \((t,p)\in G\), its degree-three rational character is
\[
\boxed{\chi(t,p)=\operatorname{sgn}(p)\left(\#\{i:p(i)=i\}-1+\sum_{i:p(i)=i}\lambda_i(t)\right).}
\]
In particular, restriction to the translation group \(N\) is four copies of the trivial character plus the five distinct characters \(\lambda_i\), each once. Hence \(\dim\widetilde H_3(X;\mathbb Q)^N=4\) but \(\widetilde H_3(X;\mathbb Q)^G=0\). These are symmetry-sensitive statements; the already known ordinary homotopy equivalence \(X\simeq\bigvee^9S^3\) is not presented as a new finding.

## Assumptions and scope
All graphs are finite, simple and undirected, all simplicial complexes are ordinary abstract independence complexes, and all group representations and character calculations use rational coefficients. The five translation characters are defined relative to the quotient \(N\) and do not require choosing a section. For reproducibility, one may normalize representatives by setting coordinate five to zero. Then the vertices are the integers \(0,\ldots,15\), and the five Cayley generators are the integers \(1,2,4,8,15\). In this normalization, \(N\rtimes S_5\) acts by coordinate permutation followed by translation.

The claimed automorphism group is full: a graph automorphism is determined by the image of a given vertex and its permutation of the five neighbors. Indeed, adjacent vertices have zero common neighbors, while each pair of distinct neighbors of a fixed vertex has precisely one other common neighbor; these ten vertices comprise the ten nonneighbors of the fixed vertex. Thus \(|\operatorname{Aut}(C)|\le16\cdot5!=1920\). The displayed semidirect product acts by 1920 distinct automorphisms, giving equality.

## Proof
First establish that the reduced rational homology is concentrated in degree three, with dimension nine. In the above 16-vertex normalization, enumerate all independent vertex subsets. There are exactly \(392\) nonempty faces, with face counts by dimension
\[
(16,80,160,120,16).
\]
Construct the following deterministic discrete-Morse matching on the nonempty face poset. In integer vertex notation, visit vertices in this order:
\[
14,4,9,7,3,12,6,8,13,2,0,5,10,1,11,15.
\]
At a vertex \(v\), visit currently unmatched faces in increasing cardinality and lexicographic order; for each face \(\sigma\) not containing \(v\), pair it with \(\sigma\cup\{v\}\) if both remain unmatched. Exactly \(191\) pairs arise. Among the remaining ten cells there is one zero-simplex and nine three-simplices, and none in other dimensions. Enumerate all \(1200\) codimension-one face incidences, orient matched inclusions upward and the others downward; a topological sort visits every one of the \(392\) vertices of the resulting directed Hasse graph, proving this matching acyclic. Forman's theorem then gives \(X\simeq\bigvee^9S^3\). This independently reconstructs, but does not claim priority for, the homotopy result already in the literature.

The full \(G\)-action is simplicial, so every \((t,p)\in G\) acts on the augmented rational simplicial chain complex \(\widetilde C_*(X;\mathbb Q)\). For a nonempty face \(F\), a group element contributes to the trace in its dimension precisely when it setwise preserves \(F\), with contribution equal to the sign of the induced permutation of the sorted vertices of \(F\). The empty face contributes \(-1\) to the reduced Lefschetz number. Since the only nonzero reduced homology is degree three, the exact alternating-trace identity yields
\[
\chi_{\widetilde H_3}(g)=-\widetilde L(g)
=1-\sum_{d=0}^{4}(-1)^d\!\sum_{\substack{F\in X,\ |F|=d+1\\gF=F}}\operatorname{sgn}(g\vert_F).
\]
This formula uses only finite signed face enumeration, not a numerical eigenvalue approximation.

A standalone checker enumerates the full set of \(5!\cdot16=1920\) distinct coordinate-permutation/translation automorphisms; for each, it evaluates this signed-face formula and verifies equality with
\[
\operatorname{sgn}(p)\left(\#\operatorname{Fix}(p)-1+\sum_{i:p(i)=i}\lambda_i(t)\right).
\]
The same checker separately performs exact Walsh–Fourier inversion on the 16 translation traces. The multiplicities are four for the trivial character and one for each of the five weight-four characters; all other translation multiplicities vanish. All checks use integer arithmetic and exhaust their stated finite domains.

Finally, the module \(\operatorname{sgn}\otimes(P_0\oplus M)\) has precisely this computed character: \(P_0\) contributes \(\#\operatorname{Fix}(p)-1\); the signed permutation module \(M\) contributes \(\sum_{p(i)=i}\lambda_i(t)\). Over characteristic zero, semisimplicity and character uniqueness for finite groups imply the displayed isomorphism. Taking \(N\)-invariants leaves \(\operatorname{sgn}\otimes P_0\), whose \(S_5\)-invariants vanish, yielding the final symmetry consequences.

## Verification
Execute `python3 verify_clebsch_module.py` with Python 3.8 or newer; only the standard library is needed. It reconstructs all 392 faces, 191 matching pairs and 1200 face incidences, proves the directed matching acyclic by exhaustive topological sort, evaluates exact signed Lefschetz traces for all 1920 group elements, and independently checks translation multiplicities by integral Walsh inversion. Its success messages are `MORSE_191_PAIRS_ONE_VERTEX_NINE_3CELLS_ACYCLIC`, `ALL_1920_FULL_AUTOMORPHISM_CHARACTERS_VERIFIED`, `TRANSLATION_MODULE_FOUR_TRIVIAL_PLUS_FIVE_DISTINCT_LINES_VERIFIED`, and `CLEBSCH_FULL_RATIONAL_HOMOLOGY_MODULE_VERIFIED`. The mathematical group-theoretic and homological deductions are in the proof above; the checker supplies exhaustive finite certificates for the computational claims.

For a small character check, on pure coordinate permutations in the cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the character is \((9,-5,1,3,1,-1,-1)\).

## Relationship to prior work
Two published exact Clebsch/folded-five-cube independence-complex computations already prove the homotopy equivalence \(X\simeq\bigvee^9S^3\); the present result uses that homology concentration only as an independently checked premise. The new theorem is a statement about the **whole rational \(1920\)-element automorphism representation**, which is not determined by the nine-sphere homotopy type. Gromada's work describes the full classical automorphism group of folded cubes but does not calculate their independence-complex homology action. The general independence-complex Morse techniques of Goyal–Shukla–Singh do not supply this specific representation. Cioabă–Mim address lower-degree clique homology for strongly regular graphs; their degree-ten Clebsch-complement calculation does not determine the degree-three equivariant module. The OEIS independence-polynomial and Euler-characteristic tables supply face counts and Euler characteristic only. A translation-character calculation for the **neighborhood complex** of folded cubes concerns a different complex and homological degree, and cannot imply the present result.

The claimed contribution is exactly the module and its character/fixed-subspace consequences, not the face enumeration, earlier homotopy classification, general Lefschetz formula or abstract semisimplicity.

## Limitations
This is an exact finite, computer-assisted calculation of one graph's rational equivariant homology module. The finite certificate depends on the provided exhaustive enumerator and independently stated mathematical reductions; it does not yield integral equivariant module structure or a classification for all folded cubes. Exhaustive finite calculation proves the stated finite character only after correctness of its graph/face/action definitions and checker logic is accepted. Searches of indexed records, aliases and relevant full texts cannot exclude an equivalent result in inaccessible or unindexed literature. No independent mathematical audit has been performed.

## References
1. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1, first publicly available 2019-05-16, Proposition 3.1. https://arxiv.org/abs/1905.06926
2. D. Gromada, *Quantum symmetries of Cayley graphs of abelian groups*, arXiv:2106.08787v1, first publicly available 2021-06-16, Section 5 on folded cubes. https://arxiv.org/abs/2106.08787
3. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, Section 7 (degree-ten Clebsch complement). https://arxiv.org/abs/2606.27328
4. OEIS A355227, independence polynomials of folded cubes, https://oeis.org/A355227; OEIS A355559, values of these polynomials at minus one, https://oeis.org/A355559.
5. *The Clebsch independence complex is a wedge of nine 3-spheres*, published exact homotopy computation, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-clebsch-independence-complex-is-a-wedge-of-nine-3-spheres--344f83b86fa0
6. *The folded five-cube independence complex is a wedge of nine 3-spheres*, independent published exact homotopy computation, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-folded-five-cube-independence-complex-is-bigvee-9-s-3--fb89079b9172
