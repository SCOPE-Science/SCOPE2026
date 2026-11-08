# A modulo-six twist resonance in synchronous majority dynamics on cubic cyclic ladders

## Finding

For each integer \(n\ge3\) and twist \(\theta\in\{0,1\}\), let \(T_n^{(\theta)}\) have vertices \((i,\ell)\), where \(0\le i<n\) and \(\ell\in\{0,1\}\). Connect both vertices of each rung, consecutive vertices of each layer for \(0\le i<n-1\), and connect \((n-1,\ell)\) to \((0,\ell\oplus\theta)\). The untwisted graph \(T_n^{(0)}\) is the prism \(C_n\square K_2\); the twisted graph \(T_n^{(1)}\) is the Möbius ladder on \(2n\) vertices. Both are simple cubic graphs in this range.

Let \(M_{n,\theta}\) synchronously update binary vertex opinions by the strict majority among the three neighbors. Write \(F_{n,\theta}=|\operatorname{Fix}(M_{n,\theta})|\), \(P_{n,\theta}=|\operatorname{Fix}(M_{n,\theta}^2)|\), and \(Q_{n,\theta}\) for the number of configurations whose next image is their bitwise complement. Define Lucas numbers \(L_0=2\), \(L_1=1\), \(L_{m+2}=L_{m+1}+L_m\), and the integer-valued residue functions
\[
\epsilon_m=2\cos(m\pi/3),\qquad \delta_m=2\cos(2m\pi/3).
\]

**Complete periodic census.** For every \(n\ge3\),
\[
\begin{aligned}
 F_{n,0}&=L_n+\epsilon_n+2,&F_{n,1}&=L_n+\epsilon_n,\\
 Q_{n,0}&=L_n+\delta_n+2\mathbf1_{2\mid n},&Q_{n,1}&=L_n-\delta_n+2\mathbf1_{2\mid n},
\end{aligned}
\]
\[
P_{n,0}=\begin{cases}(L_n+\epsilon_n+2)^2,&2\mid n,\\L_{2n}+\epsilon_{2n}+2,&2\nmid n,\end{cases}\qquad
P_{n,1}=\begin{cases}L_{2n}+\epsilon_{2n}+2,&2\mid n,\\ (L_n+\epsilon_n)^2,&2\nmid n.\end{cases}
\]
Every initial state ultimately reaches a fixed point or a primitive two-cycle. The exact number of primitive two-cycle *orbits* is \((P_{n,\theta}-F_{n,\theta})/2\); exactly \(Q_{n,\theta}/2\) of these orbits flip all \(2n\) vertices on every update.

**Sharp twist-sign resonance.** The difference in immediately periodic populations (twisted minus untwisted) is
\[
P_{n,1}-P_{n,0}=
\begin{cases}
-8L_n-14,&n\equiv0\pmod6,\\
2L_n-2,&n\equiv1,5\pmod6,\\
-2L_n-2,&n\equiv2,4\pmod6,\\
-4L_n-2,&n\equiv3\pmod6.
\end{cases}
\]
Thus twisting the seam **increases** the immediately periodic population if and only if \(\gcd(n,6)=1\), and decreases it in every other residue class. The change is exponentially large in absolute size but lower-order relative to the common leading population: with \(\varphi=(1+\sqrt5)/2\),
\[
P_{n,\theta}\sim\varphi^{2n},\qquad
\frac{P_{n,\theta}}{4^n}\sim(\varphi^2/4)^n,
\qquad \frac{Q_{n,\theta}}{P_{n,\theta}-F_{n,\theta}}\sim\varphi^{-n}.
\]
The fully flipping populations differ by the bounded arithmetic quantity \(Q_{n,1}-Q_{n,0}=-2\delta_n\). The equality \(Q_{n,\theta}=F_{n,\theta}\) holds whenever the graph is bipartite: even \(n\) for the prism and odd \(n\) for the Möbius ladder.

## Assumptions and scope

Each cyclic ladder has \(2n\) **labelled** vertices and exactly \(4^n\) binary configurations. The twist is a single fixed seam permutation, not a periodic alternation of local update rules. At every vertex the open-neighborhood degree is three; no ties occur and no inertia convention is needed. The temporal counts are for configurations, not for quotient classes under graph automorphisms. A state is immediately periodic exactly when it belongs to \(\operatorname{Fix}(M^2)\), using the proved period-at-most-two property. The statement does **not** enumerate the transient-entry-time distribution or the sizes of eventual basins.

The residue values are \((\epsilon_0,\ldots,\epsilon_5)=(2,1,-1,-2,-1,1)\) and \((\delta_0,\delta_1,\delta_2)=(2,-1,-1)\). The defining graph is simple for every integer \(n\ge3\), including the six-vertex Möbius ladder \(K_{3,3}\).

## Proof

**1. Eventual periods.** Encode binary values as spins \(s_t(v)\in\{-1,1\}\). Since every vertex has three neighbors, \(s_{t+1}(v)\) is the sign of the nonzero field \(h_t(v)=\sum_{u\sim v}s_t(u)\). Set \(\Phi_t=\sum_v s_{t+1}(v)h_t(v)\). Because the adjacency relation is symmetric,
\[
\Phi_t=\sum_v s_t(v)h_{t+1}(v),\qquad
\Phi_{t+1}-\Phi_t=\sum_v(s_{t+2}(v)-s_t(v))h_{t+1}(v)\ge0.
\]
Each nonzero summand is strictly positive, because \(s_{t+2}(v)\) is the unique maximizing sign against \(h_{t+1}(v)\). The integer potential is bounded above by \(3|V|\), so it eventually stops increasing; thereafter \(s_{t+2}=s_t\). This proves the period bound without assuming the older threshold-network theorem.

**2. Fixed points.** Let the two bits of rung \(i\) be \((a_i,b_i)\). If \(a_i\ne b_i\) in a fixed configuration, the opposite rung endpoint votes against each bit, so **both horizontal neighbors** of \((i,0)\) must agree with \(a_i\), and both horizontal neighbors of \((i,1)\) must agree with \(b_i\). Disagreement therefore propagates along every rung. With an untwisted seam the only possibilities are the two oppositely monochromatic layers. With a twisted seam, that propagation would require a bit to equal its complement, which is impossible. Otherwise every rung agrees, say \(a_i=b_i=c_i\), and the vertex rule is fixed exactly when the circular word \(c_0\ldots c_{n-1}\) contains neither \(010\) nor \(101\) as a cyclic length-three subword. Both seam conventions give the same condition for agreeing rungs.

To count these words, index two-bit states in the order \(00,01,10,11\). The allowed overlap-transfer matrix is
\[
G=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix},\qquad
\det(zI-G)=(z^2-z-1)(z^2-z+1).
\]
For \(n\ge3\), the number of admissible cyclic words is \(\operatorname{tr}(G^n)=L_n+\epsilon_n\). This **cyclic-word enumeration itself was previously obtained by Agur, Fraenkel and Klein (1988)** for their self-inclusive majority rule on a single cycle; the transfer computation here records a proof adapted to the coupled-ladder setting, not a claim of priority for this sequence. Adding the two untwisted disagreement configurations proves both fixed-point formulas.

**3. Two-periodic states via the canonical bipartite double cover.** For any graph \(H\) whose update depends only on its neighbors, form its canonical bipartite double cover \(B(H)\) with vertices \((v,t)\), \(t\in\{0,1\}\), and edges \((u,t)\sim(v,1-t)\) whenever \(u\sim v\) in \(H\). A pair of configurations \((x,y)\) with \(M(x)=y\) and \(M(y)=x\) corresponds bijectively to a fixed configuration on \(B(H)\), by labeling \((v,0)\) with \(x(v)\) and \((v,1)\) with \(y(v)\). Thus the number of configurations fixed by \(M^2\) equals the fixed-state count on \(B(H)\).

Realize \(T_n^{(\theta)}\) as the quotient of the infinite ladder with vertices \((i,\ell)\), \(i\in\mathbb Z\), by the shift-and-twist deck map \((i,\ell)\mapsto(i+n,\ell\oplus\theta)\). The infinite ladder is bipartite with checkerboard class \(i+\ell\pmod2\). The deck map preserves this class iff \(n+\theta\) is even. In that case the quotient is bipartite, and its canonical double cover is two disjoint copies of \(T_n^{(\theta)}\), yielding \(P_{n,\theta}=F_{n,\theta}^2\). If \(n+\theta\) is odd, the double cover corresponds to the subgroup generated by the square of the deck map, \((i,\ell)\mapsto(i+2n,\ell)\), and hence is \(T_{2n}^{(0)}\), yielding \(P_{n,\theta}=F_{2n,0}\). These are precisely the four formulas for \(P\).

**4. All-vertex flipping cycles.** The majority map commutes with bitwise complementation. Therefore a configuration satisfying \(M(x)=\bar x\) lies in a genuine two-cycle. If any rung of such a configuration agrees, both horizontal neighbors must have the opposite bit on both layers; propagation forces all rungs to agree in an alternating circular pattern. Exactly two such configurations exist for even \(n\), and none for odd \(n\). Otherwise all rungs disagree; writing the first-layer bits as \(c_i\), every opposite-layer bit is \(1-c_i\). For a complete flip, the first-layer circular sequence must avoid \(000\) and \(111\). With twist zero this is an ordinary periodic word; with twist one it is an **antiperiodic** word, meaning \(c_{i+n}=1-c_i\) when the word is extended to the infinite ladder.

For the same state order, put
\[
H=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
\]
Here \(J\) complements both bits of a transfer state and commutes with \(H\). The two-dimensional \(+1\) eigenspace of \(J\) carries characteristic polynomial \(z^2-z-1\) for \(H\), while its \(-1\) eigenspace carries \(z^2+z+1\). Hence periodic and antiperiodic no-triple counts are, respectively,
\[
\operatorname{tr}(H^n)=L_n+\delta_n,\qquad
\operatorname{tr}(H^nJ)=L_n-\delta_n.
\]
The ordinary periodic no-triple word count \(L_n+\delta_n\) is likewise already due to Agur, Fraenkel and Klein (1988); the twisted antiperiodic word count and its contribution to majority cycles on Möbius ladders are the graph-specific claims here. Adding the two alternating agreeing-rung configurations when \(n\) is even gives both formulas for \(Q\).

**5. Twist difference and asymptotics.** The Lucas identity \(L_n^2=L_{2n}+2(-1)^n\), the relations \(\epsilon_{2n}=\delta_n\) and \(\delta_n=(-1)^n\epsilon_n\), and the periodic residue values give the displayed four-case difference after expansion. Since \(L_n=\varphi^n+(-\varphi)^{-n}\), the fixed and full-flip counts are \(\varphi^n+O(1)\), whereas the two-step fixed count is \(\varphi^{2n}+O(\varphi^n)\), giving the three asymptotic statements. This completes the full theorem.

## Verification

Two standalone C++17 verification programs accompany this result. Run `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive` followed by `./verify_exhaustive`; it evolves **every** one of the \(4^n\) labelled configurations independently for each twist and \(3\le n\le12\), comparing all three counts to the formulas. Run `g++ -O3 -std=c++17 verify_transfer.cpp -o verify_transfer` followed by `./verify_transfer`; it **does not evolve configurations**, instead enumerating local space-time-compatible words through two separate exact finite overlap transfers, and checks fixed, full-flip and two-step fixed counts for both twists and \(3\le n\le22\). This second transfer represents all \(16\) possible one-rung, two-time labels and counts closed walks with a possible layer-swap seam. The programs print `PASS` on success; their captured outputs are included.

These checks are finite corroboration of the preceding proofs, not infinite certificates. At \(n=3\), the prism has \((F,P,Q)=(4,22,6)\) and the Möbius ladder has \((2,4,2)\); at \(n=6\) the corresponding triples are \((22,484,22)\) and \((20,326,18)\).

## Relationship to prior work

The finite symmetric-threshold period-at-most-two principle is due to Goles and Olivos (1980); it is used as historical context but is also reproved here for the cubic case. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486, first submitted 2014-05-11) prove stochastic and infinite-network stabilization results and explicitly state the classical finite-graph period theorem. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519, first submitted 2015-08-14) study voting-time bounds and general bipartite-dependent state reconstruction. Neither inspected paper supplies the present labelled fixed-state, periodic-state or full-flip enumerations for prisms and Möbius ladders, or the modulo-six sign reversal of their difference.

Agur, Fraenkel and Klein, *The number of fixed points of the majority rule* (1988), explicitly derive **both** \(L_n+\epsilon_n\) for cyclic words without singleton runs and \(L_n+\delta_n\) for cyclic words without triples. The present work does **not** claim either enumeration as new. Their dynamics uses the vertex together with its two cyclic neighbors (self-inclusive local majority), not synchronous open-neighborhood majority on either of the two cubic ladder graphs. Their formulas do not imply the prism/Möbius double-cover classification, the antiperiodic twisted closure, or the mod-six sign-resonance for the temporal-periodic population. The canonical bipartite double cover is also a standard graph construction, used rather than claimed as new. The earlier finite classification for majority dynamics on sunlet graphs concerns a different (nonregular) graph family and does not imply the Möbius-versus-prism difference; analogous Lucas terms and the leading exponential rarity of fully flipping oscillations are not claimed as new by themselves. Earlier work on parity (linear XOR) dynamics on cubic circular ladders studies a distinct update law, not strict majority.

## Limitations

No exact transient-entry-time distribution or attraction-basin census is claimed. The common leading term in the two periodic-state populations does not imply their difference is bounded: the difference is of order \(\varphi^n\), with the stated residue-dependent sign. The known bipartite-double-cover identity and standard Lucas sequence identities have independent prior provenance. Literature searches, publicly indexed research summaries and materially inspected primary full texts did not locate a direct covering theorem for cubic twisted/untwisted ladder majority populations; an unindexed equivalent calculation remains possible. The full original 1980 Goles–Olivos paper was not available for textual comparison, although its period theorem and citation were independently confirmed from later primary sources. The full Agur–Fraenkel–Klein 1988 article *was* inspected, and its classical cyclic-word counts have been credited as known. The first-public-date field uses the earliest day-specific *verified* source among the inspected preprints (2014-05-11); the earlier 1980 article has year-only public metadata here, so no day is invented.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1 (public 2014-05-11), https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519v1 (public 2015-08-14), https://arxiv.org/html/1508.03519v1.
4. Z. Agur, A. S. Fraenkel and S. T. Klein, “The number of fixed points of the majority rule,” *Discrete Mathematics* 70 (1988), 295–302, DOI: 10.1016/0012-365X(88)90005-2. Full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf. The no-singletons and no-triples cyclic-word formulas are established there.
