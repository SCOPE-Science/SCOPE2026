# A sharp one-vacancy exception for noncollision conditioning on weighted graphs

## Finding
Let \(G=(V,E)\) be a finite connected simple undirected graph with \(n=|V|\ge4\). Give each oriented edge \(i\to j\) a strictly positive continuous-time jump rate \(q_{ij}\); rates are zero on nonedges, and opposite directions need not agree. Take \(k\) labeled independent walkers, \(2\le k\le n-1\), from distinct sites. Write \(\tau\) for their first collision, \(\mathbb P^{\mathrm{Ex}}_x\) for the process suppressing collision-causing jumps, and \(\mathbb P^{\mathrm{NC}}_x\) for the process obtained by conditioning on \(\tau>T\) and then taking \(T\to\infty\) on every bounded path horizon.

Put \(s_{ij}=q_{ij}+q_{ji}\) for edges and \(s_{ij}=0\) for nonedges, and \(d_i=\sum_{j\ne i}s_{ij}\). The following conditions are equivalent for each fixed \(k\):

1. \(\mathbb P^{\mathrm{NC}}_x=\mathbb P^{\mathrm{Ex}}_x\) as full path laws for **some** distinct-coordinate initial state \(x\).
2. The same equality holds for every distinct-coordinate initial state.
3. For every \(T>0\), conditioning the independent-walker path on \(\tau>T\) gives the exclusion-process path law on \([0,T]\), for every initial state.
4. The probability \(\mathbb P_x(\tau>T_0)\) has the same value for every distinct-coordinate initial state for **one** fixed \(T_0>0\).
5. The total collision hazard \(\kappa(A)=\sum_{\{i,j\}\subset A}s_{ij}\) is constant over the \(k\)-element occupied subsets \(A\subset V\).
6. Precisely the following graph/rate criterion holds:
   - if \(2\le k\le n-2\), then \(G\) is complete and \(s_{ij}=s>0\) is the same number for all distinct \(i,j\);
   - if \(k=n-1\), then the symmetrized weighted degrees \(d_i\) are equal for all \(i\), with no completeness requirement.

In these cases \(\tau\) is exponential, with rate \(\lambda_k=\binom{k}{2}s\) in the first case and \(\lambda_{n-1}=(n-2)d/2\) in the second. More strongly, the entire killed process before collision has the law of the exclusion process stopped at an **independent** exponential time of rate \(\lambda_k\).

In particular, every connected regular sparse graph with equal symmetric edge rates has equality of noncolliding and exclusion dynamics with exactly one vacancy, but has *inequality* for every particle count from \(2\) through \(n-2\). On a cyclic graph with clockwise rate \(a>0\) and anticlockwise rate \(b>0\), the one-vacancy collision rate is \((n-2)(a+b)\), even if \(a\ne b\).

## Assumptions and scope
Time is continuous and each walker has the generator specified by \(q_{ij}\). The graph is finite, connected, undirected as an edge set, and every edge has strictly positive rates in **both** directions. The walkers are labeled, and collisions occur when a jump arrives at another walker's occupied site; simultaneous jumps have probability zero. The exclusion process is the continuous-time Markov chain on injective tuples that keeps all allowed jump rates \(q_{ij}\) and suppresses jumps into occupied sites without changing the rates of allowed jumps. There are at least two particles and at least one vacancy. All quantified equalities are exact identities of laws, not asymptotic approximations.

The assumptions do not require reversibility, spatial homogeneity, a stationary initial distribution, or equality of directional rates. The noncollision-conditioned process exists for each initial tuple: the killed chain restricted to its finite communicating component is irreducible, so its positive Perron eigenfunction gives the limiting conditioned process.

## Proof
**1. Generator identity and irreducibility.** Let \(\Omega_k\) be the set of injective ordered \(k\)-tuples. Denote the exclusion generator by \(L\), and the killed independent-walker generator on \(\Omega_k\) by \(K\). For a configuration \(x\) with occupied set \(A\), every collision-causing transition consists of an occupied \(i\to j\) with both \(i,j\in A\). Therefore its aggregate killing rate is
\[
\kappa(A)=\sum_{\{i,j\}\subset A}(q_{ij}+q_{ji}),
\qquad K=L-\operatorname{diag}(\kappa).
\]
Because both directional rates on each graph edge are positive, each communicating component of the labeled exclusion chain is irreducible. The graph of *unlabeled* \(k\)-element occupied subsets is connected: adjacent swaps of occupied and unoccupied symbols along the edges of any spanning tree generate all binary arrangements with \(k\) occupied sites. Moreover, any such unlabeled path lifts to a labeled exclusion path by moving the label located at the departure site. Hence **every** labeled communicating component projects onto **every** \(k\)-element subset \(A\).

**2. The constant-hazard direction.** If \(\kappa(A)\equiv\lambda\), then \(K=L-\lambda I\), and thus
\[
e^{tK}=e^{-\lambda t}e^{tL}.
\]
In particular, \(\mathbb P_x(\tau>t)=e^{-\lambda t}\). The killed-path measure on any time interval \([0,t]\) is exactly \(e^{-\lambda t}\) times the exclusion path measure. It follows by the Markov property that, for every \(T>0\), the independent-walker process conditional on \(\tau>T\) agrees on \([0,T]\) with exclusion. This proves (5) implies (3), (2), (1), and (4). The semigroup factorization also constructs the killed law by killing an independent exclusion trajectory at an independent \(\operatorname{Exp}(\lambda)\) time.

**3. Equality for one initial state forces constant hazard.** On any labeled component \(C\), the irreducible substochastic generator \(K_C\) has a strictly positive Perron right eigenfunction \(h_C\) and eigenvalue \(-\alpha_C\). Its long-survival conditioned generator has off-diagonal rates
\[
L^{\mathrm{NC}}(x,y)=L(x,y)\frac{h_C(y)}{h_C(x)}
\quad (x,y\in C,\ x\ne y).
\]
If the conditioned process and exclusion have the same full path law from one starting state, their transition rates agree in every reachable state of \(C\). Since all permitted edges have positive rates, \(h_C(y)=h_C(x)\) across every permitted transition, and irreducibility makes \(h_C\) constant on \(C\). The eigenfunction equation \(K_Ch_C=-\alpha_Ch_C\) then yields \(\kappa(A)=\alpha_C\) for the occupied set \(A\) of every configuration in \(C\). By the projection fact in Step 1, \(A\) ranges over all \(k\)-subsets, proving (1) implies (5).

**4. A single survival horizon is enough.** Suppose (4) holds. On a labeled component \(C\), the strictly positive matrix \(e^{T_0K_C}\) maps the all-ones vector to the same positive scalar multiple \(c\) of itself. By Perron--Frobenius its eigenvalue \(c\) is simple and its positive eigenvector is the all-ones vector. Because \(K_C\) commutes with \(e^{T_0K_C}\), the vector \(K_C\mathbf1\) must be a scalar multiple of \(\mathbf1\). But \(K_C\mathbf1=-\kappa\) coordinatewise, so \(\kappa\) is constant on that component. Projection to all occupied subsets again shows it is constant globally. Thus (4) implies (5); this argument needs equality of the survival probability over *all* initial states, not merely over one component.

**5. Classification of constant subset hazards.** If \(k=n-1\), the occupied set is \(V\setminus\{v\}\). With \(W=\sum_{\{i,j\}\subset V}s_{ij}\),
\[
\kappa(V\setminus\{v\})=W-d_v.
\]
Consequently it is constant exactly when all \(d_v\) coincide. In that case \(W=nd/2\), giving \(\lambda_{n-1}=(n-2)d/2\).

Now let \(2\le k\le n-2\). Fix distinct vertices \(a,b\) and compare the subsets \(S\cup\{a\}\) and \(S\cup\{b\}\) for each \(S\subset V\setminus\{a,b\}\) of size \(k-1\). Equality of hazards gives
\[
\sum_{j\in S}(s_{aj}-s_{bj})=0.
\]
Since \(1\le k-1\le n-3\), equality of all these fixed-size subset sums implies their \(n-2\) summands are individually zero: exchange any two elements of \(S\) to see the summands are equal, then use their zero sum. Therefore \(s_{aj}=s_{bj}\) for every pairwise distinct \(a,b,j\). Symmetry \(s_{ij}=s_{ji}\) then forces one common value for **all** unordered vertex pairs. Connectivity and strictly positive rates on graph edges make this common value positive, so there can be no missing edge: \(G\) is complete. Conversely uniform positive pair sums yield \(\kappa(A)=\binom{k}{2}s\). This proves the classification and all equivalences.

**6. Sharp density exception.** On \(C_n\), with \(n\ge4\), clockwise rate \(a>0\) and anticlockwise rate \(b>0\), each edge has \(s=a+b\), every symmetrized degree is \(d=2(a+b)\), and the graph is not complete. Step 5 gives equality only at \(k=n-1\), with rate \((n-2)(a+b)\). Hence equality at maximal nontrivial occupancy does **not** imply equality even at the immediately lower particle count. The example also permits irreversible circulation when \(a\ne b\).

## Verification
Run `python3 verify.py` in the directory containing this file. The standalone program uses only the Python standard library and exact rational arithmetic. It tests \(117816\) finite classification assertions across randomly generated complete-graph rates, **all** connected unweighted simple graphs on \(3\) through \(6\) vertices, and weighted cycle examples through \(12\) vertices. It also checks the killed-versus-exclusion diagonal identity for \(24\)-state labeled configurations of a four-vertex graph and explicitly tests that three-particle equality can coexist with two-particle inequality.

These finite computations check algebra and examples, not the theorems for arbitrary finite \(n\). The proof of all-\(n\) statements is in Steps 1--6.

## Relationship to prior work
Shiatis (2026), *Exclusion vs Noncolliding dynamics in Markov processes*, derives the general martingale-density relation between exclusion and noncollision conditioning, involving a Perron eigenfunction and the collision hazard. Its Theorem 1.4 and Sections 1.3, 2 are the closest direct predecessor. The present classification applies this framework to a different question: **when the two laws are exactly identical**, as determined by the underlying weighted graph and occupancy count. The complete-versus-regular dichotomy, its necessity, the single-horizon survival test, and the one-vacancy sparse-graph exception are not stated as an all-graph classification in that paper.

Johnston and Shiatis (2025), *The integrable snake model*, studies ASEP on a ring and a traffic change of measure; the one-vacancy cyclic example here is compatible with that specialization. The result here treats arbitrary connected finite bidirectional graphs and spatially heterogeneous, potentially nonreversible jump rates, and classifies the entire occupancy range. It does not claim that the underlying Doob-transform construction or the fact that constant killing is independent exponential killing is new.

## Limitations
Strictly positive rates in both directions of every graph edge are essential to the connectivity and necessity arguments. No classification is asserted for genuinely one-way digraphs, infinite graphs, a fully occupied system, or non-Markov holding times. The proof uses finite-state spectral and combinatorial reasoning. Published equivalent formulations using Q-processes, killing, or token graphs may exist without the same particle interpretation; the novelty assessment is necessarily provisional. The cyclic one-vacancy specialization overlaps established ring models and is supplied as a sharpness illustration, not separately claimed as new.

## References
1. R. Shiatis, *Exclusion vs Noncolliding dynamics in Markov processes*, arXiv:2610.00741v1 (first public version 30 September 2026), https://arxiv.org/html/2610.00741v1 . In particular Theorem 1.4 and Sections 1.3, 2.
2. S. G. G. Johnston and R. Shiatis, *The Integrable Snake Model*, arXiv:2501.15483v4 (2025), https://arxiv.org/html/2501.15483v4 . In particular Section 7 (traffic representation for ASEP on a ring).
3. S. D. Jacka and G. O. Roberts, *Weak convergence of conditioned processes on a countable state space*, Journal of Applied Probability 32 (1995), 902--916; cited in Shiatis (2026) for asymptotic conditioned laws.
