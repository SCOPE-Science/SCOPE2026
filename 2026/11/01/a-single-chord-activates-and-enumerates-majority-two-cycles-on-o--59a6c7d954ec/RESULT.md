# A single chord activates and enumerates majority two-cycles on odd rings

## Finding

Let \(G_{n,d}\) be the graph on the labelled vertex set \(\{0,1,\ldots,n-1\}\) consisting of the simple cycle \(C_n\) and the additional chord \(\{0,d\}\), where \(n\ge4\) and \(2\le d\le n-2\). Put \(m=n-d\); the two paths joining the chord endpoints through cycle edges have lengths \(d\) and \(m\).

Each vertex synchronously adopts the strict majority bit among its neighbors; in a tie it retains its current bit. Denote this map by \(F\). A primitive temporal two-cycle is an unordered pair \(\{x,F(x)\}\) of distinct configurations satisfying \(F^2(x)=x\). Labels are fixed; graph automorphisms and global bit complementation do **not** identify orbits.

For every integer \(\ell\ge2\), define \(U_2=1\) and \(V_2=0\). For \(\ell\ge3\), define
\[
U_\ell=\sum_{\substack{k\ge1,\ k\text{ odd}\\2k\le\ell-1}}\binom{\ell-k-2}{k-1},\qquad
V_\ell=\sum_{\substack{k\ge2,\ k\text{ even}\\2k\le\ell-1}}\binom{\ell-k-2}{k-1}.
\]
An empty sum is zero. The exact number of primitive temporal two-cycle orbits is
\[
\boxed{N_{n,d}=2(U_dU_m+V_dV_m)+2\left(\mathbf1_{d\text{ odd}}(U_m+V_m)+\mathbf1_{m\text{ odd}}(U_d+V_d)\right)+\mathbf1_{n\text{ even}}.}
\]
The three summands count disjoint dynamical mechanisms: only the two chord endpoints flip; exactly one entire cycle-edge path flips; and all vertices flip.

The formula admits a particularly short Fibonacci form. Let \(F_0=0\), \(F_1=1\), and \(F_{r+2}=F_{r+1}+F_r\). Define \(f_2=1\), \(f_\ell=F_{\ell-2}\) for \(\ell\ge3\), \(q_2=1\), and for \(\ell\ge3\)
\[
q_\ell=\begin{cases}
-1,&\ell\equiv0,1\pmod6,\\
0,&\ell\equiv2,5\pmod6,\\
1,&\ell\equiv3,4\pmod6.
\end{cases}
\]
Then
\[
\boxed{N_{n,d}=f_df_m+q_dq_m+2\left(\mathbf1_{d\text{ odd}}f_m+\mathbf1_{m\text{ odd}}f_d\right)+\mathbf1_{n\text{ even}}.}
\]
In particular, \(N_{n,d}\ge4\) for every odd \(n\), although the unchorded odd cycle has no primitive two-cycle. This single-edge creation of oscillations is exact at every chord separation, not merely asymptotic.

## Assumptions and scope

All graphs are finite, simple and undirected. The chord is required to connect nonconsecutive cycle vertices, so both cycle-edge paths have lengths at least two. The rule uses simultaneous updates and strict neighbor-majority with inertia at even-degree ties. Only primitive temporal two-cycle **orbits** are counted, rather than individual phases, and no spatial symmetry quotient is imposed. No assertion about the length or size of transient attraction basins is made.

## Proof

**1. Flipping at degree two propagates.** For a two-cycle \(x\leftrightarrow y\), call a vertex *flipping* if its two phase bits differ. At a degree-two vertex, changing its bit requires both neighbors to hold the opposite bit at the first phase. Changing back requires both neighbors to hold the reverse bit at the second phase. Thus both neighbors must also flip, and the bits across each edge incident to that vertex alternate spatially. Consequently, the flipping vertices in the interior of either cycle-edge path form either the entire interior or the empty set. No primitive orbit can flip only one chord endpoint: all three of its neighbors would then be constant through time and hence its strict majority would also be constant. If an interior vertex flips, both chord endpoints flip by propagation. If no interior vertex flips, both chord endpoints must flip. There are therefore only the three mechanisms in the finding.

**2. A stable path bounded by flipping endpoints.** Suppose the two endpoints have opposite first-phase bits and both flip. If their connecting cycle-edge path of length \(\ell\) has a stable interior, then for \(\ell=2\) the unique interior vertex sees opposite neighboring bits in both phases, and either stable bit is allowed. If \(\ell\ge3\), at the first interior vertex one neighbor flips, so stability across both phases forces its other, stable neighbor to have the same bit. The symmetric condition holds at the last interior vertex; at every other stable interior vertex, an isolated singleton run would force a flip. Hence a stable interior word of length \(\ell-1\) is valid precisely when all constant runs have length at least two. For fixed first and last bits, the number of words with matching endpoints is \(U_\ell\), and the number with different endpoints is \(V_\ell\). Indeed, a word with \(k\) runs of lengths at least two corresponds to a composition of \(\ell-1\) into \(k\) parts each at least two; the number is \(\binom{\ell-k-2}{k-1}\). Odd \(k\) produces equal word-end bits, even \(k\) unequal bits. The special \(\ell=2\) convention gives the same endpoint statistics.

**3. Only the chord endpoints flip.** If only vertices \(0,d\) flip, each has one flipping neighbor (across the chord) and two stable neighbors (one on each cycle-edge path). For its three-neighbor majority to reverse at each phase, the stable neighbors must be opposite and the chord partner must be opposite in the first phase; these conditions are also sufficient. Choose the phase bit at vertex \(0\) in two ways; the bit at \(d\) is forced opposite. For each pair of the first and last interior bits on the \(d\)-path, the corresponding bits on the \(m\)-path must be their complements. Bit complementation preserves \(U,V\). The number of pairs of stable interiors is \(2(U_dU_m+V_dV_m)\). Accounting for the two choices at vertex \(0\), then dividing the configuration count by two for the two phases of each primitive orbit, gives exactly \(2(U_dU_m+V_dV_m)\) orbits.

**4. Exactly one path flips.** If all vertices of the \(d\)-path flip, propagation forces an alternating spatial bit pattern along it. The two chord endpoints therefore have opposite phase bits exactly when \(d\) is odd. They **must** be opposite: if they were equal, at a chord endpoint its active-path neighbor and its chord partner would have opposite bits in each phase, so the single stable neighbor on the other path would need to have two opposite values at once to make the endpoint flip in both directions. Conversely, when \(d\) is odd, the active-path neighbor and chord partner together both support the flip, and the inactive \(m\)-path can have any valid stable interior as characterized in Step 2. There are \(2(U_m+V_m)\) choices for its interior bits and two choices for the active alternating phase, giving \(2(U_m+V_m)\) primitive orbits. Interchanging the paths gives \(2(U_d+V_d)\) orbits when \(m\) is odd. The cases are disjoint.

**5. Both paths flip.** All cycle vertices flip, and the degree-two propagation condition forces the entire cycle to alternate in space. This is possible exactly when \(n\) is even. Its two alternating configurations constitute one primitive temporal orbit. Each chord endpoint already sees both cycle neighbors opposite to itself, so the extra chord cannot obstruct its flip. Summing the mutually exclusive counts in Steps 3–5 proves the first boxed formula.

**6. Fibonacci simplification.** The generating functions for the fixed-endpoint word counts, valid for lengths \(\ell\ge3\), are
\[
\sum_{\ell\ge3}(U_\ell+V_\ell)z^{\ell-1}=\frac{z^2}{1-z-z^2},\qquad
\sum_{\ell\ge3}(U_\ell-V_\ell)z^{\ell-1}=\frac{z^2}{1-z+z^2}.
\]
The first has Fibonacci coefficients; the second has coefficient sequence \(1,1,0,-1,-1,0\) repeated. With the separate length-two convention this gives \(U_\ell=(f_\ell+q_\ell)/2\), \(V_\ell=(f_\ell-q_\ell)/2\) and hence the second boxed formula. The rational functions arise by summing any positive number of runs of length at least two: their length generating function is \(z^2/(1-z)\), with an alternating sign for the second identity.

**7. The odd-ring discontinuity.** On a bare cycle, if one degree-two vertex flips, propagation forces every vertex to flip and forces spatial alternation, which is impossible for odd cycle length. Thus a bare odd cycle has no primitive two-cycle. For a chorded odd cycle, choosing both path interiors to be constant and opposite produces two distinct endpoint-only two-cycles (choose which path has each bit); exactly one of the two cycle-edge path lengths is odd, and making that path alternate while choosing either constant bit on the other path produces at least two additional one-path-flipping two-cycles. These four orbits are distinct. This proves \(N_{n,d}\ge4\) without relying on the counting formula.

## Verification

The standalone program `verify_chord_majority.py` uses direct synchronous bit updates and exhaustive integer-state enumeration independently of the composition formula. It checked every \(n\) from \(4\) to \(14\) and every legal labelled chord length \(2\le d\le n-2\), comprising \(66\) parameter pairs and \(327{,}696\) examined configurations. For each pair it independently classified every primitive two-cycle by its actual flipping mask and compared all three class populations to the formula. It also directly enumerated short path interiors to verify the binomial endpoint counts. All comparisons passed. Reproduce with `python verify_chord_majority.py` using the Python standard library. The infinite-parameter statement rests on Steps 1–7, not on this finite enumeration.

Representative primitive-orbit counts: \(N_{5,2}=4\), \(N_{6,3}=7\), \(N_{9,3}=8\), \(N_{13,5}=32\), \(N_{14,7}=47\).

## Relationship to prior work

Goles and Olivos [1] established eventual period at most two for synchronous symmetric threshold dynamics. That theorem establishes the allowed eventual periods, but it does not supply the chord-specific partition or exact cycle counts here. Benjamini, Chan, O'Donnell, Tamuz and Tan [2] reproduce the finite period-two property and study majority behavior on infinite unimodular and random graphs; their relevant theorems concern eventual behavior, not an exact enumeration for a single chord. Nakar and Ron [3] study cyclic one-dimensional majority cellular automata without chords and characterize spatial structures of periodic configurations. The present theorem specifically concerns the perturbation in which exactly two cycle vertices gain a third neighbor. Adding the chord changes the local rule at those vertices and, for odd ring length, creates periodic orbits that do not exist on the unchorded ring. These structural distinctions do not by themselves prove historical priority.

## Limitations

This result counts labelled temporal two-cycle orbits and their three flipping classes only; it does not enumerate fixed points, attraction basins, or transient entry times, and does not address cycles with two or more chords. The 1980 original source was not available for a complete full-text comparison; its known principal theorem is broader in period boundedness but not known to give this specialized census. No claim of independent audit or comprehensive priority proof is made. Computed examples cannot establish the infinite formula without the combinatorial proof above.

## References

[1] E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.

[2] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1 (first posted 2014-05-11), subsequently *Stochastic Processes and their Applications* **126** (2016), 2719–2733.

[3] Y. Nakar and D. Ron, “The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity,” arXiv:2205.08972v1 (first posted 2022-05-18).