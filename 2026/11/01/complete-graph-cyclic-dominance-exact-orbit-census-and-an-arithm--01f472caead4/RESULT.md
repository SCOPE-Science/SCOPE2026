# Complete-graph cyclic dominance: exact orbit census and an arithmetic critical window

## Finding

**Theorem.** For every integer \(N\geq3\) and contact threshold \(\theta\geq1\), consider the simultaneous three-colour cyclic cellular automaton on the loopless complete graph with \(N\) labelled vertices. Every state is either fixed, belongs to a primitive three-cycle, or reaches a fixed state in one or two steps. Let \(F_N,U_{1,N},U_{2,N},P_N\) count, respectively, configurations with preperiod and eventual period \((0,1),(1,1),(2,1),(0,3)\). Set
\[
L_\theta(z)=\sum_{j=1}^{\theta-1}\frac{z^j}{j!},\qquad
H_\theta(z)=e^z-\sum_{j=0}^{\theta-1}\frac{z^j}{j!}.
\]
Then the exact complete census is
\[
\begin{aligned}
F_N&=3+3\sum_{j=1}^{\min(\theta-1,N-1)}\binom Nj+N![z^N]L_\theta(z)^3,\\
U_{1,N}&=3\sum_{j=\theta}^{N-1}\binom Nj+3N![z^N]H_\theta(z)L_\theta(z)^2,\\
U_{2,N}&=3N![z^N]H_\theta(z)^2L_\theta(z),\\
P_N&=N![z^N]H_\theta(z)^3.
\end{aligned}
\]
Empty sums are zero. These four quantities total \(3^N\); the numbers of fixed orbits and primitive three-cycles are \(F_N\) and \(P_N/3\). A primitive three-cycle exists **exactly when** \(N\geq3\theta\), while a two-step transient exists **exactly when** \(\theta\geq2\) and \(N\geq2\theta+1\).

For independent uniformly distributed initial colours, let \(\theta_N\) be positive integers satisfying
\[
\frac{N/3-\theta_N}{\sqrt N}\longrightarrow\delta\in\mathbb R.
\]
If \(\mathcal P_N\) is the probability of primitive-three periodicity, then
\[
\mathcal P_N\longrightarrow\Psi(\delta):=\Pr(G_0\geq-\delta,G_1\geq-\delta,G_2\geq-\delta),
\]
where \(G_0+G_1+G_2=0\) and \(\operatorname{Cov}(G_i,G_j)=2/9\) for \(i=j\), \(-1/9\) otherwise. The limit is zero for \(\delta\leq0\), lies strictly between zero and one for \(\delta>0\), and satisfies the sharp small-window law
\[
\Psi(\delta)\sim\frac{27\sqrt3}{4\pi}\delta^2\quad(\delta\downarrow0).
\]
At the arithmetic boundary \(\theta=\lfloor N/3\rfloor\) with \(N=3m+r\), \(r\in\{0,1,2\}\), the more delicate local-limit statement is
\[
\boxed{\displaystyle N\mathcal P_N\longrightarrow\binom{r+2}{2}\frac{3\sqrt3}{2\pi}\quad\text{as }m\to\infty.}
\]
The residue-dependent factors are exactly \(1,3,6\).

## Assumptions and scope

The vertex set is \(\{1,\ldots,N\}\), the graph is the loopless undirected complete graph, and configurations are \(s=(s_1,\ldots,s_N)\in\{0,1,2\}^N\). All vertices update synchronously. A vertex in colour \(c\) advances to \(c+1\pmod3\) precisely when it has at least \(\theta\) neighbours currently in the successor colour; otherwise it does not change. The three-colour population counts are \(n_c(s)=\#\{i:s_i=c\}\). Because a vertex never itself has its successor colour, its number of successor neighbours is exactly \(n_{c+1}(s)\). The preperiod is the smallest nonnegative number of updates before a periodic orbit starts. For the probabilistic assertions the initial vertex colours are independent and uniform; no stochasticity is introduced into subsequent evolution.

## Proof

**Population reduction.** For any currently occupied colour \(c\), every vertex of that colour advances together or remains together, according solely to the test \(n_{c+1}\geq\theta\). Thus one step is determined by three simultaneous yes/no decisions. If all three populations are positive and all at least \(\theta\), all vertices advance on every iteration. Their population triple merely rotates, hence each configuration has primitive period three (not one, because every vertex changes). If all occupied colours see fewer than \(\theta\) successor vertices, the configuration is fixed.

**Exhaustion of intermediate cases.** With exactly two occupied colours, one is predator to the other; if its count is at least \(\theta\), the prey changes to that predator in one update, and the resulting monochromatic state is fixed. Otherwise the initial state is fixed. With all three colours present, if exactly one population meets \(\theta\), only the predecessor population advances and merges with its successor, after which both occupied populations are fixed. If exactly two populations meet \(\theta\), rotate colour names so they are \(n_0,n_1\geq\theta\) while \(0<n_2<\theta\). The first update gives \((n'_0,n'_1,n'_2)=(n_2,n_0+n_1,0)\), and the second update merges all of colour zero into colour one. This state was not fixed after one update since \(n'_1\geq\theta\). These cases exhaust all configurations. A two-step transient can exist only when \(\theta\geq2\), and a witness with counts \((\theta,N-\theta-1,1)\) exists exactly when \(N\geq2\theta+1\). A three-cycle needs and is guaranteed by three populations each at least \(\theta\), equivalently \(N\geq3\theta\).

**Exact counting.** Three monochromatic configurations are fixed. For each of three unordered two-colour pairs and each size \(j=1,\ldots,N-1\) of the predator colour, exactly \(\binom Nj\) configurations have those counts. They are fixed if \(j<\theta\) and have one-step preperiod if \(j\geq\theta\). For three occupied colours, mark each colour's positive count as small (between \(1\) and \(\theta-1\)) or large (at least \(\theta\)). The preceding classification says that the numbers of large counts \(0,1,2,3\) correspond exactly to the categories \(F_N,U_{1,N},U_{2,N},P_N\). The exponential generating functions \(L_\theta\) and \(H_\theta\) count positive small and large labelled colour blocks. Choosing which of the three colours are large gives coefficients \(1,3,3,1\), proving all four formulas. They partition the set of \(3^N\) configurations.

**Gaussian critical window.** Under uniform independent colours, \((n_0,n_1,n_2)\) has the multinomial distribution with parameters \(N;(1/3,1/3,1/3)\). The multinomial central limit theorem gives the stated singular three-dimensional Gaussian, equivalently a nonsingular two-dimensional Gaussian for \((G_0,G_1)\) with covariance
\[
\Sigma=\frac19\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
Three-cycle membership is the event \(n_i\geq\theta_N\) for every colour. Boundaries of the limiting Gaussian triangle have measure zero, so the probability converges to \(\Psi(\delta)\). When \(\delta\leq0\), the three inequalities force all Gaussian coordinates to vanish (or are inconsistent), an event of probability zero. For \(\delta>0\), the allowed region in coordinates \((G_0,G_1)\) is the triangle \(x,y\geq-\delta\), \(x+y\leq\delta\), of area \(9\delta^2/2\). The Gaussian density at its center is \((2\pi\sqrt{\det\Sigma})^{-1}=3\sqrt3/(2\pi)\). Continuity of the density yields the small-window coefficient \(27\sqrt3/(4\pi)\).

**Arithmetic boundary.** For \(N=3m+r\) and \(\theta=m\), a three-cycle configuration has counts \((m+a,m+b,m+c)\) with nonnegative integers \(a+b+c=r\). There are exactly \(\binom{r+2}{2}\) such triples. The two-dimensional multinomial local central limit theorem gives, for each of these finitely many near-balanced triples, the probability \(3\sqrt3/(2\pi N)+o(N^{-1})\). Summing gives the claimed residue-dependent limit. This proves the theorem. \(\square\)

## Verification

The standalone standard-library script `verify.py` computes the updates from the vertex-level rule (not from the claimed classification), detects preperiod and primitive period for every configuration on \(3\leq N\leq9\), and compares the four exact formulas against independent multinomial enumeration for every \(1\leq\theta\leq N+1\). It checks 280,449 initial-configuration/threshold pairs. These exhaustive finite tests corroborate, but do not replace, the proof for arbitrary \(N\). The arithmetic coefficients can also be checked by the displayed local-central-limit computation.

## Relationship to prior work

España, Funez and Ugalde [1] study finite-network attractor landscapes, period lengths, basins and transient depths for Boolean automata, including signed-majority clover networks. This motivates seeking a complete landscape on another natural graph family, but their results concern different local states, graphs and rules. The explicit three-colour cyclic rule is classical. Gravner, Lyu and Sivakoff [2] study this cyclic rule with one required predecessor neighbour on arbitrary graphs; in particular the threshold-one dynamics is not claimed as a new invention. Bello and Sivakoff [3] study general contact thresholds on **infinite regular trees** and identify fixation/fluctuation regimes; their setting does not imply finite complete-graph orbit counts or the critical-window coefficient. The present theorem concerns the all-threshold finite complete-graph classification and its exact critical statistics. The three-colour uniform input is a specific mean-field comparator, not an extension of any tree theorem by graph inclusion.

## Limitations

The exact formulas require a complete loopless graph, three colours and fully synchronous deterministic updates. No statement is made about a general graph, \(\kappa>3\), asynchronous updates or other initial probability vectors. The Gaussian limit assumes independent uniform initial colours and the stated threshold scaling; the local-limit assertion along residue classes does not give a universal pointwise rate for arbitrary threshold sequences. Mathematical priority has not been independently certified. The complete-graph conclusion is a special solvable benchmark, not a claim that spatial or tree geometries share its two-step transient bound.

## References

[1] A. España, W. Funez and E. Ugalde, *Dominant vertices and attractors' landscape for Boolean networks*, arXiv:2509.03654v1, first posted 2025-09-03, primary MSC2020 37B15; https://arxiv.org/abs/2509.03654 .

[2] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016); https://arxiv.org/html/1610.07320v1 .

[3] J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees*, arXiv:2108.06404v1 (2021); https://arxiv.org/html/2108.06404v1 .
