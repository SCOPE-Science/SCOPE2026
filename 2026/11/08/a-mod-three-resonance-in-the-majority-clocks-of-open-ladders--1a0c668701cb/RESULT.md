# A mod-three resonance in the majority clocks of open ladders

## Finding
For each integer \(n\ge2\), put \(G_n=P_n\square K_2\). Let \(M_n\) be synchronous strict majority among **open neighbors**: each binary vertex adopts its neighbors' majority and retains its current bit when the neighbor votes tie. Write \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) for Fibonacci numbers, and \(L_0=2,L_1=1,L_{j+2}=L_{j+1}+L_j\) for Lucas numbers. Then the exact numbers of labelled configurations obey

\[
\begin{aligned}
\#\operatorname{Fix}(M_n)&=2(F_{n+1}+1),\\
\#\operatorname{Fix}(M_n^2)&=L_{2n}+1+3\mathbf1_{3\mid n},\\
\#\{x:M_n(x)=\overline x\}&=2F_{n-1}.
\end{aligned}
\]

Every orbit eventually has least period one or two. Consequently the number of *distinct primitive two-cycle orbits* is
\[
\frac{L_{2n}-2F_{n+1}-1+3\mathbf1_{3\mid n}}{2}.
\]
For \(n=2,3,4,5,6\), the corresponding numbers are \(1,7,18,53,149\).

The period-two population has an exact, bounded three-periodic correction to a Lucas number. The subset flipping at *every* vertex has only Fibonacci-size growth. With \(\varphi=(1+\sqrt5)/2\), the fraction of primitive two-periodic states that flip everywhere is asymptotic to \(2/(\sqrt5\varphi^{n+1})\). Uniformly among the \(4^n\) initial configurations, the probability of *already* being periodic is asymptotic to \((\varphi^2/4)^n\).

## Assumptions and scope
Vertices are \((i,s)\), \(1\le i\le n\), \(s\in\{0,1\}\). Vertices with the same \(i\) and opposite \(s\) are connected by a rung, and adjacent indices on the same rail are connected. There is no wraparound edge. The four end vertices have degree two, and all other vertices have degree three. At a degree-two tie the old opinion remains; this *open-neighborhood* rule is not the majority of the closed neighborhood. All counts distinguish vertices by their given positions, not graph automorphism classes. The number of two-cycle **orbits** is half the number of two-periodic states that are not fixed.

## Proof
**Period restriction.** Put the binary opinions in \(\{-1,+1\}\). Choose \(0<\varepsilon<1\) and form the real symmetric matrix \(W=A+\varepsilon I\), where \(A\) is the graph adjacency matrix. Because the off-diagonal neighbor sums are integers, the given update is exactly \(x_{t+1}(v)=\operatorname{sgn}((Wx_t)_v)\); the argument of the sign is never zero. Define the two-time energy \(E_t=-x_{t+1}^{\mathsf T}Wx_t\). Symmetry gives
\[
E_t-E_{t-1}=-(x_{t+1}-x_{t-1})^{\mathsf T}Wx_t\le0.
\]
Every summand in the negative is nonnegative, and it is positive whenever the corresponding opinions at times \(t+1\) and \(t-1\) differ. The finite state space permits only finitely many values of this energy. It therefore stabilizes and forces \(x_{t+1}=x_{t-1}\) eventually. This reconstructs the classical period-at-most-two argument for the exact tie convention used here.

**Fixed configurations.** Encode each rung as \(00,01,10,11\). A mixed rung \(01\) or \(10\) can be fixed only when the horizontal neighbors match it (one neighbor at an end, both at an interior rung); propagation forces the entire ladder to be identically \(01\) or identically \(10\). Otherwise every rung is homogeneous, \(00\) or \(11\). A homogeneous rung is fixed at an interior position exactly when the two adjacent rung labels are not both opposite. If \(w_i\) is the common bit on rung \(i\), the boundary does not add a restriction and the successive-change indicators \(d_i=w_i\oplus w_{i+1}\) cannot contain adjacent ones. There are \(F_{n+1}\) binary change words of length \(n-1\) with no adjacent ones and two choices for \(w_1\). Adding the two constant mixed-rung configurations gives \(2(F_{n+1}+1)\).

**Pure flipping.** If every vertex flips in one step, each end rung must be mixed. A homogeneous interior rung can flip only if *both* adjacent rungs are homogeneous and opposite, so no homogeneous rung can adjoin a mixed rung. Connectivity along the ladder forces every rung to be mixed. Encode it by its top-rail bit \(w_i\). Each endpoint must differ from its sole horizontal neighbor. At an interior vertex the rung neighbor is already opposite, so flipping requires at least one of its two horizontal neighbors to disagree. Thus \(d_1=d_{n-1}=1\), and the change word \(d_1,\ldots,d_{n-1}\) has no adjacent zeros. For \(n\ge3\), its \(n-3\) interior indicators can be chosen in \(F_{n-1}\) ways, and \(w_1\) has two choices. For \(n=2\), exactly two states flip everywhere, agreeing with \(2F_1\). Color-complement symmetry of the local rule also shows that every fully flipping configuration really belongs to a primitive two-cycle.

**Two-step periodic configurations.** A two-periodic starting state \(x\) corresponds bijectively to the ordered pair \((x,M_n(x))\), which satisfies the local update in both temporal directions. A rung at times zero and one is one of sixteen letters \(e=(u,v)\in\{0,1\}^2\times\{0,1\}^2\). Define \(B(e,f)\in\{0,1\}\) to be one exactly when *both* temporal updates at rung \(e\) are valid as a degree-two end with sole horizontal neighbor \(f\). Define \(I(e,f,g)\) similarly for the middle letter \(f\), whose horizontal neighbors are \(e,g\) and whose rung neighbor is the other rail. The tests are explicit applications of majority to two neighbors for \(B\), three for \(I\), in both temporal directions. No assumptions about later times are needed because \(M_n^2(x)=x\).

Index a \(256\)-element state space by ordered letter pairs \((e,f)\) and put
\[
\ell_{(e,f)}=B(e,f),\quad r_{(e,f)}=B(f,e),\quad
T_{(e,f),(f',g)}=\mathbf1_{f=f'}I(e,f,g),
\]
with every other transfer entry zero. Checking the left end, every interior rung, and the right end gives the *exact* identity
\[
\#\operatorname{Fix}(M_n^2)=\ell^{\mathsf T}T^{n-2}r\quad(n\ge2).
\]

The following complete, small, exact certificate proves a recurrence. For each of the \(256\) states, list the six values in the corresponding coordinate of \((r,Tr,T^2r,T^3r,T^4r,T^5r)\); only the eight rows below occur. The multiplicities sum to \(256\). Directly applying the stated majority predicates yields this table; the standalone transfer checker repeats all \(256\) coordinate calculations from the local truth tables.

| Six-coordinate values | Multiplicity |
|---|---:|
| \((0,0,0,0,0,0)\) | 190 |
| \((1,1,2,7,17,44)\) | 18 |
| \((0,1,3,6,17,45)\) | 18 |
| \((0,2,4,10,28,72)\) | 12 |
| \((1,1,4,11,27,72)\) | 12 |
| \((1,2,7,17,44,117)\) | 2 |
| \((1,1,1,1,1,1)\) | 2 |
| \((1,3,6,17,45,116)\) | 2 |

Every row satisfies the linear relation with coefficients \((-1,3,-1,1,-3,1)\). Hence
\[
(T^5-3T^4+T^3-T^2+3T-I)r=0.
\]
It follows that the two-step periodic counts satisfy this order-five recurrence at every \(n\ge2\). Their first five values, obtained from the same exact local predicates, are \(8,22,48,124,326\). The proposed expression \(L_{2n}+1+3\mathbf1_{3\mid n}\) satisfies that recurrence because its annihilating polynomial divides
\[
(z^2-3z+1)(z^3-1)=z^5-3z^4+z^3-z^2+3z-1,
\]
and agrees on all five initial values. Therefore it equals the exact count for every \(n\ge2\). Subtracting the fixed states and dividing by two gives the orbit census.

**Asymptotics.** Binet's formulas give \(L_{2n}\sim\varphi^{2n}\), \(F_{n+1}\sim\varphi^{n+1}/\sqrt5\) and \(F_{n-1}\sim\varphi^{n-1}/\sqrt5\). These imply the two stated probabilities, with the denominator of the pure-flip fraction equal to the entire nonfixed two-periodic population.

## Verification
The standalone program `transfer_verify.py` constructs the full sixteen-letter alphabet and the local boundary/interior tests independently of the closed formulas. It checks the eight exact six-coordinate rows and the full \(256\)-coordinate polynomial identity, then compares all three counts with transfer enumeration for every \(2\le n\le80\). The independent `bruteforce_verify.py` constructs the graph adjacency lists and directly evaluates both applications of the majority map on **every** one of the \(4^n\) configurations for each \(2\le n\le10\), including \(1{,}048{,}576\) states at \(n=10\). Both checks passed. Logs are included for reproducibility, but the infinite conclusion follows from the recurrence certificate, not from the finite experiments alone.

## Relationship to prior work
The general eventual-period restriction for symmetric threshold maps originates with Goles and Olivos (1980) and is also explained for this exact open-neighbor tie convention by Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, 2015), whose analysis concerns convergence time rather than the ladder orbit census. Agur, Fraenkel and Klein (1988) enumerate stationary cyclic binary words for the one-dimensional **self-inclusive** radius-one majority rule, not this open-ladder system. Turau (arXiv:2202.01580v1, 2022) characterizes fixed points and cycles for **trees**, which do not contain the ladder's squares. OEIS A395029 enumerates fixed points on open ladders for **closed-neighborhood** majority, a different local rule: at three rungs its fixed-point count is \(22\), whereas the present open-neighbor rule has \(8\). Thus agreement of graph names does not imply coverage. The formula here classifies both period-one and period-two states and distinguishes fully flipping states for the open-neighbor rule.

## Limitations
These are the populations of *initially periodic* states, not the entire eventual basins or the complete distribution of transient entry times. Finite verification through a given rung count does not establish the universal formulas; the explicitly checked transfer identity does. An earlier unindexed equivalent cannot be excluded. The full text of the original three-page 1980 general theorem was unavailable; its abstract and secondary accounts establish only the general period restriction. The count is not an independently audited theorem.

## References
- E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
- Z. Agur, A. S. Fraenkel and S. T. Klein, “The number of fixed points of the majority rule,” *Discrete Mathematics* 70 (1988), 295–302. DOI: 10.1016/0012-365X(88)90005-2; accessible author's text at https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.
- D. Kaaser, F. Mallmann-Trenn and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519v1, publicly submitted 2015-08-14, https://arxiv.org/abs/1508.03519.
- V. Turau, “Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees,” arXiv:2202.01580v1 (2022), https://arxiv.org/abs/2202.01580.
- OEIS A395029, “Number of {0,1}-labelings of the ladder graph ... majority of itself and its neighbors,” May 2026, https://oeis.org/A395029 (different update rule).
