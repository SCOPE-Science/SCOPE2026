# A complete necklace spectrum for majority dynamics on alternating connected cubic graphs

## Finding
For every integer \(m\ge2\), construct two connected, isomorphic, simple, cubic bipartite graphs \(G_0,G_1\) on the same labelled set of \(4m\) vertices. At even steps apply simultaneous strict-neighbour binary majority on \(G_0\), and at odd steps apply it on \(G_1\). The phase-augmented map is \(H(p,x)=(1-p,F_p(x))\), \(p\in\{0,1\}\). Each frozen map \(F_p\) separately has only eventual periods at most two, but the switching system has primitive augmented periods \(2d\) for **every divisor \(d\) of \(m\)**, and no others. In particular periods \(2m\) grow without bound even though every snapshot is connected, cubic, and isomorphic to the other.

At either fixed phase there are exactly \(4^{m+1}\) recurrent labelled binary configurations out of \(2^{4m}\). Writing \(\mu\) for the number-theoretic Möbius function, the number of distinct phase-augmented orbits of least period \(2d\) is exactly
\[
N_{2d}(m)=\frac4d\sum_{e\mid d}\mu(d/e)4^e\quad(d\mid m).
\]

Every initial condition enters the recurrent set after at most \(m-1\) updates, and the bound is attained. More precisely, let \(\tau\) be the first time the phase-augmented trajectory belongs to a periodic orbit, and for \(0\le t<m\) let \(A_t\) be the \((t+1)\)-state matrix with transitions \(i\to0\) for all \(0\le i\le t\) and \(i\to i+1\) for \(0\le i<t\), each of multiplicity one. Then, at either fixed initial phase,
\[
\#\{x:\tau(x)\le t\}=2^{2m}\left(1+\operatorname{tr}(A_t^m)\right)^2,\qquad 0\le t\le m-1.
\]
For \(t\ge m-1\) the count is all \(2^{4m}\) configurations. The sharp individual entry time is also given below by cyclic runs of mixed vertex pairs.

## Assumptions and scope
Let \(C_j=\{(j,0),(j,1)\}\), \(j\in\mathbb Z/(2m)\). The graph \(G_0\) contains all four edges between \(C_{2k}\) and \(C_{2k+1}\), and just the two same-label edges between \(C_{2k+1}\) and \(C_{2k+2}\). The graph \(G_1\) reverses these edge types: same-label edges between \(C_{2k}\) and \(C_{2k+1}\), and all four edges between \(C_{2k+1}\) and \(C_{2k+2}\). Indices are cyclic and \(k=0,\ldots,m-1\). Edges are simple, undirected, without loops; each vertex has three distinct neighbours. Each snapshot is connected because its cluster-adjacency support is the entire cycle. Translation \(j\mapsto j+1\) is an isomorphism \(G_0\to G_1\). All actual updates use strict majority of three open neighbours, so ties never arise.

A configuration \(x\) assigns an element of \(\{0,1\}\) to each labelled vertex. The phase \(p\) is included in the state for recurrence and period definitions. This avoids treating a constant binary configuration as a period-one orbit of the two-phase autonomous extension: its **augmented** period is two.

## Proof
**1. Exact mixed-pair factor.** Put \(a_j=x_{j,0}\), \(b_j=x_{j,1}\), and \(M_j=a_j\oplus b_j\). At a dense neighbour cluster, the two votes are equal if that cluster is uniform and split if it is mixed. Thus a cluster copies the uniform dense neighbour whenever the latter is uniform; otherwise its two vertices copy the corresponding vertices in its sparse neighbour. For either phase, the resulting mixedness satisfies the exact Boolean identity
\[
M_j(t+1)=M_{j-1}(t)M_{j+1}(t).
\]
It follows by induction that
\[
M_j(t)=\bigwedge_{r=0}^{t}M_{j-t+2r}(0).
\]
The indices on the right traverse a consecutive arc of length \(t+1\) in one of the two cyclic parity subsequences, each of length \(m\).

**2. Recurrent mixedness and sharp entry time.** Write \(E=(M_0,M_2,\ldots,M_{2m-2})\) and \(O=(M_1,M_3,\ldots,M_{2m-1})\). For any binary cyclic word \(w\) of length \(m\), let \(\lambda(w)=0\) when \(w\) is all ones, and otherwise let \(\lambda(w)\) be the longest cyclic consecutive run of ones (zero for the all-zero word). If \(w\) contains a zero, its length-\((t+1)\) cyclic moving AND is all zero exactly when \(t\ge\lambda(w)\); before that, it contains both zeros and ones. If \(w\) is all ones, its moving AND is always all ones. Therefore the first time \(M(t)\) is constant separately on its even and odd sites is exactly
\[
\tau(x)=\max\{\lambda(E),\lambda(O)\}.
\]
The four parity-constant templates are \((0,0),(1,1),(0,1),(1,0)\), recording the even and odd mixedness values. Once in this set, the evolution of the payload bits is bijective by Step 3; hence these and only these configurations are periodic in the phase-augmented state. The word with a single zero and otherwise ones has \(\lambda=m-1\), proving sharpness of the \(m-1\) bound.

**3. All four exact return permutations.** Define the payload \(u_j=a_j\); the complete pair is \((u_j,u_j\oplus M_j)\). In a uniform template, \(G_0\) swaps payloads across \((2k,2k+1)\), and \(G_1\) swaps them across \((2k+1,2k+2)\). Their two-step product has exactly two disjoint \(m\)-cycles on payload coordinates. In the all-mixed template, dense and sparse swaps exchange roles, giving the inverse product, again two \(m\)-cycles. In the mixed-even/uniform-odd template, the first update shifts all payloads by one site in one direction and the second update shifts them by one more site in the same direction; in the opposite alternating template both shifts are reversed. Hence their two-step products are translations by \(\pm2\) on the \(2m\)-cycle, also two disjoint \(m\)-cycles. The mixedness template returns after the two steps in every case. Thus the return map \(T=F_1\circ F_0\) restricted to **each** template is conjugate to a product of two independent cyclic rotations of length \(m\) on binary payloads. It is a bijection on that template, and all configurations in all templates are recurrent. Conversely the moving-AND argument in Step 2 excludes every other recurrent mixedness pattern.

**4. Exact counts and orbit periods.** There are \(2^{2m}=4^m\) payload assignments for each of four templates; this proves \(4^{m+1}\) recurrent configurations at a chosen phase. Each template contributes \(2^{2\gcd(m,k)}=4^{\gcd(m,k)}\) fixed configurations of \(T^k\), so
\[
\#\operatorname{Fix}(T^k)=4\cdot4^{\gcd(m,k)}.
\]
Möbius inversion gives \(4\sum_{e\mid d}\mu(d/e)4^e\) configurations of least return period \(d\), for each \(d\mid m\); dividing by \(d\) gives the stated augmented-orbit count. Adding a phase label doubles each full orbit length, giving exactly the periods \(2d\). A payload with one 1 among an otherwise zero \(m\)-coordinate rotation exhibits least return period \(m\), and standard primitive binary words give every \(d\mid m\).

**5. Entry-time distribution.** A cyclic length-\(m\) mixedness word has \(\lambda(w)\le t\) if and only if it is all ones, or every cyclic block of \(t+1\) positions has a zero. For \(0\le t<m\), the transfer matrix \(A_t\) counts precisely the second class: its states record the number of consecutive ones since the last zero, with every zero resetting to state zero and a one increasing the state while permitted. Closed walks on \(A_t\) correspond bijectively to labelled cyclic words with no cyclic run longer than \(t\), other than the excluded all-ones word; this works because a cyclic word containing a zero fixes its run-state uniquely. Thus there are \(1+\operatorname{tr}(A_t^m)\) admissible words per parity. Each prescribed mixedness pattern supports \(2^{2m}\) payload assignments. The independent even/odd choices give the claimed exact cumulative count.

## Verification
Run the standalone Python program `verify.py` using Python 3 without dependencies. Its recorded output is `verification_output.txt`. Direct vertex-level enumeration exhaustively checks all \(256+4096+65536=69888\) initial configurations for \(m=2,3,4\), independently computes their first recurrent-entry times and two-step return periods, and checks both the transfer-matrix cumulative counts and the analytic counts. For \(2\le m\le8\) additional tests check graph structure, graph isomorphism, all four invariant templates and the \(m\)-step return identity on prescribed payloads. These are finite checks supporting, not replacing, the all-parameter proof above.

## Relationship to prior work
Goles and Olivos established the period-at-most-two theorem for a **fixed** symmetric threshold network; Benjamini et al. explain the theorem for static finite majority graphs and extend aspects to infinite graphs. Here both graph snapshots individually satisfy their hypotheses, but the network changes periodically and the two-step composite is not a single static symmetric-threshold update. Haslegrave and Cannings obtain non-two periods in a **fixed** graph with a single nonconforming rule; no vertex is nonconforming in the present construction, which instead alternates two ordinary majority graphs. Those results therefore do not imply this full switched-cubic attractor and transient census. Exact equivalents remain possible in unindexed literature.

## Limitations
The theorem concerns this explicit two-snapshot graph family, not arbitrary time-varying cubic graphs. Augmented periods count the switching phase; some unaugmented binary state sequences may have shorter visual repetitions. Reproducible finite enumeration is not a proof for arbitrary \(m\); the proof is the Boolean mixedness factor and exact payload permutations. The count does not claim robustness to changes in graph edges or update thresholds. Independent validation and external novelty certification have not been performed.

## References
1. E. Goles and J. Olivos, "Periodic behaviour of generalized threshold functions," *Discrete Mathematics* 30 (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, "Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs," arXiv:1405.2486 (first public version 2014-05-11), https://arxiv.org/abs/1405.2486.
3. J. Haslegrave and C. Cannings, "Majority dynamics with one nonconformist," arXiv:1606.05496 (first public version 2016-06-17), https://arxiv.org/abs/1606.05496.
