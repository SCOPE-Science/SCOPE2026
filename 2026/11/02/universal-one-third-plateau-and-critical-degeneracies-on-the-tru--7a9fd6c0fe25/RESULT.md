# Universal one-third plateau and critical degeneracies on the truncated-tetrahedral Ising cluster

## Finding

Consider the finite classical Ising antiferromagnet on the 12 vertices of a truncated tetrahedron, with positive exchanges \(J\) on its twelve triangular-face edges and \(K\) on its six remaining edges. Every vertex has spin \(\sigma=\pm1\); a uniform nonnegative field \(h\) contributes \(-h\sigma\) at each vertex. For every \(J,K>0\), its complete ground-energy function is

\[
E_0(h)=\begin{cases}
-4J-6K,&0\le h\le K,\\
-4J-2K-4h,&K\le h\le K+2J,\\
12J+6K-12h,&h\ge K+2J.
\end{cases}
\]

Its exact ground-state multiplicities and total magnetizations are as follows. A magnetization entry in braces denotes the set of magnetizations attained at that one field, not a thermal average.

| Field | Ground-state count | Ground-state total magnetizations |
|---|---:|---|
| \(0\le h<K\) | 24 | \(0\) |
| \(h=K\) | 114 | \(\{0,2,4\}\), with counts \(24,60,30\) |
| \(K<h<K+2J\) | 30 | \(4\) |
| \(h=K+2J\) | 163 | \(\{4,6,8,10,12\}\), with counts \(30,72,48,12,1\) |
| \(h>K+2J\) | 1 | \(12\) |

In particular, the normalized zero-temperature magnetization has a ratio-independent one-third plateau for the whole open field interval \(K<h<K+2J\); both bounding transitions are jumps. The upper critical field has the unusually large, explicitly classified 163-state manifold. In the limit of zero temperature at the stated fixed field, the corresponding residual entropy is \(k_{\mathrm B}\log g\), where \(g\) is the count in the table.

## Assumptions and scope

Index the four untruncated tetrahedral vertices by \(i\in\{1,2,3,4\}\). Label each truncated-tetrahedral vertex by an ordered pair \((i,j)\), \(i\ne j\); vertices with the same first coordinate form a triangle, while the remaining six bonds join \((i,j)\) to \((j,i)\). The Hamiltonian is exactly

\[
H(\sigma)=J\sum_{i=1}^{4}\sum_{\{j,k\}\subseteq\{1,2,3,4\}\setminus\{i\}}\sigma_{ij}\sigma_{ik}
+K\sum_{1\le i<j\le4}\sigma_{ij}\sigma_{ji}
-h\sum_{i\ne j}\sigma_{ij}.
\]

The first sum includes three edges for each of four triangles. We assume \(J>0\), \(K>0\), \(h\ge0\), and no further interactions. At negative field the ground energies and counts follow by global spin inversion and replacing \(h\) by \(|h|\), with the magnetizations changing sign. All energies and counts refer to this finite 12-spin system, not its thermodynamic limit. The spins use \(\pm1\), not \(\pm\tfrac12\), normalization.

## Proof

**A local energy decomposition.** For a triangle with spin sum \(s\in\{-3,-1,1,3\}\), its interaction energy equals \(J(s^2-3)/2\), because the three spin products sum to \((s^2-3)/2\). It is at least \(-J\), with equality precisely when \(|s|=1\). For any bridge spins \(x,y\in\{\pm1\}\), the energy \(Kxy-b(x+y)\) has values \(-K\) for opposite spins, \(K-2b\) for two positive spins, and \(K+2b\) for two negative spins.

**Low-field regime.** For \(0\le h<K\), assign the entire field contribution to the six disjoint bridge pairs and none to the triangles. Every triangle costs at least \(-J\), and every bridge costs at least \(-K\), uniquely among its three pair types when its spins are opposite. Thus \(H\ge-4J-6K\); equality requires all four triangle sums to be \(\pm1\) and all bridges to have opposite spins. These constraints are simultaneously feasible: orient each edge of an abstract \(K_4\) toward the endpoint whose corresponding arc spin is negative, and choose an orientation with each vertex's indegree one or two. For example, a directed 4-cycle with oppositely oriented diagonals works. Therefore the bound is exact. At \(h=K\), bridges may instead have both spins positive, and the triangle conditions stay unchanged.

**Intermediate and high-field regimes.** For \(h\ge K\), split the field into a contribution \(-K(\sigma_{ij}+\sigma_{ji})\) on each bridge and a contribution \(-(h-K)\sum\sigma\) on the triangles. The bridge contribution \(Kxy-K(x+y)\) equals \(-K\) for opposite or both-positive spins and \(3K\) for both-negative spins. The triangle local energy becomes

\[
F(s)=\frac J2(s^2-3)-(h-K)s.
\]

When \(K<h<K+2J\), the unique minimizing triangle sum is \(s=1\). When \(h=K+2J\), sums \(s=1\) and \(s=3\) tie. When \(h>K+2J\), the unique minimizing sum is \(s=3\). In the open intermediate regime, one negative spin on each triangle and no bridge with two negative spins attain all local minima simultaneously: take the four negative positions as a function \(f\) with \(f(i)\ne i\) and no reciprocal two-cycle. Such functions exist; for example, a directed 4-cycle. At the upper boundary all configurations satisfying the corresponding local conditions attain the bound. Above it, all spins positive is the unique minimizer. Summing the local minima proves all three branches of \(E_0\), including their shared boundary values.

**Exact degeneracy counts.** The four triangles are indexed by vertices of \(K_4\), and each bridge corresponds to one unordered edge. In the low-field phase every bridge has exactly one negative spin, equivalent to orienting all six edges of \(K_4\). Every triangle must have either one or two negatives, equivalent to no zero-indegree or three-indegree vertex. The number is \(2^6-4\cdot 2^3-4\cdot2^3+(4\cdot3\cdot2)=24\): subtract the tournaments with a vertex of indegree 0 or 3; the only overlap is a specified source and sink, and the remaining edge has two orientations.

In the intermediate phase each triangle has exactly one negative spin; choose its location using a function \(f\) on four labels with three choices per label. The six possible reciprocal two-cycles each exclude nine choices; intersections of forbidden pairs can occur only for three disjoint pairings. Hence the number is \(3^4-6\cdot3^2+3=30\).

At the lower critical field, no bridge can have two negative spins and each triangle has one or two negatives. The total number \(q\) of negative spins is \(4,5,6\). For \(q=4\) the preceding count is 30. For \(q=6\), every bridge has one negative spin, giving the preceding tournament count 24. For \(q=5\), exactly one of the six bridges has no negative spin. Fix that bridge, say \(\{1,2\}\). On the other five bridges the negative location may be chosen in ten ways such that each triangle has one or two negatives: orient the four outer edges incident to \(1\) or \(2\), and then the remaining \(\{3,4\}\) edge; either direction of the latter admits exactly five valid outer orientations. There are six choices of absent bridge, yielding \(6\cdot10=60\). This proves \(24+60+30=114\), with magnetizations \(12-2q\).

At the upper critical field, every triangle has zero or one negative spin, and no bridge has two. For \(q=0,1,2,3,4\), choose the \(q\) triangles with negative spins and assign a non-reciprocal negative location in each. Straight inclusion-exclusion gives respective counts \(1,12,48,72,30\). More explicitly, at \(q=2\) there are \(\binom42(3^2-1)=48\); at \(q=3\) there are \(\binom43(3^3-3\cdot3)=72\); and at \(q=4\) there are \(3^4-6\cdot3^2+3=30\). The sum is 163, and the magnetizations are \(12-2q\). For higher field the all-positive state has degeneracy one. This exhausts every spin assignment through locally sharp bounds and equality characterizations, and proves the theorem for arbitrary real positive couplings.

## Verification

The independent finite enumerator in `verify_truncated_tetrahedron.py` constructs the twelve vertices, twelve triangle bonds and six connecting bonds directly from the ordered-pair labels; it scans all \(2^{12}=4096\) spin assignments using exact integer/rational arithmetic. For seven positive exchange pairs and a set of fields sampling all open regions and both boundaries, it independently compares the exact energy minimum, ground-state count, magnetizations and the local equality characterization of every configuration. It additionally checks the field-independent local counts, including the two critical degeneracies. Invoke it with `python3 verify_truncated_tetrahedron.py` using Python 3 standard library only. The output is a finite exhaustive corroboration of the analytical argument, not a substitute for its all-real-parameter proof.

## Relationship to prior work

Coffey and Trugman [1] identify the two inequivalent edge orbits of the 12-site truncated tetrahedron and investigate its Heisenberg antiferromagnet, including classical vector-spin states and quantum correlations. Their model is **not** the collinear Ising problem solved here: their classical vector-spin ground state attains a different triangle energy and their reported field response is continuous at a metamagnetic transition. The present theorem does not claim the graph, the two-bond Hamiltonian motif, frustration or magnetization plateaux generically as new.

Strečka, Karľová and Madaras [2] exactly enumerate Ising magnetization plateaux for the five **Platonic** solids, not the Archimedean truncated tetrahedron with independently variable triangular and intertriangle exchanges. Žukovič [3] studies finite planar triangular-lattice fragments with a single nearest-neighbor bond weight, not this closed two-orbit graph. The 2016 truncated-tetrahedral model [4] is a discrete spin-direction model **on the square lattice**, not Ising spins on the truncated-tetrahedral graph. The distinction assessed here is the complete parameter-uniform Ising field classification, its two exact thresholds and the 114/163-state critical manifolds. These comparisons do not establish absolute historical priority against all possible unpublished or unindexed results.

## Limitations

The conclusion is specific to the 12-vertex truncated tetrahedron, classical collinear spins, positive orbit-homogeneous exchanges, and a uniform field. It does not describe Heisenberg or quantum spin dynamics, finite-temperature phase transitions, disorder, other polyhedra, or a thermodynamic limit. The zero-temperature entropy counts are equilibrium degeneracy statements only. Historical originality has been assessed against the listed sources and searched records, not independently certified.

## References

1. D. Coffey and S. A. Trugman, *Correlations for the S=1/2 Antiferromagnet on a Truncated Tetrahedron*, arXiv:cond-mat/9206011 (first public 1992-06-26); *Phys. Rev. B* **46**, 12717 (1992). https://arxiv.org/pdf/cond-mat/9206011
2. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449 (2015-02-16). https://arxiv.org/abs/1502.04449
3. M. Žukovič, *Thermodynamic and magnetocaloric properties of geometrically frustrated Ising nanoclusters*, arXiv:1406.5626 (2014-06-21). https://arxiv.org/pdf/1406.5626
4. R. Krcmar, A. Gendiar and T. Nishino, *Phase diagram of a truncated tetrahedral model*, *Phys. Rev. E* **94**, 022134 (2016). https://doi.org/10.1103/PhysRevE.94.022134
