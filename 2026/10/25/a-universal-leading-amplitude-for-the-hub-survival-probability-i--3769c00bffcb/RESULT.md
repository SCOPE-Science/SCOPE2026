# A universal leading amplitude for the hub-survival probability in weighted wheel dimer adsorption

## Finding
For every integer \(n\geq 3\) and every spoke-rate ratio \(\lambda>0\), run irreversible random sequential dimer adsorption on the wheel \(W_{n+1}=K_1*C_n\): each rim edge attempts adsorption at rate one, each spoke at rate \(\lambda\), and a successful attempt permanently occupies its two previously vacant endpoints. Write \(P_n(\lambda)\) for the probability that the central vertex remains vacant forever. For odd \(n\), \(P_n(\lambda)=0\). For even \(n=2m+2\geq4\), let \(a=1+\lambda\), set \(q_0=1\), and define, for every integer \(m\geq1\),
\[
q_m=\frac{1}{2am-1}\sum_{j=0}^{m-1}q_jq_{m-1-j}.
\]
Then the exact hub-survival law is \(P_{2m+2}(\lambda)=q_m/a\). Its generating function, with \({}_0F_1\) denoting the standard hypergeometric limit function, is
\[
\sum_{m\geq0}q_mz^m=\frac{{}_0F_1\left(;1-\frac{1}{2a};\frac{z}{4a^2}\right)}{{}_0F_1\left(;-\frac{1}{2a};\frac{z}{4a^2}\right)}.
\]
Define \(U_a(z)={}_0F_1(; -1/(2a);z/(4a^2))\) and let \(\rho_a\) be its unique positive real zero. This zero is simple, strictly dominant in modulus among all complex zeros, and \(\rho_a>1\). For each fixed \(a>1\) there exists \(R_a>\rho_a\) such that
\[
P_{2m+2}(\lambda)=2\rho_a^{-m-1}+O_a(R_a^{-m})\qquad(m\to\infty).
\]
In particular, the *leading amplitude is exactly two for every positive rate ratio*, while \(\rho_a\) increases strictly with the spoke-rate ratio. The rare-event probability is therefore exponentially decreasing with the rim size, and more rapid spoke deposition suppresses hub survival.

## Assumptions and scope
The graph is a finite undirected simple wheel with one center and a cycle of \(n\geq3\) rim vertices. Each edge has an independent rate-constant Poisson process of attempts. Initially all vertices are vacant. Attempts across an already occupied endpoint are rejected; successful dimers never depart. Time extends to the absorbing jammed state. A zero-rate spoke is excluded: for \(\lambda=0\), the central vertex is isolated and survives with probability one, producing a singular long-time boundary. Only the eventual central-vacancy probability, not the complete joint law of occupied sites or the jamming time, is asserted.

## Proof
**Step 1: Parity and first-event splitting.** If the central vertex stays vacant, every rim vertex must eventually be paired by a rim dimer: a rim vertex that is vacant in a jammed configuration would have an available spoke to the vacant center, and at positive rate such a spoke would eventually succeed with probability one. This is impossible on an odd rim, proving \(P_n=0\) for odd \(n\).

Suppose the rim is even. While every vertex is vacant, the first successful dimer is selected from \(n\) rim edges at rate one each and \(n\) spokes at rate \(\lambda\) each. The probability it lies on the rim is \(1/a\). By rotational invariance, every rim edge is equivalent. After a rim dimer is placed, the other \(n-2\) rim vertices form a path whose available rim edges have rate one and whose spokes to the still-vacant center have rate \(\lambda\). The independent memoryless Poisson clocks make the subsequent event of completing the path by rim dimers without ever accepting a spoke independent of the past. Let \(q_m\) denote precisely this no-spoke perfect-rim-matching probability for a path of \(2m\) vacant rim vertices, with \(q_0=1\). Hence \(P_{2m+2}=q_m/a\).

**Step 2: Exact path recursion.** For a path with \(2m\) vacant vertices, the initial successful edge is selected from \(2m-1\) path edges (rate one each) and \(2m\) spokes (rate \(\lambda\) each), with total rate \(2am-1\). If the first chosen edge is a spoke, the desired event is impossible. If it is the path edge joining sites \(j\) and \(j+1\), its adsorption splits the vacant path into the independent intervals containing \(j-1\) and \(2m-j-1\) vertices. Only edges at even-spaced split positions give two even paths, indexed by \(j=0,\ldots,m-1\), whose lengths are \(2j\) and \(2(m-1-j)\). Conditional on the first rim edge, subsequent success probabilities multiply because the residual attempts have independent clocks and never interact across the occupied dimer. Summing the first-edge probabilities proves exactly
\[
(2am-1)q_m=\sum_{j=0}^{m-1}q_jq_{m-1-j}.
\]
All rates and denominators are strictly positive for \(a>1\), so this recurrence uniquely defines positive probabilities.

**Step 3: Solving the generating-function equation.** With \(f(z)=\sum_{m\geq0}q_mz^m\), multiplying the recursion by \(z^m\) and summing yields
\[
2azf'(z)=f(z)-1+zf(z)^2,\qquad f(0)=1.
\]
Put \(f=-2aU'/U\), where primes denote ordinary derivatives in \(z\). Straight substitution gives the linear equation
\[
4a^2zU''-2aU'-U=0,\qquad U(0)=1,\quad U'(0)=-\frac1{2a}.
\]
The unique analytic solution is \(U_a(z)={}_0F_1(; -1/(2a);z/(4a^2))\). By the hypergeometric derivative identity,
\[
-2aU_a'(z)={}_0F_1\left(;1-\frac1{2a};\frac{z}{4a^2}\right),
\]
which proves the asserted generating-function ratio as a formal power series, and analytically near the origin.

**Step 4: Unique dominant zero.** Write \(U_a(z)=1-\sum_{j\geq1}c_jz^j\). The coefficient formula is
\[
c_j=\frac{(4a^2)^{-j}}{j!\frac1{2a}\prod_{\ell=1}^{j-1}(\ell-\frac1{2a})}>0\qquad (j\geq1).
\]
The empty product is one. This converges for every complex \(z\). Consequently, \(U_a(x)\) is strictly decreasing for real \(x\geq0\), starts at one, and tends to negative infinity (already the \(j=1\) term tends to infinity). Thus it has exactly one positive real zero \(\rho_a\), with \(U_a'(\rho_a)<0\), so the zero is simple. If \(|z|<\rho_a\), then \(|\sum c_jz^j|<\sum c_j\rho_a^j=1\), so \(U_a(z)\ne0\). At \(|z|=\rho_a\), equality in the triangle inequality and the strictly positive consecutive coefficients \(c_1,c_2,c_3\) requires the phases of all powers of \(z\) to coincide with one, hence \(z=\rho_a\). Thus no other complex zero lies on or inside the dominant circle. Isolated zeros of a nonzero entire function give a larger zero-free annulus, and hence a number \(R_a>\rho_a\) with no other zero in \(|z|\leq R_a\).

Near the simple zero, \(f(z)=-2aU_a'(z)/U_a(z)=-2a/(z-\rho_a)+\text{analytic}\). Subtracting the pole term makes \(f\) analytic throughout \(|z|\leq R_a\); Cauchy's coefficient estimate gives \(q_m=2a\rho_a^{-m-1}+O_a(R_a^{-m})\). Division by \(a\) yields the universal coefficient two in \(P_{2m+2}\).

**Step 5: Monotonicity and exponent boundary.** Rewrite the Taylor coefficients explicitly as
\[
c_j(a)=\frac{2}{4^j j!}\,\frac{a^{1-2j}}{\prod_{\ell=1}^{j-1}(\ell-1/(2a))}.
\]
For every \(j\geq1\), the numerator factor \(a^{1-2j}\) decreases strictly as \(a>1\) increases, and all denominator factors are nondecreasing, strictly increasing when present. Thus \(c_j(a)\) decreases strictly with \(a\). Hence for each fixed \(x>0\), \(\sum_{j\geq1}c_j(a)x^j\) decreases strictly with \(a\), forcing its level-one root \(\rho_a\) to increase strictly. Finally \(\rho_a>1\): at the boundary value \(a=1\), the entire function is \(U_1(z)=\cosh\sqrt z-\sqrt z\sinh\sqrt z\), so \(U_1(1)=e^{-1}>0\). Since \(c_j(a)<c_j(1)\) for \(a>1\), we have \(U_a(1)>U_1(1)>0\), which proves \(\rho_a>1\).

## Verification
A standalone Python standard-library program, `verify_wheel.py`, independently computes the full absorbing-chain outcome by exact rational dynamic programming on all occupied-vertex masks for each rim size \(3\) through \(10\) and rate ratios \(1/2\), \(1\), \(2\). It compares every result with the path recursion, independently checks the hypergeometric series through order \(35\), and tests high-precision dominant-zero/asymptotic behavior. Its reported total is 138 assertions passing. The finite checks support, but do not substitute for, the analytical proof for all \(n\) and \(\lambda\).

For reproducibility, run `python verify_wheel.py` in a Python 3 installation; no additional packages or external files are needed. At \(\lambda=1\), \(P_4=1/6\), \(P_6=1/21\), and \(\rho_2\approx3.47547269134629\).

## Relationship to prior work
Classical random sequential adsorption and random greedy matchings were studied by Pippenger (1989) and Dyer and Frieze (1991), respectively. Krapivsky (2020), Section IV-B, equations (48)–(53), derives the **unweighted one-dimensional perfect-packing recursion**, its Riccati solution, and its asymptotic constant. In the present notation it is precisely the \(a=1\) path recursion, with no positive-rate competing spokes; it is not claimed as a new finding. Cieśla and Barbasz (2012 preprint) model adsorption interactions in a two-dimensional surface setting; their model is different from graph-edge arrivals on a wheel. The contribution assessed here is the all-positive-spoke-rate hub-survival law on finite wheels together with the resulting hypergeometric ratio and rate-independent asymptotic amplitude. The full text of Pippenger (1989) was not available for comparison, leaving a genuine coverage risk that a general older result might imply the wheel specialization. The literature search was not exhaustive, and no absolute priority claim is made.

## Limitations
The assertion concerns the event of final central vacancy, not the full configuration distribution, correlations, or adsorption time. The graph is a wheel, with homogeneous rate within each of its two edge classes; arbitrary weighted graphs, other deposition objects, and reversible motion are not addressed. The asymptotic estimate fixes the rate ratio before sending the rim size to infinity. The boundary \(\lambda=0\) changes the physical event and is excluded. The model's infinite-time realization requires the usual almost-sure completion of all available positive-rate attempts; no finite-time speed estimates are established.

## References
1. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401. DOI: 10.1137/0402034.
2. M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* **2** (1991), DOI: 10.1002/rsa.3240020104.
3. M. Cieśla and J. Barbasz, “Modelling of Interacting Dimer Adsorption,” first publicly posted 2012-10-30, arXiv:1210.8098. https://arxiv.org/abs/1210.8098.
4. P. L. Krapivsky, “Large deviations in one-dimensional random sequential adsorption,” first posted 2020, arXiv:2009.08609, especially Section IV-B. https://arxiv.org/abs/2009.08609.
