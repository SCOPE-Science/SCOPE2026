# Rim-edge deletion and parity-sensitive majority oscillations on fans and wheels

## Finding

For every integer \(n\ge3\), let \(F_n=K_1\vee P_n\) be the path fan with a hub and \(n\) labelled path vertices. Apply synchronous binary neighbor majority, with the current bit retained in a tie. Let \(N_F(n)\) denote the number of primitive temporal two-cycle **orbits**, identifying the two phases of an orbit but not graph automorphisms.

For integers \(m\ge3\), define the nonnegative integers \(c_m(a,b)\) by
\[
 c_m(0,0)=c_m(m,m)=1,
\]
\[
 c_m(a,a-r)=\frac{m}{r}\binom{a-r-1}{r-1}\binom{m-a-1}{r-1}
\]
when \(1\le a\le m-1\), \(1\le r\le\min(\lfloor a/2\rfloor,m-a)\), and set all other entries to zero. For \(m=2\), set \(c_2(0,0)=c_2(2,2)=1\), with all other entries zero.

**Theorem.** The fan has precisely two fixed configurations, the unanimous configurations, and its primitive two-cycle count is exactly
\[
 \boxed{N_F(n)=\sum_{2a>n>2b}c_n(a,b).}
\]
Every fan two-cycle flips its hub. All trajectories eventually have temporal period one or two.

For comparison let \(W_n=K_1\vee C_n\) be the wheel with the same hub and \(n\) rim vertices, and write \(N_W(n)\) for its primitive two-cycle count. For every odd \(n\ge3\),
\[
 \boxed{N_W(n)=N_F(n).}
\]
For even \(n=2m\ge4\),
\[
 \boxed{N_W(2m)=2+\sum_{a+c>m> b+d}c_m(a,b)c_m(c,d).}
\]
In particular, deleting one rim edge of the wheel can either **destroy or create** primitive two-cycles:
\[
 N_F(4)=0<2=N_W(4),\qquad
 N_F(12)=243>227=N_W(12).
\]
The odd-size equality counts recurrent orbits; it does not assert a conjugacy on all transient states.

## Assumptions and scope

The graph is finite, simple and labelled. The path \(P_n\) has vertices \(0,1,\ldots,n-1\), with edges joining consecutive integers. The hub is joined to every path vertex. Bits belong to \(\{0,1\}\). Every vertex updates **simultaneously** to the strict majority bit among its neighbors, retaining its old bit when the two bit counts tie. There are no stochastic choices, self-neighbor votes, or vertex identifications under graph symmetry. The wheel uses the same rule on \(C_n\), including \(n=3\).

A primitive two-cycle is an unordered pair \(\{s,t\}\) with \(s\ne t\), \(F(s)=t\), and \(F(t)=s\). The integer \(c_m(a,b)\) counts binary words on a labelled cycle of length \(m\) having no isolated one, exactly \(a\) ones, and exactly \(b\) cyclic edges with both endpoints one. In the auxiliary length-two case \(m=2\), the two directed cyclic adjacencies are counted with multiplicity, which is needed only for comparison with \(W_4\).

## Proof

**1. Reduction to AND and OR.** Write a configuration as hub bit \(h\) and path word \(x=(x_i)\). Define symmetric two-element neighborhoods
\[
 R_0=\{0,1\},\quad R_i=\{i-1,i+1\}\ (1\le i\le n-2),\quad R_{n-1}=\{n-2,n-1\}.
\]
They form the symmetric adjacency relation of a path with loops at its two endpoints. Define maps on binary path words by
\[
 (Ex)_i=\bigwedge_{j\in R_i}x_j,\qquad (Dx)_i=\bigvee_{j\in R_i}x_j.
\]
When the hub is zero, the path updates by \(E\); when the hub is one, it updates by \(D\). At an endpoint the tie-retention rule is exactly the insertion of its current bit as the second AND or OR argument. The hub becomes one from zero precisely when \(2\sum_i x_i>n\); it becomes zero from one precisely when \(2\sum_i x_i<n\).

**2. No nonconsensus fixed states and no hub-static primitive two-cycles.** If the hub is constantly zero over two updates, its path word satisfies \(E^2x=x\). Because \(R\) is symmetric, every length-two walk starting at \(i\) contains \(x_i\) among the AND operands, and hence \((E^2x)_i\le x_i\). More strongly, if \(x_i=1=(E^2x)_i\), all vertices reachable from \(i\) by a length-two \(R\)-walk also have bit one. The length-two-walk graph is connected: the underlying path is connected, and its endpoint loops eliminate the bipartite obstruction. Thus \(x\) is all zero or all one. The all-one path forces the hub to become one, so only unanimous zero can have a constantly zero hub. By bit complementation the analogous constantly-one hub case allows only unanimous one. This proves both fixed-state and hub-static period-two assertions.

**3. The auxiliary cycle.** Every primitive fan two-cycle therefore has a uniquely selected phase \((0,x)\) with hub zero, followed by \((1,y)\) with hub one. The path equations are
\[
 y=Ex,\qquad x=Dy,
\]
so \(x=DEx\). The unordered pairs \(R_i\) are exactly the edges of a single cycle on the path vertices. Indeed, the edges are \(\{0,1\}\), \(\{i-1,i+1\}\) for interior \(i\), and \(\{n-2,n-1\}\); their cyclic order is the even vertices in ascending order followed by the odd vertices in descending order, returning to zero. There are exactly \(n\) distinct edges, and the resulting graph is connected and two-regular for \(n\ge3\).

Each \((Ex)_i\) is one exactly when both endpoints of the corresponding auxiliary-cycle edge are one. Symmetry of \(R\) means that \((DEx)_j\) equals one precisely when \(j\) belongs to such a one-one edge. Therefore \(x=DEx\) if and only if every one in \(x\) has a one-neighbor on the auxiliary cycle. Equivalently \(x\) has **no isolated ones**. Put \(a=\sum_i x_i\) and \(b=\sum_i(Ex)_i\). The hub changes from zero to one and back precisely when \(2a>n>2b\). Thus the map from allowed auxiliary-cycle words to primitive fan two-cycle orbits is a bijection.

**4. Exact cyclic-run count.** The all-zero and all-one words contribute \(c_m(0,0)=1\) and \(c_m(m,m)=1\). For \(0<a<m\), write \(r\) for the number of runs of ones. A word with no isolated ones has \(r\) positive one-runs of length at least two and \(r\) positive zero-runs of length at least one. Their counts of ordered length compositions are respectively \(\binom{a-r-1}{r-1}\) and \(\binom{m-a-1}{r-1}\). Marking a starting vertex and then forgetting which of the \(r\) one-runs was marked multiplies the product by \(m/r\). Exactly \(a-r\) cyclic edges have two one endpoints. This gives \(c_m(a,a-r)\), and summing over the strict hub inequalities proves the fan formula. The same argument applies to a two-vertex cyclic component when each of its two directed adjacencies is counted separately.

**5. Wheel comparison.** On a wheel with hub zero, the rim update is AND of the two cyclic neighbors; with hub one it is OR. In the hub-flipping case the auxiliary edges join rim indices at cyclic distance two. For odd \(n\), those edges form one length-\(n\) cycle, with the same cyclic-run counts and hub inequalities as the fan. For even \(n=2m\), they form two length-\(m\) cyclic components (with the two edge occurrences retained if \(m=2\)). Their statistics \((a,b)\) and \((c,d)\) are independent, and the hub inequalities are \(a+c>m>b+d\). When the hub is static, the rim AND/OR square fixes only constants on each parity component; the two opposite alternating words form exactly one period-two orbit for each hub bit. They have exactly half of their rim bits equal to one, so the hub ties retain its bit. These give the extra two orbits. Other hub-static candidates do not form primitive cycles. The fixed configurations are again exactly the two unanimous states. The displayed wheel formulas and the odd-size fan-wheel coincidence follow.

**6. Exhaustion of eventual periods.** For any finite graph, encode bits as spins in \(\{-1,+1\}\) and let \(B\) be its symmetric adjacency matrix plus \(\tfrac12 I\). Majority with tie retention is exactly \(s(t+1)=\operatorname{sign}(Bs(t))\); no entry of \(Bs(t)\) vanishes. The integer- or half-integer-valued potential \(L_t=s(t+1)^TBs(t)\) obeys
\[
 L_t-L_{t-1}=(s(t+1)-s(t-1))^TBs(t)\ge0,
\]
strictly if \(s(t+1)\ne s(t-1)\), because the update chooses each coordinate to maximize its product with the nonzero corresponding field. This potential is bounded on the finite state space. Consequently it eventually stops increasing, forcing \(s(t+1)=s(t-1)\) thereafter. Thus no larger eventual periods occur. This independently proves the classical period-two bound in the present finite setting.

## Verification

Run `python3 verify.py` from the directory containing the embedded script. It requires only the Python standard library and produces the included `verification_output.txt`. The script enumerates every state of every fan for \(3\le n\le16\), independently simulates wheel dynamics for \(3\le n\le15\), and checks primitive two-cycle orbit counts against separately evaluated cyclic-run formulas. It also verifies the auxiliary opening condition on every path word for \(3\le n\le14\), compares the fan-wheel odd-size formulas for every odd \(n\le59\), and checks the two exact even-size sign examples. Finite tests corroborate but do not prove the all-size assertions.

## Relationship to prior work

Goles and Olivos (1980) proved the general period-two property of finite symmetric threshold automata. Benjamini et al. (arXiv:1405.2486, first public May 11, 2014) use the same tie-retention convention and study large and random graph limits; their full available text does not give this fan/wheel cycle census. Agur, Fraenkel and Klein (1988) give a detailed enumeration of *fixed points* of the radius-one majority cellular automaton on a cyclic word and develop the underlying run-counting techniques; their full eight-page article does not analyze majority dynamics on a fan with a globally voting hub. Veliz-Cuba and Geiser (arXiv:1609.02526, first public September 8, 2016) study fixed points of AND-OR networks on chains, without the globally coupled majority condition in the theorem here; comparison with the full article was limited by access.

The central feature here is a specific graph change: the endpoint tie convention on the path turns the two-input auxiliary relation into a single cycle even at even rim size. This yields the exact fan formula, odd-size invariance under one rim-edge deletion, and explicitly opposite effects of that deletion at two even sizes. Existing cycle-string enumeration is a component of the proof rather than an assertion that the entire counting method is new.

## Limitations

The theorem counts **recurrent** configurations and primitive cycles, not sizes of attraction basins or maximal transient times. Equality between fan and wheel for odd rim size is equality of recurrent orbit *counts*, not a full dynamical conjugacy. The numerical comparisons are exact finite checks, not exhaustive symbolic proof at unbounded \(n\). Bibliographic searches cannot establish absolute novelty; older literature might express the same invariant in different terms, and the AND-OR-network paper was not fully inspected. The graph-theoretic main claim is proved within this document, independently of computational logs.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first submitted May 11, 2014), https://arxiv.org/abs/1405.2486.
3. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), 295–302, DOI: 10.1016/0012-365X(88)90005-2. Full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.
4. A. Veliz-Cuba and L. Geiser, *The Number of Fixed Points of AND-OR Networks with Chain Topology*, arXiv:1609.02526 (first submitted September 8, 2016), https://arxiv.org/abs/1609.02526.
