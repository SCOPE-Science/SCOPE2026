# A parity-factorized periodic-orbit census for majority dynamics on sunlet graphs

## Finding
For each integer \(n\ge 3\), let \(S_n=C_n\circ K_1\) be the labelled sunlet graph: a cycle of \(n\) vertices, each carrying one distinct pendant leaf. Under synchronous binary strict-majority updating over the neighbors (no self-vote and no tie), write \(F_n\) for the number of fixed configurations and \(N_n\) for the number of distinct primitive period-two orbits, identifying only the two successive time phases, not graph rotations or reflections. Define
\[
\phi=\frac{1+\sqrt5}{2},\qquad
\psi=\frac{1-\sqrt5}{2},\qquad
R_m=\phi^m+\psi^m+2\cos\!\left(\frac{m\pi}{3}\right).
\]
Then the complete recurrent-orbit census is
\[
\boxed{F_n=R_n,\qquad
N_n=\begin{cases}
(R_{2n}-R_n)/2,&n\text{ odd},\\
R_n(R_n-1)/2,&n\text{ even}.
\end{cases}}
\]
The number \(Q_n\) of labelled configurations satisfying two-step return is \(R_{2n}\) for odd \(n\) and \(R_n^2\) for even \(n\). Every trajectory eventually reaches a fixed point or a primitive two-cycle, by the classical finite-graph period-two theorem for synchronous symmetric threshold dynamics. Thus these formulas enumerate *all* recurrent orbits.

The parity distinction has a structural cause: the two-time-layer constraint graph is one cycle of length \(2n\) for odd \(n\), but two disjoint cycles of length \(n\) for even \(n\). In particular,
\[
N_n\sim\tfrac12\phi^{2n},\qquad
\frac{Q_n}{2^{2n}}\sim\left(\frac{\phi^2}{4}\right)^n.
\]

## Assumptions and scope
The graph is undirected, simple, and has \(2n\) individually labelled vertices. The updates are parallel. A pendant vertex has its core neighbor as its sole input; a core vertex has its two cyclic neighbors and its pendant as its three inputs. All bits lie in \(\{0,1\}\), and the majority function equals the bit occurring at least twice in its three arguments. No boundary, noise, bias, self-interaction, or time-dependent schedule is present. The orbit counts identify temporal phase only; color complement, cyclic graph rotations, and graph reflections are *not* quotiented. A fixed configuration is an orbit of length one.

## Proof
Let \(u_i(t)\) and \(v_i(t)\) be the core and pendant bits, with cyclic indices in \(\mathbb Z/n\mathbb Z\). The exact update is
\[
u_i(t+1)=\operatorname{Maj}(u_{i-1}(t),u_{i+1}(t),v_i(t)),\qquad
v_i(t+1)=u_i(t).
\]
Suppose a configuration returns after two updates. Put \(a_i=u_i(t)\), \(b_i=u_i(t+1)\). Since pendants lag by one update and the state has period dividing two, \(v_i(t)=b_i\), \(v_i(t+1)=a_i\). Thus the two-step return conditions are exactly
\[
b_i=\operatorname{Maj}(a_{i-1},a_{i+1},b_i),\qquad
a_i=\operatorname{Maj}(b_{i-1},b_{i+1},a_i).
\]
For three binary inputs \(p,q,z\), the equality \(\operatorname{Maj}(p,q,z)=z\) holds if and only if at least one of \(p,q\) equals \(z\). Therefore the conditions reduce to
\[
b_i\in\{a_{i-1},a_{i+1}\},\qquad
a_i\in\{b_{i-1},b_{i+1}\},\quad i\in\mathbb Z/n\mathbb Z.
\]
Conversely, any two binary words \(a,b\) satisfying these conditions produce a genuine two-step returning pair of full configurations \((a,b)\) and \((b,a)\), with the second component in each ordered pair representing pendant bits. Hence no periodic configurations are missed or duplicated by this parametrization.

Build a bipartite graph \(H_n\) with vertices \(A_i,B_i\), and edges \(A_iB_{i-1}\), \(A_iB_{i+1}\). Assign bit \(a_i\) to \(A_i\) and \(b_i\) to \(B_i\). Every vertex has degree two, and the conditions say exactly that every vertex has at least one neighbor with the same bit. On a cyclic connected component, this means there is no singleton run of either bit (constant words are allowed). Traversing two edges of \(H_n\) advances an index by two modulo \(n\). Consequently, \(H_n\cong C_{2n}\) when \(n\) is odd, and \(H_n\cong C_n\sqcup C_n\) when \(n\) is even.

To count admissible cyclic words of length \(m\ge3\), use ordered adjacent-bit states \(00,01,10,11\) and transfer matrix
\[
M=\begin{pmatrix}
1&1&0&0\\
0&0&0&1\\
1&0&0&0\\
0&0&1&1
\end{pmatrix}.
\]
A transition from \((p,q)\) to \((q,r)\) is allowed precisely when \(q=p\) or \(q=r\). Closed walks of length \(m\) in this matrix correspond bijectively to admissible *labelled-position* cyclic words of length \(m\), so their number is \(\operatorname{tr}(M^m)\). A direct determinant calculation gives
\[
\det(\lambda I-M)=(\lambda^2-\lambda-1)(\lambda^2-\lambda+1).
\]
Its four roots are \(\phi,\psi,e^{i\pi/3},e^{-i\pi/3}\). Therefore \(\operatorname{tr}(M^m)=R_m\). The component decomposition of \(H_n\) now yields \(Q_n=R_{2n}\) for odd \(n\) and \(Q_n=R_n^2\) for even \(n\).

Fixed points are exactly the returning pairs satisfying \(a=b\); the same neighbor-agreement constraint then applies to the single binary cyclic word \(a\), so there are \(F_n=R_n\) of them. Every other two-step returning configuration belongs to a primitive orbit of exactly two configurations. Thus \(N_n=(Q_n-F_n)/2\), proving the displayed census. The established Goles–Olivos finite symmetric-threshold period theorem excludes eventual least periods greater than two. Finally \(R_m=\phi^m+O(1)\) (indeed the remaining terms are bounded), giving both asymptotics.

## Verification
The independent standalone program `verify_sunlet.py` implements the original simultaneous vertex update bitwise, without using the two-layer condition in that implementation. It enumerates every full state for \(3\le n\le10\), a total of \(1{,}398{,}080\) labelled microscopic states, and separately checks fixed and two-step-return populations. It also enumerates cyclic words for \(3\le m\le16\), checks the four-state transfer identity through power 40, and compares every tested value with the closed formulas. Run `python3 verify_sunlet.py`; the included `verify_sunlet_output.txt` records the successful replay. The computations are finite checks and do not replace the proof for arbitrary \(n\).

Values for \(n=3,4,5,6,7,8,9,10\) are respectively \(F_n=2,6,12,20,30,46,74,122\) and \(N_n=9,15,55,190,406,1035,2853,7381\).

## Relationship to prior work
Goles and Olivos established the finite symmetric-threshold period-two property, so the restriction to eventual periods one and two is classical. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, especially introduction, Theorem 1.1, and Sections 2–4) study convergence, unanimity and disagreement for finite and infinite majority dynamics. Their theorems do not provide the labelled sunlet recurrent-state counts, the even/odd two-layer decomposition, or the explicit Lucas–trigonometric formula here.

Noual (arXiv:1605.01505v1, Sections 2–10 and Table 1) treats attracting orbits of Boolean automata cycles and two tangent directed automata cycles, with particular forbidden-word conditions. Although binary necklaces and Lucas numbers appear there, the network structures and local update rules are different: the sunlet majority network has all its core inputs coupled by the ternary majority operation and \(n\) additional pendant-copy interactions, and it is not a Boolean automata cycle or a pair of tangent cycles. Neither the cited bounds nor the cycle-intersection results imply this sunlet count. Existing recurrent-orbit results for different majority-graph families likewise do not provide the present two-layer constraint-graph isomorphism.

## Limitations
These formulas count labelled recurrent states and primitive two-cycles, not the transient basin sizes, entry-time distribution, or attractor probabilities from uniform initial configurations. The second asymptotic describes the fraction of initially periodic states, not the probability that a random state eventually enters a particular orbit. No numerical calculation establishes novelty; unindexed or historically equivalent results remain possible. The connection to the general period-two theorem is acknowledged, not presented as a new result.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (first public May 11, 2014); Stochastic Processes and their Applications **126** (2016), 2719–2733.
3. M. Noual, *A combinatorial problem about binary necklaces and attractors of Boolean automata networks*, arXiv:1605.01505v1 (May 5, 2016).
