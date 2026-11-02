# A modulo-three scheduling law for sequential parity dynamics on complete bipartite graphs

## Finding

For integers \(a,b\ge1\), let \(K_{a,b}\) have labelled shores \(A,B\) of sizes \(a,b\). Each site carries a bit. During one macro-update, visit each vertex **exactly once**, in a fixed permutation \(\pi\), and replace the visited bit by itself plus the current parity of its neighbors over \(\mathbb F_2\). Repeat the same schedule each macro-update; denote its permutation of the \(2^{a+b}\) states by \(T_\pi\).

**Exact period law.** Let \(N=a+b\). Every state is periodic immediately, and \(T_\pi^4=I\) or \(T_\pi^3=I\) according to the cases below. In every case the number of fixed states is \(2^{N-2}\).

* If \(N\) is odd, the numbers of states with least periods \(1,2,4\) are respectively \(2^{N-2},\ 2^{N-2},\ 2^{N-1}\). No other periods occur, regardless of the schedule.
* If \(N=2m\) is even, write \(r\) for the number of vertices of shore \(B\) visited at odd-numbered positions \(1,3,\ldots,2m-1\). If \(b-2r\equiv0\pmod 3\), the only least periods are \(1,2\), with state counts \(2^{N-2},\ 3\cdot2^{N-2}\). Otherwise the only least periods are \(1,3\), with counts \(2^{N-2},\ 3\cdot2^{N-2}\).

Dividing each count of configurations of least period \(d\) by \(d\) gives the exact number of distinct primitive \(d\)-cycles. In particular, the odd-\(N\) primitive orbit counts are \(2^{N-2}\) fixed orbits, \(2^{N-3}\) two-cycles, and \(2^{N-3}\) four-cycles. In the even-\(N\) period-two regime there are \(3\cdot2^{N-3}\) two-cycles; in the other regime there are \(2^{N-2}\) three-cycles.

**Exact schedule law.** Among all \(N!\) permutations of labelled vertices, the number producing the even-\(N\) period-two regime is

\[
E_{a,b}=a!b!\!\!\sum_{\substack{0\le r\le m\\0\le b-r\le m\\b-2r\equiv0\pmod3}}\binom mr\binom m{b-r},\qquad N=2m.
\]

All remaining \(N!-E_{a,b}\) schedules have primitive three-cycles, while for odd \(N\) all \(N!\) schedules have primitive four-cycles. If both shores contain at least two vertices and \(N\) is even, both even-\(N\) regimes occur. On \(K_{2,2}\), the split of its 24 schedules is 16 versus 8; on \(K_{3,3}\) it is 72 versus 648.

## Assumptions and scope

The graphs are undirected, simple, loopless and labelled, with both shores nonempty. A macro-update uses the *current*, possibly already changed, neighbor states; this is a sequential rather than simultaneous process. The order is any fixed permutation visiting every vertex once per macro-update and repeated at subsequent macro-updates. Bits are elements of \(\mathbb F_2\). The theorem does not cover schedules with repeated vertices, randomized schedules, or updates involving thresholds other than parity addition.

For a state \(x\), let \(q_A(x)=\sum_{v\in A}x_v\) and \(q_B(x)=\sum_{v\in B}x_v\), over \(\mathbb F_2\), and write \(Q(x)=(q_A(x),q_B(x))\).

## Proof

**1. Exact two-dimensional quotient and invariant kernel.** An individual site update is the invertible involution

\[
U_v(x)=x+\left(\sum_{u\sim v}x_u\right)e_v.
\]

Each vertex contributes to a single macro-update exactly once, so \(T_\pi\), a product of involutions, is bijective. Updating a vertex of shore \(A\) sends \((q_A,q_B)\) to \((q_A+q_B,q_B)\); updating a vertex of \(B\) sends it to \((q_A,q_B+q_A)\). Thus \(Q(T_\pi x)=P_\pi Q(x)\), where \(P_\pi\) is the ordered product of the two matrices

\[
S_A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
S_B=\begin{pmatrix}1&0\\1&1\end{pmatrix}
\]

over \(\mathbb F_2\). The map \(T_\pi\) fixes \(\ker Q\) pointwise because both shore parities initially vanish. Conversely, if the final configuration equals the initial configuration, then no vertex could have flipped, since each vertex was visited only once. Because both shores are nonempty, this forces both original shore parities to vanish. Therefore

\[
\operatorname{Fix}(T_\pi)=\ker Q,\qquad |\operatorname{Fix}(T_\pi)|=2^{N-2}.
\]

As \(T_\pi-I\) vanishes on \(\ker Q\), there is a unique linear map \(H_\pi:\mathbb F_2^2\to\mathbb F_2^N\) with

\[
T_\pi x=x+H_\pi Q(x).
\]

The fixed-point characterization shows \(H_\pi\) is injective. Iterating and using the quotient relation gives, for every integer \(k\ge1\),

\[
T_\pi^k x=x+H_\pi\left(\sum_{j=0}^{k-1}P_\pi^j\right)Q(x).
\]

**2. The three possible quotient orders.** The matrices \(S_A,S_B\) are distinct involutions and their product has order three. They generate \(\mathrm{GL}_2(\mathbb F_2)\cong S_3\). Thus any \(P_\pi\) has order one, two or three. If \(P_\pi=I\), the iterate formula gives \(T_\pi^2=I\). If its order is three, the identity \(I+P_\pi+P_\pi^2=0\) gives \(T_\pi^3=I\). Otherwise its order is two, \(I+P_\pi\) has rank one and \((I+P_\pi)^2=0\); the iterate formula then gives \(T_\pi^4=I\), and injectivity of \(H_\pi\) gives

\[
|\operatorname{Fix}(T_\pi^2)|=2^{N-1}.
\]

Combining these with \(|\operatorname{Fix}(T_\pi)|=2^{N-2}\) and the total \(2^N\) states yields precisely the three period censuses stated above. There are no transient states because \(T_\pi\) is invertible.

**3. Schedule parity and the mod-three criterion.** Associate to a letter \(A\) the reflection of the real line \(u\mapsto-u\), and to \(B\) the reflection \(u\mapsto2-u\). These generate an infinite dihedral group whose quotient by translation through six units is \(S_3\); under this quotient, the reflections map to \(S_A,S_B\) (up to simultaneous conjugation). Therefore the product of \(N\) letters is a transposition whenever \(N\) is odd. If \(N=2m\) is even, composing the reflections in the schedule's order produces a translation by \(2(b-2r)\) units, up to sign, where \(r\) counts shore-\(B\) visits at odd positions. Its image in \(S_3\) is the identity exactly when \(b-2r\) is divisible by three; otherwise it has order three. This proves the period-selection rule.

**4. Counting labelled schedules.** If \(N=2m\), fixing \(r\) gives \(\binom mr\binom m{b-r}\) binary shore-words: choose \(r\) positions for \(B\) among the \(m\) odd positions and \(b-r\) among the \(m\) even ones. Each such word corresponds to \(a!b!\) labelled vertex orders. Restricting to \(b-2r\equiv0\pmod3\) proves the exact formula for \(E_{a,b}\). If \(a,b\ge2\), the allowed integers \(r\) contain at least three consecutive values, so at least one choice satisfies the divisibility condition and at least one does not. This proves both regimes occur in all such even-size graphs.

## Verification

The standalone script `verification/verify_async_bipartite.py` independently updates individual vertex bits, checks bijectivity and follows the entire labelled-state orbit for all simple vertex orders on ten test graph shapes, including all orders through seven vertices. It checked 12,416 distinct labelled scan orders and 1,433,144 state-order pairs, matching both the period tables and the exact schedule counts. The separate script `verification/verify_async_bipartite_quotient.py` enumerated 32,738 mixed binary shore-words of total length two through fourteen and independently checked the matrix-order/mod-three criterion. Both scripts and actual successful output are included.

These finite checks do not replace the proof for unbounded shore sizes and schedules.

## Relationship to prior work

Macauley, McCammond and Mortveit introduced update-order independence and dynamics groups for sequential dynamical systems; their detailed classifications concern asynchronous elementary rules on cycle graphs, not the complete-bipartite parity-local rule studied here. Work on lit-only sigma games and dual symplectic transvection groups classifies reachability under *arbitrary products* of generators, which is different from the exact primitive cycles of one periodically repeated, single-visit scan order. The distinction matters: even for \(K_{2,2}\), two choices of scanning order produce respectively only fixed points and two-cycles, or fixed points and three-cycles.

Previously recorded synchronous parity automata on complete multipartite graphs use simultaneous updates and do not determine this sequential schedule dependence; synchronous and sequential maps are different. The exact mod-three schedule selection and labelled schedule counts were not located in the sources and record summaries searched. This is a limited originality assessment, not proof of absolute novelty.

## Limitations

The theorem is for characteristic two, complete bipartite graphs, and fixed simple scan orders only. It does not assert a full classification of arbitrary fair words, irregular bipartite graphs or randomized scan protocols. Historical mathematical results may express the same finite-dimensional reduction under another name, and a closest published record on synchronous parity was accessible only through its summary. No independent expert review or independent audit has been performed.

## References

1. M. Macauley, J. McCammond, H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360 (first posted 2007-07-16), https://arxiv.org/abs/0707.2360.
2. M. Macauley, J. McCammond, H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238 (first posted 2008-08-08), https://arxiv.org/abs/0808.1238; Journal of Algebraic Combinatorics 33 (2011), 11–35, doi:10.1007/s10801-010-0231-y.
3. H.-w. Huang, *Lit-only sigma-game on nondegenerate graphs*, Journal of Algebraic Combinatorics 41 (2015), 385–395, doi:10.1007/s10801-014-0540-7; first posted arXiv:1209.1233 in 2012.
4. J. Sjöstrand, *Orbits under Dual Symplectic Transvections*, arXiv:2312.03933 (first posted 2023-12-06), https://arxiv.org/abs/2312.03933.
