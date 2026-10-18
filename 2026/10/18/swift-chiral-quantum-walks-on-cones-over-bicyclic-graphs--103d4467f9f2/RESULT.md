# Swift chiral quantum walks on cones over bicyclic graphs

## Finding
Let \(B\) be a finite connected simple graph with \(|E(B)|=|V(B)|+1\), and let \(N=|V(B)|\). Form its cone by adjoining an apex \(o\) adjacent to every vertex of \(B\). On this cone consider zero-diagonal Hermitian adjacency-type Hamiltonians having modulus-one coupling on every edge. The apex-to-base phases can be made \(1\) by a diagonal unitary gauge transformation.

**Bicyclic swift-transport classification.** A choice of phases gives the apex survival law
\[
\left|\langle o|e^{-itH}|o\rangle\right|^2=\cos^2(\sqrt N\,t)\qquad(t\in\mathbb R)
\]
if and only if \(B\) has no degree-one vertex and is *not* a barbell comprising two vertex-disjoint cycles joined by a path with at least one even-length cycle. Equivalently, among connected bicyclic bases of minimum degree at least two, every theta graph and every figure-eight graph is swift; a barbell is swift precisely when **both** of its cycle lengths are odd. For any swift configuration,
\[
\Pr_o(X_t=v)=\frac{\sin^2(\sqrt N\,t)}{N}\quad(v\in V(B)),
\]
so full, uniform transfer from the apex occurs at \(t=\pi/(2\sqrt N)\).

**Phase-space refinement.** Fix labels, path orientations, and apex-edge phases equal to \(1\). For a theta graph consisting of three internally vertex-disjoint paths with lengths \(\ell_1,\ell_2,\ell_3\ge1\) (at most one equals \(1\), as \(B\) is simple), the swift phase space is two disjoint copies of the circle when the three lengths have the same parity, and exactly four isolated assignments when their parities are mixed. A barbell with two odd cycles, joined by any path of positive length, admits exactly eight assignments. The figure-eight case is asserted to be feasible; a count of all of its phase assignments is not part of this finding.

## Assumptions and scope
A *unit-gain adjacency matrix* \(Q\) of a simple undirected graph is Hermitian, has zero diagonal, and has \(Q_{uv}\in\mathbb C\) of modulus \(1\) exactly on edges. All couplings, including apex edges, have fixed modulus \(1\); no vertex potentials or amplitude tuning are permitted. Fix the apex gauge and set
\[
H=\begin{pmatrix}0&\mathbf 1^{\mathsf T}\\ \mathbf 1&Q\end{pmatrix}.
\]
Here the base vertices are indexed arbitrarily; \(\mathbf1\in\mathbb R^N\) is the all-ones column. The term *swift* refers specifically to the exact displayed all-time apex return law, not only rapid escape at one time. A *theta* has two degree-three endpoints and three mutually internally vertex-disjoint endpoint paths. A *figure-eight* has two simple cycles sharing exactly one vertex. A *barbell* has two vertex-disjoint simple cycles and a connecting path whose internal vertices lie on neither cycle. All cycle lengths are edge counts; a connecting path of length one is allowed. No arbitrary changes to edge magnitudes, graph topology, or initial state are included.

## Proof
**1. Exact reduction, including necessity.** Let \(e_o\) denote the apex basis vector, and let \(\mathbf j=(0,\mathbf1)^{\mathsf T}\). Direct multiplication gives
\[
H^2e_o=Ne_o+(0,Q\mathbf1)^{\mathsf T},\qquad
\langle e_o,H^4e_o\rangle=N^2+\|Q\mathbf1\|_2^2.
\]
Taylor expansion of the real survival probability (odd powers vanish because \(H\) is Hermitian) gives
\[
|\langle e_o,e^{-itH}e_o\rangle|^2
=1-Nt^2+\left(\frac{N^2}{3}+\frac{\|Q\mathbf1\|_2^2}{12}\right)t^4+O(t^6).
\]
As \(\cos^2(\sqrt N\,t)=1-Nt^2+N^2t^4/3+O(t^6)\), exact swift transport forces \(Q\mathbf1=0\). Conversely, if \(Q\mathbf1=0\), then the orthonormal pair \(e_o\) and \(\mathbf j/\sqrt N\) spans an invariant subspace with restricted Hamiltonian \(\bigl(\begin{smallmatrix}0&\sqrt N\\\sqrt N&0\end{smallmatrix}\bigr)\). Thus
\[
e^{-itH}e_o=\cos(\sqrt N\,t)e_o-i\sin(\sqrt N\,t)\,\mathbf j/\sqrt N,
\]
which proves both the survival law and the uniform base distribution. This reduction is closely related to the general cone criterion of Frigerio and Paris [1], and is reconstructed here to pin down necessity under exactly the present hypotheses.

**2. The complete bicyclic structure.** If a vertex of \(B\) has degree one, its row of \(Q\) contains exactly one entry of modulus one and cannot sum to zero. Suppose now that \(\deg_B(v)\ge2\) for all \(v\). The handshaking identity and \(|E|=|V|+1\) yield
\[
\sum_{v\in V(B)}(\deg_B(v)-2)=2.
\]
Hence either there is exactly one degree-four vertex and all other vertices have degree two, or exactly two degree-three vertices and all others have degree two. Following degree-two chains gives, respectively, a figure-eight; or, in the second case, either three paths between the branch vertices (theta) or a cycle at each branch vertex joined by a path (barbell). These alternatives are exhaustive for connected simple bicyclic graphs of minimum degree two.

**3. Forced phases along paths.** Orient a path \(w_0,w_1,\ldots,w_\ell\) whose internal vertices have degree two, and set \(z_j=Q_{w_jw_{j+1}}\). Vanishing of the row at \(w_j\) gives
\[
\overline{z_{j-1}}+z_j=0,\quad\text{so}\quad
z_j=\begin{cases}t&j\text{ even},\\-\overline t&j\text{ odd},\end{cases}\qquad t=z_0\in\mathbb T.
\]
Here \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). Thus the phase seen outward from the far endpoint is \(\overline t\) when \(\ell\) is odd and \(-t\) when \(\ell\) is even. Along a length-\(L\) simple cycle attached at a root of higher degree, the two cycle edges contribute at the root
\[
C_L(t)=\begin{cases}2\operatorname{Re}t&L\text{ odd},\\0&L\text{ even}.
\end{cases}
\]
This holds for every possible phase assignment satisfying the degree-two internal equations.

**4. Theta phase classification.** Orient the three paths from \(u\) to \(v\), with first-edge gains \(t_1,t_2,t_3\in\mathbb T\). The equation at \(u\) is \(t_1+t_2+t_3=0\). Three unit complex numbers have zero sum exactly when they form an equilateral triple: for some \(z\in\mathbb T\), their ordered list is \((z,z\omega,z\omega^2)\) or \((z,z\omega^2,z\omega)\), with \(\omega=e^{2\pi i/3}\). At \(v\), using step 3, the row equation becomes
\[
\sum_{\ell_j\text{ odd}}\overline{t_j}-\sum_{\ell_j\text{ even}}t_j=0
\quad\Longleftrightarrow\quad
2\operatorname{Re}\!\left(\sum_{\ell_j\text{ even}}t_j\right)=0.
\]
If all path lengths have the same parity, this is automatic, yielding precisely two circles distinguished by the orientation of the equilateral triple. Otherwise there is a unique *minority-parity* path \(j\); because \(t_1+t_2+t_3=0\), the second equation is equivalent to \(\operatorname{Re}t_j=0\). Therefore \(t_j\in\{i,-i\}\), and the other two phases can be placed in two orders, giving exactly four assignments. Every assignment thus obtained satisfies all rows of \(Q\mathbf1=0\). This proves existence for every theta and the asserted counts.

**5. Figure-eight existence.** Orient each of the two constituent cycles consistently and give all its forward edges gain \(i\) (backward edges gain \(-i\)). At every degree-two vertex, the two incident contributions are \(i\) and \(-i\). The same cancellation occurs separately on each cycle at their common degree-four vertex. Thus \(Q\mathbf1=0\). More generally, feasibility for every all-even-degree graph is known from [1]; only the present explicit construction is used.

**6. Sharp barbell parity obstruction and exact counts.** Let the two root vertices \(u,v\) be joined by a path of \(k\ge1\) edges, and denote by \(b\in\mathbb T\) the first bridge gain pointing away from \(u\). By step 3, the outward bridge contribution at \(v\) is \(-b\) if \(k\) is even and \(\overline b\) if \(k\) is odd. The root equation at a cycle of *even* length would be \(0+b=0\) (or the corresponding unit phase at \(v\)), which is impossible. So both cycles must be odd.

For odd cycle lengths, let \(t_u,t_v\in\mathbb T\) denote the gains of their respective first cycle edges, oriented around each cycle. Their root equations are
\[
2\operatorname{Re}t_u+b=0,
\qquad 2\operatorname{Re}t_v+c=0,
\]
where \(c\) is the outward bridge contribution at \(v\). Since both first terms are real and \(|b|=|c|=1\), the first equation forces \(b\in\{1,-1\}\). Along the bridge this gives \(c=(-1)^{k-1}b\). For either choice of \(b\), each root equation admits exactly the two solutions
\[
t_u=\frac{-b\pm i\sqrt3}{2},\qquad
t_v=\frac{-c\pm i\sqrt3}{2}.
\]
All other edge gains are forced by the degree-two recurrences. Hence there are precisely \(2\cdot2\cdot2=8\) swift assignments, and the necessity and sufficiency of both cycle lengths being odd is proved.

Combining steps 1–6 completes the all-graph classification and the separate phase-space claims.

## Verification
Run the embedded Python 3 standard-library checker via `python3 verify.py`. It independently constructs examples across theta lengths, figure-eight lengths, odd-odd barbell lengths, and the eight barbell phase choices; tests zero row sums directly; and compares cone apex moments through order twelve with those forced by \(\cos(\sqrt N\,t)\). It also tests the even-cycle local cancellation obstruction. Expected output:

```
VERIFY_OK constructed_cones= 1145 even_lobe_obstructions= 28 cone_moment_orders=1..12
```

This is finite corroboration only. Steps 1–6 are the unrestricted proof, including both directions and exact phase-space counts. The code uses floating-point complex arithmetic for roots of unity; the proof supplies the exact algebraic identities.

## Relationship to prior work
Frigerio and Paris [1] defined swift chiral walks and derived the essential zero-row-sum criterion on cone bases; their all-even-degree theorem implies figure-eight feasibility. They also characterized cubic regular bases using perfect matchings. Those general and regular-family results do not state the rank-two bicyclic classification, the even-cycle barbell obstruction, or the theta/barbell phase-space counts, which here require exploiting every degree-two path and both branch equations. The 2023 work by Annoni, Frigerio, and Paris [2] studies other graph constructions and transport between designated endpoints, rather than this apex problem. General unit-gain spectral analysis [3] supplies adjacent methodology but not an identified dominating fixed-all-ones-zero criterion for this entire family.

The scope is deliberately limited to phase-only Hermitian adjacency quantum walks and finite connected simple bicyclic bases. It does not claim novelty for the Frigerio–Paris cone reduction or their even-degree result.

## Limitations
The characterization fails to apply without at least one of the graph, Hamiltonian, or phase-normalization hypotheses; vertex potentials, variable coupling magnitudes, more-than-two-cycle bases, and other initial states are not classified. A universal novelty claim cannot follow from literature searches, and an unlocated more general unit-gain theorem could subsume some or all specializations. Phase counts are for labelled base graphs with chosen path and cycle orientations after fixing every apex edge phase to one; they are not counts modulo graph automorphisms or freely variable vertex gauges. No all-assignment count is claimed for figure-eight graphs. No independent audit has been performed.

## References
[1] M. Frigerio and M. G. A. Paris, *Swift chiral quantum walks*, arXiv:2207.05168, version 1 publicly submitted 2022-07-11; Linear Algebra and its Applications **673** (2023), 28–45. https://arxiv.org/abs/2207.05168.

[2] E. Annoni, M. Frigerio, and M. G. A. Paris, *Enhanced quantum transport in chiral quantum walks*, arXiv:2308.14747 (2023); Quantum Information Processing (2024). https://arxiv.org/abs/2308.14747.

[3] F. Belardo, M. Brunetti, and S. Khan, *NEPS of complex unit gain graphs*, Electronic Journal of Linear Algebra **39** (2023), 621–643, doi:10.13001/ela.2023.8015. https://doi.org/10.13001/ela.2023.8015. (Unit-gain spectral framework only.)
