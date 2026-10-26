# Exact two-step dynamics and basin census of parity automata on rectangular Hamming graphs

## Finding
For synchronous binary neighbour-parity dynamics on any rectangular Hamming graph \(G=K_{n_1}\square\cdots\square K_{n_d}\), with \(d\ge1\) and integer widths \(n_i\ge1\), the global map \(F\) satisfies \(F^4=F^2\). The complete periodic-state, fixed-state and transient-depth census depends only on elementary products of the odd- and even-width axes, as given below. In particular, there are no primitive periods other than one and two, and every configuration becomes periodic after at most two updates.

Write \(N=\prod_i n_i\), let \(E=\{i:n_i\text{ is even}\}\), \(O=\{i:n_i\text{ is odd}\}\), and define the empty product to be one. Set
\[
 A=\prod_{i\in E}n_i,\qquad B=\prod_{i\in E}(n_i-2),\qquad C=\prod_{i\in O}n_i,\qquad D=\prod_{i\in O}(n_i-2).
\]
With \(\delta=d\bmod2\), set
\[
 w=\frac{C-(-1)^\delta D}{2},\quad v=C-w,\quad r=\frac{A-B}{2}.
\]
All are nonnegative integers. The number of periodic configurations, fixed configurations and distinct primitive two-cycles are respectively
\[
 P=2^{wA},\qquad Q=2^{w(A+B)/2},\qquad (P-Q)/2.
\]
If \(T_j\) denotes the number of initial configurations whose *least* time to reach a periodic configuration equals \(j\), then
\[
 T_0=2^{wA},\qquad T_1=2^{N-vr}-2^{wA},\qquad T_2=2^N-2^{N-vr}.
\]
For each positive integer \(k\), the number of \(F^k\)-fixed configurations is \(Q\) if \(k\) is odd, and \(P\) if \(k\) is even. The dynamical zeta function is \((1-t)^{-Q}(1-t^2)^{-(P-Q)/2}\).

## Assumptions and scope
The vertices are tuples \((a_1,\ldots,a_d)\), with \(1\le a_i\le n_i\); two vertices are adjacent if they differ in exactly one coordinate. A state assigns an element of \(\mathbb F_2\) to every vertex. At each synchronous update a vertex replaces its state by the sum modulo two of its *open* neighbours' states; there are no self-loops. A factor \(K_1\) is permitted, so the empty neighbourhood case is included. The asserted transient time is measured from the original state and is the first index whose state is periodic. All formulas concern labelled configurations, not rotation or graph-automorphism classes.

## Proof
Identify the state space with the tensor product \(V=\bigotimes_{i=1}^d\mathbb F_2^{n_i}\). Let \(J_i\) act by the all-ones matrix in tensor coordinate \(i\) and identity elsewhere. Since the adjacency matrix of a complete graph over \(\mathbb F_2\) is \(J_i+I\), the Cartesian-product neighbour update is
\[
 F=\delta I+\sum_{i=1}^d J_i.
\]
The operators commute and satisfy \(J_i^2=(n_i\bmod2)J_i\). Characteristic two therefore gives
\[
 F^2=\delta I+\sum_{i\in O}J_i=:H,\qquad H^2=H.
\]
In particular \(F^4=F^2=H\), and \(FH=HF\). On \(\operatorname{im}H\), \(F^2=I\); on \(\ker H\), \(F^2=0\). Hence \(\operatorname{im}H\) is exactly the set of periodic configurations, and each state enters it in at most two steps.

For an odd width, the all-ones map \(J_i\) is a rank-one projection. Its image has dimension one and its kernel dimension \(n_i-1\). Decomposing the tensor factors for all \(i\in O\), each component indexed by the subset \(S\subseteq O\) on which the image was chosen has \(H\)-eigenvalue \(\delta+|S|\bmod2\), and multiplicity \(\prod_{i\in O\setminus S}(n_i-1)\). The weighted sum of multiplicities with eigenvalue one is
\[
 w=\tfrac12\left(C-(-1)^\delta D\right),
\]
and the complementary sum is \(v=C-w\). Thus \(\operatorname{rank}H=wA\), proving the periodic-state count.

For any even width \(n_i\), the map \(J_i\) has rank one and square zero, hence is a single size-two nilpotent Jordan block plus \(n_i-2\) one-dimensional zero blocks. Put \(M=\sum_{i\in E}J_i\) on the even-axis tensor factors. Then \(M^2=0\). The tensor product of the two-term complexes associated with those square-zero maps has homology of dimension \(B=\prod_{i\in E}(n_i-2)\): every summand with a contractible size-two factor is contractible; the summand formed entirely from the zero one-dimensional factors has dimension \(B\). Since homology dimension is \(\dim\ker M-\dim\operatorname{im}M=A-2\operatorname{rank}M\), one obtains \(\operatorname{rank}M=r=(A-B)/2\). This also covers no even factors, taking \(M=0\), \(A=B=1\).

On \(\operatorname{im}H\), the remaining update is \(F=I+M\), so its fixed subspace has dimension \(w\dim\ker M=w(A-r)=w(A+B)/2\); this proves \(Q\). Since \(F^2=I\) on the periodic subspace, the remaining \(P-Q\) periodic configurations form primitive two-cycles.

On \(\ker H\) the update is \(M\) and has rank \(vr\). Therefore the map from all initial states to the nonperiodic component after one step has rank \(vr\); exactly \(2^{N-vr}\) states enter \(\operatorname{im}H\) after at most one update. Subtracting the already-periodic \(2^{wA}\) states gives \(T_1\); the remaining states give \(T_2\). The fixed-point and zeta identities follow by decomposing the periodic set into fixed points and pairs.

## Verification
The bundled standalone `verify.py` independently constructs the graph update by enumerating adjacent vertex tuples, performs exhaustive state iteration and binary rank checks, and compares with all claimed formulas. It reports `VERIFY_OK`. The accompanying `verification_output.txt` records 35 distinct small-width test instances and further independent random checks. The proof, not the finite tests, establishes every-dimensional validity.

## Relationship to prior work
Marr and Hütt [1] studied outer-totalistic graph cellular automata and motivated topology-dependent dynamics, but their account does not present this rectangular-Hamming-graph, characteristic-two orbit-and-basin census. Chen and Reidys [2] developed general algebraic descriptions of linear sequential dynamical systems and synchronous realizations; their general framework does not itself state these specialized tensor-product ranks and exact depth strata. Existing published results for parity dynamics on complete multipartite graphs or distance-two Boolean cubes concern different adjacency operators: a special common small graph is not an implication of the general rectangular-product formula. The new contribution is the simultaneous all-width, all-dimensional periodic-point and sharp transient-depth census, not the standard observation that parity updates are linear.

## Limitations
The result is specifically for synchronous open-neighbour XOR over \(\mathbb F_2\), not majority rules, other finite fields or asynchronous updating. The upper bound two need not be attained for every choice of widths; the formula for \(T_2\) determines exactly when it is. Literature searches cannot establish uniqueness against all unindexed results; the decomposition is elementary linear algebra, so an equivalent formulation may exist in earlier algebraic graph-dynamics literature. No independent scientific audit was performed.

## References
[1] C. Marr and M.-T. Hütt, *Outer-totalistic cellular automata on graphs*, arXiv:0812.2408 (first public submission 2008-12-12), https://arxiv.org/abs/0812.2408.

[2] Y. Chen and C. M. Reidys, *Linear sequential dynamical systems, incidence algebras, and Möbius functions*, arXiv:1510.04930 (first public submission 2015-10-16), https://arxiv.org/abs/1510.04930.
