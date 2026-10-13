# Exact local-Clifford graph-basis symmetry groups of all hypercubes

## Finding

For each integer \(d\geq1\), let \(Q_d\) be the graph on \(V=\mathbb F_2^d\) with edges joining strings at Hamming distance one. Write \(N=2^d\), let \(A\in\mathbb F_2^{N\times N}\) be its adjacency matrix, and let \(|Q_d\rangle\) be the associated \(N\)-qubit graph state. Its *graph basis* is \(\mathcal B_d=\{Z^u|Q_d\rangle:u\in\mathbb F_2^N\}\). All arithmetic with vertex-label vectors below is over \(\mathbb F_2\).

Let \(\mathcal C_d\) consist of all tensor products of single-qubit Clifford unitaries that permute \(\mathcal B_d\) as a set of rays, with no vertex permutations or entangling gates. Identify two such operations when they have the same local binary symplectic action, equivalently, when they differ by a tensor-product Pauli operator up to overall phase. **Then**
\[
\boxed{\mathcal C_d/\mathcal P_N\cong
\begin{cases}
\mathrm{GL}(2,\mathbb F_2)\cong S_3,&d\ \text{odd},\\
\mathbb Z_2\times\mathbb Z_2,&d\ \text{even},
\end{cases}\qquad
|\mathcal C_d/\mathcal P_N|=\begin{cases}6,&d\ \text{odd},\\4,&d\ \text{even}.\end{cases}}
\]
Here \(\mathcal P_N\) is the full tensor-product Pauli group, considered modulo global phase. Thus **every** graph-basis-preserving local Clifford has one of exactly six or four Pauli-inequivalent symplectic patterns, respectively. The induced permutation group of graph-basis **labels**, allowing local Pauli translations, has order \(6\,2^N\) for odd \(d\) and \(4\,2^N\) for even \(d\). These counts are exact for every dimension, not asymptotic.

More explicitly, partition vertices into even and odd Hamming-weight sets \(E,O\). For any valid local Clifford, write its one-site action on Pauli exponents \((x_v,z_v)\) as
\[
(x_v,z_v)\longmapsto(a_vx_v+b_vz_v,\,c_vx_v+e_vz_v).
\]
Every valid pattern is constant separately on \(E\) and \(O\) in the following precise form, with \(\delta=d\bmod2\):
\[
M_E=\begin{pmatrix}r&s\\ \delta t&w\end{pmatrix},\qquad
M_O=\begin{pmatrix}w&t\\ \delta s&r\end{pmatrix},\qquad
rw+\delta st=1\quad\text{in }\mathbb F_2.
\]
Conversely, **every** quadruple \((r,w,s,t)\in\mathbb F_2^4\) satisfying this scalar equation gives a valid graph-basis-preserving tensor product of single-qubit Cliffords. For even \(d\), necessarily \(r=w=1\), while \(s,t\) are independently free. For odd \(d\), \(M_O=M_E^{-\mathsf T}\), and \(M_E\) runs through all six elements of \(\mathrm{GL}(2,\mathbb F_2)\).

## Assumptions and scope

The qubits are distinguishable by their fixed vertices of \(Q_d\), with \(d\geq1\). Single-qubit Clifford means conjugation sends each Pauli operator to a Pauli up to phase. Global phases and local Pauli corrections do not change the counted symplectic coset. A graph-basis permutation means a permutation of the \(2^N\) rays \(Z^u|Q_d\rangle\), not merely a mapping of a single graph state to some other graph state. The result does not count vertex permutations, general nonlocal Clifford operations, or general local unitaries. The parity-indexed matrices are finite-field matrices; no complex-valued matrix equality is asserted modulo phases.

## Proof

**1. Reduction to a necessary-and-sufficient binary equation.** Graph-state Pauli stabilizers have binary labels \((x,Ax)\) for \(x\in\mathbb F_2^N\). A tensor-product Clifford with local matrices \(\begin{psmallmatrix}a_v&b_v\\c_v&e_v\end{psmallmatrix}\) maps the stabilizer *vector space* into itself exactly when
\[
C+EA+AD+ABA=0,\qquad a_ve_v+b_vc_v=1\ \text{for all }v.
\]
Here \(A\) is the hypercube adjacency matrix, and capitals \(B,C,D,E\) in the matrix equation refer respectively to diagonal matrices of \((b_v),(c_v),(a_v),(e_v)\): to avoid overloading, the displayed equation means explicitly
\[
\operatorname{diag}(c)+\operatorname{diag}(e)A
+A\operatorname{diag}(a)+A\operatorname{diag}(b)A=0.
\]
The first equation follows by requiring the transformed vector \((\operatorname{diag}(a)x+\operatorname{diag}(b)Ax,\,\operatorname{diag}(c)x+\operatorname{diag}(e)Ax)\) to lie in \(\{(y,Ay)\}\) for every \(x\). The second is precisely the one-qubit symplectic determinant condition. The transformed space has the same dimension, so containment is equality. Equality of the unsigned stabilizer space is equivalent to preservation of the joint eigenspace basis, up to Pauli phases. Thus these equations are both necessary and sufficient for the stated graph-basis symmetry.

**2. Restriction from hypercube adjacency.** In a hypercube, two distinct vertices have exactly two common neighbors when their Hamming distance is two, and no common neighbors otherwise. Adjacent vertices have no common neighbor. The diagonal entries of the first matrix equation give
\[
c_v=\sum_{w\sim v}b_w.
\]
For adjacent \(v,w\), its off-diagonal entry gives \(e_v=a_w\). Connected bipartiteness therefore forces \(a_v=r\) on even vertices, \(a_v=w\) on odd vertices, and \(e_v=w\) on even vertices, \(e_v=r\) on odd vertices. For vertices \(v,w\) at distance two, the off-diagonal equation says that the two common neighbors have equal \(b\)-values. Any two same-parity vertices at distance two arise in this way, and the graph of distance-two moves is connected on each parity class. Consequently \(b_v=s\) on \(E\) and \(b_v=t\) on \(O\). (For \(d=1\), each parity class has one vertex, making that statement immediate.) As each vertex has degree \(d\), the diagonal relation yields \(c_v=\delta t\) on \(E\) and \(c_v=\delta s\) on \(O\). All other entries of the binary equation vanish because hypercube codegrees are even. This proves that the displayed four-parameter form is both necessary and sufficient for the linear stabilizer equation.

**3. Exact finite-field group.** At every vertex the symplectic determinant equals \(rw+\delta st\), giving the single scalar restriction. If \(d\) is even, \(r=w=1\); the two free bits \((s,t)\) compose by addition, because the respective local matrices are commuting \(X\)-axis quarter-turn symplectic shears. Hence the quotient is the Klein four group. If \(d\) is odd, choosing \(M_E\) arbitrarily in \(\mathrm{GL}(2,\mathbb F_2)\) forces \(M_O=M_E^{-\mathsf T}\). Since inverse transpose respects multiplication order in this combination, this is a six-element subgroup isomorphic to \(\mathrm{GL}(2,\mathbb F_2)\cong S_3\). Every binary one-qubit symplectic matrix lifts to an actual one-qubit Clifford, so no formal pattern is spurious.

**4. Exact action on graph-basis labels.** For a graph-basis input label \(u\), conjugation of its \(Z^u\) by a valid Clifford, followed by reduction modulo the graph stabilizer space, gives the affine transformation
\[
u\longmapsto\bigl(\operatorname{diag}(e)+A\operatorname{diag}(b)\bigr)u+\eta,
\]
where \(\eta\in\mathbb F_2^N\) depends on Clifford phases. Multiplying by arbitrary \(Z^\eta\) makes all translations possible. Write \(A=\begin{psmallmatrix}0&R\\ R^{\mathsf T}&0\end{psmallmatrix}\) in the \(E,O\) ordering. A hypercube has \(A^2=\delta I\) over \(\mathbb F_2\), because each vertex has \(d\) two-step returns and each pair of vertices at distance two has two two-step paths. For odd \(d\), \(RR^{\mathsf T}=I\). Identifying a label \(u\) with the pair \((u_E,Ru_O)\), its linear transformation becomes
\[
\begin{pmatrix}u_E\\Ru_O\end{pmatrix}\longmapsto
\begin{pmatrix}w&t\\s&r\end{pmatrix}
\begin{pmatrix}u_E\\Ru_O\end{pmatrix},
\]
with the displayed \(2\times2\) matrix acting on every one of the \(2^{d-1}\) paired coordinates. All six invertible binary matrices occur. For even \(d\), the linear maps are
\[
(u_E,u_O)\longmapsto(u_E+tRu_O,\,u_O+sR^{\mathsf T}u_E),
\]
with \(RR^{\mathsf T}=R^{\mathsf T}R=0\); these four linear maps are distinct and form a Klein four group. In either parity, translations intersect these linear subgroups only at the identity, so the graph-label permutation group has the claimed semidirect-product structure and size.

## Verification

The standalone program `verify_hypercube.py` independently builds the exact full binary linear system for each \(Q_d\) with \(1\leq d\leq5\), performs binary Gaussian elimination on its \(4N\) unknowns, enumerates its entire four-dimensional solution space, imposes all one-qubit determinant conditions, checks every graph-stabilizer generator and the invertibility of every induced label transformation, and finds exactly six, four, six, four, six allowed patterns. The independent program `verify_hypercube_statevectors.py` constructs actual complex Clifford matrices from \(H\) and \(S\), applies each candidate tensor-product gate to **every** graph-basis state for \(d=1,2,3\), and checks that the output has unit overlap with exactly one graph-basis ray. It tests 1,624 individual basis permutations. These finite computations test the implementation; the all-dimensional result follows from the analytic argument in the Proof section.

Run both scripts with Python 3 using only its standard library. The first prints `VERIFY_OK`; the second prints `STATEVECTOR_VERIFY_OK 1624 individual basis permutations`.

## Relationship to prior work

Wang, Avis, Goodenough, and Krastanov (arXiv:2606.23809v1) construct a restricted two-copy family of graph-preserving Clifford gates, discuss special symmetries of the eight-vertex cube, and explicitly identify classification of exceptional graph-preserving symmetries as a future direction. Their group is not a classification of all **one-copy** local-Clifford automorphisms of the graph basis of \(Q_d\). The earlier general binary-symplectic equivalence system in Claudet's thesis (arXiv:2511.22271, Section 2.5) is the foundational criterion used in Proof step 1; it does not evaluate this system to a parity-dependent six-or-four-element group for the full hypercube family. Galgano and Holweck (DOI:10.1007/s10231-023-01361-8) give the general local symplectic action and orbit theory; their framework is consistent with the calculation here, but their graph-state orbit classification does not state the present exact hypercube stabilizer subgroup and its label action. Nation et al. (arXiv:2605.30428v1) algorithmically identify Clifford symmetries of Pauli Hamiltonians and open quantum models, rather than the particular graph-basis stabilizer classification proved here. The novelty claim is the **evaluated all-hypercube classification**, not the general symplectic criterion or the existence of special cube symmetries.

## Limitations

The theorem classifies graph-basis-preserving Clifford products only and does not address non-Clifford local unitaries, qubit permutations, multi-qubit gates, or physical gate-noise performance. The result is a specialized exact evaluation of a general known stabilizer-equivalence criterion; a previously unindexed evaluation or code-theoretic reformulation could contain equivalent coverage. No physical implementation advantage is proved. Finite checks through \(d=5\) and statevector tests through \(d=3\) are illustrative, not an exhaustive verification for arbitrary dimension.

## References

1. M. Wang, G. Avis, K. Goodenough, and S. Krastanov, *Efficient Graph State Purification with Factorized Graph-Preserving Operations across Local Clifford Orbits*, arXiv:2606.23809v1 (first posted 2026-06-22), https://arxiv.org/pdf/2606.23809.
2. N. Claudet, *Local Equivalences of Graph States*, PhD thesis, arXiv:2511.22271 (2025), Section 2.5, https://arxiv.org/pdf/2511.22271.
3. V. Galgano and F. Holweck, *Graph states and the variety of principal minors*, Annali di Matematica Pura ed Applicata, DOI:10.1007/s10231-023-01361-8 (first online 2023), https://doi.org/10.1007/s10231-023-01361-8.
4. C. Nation et al., *Graph automorphisms to obtain Clifford symmetries in open and closed qudit models*, arXiv:2605.30428v1 (2026), https://arxiv.org/pdf/2605.30428.
