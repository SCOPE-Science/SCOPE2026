# Sharp synchrony-time laws for three-color inhibitory oscillators on complete split graphs

## Finding
For all integers \(m\ge2\) and \(n\ge1\), consider the synchronous three-color inhibitory firefly rule on the complete split graph \(G_{m,n}=K_m\vee\overline{K_n}\). The first global synchronization time \(T\) belongs to \(\{0,1,2,3,4,5,6,\infty\}\) and depends **only** on which colors occur in the clique and in the independent set, not on their multiplicities. The exact decision table appears below.

Put \(u=2^m-2\), \(v=3^m-3\cdot2^m+3\), \(U=2^n-2\), and \(V=3^n-3\cdot2^n+3\). The numbers \(N_t=\#\{x:T(x)=t\}\) of labelled initial configurations are
\[
\begin{aligned}
N_0&=3,\\
N_1=N_3&=2^n(u+1),\\
N_2&=3^n(u+v)+2^n(u+1),\\
N_4&=2^n-2,\\
N_5&=u(3^n-2^n-1)+3^n-3,\\
N_6&=u(3^n-2^{n+1}+1)+3^n-2^n-1,\\
N_\infty&=V.
\end{aligned}
\]
These values sum to \(3^{m+n}\). Every configuration that never synchronizes is **already periodic at time zero**: the entire clique has color \(2\) and the independent set uses all three colors. It has primitive period three. Every other initial state synchronizes within six updates. The upper bound six is attained whenever \(n\ge2\); for \(n=1\), the sharp upper bound is three. The system has exactly \(1+V/3\) primitive three-cycle orbits and no other periods.

Under independent uniformly random initial colors, for any fixed \(m\ge2\), as \(n\to\infty\), the limiting probabilities at times \(2\), \(5\), \(6\), and \(\infty\) are respectively
\[
\frac{3^m-2^{m+1}+1}{3^m},\quad
\frac{2^m-1}{3^m},\quad
\frac{2^m-1}{3^m},\quad
3^{-m},
\]
while all remaining time probabilities tend to zero. More strongly, for every \(n\ge1\),
\[
1-\Pr(T=2)
=\bigl(2-(2/3)^n\bigr)(2/3)^m
-\bigl(1-(2/3)^n\bigr)3^{-m}.
\]
Hence \(\Pr(T=2)\to1\) uniformly over all choices of \(n\ge1\) as \(m\to\infty\).

## Assumptions and scope
The graph has a labelled clique \(C\) of size \(m\) and a disjoint labelled independent vertex set \(I\) of size \(n\), with **every** edge from \(C\) to \(I\). Each vertex has a state in \(\{0,1,2\}\). At each simultaneous update a state \(0\) becomes \(1\), a state \(1\) becomes \(2\), and a state \(2\) becomes \(0\) unless at least one neighbor is presently in blinking state \(1\), in which case the state \(2\) remains \(2\). The neighbors are open neighbors, and current states—not sequentially updated states—govern the transition. The first synchronization time is the least nonnegative time at which **all** vertices have the same color; after that the configuration rotates uniformly with period three. The value \(T=\infty\) means no such time exists. All counts refer to labelled initial configurations; only the fixed update rule is considered.

## Proof
**Reduction to 49 support classes.** Let \(A,B\subseteq\{0,1,2\}\) be the sets of colors occurring respectively on \(C\) and \(I\). Encode a nonempty color set \(S\) by the integer mask \(M(S)=\sum_{c\in S}2^c\), between \(1\) and \(7\). Two vertices initially in the same class and sharing the same initial color always have identical future colors. For clique vertices this remains true even when the shared color is \(2\), because a vertex of color \(2\) is never itself a blinking neighbor. For independent vertices, all neighbor sets coincide. Thus for each nonempty support pair \((M(A),M(B))\), tracking one vertex for each occupied color in each class is **exact**, not an approximation.

If a clique vertex is at color \(2\), it is inhibited exactly when at least one clique or independent vertex is at color \(1\). If an independent vertex is at color \(2\), it is inhibited exactly when at least one clique vertex is at color \(1\). These two Boolean conditions and the ordinary increments of colors \(0\) and \(1\) determine the entire trajectory of each representative. Applying the explicit three-state transition for at most six updates gives the following *complete 49-case table*. Row numbers are clique support masks; column numbers are independent-set support masks. An entry \(t\) is the first synchronization time and \(*\) means no synchronization.

| \(M(A)\backslash M(B)\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 2 | 2 | 3 | 6 | 6 | 6 |
| 2 | 2 | 0 | 5 | 1 | 5 | 1 | 5 |
| 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 4 | 3 | 1 | 5 | 0 | 3 | 4 | * |
| 5 | 3 | 2 | 2 | 3 | 3 | 6 | 6 |
| 6 | 2 | 1 | 5 | 1 | 5 | 1 | 5 |
| 7 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

The table follows by finite exact substitution, reproducible independently by the two packaged verification programs. Because every non-starred entry reaches the uniform invariant three-cycle at its indicated time, and the sole starred entry \((4,7)\) is itself periodic with primitive period three, this table proves the universal classification, not just finite graph experiments. Indeed \((4,7)\) means the clique is entirely color \(2\) and the independent class uses all three colors; the latter rotates through all three colors, so it continually inhibits the clique in state \(2\). Consequently all non-synchronizing configurations are periodic from the outset, and the only possible primitive periods are three. There are \(V\) labelled non-synchronizing periodic configurations, giving \(V/3\) nonsynchronous primitive orbits plus one uniform primitive orbit.

**Counting the initial conditions.** For a fixed nonempty mask whose size is respectively one, two, or three, the number of surjective labelled color assignments on \(k\) specified vertices is \(1\), \(2^k-2\), or \(3^k-3\cdot2^k+3\). Multiply the corresponding clique and independent-set weights at every table entry. For transparency, before simplifying powers, the table yields
\[
\begin{aligned}
N_0&=3,\\
N_1=N_3&=(U+2)(u+1),\\
N_2&=4Uu+3Uv+U+Vu+Vv+5u+3v+2,\\
N_4&=U,\\
N_5&=2Uu+3U+Vu+V,\\
N_6&=Uu+2U+Vu+V,\\
N_\infty&=V.
\end{aligned}
\]
Substituting the definitions of \(u,v,U,V\) produces the formulas in the finding. A direct sum also gives \(3^{m+n}\), partitioning the full initial-state space. Since the count at time six is strictly positive whenever \(n\ge2\) and the count at time three is strictly positive whenever \(n=1\), the asserted transient bounds are sharp.

**Probability limits.** Divide all counts by \(3^{m+n}\). Holding \(m\) fixed and letting \(n\to\infty\) kills all the terms involving \(2^n/3^n\) or constants, yielding exactly the four masses displayed in the finding. Algebraic rearrangement of the expression for \(N_2\) gives the exact error identity for \(1-\Pr(T=2)\). Both terms in that identity tend to zero uniformly in \(n\ge1\) as \(m\to\infty\). This uses no unproved mixing or independence assumption beyond the uniform product sampling specified in the theorem.

## Verification
The standalone script `verify_support.py` independently generates the time labels for all \(49\) nonempty pairs of support masks from the vertex-level update rule, checks the full table and all formal coefficient identities, and checks their numeric instances for clique and independent-set sizes through six. It returns `MASK_CERTIFICATE_OK`. This computation is a finite complete certificate of the universal theorem because the color-support reduction is proved above.

The separate C++ program `verify_direct.cpp` enumerates all actual labelled colorings of the complete split graphs for \(39\) pairs of sizes with total order at most eleven, tests first synchronization time against the closed formulas, and checks that each nonsynchronizing configuration starts on a primitive three-cycle with the specified structure. It checks \(923463\) configurations and returns `DIRECT_EXHAUSTIVE_OK`. It corroborates the symbolic proof; it is not an argument by finite extrapolation. Commands: `python3 verify_support.py` and `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`.

## Relationship to prior work
Hanbaek Lyu introduced this finite-state inhibitory pulse-coupled oscillator rule and established general synchronization results on paths and trees, including the local-global degree criterion (arXiv:1407.1103; publicly available July 4, 2014). Lyu's subsequent analysis of the same rule on trees (arXiv:1610.00837; first public October 4, 2016) focuses on critical tree synchronization and time bounds, not the complete split graph's exact first-entry distribution. The known special case with a one-vertex clique is the ordinary star, whose exact first-synchronization census is recovered when \(m=1\). Complete bipartite oscillator networks have a different adjacency pattern: internal clique edges in the present graph change the inhibition conditions and the time-two mass.

The current classification contributes the universal \(49\)-support table, all-size exact hitting-time counts, a sharp deterministic bound, and uniform concentration into two-step synchronization for a growing clique. These claims do not follow from the published tree criterion, from the star census alone, or from the complete bipartite census without a separate argument. Searches for direct complete-split equivalents and broader dynamical enumerations did not identify a dominating published theorem; a negative search is not proof of mathematical priority.

## Limitations
This is the exact **three-color** parallel inhibitory rule, not a result for arbitrary numbers of colors or heterogeneous update schedules. Only the complete join of a clique and an independent set is covered, not arbitrary split graphs. The counting formulas concern the first global synchronization time and the total asynchronous recurrent set, not individual synchronous phase-entry orientations or the detailed sizes of each asynchronous orbit basin under a different rule. The scientific originality judgment is based on the literature and record comparisons described separately; unindexed historical equivalents remain possible. The computational verifier provides complete finite support-class evidence and independent small-size corroboration, not independent external certification.

## References
1. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, first public July 4, 2014, arXiv:1407.1103, https://arxiv.org/abs/1407.1103.
2. H. Lyu, *Time complexity of synchronization of discrete pulse-coupled oscillators on trees*, first public October 4, 2016, arXiv:1610.00837, https://arxiv.org/abs/1610.00837.
3. A. Vogell, U. Schilcher and C. Bettstetter, *Deadlocks in the synchronization of pulse-coupled oscillators on star graphs*, Physical Review E 102 (2020), 062211, DOI:10.1103/PhysRevE.102.062211. This last work uses a distinct continuous-phase oscillator model and is contextual rather than a source of the present finite-state enumeration.
