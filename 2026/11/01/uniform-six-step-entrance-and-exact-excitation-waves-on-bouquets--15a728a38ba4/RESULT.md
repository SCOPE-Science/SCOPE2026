# Uniform six-step entrance and exact excitation waves on bouquets of squares

## Finding

For each integer \(k\ge1\), form the labelled square bouquet \(B_k\) from the vertices \(h,a_i,b_i,c_i\) for \(1\le i\le k\), with edges \(ha_i,a_ib_i,b_ic_i,c_ih\) and no others. In synchronous three-state threshold-one Greenberg–Hastings dynamics, \(0\) becomes \(1\) precisely when an adjacent vertex is \(1\); otherwise it remains \(0\). Both nonresting states advance automatically, \(1\to2\to0\). Let \(F\) denote one simultaneous update.

**Theorem.** For every \(k\ge1\),
\[
F^{10}=F^6,
\qquad N_{1}(k)=1,
\qquad N_{4}(k)=3^k-1.
\]
Here \(N_d(k)\) counts primitive temporal orbits of length \(d\) under the labelled state map; no other primitive periods occur. The unique fixed state is all zero. The fixed-point and four-cycle attraction basins have exactly
\[
B_{1}(k)=3\cdot19^k,\qquad B_{4}(k)=3(27^k-19^k)
\]
initial states, respectively. Under uniformly independent colors, the chance of eventual oscillation is \(1-(19/27)^k\). If \(T(x)\) is the first nonnegative update time at which \(F^{T(x)}(x)\) belongs to its eventual periodic orbit, then
\[
\max_{x}T(x)=\begin{cases}4,&k=1,\\6,&k\ge2.\end{cases}
\]
All counts concern labelled vertices, with temporal rotations identified for the orbit count; graph automorphisms are not identified.

## Assumptions and scope

There is exactly one common hub; distinct square petals do not share other vertices or edges. The graph has \(3k+1\) vertices and \(4k\) edges. The model has exactly three states, synchronous updates, no spontaneous firing, threshold one, and a refractory state lasting one update. The theorem holds for every positive integer \(k\), with no asymptotic extrapolation from small instances.

## Proof

**1. An all-size finite-trace lemma.** For a hub state \(h\in\{0,1,2\}\) and one petal triple \((a,b,c)\), define
\[
\psi_h(a,b,c)=\bigl(f(a,[h=1\lor b=1]),\ f(b,[a=1\lor c=1]),\ f(c,[b=1\lor h=1])\bigr),
\]
where \(f(1,z)=2\), \(f(2,z)=0\), and \(f(0,z)=1\) for true \(z\), otherwise \(0\). The hub follows \(1\to2\to0\); when resting, it advances if and only if some petal has its first or third vertex excited.

Consider an arbitrary proposed hub word \((h_0,\ldots,h_{10})\) respecting these intrinsic transitions, allowing both choices after \(h_t=0\). For each of the \(27\) possible initial petal triples, the word uniquely determines its entire local trajectory through time ten. Discard any triple that would excite the hub at a time when the proposed word keeps the hub at zero. Feasibility further requires that every proposed zero-to-one hub transition be supported by at least one remaining triple. Enumerating these elementary finite conditions leaves **exactly twelve** candidate hub words:

`00000000000`, `00120000000`, `00120012001`, `01200000000`, `01200120012`, `12000000000`, `12001200120`, `12012001200`, `20000000000`, `20012001200`, `20120000000`, `20120012001`.

For each of these twelve words, \(h_6=h_{10}\), and **every** permitted petal triple has the same local state at times six and ten. This checks all possible initial types and all feasible hub stimuli, not merely a fixed number of petals. Consequently every configuration of every \(B_k\) satisfies \(F^{10}(x)=F^6(x)\). The entirely executable `finite_certificate.py` reconstructs the twelve-word filter and all \(27\)-type trajectories from the update equations; `finite_certificate_output.txt` records all twelve type counts. Thus time six is periodic, with period dividing four.

**2. Primitive periodic states.** Since the graph has no isolated vertices and the states \(1\) and \(2\) advance automatically, all zero is the only fixed point. A nonzero period-two trajectory is impossible because a vertex that fires must next traverse states \(2\) and \(0\) before firing again. In a nonzero periodic trajectory on a connected graph, every vertex must fire: a permanently zero vertex adjacent to a firing vertex would be excited. Therefore any nonzero recurrent trajectory, whose period divides four by step 1, has primitive period exactly four, and every vertex fires exactly once per four steps.

Assign each vertex its unique excitation phase in \(\mathbb Z/4\mathbb Z\). Its neighborhood must contain a vertex in the preceding phase, while an adjacent vertex in the opposite phase would cause premature excitation and is forbidden. Set the hub phase to zero. Directly enforcing these two constraints at the three non-hub vertices of a square leaves precisely the petal phase profiles \((1,2,1)\), \((1,2,3)\), and \((3,2,1)\), where the listed entries are the phases of \((a_i,b_i,c_i)\). The hub needs a neighbor in phase three; the latter two profiles supply one, while the first does not. Hence all \(3^k\) assignments except the all-first-profile assignment are valid. Each primitive orbit has precisely one state in which the hub fires, so the number of primitive four-orbits is \(3^k-1\), as claimed. These profiles are also verified exhaustively in `finite_certificate.py`.

**3. Basins from an invariant local circulation.** On an oriented edge, define
\[
\delta(x,y)=\mathbf1_{\{x=0,\ y=1\}}-\mathbf1_{\{x=1,\ y=0\}},
\qquad W_i(x)=\delta(h,a_i)+\delta(a_i,b_i)+\delta(b_i,c_i)+\delta(c_i,h).
\]
Direct substitution of the three-state update on a single square gives \(W_i(Fx)=W_i(x)\), regardless of the other petals. For rigor, the finite certificate checks all \(81\) local four-vertex states and **all** hub successors possible in a larger bouquet, making \(93\) individual successor cases. Each local circulation lies in \(\{-1,0,1\}\). For each fixed hub color exactly \(19\) of the \(27\) petal color triples have circulation zero, and four each have circulation \(-1\) and \(+1\).

The all-zero fixed point has every circulation zero. Conversely, in any primitive four-cycle at least one petal has a spinning profile \((1,2,3)\) or \((3,2,1)\), whose circulation is nonzero. Conservation and the recurrence classification thus show that an initial configuration reaches zero **if and only if** all its petal circulations are zero. There are three choices for the hub color and independently \(19\) admissible triples per petal. Therefore the extinction basin has \(3\cdot19^k\) states. The total number of configurations is \(3^{3k+1}=3\cdot27^k\); subtraction gives the four-cycle basin count.

**4. Sharp entrance times.** Step 1 gives the universal upper bound six. For one square, exhaustive verification of all \(81\) states gives \(F^8=F^4\), hence entrance within four updates; the initial tuple \((h,a_1,b_1,c_1)=(0,0,0,1)\) first reaches zero at time four. For two petals, the initial tuple \((h,a_1,b_1,c_1,a_2,b_2,c_2)=(0,0,0,0,0,1,0)\) first reaches zero at time six. For every \(k>2\), duplicate the first petal's initial triple \((0,0,0)\): identical petals receive the same hub input, so their extra contributions cannot change the hub's Boolean OR stimulus. The two-petal trace is preserved and the sharp entrance time remains six.

## Verification

The `finite_certificate.py` implementation enumerates only a universal finite local state space, rather than truncating the parameter \(k\). Its output verifies the twelve feasible hub words, their permitted petal counts, all local circulation transitions, the three phase profiles, one-petal exact periodization, and sharp witnesses. The independent `full_state_census.cpp` implementation exhaustively iterates all \(3^{3k+1}\) labelled global configurations for \(1\le k\le4\), computes the functional graph of the update and its attraction basins, and reports agreement with every formula; these four checks include exactly \(1,655,640\) distinct initial configurations in total. Reproduction: `python3 finite_certificate.py`; `g++ -std=c++17 -O3 full_state_census.cpp -o full_state_census && ./full_state_census`. The corresponding observed outputs are embedded. The all-size proof relies on the twelve-word universal certificate, not on extrapolation from \(k\le4\).

## Relationship to prior work

Garcia, Lesne, Hütt and Hilgetag (2012) study excitable three-state networks and individual triangular and square pacemakers, including embedded squares. Garcia, Lesne, Hilgetag and Hütt (2014) analyze cycle usage in excitable networks, chiefly through simulations and mean-field estimates. Gravner, Lyu and Sivakoff (2016), Theorem 3, give a general finite-graph circulation criterion for whether three-color Greenberg–Hastings dynamics eventually synchronizes. The present local-circulation extinction count can also be deduced by specializing that established criterion; the independent contribution here is the **explicit all-parameter recurrence classification**, the exact primitive four-orbit count, and the uniform sharp entrance-time law for the interacting square bouquet. The cited general theorem gives an activity-rate characterization but does not state the sharp identity \(F^{10}=F^6\) or count the bouquet's recurrent orbits.

## Limitations

The theorem is restricted to exactly four-cycle petals and three-state, threshold-one, simultaneous excitation; attaching other cycle lengths or changing thresholds can produce different periods. Labelled configurations are counted, without quotient by graph automorphisms. The finite certificate is an exhaustive finite case proof that depends on the specified local transition rule, not an externally certified formal proof. Novelty is qualified by the possibility of equivalent unindexed prior work. Independent mathematical audit has not been performed.

## References

1. G. C. Garcia, A. Lesne, M.-T. Hütt, and C. C. Hilgetag, “Building Blocks of Self-Sustained Activity in a Simple Deterministic Model of Excitable Neural Networks,” *Frontiers in Computational Neuroscience* **6**, 50 (2012), doi:10.3389/fncom.2012.00050. Public since 2012-08-06. https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2012.00050/full
2. G. C. Garcia, A. Lesne, C. C. Hilgetag, and M.-T. Hütt, “Role of long cycles in excitable dynamics on graphs,” *Physical Review E* **90**, 052805 (2014), doi:10.1103/PhysRevE.90.052805. Author-hosted OA full text: https://www.lptmc.jussieu.fr/user/lesne/Garcia-PRE-2014.pdf
3. J. Gravner, H. Lyu, and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” arXiv:1610.07320v1 (2016-10-24), Theorem 3. https://arxiv.org/pdf/1610.07320
