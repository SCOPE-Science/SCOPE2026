# Dihedral orientation characters of generic cyclic Vietoris–Rips spheres

## Finding
For integers \(n\ge4\) and \(1\le k<n/2\), let \(C_n^k\) be the graph joining cycle vertices at shortest-path distance at most \(k\). Let \(K_{n,k}=\operatorname{Cl}(C_n^k)\), the inclusive Vietoris–Rips complex of the graph-metric cycle at scale \(k\). Fix \(\ell\ge0\) with
\[
\frac{\ell}{2\ell+1}<\frac{k}{n}<\frac{\ell+1}{2\ell+3}.
\]
The known nonequivariant result gives \(K_{n,k}\simeq S^{2\ell+1}\). This finding identifies its **integral dihedral orientation character**. Under \(r(i)=i+1\) and \(s(i)=-i\), the action on the rank-one group \(\widetilde H_{2\ell+1}(K_{n,k};\mathbb Z)\cong\mathbb Z\) is
\[
r_*^a=+1,\qquad (r^as)_*=(-1)^{\ell+1}\quad\text{for every integer }a.
\]
In particular, for the natural topological quotients, the reduced rational homology of \(K_{n,k}/\langle r\rangle\) is concentrated in degree \(2\ell+1\), with rank one. For \(K_{n,k}/\langle r,s\rangle\), this rank is one if \(\ell\) is odd and zero if \(\ell\) is even; all other reduced rational homology groups vanish.

## Assumptions and scope
The number \(k\) is an integer with \(1\le k<n/2\). All graph distances are along the simple cycle \(C_n\). A simplex is an arbitrary vertex subset of diameter at most \(k\); notably, it need not lie in a single short circular arc. The generic inequalities are strict: the singular boundary values are excluded. Homology characters are integral and quotient calculations rational. The previously established cyclic-homomorphism homotopy-equivalence theorem of Adamaszek and Adams is an essential mathematical input.

## Proof
**1. A canonical sphere for each band.** Fix \(\ell\) and put \(m=2\ell+2\), \(n_0=2m=4\ell+4\), and \(k_0=m-1=2\ell+1\). Direct cross multiplication places \(k_0/n_0\) strictly between \(\ell/(2\ell+1)\) and \((\ell+1)/(2\ell+3)\). The graph \(C_{2m}^{m-1}\) is the complete graph on \(2m\) vertices minus the \(m\) antipodal edges \(\{i,i+m\}\). Consequently its clique complex is a join of \(m\) zero-spheres, the boundary of an \(m\)-dimensional cross-polytope, homeomorphic to \(S^{m-1}=S^{2\ell+1}\).

**2. The canonical reflection degree.** Orient this cross-polytope by its ordered coordinate axes \(i=0,\ldots,m-1\), with the positive vertex on axis \(i\) labeled \(i\) and the negative vertex labeled \(i+m\). Reflection \(s_0(j)=-j\pmod{2m}\) permutes axes by \(i\mapsto-i\pmod m\). This axis permutation has \((m-2)/2=\ell\) transpositions and therefore sign \((-1)^\ell\). The reflection also exchanges positive and negative vertices on every axis except \(i=0\), contributing \((-1)^{m-1}=-1\). Thus its ambient signed-permutation determinant and its degree on the sphere boundary equal \((-1)^{\ell+1}\).

**3. Equivariant comparison inside one open winding band.** For any other \((n,k)\) satisfying the displayed strict inequalities, choose a common multiple \(N\) of \(n\) and \(n_0\), as large as needed, and an integer \(K\) satisfying
\[
\max\left\{\frac{k}{n},\frac{k_0}{n_0}\right\}<\frac KN<\frac{\ell+1}{2\ell+3}.
\]
Inclusion of equally spaced cyclic vertex subsets supplies simplicial maps \(K_{n,k}\to K_{N,K}\) and \(K_{n_0,k_0}\to K_{N,K}\), using the injective vertex maps \(j\mapsto Nj/n\) and \(j\mapsto Nj/n_0\). These are cyclic graph homomorphisms: each original forward edge is mapped to a forward edge. Their source and target winding fractions are precisely \(k/n\), \(k_0/n_0\), and \(K/N\), all in the same open band. Proposition 4.9 of Adamaszek–Adams, *The Vietoris–Rips complexes of a circle*, states that each such cyclic homomorphism induces a homotopy equivalence of clique complexes. Both maps are exactly equivariant for the reflections \(j\mapsto-j\). As their maps on the rank-one integral top homology are isomorphisms, the reflection degree for the arbitrary source equals that of the canonical cross-polytope: \((-1)^{\ell+1}\).

**4. Rotations are homologically trivial.** Choose the common multiple \(N\) still larger, if necessary, so that also \((K+1)/N<(\ell+1)/(2\ell+3)\). For any face \(\sigma\) of \(K_{N,K}\), the union of \(\sigma\) with its one-step translate \(r_N\sigma\) is a face of \(K_{N,K+1}\): by the triangle inequality, every cross-distance is at most \(K+1\). Thus the identity and the one-step rotation maps from \(K_{N,K}\) to \(K_{N,K+1}\) are contiguous and induce equal maps on homology. The inclusion between these two complexes is a homotopy equivalence by the same Proposition 4.9. It follows that \((r_N)_*\) is the identity on \(\widetilde H_{2\ell+1}(K_{N,K};\mathbb Z)\). Under the first inclusion from Step 3, the rotation \(r\) of \(C_n\) becomes \(r_N^{N/n}\). The inclusion induces an isomorphism; therefore \(r_*\) is the identity. Every product \(r^as\) consequently has degree \((-1)^{\ell+1}\).

**5. Quotient homology.** The known homotopy classification says the only nonzero reduced rational homology of the original complex is its one-dimensional group in degree \(2\ell+1\). For a finite simplicial group action, rational homology of the geometric quotient agrees with invariant rational homology: barycentrically subdivide to remove inversions and average the cellular chains over the group. The rotation subgroup always fixes the top line, whereas the entire dihedral group fixes it precisely when \((-1)^{\ell+1}=+1\), or \(\ell\) odd. This proves the quotient dichotomy.

## Verification
The independent finite checker in `verification.py` computes signed fixed-simplex Lefschetz numbers for rotation and both reflection-axis types. Using the known homology concentration, the Hopf trace formula recovers the top-homology degrees. It checks the generic regimes for \(4\le n\le28\) and \(0\le\ell\le3\), the signed cross-polytope orientation for six canonical sphere dimensions, and the contiguity inclusion on small examples. Run `python3 verification.py` with Python 3 and no external packages. The checker is finite corroboration; Steps 1–5 supply the infinite proof, with Proposition 4.9 from the cited primary source.

## Relationship to prior work
Adamaszek (arXiv:1104.0433, Corollary 6.7) established the nonequivariant homotopy types of clique complexes of cycle powers. Adamaszek and Adams (arXiv:1503.03669, Proposition 4.9) established the necessary homotopy equivalences induced by cyclic graph homomorphisms. Adamaszek, Adams, Frick, Peterson and Previte-Johnson (arXiv:1410.4336, Section 7) computed the same-looking sign character **for the different nerve complexes of evenly spaced circular arcs**. Section 8 of that work relates nerves and Vietoris–Rips clique complexes by a non-equivariant homotopy equivalence on differently sized vertex sets; it does not identify the integral dihedral action on the latter complexes. The comparison in Steps 2–4 addresses that missing equivariant implication.

## Limitations
Only the open generic winding bands are treated. At singular ratios the homology may have higher rank and the action is not determined here. The theorem gives a rank-one homology character, not an equivariant homotopy equivalence or integral homology of the quotient. The primary cyclic-map homotopy-equivalence theorem is used as a published input; no new nonequivariant sphere classification is claimed. Closely related symmetry results for circular-arc nerves and other cycle-derived complexes make equivalent treatments a residual bibliographic possibility.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first posted 2011-04-03), especially Corollary 6.7, https://arxiv.org/abs/1104.0433.
2. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first posted 2015-03-12), especially Proposition 4.9 and Section 3, https://arxiv.org/abs/1503.03669.
3. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336 (first posted 2014-10-16), especially Proposition 7.3 and Theorem 8.5, https://arxiv.org/abs/1410.4336.
