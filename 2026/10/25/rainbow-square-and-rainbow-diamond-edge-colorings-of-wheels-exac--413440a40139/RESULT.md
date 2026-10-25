# Rainbow-square and rainbow-diamond edge colorings of wheels: exact indices and optimal-coloring census

## Finding

Let \(W_n=K_1\vee C_n\) be the wheel with one hub and exactly \(n\) rim vertices, where \(n\ge 3\). A \(B\)-edge-coloring is a proper edge coloring in which every four-cycle is rainbow. A \(D\)-edge-coloring is a proper edge coloring in which every diamond (a subgraph isomorphic to \(K_4\) with one edge omitted, not necessarily induced) is rainbow. Denote the least number of colors by \(q_B\) and \(\chi'_D\), respectively.

**Theorem (wheel-index rigidity and exact optimum census).** For each integer \(n\ge3\),

\[
q_B(W_n)=\begin{cases}6,&n=3,\\8,&n=4,\\n,&n\ge5,\end{cases}
\qquad
\chi'_D(W_n)=\begin{cases}6,&n=3,\\6,&n=4,\\n,&n\ge5.\end{cases}
\]

For every \(n\ge5\), the two families of optimal colorings are identical and have the following complete description. Write rim vertices as \(v_0,\ldots,v_{n-1}\) with subscripts modulo \(n\), the spokes as \(s_i=hv_i\), and the rim edges as \(e_i=v_iv_{i+1}\). Relabeling the \(n\) colors uniquely so that \(c(s_i)=i\), an optimal coloring is exactly an assignment

\[
c(e_i)=i+d_i\pmod n,\qquad d_i\in\{3,4,\ldots,n-2\},
\]

satisfying \(d_i\ne d_{i+1}+1\) for each cyclic \(i\), where this last comparison is between ordinary integer representatives in the displayed interval (and the last index is adjacent to the first). Every such word is valid. Put \(r=n-4\), and define the \(r\)-by-\(r\) zero-one matrix \(T_r\) by

\[
(T_r)_{u,v}=\begin{cases}0,&u=v+1,\\1,&u\ne v+1,\end{cases}
\qquad 1\le u,v\le r.
\]

The number of optimal edge colorings on the fixed wheel, modulo all permutations of color names, is exactly

\[
A_n=\operatorname{tr}(T_{n-4}^{\,n}),
\]

and the number using a prescribed palette of \(n\) named colors is \(n!A_n\). Thus \(A_5=1\), \(A_6=2\), \(A_7=367\), and \(A_8=11966\).

For \(n=3\) every edge must have a distinct color for both variants; there is one optimal coloring modulo colors and \(6!\) using six named colors. For \(n=4\), every \(B\)-optimal coloring uses eight different colors on the eight edges (one orbit, \(8!\) named colorings). A \(D\)-optimal coloring uses distinct colors on the four spokes and two further colors alternating on the four rim edges (one orbit, \(6!\) named colorings). The \(D\)-index statement for \(n=4\) is also an instance of a known general result for complete multipartite graphs and is included for completeness, not claimed separately as novel.

## Assumptions and scope

All graphs are finite, simple, undirected, and vertex-labeled for enumeration. Colorings of a fixed labeled graph are distinct when they assign different colors to some edge; color-name quotient is by the full symmetric group on exactly the optimal palette. A subgraph may omit existing ambient edges; in particular, a diamond counts inside \(K_4\). In the notation \(W_n\), \(n\) is the number of rim vertices, not the total number of vertices. The hub has degree \(n\), and each rim vertex has degree three when \(n\ge4\).

## Proof

**1. All four-cycles and diamonds for \(n\ge5\).** No three rim vertices form a triangle, and a cycle of length \(n\ge5\) has no four-cycle or diamond entirely among rim vertices. Every four-cycle consists of hub \(h\) plus three consecutive rim vertices, with edges \(hv_{i-1}\), \(v_{i-1}v_i\), \(v_iv_{i+1}\), \(v_{i+1}h\). Every diamond similarly consists of the three hub spokes to these vertices and the two consecutive rim edges. Indeed, five edges on four vertices containing the hub require three spokes and two rim edges, and the latter form a length-two path on the rim. Thus every four-cycle lies in the corresponding diamond, and the diamond consists of that four-cycle plus its fifth spoke. In a *proper* edge coloring the fifth spoke is already different from each of the other two spokes. The diamond is rainbow if and only if its four-cycle is rainbow. Therefore \(B\)- and \(D\)-coloring constraints coincide for \(n\ge5\).

**2. Color restrictions.** All \(n\) hub spokes are incident, so at least \(n\) colors are needed. In a coloring using exactly \(n\) colors, relabel them so \(c(s_i)=i\). For each rim edge \(e_i\), incidence excludes the spoke colors \(i\) and \(i+1\). The two consecutive-rim diamonds described above also exclude spoke colors \(i-1\) and \(i+2\). These four indices are distinct for \(n\ge5\), and no other spoke color is forbidden: these are exactly the diamond/four-cycle conflicts involving \(e_i\). Hence the allowable offsets are exactly \(d_i\in\{3,\dots,n-2\}\). The remaining restriction is properness at each rim vertex, meaning \(c(e_i)\ne c(e_{i+1})\), equivalently \(d_i\ne d_{i+1}+1\pmod n\). The largest possible absolute difference of the two offset representatives is \(n-5<n-1\), so the modular relation is equivalent to literal integer inequality \(d_i\ne d_{i+1}+1\). This includes the wraparound pair \((n-1,0)\) because the spoke-color index increases by one modulo \(n\). There are no other nonincident rim-edge conflicts for \(n\ge5\): each diamond contains two consecutive rim edges only.

**3. Construction and exact transfer count.** The constant offset word \(d_i=3\) meets the restrictions for all \(n\ge5\); hence \(q_B(W_n)=\chi'_D(W_n)=n\) and every optimum has the stated form. Set \(u_i=d_i-2\), so \(u_i\in\{1,\dots,r\}\) with \(r=n-4\). The local restriction becomes \((T_r)_{u_i,u_{i+1}}=1\). A closed walk of exactly \(n\) transitions in the index graph is precisely a cyclic word \((u_0,\ldots,u_{n-1})\); the trace counts all such words with their distinguished rim starting vertex. Any global color relabeling fixing the colors on all spokes fixes every palette color, so the symmetric-group action is free and each normalized coloring has precisely \(n!\) distinct named relabelings. This establishes the enumerators.

**4. Exceptional wheels.** For \(n=3\), the wheel is \(K_4\), and any pair of its six edges is incident or contained in some four-cycle (also in some diamond subgraph). Thus each of the six edges requires a distinct color in either variant. For \(n=4\), the spoke colors are distinct and, for each rim edge, its two endpoints and the two remaining rim vertices yield the diamond constraints excluding *all four* spoke colors. The rim edges themselves form a four-cycle. Under \(B\), that cycle is rainbow, so all four rim edges need distinct new colors, giving eight. Under \(D\), each diamond has only two neighboring rim edges, so the only constraints among the rim-edge colors are the cyclic adjacency conditions. Two fresh alternating colors therefore suffice, and one color does not suffice. Necessity of each described optimal pattern follows immediately. Every pattern admits the asserted factorial enumeration.

## Verification

The included standalone program `verify.py` reconstructs each wheel from edge lists and independently enumerates every four-cycle on four vertices and every five-edge diamond subgraph on four vertices, including diamonds inside complete graphs; it then forms all forbidden equal-color edge pairs. It directly confirms complete six-edge and eight-edge conflict structures at \(n=3,4\), coincidence of the two forbidden-pair systems for every \(5\le n\le12\), direct canonical coloring counts versus transfer traces for \(5\le n\le8\), and explicit colorings for \(5\le n\le15\). It also verifies the two-color alternating \(D\)-extension and its failure for \(B\) at \(n=4\). Observed stdout ends with `VERIFY_OK`. Finite tests corroborate but do not replace the general structural proof.

## Relationship to prior work

Gyárfás and Sárközy introduced \(B\)-coloring; Gyárfás, Martin, Ruszinkó and Sárközy subsequently established general planar bounds and the extended line-graph characterization. Wang introduced \(D\)-coloring and proved general degree-dependent bounds. Vuolo and Kong–Wang–Zheng studied improved planar \(B\)-coloring bounds. None of the inspected relevant statements supplies the exact wheel-family indices, complete optimal-coloring classification, or trace enumerator for \(n\ge5\). The known complete multipartite \(D\)-index formula gives \(\chi'_D(W_4)=6\) because \(W_4\cong K_{1,2,2}\); that numerical special case is *not* asserted to be independently new. Existing general inequalities (including \(q_B\ge\Delta\)) provide lower bounds only, not the structural construction or optimal-census conclusion. See the self-review for the bounded priority assessment and uninspected-source risk.

## Limitations

The all-parameter result concerns wheels only. No conclusion is asserted for arbitrary joins \(K_1\vee G\), arbitrary planar graphs, or palettes larger than the optimum. Colorings are counted on fixed labeled edges, with a separate quotient by global color-name permutations. The closest later planar-coloring paper was available only through its public abstract, so the literature comparison is not a certification of historical priority. No independent mathematical audit has been performed.

## References

1. R. Wang, *Proper edge coloring with rainbow diamonds*, arXiv:2606.06831 (first posted 2026-06-05). https://arxiv.org/abs/2606.06831.
2. Z. Lu, Q. Ying, and H. Song, *\((2,\mathcal F)\)-Avoiding Coloring and B-Coloring under Bipartite Exclusions*, arXiv:2609.39716 (2026). https://arxiv.org/abs/2609.39716.
3. A. Gyárfás and G. N. Sárközy, *“Less” Strong Chromatic Indices and the (7,4)-Conjecture*, Studia Sci. Math. Hungar. 60 (2023), 109–122, doi:10.1556/012.2023.01539.
4. A. Gyárfás, R. R. Martin, M. Ruszinkó, and G. N. Sárközy, *Proper edge colorings of planar graphs with rainbow \(C_4\)-s*, J. Graph Theory 107 (2024), 833–846, arXiv:2408.09059.
5. A. Vuolo, *On B-Colorings in Planar Graphs*, arXiv:2608.09787 (2026).
6. J. Kong, Y. Wang, and M. Zheng, *B-Coloring of Planar Graphs*, J. Graph Theory 113 (2026), 274–285, doi:10.1002/jgt.70067.
7. A. Gyárfás and G. N. Sárközy, *Proper Edge Colorings of Cartesian Products with Rainbow \(C_4\)-s*, Graphs Combin. 39 (2023), article 98, doi:10.1007/s00373-023-02697-x.
