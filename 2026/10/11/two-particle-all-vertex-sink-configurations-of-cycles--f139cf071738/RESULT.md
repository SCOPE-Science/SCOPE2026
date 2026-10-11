# Two-particle all-vertex sink configurations of cycles
## Finding
For every integer \(m\ge 3\), let \(C_m\) be the cycle with vertices \(v_0,\ldots,v_{m-1}\) and edges \(e_i=[v_i,v_{i+1}]\), with indices modulo \(m\), and declare all vertices to be sinks. For two labeled particles,
\[
\operatorname{Conf}^{\mathrm{sink}}_2(C_m,V(C_m))\simeq\bigvee^{m+1}S^1.
\]
If \(\tau\) swaps the two particle labels, then
\[
H_1(\operatorname{Conf}^{\mathrm{sink}}_2(C_m,V(C_m));\mathbb Q)
\cong \mathbf 1\oplus m\,\operatorname{sgn}
\]
as a rational \(S_2\)-module. Thus the character is \(m+1\) at the identity and \(1-m\) at \(\tau\).

## Assumptions and scope
The graph is the standard \(m\)-edge cellulation of a circle, not an unmarked topological circle: sink configuration spaces depend on the chosen vertex set. A collision is permitted exactly at a vertex. The particles are labeled. The assertion is for exactly two particles and every integer \(m\ge 3\).

## Proof
Chettih--Lütgehetmann's sink-configuration retraction and Ramos's equivalent discrete model give a finite coordinate-symmetric cubical model. For two particles with every vertex a sink, its cells are precisely products \(\sigma_1\times\sigma_2\subset C_m\times C_m\) for which two edge factors are never the same edge. Hence the model \(K_m\) is the product cellulation of the torus \(C_m\times C_m\) with the interiors of the \(m\) diagonal squares \(e_i\times e_i\) removed.

Choose, inside every diagonal square \(e_i\times e_i\), a small open disk \(D_i\) invariant under coordinate interchange. The disks are pairwise disjoint. The surface
\[
Y_m=(C_m\times C_m)\setminus\bigcup_i D_i
\]
is an orientable genus-one surface with \(m\) boundary components. Inside each diagonal square, the annulus obtained by deleting \(D_i\) deformation retracts onto the outer square boundary while fixing that boundary. Performing these retractions simultaneously gives \(Y_m\searrow K_m\). Therefore \(K_m\), and hence the sink configuration space, has the homotopy type of a genus-one surface with \(m\) boundary components. Such a surface retracts to a graph of rank \(2+m-1=m+1\), proving the wedge formula.

For the label transposition \(\tau\), use the product-cell orientation. On \(C_0(K_m;\mathbb Q)\), exactly the \(m\) cells \((v_i,v_i)\) are fixed, so the trace is \(m\). Every one-cell \(e_i\times v_j\) is exchanged with \(v_j\times e_i\), so the one-chain trace is zero. Every allowed two-cell \(e_i\times e_j\), with \(i\ne j\), is exchanged with \(e_j\times e_i\), so the two-chain trace is also zero. Thus the cellular Lefschetz number is \(L(\tau)=m\). Since the space is connected and has homology only in degrees zero and one,
\[
m=1-\operatorname{tr}(\tau|H_1),
\]
so \(\operatorname{tr}(\tau|H_1)=1-m\). Together with \(\dim H_1=m+1\), the \(+1\)- and \(-1\)-eigenspaces have dimensions \(1\) and \(m\), respectively. This is exactly \(\mathbf 1\oplus m\,\operatorname{sgn}\).

## Verification
The standalone verifier reconstructs the cellular chain complex for \(3\le m\le12\), checks \(\partial_1\partial_2=0\), and computes the boundary ranks modulo \(2,3,5,7\). In every case it obtains \(\operatorname{rank}\partial_1=m^2-1\), \(\operatorname{rank}\partial_2=m(m-1)\), Betti vector \((1,m+1,0)\), chain trace \((m,0,0)\), and the predicted label-swap eigenspace dimensions \((1,m)\). These finite computations are checks of the formulas, not a substitute for the all-\(m\) surface proof.

Reproduce with `python3 artifacts/verify.py`; the recorded output is `artifacts/verify_output.txt`.

## Relationship to prior work
Chettih and Lütgehetmann introduced sink configuration spaces and proved the coordinate-symmetric finite cube-complex deformation model used here. Their small examples include an interval with two sinks and a circle with a single sink. Ramos independently treats the all-vertices-sink convention, gives the general discrete cell model and Euler-characteristic formula, proves general asphericity, and computes complete homology formulas for trees. His paper emphasizes that the general non-tree case is substantially harder and that the theory depends on the chosen cell structure. The present statement specializes the all-vertices convention to the first canonical non-tree family, cycles with two particles, and adds the exact label-swap representation.

Searches of the published-finding index under sink-configuration, permitted-collision, cycle, punctured-torus, and label-swap formulations found no statement implying the displayed all-\(m\) wedge formula together with its \(S_2\)-character. The closest indexed configuration-space result concerns ordinary two-point configurations of finite crown spaces rather than graph sink configurations, and does not imply this claim.

## Limitations
No assertion is made for three or more particles, for partial sink sets, or for unordered sink configuration spaces. The novelty comparison is limited by the possibility of uncatalogued notes or computations; the strongest directly relevant primary sources inspected do not state or imply the full claim above. The modular chain calculations cover only \(3\le m\le12\); the proof for arbitrary \(m\) is the geometric deformation argument.

## References
1. S. Chettih and D. Lütgehetmann, *The Homology of Configuration Spaces of Trees with Loops*, Algebraic & Geometric Topology 18 (2018), 2443--2469. arXiv:1612.08290. DOI: 10.2140/agt.2018.18.2443. First public version: 2016-12-25. MSC: 55R80, 57M15.
2. E. Ramos, *Configuration spaces of graphs with certain permitted collisions*, arXiv:1703.05535, first public version 2017-03-16. In particular Definition 3.1 and Corollary 3.5 give the all-vertices-sink discrete model and cell count, while the exact homology theorem in that paper is for trees.
