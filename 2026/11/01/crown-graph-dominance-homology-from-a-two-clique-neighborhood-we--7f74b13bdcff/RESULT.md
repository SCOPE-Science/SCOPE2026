# Crown-graph dominance homology from a two-clique neighborhood wedge

## Finding
For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-M\) denote the crown graph, obtained from the complete bipartite graph on labeled parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\) by deleting exactly the matching edges \(a_i b_i\). The Lovász **open-neighborhood complex** of its graph complement satisfies
\[
\mathcal N(\overline{\operatorname{Cr}_n})\simeq
S^{n-2}\vee S^{n-2}\vee \bigvee^{n^2-3n+1}S^2.
\]
Consequently the **dominance complex**, formed from subsets whose complements dominate \(\operatorname{Cr}_n\), has reduced integral homology
\[
\widetilde H_j(\mathcal D(\operatorname{Cr}_n);\mathbb Z)
\cong
\begin{cases}
\mathbb Z^{n^2-3n+1},&j=2n-5,\ n\ge5,\\
\mathbb Z^2,&j=n-1,\ n\ge5,\\
\mathbb Z^7,&j=3,\ n=4,\\
0,&\text{otherwise}.
\end{cases}
\]
All of these integral groups are torsion-free. The two nonzero degrees coincide when \(n=4\), and are distinct for every \(n\ge5\). No wedge-of-spheres homotopy claim is made for the dominance complex itself.

## Assumptions and scope
All graphs are simple and finite; \(n\ge4\) is an arbitrary integer, not a tested cutoff. The crown graph has \(2n\) vertices and edges \(a_i b_j\) precisely when \(i\ne j\). Its complement \(G_n=\overline{\operatorname{Cr}_n}\) comprises two disjoint complete graphs on \(A\) and \(B\), together with the matching \(a_i b_i\). In graph-product notation \(G_n\cong K_n\square K_2\). Its open neighborhoods are
\[
N_{G_n}(a_i)=(A\setminus\{a_i\})\cup\{b_i\},\qquad
N_{G_n}(b_i)=(B\setminus\{b_i\})\cup\{a_i\}.
\]
The open-neighborhood complex \(\mathcal N(G_n)\) consists of all subsets belonging to one such neighborhood. The dominance complex \(\mathcal D(H)\) consists of \(\sigma\subseteq V(H)\) such that \(V(H)\setminus\sigma\) is a dominating set. All homology groups in the finding are *reduced*, with integer coefficients.

## Proof
**1. Two canonical subcomplexes.** Let \(\partial\Delta(A)\) and \(\partial\Delta(B)\) denote the boundary complexes of the simplices on the corresponding vertex sets. Set
\[
P=\partial\Delta(A)\cup\bigcup_{i=1}^{n}\Delta((A\setminus\{a_i\})\cup\{b_i\}),\qquad
Q=\partial\Delta(B)\cup\bigcup_{i=1}^{n}\Delta((B\setminus\{b_i\})\cup\{a_i\}).
\]
Every proper face of \(\Delta(A)\) lies in a neighborhood of some \(a_i\), and similarly for \(B\). Therefore the explicit neighborhood sets above show, face by face, that \(\mathcal N(G_n)=P\cup Q\).

**2. The two pieces are spheres.** For fixed \(i\), the simplex on \((A\setminus\{a_i\})\cup\{b_i\}\) is a cone with apex \(b_i\) on its base \(\Delta(A\setminus\{a_i\})\), a facet already contained in \(\partial\Delta(A)\). This simplex admits elementary collapses *relative to that base*. For example fix \(a_j\) with \(j\ne i\); pair each face containing \(b_i\) but not \(a_j\) with its \(a_j\)-augmentation, removing pairs in descending dimension. Because each apex \(b_i\) appears in only one of these cones, all these collapses coexist without affecting \(\partial\Delta(A)\). Thus \(P\searrow\partial\Delta(A)\cong S^{n-2}\). Likewise \(Q\searrow\partial\Delta(B)\cong S^{n-2}\).

**3. The intersection is precisely a crown graph.** Any simplex in \(P\) has at most one vertex from \(B\); any simplex in \(Q\) has at most one vertex from \(A\). Consequently \(P\cap Q\) is at most one-dimensional. Each of its vertices occurs, while \(\{a_i,b_j\}\) belongs to both pieces exactly when \(i\ne j\). Hence \(P\cap Q\) is the one-dimensional simplicial complex \(\operatorname{Cr}_n\), with exactly \(2n\) vertices and \(n(n-1)\) edges. This graph is connected for \(n\ge3\), and its first Betti number is
\[
\beta_1(\operatorname{Cr}_n)=n(n-1)-2n+1=n^2-3n+1.
\]

**4. Homotopy pushout.** The inclusions \(\operatorname{Cr}_n\hookrightarrow P,Q\) are cellular cofibrations. For \(n\ge4\), both \(P\) and \(Q\) are simply connected because each is homotopy equivalent to \(S^{n-2}\). Every map from the connected graph \(\operatorname{Cr}_n\) into either simply connected piece is null-homotopic (contract a spanning tree and then each remaining loop). The ordinary union is a homotopy pushout of these cofibrations. Replacing both attaching maps by constant maps in that homotopy pushout gives
\[
P\cup Q\simeq P\vee Q\vee\Sigma(\operatorname{Cr}_n).
\]
A connected graph with the stated cycle rank is homotopy equivalent to a wedge of \(n^2-3n+1\) circles; its unreduced suspension therefore has the homotopy type of the corresponding wedge of two-spheres. Combining with Step 2 proves the asserted homotopy equivalence for every \(n\ge4\).

**5. Integral Alexander duality.** For every graph \(H\), Matsushita and Wakatsuki established the exact simplicial identity \(\mathcal D(H)^\vee=\mathcal N(\overline H)\) [3], where \(\vee\) is combinatorial Alexander dual. Here the common vertex set has size \(2n\). Integral combinatorial Alexander duality therefore gives
\[
\widetilde H_j(\mathcal D(\operatorname{Cr}_n);\mathbb Z)
\cong\widetilde H^{2n-j-3}(\mathcal N(G_n);\mathbb Z).
\]
The wedge decomposition in Step 4 has free integral cohomology only in degrees \(2\) (rank \(n^2-3n+1\)) and \(n-2\) (rank two). These degrees agree only for \(n=4\), yielding total rank seven in degree two on the neighborhood side. Substituting into the Alexander-duality degree shift proves every displayed dominance-homology group, including vanishing and absence of torsion.

## Verification
Run `python3 verify_crown_topology.py` with standard Python 3.9 or later. For each \(4\le n\le8\), the checker independently enumerates the open-neighborhood and dominance faces from the actual graph adjacency, verifies combinatorial Alexander duality on all \(2^{2n}\) vertex subsets, checks \(P\cup Q=\mathcal N(G_n)\), and verifies the exact face-level identity \(P\cap Q=\operatorname{Cr}_n\). Exact mod-two simplicial boundary ranks corroborate the neighborhood homology for all five values and directly corroborate dominance homology for \(n=4,5,6\). The output is saved in `verification_output.txt`. For example, at \(n=5\), neighborhood ranks are \(11\) in degree two and \(2\) in degree three, while dominance ranks are \(2\) in degree four and \(11\) in degree five. These finite computations corroborate but do not prove the all-integer result; Steps 1–5 establish the integral theorem.

## Relationship to prior work
Matsushita [2] introduced general constraints on homological connectivity of dominance complexes and motivated exact calculations. Matsushita–Wakatsuki [3, Theorem 1.1] proved the Alexander-duality identity used in Step 5; neither work provides the crown-graph calculation here. Shukla [1] classified neighborhoods of maximum-degree-three graphs and four-regular circulants. The \(n\ge5\) complementary crown graphs have degree \(n\ge5\), so they are outside those classes; the four-clique-prism at \(n=4\) is not a circulant instance of the relevant specified family. A published theorem for rook graphs \(K_m\square K_\ell\) explicitly requires \(m,\ell\ge3\) [4], so it does not cover the matching-joined two-clique graph \(K_n\square K_2\). Another published theorem treats \(K_m\square C_\ell\) for \(\ell\ge5\) [5]; its crown-graph appearance as an interface does not compute this open-neighborhood complex or the dominance complex of a crown graph. Crown-graph dissociation/independence and finite-poset configuration calculations concern different complexes. The elementary homotopy-pushout technique is standard and is not itself claimed as new.

## Limitations
The theorem applies only to \(n\ge4\). The simply connected argument cannot be reused without modification at \(n=3\); no lower-bound extension is claimed. The dominance result is a complete *integral homology* computation, not a homotopy classification. The neighborhood result is a nonequivariant homotopy classification; symmetry modules are not calculated. The bibliography comparison includes accessible close results but cannot exclude an equivalent unindexed or inaccessible computation. No publication priority or independent validation is claimed.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13.

[2] T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145, first public 2020-09-09.

[3] T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first public 2023-12-05, Theorem 1.1.

[4] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45.

[5] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c.
