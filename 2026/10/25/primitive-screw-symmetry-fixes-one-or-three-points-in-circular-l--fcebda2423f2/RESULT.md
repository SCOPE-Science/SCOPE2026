# Primitive screw symmetry fixes one or three points in circular-ladder perfect-matching complexes

## Finding
Let \(K_n\) denote the perfect-matching simplicial complex of the circular ladder \(C_n\square K_2\), for every integer \(n\ge3\). Let \(r\) rotate both layers one step and \(s\) exchange the layers. For each integer \(k\) coprime to \(n\), the geometric fixed-point spaces are
\[
|K_n|^{r^k}\cong\mathrm{pt},\qquad
|K_n|^{sr^k}\cong
\begin{cases}
\mathrm{pt},&n\text{ odd},\\
\{p_0,p_1,p_2\}\text{ discretely},&n\text{ even}.
\end{cases}
\]
In particular, with the reduced Lefschetz number defined by
\[
\widetilde L(g)=\sum_{j\ge0}(-1)^j\operatorname{tr}
\bigl(g_*\mid\widetilde H_j(K_n;\mathbb Q)\bigr),
\]
we have \(\widetilde L(r^k)=0\) and
\[
\widetilde L(sr^k)=\begin{cases}0,&n\text{ odd},\\2,&n\text{ even}.\end{cases}
\]
This asserts geometric fixed sets, not merely a numerical character identity.

## Assumptions and scope
Take indices modulo \(n\). The vertices of the graph are \(u_i,v_i\). Its edges are top rims \(U_i=\{u_i,u_{i+1}\}\), bottom rims \(V_i=\{v_i,v_{i+1}\}\), and rungs \(R_i=\{u_i,v_i\}\). Vertices of \(K_n\) are graph edges; a simplex is any subset of a perfect matching, and the facets are exactly the perfect matchings. The automorphisms are \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\), \(s(u_i)=v_i\), \(s(v_i)=u_i\). We require \(\gcd(k,n)=1\). The space \(|K_n|\) means the standard geometric realization. A fixed point need not be a fixed vertex of the simplicial complex.

## Proof
The support of a point in a geometric simplicial complex is the unique face consisting of vertices with positive barycentric coefficients. If an automorphism fixes the point, it preserves that support and the coefficients are constant on each orbit contained in the support. Conversely, every invariant simplex yields fixed barycenters on its invariant vertex orbits. Thus it suffices to classify graph-edge orbits that themselves are simplices; combining different orbits is allowed only if their union is a simplex.

For \(r^k\), coprimality makes the three graph-edge orbits precisely the full rung set \(\{R_i\}\), full top rim set \(\{U_i\}\), and full bottom rim set \(\{V_i\}\). The latter two are not matchings (their edges meet), whereas all rungs form a perfect matching. Hence there is one invariant nonempty simplex, the full-rung facet, and one fixed geometric point: its barycenter.

For \(g=sr^k\), rungs again form one orbit and are a perfect matching. On horizontal edges \(g(U_i)=V_{i+k}\) and \(g(V_i)=U_{i+k}\). If \(n\) is odd, successive even powers of \(g\) visit every top-rim index because \(\gcd(2k,n)=1\). All \(2n\) horizontal edges lie in one orbit, which is not a matching. Only the rung facet remains invariant, giving one point.

If \(n\) is even, \(k\) is odd and \(\gcd(2k,n)=2\). The horizontal edges split into two orbits of size \(n\): one consists of top rim edges with even indices and bottom rim edges with odd indices; the other consists of top rim edges with odd indices and bottom rim edges with even indices. Each orbit is a perfect matching, since alternate edges tile each even cycle in its layer. Along with the rung facet these give exactly three invariant simplices of maximal size. No union of two of the three is a matching because each already covers every graph vertex. Therefore each contributes just its barycenter, and these three points are isolated in the fixed locus.

Finally, for a finite simplicial automorphism the ordinary Lefschetz number equals the Euler characteristic of its geometric fixed-point set: apply barycentric subdivision so that invariant simplices contribute according to the ordinary fixed-complex Euler formula. Subtract the invariant trace on the constant \(H_0\)-class (or, equivalently, subtract one from unreduced Lefschetz number). The fixed sets have Euler characteristics one or three, giving the displayed reduced formula. No assumption about concentration of homology in a single degree is needed.

## Verification
The accompanying stand-alone `VERIFY.py` exhaustively enumerates perfect matchings and their downward-closed face sets for \(3\le n\le10\). It tests all primitive rotations \(r^k\) and screws \(sr^k\), independently checks invariant faces against the predicted orbit facets, and directly computes their signed augmented simplicial traces. All 60 primitive actions and 810800 face-action membership tests passed. This finite test is supplementary: the proof above is uniform in \(n\).

## Relationship to prior work
Agarwal and Basak determine nonequivariant homotopy types of circular-ladder perfect-matching complexes, including the parity-dependent contractible and sphere-wedge cases. Those homotopy types by themselves do not determine fixed-point spaces or homological characters of a simultaneous rotation and layer exchange. An available general fixed-point result for *layer exchange without rotation* is different: it does not imply this primitive screw calculation because the horizontal-edge orbit structure changes under the composite. Matching complexes, independence complexes, and cut complexes of related graphs are distinct constructions. This result claims only the primitive screw and primitive rotation fixed sets above, not a full dihedral homology decomposition or a new nonequivariant homotopy classification.

## Limitations
The primitive hypothesis is essential to this proof; nonprimitive shifts may have additional invariant edge orbits. The result determines a reduced *alternating* homological trace, not individual degree-by-degree traces. Full text of the most directly related 2026 preprint could not be inspected here; an equivalent discussion in a later section cannot be excluded. This is not independent scientific validation.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, first publicly available with circular-ladder results 2026-09-14. https://arxiv.org/abs/2608.30601
2. M. Bayer, A. Jelić Milutinović, and L. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics (2023), DOI:10.37236/11525. The object is analogous, but the graph family differs.
