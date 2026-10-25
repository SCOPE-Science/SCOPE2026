# Three-coordinate rotation fixed loci in scale-two hypercube Vietoris–Rips complexes

## Finding
For every integer \(n\geq3\), let \(Q_n=\{0,1\}^n\) carry Hamming distance and let \(g\) cyclically permute its first three coordinate positions. Put \(m=n-3\). Then there is an integral homotopy equivalence
\[
\left|\operatorname{VR}_{\leq2}(Q_n)\right|^{\langle g\rangle}
\simeq \bigvee^{2^{m+1}-1}S^1\ \vee\ \bigvee^{2c_m}S^3,
\]
where \(c_0=c_1=c_2=0\), and for every \(m\geq3\),
\[
c_m=\sum_{0\leq j<i<m}(j+1)\bigl(2^{m-2}-2^{i-1}\bigr).
\]
For example, at \(n=6\) the fixed space is \(\bigvee^{15}S^1\vee S^3\vee S^3\). More precisely, the fixed set is piecewise-linearly homeomorphic to the simplicial orbit-admissibility complex described below; that complex simplicially collapses onto two copies of \(\operatorname{VR}_{\leq2}(Q_m)\) connected by exactly \(2^{m+1}\) internally disjoint paths of length two. The two copies are joined along endpoints only, never identified with each other.

## Assumptions and scope
The Rips threshold is **inclusive**: a finite vertex set spans a simplex precisely when every Hamming distance is at most two. The action rotates the first three **coordinate positions**, not bits by translation. The fixed set is the fixed-point subspace of the geometric realization, not the subcomplex of pointwise fixed vertices. The integer \(m\) may be zero; \(Q_0\) is a one-point metric space and its Rips complex is a point. Sphere multiplicity zero means no corresponding summand. No equivariant wedge splitting or classification at other scales is asserted.

## Proof
**1. Identify geometric fixed simplices exactly.** For any finite simplicial complex with a simplicial action of a cyclic group, each geometric fixed point has unique barycentric coordinates that are constant on every group orbit of vertices. A nonnegative choice of orbit weights is admissible precisely when the union of the positively weighted vertex orbits is a simplex. Scaling each orbit's common coordinate by its cardinality gives mutually inverse piecewise-linear maps between the fixed realization and the simplicial complex of compatible full vertex orbits. This does not incorrectly replace the fixed set by the pointwise-fixed-vertex subcomplex.

**2. Calculate all orbits and conflicts.** Split a word as \((x,u)\) with \(x\in Q_3\), \(u\in Q_m\). The four orbits on \(Q_3\), labeled \(A,B,C,D\), are
\[
A=\{000\},\quad B=\{111\},\quad C=\{100,010,001\},\quad D=\{110,101,011\}.
\]
All four have diameter at most two. For types \(a,b\), let \(M_{ab}\) be the maximum Hamming distance of a point in orbit \(a\) from a point in orbit \(b\). A direct six-coordinate-pair check, or enumeration of the displayed finite sets, gives the complete symmetric matrix in order \(A,B,C,D\):
\[
M=\begin{pmatrix}0&3&1&2\\3&0&2&1\\1&2&2&3\\2&1&3&2\end{pmatrix}.
\]
The full orbit vertices are \(a_u=(a,u)\), for \(a\in\{A,B,C,D\}\) and \(u\in Q_m\). Two **distinct** orbit vertices \(a_u,b_v\) can coexist exactly when
\[
M_{ab}+d(u,v)\leq2.
\]
In particular, the \(A\)-vertices and \(B\)-vertices separately each form \(K_m=\operatorname{VR}_{\leq2}(Q_m)\), but no \(A\)-vertex can meet a \(B\)-vertex. No two *distinct* vertices of type \(C\) or \(D\) can coexist, even across those types.

**3. Describe every link and perform elementary collapses.** For each \(u\in Q_m\), the link of \(C_u\) is the **disjoint union** of the full simplex on \(\{A_v:d(u,v)\leq1\}\) and the singleton \(B_u\). Indeed, two vertices of its closed radius-one Hamming ball differ in at most two coordinates; and any \(B\)-vertex is incompatible with every \(A\)-vertex. Similarly, the link of \(D_u\) is the simplex on \(\{B_v:d(u,v)\leq1\}\) disjoint from singleton \(A_u\).

Choose \(A_u\) as anchor of the \(C_u\)-cone. For every nonempty subset \(T\) of the other \(m\) vertices in the closed radius-one ball, in **decreasing order of \(|T|\)** remove the elementary free-face pair \(\{C_u\}\cup\{A_v:v\in T\}\) and \(\{C_u,A_u\}\cup\{A_v:v\in T\}\). By descending cardinality the lower member belongs to exactly the indicated remaining coface; outside this cone no simplex uses \(C_u\). The surviving new faces are only the edges \(C_uA_u\) and \(C_uB_u\) and their subfaces. Apply the analogous operation to each \(D_u\), retaining \(D_uB_u\) and \(D_uA_u\). All operations are independent because distinct \(C\)- and \(D\)-vertices never span common simplices. There are exactly \(2^{m+1}(2^m-1)\) elementary pairs, for \(m\geq0\).

**4. Identify the remaining homotopy type.** The remaining space consists of two vertex-disjoint copies of \(K_m\), and for each \(u\in Q_m\) two internally disjoint two-edge bridges from \(A_u\) to \(B_u\). Hence there are \(2^{m+1}\) bridges. Both copies of \(K_m\) are path connected for every \(m\geq0\). Choose one bridge as a connecting tree, and contract its interior together with arbitrary spanning trees within the copies. Each of the other \(2^{m+1}-1\) bridges contributes one independent circle; more formally, attaching one-dimensional bridges with endpoints in two path-connected spaces yields the wedge of those spaces and the stated free graph factor, by the homotopy pushout of the endpoint inclusions. Thus
\[
\left|\operatorname{VR}_{\leq2}(Q_n)\right|^{\langle g\rangle}
\simeq K_m\vee K_m\vee\bigvee^{2^{m+1}-1}S^1.
\]
Adamaszek and Adams, Theorem 1, prove \(K_m\simeq\bigvee^{c_m}S^3\) for all \(m\geq3\), with the displayed exact rank formula. For \(m=0,1,2\), \(K_m\) is a simplex and contractible. Substitution finishes the integral homotopy classification, including every small boundary value.

## Verification
The accompanying standalone `verify_fixed_c3.py` independently constructs the four genuine three-bit orbits and computes their exact maximum-distance matrix. For \(3\leq n\leq9\), it checks all 43,434 distinct orbit-vertex pairs against the asserted conflict rules. For \(3\leq n\leq7\), it constructs every face by the complete cone-link description, verifies 620 explicit elementary free-face collapses, and checks equality of the reduced face sets to the two-copy bridge model. Exact reduced mod-two Betti computations for \(3\leq n\leq6\) agree with the claimed integral homotopy. Running `python3 verify_fixed_c3.py` prints `VERIFY_OK`. The proof above is valid for unbounded \(n\); finite tests neither substitute for its steps nor establish integral homotopy by themselves.

## Relationship to prior work
Adamaszek and Adams established the exact **nonequivariant** homotopy type of \(K_m\) and its multiplicity \(c_m\); that input is not new here. Galetto, Montaño and Wellner (2026) establish the full hyperoctahedral **rational homology representation** of ambient hypercube Rips complexes at scale two (among other scales). A homology representation gives rational Lefschetz information for a symmetry but does not identify the geometric fixed-point homotopy type, its nontrivial fundamental group, or the two attached base copies. The present orbit-link and collapse classification provides those geometric data. Related studies of a **Hamming-weight-truncated** Rips sublevel or of intrinsic Čech complexes have different complexes and do not imply this fixed locus.

## Limitations
This is a geometric fixed-locus classification for the chosen three-coordinate cyclic subgroup at inclusive scale two only, not a full fixed-space classification for all coordinate permutations, not an equivariant equivalence of the ambient complex, and not a persistence theorem. It relies on the published nonequivariant sphere count, whose use is explicit. The originality comparison is against inspected and indexed literature; a presently unindexed equivalent result remains a possible priority risk.

## References
1. F. Galetto, J. Montaño, Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (public June 18, 2026), especially the introduction, Section 5, and Section 8.
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040v1 (public March 1, 2021), Theorem 1 and Table 1.
3. S. Oudot and L. Waas, *Function-Rips complexes in persistent homotopy theory: Stability and persistent Latschev theorems*, arXiv:2603.23460 (2026), a distinct function-sublevel setting used only for scope comparison.
