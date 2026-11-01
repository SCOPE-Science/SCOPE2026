# Square-conjugate open-NOR dynamics and Fibonacci preimage basins on paths

## Finding

Let \(G=(V,E)\) be any finite simple undirected **bipartite** graph, and let \(F\) be synchronous **open-neighborhood NOR**: an initially active vertex set \(S\subseteq V\) is updated to
\[
 F(S)=\{v\in V:N_G(v)\cap S=\varnothing\}.
\]
The current vertex's state is **not** included among its inputs. If \(m(G)\) denotes the number of maximal independent vertex sets of \(G\), then the subsystem consisting of all recurrent configurations is conjugate to the coordinate swap on a square of size \(m(G)\). In particular, there are exactly \(m(G)^2\) recurrent configurations, exactly \(m(G)\) fixed configurations, and exactly \(\binom{m(G)}2\) distinct primitive two-cycle orbits. Every trajectory is periodic after at most one update.

For the path \(P_n\), \(n\ge2\), a further **individual-fiber formula** gives the complete attraction basin of every fixed point and every two-cycle using only the binary run lengths of the two parity subsequences. Define Fibonacci numbers \(\mathcal F_0=0\), \(\mathcal F_1=1\), and \(\mathcal F_{j+2}=\mathcal F_{j+1}+\mathcal F_j\). For a binary word \(w\) of length \(k\) and endpoint-stub flags \(\ell,r\in\{0,1\}\), put
\[
 W_{\ell,r}(w)=\prod_{[i,j]\,\mathrm{maximal\ zero\ run\ of}\,w}
 \mathcal F_{j-i+2\ell\mathbf{1}_{i=1}+2r\mathbf{1}_{j=k}}.
\]
An empty product is one; a factor \(\mathcal F_0\) is zero. For an output word \(s=(s_1,\ldots,s_n)\), let \(a=(s_1,s_3,\ldots)\) and \(b=(s_2,s_4,\ldots)\). Its **exact number of predecessors**, including outputs with no predecessors, is
\[
 p_n(s):=|F^{-1}(\{s\})|=
 \begin{cases}
 W_{0,1}(a)W_{1,0}(b),&n\text{ even},\\
 W_{0,0}(a)W_{1,1}(b),&n\text{ odd}.
 \end{cases}
\]
For a fixed attractor \(\{s\}\), its basin has size \(p_n(s)\). For a two-cycle \(\{s,F(s)\}\), its basin has size \(p_n(s)+p_n(F(s))\). These are **complete** individual-basin formulas for every \(n\ge2\); they are not limited to an attractor census.

## Assumptions and scope

All graphs are finite, simple, undirected and loopless; the general square conjugacy assumes bipartiteness, including possible isolated vertices. No randomness or asynchronous updating is imposed. Each vertex tests its *open* neighborhood, not its closed neighborhood. A recurrent configuration means a periodic state (not merely eventually periodic); a basin consists of all initial states whose eventual orbit is the specified attractor, including the attractor itself. The path \(P_n\) has the usual edges between consecutive vertices \(1,\ldots,n\).

The image of \(F\) is the recurrent set. Since the dynamics becomes involutive on that image, no deeper transient tree is present. The path-basin evaluation is \(O(n)\) arithmetic operations per orbit, independent of exhaustive enumeration of its \(2^n\) initial states.

## Proof

**1. Antitone bipartite polarity.** Write \(V=A\sqcup B\), and regard any state as \((X,Y)\) with \(X\subseteq A\), \(Y\subseteq B\). Define
\[
 f(X)=\{b\in B:N(b)\cap X=\varnothing\},\quad
 g(Y)=\{a\in A:N(a)\cap Y=\varnothing\}.
\]
Then \(Y\subseteq f(X)\) holds if and only if \(X\subseteq g(Y)\). Consequently \(gf\) and \(fg\) are extensive idempotent closure operators, and \(fgf=f\), \(gfg=g\). The NOR map is
\[
 F(X,Y)=(g(Y),f(X)).
\]
Its image is exactly \(C_A\times C_B\), with \(C_A=\operatorname{im}g\) and \(C_B=\operatorname{im}f\), because its two input coordinates are independent. The restrictions of \(f\) and \(g\) are mutual inverses between \(C_A\) and \(C_B\). On that image,
\[
 F^2(X,Y)=(gf(X),fg(Y))=(X,Y).
\]
Furthermore, \(C_A\times C_B\to C_A\times C_A\), \((X,Y)\mapsto(X,g(Y))\), conjugates \(F\) to the swap of coordinates. In particular \(F^3=F\) on all states.

**2. Fixed configurations and maximal independent sets.** A state \((X,Y)\) is fixed precisely when \(Y=f(X)\) and \(X=g(Y)\). This says that \(X\cup Y\) is independent and that every vertex outside it has an active neighbor; equivalently it is maximal independent. Conversely each maximal independent set satisfies the equalities. Thus \(|C_A|\), the number of fixed points of the swap, is \(m(G)\). Counting ordered pairs in \(C_A^2\) yields \(m(G)^2\) periodic points and \((m(G)^2-m(G))/2\) primitive two-cycles. This argument includes isolates without exception.

**3. Paths and the parity-factorization of predecessors.** For \(P_n\), the NOR values at odd sites depend only on *even* input sites and vice versa. Between consecutive output sites of one parity lies one input site; at the appropriate physical endpoints there may be an additional input site adjacent only to the first or last site of that parity. For even \(n=2m\), the odd output sequence has a right endpoint stub but not a left stub, and the even output sequence has a left but not a right stub. For odd \(n=2m+1\), the odd output sequence has no stubs and the even output sequence has both stubs.

In one parity sequence, an output one forces all incident input bits to zero, and an output zero requires at least one incident input bit to be one. Thus distinct maximal runs of output zeros have independent possible input assignments: each is an edge-covering problem on a path of \(L\) output vertices with \(t\in\{0,1,2\}\) available endpoint stub edges. An internal output vertex is covered exactly when not both incident input edges are absent. If \(t=0\), both outer internal edges must be selected; if \(t=1\), one must be selected; if \(t=2\), neither is forced. Counting the remaining bit strings with no adjacent absent edges gives respectively \(\mathcal F_{L-1}\), \(\mathcal F_{L+1}\), \(\mathcal F_{L+3}\), including the one-vertex edge cases \(0,1,3\). In unified form this is \(\mathcal F_{L-1+2t}\). Taking products over runs and then over the two independent parities proves the stated \(W\) formula for \(p_n(s)\), even when it is zero.

**4. Individual basins and the distinguished orbit.** Because \(F^3=F\), every initial state enters the recurrent set after one update, and the preimages of different periodic states are disjoint. Hence any fixed-point basin has size \(p_n(s)\), while a two-cycle basin is the sum of its two one-step fibers. In particular, \(F(\varnothing)=V\) and \(F(V)=\varnothing\) for \(P_n\) with \(n\ge2\). The full output forces the empty input, so \(p_n(V)=1\). The empty output has one all-zero run in each parity class; the run product gives
\[
 \operatorname{Bas}(\{\varnothing,V\})=
 \begin{cases}
 1+\mathcal F_{m+1}^2,&n=2m,\\
 1+\mathcal F_m\mathcal F_{m+3},&n=2m+1.
 \end{cases}
\]
For any \(n\ge3\), maximal independent sets of \(P_n\) split according to whether its first vertex is selected. If selected, deleting the first two vertices leaves a maximal independent set of \(P_{n-2}\); if absent, the second is selected and deleting the first three leaves one of \(P_{n-3}\). These are bijections, giving
\[
 m_n=m_{n-2}+m_{n-3},\qquad m_0=m_1=1,\quad m_2=2.
\]
The dominant positive root \(\rho\) of \(\rho^3=\rho+1\) is approximately \(1.324717957\), so \(m_n=\Theta(\rho^n)\). Thus the fraction of initial states that are already periodic is \(\Theta((\rho^2/2)^n)\), which tends to zero. Binet's formula gives the more specific asymptotic
\[
 \frac{\operatorname{Bas}(\{\varnothing,V\})}{2^n}
 \sim \frac{\varphi^2}{5}\left(\frac\varphi2\right)^n,
 \qquad \varphi=\frac{1+\sqrt5}{2},
\]
so the empty/full cycle's basin fraction also vanishes exponentially. Neither decay result asserts that this is the largest basin.

## Verification

The included `checker.py` directly computes NOR on each state and validates the square law against the maximal-independent-set count for every one of the 682 labelled bipartite graphs with two part sizes between one and three (isolated vertices allowed). It then verifies every preimage fiber, every fixed count and every recurrent count for paths of orders two through fifteen (65,532 possible output words).

Independently, `checker.cpp` uses direct bitwise state enumeration and a distinct implementation of the Fibonacci-run formula to validate every possible output preimage for paths of orders two through nineteen, covering 1,048,572 initial configurations. Both execution outputs are supplied. These finite computations check edge and boundary cases but **do not replace** the proofs for arbitrary graph and path size.

## Relationship to prior work

The correspondence of fixed configurations and maximal independent sets is classical in Boolean network research (Aracena, Demongeot and Goles, 2004); it is not claimed as original. The Padovan-type count of maximal independent sets of paths, and general short-period behavior of symmetric NOR/antitone networks, are likewise background. The present result isolates the exact square-conjugate recurrent subsystem for *open-neighborhood* NOR on all bipartite graphs, and supplies the individual zero-run predecessor/basin formula for every path. These are stronger assertions than a period restriction or fixed-point count, and the second is not a mere substitution into the first.

Aledo, Martínez and Valverde (2013) discuss NOR among independent local Boolean update functions. The accessible 2015 survey's account of that setting says a pure NOR network cannot have nonzero fixed points, which differs from this open-neighborhood rule: already \(P_2\) has two nonzero fixed configurations. For this reason their stated self-inclusive formulation cannot directly imply the present open-neighborhood basin theorem. The full 2013 paper was not inspected, and that historical-overlap risk is retained. The 2017 and 2020 papers by Aledo and coauthors study global Boolean maxterms/minterms on *closed* neighborhoods; their full accessible text was checked for definitions and result scopes, rather than being treated as a proof of noncoverage merely from an abstract. A 2019 parallel maxterm/minterm predecessor paper is an additional close comparison: its accessible abstract treats predecessor existence in the closed-neighborhood global-function setting, but its full text was unavailable for an individual-fiber comparison.

## Limitations

The general square conjugacy is proved only for bipartite graphs, not arbitrary graphs. The Fibonacci run formula is proved for paths, not for general trees or rings. It counts discrete deterministic attraction basins, not perturbation-stable attractors in a continuous or noisy model. Graphs with isolates are included in the first assertion, but the distinguished empty/full two-cycle requires the no-isolate condition that holds for the stated paths. No assertion of unique asymptotic basin dominance is made. Full historical coverage cannot be guaranteed, especially for inaccessible earlier primary articles. Independent external validation has not been performed.

## References

1. J. Aracena, J. Demongeot and E. Goles, *Fixed points and maximal independent sets in AND-OR networks*, Discrete Applied Mathematics **138** (2004), 277–288. DOI: `10.1016/S0166-218X(03)00461-X`.
2. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel discrete dynamical systems on independent local functions*, Journal of Computational and Applied Mathematics **237** (2013), 335–339. DOI: `10.1016/j.cam.2012.06.002`.
3. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), article 594294. DOI: `10.1155/2015/594294`.
4. J. A. Aledo, L. G. Díaz, S. Martínez and J. C. Valverde, *On the Periods of Parallel Dynamical Systems*, Complexity (2017), article 7209762. DOI: `10.1155/2017/7209762`.
5. J. A. Aledo and collaborators, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), article 9708347. DOI: `10.1155/2020/9708347`.
6. J. A. Aledo, L. G. Díaz, S. Martínez and J. C. Valverde, *Predecessors and Garden-of-Eden configurations in parallel dynamical systems on maxterm and minterm Boolean functions*, Journal of Computational and Applied Mathematics **348** (2019), 26–33. DOI: `10.1016/j.cam.2018.08.015`.
