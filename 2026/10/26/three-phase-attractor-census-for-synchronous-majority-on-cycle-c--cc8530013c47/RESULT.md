# Three-phase attractor census for synchronous majority on cycle coronas

## Finding

For integers \(n\geq3\) and \(r\geq1\), let \(G_{n,r}=C_n\circ\overline K_r\) consist of a simple cycle of \(n\) core vertices, each joined to \(r\) distinct private leaves. Under synchronous, open-neighbour binary majority, with ties retaining the vertex's current state, every orbit becomes a fixed point or a two-cycle. Put \(H_{n,r}=|\operatorname{Fix}(F_{n,r})|\) and \(P_{n,r}=|\operatorname{Fix}(F_{n,r}^2)|\). The number of primitive two-cycles (unoriented orbits) is \((P_{n,r}-H_{n,r})/2\).

Define \(Q_j\), for \(j\geq3\), as the number of cyclic binary words of length \(j\) in which no position differs from both of its two neighbours. Then
\[
Q_j=\varphi^j+\psi^j+2\cos(j\pi/3),\qquad
\varphi=(1+\sqrt5)/2,\quad\psi=(1-\sqrt5)/2.
\]
The complete attractor census is:

1. **One private leaf per core vertex.** \(H_{n,1}=Q_n\), and
\[
P_{n,1}=\begin{cases}Q_{2n},&n\text{ odd},\\Q_n^2,&n\text{ even}.\end{cases}
\]
2. **Two private leaves per core vertex.** \(H_{n,2}=2^n\), and \(P_{n,2}=\operatorname{tr}(M^n)\), where the explicitly defined integer \(16\times16\) transition matrix \(M\) below has characteristic polynomial
\[
\det(zI-M)=z^8(z^2+2)(z^2+z+1)(z^4-3z^3-z^2+2).
\]
Equivalently, if \(\alpha_1,\ldots,\alpha_4\) are the four complex roots, counted with multiplicity, of \(z^4-3z^3-z^2+2\), then
\[
P_{n,2}=\sum_{j=1}^4\alpha_j^n+2\cos(2\pi n/3)
 +\begin{cases}2(-2)^{n/2},&n\text{ even},\\0,&n\text{ odd}.\end{cases}
\]
3. **Three or more private leaves per core vertex.** \(H_{n,r}=2^n\), \(P_{n,r}=4^n\), and every initial state reaches its eventual one- or two-cycle after at most one synchronous update. That upper bound is sharp among all initial states for each allowed \(n,r\).

The asymptotic bases of \(P_{n,r}\) as \(n\to\infty\) are respectively \(\varphi^2\approx2.618034\), \(\lambda\approx3.2494533945\) (the largest root of the displayed quartic), and \(4\). Thus adding the first, second, then third private leaf produces three distinct recurrent-state growth regimes.

## Assumptions and scope

Each private leaf is adjacent only to its designated core vertex; cycle edges are undirected, with \(n\ge3\) so that the left and right cycle neighbours are distinct. States are \(0,1\). The core vertex takes the strict majority of its \(r+2\) neighbour bits and keeps its old bit on a tie. Each leaf copies the current core bit. Time is synchronous. Configurations are labelled by the original cycle vertices and by the private leaves. \(P\) counts *periodic states*, not the number of two-cycles. No claim is made about exact entry time when \(r=1\) or \(r=2\).

For \(r=2\), let the four-letter alphabet be \(\Sigma=\{(0,0),(0,1),(1,0),(1,1)\}\). A letter \(v=(a,c)\) encodes the core bit \(a\) and the common bit \(c\) of its private leaves in one phase. For \(u=(a_-,c_-)\), \(v=(a,c)\), \(w=(a_+,c_+)\), set
\[
T(u,v,w)=1\iff a=c\quad\text{or}\quad
\bigl((a_-=c\text{ or }a_+=c)\text{ and }(c_-=a\text{ or }c_+=a)\bigr).
\]
Otherwise \(T=0\). Index \(M\) by ordered pairs \((u,v)\in\Sigma^2\) and define \(M_{(u,v),(v',w)}=T(u,v,w)\) when \(v'=v\), and zero otherwise. This fixes all \(16\) states and all edges of the transfer matrix unambiguously.

## Proof

**Eventual periods.** Encode bits by spins \(s_i(t)\in\{-1,1\}\). Add an identical positive diagonal weight \(0<\varepsilon<1\) to the symmetric adjacency matrix, obtaining \(B\). Every integer neighbour sum retains its sign, while zero sums become \(\varepsilon s_i\); thus \(s_i(t+1)=\operatorname{sgn}((Bs(t))_i)\) exactly implements the stated tie convention. Set \(E_t=-s(t+1)^TBs(t)\). Symmetry gives
\[
E_{t+1}-E_t=-\sum_i (s_i(t+2)-s_i(t))(Bs(t+1))_i\le0.
\]
Because \(s_i(t+2)\) is the sign of its nonzero local field, each nonzero difference makes its corresponding summand strictly negative. There are finitely many \(E_t\) values, so eventually \(s(t+2)=s(t)\). Thus all eventual periods divide two.

**Phase representation.** On any periodic orbit, the private leaves attached to one core vertex have identical bits, since at every step all copy that core's preceding state. Denote a phase by \((a,c)\in\{0,1\}^n\times\{0,1\}^n\): \(a\) is the core word, and all \(r\) private leaves at site \(i\) have bit \(c_i\). To have period dividing two the next phase must be \((c,a)\), because the leaves in the next phase copy \(a\). Conversely, if the core rule takes \((a,c)\) to \((c,a)\), and the core rule takes \((c,a)\) back to \((a,c)\), this is a periodic state; no two different ordered pairs yield the same labelled state.

**One leaf.** At site \(i\) a prescribed core transition from \(a_i\) to \(c_i\) succeeds exactly when \(a_{i-1}=c_i\) or \(a_{i+1}=c_i\): of three neighbours, one is the private leaf with bit \(c_i\). The reverse transition requires \(c_{i-1}=a_i\) or \(c_{i+1}=a_i\). Consequently, in the bipartite double cover of the cycle, whose two vertex classes carry words \(a\) and \(c\) and whose edges connect indices differing by one, every vertex has at least one equally labelled neighbour. For odd \(n\), this double cover is one cycle with \(2n\) vertices; for even \(n\), it is two disjoint \(n\)-cycles. This gives the displayed counts \(P_{n,1}\). A fixed configuration has \(a=c\), reducing to the no-isolated-bit criterion on \(C_n\), giving \(H_{n,1}=Q_n\). To compute \(Q_j\), index a four-state adjacency matrix \(N\) by ordered bit pairs, allowing \((u,v)\to(v,w)\) exactly when \(v=u\) or \(v=w\); then \(Q_j=\operatorname{tr}(N^j)\) and direct determinant expansion yields \(\det(zI-N)=(z^2-z-1)(z^2-z+1)\). Its four roots prove the formula for \(Q_j\).

**Two leaves.** A core vertex sees two private bits \(c_i\) and its two core-cycle neighbours. If \(a_i=c_i\), the proposed transition is automatic, even if both cycle neighbours disagree, because a two-to-two tie retains \(a_i\). If \(a_i\ne c_i\), the proposed transition occurs precisely when at least one adjacent core bit agrees with \(c_i\); the reverse proposed transition occurs precisely when at least one adjacent leaf-word bit agrees with \(a_i\). Thus the two simultaneous constraints are exactly \(T(u,v,w)=1\). The standard bijection between admissible cyclic \(n\)-letter words and closed length-\(n\) walks in the ordered-pair transition graph gives \(P_{n,2}=\operatorname{tr}(M^n)\), with no rotational quotient. The finite determinant identity for \(M\) follows from exact integer matrix multiplication and Newton's identities, also independently reproducible in the supplied script. Its nonzero roots yield the stated root sum. Fixed configurations force \(a=c\), and every such assignment is fixed because the two private neighbours agree with the core; hence \(H_{n,2}=2^n\).

**Three or more leaves.** Once the system has undergone one step, the private leaf bundle at every core site is monochromatic. Thereafter, its \(r\ge3\) identical leaf votes strictly outweigh the two cycle-neighbour votes, so for each \(t\ge1\) the core word at \(t+1\) equals the leaf word at \(t\), while leaves at \(t+1\) equal the core at \(t\). Therefore the state at \(t+2\) equals that at \(t\) for every \(t\ge1\), proving the one-step entrance bound. Every chosen ordered pair of core and monochromatic-leaf words is already periodic, giving \(4^n\) states, and those with equal words are precisely \(2^n\) fixed states. Taking any initial state with a nonmonochromatic bundle shows that zero updates cannot suffice uniformly; the upper bound one is sharp.

## Verification

The standalone script `VERIFY.py` implements the *vertex-level* majority update, including individual labelled leaves. It checks the sixteen-state transfer matrix's full characteristic polynomial using exact Newton identities, and then independently checks its traces against explicit phase-pair enumeration for \(3\le n\le9\). Exhaustive enumeration of all labelled initial states verifies the claimed fixed and periodic counts for \(r=1,3\le n\le9\), \(r=2,3\le n\le6\), \(r=3,3\le n\le4\), and \(r=4,n=3\), a total of \(751{,}424\) initial configurations. For \(r\ge3\), it additionally checks the stated one-update convergence on every enumerated state. The script and its passing stdout are included. These finite checks corroborate the independent all-size proof; they are not substituted for it.

## Relationship to prior work

Goles and Olivos established eventual-period-two behaviour for finite symmetric threshold networks; that general theorem is re-proved here in the exact tie convention. Agur, Fraenkel and Klein derived the no-isolated-run cyclic word count for the radius-one closed-neighbourhood majority rule; consequently, \(Q_n\) and its recurrence are not claimed as new. The present cycle-corona graph dynamics differs: private leaves encode a one-step delayed input, and the new contribution is the *complete three-regime exact census* of periodic states across all leaf multiplicities, including the two-leaf quartic spectrum. The 2014 work of Benjamini, Chan, O'Donnell, Tamuz and Tan studies convergence and disagreement on different graph classes; Turau's 2022 fixed-point/2-cycle characterizations concern trees, rather than these unicyclic coronas. A similar underlying sunlet graph equipped with XOR-neighbour updates is a different dynamical system and does not imply majority counts.

## Limitations

Historical uniqueness is bounded by accessible sources, including searches for equivalent weighted-majority and delayed-majority formulations; an unindexed exact corona census may exist. The ring fixed-point formula \(Q_n\) is known prior art. The result gives exact eventual attractor counts, not basin sizes or sharp entry times for \(r=1,2\). The transfer-matrix characteristic polynomial is a finite exact algebraic identity; it is also reproducible from the included integer checker. No independent external audit has been performed.

## References

1. E. Goles and J. Olivos, "Periodic behaviour of generalized threshold functions", *Discrete Mathematics* **30** (1980), 187–189. DOI: `10.1016/0012-365X(80)90121-1`.
2. Z. Agur, A. S. Fraenkel and S. T. Klein, "The number of fixed points of the majority rule", *Discrete Mathematics* **70** (1988), 295–302. DOI: `10.1016/0012-365X(88)90005-2`. Lawfully accessible full text: `https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf`.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, "Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs", arXiv:1405.2486v1 (first publicly submitted 2014-05-11), `https://arxiv.org/abs/1405.2486`.
4. V. Turau, "Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees", arXiv:2202.01580 (2022), `https://arxiv.org/abs/2202.01580`.
