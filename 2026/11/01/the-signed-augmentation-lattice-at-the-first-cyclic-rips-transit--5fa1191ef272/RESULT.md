# The signed augmentation lattice at the first cyclic Rips transition

## Finding

For every integer \(k\ge 2\), let \(C_{3k}\) be the simple cycle on \(\mathbb Z/(3k)\), and let
\[
X_k=\operatorname{Cl}(C_{3k}^{\,k})
\]
be the clique complex of its distance-\(k\) power (equivalently, the **inclusive** graph-metric Vietoris–Rips complex at scale \(k\)). The dihedral group
\[
D_{3k}=\langle r,s\mid r^{3k}=s^2=1,\ srs=r^{-1}\rangle
\]
acts by \(r(i)=i+1\) and \(s(i)=-i\), with indices modulo \(3k\).

Let \(E_k=\mathbb Z\{e_a:a\in\mathbb Z/k\}\), with integral dihedral action
\[
r e_a=e_{a+1},\qquad s e_a=-e_{-a}.
\]
Define \(\varepsilon:E_k\to\mathbb Z\) by \(\varepsilon(\sum_a c_a e_a)=\sum_a c_a\), where the target has trivial rotation and negative reflection action. Then the **complete integral homology representation** is
\[
\boxed{\widetilde H_2(X_k;\mathbb Z)\cong\ker\varepsilon,\qquad
\widetilde H_i(X_k;\mathbb Z)=0\quad(i\ne2).}
\]
The isomorphism is integral and equivariant. In particular, \(X_k\simeq\bigvee^{k-1}S^2\), and the homology action factors through the quotient that sends \(r\) to rotation of \(k\) residue classes.

For a rotation \(r^a\), the rational top-homology character is \(k-1\) if \(a\equiv0\pmod{k}\) and \(-1\) otherwise. For a reflection \(r^a s\), it is
\[
\boxed{\operatorname{tr}(r^as\mid H_2(X_k;\mathbb Q))=
1-\#\{b\in\mathbb Z/k:2b\equiv a\pmod{k}\}.}
\]
Thus the reflection trace is zero for odd \(k\); for even \(k\) it is \(-1\) when \(a\) is even and \(+1\) when \(a\) is odd. The rotation-\(r^a\)-fixed homology rank is \(\gcd(k,a)-1\), where \(\gcd(k,0)=k\).

## Assumptions and scope

All cycles are undirected and have no loops. Distances are shortest-path distances in \(C_{3k}\), and every pair of vertices at distance at most \(k\) spans an edge in its power. Geometric realization of an abstract finite simplicial complex is understood. The oriented simplex \([a,a+k,a+2k]\) uses the displayed cyclic order (and not necessarily increasing representatives modulo \(3k\)). Every group action is the action induced by its permutation of simplicial vertices. The claim covers **all integers** \(k\ge2\), not merely the tested examples.

## Proof

**1. Classify all cliques.** Let \(A_k\) be the subcomplex whose simplices fit inside some consecutive circular interval \(\{i,i+1,\ldots,i+k\}\). Every simplex of \(A_k\) is a clique. Conversely, fix a clique \(Q\) and translate one of its vertices to \(0\). All other vertices are either \(a\in\{1,\ldots,k\}\) or \(-b\) with \(b\in\{1,\ldots,k\}\). If only one sign occurs, \(Q\in A_k\). If both occur, let \(a\) and \(b\) be their respective maxima. Adjacency of \(a\) and \(-b\) forces
\[
\min(a+b,3k-a-b)\le k,
\]
so either \(a+b\le k\) or \(a+b\ge2k\). In the first case the clique lies in \([-b,a]\), an interval of at most \(k\) steps. In the second case \(a=b=k\); no other nonzero vertex can be adjacent to both \(k\) and \(-k\). Therefore the only cliques not in \(A_k\) are the \(k\) exceptional triangles
\[
T_a=\{a,a+k,a+2k\},\qquad 0\le a<k.
\]
Every edge and vertex of each \(T_a\) already belongs to \(A_k\), and no higher-dimensional exceptional face exists. Accordingly \(X_k\) is obtained from \(A_k\) by attaching exactly these \(k\) two-simplices along their complete boundaries.

**2. Identify the arc core.** Regard \(\mathbb R/(3k)\mathbb Z\) as a circle. Fix \(0<\delta<1/4\) and define the open circular arcs \(U_i=(i-\delta,i+k+\delta)\) modulo \(3k\). Their nerve is precisely \(A_k\): a collection of arcs has common intersection exactly when its indices lie in an interval of \(k+1\) successive integral positions. Since each arc has length \(k+2\delta<3k/2\), every nonempty finite intersection is itself an open arc, hence contractible. The arcs cover the circle. The nerve theorem therefore gives \(A_k\simeq S^1\).

More concretely, send vertex \(i\) to \(\exp(2\pi\mathrm i\,i/(3k))\). On each simplex of \(A_k\), extend affinely in the complex plane and normalize radially to the unit circle, obtaining \(f:|A_k|\to S^1\). This is well-defined since each face occupies an arc of angle at most \(2\pi/3\), whose convex hull avoids the origin. The embedded \(3k\)-cycle is mapped with degree \(+1\). Because \(H_1(A_k;\mathbb Z)\cong\mathbb Z\), this proves that \(f_*:H_1(A_k;\mathbb Z)\to H_1(S^1;\mathbb Z)\) is an isomorphism. The map is dihedrally equivariant, where rotations rotate the circle and reflections reverse its orientation.

**3. Compute the relative attachment map integrally.** Orient \(T_a\) as \([a,a+k,a+2k]\). Its boundary travels through three circular arcs of length \(k\), giving degree \(+1\) under \(f\), so all \(k\) exceptional triangles map to the **same primitive** positive generator of \(H_1(A_k;\mathbb Z)\). Since \(C_j(X_k,A_k)=0\) for \(j\ne2\) and \(C_2(X_k,A_k)\cong\mathbb Z^k\), the relative long exact sequence contains
\[
0\longrightarrow H_2(X_k;\mathbb Z)\longrightarrow
\mathbb Z^k\xrightarrow{(1,\ldots,1)}\mathbb Z
\longrightarrow H_1(X_k;\mathbb Z)\longrightarrow0.
\]
Thus \(H_2(X_k;\mathbb Z)=\ker(1,\ldots,1)\), the first homology vanishes, and all other reduced integral homology is zero. Attaching one triangle along a degree-one circle loop kills the fundamental group; attaching the remaining \(k-1\) disks then produces a wedge of \(k-1\) two-spheres.

**4. Preserve dihedral orientation signs.** The arcs and their nerve are dihedrally invariant. Rotation acts on the oriented relative triangles by \(r[T_a]=[T_{a+1}]\), including the wraparound case, which is an even three-cycle of ordered vertices. Reflection acts by \(s[T_a]=-[T_{-a}]\). The boundary target \(H_1(A_k;\mathbb Z)\cong\mathbb Z\) has rotation \(+1\) and reflection \(-1\), so the integral boundary map is equivariant, and its kernel has exactly the stated action. Traces follow from the signed permutation action on \(E_k\) after subtracting the one-dimensional sign character of the quotient. For rotations the fixed-residue count is either \(k\) or zero; for \(r^as\) it is the number of solutions of \(2b\equiv a\pmod{k}\). This proves the formulas for every \(k\ge2\).

## Verification

The standalone dependency-free program `verify_cycle_power.py` reconstructs all simplices as cyclic interval faces plus exceptional triangles, independently brute-forces clique membership for \(2\le k\le4\), checks face and boundary conditions and computes exact signed simplicial Lefschetz traces for every rotation and reflection for \(2\le k\le8\). The output is in `verify_cycle_power_output.txt`; each tested parameter passed. These finite tests corroborate the **all-parameter** cover-and-attachment proof, rather than replacing it.

To reproduce: run `python3 verify_cycle_power.py` from the extracted package directory. No external Python modules, proprietary datasets, or unlisted files are required.

## Relationship to prior work

Adamaszek's *Clique complexes and graph powers* (first submitted 2011-04-03, arXiv:1104.0433), Corollary 6.7, already gives the nonequivariant wedge \(X_k\simeq\bigvee^{k-1}S^2\). **That homotopy classification is not claimed as new.** The present refinement identifies the full **integral dihedral module**, including the reflection sign and all elementwise traces, which the cited nonequivariant theorem does not imply.

Adamaszek, Adams, Frick, Peterson and Previte-Johnson, *Nerve complexes of circular arcs* (first submitted 2014-10-16, arXiv:1410.4336), Proposition 7.2, determine dihedral actions for **nerve** complexes of evenly spaced arcs. Their Section 8 separately identifies the clique complex of cycle powers and provides a homotopy equivalence to a nerve complex with **a different number of vertices** (Theorem 8.5). That comparison does not intertwine the full \(D_{3k}\)-action on the clique complex. In particular, the signed reflection action here is not obtained simply by transporting a nerve character along an unspecified equivariant map. The two complexes and the direction of their respective group actions must not be conflated.

## Limitations

The integral module is determined only at the first singular ratio \(k/(3k)=1/3\), not at all higher critical winding fractions. The result does not classify equivariant homotopy types, integral homology of ordinary orbit spaces, or persistence maps at adjacent scales. An equivalent calculation in unindexed material remains possible; independent mathematical assessment has not been performed.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public version 2011-04-03, especially Corollary 6.7. https://arxiv.org/abs/1104.0433
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336, first public version 2014-10-16, especially Propositions 7.2–7.3 and Theorems 8.2, 8.5. https://arxiv.org/abs/1410.4336
3. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, first submitted 2015-03-12, background on winding-fraction homotopy transitions. https://arxiv.org/abs/1503.03669
