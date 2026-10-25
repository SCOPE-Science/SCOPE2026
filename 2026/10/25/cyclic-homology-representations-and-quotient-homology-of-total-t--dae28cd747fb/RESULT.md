# Cyclic homology representations and quotient homology of total two-cut complexes of cycle powers

## Finding
Let \(p\ge3\) and \(2p+3\le n\le3p\) be integers. Put \(m=n-2p\), and let \(K=\Delta_2^t(C_n^p)\) be the total two-cut complex of the \(p\)-th power of the cycle on vertices \(\mathbb Z/n\mathbb Z\). Let \(C_n=\langle\rho\rangle\) act by rotation \(\rho(v)=v+1\), and let \(\varepsilon_n\) be the one-dimensional rational character \(\varepsilon_n(\rho^a)=(-1)^{n-\gcd(n,a)}\), induced by the sign of the vertex permutation.

The **entire nonzero reduced rational homology representation** is as follows. If \(m\nmid p\), then \(\widetilde H_{n-2\lfloor p/m\rfloor-4}(K;\mathbb Q)\cong\varepsilon_n\). If \(m\mid p\), then
\[
\widetilde H_{n-2p/m-3}(K;\mathbb Q)\cong
\varepsilon_n\otimes\operatorname{Inf}^{C_n}_{C_m}\!\left(\mathbb Q[C_m]/\mathbb Q\mathbf1\right),
\]
where the quotient denotes the augmentation representation (equivalently the kernel of the augmentation homomorphism), and inflation is along the natural rotation quotient \(C_n\twoheadrightarrow C_m\). All other reduced rational homology groups vanish.

Equivalently, for \(a\in\{0,\ldots,n-1\}\), writing \(h=\gcd(n,a)\) with \(\gcd(n,0)=n\), the trace in the unique nonzero degree is
\[
\operatorname{tr}(\rho^a)=
\begin{cases}
(-1)^{n-h},&m\nmid p,\\
(-1)^{n-h}(m-1),&m\mid p\text{ and }m\mid a,\\
-(-1)^{n-h},&m\mid p\text{ and }m\nmid a.
\end{cases}
\]
The rational reduced homology of the orbit space \(K/C_n\) has rank one in that degree precisely if \(m\nmid p\) and \(n\) is odd, or if \(m\mid p\) and \(m\) is even; in every other case its reduced rational homology vanishes. This is a statement about rational homology, not necessarily the homotopy type of the quotient.

## Assumptions and scope
The graph \(C_n^p\) has edges between distinct residues of cyclic distance at most \(p\). A simplex \(S\) belongs to \(K\) if and only if its complement contains a nonedge of \(C_n^p\). The stated range ensures \(m=n-2p\ge3\), \(p<n/2\), and \(m\le p\). All group representations are over \(\mathbb Q\). The non-equivariant homotopy types and homology dimensions used below were already determined in the cited literature; their rediscovery is not claimed.

## Proof
**1. Alexander duality with its orientation twist.** Let \(L=\operatorname{Cl}(C_n^p)\), the clique complex on the same labeled vertex set. From the definition, \(K=L^*\), its combinatorial Alexander dual. Equivariant simplicial Alexander duality identifies, in the corresponding degrees,
\[
\widetilde H_i(K;\mathbb Q)\cong\varepsilon_n\otimes\widetilde H^{n-i-3}(L;\mathbb Q).
\]
The twist is exactly the orientation character on the ambient \((n-1)\)-simplex, namely the sign of the vertex permutation. This follows by tracking the ordered-vertex complement basis of the relative augmented cochain/chain pairing; replacing a simplex by its oriented complement contributes the determinant of the ambient vertex permutation. Rational cohomology has the same character as rational homology.

**2. The unique clique-homology degree.** Write \(r=\lfloor p/m\rfloor\). The cyclic clique-complex theorem of Adamaszek gives \(L\simeq\bigvee^{m-1}S^{2r}\) if \(m\mid p\), and \(L\simeq S^{2r+1}\) otherwise. Thus the unique reduced clique-homology degree is \(j=2r\) in the first case and \(j=2r+1\) in the second. Alexander duality places the corresponding homology of \(K\) in \(n-j-3\), with the ranks stated above.

**3. Fixed-orbit clique classification.** For a rotation \(g=\rho^a\), let \(h=\gcd(n,a)\) and \(t=n/h\), its orbit length. If \(t\) is even, every vertex orbit contains an antipodal pair, which is not an edge of \(C_n^p\) since \(p<n/2\). Hence \(L\) has no nonempty \(g\)-invariant face. If \(t\) is odd, the vertex orbits are labeled by residues modulo \(h\). For two such orbits \(O_u,O_v\), the largest cyclic distance between their vertices is exactly
\[
\frac{t-1}{2}h+\operatorname{dist}_{C_h}(u,v),
\]
with \(u=v\) giving the orbit's internal diameter. Therefore a nonempty invariant clique can occur only if \(P=p-(t-1)h/2\ge0\). If this holds, unions of vertex orbits are precisely the cliques of \(C_h^P\), with the convention \(C_h^0\) has no edges. We have \(h-2P=n-2p=m\), and \(0\le P<h/2\).

**4. Signed Lefschetz calculation.** The reduced alternating trace on the augmented chain complex of \(L\) equals \(-1\) when there is no nonempty fixed face. For odd \(t\) all \(g\)-cycles on fixed faces have odd length and therefore even permutation sign; the reduced Lefschetz trace is the reduced Euler characteristic of \(\operatorname{Cl}(C_h^P)\). Applying the same cyclic clique-complex homotopy theorem to \((h,P)\), its reduced Euler characteristic is \(m-1\) if \(m=h-2P\) divides \(P\), and \(-1\) otherwise. The divisibility is equivalent to \(h/m\) being an odd integer. In that exceptional case \(t\) is automatically odd because \(n/m\) is odd. Consequently for every \(a\),
\[
\widetilde\Lambda(g;L)=
\begin{cases}m-1,&m\mid p\text{ and }m\mid a,\\-1,&\text{otherwise}.
\end{cases}
\]
Here \(\widetilde\Lambda\) includes the empty-face contribution \(-1\); this normalization is essential.

Since reduced homology of \(L\) is concentrated in degree \(j\), \(\widetilde\Lambda(g;L)=(-1)^j\operatorname{tr}(g;\widetilde H_j(L;\mathbb Q))\). In the noncritical case \(j\) is odd, so its homology character is constantly \(1\). In the critical case \(j\) is even, and the character equals \(m-1\) on multiples of \(m\) and \(-1\) on other rotations, exactly the inflated cyclic augmentation character. The orientation twist of Step 1 yields the displayed \(K\)-characters.

**5. Quotient.** For a finite simplicial group action, rational homology of the orbit space is the invariant homology of the complex (after barycentric subdivision, by averaging). In the noncritical case \(\varepsilon_n\) is trivial precisely for odd \(n\). In the critical case \(n/m=2r+1\) is odd and \(\varepsilon_n\) factors through \(C_m\); its tensor product with the augmentation module contains the trivial module once exactly when \(m\) is even, and otherwise never. This proves the quotient statement.

## Verification
The accompanying standalone Python program `verify.py` enumerates all cliques and computes mod-two simplicial homology for 15 distinct \((n,p)\) pairs with \(3\le p\le7\), totaling 20,978 nonempty clique faces. It separately generates and checks the Alexander-dual complexes in three cases (6,181 faces), and verifies 235 independently computed signed rotation Lefschetz numbers against the complete trace formula. The recorded output `verify_output.txt` ends in `VERIFY_OK`. These finite checks do not replace the infinite argument or establish integral quotient homology.

## Relationship to prior work
Chauhan, Shukla and Vinayak introduced the finite-parameter question for total two-cut complexes of cycle powers (2025). **Carnero Bravo (2026) subsequently determined their full nonequivariant homotopy types**, including the relevant range; these results are acknowledged and not claimed as original. Adamaszek's earlier theorem already determines the non-equivariant homotopy types of cyclic clique complexes. Adamaszek and collaborators also determined dihedral homology actions on *circular-arc nerve complexes*, but their Section 8 distinguishes these nerves from cyclic clique complexes, and its nonequivariant mod-reduction equivalence between different numbers of vertices is not compatible with the one-step rotations. The present claim concerns the complete rotational representation of the **Alexander-dual total two-cut complex** and its rational quotient homology, neither of which is stated in those inspected results.

## Limitations
No reflection-action classification, integral lattice identification, integral quotient homology, or arbitrary-parameter extension is asserted. The self-review remains subject to possible unlocated equivalent results and to independent scholarly examination. The trace computation relies on the published clique-complex homotopy classification and the standard equivariant form of combinatorial Alexander duality.

## References
1. P. Chauhan, S. Shukla, K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486 (first public 2025-12-04), https://arxiv.org/abs/2512.04486.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first public 2026-02-24), https://arxiv.org/abs/2602.21427.
3. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011), https://arxiv.org/abs/1104.0433.
4. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336 (2014), especially Sections 7–8, https://arxiv.org/abs/1410.4336.
