# Sharp global escape boundary and log-log critical clock for coupled Gaussian-cubic maps

## Finding
Let \(a>0\), \(b\in\mathbb R\), and consider the smooth map of the entire real plane
\[
T_{a,b}(x,y)=\bigl(f_a(x)+b(y-x),\ f_a(y)+b(x-y)\bigr),
\qquad f_a(t)=a\,t(1-t^2)e^{-t^2}.
\]
For any initial state \((x_0,y_0)\in\mathbb R^2\), write \((x_n,y_n)=T_{a,b}^n(x_0,y_0)\), and define mean and transverse coordinates \(u_n=(x_n+y_n)/2\), \(v_n=(x_n-y_n)/2\). Then the following statements hold, with quantifiers over **every** fixed \(a>0\):

1. **Complete boundedness threshold.** Every forward orbit is bounded if and only if \(-\tfrac12\le b<\tfrac12\). The included endpoint \(b=-\tfrac12\) and excluded endpoint \(b=+\tfrac12\) are genuinely different.
2. **Exponential escape outside both endpoints.** Whenever \(|b|>\tfrac12\), there is a nonempty open set of initial conditions whose orbits escape to infinity. Every unbounded orbit satisfies
   \[
   u_n\longrightarrow0,\qquad
   \frac{v_n}{(-2b)^n}\longrightarrow c\in\mathbb R\setminus\{0\}.
   \]
3. **Ultraslow escape at the positive endpoint.** For \(b=\tfrac12\), a nonempty open set of orbits escapes, and **every** unbounded orbit satisfies \(u_n\to0\), \(|v_n|\to\infty\), and
   \[
   \boxed{\frac{e^{v_n^2}}{2a\,n\,v_n^4}\longrightarrow1,\qquad
   v_n^2=\log n+2\log\log n+\log(2a)+o(1).}
   \]
   The additive constant in the critical expansion is independent of the initial condition. The diagonal \(x=y\) remains a bounded invariant set in all parameter regimes, so the existence of open escape basins does not assert that all trajectories escape.

## Assumptions and scope
The domain is the full real plane, not a numerically plotted finite box, and the map has no truncation or compactification. \(a>0\) is essential for the stated directional sign at infinity. A forward orbit is **bounded** when \(\sup_{n\ge0}(|x_n|+|y_n|)<\infty\) and is **unbounded** otherwise. Escape means the Euclidean norm tends to infinity as \(n\to\infty\), not a finite-time singularity. The exponentials in the formula use natural logarithms, and the indexing is the actual single-iterate time \(n\).

Set \(M=\sup_{t\in\mathbb R}|f_a(t)|<\infty\). Since \(f_a\) is odd, bounded and decays at both infinities, \(|u_n|\le M\) for every \(n\ge1\). For \(|t|>1\), \(f_a(t)\) has sign strictly opposite to \(t\), and \(f_a'(t)\to0\) as \(|t|\to\infty\).

## Proof
**Step 1: Exact mean/transverse dynamics.** Set
\[
E_a(u,v)=\frac{f_a(u+v)-f_a(u-v)}2
          =\frac{f_a(v+u)+f_a(v-u)}2.
\]
Direct substitution gives
\[
 u_{n+1}=\frac{f_a(u_n+v_n)+f_a(u_n-v_n)}2,
 \qquad v_{n+1}=-2b\,v_n+E_a(u_n,v_n).
\]
Always \(|E_a(u,v)|\le M\). If \(n\ge1\) and \(|v_n|>M+1\), the arguments \(u_n+v_n\) and \(u_n-v_n\) have opposite signs and both have magnitude exceeding one. Consequently \(E_a(u_n,v_n)\ne0\) and its sign is opposite to that of \(v_n\).

**Step 2: Both bounded regimes, including the exceptional negative endpoint.** When \(q=2|b|<1\), the inequality \(|v_{n+1}|\le q|v_n|+M\) gives the explicit uniform-in-time estimate
\[
|v_n|\le q^{n-1}|v_1|+\frac{M(1-q^{n-1})}{1-q},\qquad n\ge1.
\]
At \(b=-\tfrac12\), the transverse recurrence becomes \(v_{n+1}=v_n+E_a(u_n,v_n)\). In the outer region \(|v_n|>M+2\), the sign fact and \(|E_a|\le M<|v_n|\) give \(|v_{n+1}|<|v_n|\). In the complementary region, \(|v_{n+1}|\le2M+2\). Hence \(|v_n|\le\max\{|v_1|,2M+2\}\) for every \(n\ge1\). Since \(|u_n|\le M\), all corresponding orbits are bounded.

**Step 3: Exponential escape when \(|b|>\tfrac12\).** Put \(\lambda=-2b\), \(q=|\lambda|>1\). If \(|v_n|>M/(q-1)\), then
\[
|v_{n+1}|\ge q|v_n|-M>|v_n|.
\]
Choose a sufficiently large \(R>M/(q-1)\). Once \(|v_n|>R\), elementary iteration yields
\[
|v_{n+k}|\ge q^k\Bigl(|v_n|-\frac M{q-1}\Bigr)+\frac M{q-1},\qquad k\ge0.
\]
The region of states that cross this threshold is open, and it is nonempty: choose sufficiently large antidiagonal initial points \((x_0,y_0)=(v_0,-v_0)\). Because \(u_n\) is bounded from time one, an unbounded orbit must cross the same threshold and thereafter escape. The exact telescoping identity
\[
\frac{v_n}{\lambda^n}
=v_0+\sum_{j=0}^{n-1}\frac{E_a(u_j,v_j)}{\lambda^{j+1}}
\]
converges absolutely; the displayed lower bound guarantees a nonzero limiting absolute value. Also \(u_n\to0\), because both arguments of \(f_a\) go to infinity in magnitude while \(|u_n|\le M\).

**Step 4: Opposite drift and genuine escape at \(b=\tfrac12\).** Here \(v_{n+1}=-v_n+E_a(u_n,v_n)\). Choose \(R>M+2\) so large that
\[
\sup_{|t|\ge R-M}|f_a'(t)|\le\tfrac12.
\]
For any \(n\ge1\) with \(|v_n|>R\), Step 1 shows \(v_{n+1}\) changes sign and
\[
|v_{n+1}|=|v_n|+|E_a(u_n,v_n)|>|v_n|.
\]
The outer region is forward invariant. The mean-coordinate update is the symmetric difference
\[
 u_{n+1}=\frac{f_a(v_n+u_n)-f_a(v_n-u_n)}2;
\]
by the mean-value theorem and \(|u_n|\le M\), it obeys \(|u_{n+1}|\le|u_n|/2\). Thus \(u_n\to0\) exponentially along every orbit trapped in this outer region. If \(|v_n|\) converged to a finite number \(r_\infty>R>1\), continuity and oddness would imply \(|E_a(u_n,v_n)|\to|f_a(r_\infty)|>0\), contradicting convergence. Therefore \(|v_n|\to\infty\).

Every unbounded orbit eventually enters \(|v_n|>R\), because \(|u_n|\le M\); conversely, this region is reachable from an open set of sufficiently large initial states. This proves the full escape-versus-boundedness alternative at the positive endpoint.

**Step 5: The universal critical time law.** Along any orbit from Step 4, write \(r_n=|v_n|\) and \(s_n=r_n^2\). From \(|E_a|\le M\) we have \(r_n\le r_N+M(n-N)\) for all \(n\ge N\), whereas \(|u_n|\le2^{-(n-N)}|u_N|\). Thus \(r_n|u_n|\to0\). Using the explicit Gaussian-cubic formula at the two arguments \(v_n\pm u_n\) gives
\[
\frac{E_a(u_n,v_n)}{f_a(v_n)}\longrightarrow1.
\]
For \(r_n>1\), \(|f_a(v_n)|=a r_n(r_n^2-1)e^{-r_n^2}\), so Step 4 implies
\[
 r_{n+1}-r_n=a r_n(r_n^2-1)e^{-r_n^2}(1+o(1)),
\quad
 s_{n+1}-s_n=2a\,s_n^2e^{-s_n}(1+o(1)).
\]
In particular \(s_n\to\infty\) and \(s_{n+1}-s_n\to0\). Define \(H(s)=e^s/(2a s^2)\) for \(s>2\). Its derivative satisfies
\[
H'(s)=\frac{e^s}{2a s^2}\Bigl(1-\frac2s\Bigr),
\quad
H(s_{n+1})-H(s_n)\longrightarrow1.
\]
The second assertion follows from the mean-value theorem and the preceding increment formula, because \(s_{n+1}-s_n\to0\). Summing the increments gives \(H(s_n)/n\to1\), exactly the first critical limit in the finding. Taking logarithms gives
\[
s_n=\log n+2\log s_n+\log(2a)+o(1).
\]
The same relation implies \(s_n/\log n\to1\), whence \(2\log s_n=2\log\log n+o(1)\), proving the second critical formula. Both constants are independent of initial conditions. Steps 2–4 prove the exact boundedness parameter interval.

## Verification
A self-contained standard-library numerical checker accompanies this result as `verify.py`. Running `python3 verify.py` reproduces 84 direct-coordinate versus mean/transverse iterate identities, 36 outer-region sign checks at the two endpoints, six supercritical escape trajectories, and three long-orbit critical drift diagnostics (600,000 steps per parameter). The checks are finite and **do not** prove the global assertions or asymptotic limit. Those follow from the quantified inequalities and summation argument above.

## Relationship to prior work
Soula, Jahanshahi, Al-Barakati, and Moroz (2023, equations (2)–(3), Sections 2–5) introduced and numerically analyzed precisely this coupled Gaussian-cubic map using critical curves, synchronization, chaotic basins, and contact bifurcations. Their conclusion also discusses attractors at infinity. This proof addresses a different quantitative question: the exact global threshold for the **possibility of unbounded escape** and the universal two-logarithm clock at its singular positive endpoint. The predecessor system of Ding and Yang discussed in their introduction has different nonlinear coupling terms and does not supply the asserted formula by parameter renaming. The conclusions here do not strengthen the paper's local synchronization or chaos classifications; they concern global boundedness and the asymptotic geometry of the escape set.

## Limitations
The theorem does not classify bounded attractors, their internal bifurcations, all basins of attraction, or their fractal boundaries. It does not assert that every orbit escapes when escape basins exist. It excludes \(a\le0\), where the sign mechanism may differ. Numerical diagnostics alone cannot certify an asymptotic statement; novelty is assessed against inspected prior sources and can remain subject to unlocated equivalent treatments of coupled maps with bounded nonlinearities. Independent evaluation has not been performed.

## References
1. Y. Soula, H. Jahanshahi, A. A. Al-Barakati, and I. Moroz, *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics **11** (2023), 1517, DOI:10.3390/math11061517. Published online 2023-03-21. Open-access complete text: https://www.researchgate.net/publication/369433718_Dynamics_and_Global_Bifurcations_in_Two_Symmetrically_Coupled_Non-Invertible_Maps.
2. M. Ding and W. Yang, *Observation of Intermingled Basins in Coupled Oscillators Exhibiting Synchronized Chaos*, Physical Review E **54** (1996), 2486–2494. Distinct predecessor coupling, cited and displayed in reference 1.
