# A four-phase parity-dynamics law on distance-three Boolean cubes

## Finding
Let \(n\ge3\) and let \(Q=2^f\) for any integer \(f\ge1\). Index \(Q^{2^n}\) configurations by binary words \(v\in\{0,1\}^n\); their values lie in \(\mathbb F_Q\). In one synchronous update, each word receives the sum of its \(\binom n3\) neighbors at Hamming distance exactly three. Denote this linear update by \(A_n\), acting on a vector space of dimension \(N=2^n\) over \(\mathbb F_Q\).

For every \(n\ge3\), the update satisfies
\[
 A_n^2=\begin{cases}I,&n\equiv3\pmod4,\\0,&n\not\equiv3\pmod4.\end{cases}
\]
Its complete rank profile is
\[
\operatorname{rank}_{\mathbb F_Q}A_n=\begin{cases}
 2^{n-1},&n\equiv0\pmod4,\\
 2^{n-1}-2^{(n-1)/2},&n\equiv1\pmod4,\\
 2^{n-2}-2^{n/2-1},&n\equiv2\pmod4,\\
 2^n,&n\equiv3\pmod4.
\end{cases}
\]
When \(n\equiv3\pmod4\), \(\operatorname{rank}(A_n-I)=2^{n-1}\). For \(n\not\equiv3\pmod4\), put \(r=\operatorname{rank}(A_n)\). The exact first-entry populations at the zero fixed point are
\[
  N_0=1,\qquad N_1=Q^{N-r}-1,\qquad N_2=Q^N-Q^{N-r}.
\]
There are no other periodic states and the maximum extinction time is exactly two. If \(n\equiv3\pmod4\), every state is periodic from time zero: there are exactly \(Q^{N/2}\) fixed states and \((Q^N-Q^{N/2})/2\) primitive two-cycle orbits.

A structural refinement is that in the nilpotent cases the dimension of \(\ker A_n/\operatorname{im}A_n\) is exactly \(0\), \(2^{(n+1)/2}\), or \(2^{n-1}+2^{n/2}\) when \(n\equiv0,1,2\pmod4\), respectively. These values distinguish a maximal-rank square-zero phase, a small exceptional homology phase, and a large exceptional homology phase.

## Assumptions and scope
The vertex set is the *full* binary \(n\)-cube, but adjacency in the update is defined by Hamming distance exactly three, not distance at most three and not ordinary cube adjacency. Graph edges are undirected and simple, updates are simultaneous and **open-neighborhood** sums, and every vertex has a label; no quotient by graph automorphisms is used when counting configurations. Addition takes place in any finite field of characteristic two. Least-period-one states include the zero state; a transient state is not counted as periodic at time zero. The boundary \(n=3\) is included (its graph is a perfect matching); the theorem does not make assertions for \(n<3\), for other Hamming distances, or for odd characteristic.

## Proof
**1. Convolution model.** Let \(G=(\mathbb Z/2\mathbb Z)^n\). The state space has the group-algebra basis \(g_S\), \(S\subseteq[n]\), where \(g_S\) translates a word by flipping coordinates in \(S\). The update is multiplication by \(a_n=\sum_{|S|=3}g_S\) in \(\mathbb F_Q[G]\). As every \(g_S^2=1\), and distinct cross terms cancel in characteristic two, \(a_n^2=\binom n3\cdot1\). The parity of \(\binom n3\) equals one precisely when the lowest two binary digits of \(n\) are both one; thus it is one precisely when \(n\equiv3\pmod4\).

**2. Squarefree coordinates.** Put \(y_i=1+g_{\{i\}}\), so \(y_i^2=0\). These variables give the entire group algebra as \(R_n=\mathbb F_Q[y_1,\ldots,y_n]/(y_1^2,\ldots,y_n^2)\). Write \(e_j\) for the degree-\(j\) elementary symmetric polynomial in the \(y_i\), with \(e_0=1\). Expanding each \(g_S=\prod_{i\in S}(1+y_i)\) yields
\[
 a_n=\sum_{j=0}^3 \binom{n-j}{3-j}e_j,
\]
where integer coefficients are reduced modulo two. Hence, in the four residue classes \(n\bmod4\), the multiplier \(a_n\) is respectively
\[
  e_1+e_3,\quad e_2+e_3,\quad e_3,\quad1+e_1+e_2+e_3.
\]
In the squarefree algebra, \(e_1e_2=e_3\) because each triple is formed exactly three times and the other products vanish. Moreover every positive-degree element squares to zero, and \(1+u\) is invertible whenever \(u\) has zero constant term.

**3. Rank of multiplication by \(e_2\).** Let \(R_m\) be a squarefree polynomial algebra over a field of characteristic two, and \(D_m\) multiplication by \(e_2(y_1,\ldots,y_m)\). The skew-symmetric coefficient matrix of this quadratic exterior element has zeros on its diagonal and ones elsewhere. Its rank is \(m\) when \(m\) is even and \(m-1\) when \(m\) is odd: the kernel equation is \(v+(\sum_i v_i){\boldsymbol1}=0\), whose only solutions are zero for even \(m\), and the multiples of \({\boldsymbol1}\) for odd \(m\). An invertible linear change of squarezero generators therefore carries this quadratic element to \(u_1v_1+\cdots+u_sv_s\), where \(s=\lfloor m/2\rfloor\), with one unused generator if \(m\) is odd. (This is the elementary symplectic normal form of an alternating bilinear matrix; it is classification of an exterior degree-two element, not of a characteristic-two quadratic function.)

On each pair factor \(\mathbb F_Q[u_i,v_i]/(u_i^2,v_i^2)\), multiplication by \(u_iv_i\) has one length-two nilpotent chain \(1\mapsto u_iv_i\mapsto0\) and two isolated kernel vectors \(u_i,v_i\). Its homology \(\ker D/\operatorname{im}D\) has dimension two. Over characteristic two, multiplication by the sum \(\sum_i u_iv_i\) is the tensor-product differential. The elementary tensor-product homology decomposition gives dimension \(2^s\), multiplied by two if an unused generator remains. Because \(D_m^2=0\), the rank is half the dimension of \(R_m\) minus half the homology dimension. Thus
\[
 \operatorname{rank}D_m=\begin{cases}
 2^{m-1}-2^{m/2-1},&m\text{ even},\\
 2^{m-1}-2^{(m-1)/2},&m\text{ odd}.
 \end{cases}
\]
The tensor-product homology claim can also be checked without invoking a theorem: a basis for each pair splits into a two-term acyclic subcomplex with vectors \(1,uv\), and a zero-differential two-dimensional subspace spanned by \(u,v\). Every tensor summand containing an acyclic factor is acyclic, leaving precisely the product of the zero-differential two-dimensional factors (and, when present, the free unused generator).

**4. Rank in the four cases.** For \(n\equiv0\pmod4\), \(a_n=e_1(1+e_2)\). Since \(1+e_2\) is a unit and \(e_1\) is a nonzero linear generator, multiplication by \(e_1\) has rank \(2^{n-1}\). For \(n\equiv1\pmod4\), \(a_n=e_2(1+e_1)\), so its rank is the \(e_2\)-rank in \(n\) (odd) variables, given in step 3. For \(n\equiv2\pmod4\), \(a_n=e_3=e_1e_2\). Choose the linear generator \(z=e_1(y_1,\ldots,y_n)\), keeping \(y_1,\ldots,y_{n-1}\) as other generators. Since \(y_n=z+\sum_{i<n}y_i\), reduction modulo \(z\) takes \(e_2(y_1,\ldots,y_n)\) to \(e_2(y_1,\ldots,y_{n-1})\). Hence \(e_3=z e_2(y_1,\ldots,y_{n-1})\); its multiplication rank is exactly the \(e_2\)-rank on \(n-1\) (odd) variables, as stated.

For \(n\equiv3\pmod4\), \(a_n=1+e_1+e_2+e_3\) and \(a_n^2=1\), so the update is invertible and every orbit has period dividing two. To count fixed states, use \(z=e_1\), \(m=n-1\), \(S=\sum_{i=1}^m y_i\) and \(q=e_2(y_1,\ldots,y_m)\). Then \(e_2(y_1,\ldots,y_n)=q+zS\) and \(e_3=zq\), so
\[
 a_n-1=q+z(1+S+q).
\]
Writing an arbitrary vector as \(b+zc\) in \(R_m\oplus zR_m\), multiplication by \(a_n-1\) is
\[
 (b,c)\longmapsto\bigl(qb,\, (1+S+q)b+qc\bigr).
\]
Here \(q^2=0\), and \(1+S+q\) is a unit. The kernel is parametrized uniquely by arbitrary \(c\), with \(b=(1+S+q)^{-1}qc\); its dimension is therefore \(2^m=2^{n-1}\), proving the fixed-subspace count.

**5. State counts and boundaries.** In the square-zero cases, \(\operatorname{im}A_n\subseteq\ker A_n\); every state reaches zero by update two. There are \(Q^{N-r}\) initial states in \(\ker A_n\), including zero itself. The kernel is proper because all three noninvertible ranks are positive for \(n\ge3\). This proves the sharp time-two bound and the stated exact first-entry counts. In the involutive case all states satisfy \(A_n^2x=x\); fixed states are the kernel of \(A_n-I\), and all others fall into disjoint pairs. The homology dimensions in the square-zero cases are \(N-2r\). Each assertion follows for every \(n\ge3\) and every finite field of characteristic two, without extrapolation from computations.

## Verification
Three standalone Python 3 programs accompany this result. `verify_graph.py` constructs the actual distance-three adjacency operator and checks the predicted rank and the exact square identity for all \(3\le n\le11\), as well as the fixed-subspace rank for \(n=3,7,11\). `verify_algebra.py` independently checks the group-to-squarefree coordinate transformation, the four expressions for the multiplier, and 20 independently sampled states for each \(3\le n\le11\). `verify_forms.py` checks graded multiplication ranks of the two exterior elementary-symmetric elements for all \(2\le n\le12\). The files ending `.out` are captured runs of exactly these packaged sources. Finite checks corroborate algebraic steps but are not the proof of the infinite family.

## Relationship to prior work
Wolfram's 1983 survey and Martin–Odlyzko–Wolfram's 1984 work establish cellular-automaton state-transition and additive-map methods, but their studied one-dimensional translation rules do not supply the distance-three Boolean-cube rank law. Peeters's 2002 Hamming-graph section treats open-neighbor distance-one adjacency matrices, including their modular ranks, not the separate distance-three relation. Fish–Key–Mwambene's 2009 Hamming-graph code computations are also for distance-one neighborhoods, and emphasize ternary-alphabet graphs. Hanaki–Yoshikawa (2005) classifies modular standard modules for association schemes of class two, whereas the binary Hamming scheme here has class \(n\ge3\); its hypotheses do not cover this family. Yoshikawa's full 2003 proceedings article (2002 symposium), pages 133–138, explicitly determines the abstract modular Hamming-scheme adjacency algebra (Theorems 2.4 and 3.4), but does not give the rank of the distance-three adjacency matrix on the full standard vertex space or a dynamical first-entry count. The later 2004 journal article is related but was not read in full; its inaccessible text leaves a residual possibility of additional standard-module results. A separately published distance-two Boolean-cube parity census is also pertinent, but its stated claims are about distance exactly two, whereas the cubic multiplier here has different modular ranks and square-root-sized correction terms. No claim is made that the general group-algebra technique, symplectic normal form, or the small \(n=3,4\) examples are new.

## Limitations
The originality assessment concerns the explicit four-class distance-three rank and dynamical census, **not** finite-field linear algebra or the abstract fact that parity-convolution operators square to a scalar. No exhaustive index of older papers is possible. Relevant published sources not read in full, including Yoshikawa's later 2004 journal article and the nearby distance-two census, leave a residual possibility of stronger standard-module statements implying the present formulas; the accessible descriptions alone do not justify a definitive not-covered judgement for those works. This work supplies an internal proof and checks, not an independent audit or external certification.

## References
1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics **55** (1983), 601–644, published 1983-07-01, DOI 10.1103/RevModPhys.55.601.
2. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics **93** (1984), 219–258, DOI 10.1007/BF01223745.
3. R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics **15** (2002), 127–149, https://emis.de/ft/43347.
4. W. Fish, J. D. Key and E. Mwambene, *Codes, designs and groups from the Hamming graphs*, Journal of Combinatorics, Information & System Sciences **34** (2009), 169–182, https://www.researchgate.net/publication/268301204_Codes_designs_and_groups_from_the_Hamming_graphs.
5. M. Yoshikawa, *Modular adjacency algebras of the Hamming association schemes*, Proceedings of the 35th Symposium on Ring Theory and Representation Theory, Okayama, published January 2003, pp. 133–138, https://ring-theory-japan.com/ring/oldmeeting/old-proc/ring-sympo/%282002%29.pdf (full text inspected).
6. M. Yoshikawa, *Modular adjacency algebras of Hamming schemes*, Journal of Algebraic Combinatorics **20** (2004), 331–340, DOI 10.1023/B:JACO.0000048521.68503.2b (abstract examined; full text not available).
7. A. Hanaki and M. Yoshikawa, *On modular standard modules of association schemes*, Journal of Algebraic Combinatorics **21** (2005), 269–279, https://studylib.net/doc/10958735/on-modular-standard-modules-of-association-schemes (full text introduction and scope inspected).
8. *A mod-four orbit census for parity automata on distance-two Boolean cubes*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-mod-four-orbit-census-for-parity-automata-on-distance-two-bool--f288ef2fe8b4 (searchable abstract only).
