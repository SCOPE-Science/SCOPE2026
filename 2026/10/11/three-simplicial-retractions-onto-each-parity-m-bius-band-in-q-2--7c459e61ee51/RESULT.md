# Three simplicial retractions onto each parity Möbius band in \(Q_{2m+1,2}\)

## Finding
For every integer \(m\ge 2\), let \(p=2m+1\) and write the Datta--Upadhyay weakly regular Klein-bottle triangulation \(Q_{2m+1,2}\) on \(\mathbb Z/(2p)\) with facets \(\{i,i+1,i+2\}\) and \(\{i,i+2,i+p+1\}\). The induced subcomplex on the even vertices and the induced subcomplex on the odd vertices are both triangulated Möbius bands. For either parity subcomplex \(M\), there are exactly three simplicial retractions \(Q_{2m+1,2}\to M\): they fix \(M\) pointwise and send every vertex of the opposite parity by \(v\mapsto v-1\), \(v\mapsto v+1\), or \(v\mapsto v+p\), respectively, modulo \(2p\). Consequently each inclusion \(M\hookrightarrow Q_{2m+1,2}\) is split injective on integral first homology.

## Assumptions and scope
Fix an integer \(m\ge 2\), put \(p=2m+1\), and index the vertices by \(\mathbb Z/(2p)\). The triangulation used here is the family denoted \(Q_{2m+1,2}\) by Datta and Upadhyay. In this indexing its facets are
\[
A_i=\{i,i+1,i+2\},\qquad B_i=\{i,i+2,i+p+1\},
\]
for all \(i\in\mathbb Z/(2p)\). Let \(M_0\) and \(M_1\) be the induced subcomplexes on the even and odd vertices, respectively. All congruences below are modulo \(2p\), except after rescaling a parity class where they are modulo \(p\).

## Proof
Consider \(M_0\); the odd case follows by translating every vertex by one. Only the facets \(B_i\) with even \(i\) lie entirely in \(M_0\). After writing \(i=2a\) and dividing all even labels by two, these facets become
\[
T_a=\{a,a+1,a+m+1\},\qquad a\in\mathbb Z/p.
\]
Thus \(M_0\) has \(p\) vertices, \(2p\) edges, and \(p\) triangles. Its boundary edges are exactly \(\{a,a+1\}\), so the boundary is one \(p\)-cycle. The link of vertex \(0\) is the path
\[
1-(m+1)-m-2m,
\]
and cyclic symmetry gives the same local type at every vertex. Hence \(M_0\) is a connected compact surface with one boundary component and Euler characteristic \(p-2p+p=0\). By the classification of compact surfaces it is a Möbius band.

Now let \(r:Q_{2m+1,2}\to M_0\) be any simplicial retraction. Write the odd vertex \(2k+1\) as \(o_k\), and write \(r(o_k)=2x_k\) with \(x_k\in\mathbb Z/p\). Since \(A_{2k}=\{2k,o_k,2k+2\}\) contains the boundary edge \(\{2k,2k+2\}\) of \(M_0\), and that edge lies in the unique triangle \(T_k\), simpliciality forces
\[
x_k\in\{k,k+1,k+m+1\}.
\]
Encode these three possibilities by states \(0,1,2\), respectively. The next triangle \(A_{2k+1}\) forces the pair of consecutive states to belong to
\[
\{(0,0),(1,0),(1,1),(1,2),(2,0),(2,2)\}.
\]
Indeed, after translating \(k\) to zero this is obtained by testing the three candidates \(0,1,m+1\) for \(x_0\) and \(1,2,m+2\) for \(x_1\) against the three triangles of \(M_0\) that contain vertex \(1\).

Because the state sequence is cyclic, if state \(0\) occurs then every following state is \(0\), hence all states are \(0\). If no \(0\) occurs but state \(2\) occurs, then every following nonzero state is \(2\), hence all states are \(2\). Otherwise every state is \(1\). Therefore any retraction is one of exactly three maps. In the original vertex labels they are
\[
r_-(v)=v-1,\qquad r_+(v)=v+1,\qquad r_p(v)=v+p
\]
on odd vertices, while fixing even vertices.

These three maps are simplicial for every \(m\ge2\). For \(r_-\) and \(r_+\), each triangle \(A_i\) maps to an edge, while an odd-indexed \(B_i\) maps to \(B_{i-1}\) or \(B_{i+1}\), respectively; even-indexed \(B_i\) is fixed. For \(r_p\), the images of the \(A_i\) and odd-indexed \(B_i\) are again target triangles by direct substitution, while even-indexed \(B_i\) is fixed. Thus all three candidates really are retractions. Translation by one proves the identical statement for \(M_1\).

Finally, if \(j:M_e\hookrightarrow Q_{2m+1,2}\) is either inclusion and \(r\) is any of the three retractions, then \(r\circ j=\operatorname{id}_{M_e}\). Hence \(r_*\circ j_*=\operatorname{id}\) on integral homology, so \(j_*:H_1(M_e;\mathbb Z)\to H_1(Q_{2m+1,2};\mathbb Z)\) is split injective.

## Verification
The accompanying `verify.py` reconstructs the facet formula, checks the parity-induced surface data and all three explicit maps for several family members, exhaustively enumerates all simplicial retractions onto both parity subcomplexes for \(p=5,7,9,11\), and independently checks the six-state transition table used in the symbolic argument for additional odd values of \(p\). These finite checks are stress tests of the formulas; the proof above establishes the universal quantifier.

A clean replay prints:

`VERIFY_OK parity_bands=Mobius retractions_per_band=3 brute_p=5,7,9,11 symbolic_p_through=19`

## Relationship to prior work
Datta and Upadhyay introduce the family \(Q_{2m+1,2}\) and prove that it triangulates the Klein bottle with a vertex-transitive cyclic action. The inspected source gives the facet formula used above, but does not state that either parity class induces a Möbius band, nor does it classify simplicial retractions onto those induced subcomplexes. Searches for equivalent formulations involving parity subcomplexes, Möbius bands, and simplicial retractions did not locate a statement implying the exact three-retraction theorem. A general topological decomposition of a Klein bottle into Möbius bands would not imply that these particular induced subcomplexes are Möbius bands or that there are exactly three simplicial retractions.

## Limitations
The theorem concerns the specific Datta--Upadhyay family \(Q_{2m+1,2}\), not arbitrary Klein-bottle triangulations. It classifies retractions onto the two parity-induced subcomplexes only; it does not classify all simplicial self-maps, all Möbius-band subcomplexes, or all homotopy classes of self-maps. The originality comparison cannot exclude an unindexed older observation about the same family.

## References
B. Datta and A. K. Upadhyay, “Degree-regular triangulations of torus and Klein bottle,” arXiv:math/0403433, first public version 2004-03-25. The source lists MSC 57Q15 first and gives the family \(Q_{2m+1,2}\) in Example 6.
