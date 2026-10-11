# Complete rational automorphism character of the \(K_{3,3}\) Morse complex

## Finding
Let \(K_{3,3}\) be the complete bipartite graph on two sets of three vertices, and let \(X=\mathcal M(K_{3,3})\) be its **ordinary Morse complex of acyclic discrete vector fields**. Its full automorphism group is
\[
G=\operatorname{Aut}(K_{3,3})\cong(S_3\times S_3)\rtimes C_2.
\]
The group acts naturally on \(\widetilde H_4(X;\mathbb Q)\), a rational vector space of dimension \(80\). The following is the complete decomposition into irreducible rational \(G\)-representations:
\[
\boxed{\begin{aligned}
\widetilde H_4(X;\mathbb Q)\cong{}&W_{\mathbf1}^{+}\oplus2W_{\mathbf1}^{-}
\oplus W_{\mathrm{sgn}}^{+}\oplus2W_{\mathrm{sgn}}^{-}\\
&\oplus4W_{\mathrm{st}}^{+}\oplus5W_{\mathrm{st}}^{-}
\oplus3I_{\mathbf1,\mathrm{sgn}}\\
&\oplus4I_{\mathbf1,\mathrm{st}}\oplus4I_{\mathrm{sgn},\mathrm{st}}.
\end{aligned}}
\]
Here \(\mathbf1,\mathrm{sgn},\mathrm{st}\) denote the trivial, sign, and two-dimensional standard rational representations of \(S_3\). To define the irreducibles, write \(G\) as triples \((a,b;t)\) with \(a,b\in S_3\) and \(t\in\{0,1\}\), where \(t=1\) interchanges the bipartition. For each of the three representations \(\rho\) of \(S_3\), \(W_\rho^\pm\) extends \(\rho\boxtimes\rho\), with the interchange acting by the positive or negative flip. Thus
\[
\chi_{W_\rho^\pm}(a,b;0)=\chi_\rho(a)\chi_\rho(b),\qquad
\chi_{W_\rho^\pm}(a,b;1)=\pm\chi_\rho(ba).
\]
For distinct \(\rho,\sigma\), define
\[
I_{\rho,\sigma}=\operatorname{Ind}_{S_3\times S_3}^{G}(\rho\boxtimes\sigma).
\]
The sole nonzero reduced rational homology degree is \(4\). The fixed subspace under the full automorphism group has dimension \(1\). For the pure bipartition interchange, the character value is \(-4\), giving positive and negative eigenspace dimensions \(38\) and \(42\).

## Assumptions and scope
The graph has vertices \(A=\{0,1,2\}\) and \(B=\{3,4,5\}\), with edges exactly between the parts. A vertex of \(X\) is one primitive gradient pair \((u,\{u,v\})\), written as a directed arrow \(u\to v\). A face is a finite set of such pairs in which every original graph vertex and original graph edge participates in at most one gradient pair and no closed gradient path exists. Equivalently it is a partially oriented forest with each vertex of outdegree at most one and no directed cycle. This is **not** the ordinary edge-matching complex and not a configuration-space Morse chain complex. We use reduced simplicial homology over \(\mathbb Q\), with the natural signed action on oriented simplices.

## Proof
**1. Complete rational homology concentration.** There are \(18\) primitive arrows, one per ordered incident vertex-edge pair. Enumerating every choice of at most one outgoing arrow per graph vertex and rejecting repeated used edges and directed cycles gives the nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(18,126,432,729,486).
\]
A separate enumeration assigning one of three states (unused, arrow one way, arrow the other way) to each of the nine original edges yields exactly the same \(1791\) faces. The augmented simplicial boundary matrices have ranks over \(\mathbb F_2\)
\[
(\operatorname{rank}\partial_0,\ldots,\operatorname{rank}\partial_4)
=(1,17,109,323,406),
\]
where \(\partial_0:C_0\to C_{-1}=\mathbb F_2\) is augmentation. These are exact finite ranks, reconstructed by the verifier's bitset elimination. They also determine **the rational ranks**, without incorrectly equating finite-field rank and rational rank in general: rational rank is at least mod-\(2\) rank, while \(\partial_k\partial_{k+1}=0\) gives successive upper bounds
\[
\operatorname{rank}_{\mathbb Q}\partial_{k+1}
\leq\dim_{\mathbb Q}C_k-\operatorname{rank}_{\mathbb Q}\partial_k.
\]
Starting with augmentation rank \(1\), each displayed mod-\(2\) rank saturates that upper bound, forcing equality over \(\mathbb Q\) at every step. Therefore \(\widetilde H_i(X;\mathbb Q)=0\) for \(i\ne4\), and \(\dim\widetilde H_4=486-406=80\). These nonequivariant Betti numbers were already recorded in prior work; they are reconstructed here only to justify the character calculation.

**2. Signed Lefschetz calculation.** Given a graph automorphism \(g\), order all primitive arrows lexicographically, then act on each oriented face by permuting its arrows. If \(F_k\) is the set of faces containing exactly \(k\) arrows, the reduced Lefschetz formula and the proven homology concentration give
\[
\chi_4(g)=\sum_{k=1}^{5}(-1)^{k-1}
\sum_{\substack{\sigma\in F_k\\g\sigma=\sigma}}
\operatorname{sgn}(g|_\sigma)-1.
\]
The \(-1\) subtracts the trace on ordinary \(H_0\), on which every automorphism acts as identity. The inner sign is the parity of the induced permutation of the ordered arrows in the fixed face. Independently, if \(g\) has \(c\) cycles on the \(k\) arrows of a fixed face, its total Lefschetz contribution is \((-1)^{c-1}\); these two computations agree for every fixed face for all \(72\) automorphisms.

Writing \(e\), \(s\), and \(c\) for the identity, a transposition, and a three-cycle conjugacy type of \(S_3\), the **complete character** reduces to the following nine conjugacy-class values:

| Automorphism type | \(\chi_4\) |
| --- | ---: |
| Preserving parts, \((e,e)\) | \(80\) |
| Preserving parts, \((e,s)\) | \(0\) |
| Preserving parts, \((e,c)\) | \(2\) |
| Preserving parts, \((s,s)\) | \(0\) |
| Preserving parts, \((s,c)\) | \(0\) |
| Preserving parts, \((c,c)\) | \(5\) |
| Swapping parts, product \(ba\) of type \(e\) | \(-4\) |
| Swapping parts, product \(ba\) of type \(s\) | \(0\) |
| Swapping parts, product \(ba\) of type \(c\) | \(-1\) |

The six preserving-part types are unordered pairs of conjugacy types; in the swapping coset, the conjugacy class depends on the cycle type of \(ba\).

**3. Irreducible decomposition.** By the normal subgroup \(S_3\times S_3\) and the factor-flip involution, its irreducible rational representations are exactly the six \(W_\rho^\pm\) and the three \(I_{\rho,\sigma}\) above. For the latter, the character is \(\chi_\rho(a)\chi_\sigma(b)+\chi_\sigma(a)\chi_\rho(b)\) on the preserving coset and zero on the swapping coset. Character orthogonality (or direct summation over the \(72\) group elements) gives multiplicities, in the order displayed in the finding,
\[
(1,2,1,2,4,5,3,4,4).
\]
The nine candidate characters are pairwise orthonormal; the sum of the squares of their dimensions is \(72\), so this is the full irreducible list. Their weighted dimensions sum to \(80\), confirming the decomposition. Exactly one trivial character \(W_{\mathbf1}^+\) occurs. The identity interchange has trace \(-4\), proving the two eigenspace dimensions.

## Verification
Run `python3 verify.py` with Python \(3\), using only its standard library. The verifier reconstructs the entire complex in two combinatorially different ways, checks all augmented mod-\(2\) boundary ranks, enumerates all \(72\) automorphisms, checks every fixed-face sign by a second permutation-cycle count, verifies the entire class table, tests orthonormality of the nine irreducible characters, and calculates all multiplicities. The successful output ends with `VERIFY_OK` and prints the exact face vector, boundary ranks, conjugacy values, multiplicities, invariant dimension, and interchange eigenspaces. The character proof is an exact finite computation combined with standard character theory and Lefschetz–Euler–Poincaré; no statistical sampling or numerical approximation is used.

## Relationship to prior work
Lin and Scoville determine the automorphism group of the Morse complex of a connected graph, including this graph by their general theorem [1]; that result does not compute the induced homology representation. Donovan–Lin–Scoville [2] introduce relevant homotopy and strong-collapse methods, but do not give the present representation. Scoville–Zaremsky [3, Example 4.6] explicitly treat complete bipartite Morse complexes at the level of connectivity, not their full rational character. Donovan–Scoville [4] treat star-cluster homotopy types of other graph families. A publicly available exact calculation [5] already establishes the nonequivariant homotopy type \(\mathcal M(K_{3,3})\simeq\bigvee^{80}S^4\); **that is not part of the originality claim here**. The distinct claim is the complete \(S_3\wr C_2\) homology module and the new class-character and irreducible-multiplicity information.

## Limitations
The theorem concerns rational homology and its automorphism character for this canonical finite graph only; it makes no new integral-torsion claim, no stronger homotopy classification, and no claim for all complete bipartite graphs. A proof of non-coverage cannot exclude inaccessible, unpublished, or differently indexed sources, although the closest relevant full texts and the published nonequivariant result were compared. The verifier exhausts this finite complex; it is not an infinite-family proof.

## References
1. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907 (first public 2019-04-24), https://arxiv.org/abs/1904.10907.
2. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, https://arxiv.org/abs/1909.11440.
3. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, https://arxiv.org/abs/2004.10481.
4. C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized Morse complex*, arXiv:2207.13780, https://arxiv.org/abs/2207.13780.
5. *The Morse complex of \(K_{3,3}\) is a wedge of \(80\) four-spheres*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-morse-complex-of-k-3-3-is-a-wedge-of-80-four-spheres--ada39e4b9bea/RESULT.md.
