# Three-particle homotopy transitions on equilateral metric stars

## Finding

Let \(T_{m,L}\) be a metric star with \(m\ge 3\) arms, each a segment of length \(L>0\), attached at a common center. For \(r\ge0\) let
\[
\mathcal U_3(T_{m,L};r)=\{(x_1,x_2,x_3)\in T_{m,L}^{3}:d(x_i,x_j)\ge r\text{ for }i\ne j\}/\mathfrak S_3.
\]
Write \(\bigvee^{b}S^1\) for a wedge of \(b\) circles, interpreted as a point when \(b=0\). Define
\[
b_{\mathrm{small}}(m)=1+(m-1)\binom{m+1}{2}-\binom{m+2}{3}
=1+\frac{m(m+1)(2m-5)}6,
\]
\[
b_{\mathrm{middle}}(m)=1+2\binom m3-\binom m2.
\]
Then the **entire stagewise homotopy classification**, including the critical values, is
\[
\mathcal U_3(T_{m,L};r)\simeq
\begin{cases}
\{*\},&r=0,\\
\bigvee^{b_{\mathrm{small}}(m)}S^1,&0<r\le L/2,\\
\bigvee^{b_{\mathrm{middle}}(m)}S^1,&L/2<r\le L,\\
\coprod^{\binom m3}\{*\},&L<r\le2L,\\
\varnothing,&r>2L.
\end{cases}
\]
In particular, for a tripod the positive-separation stages are a wedge of three circles, then a point, then a point, before becoming empty; for a four-arm star their first Betti numbers are respectively \(11\), \(3\), and \(0\), with four components in the third nonempty regime. All homology groups in this classification are torsion-free.

## Assumptions and scope

The star is the finite metric tree obtained from \(m\) closed line segments of the same positive length, with their zero endpoints identified. Distance is the shortest-path metric. Particles are indistinguishable, are represented by exactly three coordinates modulo permutation, and must satisfy the **weak** separation inequality \(d(x_i,x_j)\ge r\). For \(r>0\) the particles are automatically distinct. At \(r=0\), collisions are allowed, so the space is the third symmetric product and not the distinct-point configuration space. Homotopy equivalence is not asserted to be a natural equivalence of persistence diagrams, and no calculation for unequal arm lengths or more than three particles is claimed.

## Proof

**1. Convex chamber cover.** By scaling we take \(L=1\) and put \(s=r/L\). For \(s>0\), assign each particle to an arm, counting a particle at the center as belonging to any one arm. Let \(\alpha=(\alpha_1,\ldots,\alpha_m)\) be the resulting occupancy vector, with nonnegative integer coordinates and \(\sum\alpha_i=3\). Denote by \(P_\alpha(s)\) the set of configurations admitting that assignment. On arm \(i\), choose sorted coordinates
\[
0\le t_{i,1}\le\cdots\le t_{i,\alpha_i}\le1.
\]
The separation inequalities reduce to
\[
t_{i,j+1}-t_{i,j}\ge s \quad (1\le j<\alpha_i),
\qquad t_{i,1}+t_{j,1}\ge s\quad(i\ne j,\ \alpha_i\alpha_j>0).
\]
Thus every nonempty \(P_\alpha(s)\) is the embedded image of a compact convex polytope. Within a fixed occupancy vector this coordinate map is one-to-one: at most one particle can occupy the center when \(s>0\). The finitely many chamber polytopes cover \(\mathcal U_3(T_{m,1};s)\).

**2. All intersections and the nerve.** If a configuration belongs to two *different* chambers, it must have one particle at the center; removing it leaves a unique occupancy vector \(\beta\) of total size two. Precisely the \(m\) chambers indexed by \(\beta+e_i\), for \(1\le i\le m\), contain this center-face configuration. Their common intersection is a convex polytope \(Q_\beta(s)\): it consists of the other two particles, with their distances from the center and each other at least \(s\). A center-face vector with both other particles on the same arm is feasible exactly for \(2s\le1\); one with the other particles on different arms is feasible exactly for \(s\le1\). Every nonempty multiple intersection of chambers is therefore contractible. At the equality cases it may degenerate to a lower-dimensional polytope, which is still contractible.

Let \(A_s\) be the feasible occupancy vectors \(\alpha\) of weight three and \(B_s\) the feasible center-face vectors \(\beta\) of weight two. By the nerve theorem for finite covers by subpolyhedra with contractible intersections, the configuration space has the homotopy type of the abstract nerve
\[
N_s=\bigcup_{\beta\in B_s}\Delta\bigl(\{\beta+e_i:1\le i\le m\}\bigr)
\ \cup\ \{\text{isolated vertices }\alpha\in A_s\text{ not already covered}\}.
\]
Two different simplices indexed by \(\beta\ne\gamma\) meet in at most one vertex. Indeed, if \(\beta+e_i=\gamma+e_j\) then \(\gamma-\beta=e_i-e_j\), fixing the only possible common occupancy vector; a second would force \(\beta=\gamma\). Each simplex may consequently be replaced, up to homotopy, by a star joining a new vertex \(\beta\) to its chamber vertices \(\beta+e_i\). This yields the finite bipartite **incidence graph** \(G_s\), with chamber vertices \(A_s\), center-face vertices \(B_s\), and an edge \(\beta\sim\beta+e_i\) for each feasible center face and each arm. The spaces therefore have the homotopy types of graphs. The replacement is valid also at \(s=1/2\) and \(s=1\), since all intersections remain convex subpolyhedra.

**3. Occupancy feasibility.** All three particles on one arm fit exactly when \(2s\le1\); two on one arm and one on another fit exactly when \(s\le1\); three on distinct arms fit exactly when \(s\le2\). For the converses, use positions \((0,s,2s)\) on one arm, positions \((0,s)\) on one and \(s\) on another, and three arm tips, respectively. The center-face conditions were established above. These are the only occupancy types, so there can be no other threshold.

**4. Graph homology and homotopy.** For \(0<s\le1/2\), the incidence graph has
\[
|A_s|=\binom{m+2}{3},\quad |B_s|=\binom{m+1}{2},\quad |E(G_s)|=m\binom{m+1}{2}.
\]
It is connected: the portion whose center-faces occupy two distinct arms is connected, since the edges of the complete graph on the arm set are linked through triangles; each remaining center-face (two particles on one arm) attaches through a chamber carrying two particles on that arm and one on another. Hence its first Betti number, \(|E|-|V|+1\), is exactly \(b_{\mathrm{small}}(m)\).

For \(1/2<s\le1\), only distinct-arm center-faces survive. The graph has
\[
|A_s|=m(m-1)+\binom m3,\quad |B_s|=\binom m2,\quad |E(G_s)|=m\binom m2.
\]
It is connected for the same triangle argument, and
\[
|E|-|A_s|-|B_s|+1
=1+2\binom m3-\binom m2=b_{\mathrm{middle}}(m).
\]
For \(1<s\le2\) the center-face set is empty, and the only feasible occupancy vectors have one particle on each of three distinct arms: the nerve is exactly \(\binom m3\) isolated vertices. For \(s>2\) there are no configurations. A finite connected graph is homotopy equivalent to a wedge of its first Betti number of circles, proving every positive-separation case.

Finally \(\mathcal U_3(T_{m,L};0)=\operatorname{SP}^3(T_{m,L})\) is contractible: contracting each point of the tree continuously along its arm to the center induces a contraction of its symmetric cube. Restoring the length scale proves the stated five regimes and endpoint inclusions.

## Verification

A standalone, dependency-free enumerator `verify_star3.py` constructs every feasible occupancy chamber and center face, builds the bipartite incidence graph, and checks its connected-component and first-Betti counts for all arm numbers \(3\le m\le11\) at seven representative or critical normalized separations. The exact output is embedded as `verification_output.txt` and reports `INCIDENCE_VERIFY_OK`. An additional direct linear-program feasibility stress-test, performed before acceptance but not required by the standalone verifier, checked every chamber and center-face inequality type for \(3\le m\le6\), including both critical values. These finite checks corroborate the chamber formulas; the general theorem rests on the proof above, not on an extrapolation from finite enumeration.

## Relationship to prior work

Dover and Özaydın, *Homeomorphism and Homotopy Types of Restricted Configuration Spaces of Metric Graphs* (arXiv:1301.5693, first submitted 2013-01-24), develop the convex-polytope cell model for **ordered** restrained graph configurations and a polynomial upper bound on the number of combinatorial types. Sections 3–5 were materially inspected. Their explicit examples and sharp lower bound are for two particles, rather than this all-arm-number, three-**unordered**-particle classification.

Deeley's 2011 article studies two thick particles on a metric graph, while the broad 2011 thesis abstract describes general finite-critical-value Morse theory and focuses its explicit algorithm on two particles. The thesis full text was inaccessible; it is not asserted to be noncovering beyond its accessible abstract. Li and Özaydın, arXiv:2603.00914 (2026), provide a persistent graph model for **second**, not third, restrained configurations of metric stars, and are context rather than the archive source. Wawrykow, arXiv:2401.13821 (2024), studies **ordered, unrestrained** star configurations. The small-separation rank is consistent with the classical graph braid group of a star; the new content here is the sharp bounded-arm-length transition across both positive separation thresholds and the full stagewise homotopy types.

## Limitations

The finding is specific to three indistinguishable particles, equal finite positive arm lengths, the geodesic metric, and weak separation. It does not classify inequilateral stars, labeled particles, fourth or higher particle counts, nor the natural maps on homology between stages (only each stage's homotopy type). The inaccessible 2011 thesis remains a literature-coverage risk.

## References

1. J. Dover and M. Özaydın, *Homeomorphism and Homotopy Types of Restricted Configuration Spaces of Metric Graphs*, arXiv:1301.5693 (initial public submission 2013-01-24), Sections 1, 3, 4 and 5; later journal DOI 10.1093/imrn/rnx061.
2. K. Deeley, *Configuration spaces of thick particles on a metric graph*, *Algebraic & Geometric Topology* 11 (2011), 1861–1892, DOI 10.2140/agt.2011.11.1861. Journal abstract materially checked.
3. K. Deeley, *Configuration spaces of thick particles on graphs*, Durham University thesis (2011), https://etheses.dur.ac.uk/862/; repository abstract materially checked, full thesis unavailable.
4. W. Li and M. Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914 (initial public submission 2026-03-01), Sections 1–3.
5. N. Wawrykow, *Homology generators and relations for the ordered configuration space of a star graph*, arXiv:2401.13821 (2024), Sections 1 and 5.
