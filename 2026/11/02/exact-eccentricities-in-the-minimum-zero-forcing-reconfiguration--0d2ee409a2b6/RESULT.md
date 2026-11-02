# Exact eccentricities in the minimum zero-forcing reconfiguration graph of gear graphs

## Finding
For every integer \(m\ge4\), let \(G_m\) be the gear graph obtained by subdividing every rim edge of the wheel on \(m\) rim vertices exactly once. Its minimum zero-forcing sets have size three. Write \(\mathcal R_m\) for their *token-jumping reconfiguration graph*: a vertex is a minimum zero-forcing set and two vertices are adjacent when their sets differ in exactly one vertex. Then \(\mathcal R_m\) has \(5m\) vertices, \(11m\) edges, is connected, and its complete eccentricity distribution is given by five explicit rotational classes. In particular,
\[
\operatorname{rad}(\mathcal R_m)=\left\lfloor\frac{3m+3}{4}\right\rfloor,
\qquad
\operatorname{diam}(\mathcal R_m)=\left\lfloor\frac{3m+6}{4}\right\rfloor.
\]
The two classes \(A,B\) (each containing \(m\) configurations) have eccentricity equal to the diameter; class \(D\) (\(m\) configurations) has eccentricity equal to the radius. Classes \(C,E\) have radius eccentricity unless \(4\mid m\), in which case they have eccentricity radius plus one. Thus every individual configuration's farthest-set distance is determined for all \(m\ge4\).

## Assumptions and scope
Use indices \(i\) modulo \(m\), a hub \(h\), rim vertices \(u_i\), and inserted vertices \(v_i\). Edges are \(hu_i\), \(u_iv_i\), and \(v_iu_{i+1}\). Under standard zero forcing, blue vertices iteratively force their unique white neighbor; a set is zero forcing when this reaches all vertices. The five families of minimum sets are
\[
\begin{aligned}
A_i&=\{h,u_i,v_i\},&B_i&=\{h,u_{i+1},v_i\},\\
C_i&=\{u_i,v_i,v_{i+1}\},&D_i&=\{u_{i+1},v_i,v_{i+1}\},\\
E_i&=\{u_{i+2},v_i,v_{i+1}\}.
\end{aligned}
\]
The zero-forcing number three and classification up to symmetry are prior literature; the new object of study is the *exact all-size metric* under named-vertex one-for-one exchanges. Every formula concerns this token-jumping graph, not token slides along edges of \(G_m\).

## Proof
**1. State space and graph.** Directly inspect the forcing rule at the hub and the inserted vertices. A two-vertex initial set cannot force the gear: before the hub turns blue, the two blue vertices cannot enable the pair of consecutive inserted vertices needed for an initial force sequence; with the hub initially blue, it cannot force when at least two spokes remain white. For three starting vertices without the hub, the only possibility is two consecutive inserted vertices together with one of the three incident rim vertices; these give \(C_i,D_i,E_i\). With the hub, the initial rim-inserted pair must be incident, yielding \(A_i,B_i\). Each displayed triple forces around the rim, and the five families are distinct for \(m\ge4\). (An exhaustive independent check of all triples for \(4\le m\le10\) is supplied; the all-size elementary forcing classification is also consistent with the cited gear-graph study.)

Two triples are adjacent precisely when their intersection has size two. A direct intersection calculation gives the *entire* adjacency rule (indices modulo \(m\)):
\[
\begin{array}{c|l}
A_i&B_i,B_{i-1},C_i,D_{i-1}\\
B_i&A_i,A_{i+1},D_i,E_{i-1}\\
C_i&A_i,D_i,D_{i-1},E_i\\
D_i&A_{i+1},B_i,C_i,C_{i+1},E_i,E_{i-1}\\
E_i&B_{i+1},C_i,D_i,D_{i+1}
\end{array}
\]
Hence four classes have degree four and class \(D\) degree six; handshaking yields \(11m\) edges. The path \(A_i,B_i,A_{i+1}\) traverses the cyclic indices and every other class is adjacent to an \(A\) or \(B\) class; hence the graph is connected.

**2. Explicit distance certificate on the infinite cyclic cover.** Replace the residue class \(i\bmod m\) in the preceding neighbor table by \(i\in\mathbb Z\). For each source type \(s\in\{A,B,C,D,E\}\), target type \(t\), and displacement \(j\in\mathbb Z\), define \(f(s,t,j)\) from the complete integer table `verification/cover_distance_table.json`:
\[
f(s,t,j)=\begin{cases}
\texttt{small}[s][t][j+5],&-5\le j\le5,\\
\lfloor3j/2\rfloor+\texttt{positive}[s][t][j\bmod2],&j\ge6,\\
\lfloor3(-j)/2\rfloor+\texttt{negative}[s][t][(-j)\bmod2],&j\le-6.
\end{cases}
\]
All three arrays are included in full rather than quoted from an external computation. The verifier checks the *algebraic Bellman certificate*: \(f\ge0\), the only zero is its source, neighboring labels differ by at most one, and every nonzero vertex has a neighbor with value exactly one smaller. These conditions prove, in both directions, that \(f\) is the genuine graph distance from the source: the edge-Lipschitz condition bounds every path from below, and repeatedly descending by one constructs a path of the claimed length. The finite check covers every possible branch change at indices \(-10,\ldots,10\). For each tail, the integer formula changes by exactly three under displacement by two, so these finite checks also prove all the remaining infinitely many cases. This is a finite verification of an explicit symbolic formula, **not** an inference from sampling finite graph sizes.

**3. Descend to a finite gear.** Any path between configurations on the finite cyclic-index graph lifts to a path on the infinite cover; conversely, any lifted path projects to a finite path. Therefore
\[
d_m((s,0),(t,j))=\min_{q\in\mathbb Z} f(s,t,j+qm),\quad 0\le j<m.
\]
The displayed table verifies that, for each source/target type, \(f(s,t,j)\) is nondecreasing as a function of \(\lvert j\rvert\) on either ray from magnitude four onward, and that its four smaller arguments never exceed the value at magnitude four. Consequently the two closest translates suffice:
\[
d_m((s,0),(t,j))=\min\{f(s,t,j),f(s,t,j-m)\}.
\]
This exact identity is also checked directly against the reconfiguration graph in the independent exhaustive program for the stated small cases.

**4. All-size maxima by a four-step induction.** Define \(e_s(m)=\max_{t,\,0\le j<m}d_m((s,0),(t,j))\). The standalone metric verifier evaluates this explicit finite maximum for every \(4\le m\le27\) and confirms the five claimed eccentricity formulas. To establish them for *all larger* \(m\), let \(m\ge24\) and \(b=\lfloor m/2\rfloor\). Split the displacement range into the central band \(b-5\le j\le b+5\) and the two outside intervals. Within the central band, both displacement arguments have magnitude at least six; the two tail formulas give
\[
d_{m+4}((s,0),(t,j+2))=d_m((s,0),(t,j))+3.
\]
Outside the band, monotonicity from the previous step bounds every candidate distance by a boundary value \(f(s,t,b-5)\) on the left or \(f(s,t,b+5-m)\) on the right. The verifier checks at \(m=24,25,26,27\) that both boundary maxima are at most the central-band maximum; all three increase by exactly three under \(m\mapsto m+4\). Thus *for each residue class modulo four* the global maximum remains in the central band and satisfies \(e_s(m+4)=e_s(m)+3\) indefinitely. The explicit formulas have precisely this recurrence and match the base cases, completing the proof.

## Verification
Run `python verification/verify_gear_direct.py` and `python verification/verify_gear_metric.py` from the package's root directory, using Python 3 standard library only. The direct verifier exhaustively checks every triple's forcing outcome for \(4\le m\le10\), the exact graph, connectivity, and eccentricities. The metric verifier verifies the infinite-cover Bellman identities by a finite symbolic branch-and-tail check; it verifies the two-lift reduction, all base cases and the induction inequalities. Successful output reports `DIRECT_ZERO_FORCING_ALL_TRIPLES_PASS`, `DIRECT_TOKEN_JUMP_ALL_PAIRS_PASS`, `INFINITE_COVER_BELLMAN_PASS`, `RING_PROJECTION_AND_BASE_CASES_PASS`, and `ALL_SIZE_ECCENTRICITY_INDUCTION_PASS`.

## Relationship to prior work
Zero forcing was developed in the minimum-rank setting and subsequent propagation-time work. The 2020 study *Reconfiguration graphs of zero forcing sets* formulates the token-jumping process on minimum zero-forcing sets. The gear-graph study *The zero forcing numbers and propagation times of gear graphs and helm graphs* proves the zero-forcing number and classifies possible minimum configurations up to isomorphism; those are **not** novel assertions here. Unlike these statements, the theorem above gives a complete labelled reconfiguration adjacency structure and sharp, type-by-type farthest-distance results for the entire two-parameter family \((m,\text{configuration})\). The corresponding stronger distance conclusions were not found in the inspected primary works or targeted searches; a historical equivalent under another name remains possible.

## Limitations
This concerns standard zero forcing and token-*jumping* between minimum sets on gear graphs with \(m\ge4\), not weighted forcing, token sliding, or arbitrary graphs. The cover table is an explicit, independently replayable finite certificate for the all-integer distance lemma. Computational checks of finite sizes alone would not prove the theorem; the tail identities and induction are essential. Self-review does not constitute an independent scholarly audit. An unindexed earlier presentation of the distance theorem cannot be ruled out.

## References
1. *Propagation time for zero forcing on a graph*, arXiv:1410.4191, first publicly submitted October 15, 2014. https://arxiv.org/abs/1410.4191
2. Geneson, Haas and Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first publicly submitted September 1, 2020. https://arxiv.org/abs/2009.00220
3. Anderton et al., *The zero forcing numbers and propagation times of gear graphs and helm graphs*, arXiv:2310.18513, first publicly submitted October 27, 2023. https://arxiv.org/abs/2310.18513
