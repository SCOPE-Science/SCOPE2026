# Global equilibrium classification and a high-bias survival transition in two-patch logistic chemotaxis

## Finding

For the two-patch exponential-preference Keller–Segel system with logistic patch growth, there is a **sharp and complete nonnegative equilibrium diagram**: exactly two equilibria (extinction and homogeneous carrying capacity) at or below the linear threshold, and exactly four above it, including precisely one pair of nonuniform positive equilibria. The nonuniform branches cannot fold. Their total population and chemoattractant decrease strictly with chemotactic sensitivity; in the infinite-bias limit, both patches retain positive populations if and only if local growth exceeds half the population-migration rate.

Precisely, put \(B=\beta+\eta_c/2\), \(\gamma=2r/\eta_n\), and
\[
\chi_c=\frac{B}{\alpha K}(1+\gamma).
\]
For \(\chi\le\chi_c\), the complete nonnegative equilibrium set is \(\{(0,0,0,0),(K,K,\alpha K/\beta,\alpha K/\beta)\}\). For every \(\chi>\chi_c\) exactly one positive asymmetry parameter \(t\) solves the following equation, and the two nonuniform equilibria are its displayed state and the simultaneous interchange of patch indices:
\[
\begin{gathered}
\chi=\Xi_\gamma(t):=\frac{B(1+t^2)}{\alpha Kt}
\left[\operatorname{artanh}t+
\operatorname{artanh}\left(\frac{\gamma t}{1+(1-\gamma)t^2}\right)\right],\\
(n_1,n_2)=\frac{K}{1+t^2}(1+t,1-t),\\
(c_1,c_2)=\frac{\alpha K}{\beta(1+t^2)}(1,1)
+\frac{\alpha Kt}{B(1+t^2)}(1,-1).
\end{gathered}
\]
The admissible interval is \(0<t<t_\gamma\), where
\[
t_\gamma=\begin{cases}
1,&0<\gamma\le1,\\
\frac{2}{\gamma+\sqrt{\gamma^2+4(\gamma-1)}},&\gamma>1.
\end{cases}
\]
The scalar function \(\Xi_\gamma\) is a strict increasing bijection from this interval onto \((\chi_c,\infty)\), and
\[
\Xi_\gamma(t)=\chi_c+
\frac{B}{\alpha K}\frac{4+3\gamma^2+\gamma^3}{3}\,t^2+O(t^4)
\quad(t\downarrow0).
\]
In particular, both patch densities tend to positive limits as \(\chi\to\infty\) if \(\gamma>1\), whereas the smaller patch tends to zero if \(\gamma\le1\). This sharp survival transition is at \(2r=\eta_n\).

## Assumptions and scope

All parameters \(r,\eta_n,\eta_c,\alpha,\beta,K\) are real and strictly positive; chemotactic sensitivity \(\chi\ge0\). Consider the graph model of Kim–Zhang–Zhao–Cooney [1] specialized to exactly two connected patches with unit off-diagonal adjacency and per-patch logistic response \(f(n)=rn(1-n/K)\). Writing \(p_i=e^{\chi c_i}/(e^{\chi c_1}+e^{\chi c_2})\), its autonomous ODE is
\[
\begin{aligned}
\dot n_1&=\tfrac{\eta_n}{2}(n_2p_1-n_1p_2)+rn_1(1-n_1/K),\\
\dot n_2&=-\tfrac{\eta_n}{2}(n_2p_1-n_1p_2)+rn_2(1-n_2/K),\\
\dot c_1&=\tfrac{\eta_c}{4}(c_2-c_1)+\alpha n_1-\beta c_1,\\
\dot c_2&=\tfrac{\eta_c}{4}(c_1-c_2)+\alpha n_2-\beta c_2.
\end{aligned}
\]
The equilibrium classification is within the nonnegative state orthant. It concerns stationary points, not stability, transient dynamics, basins of attraction, or general graphs. The threshold \(\chi_c\) agrees with [1, Eq. (3.18)] for logistic growth because \(f'(K)=-r\).

## Proof

**Boundary and symmetric states.** At a nonnegative equilibrium, if \(n_1=0<n_2\), then \(\dot n_1=\eta_n n_2p_1/2>0\), a contradiction, and likewise with indices exchanged. If both populations vanish, the linear chemical subsystem has only the zero equilibrium. For \(n_1,n_2>0\), define their mean \(u=(n_1+n_2)/2>0\) and asymmetry \(s=(n_1-n_2)/(n_1+n_2)\in(-1,1)\). Adding the population equations gives
\[
0=f(u(1+s))+f(u(1-s))=2ru\left[1-\frac{u(1+s^2)}K\right],
\]
so \(u=K/(1+s^2)\). Adding and subtracting the chemical equations uniquely gives
\[
\frac{c_1+c_2}{2}=\frac{\alpha u}{\beta},\qquad
\frac{c_1-c_2}{2}=\frac{\alpha u s}{B}.
\]
If \(s=0\), the unique positive solution is the homogeneous carrying-capacity equilibrium listed above. If \(s\ne0\), exchange patches to take \(s=t>0\).

**Exact scalar reduction.** Put \(z=\chi\alpha ut/B\). The softmax migration flux is exactly
\[
n_2p_1-n_1p_2=u(\tanh z-t).
\]
The first population balance, together with \(u=K/(1+t^2)\), is therefore equivalent to
\[
\tanh z=t+\gamma t\frac{1-t^2}{1+t^2}.
\tag{1}
\]
Introduce \(w=\gamma t/[1+(1-\gamma)t^2]\). Direct algebra gives
\[
t+\gamma t\frac{1-t^2}{1+t^2}=\frac{t+w}{1+tw}.
\]
Because \(0<t<1\), this right-hand side lies in \((0,1)\) precisely when \(0<w<1\). For \(\gamma\le1\), this holds for all \(t\in(0,1)\); for \(\gamma>1\), it holds precisely when \(0<t<t_\gamma\), where \(t_\gamma\) is the unique positive solution of \((\gamma-1)t^2+\gamma t=1\). Taking inverse hyperbolic tangents in (1) yields \(z=\operatorname{artanh}t+\operatorname{artanh}w\), which is exactly the claimed equation \(\chi=\Xi_\gamma(t)\). Conversely, inserting any such \(t\) and \(\chi\) into these equations makes all four equilibrium residuals zero, so the reduction has lost no positive stationary states.

**No folds and global count.** Rewrite the parameter curve as
\[
\Xi_\gamma(t)=\frac{B}{\alpha K}\left[
(1+t^2)\frac{\operatorname{artanh}t}{t}
+\gamma\frac{1+t^2}{1+(1-\gamma)t^2}
\frac{\operatorname{artanh}w}{w}\right].
\]
On \((0,1)\), \(v\mapsto\operatorname{artanh}(v)/v\) is strictly increasing (for example from its positive-coefficient power series). Throughout the admissible interval, the denominator \(1+(1-\gamma)t^2\) is positive, \(w\in(0,1)\), and
\[
w'(t)=\gamma\frac{1-(1-\gamma)t^2}{[1+(1-\gamma)t^2]^2}>0.
\]
Furthermore the factor \((1+t^2)/[1+(1-\gamma)t^2]\) is strictly increasing, its derivative being \(2\gamma t/[1+(1-\gamma)t^2]^2>0\). Both bracketed terms are therefore strictly increasing. At \(t\downarrow0\) their sum tends to \(1+\gamma\), giving \(\Xi_\gamma(0+)=\chi_c\). At the upper endpoint either \(t\uparrow1\) or \(w\uparrow1\), so one inverse hyperbolic tangent diverges; \(\Xi_\gamma(t)\to\infty\). This proves strict bijectivity, existence, uniqueness up to swapping, and the exact global equilibrium counts, including the critical equality.

**Onset, population response and high-bias dichotomy.** Expanding \(\operatorname{artanh}t\) and \(w=\gamma t+\gamma(\gamma-1)t^3+O(t^5)\) proves the displayed quadratic expansion with positive coefficient. The total stationary population on the branch is exactly \(2K/(1+t^2)\); the total chemical concentration is \(2\alpha K/[\beta(1+t^2)]\). Since \(t\) increases strictly with \(\chi\), both totals decrease strictly. As \(\chi\to\infty\), strict bijectivity forces \(t\uparrow t_\gamma\). For \(\gamma\le1\), \(t_\gamma=1\) and the two population limits are \(K\) and \(0\). For \(\gamma>1\), \(0<t_\gamma<1\), and the limits are \(K(1\pm t_\gamma)/(1+t_\gamma^2)\), both strictly positive. All claims follow.

## Verification

The accompanying self-contained Python script `check.py` evaluates all four original ODE residuals at 72 branch states spanning eight growth-to-migration ratios and nine relative asymmetries each; it checks numerical strict monotonicity at those sampled points and verifies the derived onset coefficient numerically. Run with `python3 check.py` using the Python standard library. It is a **finite algebraic diagnostic**, not an exhaustive proof; universal uniqueness, monotonicity and limits are established in the preceding analytic argument.

## Relationship to prior work

Kim, Zhang, Zhao and Cooney [1, Sections 3 and 5] derive the graph chemotaxis system, the two-patch homogeneous linear instability threshold, numerically plot patterned outcomes, and establish a Jensen-based mass deficit for nonuniform steady states. Here that threshold is upgraded **for the specific two-patch logistic softmax model** to a complete nonlinear count of all nonnegative stationary states with an explicit globally monotone branch. The Jensen mass deficit itself is not new; the strict global dependence on sensitivity, the absence of additional/folded branches and the high-bias survival transition are the asserted additions.

Wang, Yan and Gai [2] prove local and global-branch results for a continuum one-dimensional Neumann Keller–Segel PDE; their differential operator and boundary conditions are not this two-patch softmax migration ODE. General logistic multiple-patch models with fixed migration [3] do not fix the state-dependent exponential movement law. The claimed theorem is not an assertion for those broader classes.

## Limitations

No assertion is made about stability of nonhomogeneous equilibria, uniqueness of trajectories, global attractors, transient population monotonicity, arbitrary connected graphs, nonlogistic reaction terms, or graphon continuum limits. The high-bias threshold concerns *stationary patch populations*, not finite-time extinction. Broader historical literature may contain a general theorem subsuming part of this calculation.

## References

[1] D. Kim, Y. Zhang, Y. Zhao, D. B. Cooney, "The Keller–Segel Model for Chemotaxis on Metapopulation Graphs and Graphons", arXiv:2610.31049v1 (public 2026-10-22), https://arxiv.org/html/2610.31049v1, especially Eq. (3.6), Sec. 3 and Sec. 5.4.

[2] Q. Wang, J. Yan, C. Gai, "Qualitative analysis of stationary Keller–Segel chemotaxis models with logistic growth", arXiv:1312.0258v4, https://arxiv.org/html/1312.0258v4, Secs. 2–4.

[3] "The multi-patch logistic equation with asymmetric migration", arXiv:2103.13144, https://arxiv.org/abs/2103.13144 (contextual abstract only; the full text was not inspected).
