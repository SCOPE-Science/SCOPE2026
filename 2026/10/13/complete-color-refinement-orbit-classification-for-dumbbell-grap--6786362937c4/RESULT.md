# Complete color-refinement orbit classification for dumbbell graphs
## Finding
For integers \(p,q\ge3\) and \(k\ge0\), let \(D_{p,k,q}\) be the dumbbell graph obtained from two vertex-disjoint cycles \(C_p,C_q\) and a path \(P_{k+2}\) by identifying the two path endpoints with one vertex of each cycle. Write \(r=k+1\) for the connector length in edges between the two degree-three attachment vertices.

Then ordinary color refinement from the uniform coloring recovers the automorphism-orbit partition of \(D_{p,k,q}\) if and only if
\[
\neg(p=q=k+1).
\]
Equivalently, the only non-refinable dumbbell graphs are the balanced family
\[
D_{m,m-1,m}\qquad(m\ge3),
\]
where the two cycle lengths and the connector length are all equal.

If \(p\ne q\), the two degree-three attachment vertices split exactly in round
\[
\min\{p,q\}+1.
\]

In the balanced graph \(D_{m,m-1,m}\), the two attachment vertices form one stable color class. For each \(1\le d\le\lfloor m/2\rfloor\), all degree-two vertices at unordered endpoint-distance pair \(\{d,m-d\}\) on any of the three length-\(m\) threads lie in one stable class. Thus for \(d<m/2\) this class has six vertices, and for even \(m\) at \(d=m/2\) it has three. These classes merge distinct automorphism orbits because connector vertices are cut vertices whereas cycle vertices are not.

## Assumptions and terminology
Graphs are finite, simple, undirected, and initially uncolored. Round \(0\) is the uniform coloring, and every later round recolors a vertex by its previous color together with the multiset of previous colors of its neighbors.

A graph is called refinable when its stable color-refinement partition equals the orbit partition of its automorphism group.

## Proof
Let \(u,v\) be the two degree-three attachment vertices and put \(r=k+1\). In the universal cover, suppressing degree-two vertices leaves a tree of degree-three branch vertices joined by subdivided threads. At a lift of \(u\), the three incident thread lengths are \(p,p,r\); at a lift of \(v\), they are \(q,q,r\).

Krebs and Verbitsky (Lemmas 2.6–2.7) identify color-refinement colors with rooted universal-cover truncation types, and stable color equality with isomorphism of the full rooted universal covers.

Assume first that \(p\ne q\), say \(p<q\). Through round \(p\), the two attachment vertices still have the same color. In round \(p+1\), the two \(p\)-threads at \(u\) reveal degree-three branch vertices one layer earlier than the two \(q\)-threads at \(v\); the connector contributes identically at both roots. Hence \(u\) and \(v\) split exactly in round \(p+1=\min\{p,q\}+1\).

Once the stable colors of \(u\) and \(v\) differ, every degree-two vertex is determined by the colors and distances of the nearest degree-three vertices in its two directions in the universal cover. A left-cycle vertex sees two \(u\)-type branch vertices, at distances \(i\) and \(p-i\). A connector vertex sees one \(u\)-type and one \(v\)-type branch vertex, at distances \(j\) and \(r-j\). A right-cycle vertex sees two \(v\)-type branch vertices, at distances \(h\) and \(q-h\). Hence no stable color can cross between these three regions.

Within the left cycle, equality of stable colors is exactly equality of the unordered pair \(\{i,p-i\}\), which is precisely the reflection orbit about \(u\); likewise on the right cycle. On the connector, the endpoint colors are different, so equality forces the ordered distances to \(u\) and \(v\) to agree, making every internal connector vertex a singleton orbit and stable class. Thus every unequal-cycle dumbbell is refinable.

Now suppose \(p=q=m\). There is an automorphism swapping the two cycles and reversing the connector, so \(u\) and \(v\) remain in one color class. Every degree-two vertex lies on one of three finite threads between branch vertices in the universal cover: two cycle threads of length \(m\) and the connector thread of length \(r\). Since the endpoint branch colors are equal, a position is determined by its unordered endpoint-distance pair.

If \(r\ne m\), a cycle-thread position has endpoint-distance sum \(m\) and a connector position has sum \(r\), so they cannot share a stable color. Equality within a fixed thread length is exactly equality up to reversal, which gives precisely the automorphism orbits. Hence the graph is refinable.

If \(r=m\), all three thread lengths are equal and all branch endpoints have the same stable color. Corresponding positions on all three threads therefore have isomorphic rooted universal covers and remain color-equivalent forever. But connector vertices are cut vertices and cycle vertices are not, so these stable classes contain multiple automorphism orbits. Hence exactly the balanced family is non-refinable.

## Verification
The newly replayed dumbbell_replay.py checks all 13,056 triples with 3<=p,q<=18 and 0<=k<=50, including 12,240 unequal-cycle attachment split times and 16 balanced partitions. Its actual output and replay hash are recorded in VERIFICATION.md. These checks corroborate the uniform proof.

## Relationship to prior work
Wang, Belardo, Huang, and Li Marzi use the dumbbell family in their 2010 spectral-characterization work. Liu and Lu later use the notation \(D_{p,k,q}\) and explicitly define it as two cycles joined through \(P_{k+2}\). These papers study graph spectra rather than color refinement.

Krebs and Verbitsky give the universal-cover characterization of color-refinement rounds used in the proof. Arvind, Köbler, Rattan, and Verbitsky call a graph refinable when its stable color partition equals its automorphism-orbit partition; their inspected text discusses the general hierarchy and the classical tree case but does not state a dumbbell classification.

A prior equal-cycle calculation identifies the resonance \(k+1=m\). The present theorem is strictly broader: it proves that every unequal-cycle dumbbell is refinable, including cases where the connector length equals one of the two cycle lengths, and combines this with the equal-cycle analysis to give the complete if-and-only-if classification for all dumbbell graphs.

Targeted published-finding corpus and web searches using dumbbell/handcuff terminology together with color refinement, \(1\)-WL, Weisfeiler--Leman, equitable partitions, refinability, and automorphism orbits did not locate an equivalent theorem.

## Limitations
The theorem concerns ordinary one-dimensional color refinement from the uniform coloring on the standard dumbbell family. It does not classify amenability, compactness, higher-dimensional Weisfeiler--Leman behavior, arbitrary cactus graphs, or full iteration depth for unequal-cycle dumbbells. The literature search was targeted rather than exhaustive.

## References
1. J. Wang, F. Belardo, Q. Huang, and E. M. Li Marzi, *Spectral Characterizations of Dumbbell Graphs*, Electronic Journal of Combinatorics 17(1), R42, 2010, DOI: 10.37236/314.
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
3. X. Liu and P. Lu, *Laplacian spectral characterization of dumbbell graphs and theta graphs*, arXiv:1407.5255, first posted 20 July 2014.
4. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015.
