# The Desargues independence complex is a mixed-dimensional wedge of spheres
## Finding
Let \(D\) be the Desargues graph, also called the generalized Petersen graph \(GP(10,3)\). Its ordinary independence complex \(\operatorname{Ind}(D)\) consists of all subsets of graph vertices containing no adjacent pair. Then
\[
\operatorname{Ind}(D)\simeq S^4\vee\bigvee^{5}S^5.
\]
In particular, its reduced integral homology is torsion-free, with one generator in degree four and five in degree five, and vanishes in all other degrees. This is a homotopy equivalence, not only a homology statement.

## Assumptions and scope
All graphs are finite, undirected, and simple. Construct the Petersen graph \(P\) on vertices \(0,\ldots,9\): for each \(i\in\mathbb Z/5\mathbb Z\), include the edges \(\{i,i+1\}\), \(\{5+i,5+((i+2)\bmod 5)\}\), and \(\{i,5+i\}\), with all displayed cycle indices reduced modulo five. Construct its canonical bipartite double cover \(D=P\times K_2\) on labels \(0,\ldots,19\): each edge \(\{a,b\}\) of \(P\) becomes the two edges \(\{a,b+10\}\) and \(\{a+10,b\}\). Thus \(D\) has twenty vertices and thirty edges.

For clarity, the bundled verifier also checks an explicit permutation identifying this cover with the standard \(GP(10,3)\) presentation having outer edges \(u_i u_{i+1}\), spokes \(u_iv_i\), and inner edges \(v_iv_{i+3}\), indices modulo ten. The theorem concerns this one graph and the ordinary **vertex** independence complex. It does not concern the matching complex, whose vertices are graph edges.

## Proof
**(1) Exhaustive description of the finite complex.** Encode a vertex set as a 20-bit nonnegative integer. Let \(N(v)\) be the bit mask of the three neighbors of vertex \(v\). Start with the empty face. For \(v=0,1,\ldots,19\), add \(s\cup\{v\}\) for every currently enumerated face \(s\) satisfying \(s\cap N(v)=\varnothing\). By induction on \(v\), every independent set is enumerated exactly once. The total is 6,212 faces including the empty face. Their cardinality distribution, from zero through ten, is
\[
(1,20,160,660,1510,1924,1320,480,115,20,2).
\]
The alternating sum of these counts in reduced-Euler-characteristic convention is \(-4=1-5\).

**(2) Complete matching.** Initially mark every face available, including the empty face. Process pivot vertices \(v=0,1,\ldots,19\) in order. At pivot \(v\), visit in increasing bit-mask order all currently available faces \(a\) not containing \(v\); if \(b=a\cup\{v\}\) is available, record the matched cover relation \(a\prec b\) and remove both faces from the available set. The resulting 3,103 pairs are disjoint, and exactly six faces are unmatched: one 4-dimensional face, whose bit mask is `0x7c00`, and five 5-dimensional faces, with masks
`0x2ec00`, `0x71c00`, `0x99c00`, `0xccc00`, `0xe2c00`.
There is exactly one matching pair containing the empty face. Removing that pair while restricting to nonempty faces leaves exactly one critical vertex, one critical 4-face, and five critical 5-faces.

Orient every unmatched covering edge of the augmented face-poset Hasse diagram downward, and reverse the covering edges belonging to these 3,103 matching pairs. The Hasse diagram contains precisely 30,380 oriented incidences on 6,212 faces. An exhaustive topological sort processes all 6,212 vertices, proving the directed graph is acyclic. Removing the empty face and its pair cannot create a directed cycle, so the ordinary matching is also acyclic. The fundamental theorem of acyclic discrete Morse matchings therefore reduces the complex to a CW model with exactly one 0-cell, one 4-cell, and five 5-cells.

**(3) Integral attachments.** Orient each simplex using the increasing order of its vertex labels, with signed simplicial boundary
\[
\partial[v_0,\ldots,v_k]=\sum_{j=0}^{k}(-1)^j[v_0,\ldots,\widehat{v_j},\ldots,v_k].
\]
For a four-dimensional face \(t\), let \(p(t)\) be its integral coefficient at the single critical 4-face after Morse cancellation. Put \(p(t)=1\) for that critical face, and \(p(t)=0\) if \(t\) is not a lower face of a 4/5 matched pair. If \(t\prec u\) is such a pair, then \([u:t]=\pm1\) and elementary cancellation of this unit incidence gives
\[
p(t)=-[u:t]^{-1}\sum_{\substack{w\prec u\\w\ne t}}[u:w]p(w),
\]
where \([u:w]\in\{\pm1\}\) is the signed simplicial incidence. The acyclic matching ensures this recursive expansion terminates. For every one of the five critical 5-faces \(z\), the exact computation of \(\sum_{t\prec z}[z:t]p(t)\) gives zero. Consequently the entire integral Morse boundary map \(\partial^{\mathrm{Morse}}_5\colon\mathbb Z^5\to\mathbb Z\) is the zero row matrix.

The CW complex's 4-skeleton is \(S^4\). Each 5-cell attaches by a map \(S^4\to S^4\), classified up to homotopy by its degree in \(\pi_4(S^4)\cong\mathbb Z\). These degrees equal the entries of the just-computed Morse boundary and are all zero, so every attaching map is null-homotopic. All five 5-cells split off as 5-spheres, giving the claimed wedge decomposition. No cells of dimension above five remain in the Morse model.

## Verification
The bundled standalone script `verify.py` uses only Python's standard library. Execute `python3 verify.py`. It constructs both graph descriptions and checks a concrete isomorphism, enumerates every independent face, verifies all 3,103 matching pairs and six critical faces, builds and topologically sorts the complete 30,380-incidence directed Hasse diagram, and computes each of the five signed integral Morse coefficients. It separately performs binary Gaussian elimination on all original, unreduced simplicial boundary matrices, confirming reduced mod-two Betti ranks one in degree four and five in degree five, zero elsewhere. A successful execution prints `VERIFY_OK`.

The full enumeration and integer cancellation are finite exhaustive mathematical certificates; the mod-two homology computation corroborates but does not by itself establish a wedge decomposition. The proof's homotopy conclusion depends on the acyclic matching and exact integral attaching degrees, not on extrapolating from sampled cases.

## Relationship to prior work
Carnero Bravo's 2026 theorem for generalized Mycielskians of a graph expresses their independence-complex homotopy types in terms of the original graph's independence complex and that of its Kronecker double cover. The worked instances in that paper concern paths, cycles, complete graphs, and specified categorical products; it does not evaluate the double cover of the Petersen graph. The present result supplies that precise missing input, without claiming a new result about the Mycielskian itself.

Krnc and Pisanski characterize generalized Petersen graphs that are Kronecker covers and explicitly identify the Desargues graph as the double cover of the Petersen graph; they do not determine its independence-complex topology. Nilakantan and Shukla classify independence complexes of the cyclic-consecutive-neighborhood family \(G_m^d\); their 3-regular graph with ten vertices per bipartition has four-cycles, whereas the Desargues graph has girth six, so the classification does not imply the present claim. Kumar, Singh, and Verma study the bipartite Kneser graph \(H(5,2)\), an equivalent presentation of the Desargues graph, but their exact results address the *linear strand* of edge-ideal Betti numbers and bounds on regularity/projective dimension, not the full homotopy type of the independence complex. Their reported projective dimension 15 is consistent with the rank-one fourth homology here via Hochster's formula, but does not imply this wedge decomposition. Berghoff's independence-complex calculation for the Petersen graph itself does not classify its double cover.

Indexed mathematical findings on the *matching complex* of the Desargues graph and the *independence complex* of the dodecahedral graph \(GP(10,2)\) use different simplicial complexes or different graphs, and their conclusions do not imply the present result. The comparison is mathematical rather than merely terminological: matching-complex vertices are edges, and the dodecahedron is not \(GP(10,3)\).

## Limitations
This is a finite graph-specific classification. It proves no formula for general \(GP(n,k)\), higher independence complexes, equivariant actions, or all bipartite Kneser graphs. The acyclicity and integer Morse boundary rely on exhaustive reproducible enumeration rather than a short hand classification of all gradient paths. Literature comparisons identify no decisive covering published statement among the checked sources but cannot rule out differently indexed, unpublished, or otherwise inaccessible equivalent work.

## References
1. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1, publicly posted 2026-01-19. https://arxiv.org/abs/2601.13432
2. M. Krnc and T. Pisanski, *Characterization of generalized Petersen graphs that are Kronecker covers*, arXiv:1802.07134, 2018; published in Discrete Mathematics & Theoretical Computer Science 21(4), 2019. https://arxiv.org/abs/1802.07134
3. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789, 2017. https://arxiv.org/abs/1709.04789
4. A. Kumar, P. Singh, and R. Verma, *Certain homological invariants of bipartite Kneser graphs*, arXiv:2105.06144, 2021. https://arxiv.org/abs/2105.06144
5. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, 2020. https://arxiv.org/abs/2008.06267
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
