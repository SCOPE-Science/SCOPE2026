# Parity-selective periodic excitation on complete bipartite graphs

## Finding

Let \(q\ge3\) and \(a,b\ge1\) be integers. Consider synchronous \(q\)-state Greenberg–Hastings dynamics on the labelled loopless complete bipartite graph \(K_{a,b}\): an excited vertex has state \(1\), and each nonzero state advances by one modulo \(q\); a resting vertex of state \(0\) advances to \(1\) exactly when an opposite-part vertex has state \(1\), and otherwise remains \(0\). Put \(m=\lceil q/2\rceil\) and define the onto-map count
\[
 U_k(n)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k-j)^n=k!\,\left\{\begin{matrix}n\\k\end{matrix}\right\}.
\]
Every state eventually enters exactly one of the following three disjoint periodic families:

1. The all-rest fixed configuration (exact period \(1\)).
2. Uniform phase-rotation configurations of exact period \(q\), with every one of the \(q\) states represented in **each** vertex part. There are exactly \(U_q(a)U_q(b)\) such labelled states.
3. Alternating-activity configurations of exact period \(2m\), with each part surjecting onto its corresponding \(m\)-element phase palette defined below. There are exactly \(2U_m(a)U_m(b)\) such labelled states.

Thus the total number of periodic configurations is
\[
 R_q(a,b)=1+U_q(a)U_q(b)+2U_m(a)U_m(b),
\]
and the Artin–Mazur dynamical zeta function is
\[
 \zeta_F(z)=\frac{1}{(1-z)(1-z^q)^{U_q(a)U_q(b)/q}
 (1-z^{2m})^{U_m(a)U_m(b)/m}}.
\]
When \(q\) is even, the two nontrivial families have the *same* exact period \(q=2m\) but are disjoint. When \(q\) is odd, their periods are \(q\) and \(q+1\). The alternating family exists if and only if \(\min(a,b)\ge m\); the full-rotation family exists if and only if \(\min(a,b)\ge q\). If \(\min(a,b)<m\), every initial configuration eventually becomes all-rest. For each fixed \(q\), the fraction of states that are already periodic on \(K_{n,n}\) tends to \(1\) as \(n\to\infty\), while the alternating-family fraction is asymptotic to \(2(m/q)^{2n}\).

## Assumptions and scope

Vertices are labelled, updates are simultaneous, and each part is nonempty. There is no self-interaction and the threshold is one excited neighbour. The period of a configuration is the least positive return time under the full synchronous map. The two nontrivial families are *periodic states*, not necessarily basins of attraction; no transient-depth enumeration is claimed. For even \(q\), add the two contributions to obtain the total number of states of exact period \(q\). For odd \(q\), the contributions belong to different exact periods.

Write \(A_t\) and \(B_t\) for the sets of colors occupied by their respective parts at integer time \(t\). A configuration is recurrent exactly when it lies on a finite deterministic periodic orbit. On such an orbit, times may be indexed by all integers.

## Proof

**1. Rigidity of the global excitation signals.** Let \(e_A(t)=\mathbf1_{\{1\in A_t\}}\) and define \(e_B\) analogously. For \(q\ge3\), an excited vertex at time \(t\) must have been resting and have received stimulation at time \(t-1\). Consequently, on any periodic orbit,
\[
 e_A(t)\le e_B(t-1)\le e_A(t-2).
\]
The time series is periodic. Summing this inequality over an entire time period forces equality of all three terms at every time. Hence \(e_A(t)=e_B(t-1)=e_A(t-2)\), and similarly \(e_B(t)=e_A(t-1)=e_B(t-2)\). The only possibilities are: both parts excited at every time, or the two parts excited on complementary time parities, or neither ever excited. In the last case, all nonzero colors decay to zero within at most \(q-1\) steps, so periodicity forces the all-rest fixed point.

**2. Excitation at every time.** A resting vertex sees an excited neighbour every time, so every vertex advances by exactly one modulo \(q\) each step. Such a part sends an excitation at every time if and only if its initial assignment includes each of the \(q\) colors. This proves the full-rotation characterization, exact period \(q\), and its labelled count \(U_q(a)U_q(b)\).

**3. Alternating excitation.** By shifting the time origin if necessary, suppose \(e_B(t)=1\) at even times and \(e_A(t)=1\) at odd times. A vertex in the first part receives a periodic external drive of \(1,0,1,0,\ldots\); a vertex in the other part receives \(0,1,0,1,\ldots\). For a single vertex put
\[
 f_1(0)=1,\quad f_0(0)=0,\qquad f_0(x)=f_1(x)=x+1\pmod q\quad(1\le x\le q-1).
\]
At even times the two-step return maps are \(G=f_0\circ f_1\) for the first part and \(H=f_1\circ f_0\) for the second. Directly,
\[
 G(x)=\begin{cases}x+2,&0\le x\le q-3,\\0,&x=q-2\text{ or }q-1,\end{cases}
\]
and
\[
 H(x)=\begin{cases}1,&x=0\text{ or }q-1,\\x+2,&1\le x\le q-3,\\0,&x=q-2.\end{cases}
\]
The unique periodic cycle of \(G\) is
\[
 E_q=\{0,2,4,\ldots,2m-2\},
\]
and the unique periodic cycle of \(H\) is
\[
 O_q=\begin{cases}
 \{1,3,\ldots,q-1\},&q\text{ even},\\
 \{0,1,3,\ldots,q-2\},&q\text{ odd}.
 \end{cases}
\]
Each has exactly \(m\) points. Every other scalar state eventually enters the relevant cycle but cannot itself be periodic for the two-step forced dynamics. Each member of either cycle visits the excited state exactly once in \(2m\) single updates. To sustain the prescribed alternating excitation *at every appropriate time*, all \(m\) cycle phases must be occupied in **each** part. Thus the first part has occupied palette exactly \(E_q\), and the second exactly \(O_q\), with every palette color represented. Conversely, any such pair of onto assignments perpetuates the assumed alternating signals. Interchanging the parts gives the second, disjoint orientation. Each vertex has exact period \(2m\): when \(q\) is even it visits all \(q\) colors once, whereas when \(q\) is odd it visits nonzero colors once and the resting color twice. In both cases the full configuration therefore has exact period \(2m\). This gives \(2U_m(a)U_m(b)\) labelled configurations.

**4. Counts, thresholds, and zeta function.** A map from \(n\) labelled vertices onto a prescribed \(k\)-color palette is counted by inclusion–exclusion as \(U_k(n)\), which vanishes for \(n<k\). Families in the previous steps are disjoint because \(m<q\). Every deterministic orbit on the finite configuration space becomes periodic, so the classification is exhaustive. The numbers of primitive orbits are \(U_q(a)U_q(b)/q\) for the full-rotation family and \(U_m(a)U_m(b)/m\) for the alternating family. The zeta expression follows from the periodic-orbit Euler product. For fixed \(q\), \(U_q(n)/q^n\to1\) by the coupon-collector union bound; similarly \(U_m(n)/m^n\to1\). Substituting in \(R_q(n,n)/q^{2n}\) proves both asymptotic statements.

## Verification

The standalone script `verify_gh_multicolor.py` independently constructs the complete functional graph for \(73\) triples of parameters with \(3\le q\le7\) and tests \(951316\) labelled configurations in total. It compares *all* detected periodic points and their exact periods with the theorem, rather than assuming the predicted period bound. It separately checks forced scalar return maps for every \(3\le q\le64\) and direct alternating-orbit witnesses for \(7\le q\le15\). The recorded output is in `CHECKS.txt`. These finite tests corroborate the theorem; the all-parameter proof is the preceding analytic argument, not extrapolation from tests.

For examples, \(q=5\) and \(a=b=3\) give exactly \(72\) periodic configurations of exact period \(6\) in addition to all-rest, whereas \(q=4\) and \(a=b=4\) give \(968\) nontrivial periodic configurations, all of exact period \(4\).

## Relationship to prior work

Greenberg and Hastings introduced the excitable-media rule in 1978. Durrett and Griffeath (public arXiv preprint dated 22 March 1993) treat multicolor Greenberg–Hastings dynamics and lattice-scale spiral/threshold behavior, not this exact complete-bipartite state census. Gravner, Lyu and Sivakoff (arXiv 1610.07320, first posted 24 October 2016) prove a general circulation criterion and activity statements for **three** colors on finite graphs; their Theorem 3 and the definitions on pages 2–4 do not supply the arbitrary-color bipartite recurrence and parity count above. In the special three-color case, complete-bipartite orbit classifications are already known; the contribution here is the uniform proof for all \(q\ge3\), in particular the sharp \(\lceil q/2\rceil\)-vertex excitation threshold and the even/odd phase-return dichotomy. A published indexing search found no stronger formula implying the stated all-color zeta function. Lack of a match is not a uniqueness certificate.

## Limitations

The result covers only deterministic synchronous threshold-one Greenberg–Hastings dynamics on complete bipartite graphs with positive part sizes, not other graph families, higher thresholds, asynchronous updates, or the distribution of transient lengths and basins. The multicolor proof has not received an independent audit. The literature assessment is necessarily bounded: an unpublished or unindexed equivalent could exist, and some original historical journal texts were not inspected in their complete publisher representation. The cited arXiv 2016 paper was read at the level of its definitions and theorems and does not assert a multicolor analogue of its three-color circulation formula.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523, DOI: 10.1137/0134040.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics 2 (1993), 183–208; arXiv: patt-sol/9303002 (first public preprint dated 1993-03-22), DOI: 10.1080/10586458.1993.10504277.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320 (posted 2016-10-24), Annals of Applied Probability 28 (2018), 3324–3357.
