# Basin concentration for closed-neighborhood NOR on triangular graphs

## Finding

Let \(n\ge4\), let \(T_n=L(K_n)\) be the triangular graph, and identify its vertices with the edges of the complete graph \(K_n\). Consider the synchronous **closed-neighborhood NOR** map \(F\) on binary configurations: a vertex is on at the next step if and only if neither it nor any of its neighbors is on at the current step. Write \(E(W)=\binom{W}{2}\) for the complete edge set on \(W\subseteq[n]\). For \(m\ge0\), let
\[
c_m=\sum_{j=0}^{m}(-1)^j\binom mj2^{\binom{m-j}{2}},
\]
so \(c_m\) counts labelled simple graphs on \(m\) vertices without isolated vertices (with \(c_0=1\) and \(c_1=0\)).

**Exact attraction-basin classification.** Every state enters a primitive two-cycle after at most one update, with no fixed configurations. The periodic orbits are the distinguished pair \(\varnothing\leftrightarrow E([n])\), and the pairs
\[
E(W)\leftrightarrow E([n]\setminus W),\qquad 2\le |W|\le n-2,
\]
where complementary choices of \(W\) name the same orbit. There are exactly \(2^{n-1}-n\) distinct primitive two-cycles, comprising \(2^n-2n\) periodic configurations; all other configurations have first periodic-entry time exactly one.

The distinguished orbit attracts exactly
\[
\boxed{B_n=1+c_n+n c_{n-1}}
\]
initial configurations. Every other orbit corresponding to a complementary pair with \(|W|=m\) attracts exactly
\[
\boxed{c_m+c_{n-m}}.
\]
The distinguished orbit is the **unique largest attraction basin** for every \(n\ge4\). For a uniformly random initial configuration, its attraction probability has the sharp asymptotic law
\[
\boxed{\frac{B_n}{2^{\binom n2}}=1-\binom n2 2^{-(2n-3)}\bigl(1+O(n2^{-n})\bigr)}\quad(n\to\infty).
\]
Hence the number of distinct attractors grows exponentially with \(n\), while the fraction of initial configurations attracted to all but one of them is asymptotic to \(\binom n2 2^{-(2n-3)}\).

## Assumptions and scope

All graphs are finite, simple and labelled; edges of \(K_n\) index the Boolean coordinates of its line graph. The update uses the **closed** neighborhood of every coordinate, including that coordinate itself. It is not open-neighborhood NOR: dropping self-dependence changes the dynamics and may introduce fixed points. The attraction basin of a periodic orbit means the full set of initial configurations eventually entering that orbit, including its periodic configurations. The value \(c_0=1\) includes the empty graph on zero vertices. No randomness is assumed in the finite exact formulas; the probability statement uses independent fair initial bits.

## Proof

**1. The update identity.** For an initial edge set \(S\subseteq E([n])\), let \(U(S)\subseteq[n]\) be the set of endpoints incident with at least one edge of \(S\). Two coordinates of \(T_n\) are adjacent exactly when their associated edges share an endpoint. Because the rule includes self-dependence, a coordinate \(e\) updates to one precisely when \(e\) is disjoint from every edge in \(S\). Consequently,
\[
\boxed{F(S)=E([n]\setminus U(S))}.
\]
The right-hand side is the empty set when fewer than two vertices lie outside \(U(S)\). In particular, \(F(\varnothing)=E([n])\), \(F(E([n]))=\varnothing\). If \(S\ne\varnothing\) and \(2\le|U(S)|\le n-2\), then
\[
F(S)=E([n]\setminus U(S)),\qquad F^2(S)=E(U(S)),\qquad F^3(S)=F(S).
\]
If \(|U(S)|\ge n-1\), then \(F(S)=\varnothing\), followed by \(E([n])\). These cases prove \(F^3=F\) for every state, every eventual period is two, and all the displayed orbit pairs occur. No fixed state exists because a coordinate already on necessarily updates to zero, whereas the all-zero state updates to the all-one state. A nonperiodic initial state exists, for example two intersecting edges of \(K_n\), so the one-update entrance bound is sharp.

**2. Distinct cycles and their basins.** For \(W\) and its complement both of cardinality at least two, the configurations entering the pair \(E(W)\leftrightarrow E(W^c)\) are precisely the edge sets whose endpoint support is exactly \(W\) or exactly \(W^c\). These two classes are disjoint. The number of edge sets of support exactly a prescribed \(m\)-vertex set is \(c_m\), by the standard inclusion–exclusion count of graphs without isolated vertices. Hence this basin has \(c_m+c_{n-m}\) elements. The remaining configurations are the empty edge set and the nonempty edge sets whose endpoint support has cardinality \(n-1\) or \(n\); their count is \(1+n c_{n-1}+c_n\), which is the distinguished basin. Counting unordered complementary subsets with both sizes at least two yields
\[
1+\frac12\sum_{m=2}^{n-2}\binom nm=2^{n-1}-n
\]
two-cycles. Each has two periodic states, giving the exact first-entry census.

**3. Uniqueness of the dominant basin.** For every \(m\ge2\), there is an injection from graphs on \(m\) vertices without isolates into graphs on \(m+1\) vertices without isolates (attach the new vertex to a fixed existing vertex). Hence \(c_m\le c_{m+1}\). In particular, for every \(2\le m\le n-2\), a non-distinguished basin has size at most \(2c_{n-2}\). Starting from any isolate-free graph on \(n-2\) vertices, attach each of two fresh vertices to an arbitrary nonempty subset of the original vertices, with no edge between the fresh pair. This construction is injective and produces isolate-free graphs on \(n\) vertices. Thus
\[
c_n\ge (2^{n-2}-1)^2c_{n-2}>2c_{n-2},\qquad n\ge4.
\]
Therefore \(B_n\ge c_n\) strictly exceeds the basin size of every other orbit.

**4. Sharp probability deficit.** Identify a uniformly random edge set with the Erdős–Rényi graph \(G(n,1/2)\). It enters the distinguished orbit if and only if it has at most one isolated vertex **or it is the empty graph**. Let \(A_{ij}\) denote the event that both prescribed vertices \(i,j\) are isolated. Exactly \(2n-3\) distinct potential edges must be absent, so \(\mathbb P(A_{ij})=2^{-(2n-3)}\). If two distinct pairs overlap, three prescribed vertices are isolated and their intersection has probability \(2^{-(3n-6)}\); if disjoint, four prescribed vertices are isolated and the intersection has probability \(2^{-(4n-10)}\). The first two Bonferroni bounds give
\[
\mathbb P\Bigl(\bigcup_{i<j}A_{ij}\Bigr)
=\binom n2 2^{-(2n-3)}+O\bigl(n^3 2^{-(3n-6)}+n^4 2^{-(4n-10)}\bigr).
\]
The empty graph, which belongs to the distinguished basin despite having at least two isolated vertices, has probability \(2^{-\binom n2}\). Subtracting this probability, and dividing the error by the positive leading term, proves the claimed asymptotic with relative error \(O(n2^{-n})\).

## Verification

`verify_closed_nor.py` constructs the closed neighborhoods of \(T_n\) directly and exhaustively checks every initial configuration for \(n=4,5,6\), including its first-entry time, complete orbit key and individual basin count. `verify_closed_nor.cpp` uses independent base-edge support bitmasks, exhaustive state enumeration for \(n=4,5,6,7\), and the exact inclusion–exclusion formula. Both check orbit counts, the distinguished and other basins, the one-step bound and the absence of fixed points. Their actual outputs are included in `closed_nor_python_output.txt` and `closed_nor_cpp_output.txt`; all checks completed. Finite enumeration is a consistency check, not a substitute for the all-\(n\) proof.

## Relationship to prior work

The 2015 survey of Aledo, Martínez and Valverde describes synchronous minterm NOR graph dynamics with each vertex's own state included in its update. The general restriction to fixed points or two-cycles and the corresponding special all-negative, self-including NOR rule are established background; they are not claimed as new. Aledo and coauthors' 2017 paper gives the dichotomy of allowable periodic orbit types. Their 2020 paper provides a general combinatorial framework for counting periodic points of NAND/NOR graph systems, which can imply a periodic-point count after specialisation, and even states an exact count for \((N-2)\)-regular graphs (covering the periodic-point count for \(T_4\)). These are not novel ingredients here.

The specific claimed contribution is instead the **individual attractor-basin census on all triangular graphs \(T_n\)** and its **sharp dominant-basin concentration asymptotic**. Neither the surveyed Boolean dynamics theory nor the inspected 2017/2020 primary results states these basin formulas or the two-isolated-vertex rarity law. The 2014 AND–OR–NOT fixed-point paper concerns mainly fixed points and does not yield the claimed basin census. A plausible 2012 maxterm/minterm paper could not be read in full, so historical overlap beyond the accessible evidence is unresolved.

## Limitations

The classification is specifically for the closed-neighborhood NOR rule on \(L(K_n)\), with \(n\ge4\); it does not apply to open-neighborhood NOR, asynchronous rules, arbitrary line graphs or different Boolean functions. The asymptotic assumes independent fair initial bits, while exact basins are deterministic. Known universal two-period restrictions are acknowledged rather than reintroduced as discoveries. An earlier inaccessible primary paper on maxterm/minterm dynamics and unindexed exact studies remain possible overlap risks. No independent audit of the result is claimed.

## References

1. J. A. Aledo, S. Martínez, J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), article 594294, first published 24 March 2015, DOI: 10.1155/2015/594294.
2. J. A. Aledo, S. Martínez, F. L. Pelayo, J. C. Valverde, *Parallel discrete dynamical systems on maxterm and minterm Boolean functions*, Mathematical and Computer Modelling 55 (2012), 666–671, DOI: 10.1016/j.mcm.2011.08.040. Full text unavailable for direct comparison.
3. J. A. Aledo, L. G. Díaz, S. Martínez, J. C. Valverde, *On the Periods of Parallel Dynamical Systems*, Complexity (2017), article 7209762, DOI: 10.1155/2017/7209762.
4. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan, J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), article 9708347, DOI: 10.1155/2020/9708347.
5. J. Aracena, A. Richard, L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, J. Comput. Syst. Sci. 80 (2014), 1175–1190, DOI: 10.1016/j.jcss.2014.04.025.
