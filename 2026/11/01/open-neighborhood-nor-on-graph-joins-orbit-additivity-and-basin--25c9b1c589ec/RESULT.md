# Open-neighborhood NOR on graph joins: orbit additivity and basin concentration

## Finding

Let \(G\) and \(H\) be arbitrary **nonempty finite simple undirected graphs**, each with at least one vertex. Their **join** \(J=G\vee H\) is their disjoint union with every possible edge between the two vertex sets. For any graph \(X\), define the simultaneous open-neighborhood NOR map on binary configurations by
\[
(F_X(x))_v=\prod_{u\in N_X(v)}(1-x_u),
\]
with an empty product equal to one. The vertex's **own** state is not an input, and all updates are simultaneous. Let \(Q(X)\) denote the number of primitive temporal period-two *orbits* (not states), \(E(X)\) the number of fixed states, \(\delta(X)\) the indicator that \(X\) has no isolated vertices, and \(T(X)\) the number of **total dominating subsets** \(S\subseteq V(X)\), i.e. \(N_X(S)=V(X)\), where \(N_X(S)\) is the union of the open neighborhoods of vertices in \(S\).

**Join decomposition theorem.** For every such pair \(G,H\),
\[
\boxed{E(G\vee H)=E(G)+E(H),\qquad
Q(G\vee H)=Q(G)+Q(H)+1-\delta(G)-\delta(H).}
\]
Every configuration of every graph enters a fixed point or a primitive two-cycle after at most **one** update. The all-zero and all-one configurations of \(J\) form a primitive two-cycle. Its basin (including these two periodic configurations) has exactly
\[
\boxed{B_{0,1}(G\vee H)=1+
(2^{|V(G)|}-1)(2^{|V(H)|}-1)+T(G)+T(H).}
\]

In particular, for any nonempty graph \(G\) with \(n\) vertices and any integer \(m\ge1\), adjoining a clique \(K_m\) yields
\[
\boxed{E(G\vee K_m)=E(G)+m,\quad
Q(G\vee K_m)=Q(G)+1-\delta(G),}
\]
\[
\boxed{B_{0,1}(G\vee K_m)=2^{n+m}-2^n+T(G)-m+1.}
\]
Thus a clique leaves **every primitive two-cycle count unchanged** when \(G\) has no isolates, but produces exactly **one new** primitive two-cycle when \(G\) has at least one isolate. For fixed \(G\), the fraction of all binary initial configurations lying outside the universal two-cycle's basin is exactly
\[
\frac{2^n-T(G)+m-1}{2^{n+m}}\longrightarrow0
\qquad(m\longrightarrow\infty).
\]
So even when the number of primitive oscillatory orbits is conserved, almost every initial configuration is captured by one distinguished oscillation.

## Assumptions and scope

Graphs are finite, nonempty, simple, undirected, labelled for configuration counting, and loopless. Isolated vertices are permitted in the individual factors. The binary state alphabet is \(\{0,1\}\); no vertex is included in its own update neighborhood. A period-two orbit is an unordered temporal pair \(\{x,F_X(x)\}\) with distinct states and \(F_X^2(x)=x\). Basins are sets of **initial configurations** that eventually reach the specified attractor, not merely states on that attractor. There is no assumption of graph connectedness, regularity, or a particular number of vertices beyond nonemptiness.

## Proof

**1. Every transient has length at most one.** Identify a configuration with its set \(A\) of vertices in state one, and put \(\Phi_X(A)=V(X)\setminus N_X(A)\). This is precisely its state-one support after one NOR update. Because adjacency is symmetric, \(A\subseteq\Phi_X^2(A)\): if \(v\in A\), none of \(v\)'s neighbors can belong to \(\Phi_X(A)\). The map \(\Phi_X\) is inclusion reversing. Applying it to the inclusion gives \(\Phi_X^3(A)\subseteq\Phi_X(A)\); applying the same extensivity inclusion to \(\Phi_X(A)\) gives the reverse. Thus \(\Phi_X^3=\Phi_X\) identically. For every initial state \(A\), its successor \(\Phi_X(A)\) satisfies \(\Phi_X^2(\Phi_X(A))=\Phi_X(A)\), so it is on a fixed point or a two-cycle. This is an all-graphs identity, not an inference from finite experiments.

**2. Periodic supports in a join.** Write a configuration on \(J\) as the pair \((A,B)\) of its supports in \(G\) and \(H\). If \(A,B\) are both nonempty, then \(\Phi_J(A,B)=(\varnothing,\varnothing)\). If both are empty, \(\Phi_J(A,B)=(V(G),V(H))\). Hence these two global configurations form a primitive two-cycle, and no other periodic configuration can simultaneously have both supports nonempty. If \(A\ne\varnothing\) and \(B=\varnothing\), then
\[
\Phi_J(A,\varnothing)=(\Phi_G(A),\varnothing).
\]
The corresponding identity holds with the two factors interchanged. Consequently every factor's periodic orbit that avoids the empty support embeds in the join, with the other factor identically zero. These are all other periodic orbits, and they remain distinct.

For a nonempty factor \(X\), \(\Phi_X(\varnothing)=V(X)\), while \(\Phi_X(V(X))\) equals its set of isolated vertices. Thus the empty state is periodic **if and only if** \(X\) is isolate-free; in that event it belongs to exactly one primitive two-cycle, \(\varnothing\leftrightarrow V(X)\). The join contributes its own global two-cycle and excludes precisely one factor two-cycle for each isolate-free factor. This proves the stated formula for \(Q\), including both isolate boundary cases.

**3. Fixed states.** A nonempty support \(A\) satisfies \(A=\Phi_X(A)\) exactly when it is independent and every vertex outside it has a neighbor in it, equivalently \(A\) is maximal independent. Every fixed state of \(J\) is supported entirely in one factor, and exactly the fixed states of that factor remain. Therefore \(E(J)=E(G)+E(H)\).

**4. Exact basin of the universal two-cycle.** Because every orbit is recurrent after its first update, a state is in the basin of \(\varnothing\leftrightarrow V(J)\) exactly when its first image is \(\varnothing\) or \(V(J)\). The join has no isolated vertices. Thus \(\Phi_J(A)=V(J)\) occurs only for \(A=\varnothing\); and \(\Phi_J(A)=\varnothing\) occurs exactly for total dominating \(A\). A subset of \(V(J)\) is total dominating if and only if it meets **both** factors, or is contained in one factor and is total dominating there. The alternatives are disjoint. They contribute \((2^{|V(G)|}-1)(2^{|V(H)|}-1)\), \(T(G)\), and \(T(H)\), respectively. Add the empty initial set to obtain \(B_{0,1}\).

**5. Clique specialization.** The complete graph \(K_m\) has \(m\) maximal independent subsets (the singletons), and one primitive two-cycle (all zeros versus all ones) when \(m\ge2\); for \(m=1\) it has one fixed point, no primitive two-cycle, and one isolate. In either case \(Q(K_m)-\delta(K_m)=0\). Its total dominating subsets are precisely those of size at least two, so \(T(K_m)=2^m-m-1\) also for \(m=1\). Substitute these facts in the join identities. Taking the complement of the basin count gives the displayed concentration law. All claims follow.

## Verification

An independently implemented bit-mask checker directly constructs every graph with \(1\) to \(4\) labelled vertices and tests **all \(5{,}625\) ordered pairs** of such graphs. For every pair, it enumerates every state of the joined graph and computes the actual next and second states, the number of fixed points and primitive two-cycles, and the full two-cycle basin. It independently counts total dominating subsets of each factor. All equalities pass, including graphs with isolated vertices and both one-vertex boundary cases. A second deterministic-seed batch covers \(120\) additional pairs with factor orders through \(7\). The executable source and its observed output are embedded alongside this manuscript as `verify_join_nor.py` and `verification_output.txt`. Run using `python3 verify_join_nor.py` with a standard Python installation; no third-party packages are needed.

For a concrete illustration, take \(G=C_5\), which has \(E(G)=5\), \(Q(G)=6\), and \(T(G)=11\). Then \(G\vee K_3\) has \(8\) fixed states, still exactly \(6\) primitive two-cycles, and \(233\) of its \(256\) configurations lie in the universal oscillation basin. These values were recomputed by direct exhaustive iteration. The general theorem is established by the foregoing proof, not by these finite tests.

## Relationship to prior work

Jarrah, Laubenbacher, and Veliz-Cuba (arXiv:0805.0275, first posted May 2, 2008) classify network dynamics for **positive** conjunctive and disjunctive coordinate maps. The present map is antitone and uses exclusively open-neighborhood NOR, so their positive-map limit-cycle results neither imply the join identities nor apply through an identical update rule. Veliz-Cuba and Laubenbacher (2011) relate fixed states of AND-NOT networks to maximal independent sets; this is consistent with and precedes the fixed-point portion of our proof. Their publicly accessible abstract does not establish the join two-cycle or basin laws. Aledo and collaborators' work on maxterm/minterm parallel graph systems (2015 survey; 2017 and 2020 primary papers) specifies **self-inclusive** vertex neighborhoods. These differ from the open-neighborhood update here: in particular, their homogeneous NOR systems do not permit the fixed/two-cycle coexistence proved here. Fukś's explicit evolution formula for elementary cellular automaton Rule 5 treats the open-NOR rule on a ring, but not joins of arbitrary graphs or the associated basin decomposition. No equivalence or stronger result was identified in the examined material. This is a qualified literature assessment, not a proof of publication priority.

## Limitations

The formulas are specific to the **open-neighborhood** simultaneous NOR rule on finite simple undirected loopless graphs. They do not assert analogous behavior for directed, weighted, self-inclusive, asynchronous, or other Boolean threshold updates. The factor graphs must be nonempty; the isolated-vertex correction is essential (for instance, coning \(K_1\) creates a new global two-cycle). The exact basin formula concerns the all-zero/all-one attractor, not the individual basin sizes of every other attractor. Finite computation corroborates, but does not independently certify, the infinite all-graph theorem. Previously unindexed equivalent results are possible, and one relevant historical fixed-point paper was not accessible in full text.

## References

1. A. S. Jarrah, R. Laubenbacher, A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, arXiv:0805.0275 (first posted 2008-05-02), https://arxiv.org/abs/0805.0275.
2. A. Veliz-Cuba, R. Laubenbacher, *On the computation of fixed points in Boolean networks*, Journal of Applied Mathematics and Computing 39 (2012), 145–153; publicly posted 2011-10-15, https://doi.org/10.1007/s12190-011-0517-9.
3. J. A. Aledo, S. Martinez, J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), 594294, https://doi.org/10.1155/2015/594294.
4. J. A. Aledo, L. G. Diaz, S. Martinez, J. C. Valverde, *On the Periods of Parallel Dynamical Systems*, Complexity (2017), 7209762, https://doi.org/10.1155/2017/7209762.
5. J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), 9708347, https://doi.org/10.1155/2020/9708347.
6. H. Fukś, *Solvable Cellular Automata: Methods and Applications* (2023), rule-5 formula on the author's public companion page https://lie.ac.brocku.ca/~hfuks/solvableca.html.
