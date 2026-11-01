# Signed-loop symmetry of two-particle rose configurations

## Finding

Let \(R_m=\bigvee_{i=1}^{m}S^1\) be the rose with \(m\ge 2\) circular petals and one common vertex, and let \(X_m=\operatorname{UConf}_2(R_m)\) be its unordered two-point configuration space. The signed permutation group \(B_m=(C_2)^m\rtimes S_m\) acts by petal permutations and independent reflection of individual petals. For \(g\in B_m\), let \(a(g)\) count petals fixed with their orientations preserved, \(b(g)\) count petals fixed with their orientations reversed, and \(r(g)\) count two-cycles in the underlying petal permutation. Then, for every \(m\ge2\) and every \(g\in B_m\),

\[
\operatorname{tr}\!\left(g\mid H_1(X_m;\mathbb Q)\right)
=1+\frac{3a(g)^2+2a(g)b(g)-b(g)^2-3a(g)-3b(g)}{2}-r(g).
\]

Moreover, \(X_m\simeq\bigvee^{1+3\binom m2}S^1\), so its integral first homology is free of rank \(1+3\binom m2\). The spaces fixed by *all* petal permutations and by *all* signed petal permutations have rational first-homology dimensions, respectively,

\[
\dim H_1(X_m;\mathbb Q)^{S_m}=2,
\qquad \dim H_1(X_m;\mathbb Q)^{B_m}=0.
\]

The character, not the underlying Betti number, is the principal finding.

## Assumptions and scope

The petals are topological circles with one common point \(o\), and distinct unordered particles are never allowed to collide, including at \(o\). The action fixes \(o\), permutes the petals, and can reverse the parametrization of each circle independently. Petal reflections are actual graph homeomorphisms of order two, not particle-label exchanges. All homology is ordinary singular homology, not Borel–Moore homology or homology of configurations with sinks. The formulas hold for integers \(m\ge2\) without an upper bound and are rational-representation statements except where integral homotopy and integral homology are explicitly asserted.

Subdivide each petal into a triangle: vertices \(o,a_i,b_i\), outward-oriented radial edges \(R_{i,a}:o\to a_i\) and \(R_{i,b}:o\to b_i\), and oriented peripheral edge \(E_i:a_i\to b_i\). Thus the graph has \(2m+1\) vertices and \(3m\) edges. This symmetric subdivision fulfills the two-particle discretization criterion: every embedded cycle has three edges and paths between distinct essential vertices have the required number of edges (there is only one essential vertex). The standard Abrams discrete cubical model \(UD_2(R_m)\) therefore represents \(X_m\) equivariantly under the indicated finite graph symmetries. Its \(k\)-cells are unordered selections of two open graph cells of combined dimension \(k\) whose closed supports are disjoint.

## Proof

**1. Complete cell census and one-dimensional homotopy type.** The cubic model has \(c_0=m(2m+1)\) unordered pairs of distinct graph vertices. Each oriented edge admits every graph vertex except its two endpoints, so \(c_1=3m(2m-1)\). Two radial edges always meet at \(o\). Disjoint edge-pairs are either a radial edge and a peripheral edge on a *different* petal, giving \(2m(m-1)\) squares, or a pair of peripheral edges on different petals, giving \(\binom m2\) squares. Hence \(c_2=5\binom m2\).

There is a concrete sequence of elementary cubical collapses. First, for every square \((R_{i,s},E_j)\) with \(i\ne j\), pair the square with its free edge \((a_j,R_{i,s})\), where a graph vertex is written first in a one-cell. This edge belongs to no other two-cell: the only graph edge incident to \(a_j\) disjoint from \(R_{i,s}\), other than \(E_j\), would be the radial edge \(R_{j,a}\), which shares \(o\) with \(R_{i,s}\). Thus there are \(2m(m-1)\) valid elementary collapses. Next, for each \(i<j\), the square \((E_i,E_j)\) is paired with its now-free edge \((a_j,E_i)\). Any former competing radial/peripheral square has already been removed, and no other peripheral/peripheral square contains this edge. Hence \(\binom m2\) further elementary collapses remove every two-cell.

The remaining one-dimensional graph is connected. To see this directly, any pair of outer vertices on different petals can be moved by a surviving peripheral edge (if needed) to include one \(b\)-vertex; a surviving radial one-cell then moves its other particle to \(o\). The pair \((a_i,b_i)\) similarly moves to \((o,b_i)\) along \(R_{i,a}\), and \((o,a_i)\) moves to \((o,b_i)\) along \(E_i\). Finally, the \((o,b_i)\) configurations are connected to one another through pairs \((b_i,b_j)\) using radial one-cells. The rank of the graph's fundamental group is therefore

\[
1-c_0+(c_1-c_2)
=1-m(2m+1)+3m(2m-1)-5\binom m2
=1+3\binom m2.
\]

A connected graph is homotopy equivalent to a wedge of precisely that many circles. This proves the integral homotopy and homology assertions, including \(H_k(X_m;\mathbb Q)=0\) for \(k\ge2\) and trivial \(H_0\) action.

**2. Signed cellular Lefschetz traces.** Fix \(g\in B_m\). Write \(a=a(g),b=b(g),r=r(g)\). Among the \(r\) two-cycles of petals, write \(u\) for those whose two reflections compose to an orientation-preserving return, and \(w\) for those whose return is orientation-reversing; \(u+w=r\). The chain traces, with the orientation of a square given by the ordered pair of its oriented edge coordinates, are

\[
\begin{aligned}
t_0&=\operatorname{tr}(g\mid C_0)=\binom{2a+1}{2}+b+2u,\\
t_1&=\operatorname{tr}(g\mid C_1)=3a(2a-1)-b(2a+1),\\
t_2&=\operatorname{tr}(g\mid C_2)
=2a(a-1)-2ab+\binom a2+\binom b2-ab-u+w.
\end{aligned}
\]

Here is a derivation to fix all orientation signs. The fixed graph vertices are \(o\) and the two outer vertices of each fixed non-reflected petal: \(2a+1\) vertices. A reflected fixed petal contributes one swapped outer-vertex pair, while an even-reflection petal two-cycle contributes two swapped outer-vertex pairs, giving \(t_0\). A fixed outward radial edge occurs twice per orientation-preserved fixed petal and may be accompanied by any of the remaining \(2a-1\) fixed outer vertices. A fixed peripheral edge occurs on every fixed petal, contributing \(a\) positive or \(b\) negative signs, and is disjoint from \(2a-1\) or \(2a+1\) fixed vertices, respectively; their sum is \(t_1\).

For squares, the radial/peripheral pairs fixed individually contribute \(2a(a-1)-2ab\). The individually fixed peripheral/peripheral pairs contribute \(\binom a2+\binom b2-ab\). Finally, a square consisting of the two peripheral edges on a transposed petal pair is fixed setwise: interchanging its two edge coordinates contributes an extra minus sign. The product of the two peripheral reflection signs is positive in the \(u\) cases and negative in the \(w\) cases, producing \(-u+w\). No square containing two radial edges is admissible, and no radial/peripheral type can be exchanged under these graph symmetries. These cases exhaust all fixed oriented cells.

The signed cellular Lefschetz identity holds for this invariant finite cubical complex. The equivariant discretization identifies its character with that of \(X_m\). Because the complex is connected and has no higher homology, \(\operatorname{tr}(g\mid H_1)=1-t_0+t_1-t_2\). Substitution, using \(u+w=r\), yields precisely

\[
1+\frac{3a^2+2ab-b^2-3a-3b}{2}-r.
\]

In particular the numerator is always even. The identity element has \(a=m,b=r=0\), recovering \(1+3\binom m2\).

**3. Averaging the two symmetry groups.** For \(S_m\), all flips vanish, hence \(b=0\) and the trace is \(1+3\binom f2-r\), where \(f\) is the number of fixed petals and \(r\) their number of transpositions. In a uniformly random permutation of at least two letters, \(\mathbb E\binom f2=\tfrac12\) and \(\mathbb E r=\tfrac12\); the character average is \(2\). This equals the multiplicity of the trivial representation in rational first homology.

For the full signed group, conditioned on an underlying permutation with \(f\) fixed petals, the independent orientation flips give \(a\sim\operatorname{Binomial}(f,\tfrac12)\) and \(b=f-a\). Directly averaging the trace polynomial over flips gives \(1+\tfrac12(f^2-3f)-r\). Since \(\mathbb E f=1\), \(\mathbb E f^2=2\), and \(\mathbb E r=\tfrac12\) for \(m\ge2\), the resulting character average is \(0\). This completes the proof.

## Verification

The attached standalone program `verify_rose.py` constructs the cubical cells directly, independently evaluates signed fixed-cell traces, checks every claimed free-face collapse and connectivity of the remaining one-skeleton, and enumerates every signed petal permutation for \(1\le m\le5\). The five cell triples are \((3,3,0)\), \((10,18,5)\), \((21,45,15)\), \((36,84,30)\), and \((55,135,50)\). Its exhaustive tests cover \(4282\) group elements in total, and its recorded output finishes with `VERIFY_OK`. Execute `python3 verify_rose.py` from the directory containing the extracted standalone script; no nonstandard packages are required. The finite checks corroborate the global argument but do not serve as an infinite proof.

## Relationship to prior work

Ghrist introduced the graph-configuration-space framework and proved essential-vertex dimension bounds, without the present signed-loop character. Farley and Sabalka describe the discrete cubical model and its subdivision hypotheses used here. Chettih and Lütgehetmann analyze ordered configuration spaces of trees with loops and their generators, rather than the complete signed action on ordinary first homology of *unordered* configurations of a rose. Maciążek and Sawicki study the homology of indistinguishable particles on one-connected graphs but do not present this full hyperoctahedral character. Lütgehetmann's representation-stability results and Gadish–Hainaut's compactly supported ordered-configuration results address other modules and do not state this character or the symmetry-fixed dimensions. Work on all-vertex-sink configurations, on particle-label swaps, or on Borel–Moore homology has different collision, coefficient, or equivariant structures and does not imply the displayed ordinary-homology character without an additional argument.

## Limitations

No explicit decomposition into irreducible \(B_m\)-representations over \(\mathbb Q\) or integral \(B_m\)-lattice classification is claimed. The two dimensions of invariant first homology are rational, not integral fixed-sublattice rank computations. The proof concerns precisely two unordered distinct particles; it does not claim the same pattern for three or more particles or for a general graph with several essential vertices. Priority relative to unindexed or inaccessible equivalent work cannot be guaranteed from searches alone. Independent expert audit has not been performed.

## References

1. R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, first posted 1999-05-05, arXiv:math/9905023, https://arxiv.org/abs/math/9905023.
2. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, first posted 2004-10-25, arXiv:math/0410539, https://arxiv.org/abs/math/0410539.
3. S. Chettih and D. Lütgehetmann, *The homology of configuration spaces of trees with loops*, arXiv:1612.08290, https://arxiv.org/abs/1612.08290.
4. T. Maciążek and A. Sawicki, *Homology groups for particles on one-connected graphs*, arXiv:1606.03414, https://arxiv.org/abs/1606.03414.
5. D. Lütgehetmann, *Representation stability for configuration spaces of graphs*, arXiv:1701.03490, https://arxiv.org/abs/1701.03490.
6. N. Gadish and M. Hainaut, *Configuration spaces on a wedge of spheres and Hochschild–Pirashvili homology*, arXiv:2202.12494, https://arxiv.org/abs/2202.12494.
