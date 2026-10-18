# Integral equivariant \(\operatorname{MH}_{3,4}\) of the Shrikhande graph

## Finding

Write \(T=(\mathbb Z/4\mathbb Z)^2\), and let \(S=\operatorname{Cay}(T,U)\) be the sixteen-vertex Shrikhande graph, where
\[
U=\{\pm(1,0),\ \pm(0,1),\ \pm(1,1)\}.
\]
For every ordered vertex pair \((a,b)\), the endpoint-localized **integral** magnitude-homology group is
\[
\operatorname{MH}_{3,4}(S;a,b;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&d_S(a,b)=2,\\
0,&d_S(a,b)\in\{0,1\}.
\end{cases}
\tag{1}
\]
In particular, the known total rational rank \(144\) lifts to the torsion-free integral group \(\operatorname{MH}_{3,4}(S;\mathbb Z)\cong\mathbb Z^{144}\).

There is additional **equivariant** information not conveyed by the rank. Let
\[
P=\{A\in\operatorname{GL}_2(\mathbb Z/4\mathbb Z): A(U)=U\},\qquad
\Gamma=T\rtimes P=\operatorname{Aut}(S).
\]
The two \(P\)-orbits of nonneighbor displacements have representatives \(d_0=(0,2)\) and \(d_1=(1,2)\), of sizes \(3\) and \(6\), respectively. Write \(H_i=\{A\in P:Ad_i=d_i\}\). Then \(|H_0|=4\) and \(|H_1|=2\). Define characters \(\varepsilon_i:H_i\to\{\pm1\}\) by the following complete tables, in which \([a,b;c,d]\) denotes the matrix with rows \((a,b)\) and \((c,d)\), interpreted modulo four:

| Stabilizer | Matrices acting by \(+1\) | Matrices acting by \(-1\) |
| --- | --- | --- |
| \(H_0\) | \([1,0;0,1]\), \([3,0;3,1]\) | \([1,0;1,3]\), \([3,0;0,3]\) |
| \(H_1\) | \([1,0;0,1]\) | \([3,1;0,1]\) |

Here \(\mathbb Z_{\varepsilon_i}\) is the rank-one integral \(H_i\)-module with the displayed action. The **complete integral automorphism module** in this bidegree is
\[
\boxed{\operatorname{MH}_{3,4}(S;\mathbb Z)\cong
\operatorname{Ind}_{H_0}^{\Gamma}\mathbb Z_{\varepsilon_0}
\oplus\operatorname{Ind}_{H_1}^{\Gamma}\mathbb Z_{\varepsilon_1}.}\tag{2}
\]
The groups \(H_i\) are embedded in \(\Gamma\) as linear automorphisms fixing the ordered pair \((0,d_i)\). On the translation subgroup \(T\), the right side restricts to \(\mathbb Z[T]^{\oplus9}\). Neither induced summand has a nonzero \(\Gamma\)-invariant vector; hence
\[
\operatorname{MH}_{3,4}(S;\mathbb Z)^{\Gamma}=0,
\quad
\big(\operatorname{MH}_{3,4}(S;\mathbb Z)\big)_{\Gamma}
\cong(\mathbb Z/2\mathbb Z)^2.
\tag{3}
\]

## Assumptions and scope

All homology is the original signed integral magnitude homology of a finite simple undirected graph with the shortest-path metric. The chain group \(C_{k,4}(a,b)\) is free abelian on all ordered sequences \((x_0,\ldots,x_k)\) with \(x_0=a\), \(x_k=b\), adjacent sequence elements distinct, and \(\sum_{i=0}^{k-1}d(x_i,x_{i+1})=4\). Its differential deletes an interior vertex \(x_i\) with coefficient \((-1)^i\) only if \(d(x_{i-1},x_{i+1})=d(x_{i-1},x_i)+d(x_i,x_{i+1})\); all other deletions vanish. This fixes the sign and normalization convention.

The bidegree \((3,4)\), the displayed graph, and its full automorphism group are the exact scope. A claim about rational ranks alone is not new: that computation appears in Gu (2018, Appendix A).

## Proof

**1. Complete endpoint and symmetry reduction.** Construct the graph from the six generators above. Exact breadth-first shortest-path enumeration gives distance distribution \((1,6,9)\) at each vertex. Enumerating the matrices preserving \(U\) yields twelve elements in \(P\); translations and these matrices give 192 different automorphisms. Brouwer's independent graph record gives \(|\operatorname{Aut}(S)|=192\), so this subgroup is all of \(\Gamma\). On displacements relative to \(0\), \(P\) has precisely four orbits, represented by \(0\), \((1,0)\), \((0,2)\), and \((1,2)\), of sizes \(1,6,3,6\). Thus every one of the 256 ordered endpoint pairs belongs to one of these four representatives after an automorphism.

**2. Exact integral boundary calculation.** Exhaustively generate all signed length-four magnitude chains of degrees \(2,3,4\) for each representative. Write \(\partial_k\) for the corresponding integer matrix. The complete exact calculations are:

| Displacement \(b-a\) | \(\operatorname{rank}C_{2,4}\) | \(\operatorname{rank}C_{3,4}\) | \(\operatorname{rank}C_{4,4}\) | \(\operatorname{rank}\partial_3\) | Nonzero Smith factors of \(\partial_4\) | \(\operatorname{rank}H_3\) |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| \((0,0)\) | 9 | 54 | 96 | 9 | forty-five \(1\)'s | 0 |
| \((1,0)\) | 6 | 54 | 80 | 6 | forty-eight \(1\)'s | 0 |
| \((0,2)\) | 4 | 66 | 80 | 4 | sixty-one \(1\)'s | 1 |
| \((1,2)\) | 4 | 66 | 80 | 4 | sixty-one \(1\)'s | 1 |

All four products \(\partial_3\partial_4\) vanish exactly. Every nonzero integer Smith invariant of \(\partial_4\) equals \(1\), proving its image is primitive in \(C_{3,4}\). Therefore \(\ker\partial_3/\operatorname{im}\partial_4\), a subgroup of the torsion-free quotient \(C_{3,4}/\operatorname{im}\partial_4\), is torsion-free. Its rank is \(\operatorname{rank}C_{3,4}-\operatorname{rank}\partial_3-\operatorname{rank}\partial_4\), yielding (1). There are \(16\cdot9=144\) nonadjacent ordered endpoints. In fact the nonzero Smith factors of \(\partial_3\) are all also \(1\), so it is surjective onto \(C_{2,4}\), giving \(H_2=0\) for these fixed-length endpoint complexes.

**3. Signed stabilizer characters.** For each \(i=0,1\), compute the integer \(\partial_4\) and a nonzero rational class \([w_i]\) in \(\ker(\partial_4^\mathsf T)/\operatorname{im}(\partial_3^\mathsf T)\), which is one-dimensional. The included certificate records a signed cocycle witness with support on twelve or fourteen basis chains, respectively. For each of the four (respectively two) matrices fixing \(d_i\), relabel the full ordered chain basis and check exactly that \(A^*w_i-\varepsilon_i(A)w_i\) lies in \(\operatorname{im}(\partial_3^\mathsf T)\), for exactly one sign. These tests yield precisely the two tables above. Since localized \(H_3\cong\mathbb Z\), its induced integral automorphism is also the corresponding sign: the dual rank-one action has the same sign.

**4. Induction and consequences.** Endpoint-localized chain groups are preserved under the diagonal vertex action of \(\Gamma\). The 144 nonadjacent ordered endpoints split into two \(\Gamma\)-orbits, with representative stabilizers \(H_0,H_1\), and each localized homology fiber is a rank-one \(\mathbb Z\)-module carrying \(\varepsilon_i\). The direct sum over an orbit is exactly the induced module from its stabilizer. This proves (2). The translation subgroup acts freely on each fixed displacement, providing nine regular summands on restriction. Frobenius reciprocity and the nontriviality of both characters give no invariant vectors; induction followed by coinvariants gives two copies of \(\mathbb Z/2\), proving (3).

## Verification

All numerical and signed claims above were recomputed by the embedded standalone `verify.py` using Python and SymPy exact integer matrices. Run `python verify.py` alongside `certificate.json` after installing `requirements.txt`. The script constructs the graph and shortest paths, enumerates the full symmetry group, independently generates each complete magnitude-chain basis, tests \(\partial_3\partial_4=0\), computes all integer Smith factors, tests each signed cocycle class under every stabilizer element, and checks its output against the embedded `certificate.json`. The exact success marker is `VERIFY_SHRIKHANDE_INTEGRAL_MAGNITUDE_EQUIVARIANT_OK`. No finite-size extrapolation is involved: the four orbit representatives exhaust the entire finite graph and its complete automorphism action.

## Relationship to prior work

Gu's *Graph magnitude homology via algebraic Morse theory* (2018), Appendix A, Proposition A.2 and Tables 1–2, already reports the rational rank \(144\) for the Shrikhande graph in bidegree \((3,4)\) and rank zero for the four-by-four rook graph; the distinct numerical rank is **not claimed as new here**. The new statement is the full integral endpoint-support and torsion classification, together with the signed action of every graph automorphism, specifically the two nontrivial stabilizer characters. Asao and Izumihara develop endpoint-complex methods, but the inspected treatment does not provide this graph-specific integral and equivariant classification. Sazdanovic and Summers show why rational rank alone cannot generally rule out integral torsion. Brouwer's graph record supplies an independent full-group order and orbit comparison. No inspected published or mathematical-record result was found whose statement implies the signed integral induced-module decomposition.

## Limitations

Only the single magnitude bidegree \((3,4)\) is classified. Other bidegrees and graph families are not covered. The result makes no claim of an independently audited computation or of exhaustive literature coverage; equivalent unindexed work remains possible. The previously published rational rank and rook-graph contrast are background rather than new findings.

## References

1. Y. Gu, *Graph magnitude homology via algebraic Morse theory*, arXiv:1809.07240 (2018), especially Appendix A, Proposition A.2 and Tables 1–2. https://arxiv.org/abs/1809.07240
2. Y. Asao and K. Izumihara, *Geometric approach to graph magnitude homology*, arXiv:2003.08058 (2020). https://arxiv.org/abs/2003.08058
3. R. Sazdanovic and V. Summers, *Torsion in the magnitude homology of graphs*, arXiv:1912.13483 (2019). https://arxiv.org/abs/1912.13483
4. Y. Tajima and M. Yoshinaga, *Magnitude homology of graphs and discrete Morse theory on Asao–Izumihara complexes*, arXiv:2110.02458 (2021). https://arxiv.org/abs/2110.02458
5. A. E. Brouwer, *Shrikhande graph*, graph record, https://aeb.win.tue.nl/graphs/Shrikhande.html (graph description and automorphism group order).
