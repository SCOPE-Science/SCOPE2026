# Two excitation modes and a sharp seven-step clock in four-state threshold-two dynamics on complete bipartite graphs

## Finding

For every pair of integers \(a,b\ge2\), consider the synchronous four-color, contact-threshold-two Greenberg–Hastings automaton on the labelled complete bipartite graph \(K_{a,b}\). Its global map \(F\) obeys the **uniform identity**
\[
F^{11}=F^7.
\]
It has exactly one fixed configuration (all vertices resting), and every other periodic configuration lies on a primitive four-cycle. The nonzero periodic states are precisely the following **disjoint families**:

1. **Alternating two-phase states:** one shore has exclusively colors \(0,2\), with at least two vertices of each color; the other has exclusively \(1,3\), again with at least two of each (in either shore orientation).
2. **Fully rotating four-phase states:** each shore has at least two vertices in each of the four colors \(0,1,2,3\).

Set \(S(n)=2^n-2n-2\) for \(n\ge4\), and \(S(n)=0\) otherwise. Set
\[
T(n)=\sum_{\substack{n_0+n_1+n_2+n_3=n\\n_0,n_1,n_2,n_3\ge2}}
\frac{n!}{n_0!n_1!n_2!n_3!}
=n![z^n](e^z-1-z)^4.
\]
The number of primitive temporal four-cycle **orbits** (labelled states identified only under time translation) is exactly
\[
\boxed{Q_4(a,b)=\frac12S(a)S(b)+\frac14T(a)T(b).}
\]
The alternating family first appears when \(\min(a,b)=4\); the fully rotating family first appears when \(\min(a,b)=8\). In particular, \(Q_4(4,4)=18\), \(Q_4(4,5)=60\), and \(Q_4(8,8)=1{,}615{,}922\).

Let the **first-periodic-entry time** be
\[
\tau(x)=\min\{t\ge0:F^{t+4}(x)=F^t(x)\}.
\]
The maximum \(H(a,b)=\max_x\tau(x)\) is the following sharp, exhaustive phase diagram:
\[
H(a,b)=\begin{cases}
4,&a=b=2,\\
5,&\min(a,b)=2,\ \max(a,b)\ge3,\ \text{or }a=b=3,\\
7,&\min(a,b)\ge7,\ \max(a,b)\ge8,\\
6,&\text{in all remaining cases}.
\end{cases}
\]
At \(K_{7,8}\), a configuration with the first shore \(0011233\) and second shore \(00112233\) attains \(\tau=7\). The bound of seven is independent of the number of vertices.

There is also a **complete exact coefficient formula for every entrance-time/period basin**. For \(r\in\{0,1,2\}\), put
\(g_0(z)=1\), \(g_1(z)=z\), and \(g_2(z)=e^z-1-z\). Define the finite set of capped occupancy signatures \(\Sigma=\{0,1,2\}^8\), representing the four initial color-population classes on each shore, capped at two. For \(s\in\Sigma\), the supplied exact finite-state certificate records \(\tau(s)\) and eventual primitive period \(p(s)\in\{1,4\}\). For each \(0\le u\le7\), \(v\in\{1,4\}\), the number of labelled initial configurations with first entry \(u\) and eventual period \(v\) is exactly
\[
\boxed{B_{u,v}(a,b)=a!b![x^a y^b]
\sum_{\substack{s\in\Sigma\\\tau(s)=u,\ p(s)=v}}
\prod_{j=0}^3g_{s_j}(x)\prod_{j=4}^7g_{s_j}(y).}
\]
This finite polynomial/exponential coefficient prescription applies to **all** \(a,b\ge2\); it is not an asymptotic fit to small graphs.

## Assumptions and scope

The graph \(K_{a,b}\) is simple, undirected, and has two labelled vertex shores of sizes \(a\) and \(b\), each at least two. States are \(0\) (resting), \(1\) (excited), \(2,3\) (refractory). At each integer time all vertices update simultaneously. A vertex in state \(j\in\{1,2,3\}\) advances to \(j+1\pmod4\); a vertex in state \(0\) changes to \(1\) iff **at least two** opposite-shore neighbors are in state \(1\), and otherwise remains \(0\). All initial assignments in \(\{0,1,2,3\}^{a+b}\) are admitted. Orbit counts do not identify configurations under graph isomorphisms, permutations, or exchange of shores.

## Proof

**Population-capping lemma.** Vertices in the same shore with identical initial color evolve identically for all time: they have identical neighbor sets and the same transition rule. Thus the eight initial shore–color classes never split. Replacing each class of size \(m\) by \(\min(m,2)\) representatives leaves the truth of each event “the opposite shore contains at least two excited vertices” unchanged at every time, by induction on time. Consequently the eight capped multiplicities in \(\{0,1,2\}^8\) determine the entire classwise trajectory and its least eventual entry time and period. This is an exact reduction for unbounded shore sizes, not a finite-size approximation.

**Exact finite quotient.** The included `cap_certificate.py` independently iterates each of the \(3^8=6561\) capped signatures through step eleven, and asserts the identity \(F^{11}(s)=F^7(s)\) for every signature. It also tests whether \(F^4(s)=s\), checks the above three possible periodic types, and rejects any other periodic shape. The observed twelve periodic signatures consist of nine zero-only patterns (including capped empty-shore signatures outside the present domain), two alternating signatures, and one four-color signature. The only feasible fixed point on shores of size at least two is all-zero; all other periodic states have primitive period exactly four, since the program checks no nonzero periodic state satisfies either \(F(x)=x\) or \(F^2(x)=x\). These assertions are checked by executable deterministic integer-state iteration, not inferred from logs. Together with the capping lemma, they establish the global identity and exhaustive orbit classification for every finite \(a,b\ge2\).

**Counting the periodic orbits.** On a shore of size \(n\), \(S(n)=\sum_{j=2}^{n-2}\binom nj\) counts assignments of the two prescribed alternating colors with at least two occurrences of each. There are two choices of which shore receives the even colors, giving \(2S(a)S(b)\) alternating periodic **states**. For the fully rotating family, the shores have \(T(a)\) and \(T(b)\) assignments to four colors, giving \(T(a)T(b)\) states. The two families are disjoint and every nonzero state has primitive period four, so division by four gives the asserted orbit formula. The first size thresholds are immediate from the requirement of two vertices per occupied color.

**Sharp entry cutoff.** For a capped four-class signature \(c\), its feasibility on a shore of size \(n\) is equivalent to: if \(c\) contains a 2, then \(n\ge\sum c_j\); otherwise \(n=\sum c_j\). In the first case, the surplus is assigned to a class already capped at two. All cap vectors have \(\sum c_j\le8\), so for every shore size \(n\ge8\) the set of feasible cap signatures is unchanged. The certificate exhaustively computes \(\tau(s)\) and maximizes it over feasible signatures for every \((a,b)\) with \(2\le a,b\le8\), verifying exactly the displayed phase diagram; stabilization beyond size eight then proves it for all larger sizes. In particular the two seven-step signatures first become feasible on shores of sizes seven and eight. A labelled witness is provided above. Every comparison is exact, and the finite quotient is exhaustive by the population-capping lemma.

**Basins.** For a particular initial color class, the labelled exponential generating functions for multiplicity zero, one, or at least two are respectively \(1\), \(z\), and \(e^z-1-z\). Multiplying these eight independent class enumerators and taking the coefficients \([x^a y^b]\), followed by multiplication by \(a!b!\), counts each labelled initial configuration once. The signature table computes its exact \((\tau,p)\), proving the stated complete basin coefficient formula.

## Verification

`cap_certificate.py`, `cap_certificate.csv` and `cap_certificate.out` encode an exhaustive, parameter-independent certificate of all \(6561\) capped signatures and the sharp phase diagram. `direct_check.cpp` and `direct_check.out` provide a distinct C++17 implementation enumerating **4,657,408 labelled configurations** across ten graph sizes and checking the update identity, fixed points, exact number of periodic states, and all first-entry histograms. `basin_formula_check.py` and `basin_formula_check.out` independently expand the coefficient formula at five graph sizes and match the direct count. The two implementations use different representations (eight class-population signatures versus individually labelled two-bit states). All necessary source and output files are embedded alongside this document; exact reproduction commands are in `VERIFICATION.md`.

## Relationship to prior work

Fisch, Gravner and Griffeath investigated multistate, multi-threshold excitable automata on spatial lattices; their transition formalism motivates the present threshold-two question but their planar spatial setting and results do not imply the bipartite orbit census. Gravner, Lyu and Sivakoff established general results for three-color excitable systems, not four-color threshold-two systems on complete bipartite graphs. Bello and Sivakoff study multicolor threshold excitable automata on infinite regular trees, but not these finite bicliques. The original Greenberg–Hastings model supplies the foundational excitation mechanism. The present statement concerns a different specified finite graph family with exact orbit and first-entry statistics; it does not claim the origin of the update model or any general convergence theory. The separate binary parity automata and irreversible threshold-diffusion results located in published mathematical records use non-equivalent update maps. A search for the numerical sequence alone does not establish mathematical novelty; superficially matching rows occur in an unrelated binomial triangle (OEIS A132813).

## Limitations

The result is for four states, excitation threshold exactly two, and complete bipartite graphs with both shores at least two. It does not give analogous formulas for arbitrary graph structures, other contact thresholds, stochastic dynamics, or other numbers of refractory states. The basin formula is a finite coefficient extraction, not a simplified closed form. The finite quotient and direct checks verify mathematical statements; they do not establish historical uniqueness. Similar older results under different names or in inaccessible material remain possible. No independent external audit has been performed.

## References

- R. Fisch, J. Gravner and D. Griffeath, “Threshold-range scaling of excitable cellular automata,” *Statistics and Computing* (1991). Lawful full text: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf ; public preprint arxiv:patt-sol/9304001 (first verified upload 1993-04-02), https://arxiv.org/abs/patt-sol/9304001.
- J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” arxiv:1610.07320 (2016), https://arxiv.org/html/1610.07320v1.
- N. Bello and D. Sivakoff, “Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees,” arxiv:2108.06404 (2021), https://arxiv.org/abs/2108.06404.
- J. M. Greenberg and S. P. Hastings, “Spatial patterns for discrete models of diffusion in excitable media,” *SIAM Journal on Applied Mathematics* (1978), doi:10.1137/0134040.
- OEIS Foundation, A132813, unrelated binomial-product triangle; inspected solely for possible numerical coincidences: https://oeis.org/A132813.
