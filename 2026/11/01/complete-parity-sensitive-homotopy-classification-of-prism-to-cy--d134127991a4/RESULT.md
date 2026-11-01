# Complete parity-sensitive homotopy classification of prism-to-cycle Hom complexes

## Finding

For integers \(n\ge3\) and \(q\ge3\), let \(P_n=C_n\square K_2\) be the polygonal-prism graph, and let \(\operatorname{Hom}(P_n,C_q)\) be the ordinary (undirected) graph-homomorphism cell complex. Define
\[
W(n,q)=\{w\in\mathbb Z:|qw|\le n,\ qw\equiv n\pmod2\},\quad W^\circ(n,q)=\{w\in W(n,q):|qw|<n\}.
\]
Then the **complete homotopy type**, for all source and target sizes, is as follows.

* If \(q\) is odd, \(\operatorname{Hom}(P_n,C_q)\simeq\bigl(\coprod_{w\in W^\circ(n,q)}S^1\bigr)\amalg\coprod^{4q\mathbf1_{q\mid n}}\{\mathrm{pt}\}\).
* If \(q\ge6\) is even and \(n\) is even, \(\operatorname{Hom}(P_n,C_q)\simeq\bigl(\coprod_{w\in W^\circ(n,q)}(S^1\amalg S^1)\bigr)\amalg\coprod^{4q\mathbf1_{q\mid n}}\{\mathrm{pt}\}\).
* If \(q\) is even and \(n\) is odd, the complex is empty.
* If \(q=4\) and \(n\) is even, the complex has exactly two contractible connected components: \(\operatorname{Hom}(P_n,C_4)\simeq S^0\).

Each circle term is exactly one connected component, and the point terms are **actual isolated graph homomorphisms**, not merely contractible nontrivial components. The number of circle components for odd \(q\) is
\[
\begin{cases}1+2\lfloor(n-1)/(2q)\rfloor,&n\text{ even},\\2\lfloor(n+q-1)/(2q)\rfloor,&n\text{ odd},\end{cases}
\]
whereas for even \(q\ge6\) and even \(n\) it is \(2+4\lfloor(n-1)/q\rfloor\).

## Assumptions and scope

The graphs are simple, finite, undirected, loopless. The vertices of \(P_n\) are \((i,a)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\{0,1\}\); edges are consecutive rim edges and corresponding vertical rungs. The graph \(C_q\) has vertex set \(\mathbb Z/q\mathbb Z\) with adjacent residues differing by \(\pm1\). A cell of \(\operatorname{Hom}(G,H)\) is a function from source vertices to nonempty subsets of target vertices, with every pair of subsets on a source edge forming a complete bipartite adjacency in \(H\). Its vertices are ordinary homomorphisms and its one-skeleton consists of single-vertex recolorings.

For \(q\ne4\), each oriented graph edge has a unique signed color increment \(\epsilon_f(u,v)\in\{+1,-1\}\). Its rim winding \(w(f)\) is the signed increment sum around one rim divided by \(q\).

## Proof

**1. Square circulation and the possible winding numbers.** Assume first \(q\ne4\). Every square of the prism has signed circulation equal to a multiple of \(q\) and lying in \(\{-4,-2,0,2,4\}\). For \(q\ge5\) this forces zero, and for \(q=3\) it also forces zero since a nonzero multiple of three cannot be even with absolute value at most four. Consequently the signed sums around both rims coincide, since differences of rim chains are boundaries of squares. Their common sum is \(qw\), has parity \(n\), and absolute value at most \(n\). Conversely, for each \(w\in W(n,q)\), choose rim edge signs whose sum is \(qw\) and extend the top-rim coloring to the bottom by a constant \(+1\) color shift. This constructs a homomorphism with winding \(w\).

**2. Winding and target bipartition are recoloring invariants.** When \(q\ne4\), a legal single-vertex recoloring changes that vertex's color by \(\pm2\) (modulo \(q\)), and reverses all its incident signed increments. On every cycle the two changed incidences cancel, so integral rim winding is preserved. If \(q\) is even, the parity of the color at any fixed source vertex is also preserved. Since \(P_n\) contains an odd rim precisely when \(n\) is odd, no homomorphism to an even cycle exists in that case.

**3. All nonextreme orientations are acyclic.** For \(f\) with \(|qw(f)|<n\), orient each source edge in the direction of color increment \(+1\). The signed sum along any closed source walk is \(qw(f)m\), where \(m\in\mathbb Z\) is its horizontal winding in the annulus obtained by filling all prism squares. Any closed walk with nonzero winding \(m\) uses at least \(n|m|\) horizontal edges. A directed cycle of length \(L>0\) would have signed sum \(L\). For \(m=0\), this contradicts \(L>0\); for \(m\ne0\), it implies \(L=|qw(f)m|<n|m|\le L\). Therefore there is no directed cycle.

**4. Exact connectivity with winding and parity fixed.** Let \(f,g\) be two homomorphisms with equal \(w\). The integral cochain \((\epsilon_g-\epsilon_f)/2\) vanishes around every filled square and each rim, hence around every source graph cycle. It is therefore an integral coboundary \(dh\) for some \(h:V(P_n)\to\mathbb Z\). The difference between \(g\) and \(f+2h\pmod q\) is a common additive constant. When \(q\) is odd, multiplication by two is surjective modulo \(q\), so adding a constant to \(h\) makes them agree; when \(q\) is even, this is possible precisely if \(g\) and \(f\) have the same color parity at a source vertex.

Fix \(f\). If \(u\to v\) is an edge directed by \(\epsilon_f=+1\), the set of legal integer heights is exactly
\[
\mathcal H_f=\{h:V(P_n)\to\mathbb Z:h(v)\le h(u)\le h(v)+1\text{ for each }u\to v\}.
\]
The minimum of two legal heights, taken coordinatewise, is legal. For any legal heights \(p\le r\), let \(S=\{v:p(v)<r(v)\}\). On an arrow entering \(v\in S\) in the orientation induced by the coloring \(f+2p\), its predecessor must also be in \(S\), or the edge would violate the inequalities for \(r\). Since this coloring has the same nonextreme winding, Step 3 shows its orientation is acyclic. Thus there is a source vertex of the finite induced digraph on \(S\), which is also a source in the whole orientation; increasing \(p\) by one at that vertex is a legal single-vertex recoloring, staying \(\le r\). Repeating reaches \(r\). Joining arbitrary heights through their coordinatewise minimum proves the required connectivity. Therefore each nonextreme \(w\) contributes exactly one component for odd \(q\), and exactly two for even \(q\ge6\), distinguished by source-color parity.

**5. Each nonextreme component is a circle.** Fujii, Iwamasa, Kimura, Nozaki, and Suzuki [1, Theorem 5.1] prove that, for a connected source mapping to \(C_q\) with \(q\ge3\), \(q\ne4\), the Hom component is homotopy equivalent to a circle if the source orientation has no directed cycle, and is contractible otherwise. Steps 3–4 verify the first case for every nonextreme component, so each is \(S^1\).

**6. Extremal and square-target cases.** If \(|qw|=n\), the two rim increment sequences consist entirely of the same sign. The square equations then force every vertical increment to have a common sign. For each of the two horizontal signs, there are \(q\) starting colors and two vertical signs: \(2q\) homomorphisms per horizontal sign, yielding exactly \(4q\) when \(q\mid n\). The distinct colors of the two horizontal neighbors at every vertex prevent recoloring, so all are isolated. For \(q=4\), fold the target four-cycle by identifying its two vertices with the same neighbor set. The standard Hom-folding equivalence [1, Section 2; 2, Section 3] reduces \(\operatorname{Hom}(P_n,C_4)\) to \(\operatorname{Hom}(P_n,K_2)\): two points for a connected bipartite source (even \(n\)), and empty otherwise. Counting the admissible winding integers gives the displayed closed formulas.

## Verification

The standalone Python verifier `artifacts/verify_prism_targets.py` generates all homomorphisms by enumerating signed rim increments and vertical increment choices; it independently builds the recoloring graph and enumerates connected components. It checks the winding labels, parity-component multiplicities, and exact numbers of isolated extreme points on nineteen independently selected size pairs (target lengths \(3,5,6,7,8\); source sizes \(3\) through \(8\)). Recorded output is in `artifacts/verification_output.txt` and ends with `PRISM_ALL_CYCLES_WINDING_AND_COMPONENT_COUNTS_VERIFIED`. The finite experiments check component counts, **not** the circle homotopy types; the infinite-parameter homotopy conclusion follows from the six proof steps above and the cited published component theorem. The singular target \(q=4\) is handled by the folding theorem rather than by the signed-increment verifier.

## Relationship to prior work

Čukić and Kozlov [2] determine \(\operatorname{Hom}(C_m,C_q)\) for a single cycle source, not a two-rim prism. Fujii et al. [1] provide the universal point-or-circle component criterion for an arbitrary connected graph into any cycle, but do not state the prism component multiplicities or their even-target parity splitting. Matsushita [3] establishes a general square-free-target classification that similarly does not determine these precise component counts. The previously established pentagon-specific prism formula is a proper special case; the present classification also treats all even targets, the bipartite parity separation, all odd targets (including the triangle), and the exceptional folded square target.

## Limitations

The theorem is for the Cartesian-product prism family only, with cycle targets. It does not classify graph Hom complexes for arbitrary cubic sources or arbitrary square-free targets. The proof uses [1, Theorem 5.1] and the standard target-fold equivalence, rather than supplying independent proofs of those general results. No equivariant decomposition is asserted. Exhaustive experiments are limited to the listed finite size pairs; the all-parameter claim is mathematical, not extrapolated.

## References

[1] S. Fujii, Y. Iwamasa, K. Kimura, Y. Nozaki, A. Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, first public version 2024-08-09, arXiv:2408.04802, Theorems 1.1 and 5.1.

[2] S. L. Čukić and D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, first public arXiv version 2004-08-02, arXiv:math/0408015.

[3] T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, first public version 2024-12-26, arXiv:2412.19144.

