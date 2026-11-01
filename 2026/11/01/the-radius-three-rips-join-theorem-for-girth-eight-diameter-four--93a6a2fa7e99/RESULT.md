# The radius-three Rips join theorem for girth-eight diameter-four bipartite graphs

## Finding
Let \(G\) be any finite, connected, simple, bipartite graph with diameter exactly four and girth at least eight (the girth of a forest is infinite). Equip \(V(G)\) with the graph shortest-path metric, and use the **inclusive, unscaled** Vietoris–Rips filtration \(K_r=\operatorname{VR}_{\le r}(V(G),d_G)\), for real \(r\ge0\). Put \(n=|V(G)|\), \(e=|E(G)|\), and \(b=e-n+1\). Then

\[
K_r\simeq\begin{cases}
\bigvee^{n-1}S^0,&0\le r<1,\\
\bigvee^b S^1,&1\le r<3,\\
\bigvee^{b^2}S^3,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]

The zero-fold wedge is interpreted as a point. The inclusion \(K_1\hookrightarrow K_2\) is a simplicial-collapse equivalence. All reduced integral persistent homology groups are free, and the **entire reduced integral barcode**, including multiplicities, is: \(n-1\) intervals \([0,1)\) in degree zero, \(b\) intervals \([1,3)\) in degree one, and \(b^2\) intervals \([3,4)\) in degree three; all other intervals are absent.

For the incidence graph of any finite generalized quadrangle of order \((s,t)\), with integers \(s,t\ge1\), one has \(n=(st+1)(s+t+2)\) and \(b=s^2t^2\). Consequently its radius-three complex is a wedge of \(s^4t^4\) three-spheres. In particular, an order-\((3,3)\) symplectic quadrangle yields \(6561\) three-spheres. This is a uniform result over every existing generalized quadrangle, not merely the previously treated order-\((2,2)\) case.

## Assumptions and scope
A subset of vertices is a simplex of \(K_r\) precisely when every two of its vertices have graph distance at most \(r\). Distances are integers, so changes occur only at the four positive thresholds \(1,2,3,4\). Fix the bipartition \(V(G)=A\sqcup B\). Girth at least eight excludes four- and six-cycles. For vertices on opposite sides the distance is odd and, because the diameter is four, is either one or three. For distinct vertices on the same side, distance is two or four.

Let \(L_A\) be the clique complex on the vertex set \(A\), joining distinct vertices when they have a common neighbor in \(B\); define \(L_B\) symmetrically. These are finite simplicial complexes even when some vertex has degree one. No regularity, transitivity, thickness, or existence of a generalized quadrangle is required for the main assertion. The homotopy statements are ordinary, not equivariant; the barcode is over \(\mathbb Z\) and uses the usual inclusions of the filtration.

## Proof
**1. First two scales.** At \(r=0\) there are \(n\) isolated vertices. For \(1\le r<2\), \(K_r=G\), since \(G\) is bipartite and hence triangle-free. A finite connected graph has integral \(H_1\) free of rank \(b=e-n+1\). By Proposition 2.2 of Adamaszek [1], a graph of girth at least \(3j+1\) has a simplicial collapse \(\operatorname{Cl}(G^j)\searrow\operatorname{Cl}(G^{j-1})\) for \(j\ge2\) within the specified range. Taking \(j=2\), the girth bound is seven, so \(K_2\searrow K_1=G\). In particular the actual inclusion induces an integral isomorphism on \(H_1\). This establishes the first two nonzero homotopy stages and the persistence through the threshold two.

**2. Exact join at scale three.** Every two vertices on opposite bipartition sides have distance at most three, while distinct vertices on the same side have distance at most three exactly when they share an original neighbor. Thus every cross-side pair is an edge of the threshold-three graph, and its within-side induced graphs are precisely the one-skeletons of \(L_A\) and \(L_B\). Since Rips complexes are flag complexes, this gives the **literal simplicial identity**
\[
K_3=L_A*L_B.
\]

**3. A bipartite neighborhood-collapse lemma.** We show \(L_A\simeq G\), and symmetry gives \(L_B\simeq G\). Consider a clique \(C\subseteq A\) of size at least two. Choose distinct \(a,b\in C\). They have a common neighbor \(y\in B\), unique by the absence of four-cycles. Any third \(c\in C\) must also be adjacent to \(y\). Indeed, otherwise the common neighbors of \(a,c\) and of \(b,c\) differ from \(y\) and from one another (the latter follows again from absence of four-cycles); together with \(y\) these give the six-cycle \(a-y-b-y_{bc}-c-y_{ac}-a\), a contradiction. Applying the same argument to every other vertex of \(C\) shows that \(C\) lies in the neighbor set \(N_G(y)\). Singletons are also covered because the graph is connected and has no isolated vertices. Consequently
\[
L_A=\bigcup_{y\in B}\Delta(N_G(y)),
\]
where \(\Delta(S)\) is the full simplex on the set \(S\). Because there are no four-cycles, two distinct such neighborhood simplices share at most one vertex.

Adjoin a new vertex labeled \(y\) for every \(y\in B\) and attach the full simplex \(\Delta(N_G(y)\cup\{y\})\) along its opposite face \(\Delta(N_G(y))\). Denote the resulting complex by \(\widehat L_A\). Each attached simplex collapses back onto its opposite face; attachments with different apex labels have no faces in common outside \(L_A\). Hence \(\widehat L_A\searrow L_A\).

There is also an explicit collapse \(\widehat L_A\searrow G\). For each \(y\in B\), and in **descending order** of \(|\sigma|\), remove the pair
\[
(\sigma,\sigma\cup\{y\}),\qquad \sigma\subseteq N_G(y),\quad |\sigma|\ge2.
\]
Every pair is an elementary free-face removal: the absence of four-cycles makes each base face \(\sigma\) with two or more vertices belong to only one neighborhood block; larger cofaces have already been removed by the descending order. No pair alters an edge \(\{y,a\}\) with \(a\in N_G(y)\), and after all pairs exactly these edges and all vertices remain, giving the original bipartite graph \(G\). Thus \(L_A\simeq\widehat L_A\simeq G\). The same argument, with \(A,B\) interchanged, proves \(L_B\simeq G\).

**4. Topology of the join.** A finite connected graph with cycle rank \(b\) is homotopy equivalent to a wedge of \(b\) circles; when \(b=0\) it is contractible. The join of connected based CW complexes is homotopy equivalent to the reduced suspension of their smash product. Therefore
\[
K_3=L_A*L_B\simeq G*G\simeq
\Sigma\bigl((\bigvee^b S^1)\wedge(\bigvee^b S^1)\bigr)
\simeq\bigvee^{b^2}S^3.
\]
If \(b=0\), the join is contractible and the same zero-fold convention applies.

**5. Final scale, maps, and barcode.** Since \(G\) has diameter exactly four, \(K_r\) is the complete simplex on \(V(G)\) for every \(r\ge4\). At scales one and two, the graph's degree-one classes are carried isomorphically by the inclusion; at scale three there is no degree-one homology, so they all die exactly at three. No positive-degree reduced homology is present before one, and the degree-three classes appear only at three and disappear at four. The degree-zero classes die at one by connectedness. There are no torsion groups, and no unspecified extension maps. This proves the exact integral barcode.

**6. Generalized quadrangles.** A finite generalized quadrangle of order \((s,t)\) has \((st+1)(s+1)\) points, \((st+1)(t+1)\) lines, and \((st+1)(s+1)(t+1)\) incidences. Its incidence graph is bipartite, of girth eight and diameter four. Hence its cycle rank is
\[
 b=(st+1)\bigl((s+1)(t+1)-(s+1)-(t+1)\bigr)+1
 =(st+1)(st-1)+1=s^2t^2.
\]
Substitute this value into the main theorem. All displayed expressions are exact integers for every existing finite generalized quadrangle.

## Verification
Two independent standard-library Python programs accompany this statement. `verify.py` builds the eight-cycle, the \(3\)-by-\(3\) grid quadrangle, and the symplectic quadrangles \(W(2)\) and \(W(3)\) directly over finite prime fields. It checks diameter four, common-neighbor uniqueness, triangle common-center coverage, and computes the mod-two chain ranks of each within-part clique complex. The outputs give respective cycle ranks \(1,4,16,81\), and predicted radius-three third Betti numbers \(1,16,256,6561\). The \(W(3)\) complexes on each side have face vector \((40,240,160,40)\) and mod-two Betti vector \((1,81,0,0)\).

Independently, `crosscheck.py` uses the duad–syntheme model of the \(W(2)\) graph, enumerates **every** maximal threshold clique at scales zero through three, reconstructs all boundary matrices and reduces them exactly modulo two. At radius three it finds face vector \((30,315,1380,2475,1350,225)\) and mod-two Betti vector \((1,0,0,256,0,0)\). Both programs were run successfully; their verbatim output is in `verification_output.txt`. These finite checks are neither a substitute for the uniform proof nor a certification of integer homology by modular rank alone; integrality is established by the explicit collapses and join decomposition.

## Relationship to prior work
Adamaszek's graph-power collapse theorem [1] is the input controlling radius two; its stated girth hypothesis does **not** cover radius three for girth-eight graphs. The prior published computation [2] proves the \(256\)-sphere conclusion for the Tutte–Coxeter incidence graph \(GQ(2,2)\) by using its duad–syntheme structure. This specific numerical case is already known and is **not** claimed as a new result. The present theorem identifies a structural collapse applying to both color classes of every finite bipartite graph of diameter four and girth at least eight, yielding a uniform square-of-cycle-rank law; for generalized quadrangles this is the \(s^4t^4\) formula and, for \(W(3)\), the \(6561\)-sphere result.

McCabe [3, Section 3.1] uses generalized-polygon incidence graphs and the earlier girth-stability theorem to establish large persistent first homology through radius two (with a metric convention twice ours). The inspected statements concern that stable range and lower bounds for approximations, not the new radius-three join classification. The published particular case [2] and the stability theorem [1] are therefore logically weaker than the general radius-three theorem, although the methods and the particular case significantly motivate it. No universal prior statement covering the present conclusion was found in the inspected sources and indexed searches; undocumented equivalent work remains a possibility.

## Limitations
The theorem requires bipartiteness, graph diameter four and absence of cycles shorter than eight. It does not classify other generalized polygons, graphs with six-cycles, Euclidean point-cloud distances, quotient homotopy types, or equivariant integral representations. Although the proof is self-contained apart from the cited radius-two collapse theorem, the computational checks verify particular finite examples rather than the infinite quantifier. Independent review and a definitive exhaustive publication-priority assessment have not been performed.

## References
1. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first publicly posted 2011-04-03; Proposition 2.2 and Sections 2–3. Full-text HTML: https://arxiv.org/html/1104.0433v3 .
2. *The scale-3 Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, publicly posted research note, 2026-10-11, record identifier 9454ecd0bd54; full statement and proof inspected.
3. Kenneth McCabe, *Lower Bounds for Approximating the Vietoris-Rips Filtration*, arXiv:2607.06524, first publicly posted 2026-07-07; Proposition 3.4, Lemma 3.5 and Theorem 3.6.
4. *Quadrangle*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Quadrangle ; definitions of finite generalized quadrangles and their incidence parameters.
