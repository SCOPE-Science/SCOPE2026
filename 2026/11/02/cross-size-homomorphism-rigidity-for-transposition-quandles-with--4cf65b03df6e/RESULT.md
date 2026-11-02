# Cross-size homomorphism rigidity for transposition quandles with a unique four-vertex quotient

## Finding
For integers \(n\ge 3\) and \(m\ge 2\), let \(T_n\) be the quandle of transpositions in the symmetric group \(S_n\), with \(x\triangleright y=yxy\). Equivalently its elements are the two-element subsets of \(\{1,\ldots,n\}\), and conjugation replaces each endpoint by its image under the transposition represented by \(y\).

**Classification.** Every quandle homomorphism \(T_n\to T_m\) is exactly one of the following: a constant map; an injection induced by an injection of the underlying \(n\)-element vertex set into the \(m\)-element vertex set; or, exclusively when \(n=4\), a rank-three map obtained by first identifying the three pairs of opposite edges of \(K_4\), giving \(T_3\), and then embedding \(T_3\) as the three edges of a triangle in \(K_m\). These classes are disjoint. For \(n=3\), the second type is the triangle embedding, and the third type is not counted separately.

Writing \((m)_n=m!/(m-n)!\) when \(m\ge n\) and \((m)_n=0\) otherwise, the resulting complete Hom-set cardinality is
\[
\lvert\operatorname{Hom}(T_n,T_m)\rvert=\binom m2+\begin{cases}
6\binom m3,&n=3,\\
(m)_4+6\binom m3,&n=4,\\
(m)_n,&n\ge5.
\end{cases}
\]
The rank distribution is exactly the decomposition just stated: rank one has multiplicity \(\binom m2\); rank three has multiplicity \(6\binom m3\) for \(n=3,4\); rank six has multiplicity \((m)_4\) for \(n=4\); and rank \(\binom n2\) has multiplicity \((m)_n\) for \(n\ge5\). Zero multiplicities are omitted when a rank cannot fit the target.

In particular, for \(n\ge5\), every nonconstant endomorphism of \(T_n\) is a vertex-permutation automorphism. For \(T_4\), the rank-three endomorphisms form a \(24\)-element multiplicative subsemigroup isomorphic to the direct product of \(S_3\) with the four-element left-zero semigroup (operation \(a\cdot b=a\)). Consequently \(T_4\) has exactly four rank-three idempotent endomorphisms.

## Assumptions and scope
All sets are finite. The source has \(n\ge3\) vertices and target has \(m\ge2\) vertices. The operation convention is the right-conjugation quandle \(x\triangleright y=yxy\); because transpositions are involutions, this is a quandle. An edge of \(K_r\) is a two-element vertex subset; its quandle product with another edge is the latter edge's endpoint swap acting on the former. Two distinct edges commute under this operation if and only if they are disjoint. Two distinct intersecting edges have the same product in either order, namely the third edge of the triangle they span.

The phrase *rank* means cardinality of the image of a homomorphism, not the rank of a group or a matrix. No ring or field is involved. The theorem does not classify all maps into arbitrary quandles.

## Proof
**Step 1: Adjacent source edges cannot have distinct disjoint images.** Suppose \(a,b\) are distinct intersecting source edges. Then \(a\triangleright b=b\triangleright a=c\), the third triangle edge. If \(f(a),f(b)\) were disjoint, their products in the target would equal their respective first factors, forcing \(f(a)=f(c)=f(b)\), a contradiction. Therefore distinct images of adjacent source edges intersect.

**Step 2: Collapsing an adjacent pair forces a constant map.** By relabeling suppose \(f(12)=f(13)=t\). Then \(f(23)=t\). Fix \(k\notin\{1,2,3\}\), and put \(u=f(1k)\). As \(12\) and \(1k\) meet, Step 1 says \(u=t\) or the two target edges meet. Suppose \(u\ne t\). Then \(v=t\triangleright u\) is a third triangle edge distinct from \(t,u\). Since \(12\triangleright 1k=2k\) and \(13\triangleright 1k=3k\), both \(2k,3k\) map to \(v\). But \(23\triangleright 2k=3k\) implies \(t\triangleright v=v\), whereas the two distinct intersecting edges \(t,v\) have \(t\triangleright v=u\ne v\). Contradiction. Thus \(f(1k)=t\), and all \(2k,3k\) map to \(t\). Finally for \(j,k\not=1\), the identity \(1j\triangleright 1k=jk\) shows \(f(jk)=t\). Hence \(f\) is constant. The case \(n=3\) follows already from the initial triangle; for larger \(n\), the argument applies to every additional vertex. It follows that any nonconstant map separates every two adjacent edges.

**Step 3: For \(n\ge5\), nonconstant maps come from vertex injections.** For each source vertex \(i\), the \(n-1\ge4\) edges incident with \(i\) map to pairwise distinct, pairwise intersecting edges of \(K_m\). Any family of at least four pairwise intersecting distinct edges has a unique common vertex: a family not contained in a star has at most the three edges of one triangle. Call this target vertex \(\sigma(i)\).

Suppose \(\sigma(i)=\sigma(j)=v\) for distinct source vertices \(i,j\). If some \(k\) has \(\sigma(k)\ne v\), then the images of \(ik\) and \(jk\) are both forced to be the single edge \(\{v,\sigma(k)\}\), contradicting Step 2 since these source edges are adjacent. Otherwise every \(\sigma(k)=v\), and all image edges contain \(v\). Because disjoint source edges commute, their image edges must commute; distinct star edges cannot commute. Therefore the images of \(12,34,35\) are all equal (since \(12\) is disjoint from both \(34\) and \(35\)), again contradicting Step 2. This uses five distinct source vertices. Thus \(\sigma\) is injective.

The image of \(ij\) lies in the target stars centered at both \(\sigma(i)\) and \(\sigma(j)\). Since the centers are different, it is precisely \(\{\sigma(i),\sigma(j)\}\). Conversely any injection of vertex sets induces a quandle embedding by conjugation. Different injections induce distinct quandle maps for \(n\ge3\), proving the \((m)_n\) term.

**Step 4: The three-vertex source.** Any nonconstant \(T_3\to T_m\) separates the three edges (Step 2). These edges form a triangle and their two-by-two quandle products are the third edge; their images therefore also form a triangle. Every three-vertex subset of the target supports exactly six such isomorphisms. There are \(6\binom m3\) nonconstant maps.

**Step 5: Injective maps from the four-vertex source.** Let \(f:T_4\to T_m\) be injective. The images of \(12,13,23\) form a triangle on three target vertices \(A,B,C\). Choose labels so that \(f(12)=AB\), \(f(13)=AC\), and \(f(23)=BC\). The edge \(f(14)\) must meet both \(AB\) and \(AC\) but is not among these three images. Therefore \(f(14)=AD\) for a fourth target vertex \(D\). The quandle equations force \(f(24)=BD\) and \(f(34)=CD\). This is exactly the map induced by a unique injection of four source vertices into the target; there are \((m)_4\) such maps.

**Step 6: The exceptional four-vertex quotient.** A nonconstant but noninjective map \(f:T_4\to T_m\) can only identify disjoint source edges (Step 2). The equivalence relation \(f(x)=f(y)\) is stable under every right translation of \(T_4\), and these translations generate all vertex permutations of \(K_4\). Because that group acts transitively on the three *pairs of opposite edges*, collapsing one such pair collapses all three. Hence \(f\) factors through the three-element quotient \(q:T_4\to T_3\) whose classes are \(\{12,34\}\), \(\{13,24\}\), and \(\{14,23\}\). The quotient product sends each ordered pair of distinct classes to the third class, and is therefore \(T_3\). A nonconstant map out of this quotient embeds it into a triangle by Step 4, producing exactly \(6\binom m3\) maps of rank three. These have rank less than six, so do not overlap Step 5.

**Step 7: The four-vertex rank-three semigroup.** For each of the four triangles \(T\subset K_4\), the restriction \(q|_T:T\to T_3\) is an isomorphism; let \(s_T:T_3\to T\) be its inverse. Every rank-three endomorphism has the unique form \(s_T\circ g\circ q\) with \(g\in S_3=\operatorname{Aut}(T_3)\). Because \(q\circ s_U\) is the identity for every triangle \(U\), composition gives
\[
(s_Tgq)\circ(s_Uhq)=s_T(gh)q.
\]
Thus these 24 maps multiply as \(S_3\) times a four-element left-zero semigroup, and the idempotents are exactly the four \(s_Tq\).

Together Steps 1–7 prove all claimed classifications and counts for every stated \(n,m\).

## Verification
The standalone `verify.py` enumerates all homomorphisms directly from multiplication tables: it assigns image edges, repeatedly propagates quandle product equations, rejects conflicts, and counts *every* completed assignment. It independently compares all rank spectra for \(3\le n\le6\), \(2\le m\le7\), plus \((n,m)=(7,7),(7,8)\), with the formula. This is \(26\) complete source-target censuses, with no tolerance parameters or sampling. It also composes all \(576\) ordered pairs of the exceptional 24 rank-three endomorphisms, verifies their image law, and counts the four idempotents. The final test result is `VERIFY_OK`.

These finite checks corroborate the all-parameter proof; they cannot replace it.

## Relationship to prior work
The transposition quandle and its conjugation multiplication appear explicitly in Anderson et al., *Quandle Basics* (2006), §2.4. Bonatto, *Principal and Doubly Homogeneous Quandles* (arXiv:1904.13388; first publicly posted 2019-04-30), studies structural quandle classes, their automorphisms and congruences; it does not state the two-parameter Hom-set formula here. Cvrček–Stanovský, *Primitive quandles with alternating displacement group* (arXiv:2401.15642; first posted 2024-01-28), proves that the transposition conjugation quandles of \(S_n\) are primitive for \(n=3\) and \(n\ge5\). Their primitivity implies the previously known *injective-or-constant* dichotomy for those sources, but not the classification of all embeddings into each target \(T_m\), the cross-size formula, or the four-vertex quotient ideal. Suzuki, *On Embeddings of Homogeneous Quandles* (arXiv:2603.08085), gives general sufficient criteria for certain embeddings into group conjugation quandles, not a classification of transposition-to-transposition Hom sets. The present claim is exactly the full cross-size classification and its exceptional rank-three multiplication structure, not a new claim of source simplicity.

## Limitations
The theorem is confined to source transposition quandles and target transposition quandles. For \(n=2\), \(T_2\) is the singleton quandle and every map is constant, so the substantive statement starts at \(n=3\). The classification treats quandle homomorphisms, not arbitrary group homomorphisms \(S_n\to S_m\). Broad results on conjugacy-class embeddings or semigroup representations may imply parts of the conclusion under another formulation; priority is assessed only against the specified inspected sources and the available claim search, without independent publication-priority certification.

## References
1. M. Bonatto, *Principal and Doubly Homogeneous Quandles*, arXiv:1904.13388 (first posted 2019-04-30), https://arxiv.org/abs/1904.13388.
2. M. Cvrček and D. Stanovský, *Primitive quandles with alternating displacement group*, arXiv:2401.15642 (first posted 2024-01-28), https://arxiv.org/pdf/2401.15642.
3. A. Suzuki, *On Embeddings of Homogeneous Quandles*, arXiv:2603.08085 (2026), https://arxiv.org/pdf/2603.08085.
4. J. Anderson, A. Brownell, H. Potter and D. Yetter, *Quandle Basics*, 2006, §2.4, https://www.math.ksu.edu/research/reu/reu2005-2008/2006/pdfs/quandle06.pdf.
