# Cyclic homology characters and necklace invariants of cycle–clique independence complexes

## Finding

**Theorem.** Let \(r\ge1\) and \(n\ge2\) be integers, write \(m=3r\), \(q=n-1\), and let \(K=\operatorname{Ind}(C_m\times K_n)\), where \(\times\) is the categorical (tensor/Kronecker) product of *simple* graphs. The cyclic group \(C_m=\langle\rho\rangle\) acts on \(K\) by \(\rho(i,c)=(i+1\bmod m,c)\). The only nonzero reduced rational homology occurs in degree \(2r-1\).

For \(0\le t<m\), define \(d=\gcd(m,t)\), taking \(\gcd(m,0)=m\). The **complete rational cyclic homology character** is
\[
\operatorname{tr}\bigl(\rho^t\mid\widetilde H_{2r-1}(K;\mathbb Q)\bigr)
=\begin{cases}
q(-1)^d+3q^{d/3},&3\mid d,\\
q(-1)^d,&3\nmid d.
\end{cases}
\]

More precisely, let \(H=\langle\rho^3\rangle\cong C_r\), and let \(W_{q,r}\) be the rational permutation representation of \(H\) on words of length \(r\) over an alphabet with \(q\) letters, where \(\rho^3\) cyclically shifts the letters. Let \(\mathbf 1\) be the trivial \(C_m\)-representation; when \(r\) is even, let \(\varepsilon\) be the sign representation \(\rho\mapsto-1\). Then there are (not canonically specified) isomorphisms of rational \(C_m\)-modules:
\[
\begin{cases}
\widetilde H_{2r-1}(K;\mathbb Q)\oplus\mathbf 1^{\oplus q}
\cong\operatorname{Ind}_{H}^{C_m}W_{q,r},&r\text{ odd},\\
\widetilde H_{2r-1}(K;\mathbb Q)
\cong\operatorname{Ind}_{H}^{C_m}W_{q,r}\oplus\varepsilon^{\oplus q},&r\text{ even}.
\end{cases}
\]

Writing \(N_r(q)=\frac1r\sum_{s=0}^{r-1}q^{\gcd(r,s)}\), the usual number of length-\(r\) necklaces over \(q\) symbols, the top rational Betti number of the geometric rotation quotient is
\[
\dim_{\mathbb Q}\widetilde H_{2r-1}(|K|/C_m;\mathbb Q)
=\begin{cases}N_r(q)-q,&r\text{ odd},\\N_r(q),&r\text{ even}.\end{cases}
\]
All other reduced rational homology groups of this quotient vanish.

## Assumptions and scope

The graph \(C_m\) has positions \(\mathbb Z/m\mathbb Z\); \(K_n\) has colors \(\{1,\ldots,n\}\). Distinct \((i,c)\) and \((j,c')\) are adjacent exactly when \(j=i\pm1\pmod m\) and \(c\ne c'\). The independence complex contains all vertex subsets without such edges. The cyclic action changes only the position. The theorem applies to every \(r\ge1\), including \(m=3\), and every \(n\ge2\). All representation statements are over \(\mathbb Q\), not assertions about integral \(\mathbb Z[C_m]\)-lattices.

## Proof

**1. Concentration in one odd degree.** Theorem 22 of Antolín Camarena and Carnero Bravo, including its small cases, proves \(\operatorname{Ind}(C_{3r}\times K_n)\) is a wedge of spheres of dimension \(2r-1\) for all \(r\ge1,n\ge2\). Thus \(\widetilde H_j(K;\mathbb Q)=0\) for \(j\ne2r-1\). No equivariant equivalence is asserted or required.

**2. Signed fixed-face trace.** Fix \(t\), put \(d=\gcd(m,t)\) and \(L=m/d\). Each vertex orbit of \(\rho^t\) has exactly \(L\) elements, all with the same color and the same position residue modulo \(d\). A fixed simplex is a disjoint union of \(a\) such vertex orbits. On its oriented \((La-1)\)-chain, rotation has permutation sign \((-1)^{a(L-1)}\); consequently its alternating trace contribution is \((-1)^{La-1+a(L-1)}=(-1)^{a-1}\). Including the empty face of the augmented chain in degree \(-1\) contributes \(-1\). Therefore the reduced Lefschetz number is the negative of the signed sum of admissible selections of vertex orbits, assigning weight \((-1)^a\) to a selection containing \(a\) orbits.

**3. Quotient-row combinatorics, including short quotients.** Encode the chosen color-orbits in each of the \(d\) position residues by subsets \(A_0,\ldots,A_{d-1}\subseteq\{1,\ldots,n\}\). The independence condition for consecutive residues (read cyclically) is: either subset is empty, or both are the *same singleton*. This criterion holds even for \(d=1\) and \(d=2\): when \(d=1\) it demands \(A_0\) be empty or a singleton; when \(d=2\) it imposes the same compatibility in both directions. These are formal quotient-row constraints; no ordinary simple quotient graph is presumed. Every admissible selection has signed weight \(\prod_i(-1)^{|A_i|}\).

**4. Transfer matrix.** Give an empty row weight \(1\), each specified singleton row weight \(-1\), and replace all rows with at least two colors by a single state \(M\) of total weight
\[
\sum_{a=2}^{n}\binom na(-1)^a=n-1=q.
\]
Such a multicolor row is adjacent only to an empty row, so summing it into \(M\) preserves every cyclic weighted sum. On the states \(0,1,\ldots,n,M\), define \(T_{uv}=w(v)\) for compatible successive states and zero otherwise. The signed sum in step 2 is exactly \(\operatorname{tr}(T^d)\). The subspace of color coordinates summing to zero has dimension \(n-1=q\) and \(T\) acts on it as \(-I\). On the complementary subspace of vectors constant across colors, \(T\) acts, in the coordinates (empty, constant-singleton, multicolor), by
\[
B=\begin{pmatrix}1&-n&q\\1&-1&0\\1&0&0\end{pmatrix},\qquad B^3=qI_3.
\]
Since \(q\ge1\), the three complex eigenvalues of \(B\) are the distinct cube roots of \(q\). Hence their \(d\)-th powers sum to \(0\) when \(3\nmid d\), and to \(3q^{d/3}\) when \(3\mid d\). It follows that
\[
\operatorname{tr}(T^d)=q(-1)^d+3\mathbf1_{3\mid d}q^{d/3},
\]
where the latter term is understood as zero for \(3\nmid d\). By step 2 the reduced Lefschetz number is its negative. By step 1, that reduced Lefschetz number is also \(-\operatorname{tr}(\rho^t\mid\widetilde H_{2r-1})\), proving the stated character.

**5. Representation and quotient.** A permutation of \(r\) places by a shift of \(s\) fixes \(q^{\gcd(r,s)}\) words. Therefore the induced word module has character \(3q^{\gcd(r,s)}\) on \(\rho^{3s}\in H\) and zero outside \(H\). If \(r\) is odd, then \(m\) and every \(d\) are odd, so the remaining character term is \(-q\) times the trivial character. If \(r\) is even, then \((-1)^d=(-1)^t\), and the remaining term is \(q\) times the sign character. Equality of characters of finite-dimensional representations of a finite group over characteristic zero gives the displayed rational module isomorphisms. By Frobenius reciprocity, the trivial multiplicity of the induced word module is the dimension of its \(H\)-invariants, namely \(N_r(q)\) by Burnside's lemma. The extra trivial/sign contributions yield the formula. Finally, for an action of a finite group on a finite simplicial complex, rational homology of the geometric quotient equals the invariant rational homology, for example by the equivariant-to-quotient transfer after barycentric subdivision; the quotient formula follows.

## Verification

Run `python3 verify.py` (Python standard library only). Its direct oriented-face enumerator computes reduced Lefschetz traces without the quotient-orbit or transfer formula for the cases \((m,n)=(3,2),(3,3),(3,4),(6,2),(6,3),(9,2)\) and all their rotations. Independent cyclic row-subset enumeration and integer transfer matrices check \(1\le d\le9\) and \(2\le n\le5\), and exact formula evaluations are compared throughout. Fourier calculations test nonnegative integer multiplicities and the necklace invariant formula for \(1\le r\le7\), \(2\le n\le7\). The uniform theorem is established by the proof, not by these finite tests. The script prints `ALL_TESTS_PASSED` on success.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (first publicly available July 23, 2023, arXiv:2307.12401, Theorem 22) determine the **nonequivariant** wedge-of-spheres homotopy type of precisely this family. Their result is used in proof step 1, not claimed as new. Goyal, Shukla and Singh (arXiv:1905.06926, Proposition 3.2) determine the nonequivariant homotopy type of categorical products of two complete graphs; this includes the base \(r=1\) graph but gives no rotation action. The present theorem supplies the complete rational cyclic character, an explicit induced-word-module description, and rational homology of the rotation quotient; none is implied by an ordinary wedge decomposition without compatible equivariant data. Related computations for other graph complexes and cycle products do not assert the displayed cyclic character for this family.

## Limitations

The representation is classified rationally, not as an integral equivariant lattice; no natural choice of module splitting is asserted. The theorem treats the position-rotation subgroup, not the full dihedral or color-permutation group. It depends on the cited already-published nonequivariant homotopy theorem for the assertion that homology is concentrated in one degree. The novelty assessment is necessarily limited to the inspected and searchable literature and is not a claim of absolute priority. No computational experiment alone proves the all-parameter theorem.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public version July 23, 2023), Theorem 22 and Section 3. https://arxiv.org/abs/2307.12401
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (May 16, 2019), Proposition 3.2. https://arxiv.org/abs/1905.06926
