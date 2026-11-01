# Arm and pole symmetry of two-point generalized-theta configuration homology

## Finding
Let \(m\ge3\), let \(\Theta_m\) consist of two poles joined by \(m\) internally disjoint length-three paths, and set \(X_m=\operatorname{UConf}_2(|\Theta_m|)\). The group \(S_m\times C_2\) permutes the paths and, independently, interchanges the poles. There is a homotopy equivalence
\[
X_m\simeq\bigvee^{\binom m2}S^1.
\]
More substantially, as a *rational* representation of this full symmetry group,
\[
H_1(X_m;\mathbb Q)\cong\bigl(\bigwedge^2\mathbb Q^{[m]}\bigr)\boxtimes\varepsilon,
\]
where \(\mathbb Q^{[m]}\) is the permutation module of the arms and \(\varepsilon\) is the nontrivial character of the pole-swap group. If \(f\) is the number of fixed arms and \(t\) the number of two-cycles of an arm permutation \(\sigma\), then
\[
\operatorname{tr}\left((\sigma,\rho^\epsilon)\mid H_1(X_m;\mathbb Q)\right)=(-1)^\epsilon\left(\binom f2-t\right),\qquad \epsilon\in\{0,1\}.
\]
In particular, pole swapping acts as negative identity, while no nonzero class is invariant under all arm permutations. The non-equivariant first Betti number is covered by older general graph-braid homology formulas; the representation and pole-sign refinements are the finding.

## Assumptions and scope
The topological graph has vertices \(u,v,a_i,b_i\) and edges \(A_i=(u,a_i)\), \(B_i=(a_i,b_i)\), \(C_i=(v,b_i)\), with \(1\le i\le m\). All edges have unit topology; edge lengths are irrelevant to configuration-space homotopy. Pole interchange maps \(u\leftrightarrow v\) and \(a_i\leftrightarrow b_i\); each arm permutation maps its index as indicated. The space is **unordered**, points cannot coincide, and the representation assertion is rational (not a claim that an integral exterior-power lattice has been identified). Homotopy and integral homology assertions hold for every integer \(m\ge3\).

## Proof
**Cubical model.** The disjoint-closure unordered two-point cubical configuration complex \(D_m\) has vertices consisting of unordered pairs of different graph vertices, edges consisting of one graph vertex and one nonincident open graph edge, and squares consisting of unordered pairs of graph edges with disjoint closures. The standard sufficiently-subdivided graph-configuration theorem makes the natural inclusion \(D_m\hookrightarrow X_m\) a homotopy equivalence. It is equivariant as a map, hence it induces the same symmetry action on homology. The length-three subdivision satisfies the required conditions for two particles. The oriented graph edges are \(A_i:u\to a_i\), \(B_i:a_i\to b_i\), and \(C_i:v\to b_i\).

The cubical cell counts by dimension are
\[
(c_0,c_1,c_2)=\left(\binom{2m+2}{2},\,6m^2,\,\frac{7m^2-5m}{2}\right).
\]
For \(c_2\), begin with the \(\binom{3m}{2}\) pairs of edges and subtract the \(2\binom m2+2m\) pairs sharing an endpoint. Hence \(\chi(D_m)=1-\binom m2\).

**Integral collapse.** Every square has a freely removable boundary edge by the following ordered elementary-collapse scheme; here \((z,E)\) denotes the one-cell with stationary point at vertex \(z\) and moving point along edge \(E\). In the first stage remove all squares \(A_iC_i\) along \((a_i,C_i)\), all \(A_iB_j\), \(i\ne j\), along \((a_j,A_i)\), and all \(B_iC_j\), \(i\ne j\), along \((b_i,C_j)\). Each indicated one-cell belongs to just its named square even before any collapse: its stationary vertex has two incident graph edges, and the other candidate shares a pole with the moving graph edge (or shares a middle endpoint). In the second stage remove all \(A_iC_j\), \(i\ne j\), along \((a_i,C_j)\), since the sole alternative incident square \(B_iC_j\) has already been removed. Finally remove all \(B_iB_j\), \(i<j\), along \((a_i,B_j)\), since its sole alternative incident square \(A_iB_j\) has already been removed. These exhaust the five classes of disjoint edge pairs, and every chosen boundary edge is distinct. Thus \(D_m\) collapses to a connected graph. Connectivity follows by moving one token through the common poles while holding the other token on an available third arm; equivalently its one-skeleton is the connected two-token graph of a connected graph. From the Euler characteristic the resulting graph has first Betti number \(\binom m2\), proving the homotopy and integral homology claims.

**Character calculation.** Let \(\sigma\in S_m\) have \(f\) fixed arms and \(t\) two-cycles. For an automorphism, orient each fixed cell by the indicated ordering of the graph edges. The alternating sum of signed cellular traces equals the ordinary Lefschetz number, which is \(1-\operatorname{tr}(g\mid H_1)\) because the model is connected and has no homology above degree one.

Without pole interchange, the signed traces on the three cellular dimensions are
\[
\operatorname{tr}(C_0)=\binom{2+2f}{2}+2t,\quad
\operatorname{tr}(C_1)=6f^2,\quad
\operatorname{tr}(C_2)=\frac{7f^2-5f}{2}-t.
\]
The last negative term comes from swapping the two axes of an \(B_iB_j\) square on a two-cycle of the arms. Their alternating sum is \(1-\binom f2+t\), so the first-homology trace is \(\binom f2-t\).

With pole interchange, no graph vertex is individually fixed and hence \(\operatorname{tr}(C_1)=0\). The other signed traces are
\[
\operatorname{tr}(C_0)=1+f+2t,\qquad
\operatorname{tr}(C_2)=\binom f2-f-3t.
\]
Indeed a pole swap exchanges the two axes of each fixed \(A_iC_j\) square, yielding \(-f-2t\), while each invariant \(B_iB_j\) square contributes \(+1\) for two fixed arms and \(-1\) for a two-cycle. Therefore its first-homology trace is \(-\binom f2+t\). Finally, \(\bigwedge^2\mathbb Q^{[m]}\) has character \(\binom f2-t\), since a fixed two-element subset contributes its permutation sign. Rational representations of finite groups are determined by their characters, giving the claimed isomorphism. Averaging its character over \(S_m\) gives zero (for every unordered pair the transposition of that pair acts with opposite sign), proving the invariant statement.

## Verification
Run `python3 artifacts/theta_two_config_verify.py` with Python 3 and no dependencies beyond the standard library. The program constructs all zero-, one-, and two-cells, checks each square has zero cellular boundary-of-boundary, checks each claimed free elementary collapse against the complete live incidence map, checks connectivity, and computes signed fixed-cell traces for both pole choices. It exhausts all arm permutations for \(3\le m\le7\) and one representative of each cycle type for \(8\le m\le10\). The expected output in `artifacts/theta_two_config_verify.out` ends with `VERIFY_OK`. Finite tests corroborate the general structural argument and do not replace it.

## Relationship to prior work
Barnett and Farber develop the topology of two-particle graph configuration spaces; Kurlin and the subdivision results used by Ko and Park justify discrete cubical models. Ko and Park give a general first-homology rank and torsion formula for graph braid groups, which already subsumes the **nonequivariant rank**, and their paper explicitly discusses generalized theta graphs. The originality here is not a new Betti-number formula. An and Knudsen, in their theta-configuration results, and subsequent work on three-particle theta classes, concern different particle numbers, homological degrees, and representations. The new character handles the full arm-permutation and pole-interchange action for two unordered particles. Related configurations on other graphs and graph-metric Vietoris–Rips complexes are not the same object, and their theorems do not imply these characters.

## Limitations
No integral equivariant exterior-power lattice identification is asserted. The graph must have exactly two common poles and \(m\ge3\) parallel, internally disjoint arms; statements are not extended to graphs with additional branches or particles. A negative database search does not exclude equivalent unindexed literature. The homotopy collapse is not claimed to be equivariant; equivariance of the induced homology character follows from the equivariant inclusion into the configuration space.

## References
1. K. Barnett and M. Farber, "Topology of Configuration Space of Two Particles on a Graph, I," arXiv:0903.2180, first public 2009-03-12, https://arxiv.org/abs/0903.2180.
2. V. Kurlin, "Computing braid groups of graphs with applications to robot motion planning," arXiv:0908.1067, first public 2009-08-07, https://arxiv.org/abs/0908.1067.
3. K. H. Ko and H. W. Park, "Characteristics of graph braid groups," arXiv:1101.2648, first public 2011-01-13, https://arxiv.org/abs/1101.2648.
4. B. H. An and B. Knudsen, "On the second homology of planar graph braid groups," arXiv:2008.10371, https://arxiv.org/abs/2008.10371.
