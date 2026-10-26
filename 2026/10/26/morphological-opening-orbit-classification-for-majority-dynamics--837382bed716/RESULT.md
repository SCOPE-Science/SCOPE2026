# Morphological-opening orbit classification for majority dynamics on fan graphs

## Finding
For every integer \(n\ge3\), let \(F_n\) be synchronous binary open-neighbour majority with tie retention on the fan \(K_1\vee P_n\): a hub adjacent to every vertex of an open path of length \(n\) vertices. Exactly two configurations are fixed: the two monochromatic configurations. Every other recurrent state belongs to a primitive two-cycle in which the hub flips at every step; no hub-preserving two-cycle exists.

There is an exact and constructive description of every primitive two-cycle. Index path sites by \(0,\ldots,n-1\). For binary path words \(x,y\), define the endpoint-reflexive adjacency neighborhoods \(B_0=\{0,1\}\), \(B_{n-1}=\{n-2,n-1\}\), and \(B_i=\{i-1,i+1\}\) for \(1\le i\le n-2\). Let
\[
(E x)_i=\bigwedge_{j\in B_i}x_j,\qquad (D y)_i=\bigvee_{j\in B_i}y_j.
\]
Primitive two-cycles correspond bijectively to binary words \(x\) satisfying
\[
D E x=x,\qquad 2|x|>n,\qquad 2|E x|<n.
\]
The corresponding orbit is exactly \((0,x)\leftrightarrow(1,E x)\), where \(0\) and \(1\) denote hub states and \(|\cdot|\) is Hamming weight.

The number \(H_n\) of distinct primitive two-cycles has the exact finite transfer expression
\[
H_n=\sum_{2i>n,\,2j<n}[U^iV^j]P_n(U,V),\qquad P_n(U,V)=L(U,V)\,T(U,V)^{n-2}\,R.
\]
Here the explicitly defined matrix \(T\) has size \(16\times16\), the vectors \(L,R\) are given below, and all entries are polynomials with nonnegative integer coefficients. Thus the exact number of recurrent labelled configurations is \(2+2H_n\). Moreover, \(H_4=0\), while \(H_n>0\) for \(n=3\) and every \(n\ge5\).

## Assumptions and scope
All graph vertices are distinct and labelled. Path endpoints have degree two, internal path vertices have degree three, and the hub has degree \(n\). A tie at any vertex keeps that vertex's previous state. All updates are parallel. Set \(\Sigma=\{(0,0),(0,1),(1,0),(1,1)\}\). Write \(s=(s_x,s_y)\) for a letter. Index transfer states by ordered pairs \((s,t)\in\Sigma^2\), of which there are sixteen.

Define the left-boundary vector, interior matrix, and right-boundary vector by
\[
L_{(s,t)}=\mathbf1\{s_y=s_xt_x,\;s_x=s_y\lor t_y\}\,U^{s_x+t_x}V^{s_y+t_y},
\]
\[
T_{(s,t),(t',u)}=\mathbf1\{t=t',\;t_y=s_xu_x,\;t_x=s_y\lor u_y\}\,U^{u_x}V^{u_y},
\]
\[
R_{(s,t)}=\mathbf1\{t_y=s_xt_x,\;t_x=s_y\lor t_y\}.
\]
Here Boolean products mean AND and \(\lor\) means OR, while \(\mathbf1\) is the truth indicator. For \(n=2\) the formula remains meaningful, but the claimed classification and cutoff are stated for \(n\ge3\).

## Proof
**Period bound.** Represent states by spins \(\pm1\) and let \(W\) be the symmetric real adjacency matrix of the fan plus \(\frac12 I\). Every spin's majority-with-tie-retention update equals the sign of its \(W\)-weighted neighbor sum; none of those sums vanish. Let \(z(t)\) be the spin vector and set \(Q_t=z(t)^\mathsf T W z(t+1)\). Since \(W\) is symmetric, choosing \(z(t+2)\) coordinatewise to maximize the nonzero local fields at time \(t+1\) gives \(Q_{t+1}\ge Q_t\), with strict inequality whenever \(z(t+2)\ne z(t)\). There are finitely many ordered state pairs, so a strict increase cannot continue forever. Hence all trajectories eventually have primitive period one or two.

**No hub-preserving recurrent orbit.** If a hub stays zero for two successive updates, the path update is the AND map \(E\) above; if it stays one, it is the OR map \(D\). The relation \((E^t x)_i\) is AND over the endpoint-reflexive walks of length \(t\) from site \(i\), and analogously \((D^t x)_i\) is OR over those walks. The endpoint-reflexive path graph is connected and contains loops at its two endpoints. For every sufficiently large \(t\) (for example \(t\ge2n\)), every vertex is reachable from every other by a walk of precisely \(t\). Thus \(E^t x\) is all zero unless \(x\) is all one, and \(D^t x\) is all one unless \(x\) is all zero. Consequently a period-one or period-two path state with a constant hub must be monochromatic. The pair consisting of a zero hub with all-one path cannot recur since its hub changes immediately; likewise a one hub with all-zero path. Exactly the two entirely monochromatic configurations remain fixed, and no nontrivial hub-preserving orbit is recurrent.

**Hub-flipping characterization.** At hub zero, an internal path vertex adopts one precisely if both path neighbors are one, and a path endpoint adopts one precisely if itself and its sole path neighbor are one. Hence the path update is \(E\). At hub one, these rules become OR, namely \(D\). Therefore the two-step return condition is precisely \(y=E x\) and \(x=D y\). The zero hub flips to one exactly when \(2|x|>n\); the one hub flips back exactly when \(2|y|<n\), since ties retain their hub state. These two strict weight inequalities together with \(DE x=x\) are thus necessary and sufficient. Each primitive cycle has exactly one state with hub zero, proving the claimed bijection.

**Exact count.** A pair of length-\(n\) words \(x,y\) satisfying \(y=Ex\), \(x=Dy\) is uniquely encoded by successive letters \(s_i=(x_i,y_i)\in\Sigma\). The left-boundary constraints are exactly the indicator in \(L\); for any three consecutive letters \((s,t,u)\), the middle constraints are exactly the indicator in \(T\); the right-boundary constraints are exactly the indicator in \(R\). Multiplication by \(U^{x_i}V^{y_i}\) counts both Hamming weights once each. Therefore the polynomial \(P_n=L T^{n-2}R\) counts each compatible pair exactly once. Filtering exponents with \(2i>n\), \(2j<n\) counts the hub-flipping cycles exactly.

**Existence cutoff.** For \(n=3\), the zero-hub path word \(110\) satisfies the conditions. For every odd \(n\ge5\), take \(x=1^{(n+1)/2}0^{(n-1)/2}\); the endpoint-reflexive AND map yields \(|Ex|=(n-1)/2\), and \(DEx=x\). For each even \(n\ge6\), take \(x=0\,1^{n/2+1}0^{n/2-2}\); then \(|Ex|=n/2-1\) and again \(DEx=x\). The corresponding \(x\) always has more than \(n/2\) ones. At \(n=4\), any \(x\) of weight at least three has \(|Ex|\ge2\), so the strict two-cycle inequality fails. Hence \(H_4=0\).

## Verification
The included standalone program computes the transfer matrix's weight-filtered count independently of exhaustive full majority updates. It checked every labelled state for each \(3\le n\le12\), covering 16,368 starting states, and independently confirmed both the fixed-state count and the hub-oriented primitive two-cycle census. The resulting sequence \((H_3,\ldots,H_{12})\) is \((3,0,5,3,21,16,66,65,220,243)\). All unbounded claims follow from the proof, not the finite simulation.

## Relationship to prior work
The general finite-graph period-one-or-two theorem is classical (Goles--Olivos, 1980), and general majority voting-time bounds were sharpened by Kaaser, Mallmann-Trenn and Natale (2015/2016). The graph-specific result here instead describes every recurrent configuration and gives an exact endpoint-sensitive transfer census. Existing studies of the wheel (a cone over a *cycle*, rather than over this open path) cannot transfer their circular boundary conditions directly; in particular, this open boundary rules out all hub-preserving two-cycles. The morphology operators are the natural one-dimensional AND erosion and OR dilation associated with endpoint-reflexive path adjacency.

## Limitations
The theorem classifies recurrent states and counts them exactly for each finite \(n\); it does not give basin sizes, entrance times, or a closed scalar linear recurrence for the inequality-filtered sequence \(H_n\). The transfer formula is finite and effective, not a proof of a simple closed asymptotic law. The historical literature comparison is bounded; an unindexed equivalent classification cannot be ruled out. Independently verify novelty before asserting priority.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, submitted 2015-08-14; MFCS 2016, DOI: 10.4230/LIPIcs.MFCS.2016.55.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, submitted 2014-05-11.
