# Scale-two Rips collapses of unbounded-width cyclic clique cylinders

## Finding
For integers \(n\ge7\), \(m\ge3\), consider the shortest-path metric on \(G_{n,m}=C_n\square K_m\). Let \(R_j\) be the inclusive graph-metric Vietoris–Rips complex at threshold \(j\). There is a simplicial elementary collapse
\[
R_2\searrow C_n
\]
onto the cycle using the fixed color \(0\) in all fibers, with precisely
\[
N(n,m)=\frac n2\left(4^m+(m-1)2^m-2\right)
\]
elementary free-face pairs. At scale one, \(R_1\simeq\bigvee^{n(m-1)+1}S^1\). The inclusion \(R_1\hookrightarrow R_2\) induces a surjection on integral first homology, with kernel \(\mathbb Z^{n(m-1)}\). This describes the positive-degree persistence through threshold \(2\): exactly \(n(m-1)\) degree-one classes die at threshold \(2\), and one class survives past that threshold.

## Assumptions and scope
The vertex set is \(\mathbb Z/n\mathbb Z\times\{0,\ldots,m-1\}\); distinct vertices \((i,a),(j,b)\) are adjacent in \(G_{n,m}\) precisely when \(i=j\) and \(a\ne b\), or \(a=b\) and \(i,j\) are consecutive on \(C_n\). Thus their distance is \(d_{C_n}(i,j)+\mathbf1_{a\ne b}\). A simplex in \(R_j\) is a nonempty finite set whose pairwise distances are at most \(j\). Both parameters are unbounded within the stated inequalities. The ordinary graph metric, not the continuous metric graph, is intended.

## Proof
A pair at distance at most two either lies in the same fiber, in consecutive fibers (arbitrary colors), or in fibers at cyclic distance two with equal colors. The last edges are \(e_{i,a}=\{(i-1,a),(i+1,a)\}\). For \(n\ge7\), the complete common-neighbor link of \(e_{i,a}\) in \(R_2\) is exactly the simplex on the \(m\) vertices of the middle fiber \(V_i\). In particular, a simplex cannot contain two distinct distance-two edges. Fix \((i,0)\in V_i\), and for each \(e_{i,a}\) pair every simplex \(e_{i,a}\cup\sigma\), with \(\sigma\subseteq V_i\setminus\{(i,0)\}\), against \(e_{i,a}\cup\sigma\cup\{(i,0)\}\). Process these pairs by decreasing size of \(\sigma\). Every lower simplex is then free, because any other containing face involving that distance-two edge has already been removed, and no face can contain two such edges. For each of \(nm\) distance-two edges this gives \(2^{m-1}\) elementary collapses.

The remaining flag complex \(K\) has exactly those nonempty simplices supported in one fiber \(V_i\) or the union of two consecutive fibers \(V_i\cup V_{i+1}\). All such consecutive-pair unions are simplices of size \(2m\). Every vertex \((i,a)\) with \(a\ne0\) is dominated in this complex by \((i,0)\): any face containing \((i,a)\) but not \((i,0)\) remains a face after adding \((i,0)\). Pair these faces with their extensions by \((i,0)\), processing decreasing face size; this is a succession of elementary collapses removing the dominated vertex. Perform this for all nonzero colors and all fibers. The surviving complex is the flag complex of the length-\(n\) cycle on \((i,0)\), which is the cycle itself since \(n\ge7\).

Counting nonempty simplices of \(K\) from its \(n\) maximal \(2m\)-vertex simplices, each pairwise consecutive overlap being an \(m\)-vertex fiber, gives exactly \(n(2^{2m}-2^m)\) faces. The final cycle has \(2n\) nonempty faces. Thus the second stage has \(n(2^{2m}-2^m-2)/2\) pairs. Together with the first-stage \(nm2^{m-1}\) pairs, this gives the formula for \(N(n,m)\). No dimension restriction occurs in either stage; maximal simplex dimension grows as \(2m-1\).

At threshold one, each fiber contributes a contractible \((m-1)\)-simplex, and the remaining edges are the \(nm\) parallel-color links between consecutive fibers. This is a connected graph of contractible spaces with first Betti number \(nm-n+1=n(m-1)+1\), hence has the claimed graph homotopy type. One fixed-color rim cycle already belongs to \(R_1\) and maps to the generator of \(H_1(R_2;\mathbb Z)\) under the retraction. The inclusion on \(H_1\) is therefore surjective, and its kernel is free of the claimed rank.

## Verification
The standalone script `check_cyclic_clique.py` reconstructs flag complexes from all shortest-path distances, independently enumerates faces from maximal cliques, and verifies each proposed elementary collapse by checking the free-face condition against the entire current complex. It checks \((n,m)=(7,3),(8,3),(9,3),(7,4),(8,4),(7,5)\), including all claimed pair counts. The infinite proof is the uniform link and dominance argument above; finite checks do not replace it.

## Relationship to prior work
Saleh, Titz Mite, and Witzel classify graph-metric Vietoris–Rips complexes of vertices of the five Platonic solids, and explicitly discuss extending the setting to other structured vertex sets. That classification does not cover \(C_n\square K_m\) for unbounded \(n,m\). Adamaszek and collaborators analyze metric gluing constructions but do not supply the present clique-fiber collapse or scale-one-to-two persistence computation. A previously recorded width-two circular-ladder collapse has the special-case count \(9n\), recovered by formally setting \(m=2\) in the formula here; that width-two result does not imply any case \(m\ge3\), where maximal simplex dimensions become unbounded. The statement is not a claim about generic metric cylinders or full persistence beyond threshold two.

## Limitations
No assertion is made for \(n<7\), for threshold \(j\ge3\), or for Vietoris–Rips complexes of continuous metric graphs. The scale-two homotopy equivalence does not imply that the persistent generator survives all larger thresholds. Literature indexing can miss equivalent constructions under different names. Independent validation has not been performed.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), especially introductory theorem and Section 2. https://arxiv.org/html/2302.14388v1
2. M. Adamaszek et al., *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.3
