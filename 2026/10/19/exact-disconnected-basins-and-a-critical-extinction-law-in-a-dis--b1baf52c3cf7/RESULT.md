# Exact disconnected basins and a critical extinction law in a discontinuous logistic dispersal map

## Finding
Consider the single-population density-dependent dispersal map of Morozov, Almutairi, Petrovskii and Lai (2023), restricted to the natural nonnegative unit state interval:
\[
H(x)=\mu x(1-x)\{1+\varepsilon\operatorname{sgn}[x-\mu x(1-x)]\},\qquad 0\le x\le1,
\]
with \(\operatorname{sgn}(0)=0\). For every \(1<\mu<2\) and \(0<\varepsilon<1\) satisfying \(r_+=\mu(1+\varepsilon)\le3\), put
\[
a=1-\frac1\mu,\quad r_-=\mu(1-\varepsilon),\quad b=\frac{1+\sqrt{1-4a/r_+}}2,\quad p_+=1-\frac1{r_+}.
\]
Then \(0<a<1/2<b<1\), and the full basin decomposition on \([0,1]\) is as follows. Both \(a\) and \(b\) reach the fixed point \(a\) (the latter after exactly one step), while \(0\) and \(1\) reach \(0\). Every point in \((a,b)\) converges to the positive fixed point \(p_+\). Every point in \((0,a)\cup(b,1)\) eventually follows the logistic branch of parameter \(r_-\), and tends to
\[
p_-=1-\frac1{r_-}>0\quad\text{if }r_->1,\qquad 0\quad\text{if }r_-\le1.
\]
In particular, for uniformly distributed initial density on \([0,1]\), the exact probability of convergence to \(p_+\) is \(b-a\); the complementary lower-branch basin has length \(1-b+a\). At the exact extinction threshold \(r_-=1\), every lower-basin orbit satisfies \(\lim_{n\to\infty}n x_n=1\). For \(r_-<1\), every such orbit instead has \(x_n\sim C r_-^n\) with a finite \(C>0\) depending on the initial state.

The transition occurs at \(\varepsilon_c=1-1/\mu\): below it there are two positive attracting equilibria, at it the lower attractor becomes neutral extinction with the inverse-time law, and above it the lower basin becomes an extinction basin while the upper attractor persists. As \(\varepsilon\downarrow0\) at any fixed \(1<\mu<2\), the two positive attracting equilibria coalesce at \(a\), but the proportion selected by the upper branch tends to the nonzero value \(2/\mu-1\).

## Assumptions and scope
All parameters are real. The complete parameter domain is \(1<\mu<2\), \(0<\varepsilon<1\), and \(\mu(1+\varepsilon)\le3\). All initial conditions lie in the closed unit interval. No assertion concerns higher-growth parameters, noisy dynamics, or states outside this interval. A fixed discontinuity point is defined using \(\operatorname{sgn}(0)=0\), as in the mathematical sign convention.

## Proof
**Branch reduction.** The identity \(x-\mu x(1-x)=\mu x(x-a)\) gives \(H(x)=r_-x(1-x)\) on \((0,a)\), \(H(a)=a\), and \(H(x)=r_+x(1-x)\) on \((a,1)\); also \(H(0)=H(1)=0\). The discriminant defining \(b\) is positive. Indeed \(r_+>\mu\), so \(4a/r_+<4(\mu-1)/\mu^2<1\) for \(1<\mu<2\). Thus \(1/2<b<1\). Since \(r_+b(1-b)=a\), \(H(b)=a\); strict decrease of the right-hand logistic quadratic on \((b,1)\) implies \(H((b,1))\subset(0,a)\).

**Lower interval.** Because \(a<1/2\), the lower logistic quadratic increases on \([0,a]\) and its one-sided endpoint value is \(r_-a(1-a)=a(1-\varepsilon)<a\). Hence \((0,a)\) is forward invariant. For \(0<r_-<1\), the inequality \(0<x_{n+1}\le r_-x_n\) proves exponential extinction; \(\sum_n x_n<\infty\) makes \(\prod_n(1-x_n)\) converge to a positive limit, yielding the stated positive exponential prefactor. For \(r_-=1\), \(x_{n+1}=x_n(1-x_n)\to0\), and
\[
\frac1{x_{n+1}}-\frac1{x_n}=\frac1{1-x_n}\longrightarrow1,
\]
so Stolz–Cesàro gives \(n x_n\to1\). For \(1<r_-<2\), the logistic identity
\[
 r_-x(1-x)-p_-=(x-p_-)(1-r_-x)
\]
and \(|1-r_-x|<1\) for \(0<x<a<1/2\) imply convergence to \(p_-\); alternatively monotonicity of the lower branch proves the same fact. The inequality \(p_-<a\) follows from \(r_-<\mu\).

**Upper interval.** The right quadratic \(r_+x(1-x)=a\) has one root strictly below \(a\), since its value at \(a\) equals \(a(1+\varepsilon)>a\), and one root \(b>a\). Therefore \(r_+x(1-x)>a\) for \(a<x<b\). Its maximum \(r_+/4\) is smaller than \(b\): if \(r_+\le2\), this is immediate from \(b>1/2\). If \(2<r_+\le3\), then \(r_+/4\in(1/2,3/4]\), and
\[
r_+\frac{r_+}{4}\left(1-\frac{r_+}{4}\right)=\frac{r_+^2(4-r_+)}{16}\ge\frac12>a.
\]
The first inequality follows by differentiation on \([2,3]\). Because \(r_+/4>1/2\), it belongs to the open interval between the two roots and hence lies below \(b\). Thus \((a,b)\) is invariant. The fixed point \(p_+\) belongs to \((a,b)\).

For completeness, the classical convergence theorem for logistic maps at \(1<r\le3\) applies. A short verification of its no-period-two hypothesis is the exact factorization
\[
f_r(f_r(x))-x=-x(rx-r+1)\left[r^2x^2-r(r+1)x+r+1\right],\quad f_r(x)=rx(1-x).
\]
The quadratic's discriminant is \(r^2(r+1)(r-3)\le0\); at \(r=3\) its sole zero coincides with the ordinary positive fixed point. Consequently there is no primitive two-cycle. Coppel's interval-iteration theorem then shows that every orbit of this continuous logistic branch converges to a fixed point. Since the invariant interval \((a,b)\) contains only the positive logistic fixed point, its orbits converge to \(p_+\). (Equivalently, use the standard elementary global-convergence theorem for \(1<r\le3\).)

**Measures and singular selection.** The only exceptional starting states are \(0,1,a,b\). Interval lengths give the exact basin fractions. At \(\varepsilon=0\), the larger root of \(\mu x(1-x)=a\) is \(1/\mu\) because \(1<\mu<2\). Continuity of the explicit root for positive \(\varepsilon\to0\) yields \(\lim_{\varepsilon\downarrow0}(b-a)=2/\mu-1>0\), although both attracting equilibrium values tend to \(a\). Finally \(r_-=1\) rearranges exactly to \(\varepsilon=1-1/\mu\).

## Verification
A standalone checker (`checker.py`) verifies the exact logistic two-iterate factorization symbolically and samples admissible parameters, interval inclusions, basin convergence and the critical decay. The computations are checks of the formulas and are not used as substitutes for the infinite-trajectory proof above. Reproduce with `python checker.py` (Python 3 with SymPy).

## Relationship to prior work
Morozov, Almutairi, Petrovskii and Lai (2023), DOI 10.1016/j.chaos.2023.113707, introduce and investigate precisely this discontinuous single-species logistic dispersal map, emphasizing high-growth transients, intermittency and discontinuity-based trapping regions. Their published article, including section 2, the numerical parameter diagrams and Appendix A, does not present the present complete low-growth basin partition, exact uniform initial-condition probabilities, critical inverse-time extinction result or nonvanishing small-dispersal selection fraction. The standard logistic convergence theorem is prior mathematics and is explicitly used, not claimed as new. A later work, Morozov et al., DOI 10.1016/j.biocon.2023.110419, treats related density-dependent dispersal phenomena; the material available for comparison does not resolve priority over possible differently phrased basin calculations.

## Limitations
This is a complete classification solely for the stated weak-growth parameter strip and unit initial interval. The result does not classify transient chaotic regimes elsewhere, does not assign a limiting state for initial distributions outside the specified interval, and is not an independent mathematical audit. Novelty remains subject to specialized or unindexed antecedents, particularly subsequent ecological analyses. The formulas use the exact mathematical sign convention at the discontinuity.

## References
1. A. Yu. Morozov, D. Almutairi, S. V. Petrovskii and Y.-C. Lai, “Long transients in discontinuous time-discrete models of population dynamics,” *Chaos, Solitons & Fractals* **174** (2023), 113707; DOI: 10.1016/j.chaos.2023.113707; first indexed public publication 2023-07-12 (OpenAlex W4384103761).
2. A. Yu. Morozov, D. Almutairi, S. V. Petrovskii and A. Hastings, “Regime shifts, extinctions and long transients in models of population dynamics with density-dependent dispersal,” *Biological Conservation* **290** (2024), 110419; DOI: 10.1016/j.biocon.2023.110419 (priority-risk comparison only).
3. W. A. Coppel, “The solution of equations by iteration,” *Proc. Cambridge Philos. Soc.* **51** (1955), 41–43 (standard interval-map convergence theorem).
