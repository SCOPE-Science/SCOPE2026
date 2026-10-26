# Exact oscillation census for synchronous majority dynamics on wheel networks

## Finding
Fix an integer \(n\ge4\). The **wheel** has a labeled rim \(v_0,\dots,v_{n-1}\) arranged in a cycle and a hub \(h\) adjacent to every rim vertex. At every integer time, all vertices simultaneously adopt the strict majority among their **open** neighbors; a vertex retains its current binary opinion when its neighbors tie. Distinguish a *periodic state* (a labeled coloring on a recurrent orbit) from a *two-cycle orbit* (an unordered pair of distinct successive colorings).

Define, for an integer \(\ell\ge2\), the following exact integer-coefficient polynomial:
\[
G_\ell(u,v)=1+u^\ell v^\ell+\sum_{r=1}^{\lfloor\ell/3\rfloor}\ \sum_{a=2r}^{\ell-r}
 \frac{\ell}{r}\binom{a-r-1}{r-1}\binom{\ell-a-1}{r-1}u^a v^{a-r}.
\]
An empty sum contributes zero. Define
\[
 H_n(u,v)=\begin{cases}G_n(u,v),&n\text{ odd},\\G_{n/2}(u,v)^2,&n\text{ even},\end{cases}
 \qquad B_n=\sum_{2a>n,\,2b<n}[u^av^b]H_n(u,v).
\]
All coefficient exponents \(a,b\) in the last sum are nonnegative integers; the sum is finite.

**Theorem.** Every initial binary configuration eventually reaches a fixed point or a genuine two-cycle. There are exactly **two fixed points**, namely the two unanimous configurations. The number of **distinct genuine two-cycle orbits** is exactly
\[
\boxed{B_n+2\mathbf1_{2\mid n}.}
\]
Of these, \(B_n\) have a hub that reverses its opinion every round, and the other two (when \(n\) is even) have a constant hub and an alternating rim. Equivalently, there are exactly \(2+2B_n+4\mathbf1_{2\mid n}\) periodic labeled configurations, including fixed points.

For rim lengths \(n=4,5,6,7,8,9,10,11,12,13,14,15,16\), the corresponding hub-flipping orbit counts \(B_n\) are respectively \(0,5,9,21,32,66,75,220,225,715,833,2318,2976\). In addition, for every \(n\ge96\),
\[
\boxed{B_n\ge 2^{n/12}.}
\]
Thus adding one universal hub to a rim with arbitrarily many vertices leaves only two fixed opinion profiles, yet the wheel retains exponentially many genuine oscillatory attractors. These are counts of distinct periodic orbits, **not** probabilities of their attraction basins.

## Assumptions and scope
The graph is the simple undirected wheel on \(n+1\) labeled vertices, with \(n\ge4\). Opinion states lie in \(\{0,1\}\). Updates are deterministic and synchronous. Rim vertices have degree three; the hub has degree \(n\). Ties are possible only at the hub when \(n\) is even and are resolved by retention. The coefficients of \(H_n\) count explicitly labeled rim states, not rotation classes. No randomness, stubborn voters, biases, or asynchronous updates are present.

For a rim configuration \(x\in\{0,1\}^n\), with indices modulo \(n\), define
\[
 A(x)_i=x_{i-1}x_{i+1},\quad C(x)_i=x_{i-1}\lor x_{i+1},\quad a(x)=\sum_i x_i,\quad b(x)=\sum_i x_{i-1}x_{i+1}.
\]
The symbol \(\lor\) is Boolean OR and multiplication is Boolean AND. Define a *step-two cycle* by following \(i\mapsto i+2\pmod n\); there is one such cycle of length \(n\) for odd \(n\), and two cycles of length \(n/2\) for even \(n\). For length two, the two cyclic successor positions are counted with multiplicity for the statistic \(b\); no multigraph is introduced into the underlying wheel.

## Proof
**1. Every trajectory becomes one- or two-periodic.** Convert binary opinions to spins \(s_i\in\{-1,+1\}\). Let \(W\) be the symmetric adjacency matrix of the wheel; additionally set the hub diagonal entry to one if \(n\) is even, and otherwise leave all diagonal entries zero. Every row sum of \(W\) is odd. Thus \((Ws)_i\ne0\) for every spin configuration, and the prescribed update is exactly \(s_i(t+1)=\operatorname{sgn}((Ws(t))_i)\). The added hub self-weight breaks neighbor ties in favor of the old opinion and never changes a strict neighbor majority.

Define \(\mathcal L_t=-s(t+1)^TW s(t)\). By symmetry,
\[
 \mathcal L_{t+1}-\mathcal L_t
 =-\sum_i \bigl(s_i(t+2)-s_i(t)\bigr)(Ws(t+1))_i\le0.
\]
Each summand before the leading minus sign is nonnegative, and is strictly positive whenever \(s_i(t+2)\ne s_i(t)\), since the local field is a nonzero odd integer and \(s_i(t+2)\) is its sign. The integer \(\mathcal L_t\) is bounded below (\(W\) is finite). Therefore \(s(t+2)=s(t)\) from some time onward.

**2. The two fixed points and constant-hub two-cycles.** Suppose the hub is zero at each of two successive times. The rim map at both steps is \(A\). Direct substitution gives
\[
 A(A(x))_i=x_{i-2}x_i x_{i+2}.
\]
The equality \(A(A(x))=x\) therefore forces every occupied (one-valued) position to have both step-two neighbors occupied. Along each connected step-two component, all positions must consequently be identical. For odd \(n\), the rim is either all zero or all one; all one would force the zero hub to switch to one, leaving only the unanimous-zero fixed point. For even \(n\), each of the two parity classes is constant. Both classes zero give the unanimous-zero fixed point, both one force the hub to switch, and opposite constant classes give precisely the two alternating-rim states of a genuine two-cycle with hub fixed at zero (because exactly half the rim is one, so the hub tie retains zero). Complementing colors gives the unanimous-one fixed point and, when \(n\) is even, one further two-cycle with hub fixed at one. No other constant-hub periodic states exist.

**3. Hub-reversing two-cycles.** In a state with hub zero and rim \(x\), the next hub equals one if and only if \(2a(x)>n\). The next rim is \(y=A(x)\), and the number of its one-valued vertices is \(b(x)\). The hub then returns to zero if and only if \(2b(x)<n\). During that second step, the rim uses \(C\), so
\[
 C(A(x))_i=x_i\bigl(x_{i-2}\lor x_{i+2}\bigr).
\]
Hence the rim returns to \(x\) exactly when each one-valued rim position has at least one one-valued step-two neighbor. In other words, there is **no isolated one** on any step-two cycle. Both inequalities and this no-isolated-one rule are jointly necessary and sufficient. Each such \(x\) determines a unique two-cycle orbit by following its hub-zero state to its hub-one state; different \(x\)'s give different orbits.

**4. Count the admissible rim words.** For a labeled cyclic word of length \(\ell\), let \(a\) count one-valued sites and \(b\) count cyclic adjacent one-one pairs. The no-isolated-one words are the all-zero word, the all-one word, and words with \(r\ge1\) cyclic runs of ones, all of length at least two, separated by nonempty runs of zeros. In the latter case \(b=a-r\). The number of length-\(\ell\) labeled words with given \(a,r\) is
\[
 \frac\ell r\binom{a-r-1}{r-1}\binom{\ell-a-1}{r-1}.
\]
Indeed, choose one of the \(\ell\) possible locations for the start of a marked one-run, choose the positive compositions of the \(a\) ones into \(r\) lengths at least two and the \(\ell-a\) zeros into \(r\) positive lengths, then divide by the \(r\) choices of marked one-run in the resulting word. This proves that \(G_\ell\) is the generating polynomial of no-isolated-one cyclic words by the statistics \(a,b\).

For odd \(n\), the step-two ordering permutes the rim labels into a single \(n\)-cycle, and the statistic \(b(x)\) becomes the adjacent one-one count in that order. For even \(n\), the two step-two cycles are independent, so their generating polynomials multiply. Thus \(H_n\) counts exactly the rim words meeting the local condition, and its coefficient restriction \(2a>n,2b<n\) counts precisely the hub-reversing two-cycle orbits. This proves the exact census.

**5. Exponentially many hub-reversing cycles.** For every integer \(\ell\ge48\), choose a nonnegative integer \(q\) with \(q\equiv\ell\pmod3\) and \(|q-\ell/8|\le3/2\), and put \(p=(\ell-4q)/3\). Then \(p,q\ge\ell/12\). Every ordering of \(p\) copies of the binary block `110` and \(q\) copies of `1100`, beginning at a fixed labeled position, produces a distinct admissible cyclic word: its one-runs have length two, its number of ones is \(2(p+q)>\ell/2\), and its number of one-one cyclic edges is \(p+q<\ell/2\). The block boundaries are uniquely recoverable from the word, giving at least \(\binom{p+q}{p}\ge2^{\min(p,q)}\ge2^{\ell/12}\) such words.

For odd \(n\ge96\), apply the construction to the unique step-two cycle of length \(n\). For even \(n\ge96\), apply it separately to both step-two cycles of length \(n/2\), multiplying the numbers of admissible choices. The strict majority inequalities then hold after combining both components. Hence \(B_n\ge2^{n/12}\), as asserted.

## Verification
Run `python3 verify_wheel.py` (standard library only) in the same directory. It constructs the original wheel's adjacency majority update directly, exhaustively checks all \(2^{n+1}\) binary configurations for each \(4\le n\le16\), and independently constructs the polynomial coefficients by two methods: explicit enumeration of words on a cycle and cyclic-run compositions. The direct wheel tests examine \(262112\) labeled configurations. The code checks fixed states, hub-reversing two-cycle states, constant-hub two-cycle states and all reported \(B_n\). These are finite tests; the proof above establishes the all-length theorem. The growth bound is proved by explicit injection, not by extrapolation.

## Relationship to prior work
Volker Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees* (2022, arXiv:2202.01580v1) establishes fixed- and two-cycle structures for **trees**, whose absence of cycles differs from a wheel. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes* (2023, arXiv:2302.06760v1), analyzes cycles and general graphs and shows exponentially many stable cycle configurations, but its cycle graph does not include a universal hub and its main exact cycle results do not count wheel oscillators. Nakar and Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata* (2022, arXiv:2205.08972v1), study a fixed local-radius self-inclusive cellular automaton on a cycle, not a globally coupled universal-hub majority network. Period-at-most-two is classical for symmetric threshold networks and independently reproved here; it is **not** claimed as a novel mechanism. The new claimed contribution is the wheel-specific structural classification, the explicit binomial census and the exponential family of hub-flipping two-cycles. The literature comparison cannot prove global uniqueness; equivalent results under threshold-network terminology may exist.

## Limitations
No attraction-basin sizes, random-start convergence probabilities, mixing properties, error resilience, signed edges, asynchronous dynamics, weighted spokes or multiple hubs are evaluated. The total number of recurrent states is not a measure of how often a randomly initialized trajectory reaches each orbit. The lower bound \(2^{n/12}\) is not presented as the exact exponential growth constant. Literature comparisons are limited to the enumerated accessible sources, their actual material and searched records; unindexed equivalents remain possible. Independent audit and validation have not been performed.

## References
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1, first posted 2022-02-03. https://arxiv.org/html/2202.01580v1
- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, first posted 2023-02-14. https://arxiv.org/html/2302.06760v1
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972v1, first posted 2022-05-18. https://arxiv.org/abs/2205.08972
