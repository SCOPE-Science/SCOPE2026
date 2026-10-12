# Sharp coexistence-equilibrium census for a refuge-and-cooperation Ricker map

## Finding

For every \(r>0\), \(0<b<1\), \(c\geq 0\), and \(\beta>0\), the normalized cooperative-hunting Ricker system below has at most **two** strictly positive coexistence equilibria. Their number is completely determined by the following sharp criterion.

Let \(R=\beta b\) and \(c_0=\tfrac12+\tfrac br\). If \(c\leq c_0\), there is exactly one positive equilibrium when \(R>1\) and none when \(R\leq1\). If \(c>c_0\), define the scalar equilibrium function \(q\) below and its unique strict maximum \(q_*>1\); set \(R_*=q_*^{-1}\). Then the equilibrium count is

\[
\begin{array}{c|ccccc}
R & (0,R_*) & R_* & (R_*,1) & 1 & (1,\infty)\\\hline
\text{number of positive equilibria} & 0 & 1\ \text{(tangent)} & 2 & 1 & 1.
\end{array}
\]

The tangency at \(R=R_*\) is a nondegenerate fold of the scalar equilibrium equation: its second derivative in the predator coordinate is negative and its first derivative with respect to \(R\) is nonzero. This statement concerns equilibrium branches, not nonlinear dynamical stability.

## Assumptions and scope

The exact dimensionless map studied is

\[
\begin{aligned}
x_{n+1}&=x_n\bigl[1-b+b e^{-y_n(1+c y_n)}\bigr]e^{r(1-x_n)},\\
y_{n+1}&=\beta b x_n\bigl(1-e^{-y_n(1+c y_n)}\bigr).
\end{aligned}
\]

Here \(x_n\) and \(y_n\) are normalized prey and predator densities; \(r>0\) is Ricker growth, \(0<b<1\) is the vulnerable prey fraction, \(c\ge0\) controls cooperation and \(\beta>0\) controls conversion. A coexistence equilibrium means \(x>0\) **and** \(y>0\). No restriction \(r<2\) is imposed.

For \(y>0\), put

\[
\begin{aligned}
u(y)&=y+c y^2, &s(y)&=1-e^{-u(y)},\\
x(y)&=1+\frac1r\log(1-bs(y)),\\
q(y)&=\frac{s(y)\,[r+\log(1-bs(y))]}{r y}.
\end{aligned}
\]

The physically admissible domain is the interval \(I=\{y>0:x(y)>0\}\), containing all sufficiently small positive \(y\). Since \(s\) increases strictly, \(x\) decreases strictly, and \(I\) is either \((0,\infty)\) or \((0,y_{\rm end})\). The equation for a positive equilibrium is exactly \(R q(y)=1\), with \(x=x(y)\) and \(R=\beta b\). Moreover \(\lim_{y\downarrow0}q(y)=1\), and \(q(y)\) tends to zero at the far end of \(I\).

## Proof

**Step 1 — an elementary concavity transform.** Define \(G(s)=s[r+\log(1-bs)]\) on \(0\le s<1\), and let \(T(y)=G(s(y))\), so \(q(y)=T(y)/(r y)\). Its derivatives are

\[
\begin{aligned}
G'(s)&=r+\log(1-bs)-\frac{bs}{1-bs},\\
G''(s)&=-\frac{b(2-bs)}{(1-bs)^2}<0,\\
G'''(s)&=-\frac{b^2(3-bs)}{(1-bs)^3}<0.
\end{aligned}
\]

In particular \(G'(0)=r>0\), and \(G'\) decreases strictly. Therefore the set \(J=\{y>0:G'(s(y))>0\}\) is an initial interval. On \(I\setminus J\), \(T>0\) and \(T'\le0\), so \(q'<0\). All possible increases and extrema of \(q\) must occur in \(I\cap J\).

**Step 2 — a strictly decreasing curvature comparison.** Let \(w(y)=1+2cy\). Direct differentiation gives

\[
s'(y)=w e^{-u},\quad s''(y)=e^{-u}(2c-w^2),\quad
Q(y):=\frac{s''}{(s')^2}=e^u\left(\frac{2c}{w^2}-1\right).
\]

A second differentiation yields the strict identity

\[
Q'(y)=-\frac{e^{u(y)}}{w(y)^3}\left[(w(y)^2-c)^2+7c^2\right]<0.
\]

For \(y\in J\), set \(P(s)=-G''(s)/G'(s)>0\). Since \(G''<0\), \(G'''<0\) and \(G'>0\),

\[
\frac{dP}{ds}=\frac{[G''(s)]^2-G'''(s)G'(s)}{[G'(s)]^2}>0.
\]

The chain rule now gives

\[
T''(y)=G'(s(y))\,[s'(y)]^2\,\bigl[Q(y)-P(s(y))\bigr].
\]

Thus \(Q(y)-P(s(y))\) is **strictly decreasing** on \(J\). Consequently \(T''\), as long as \(G'>0\), can change sign **at most once and only from positive to negative**. At the left endpoint,

\[
Q(0)=2c-1,\quad P(0)=\frac{2b}{r},\quad
T''(0)=2r\left(c-\frac12-\frac br\right).
\]

**Step 3 — uniqueness of the maximum.** Define \(W(y)=yT'(y)-T(y)\), so \(q'(y)=W(y)/(r y^2)\), \(W(0)=0\), and \(W'(y)=yT''(y)\). If \(c\le c_0\), Step 2 shows \(T''<0\) for every positive \(y\in J\); hence \(W<0\) there, and also on \(I\setminus J\). Thus \(q\) is strictly decreasing.

If \(c>c_0\), then \(T''>0\) near zero. Step 2 shows that \(T''\) becomes negative before the end of \(J\): if \(G'\) vanishes at a finite point, \(P\) diverges there; if \(G'>0\) always, \(Q(y)\to-\infty\). Hence \(W\) initially increases strictly, then decreases strictly as long as \(G'>0\). It must cross zero: if \(G'\) vanishes, \(W=-T<0\) at that point; otherwise \(T(y)\to G(1)>0\) and \(yT'(y)\to0\), so \(W(y)\to-G(1)<0\). After \(G'\le0\), \(W<0\). Therefore \(W\) has exactly one positive zero \(y_*\in I\), with \(q'>0\) before and \(q'<0\) after it. Furthermore \(T''(y_*)<0\), which implies \(q''(y_*)=T''(y_*)/(r y_*)<0\). The strict maximum \(q_*=q(y_*)\) exceeds \(q(0+)=1\).

**Step 4 — exact count and fold.** The graph of \(q\) is continuous and positive on \(I\), tends to one at its left endpoint, and tends to zero at its right endpoint. In the decreasing case, \(R q=1\) has one solution precisely for \(R>1\). In the one-maximum case, horizontal lines at height \(1/R\) yield the five stated counts. At \(R=R_*\), the scalar equation \(F(R,y)=R q(y)-1\) satisfies

\[
F(R_*,y_*)=F_y(R_*,y_*)=0,\qquad
F_{yy}(R_*,y_*)=R_*q''(y_*)<0,\qquad
F_R(R_*,y_*)=q_*>0.
\]

This is a nondegenerate algebraic fold. Every solution gives exactly one positive prey coordinate \(x(y)\); hence there can never be a third coexistence equilibrium. \(\square\)

## Verification

The curvature identity and derivatives can be checked independently by direct differentiation. The included script `verify.py` checks these identities symbolically and reproduces a published two-equilibrium parameter example numerically; the global count is established by the analytic sign proof above, not by numerical sampling.

For the paper's illustrative choice \(r=1\), \(b=0.49\), \(c=3\), \(\beta=2\), a high-precision scalar computation gives \(y_*\approx0.1747978779\), \(q_*\approx1.1752901285\), and \(R_*\approx0.8508537388\). Since \(R=0.98\), exactly two positive equilibria follow; the scalar roots are approximately \(0.01044918157\) and \(0.36448793773\), agreeing with the source's displayed equilibria.

## Relationship to prior work

De Silva and Jang (2026), model (2.5), Proposition 3.2, analyze the predator nullcline and give an intersection criterion, but expressly note that their geometric argument does not exclude additional intersections when \(2c>1\) and \(\beta b<1\). The result above proves a sharp global two-intersection ceiling for their actual Ricker recruitment law and settles the equality \(\beta b=1\) case.

Jang and Yousef (2023), Theorem 2.4, prove an at-most-two result for a **different** Beverton–Holt-type prey recruitment, whose prey nullcline is affine in \(e^{-u}\). That proof does not itself establish the curvature bound for the logarithmic Ricker nullcline. Chou, Chow, Hu and Jang (2021) study cooperative hunting with Ricker prey growth but without the present proportional prey refuge. Their abstract establishes dependence of equilibrium counts on cooperation; the complete text was not available for a decisive theorem-by-theorem comparison. A separate result for this 2026 Ricker map identifies instability of a lower equilibrium **assuming exactly two equilibria**; its implication does not bound the total number.

## Limitations

The theorem counts stationary strictly positive solutions of this specific two-dimensional deterministic model only. It does not infer attraction basins, global extinction, persistence, stability of the fold branches, or higher-period dynamics. The fold threshold is defined exactly through a unique one-dimensional maximizer, not asserted to have an elementary closed form. No claim is made for a change in the biological predation law or for demographic stochasticity. Literature outside the inspected sources may contain related implicit unimodality arguments.

## References

1. T. M. M. De Silva and S. R.-J. Jang, *Persistence, extinction, and chaotic dynamics in a predator-prey system with cooperative hunting and prey refuge*, AIMS Mathematics **11** (2026), 21412–21440. DOI: 10.3934/math.2026868. Published July 17, 2026.
2. S. R.-J. Jang and A. M. Yousef, *Effects of prey refuge and predator cooperation on a predator–prey system*, Journal of Biological Dynamics **17** (2023), article 2242372. DOI: 10.1080/17513758.2023.2242372.
3. Y.-H. Chou, Y. Chow, X. Hu and S. R.-J. Jang, *A Ricker-type predator–prey system with hunting cooperation in discrete time*, Mathematics and Computers in Simulation **190** (2021), 570–586. DOI: 10.1016/j.matcom.2021.06.003.
