# Exact actuator count below zero forcing for bouquets of arbitrary cycles

## Finding
For every integer \(k\ge 2\) and every sequence of integers \(m_1,\ldots,m_k\ge3\), form the *cycle bouquet* \(G=B(m_1,\ldots,m_k)\) by identifying exactly one vertex (the hub \(o\)) of \(k\) otherwise vertex-disjoint, unweighted simple cycles \(C_{m_i}\). Let \(L\) be its combinatorial Laplacian. For any vertex set \(T\), write \(B_T=[e_v]_{v\in T}\), with a separate independent real control input at each selected vertex. Define \(\gamma(G)\) as the minimum \(|T|\) such that \(\dot z=-Lz+B_Tu\) is Kalman-controllable, and define \(Z(G)\) as the ordinary graph zero-forcing number.

**Theorem.** For every such bouquet,
\[
\boxed{\gamma(G)=k,\qquad Z(G)=k+1.}
\]
In particular, selecting the vertex next to the hub on each cycle yields a controllable \(k\)-actuator system; adding the hub yields a zero-forcing set. The conclusions hold for arbitrary unequal cycle lengths, with no primality or coprimality condition. By matrix symmetry, the same vertices give complete state observability when used as coordinate sensors.

## Assumptions and scope
The graph is simple, connected, undirected, *unit-edge-weighted*, and has precisely the shared-hub intersection specified above; every petal has length at least three and there are at least two petals. No edges join interiors of different cycles. The hub has degree \(2k\) and every nonhub vertex has degree two. The controller model permits independent input columns at distinct vertices; it is not a single common-input model. The exact graph Laplacian is fixed, and the result is not a generic-weight or strong-structural-controllability statement. Zero forcing uses the ordinary rule that a blue vertex with exactly one white neighbor may force that neighbor blue.

## Proof
**Necessity of \(k\) actuators.** Index petal \(i\) by \(v_{i,0}=o,v_{i,1},\ldots,v_{i,m_i-1},v_{i,m_i}=o\) in cyclic order. Define a real vector \(y^{(i)}\) to be zero on the hub and on every other petal, and on petal \(i\) set
\[
y^{(i)}(v_{i,j})=\sin(2\pi j/m_i),\quad1\le j\le m_i-1.
\]
The two contributions to the Laplacian at the hub cancel, and the usual cycle sine identity gives
\[
Ly^{(i)}=(2-2\cos(2\pi/m_i))y^{(i)}.
\]
This vector is nonzero, even for \(m_i=3\). If \(T\) contains no nonhub vertex of petal \(i\), then \(B_T^{\mathsf T}y^{(i)}=0\), violating the Popov–Belevitch–Hautus (PBH) criterion for the symmetric Laplacian. Every controllable \(T\) must therefore contain at least one nonhub vertex in each petal, and \(|T|\ge k\).

**Sufficiency of the adjacent-petal set.** Set \(T_*=\{v_{i,1}:1\le i\le k\}\). Suppose for contradiction that a nonzero real Laplacian eigenvector \(x\) with eigenvalue \(\lambda\) vanishes at every vertex of \(T_*\). Put \(h=x(o)\), \(t=2-\lambda\). Since every nonhub vertex has degree two, the coordinates along each petal obey
\[
x(v_{i,j+1})=t\,x(v_{i,j})-x(v_{i,j-1}),\qquad 1\le j\le m_i-1.
\]
If \(h=0\), the initial values \(x(v_{i,0})=x(v_{i,1})=0\) force every petal to vanish. Thus \(h\ne0\). After division by \(h\), the common recurrence has initial values \(f_0=1,f_1=0\). For \(j\ge2\),
\[
f_j=-U_{j-2}(t/2),
\]
where \(U_n\) is the Chebyshev polynomial of the second kind. The closure condition \(v_{i,m_i}=o\) requires \(f_{m_i}=1\) for each petal.

If \(|t|\ge2\), then \(|U_{m_i-2}(t/2)|\ge m_i-1\ge2\), contrary to the closure condition. Hence \(|t|<2\), so write \(t=2\cos\theta\) with \(0<\theta<\pi\). The recurrence becomes
\[
f_j=-\frac{\sin((j-1)\theta)}{\sin\theta}\quad(j\ge2).
\]
Closure is therefore equivalent to
\[
\sin((m_i-1)\theta)+\sin\theta
=2\sin(m_i\theta/2)\cos((m_i-2)\theta/2)=0.
\]
If the first factor vanishes, the recurrence gives \(f_{m_i-1}=t\); if the second vanishes, it gives \(f_{m_i-1}=0\). Thus, for each petal, the coordinate adjacent to the hub on the other side belongs to \(\{0,th\}\). Let \(s\) be the number of petals contributing \(th\), with \(0\le s\le k\). At the hub, whose degree is \(2k\), the eigenvalue equation reads
\[
(2k-\lambda)h=s\,th,
\qquad\text{or}\qquad
2(k-1)=(s-1)t.
\]
For \(s=0\), this forces \(t=-2(k-1)\le-2\); for \(s=1\), it forces \(2(k-1)=0\); and for \(2\le s\le k\), it forces \(t=2(k-1)/(s-1)\ge2\). All contradict \(k\ge2\) and \(|t|<2\). Therefore no nonzero eigenvector vanishes on \(T_*\), and the PBH criterion proves controllability. Together with the lower bound, \(\gamma(G)=k\).

**Exact ordinary zero forcing.** If no vertex other than the hub is initially blue on some petal, then that petal can never receive its first nonhub blue vertex: the hub faces two white neighbors there and cannot force either. Consequently any zero-forcing set contains at least one nonhub vertex on each petal. A set of exactly \(k\) blue vertices would have exactly one such vertex per petal and a white hub. Every initially blue vertex then has both its cycle neighbors white, so no force can start. Thus \(Z(G)\ge k+1\). Conversely, color the hub and \(v_{i,1}\) on every petal blue. Every \(v_{i,1}\) has the hub blue and can force \(v_{i,2}\); successive vertices force along each cycle until all vertices are blue. Hence \(Z(G)\le k+1\), completing the proof.

## Verification
The standalone standard-library program `verify_bouquet.py` constructs exact integer Laplacians and tests the stated actuator choices by modular Kalman-rank elimination. Full modular rank implies full rank over the rationals for these tested instances. It also checks the zero-forcing construction and exhaustively rejects every \((k-1)\)-vertex zero-forcing candidate across the enumerated small graphs. Running `python3 verify_bouquet.py` produced: `PASS: 4595 exact modular-rank/forcing checks across 50 bouquets`. These finite tests corroborate but do not establish the infinite-family theorem, which is proved above.

## Relationship to prior work
Parlangeli and Notarstefano established Laplacian reachability/observability criteria for individual path and cycle graphs, including a two-adjacent-vertex cycle construction; their arXiv version 1 became public on 2011-09-16 [1]. Notarstefano and Parlangeli subsequently treated Cartesian grid graphs [2]. Neither covers arbitrary bouquets joined at one articulation hub, and cycle-by-cycle reasoning alone does not settle PBH modes coupled at that hub. General critical-eigenvector leader-selection machinery [3] supplies a framework, but does not itself supply the present explicit heterogeneous-bouquet minimum or placement. Standard zero-forcing sufficiency [4] gives a \((k+1)\)-vertex certificate but misses this exact fixed-unit-Laplacian optimum by one. The special-case identity \(Z(F_k)=k+1\) for all-triangle friendship graphs also appears in an earlier zero-forcing-polynomial classification; the present theorem does not claim that isolated identity as new.

Related work titled *Controllability of multiagent systems based on path and cycle graphs* [5] describes other derived graph families in its abstract; its uninspected full text leaves possible overlap unresolved. Work specifically titled *Observability of Friendship Networks* [6] addresses the all-triangle subclass and must not be treated as absent or irrelevant, although its full text was not accessible for comparison. Similarly, *Controllability of Windmill Networks* [7] may concern the all-triangle/complete-clique subclasses; its full text was not accessible. The present claim is for **every** choice of \(k\ge2\) and heterogeneous lengths \(m_i\ge3\), not a claim that the friendship-graph case has no antecedent.

## Limitations
The result may fail under arbitrary nonuniform edge weights, when extra cross-petal edges are added, or if all actuators share one scalar input. It is an exact-controllability/observability classification, not a statement about control energy, Gramian conditioning, robustness to edge perturbations, or strong structural controllability. Unexamined closely relevant full texts [5]–[7] and unindexed results create a genuine prior-coverage risk. Zero forcing is a sufficient structural criterion, not a necessary criterion for controllability of this fixed Laplacian.

## References
[1] G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (2011-09-16), https://arxiv.org/pdf/1109.3556.

[2] G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1 (2012-03-01), https://arxiv.org/pdf/1203.0129.

[3] L. Dai et al., *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications (2023), DOI:10.1049/cth2.12385.

[4] N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, IEEE Transactions on Automatic Control 59 (2014), 2562–2567.

[5] X. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, International Journal of Robust and Nonlinear Control (first online 2017-06-30), DOI:10.1002/rnc.3870.

[6] T. Dong et al., *Observability of Friendship Networks*, IEEE iThings/GreenCom/CPSCom/SmartData/Cybermatics (2023), DOI:10.1109/iThings-GreenCom-CPSCom-SmartData-Cybermatics60724.2023.00042.

[7] P. Guo et al., *Controllability of Windmill Networks*, Bio-Inspired Computing: Theories and Applications (2024), DOI:10.1007/978-981-97-2275-4_16.
