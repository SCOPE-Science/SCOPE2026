# A universal right-endpoint obstruction removes two advertised UWG hazard regimes
## Finding
Let the unit-Weibull baseline have
\[
G(x)=\exp\!\left[-\alpha(-\log x)^\beta\right],
\qquad 0<x<1,\quad \alpha,\beta>0,
\]
and let
\[
\Pr(N=n)=(1-\rho)\rho^{n-1},
\qquad n=1,2,\ldots,\quad 0<\rho<1.
\]
For independent baseline lifetimes \(X_1,X_2,\ldots\), define the series-system lifetime
\[
Y=\min(X_1,\ldots,X_N).
\]

Then its hazard \(h_Y\) has the universal right-endpoint law
\[
\boxed{\lim_{x\uparrow1}(1-x)h_Y(x)=\beta.}
\]
In particular,
\[
h_Y(x)\longrightarrow+\infty
\qquad(x\uparrow1)
\]
for every admissible \((\alpha,\beta,\rho)\).

Therefore the hazard cannot be globally decreasing on \((0,1)\). It also cannot be globally unimodal in the usual reliability sense of an upside-down-bathtub hazard: nondecreasing up to one interior maximum and nonincreasing thereafter. Both properties would make the hazard bounded above on every sufficiently late part of the support, contradicting the right-endpoint divergence.

The 2026 UWG article advertises monotonic decreasing and unimodal hazard profiles among the model's global hazard shapes. Under the standard meanings above, those two regimes are impossible. Its published hazard figure is consistent with the obstruction at the endpoint: every displayed curve ultimately rises sharply as \(x\) approaches \(1\), including curves that can look decreasing or hump-shaped over an earlier finite window.

There is also a left-endpoint classification:
\[
h_Y(x)\sim
\frac{\alpha\beta}{1-\rho}
(-\log x)^{\beta-1}
\exp\!\left[-\alpha(-\log x)^\beta-\log x\right]
\qquad(x\downarrow0).
\]
Consequently,
\[
\lim_{x\downarrow0}h_Y(x)=
\begin{cases}
+\infty, & 0<\beta<1,\\
+\infty, & \beta=1,\ 0<\alpha<1,\\
(1-\rho)^{-1}, & \beta=1,\ \alpha=1,\\
0, & \beta=1,\ \alpha>1,\\
0, & \beta>1.
\end{cases}
\]
Thus \(0<\beta<1\) forces divergence at both endpoints and therefore at least one interior hazard minimum.

## Assumptions and scope
The geometric convention is stated explicitly:
\[
\Pr(N=n)=(1-\rho)\rho^{n-1}.
\]
Using the alternative convention in which the success parameter is written instead of the continuation parameter only relabels \(\rho\); the endpoint conclusion is unchanged.

“Globally unimodal hazard” means the standard upside-down-bathtub shape: there is an interior point after which the hazard is nonincreasing. The result does not rule out a local hump followed by a later valley and terminal increase; such a curve is not globally unimodal.

The claim concerns the hazard shape on the full mathematical support \((0,1)\), not how a curve may appear on a truncated plotting window.

## Proof
Write the unit-Weibull survival as
\[
S_0(x)=1-G(x).
\]
Conditional on \(N=n\),
\[
\Pr(Y>x\mid N=n)=S_0(x)^n.
\]
Summing over the positive geometric law gives
\[
S_Y(x)
=
\sum_{n\ge1}(1-\rho)\rho^{n-1}S_0(x)^n
=
\frac{(1-\rho)S_0(x)}
{1-\rho S_0(x)}.
\]
Since \(1-\rho S_0(x)=1-\rho+\rho G(x)\), differentiation gives
\[
f_Y(x)=
\frac{(1-\rho)g(x)}
{[1-\rho+\rho G(x)]^2},
\]
where
\[
g(x)=
\frac{\alpha\beta}{x}
(-\log x)^{\beta-1}
\exp[-\alpha(-\log x)^\beta].
\]
Hence
\[
h_Y(x)
=
\frac{g(x)}
{[1-G(x)][1-\rho+\rho G(x)]}.
\]

Set \(t=-\log x\). As \(x\uparrow1\), one has \(t\downarrow0\) and
\[
1-G(x)
=
1-e^{-\alpha t^\beta}
=
\alpha t^\beta(1+o(1)),
\]
while
\[
g(x)=\frac{\alpha\beta}{x}t^{\beta-1}(1+o(1)),
\qquad
1-\rho+\rho G(x)=1+o(1).
\]
Therefore
\[
h_Y(x)=\frac{\beta}{x\,t}(1+o(1)).
\]
Since
\[
\frac{1-x}{x(-\log x)}\longrightarrow1,
\]
it follows that
\[
(1-x)h_Y(x)\longrightarrow\beta.
\]

A globally decreasing hazard is bounded above on \([x_0,1)\) by \(h_Y(x_0)\) for every fixed \(x_0>0\), contradicting \(h_Y(x)\to\infty\). Likewise, a globally upside-down-bathtub hazard is nonincreasing after its mode, hence bounded on its terminal interval, giving the same contradiction.

For the left endpoint, \(t\to\infty\), \(G(x)\to0\), and
\[
[1-G(x)][1-\rho+\rho G(x)]\to1-\rho.
\]
Because \(x=e^{-t}\),
\[
g(x)
=
\alpha\beta\,t^{\beta-1}
e^{t-\alpha t^\beta}.
\]
The five cases in the finding follow by comparing \(t\) and \(t^\beta\). When the hazard tends to \(+\infty\) at both endpoints, continuity and finiteness at interior points force attainment of a minimum at some interior point.

## Verification
The included checker evaluates the exact hazard formula at increasingly close right-endpoint arguments for several widely separated parameter triples and verifies convergence of
\[
(1-x)h_Y(x)
\]
to \(\beta\).

It also stress-checks the left-endpoint classification for representative cases with \(\beta<1\), \(\beta=1\), and \(\beta>1\).

These finite calculations are consistency checks only. The endpoint theorem is proved by the exact geometric-series identity and the asymptotic expansions above.

## Relationship to prior work
The 2026 UWG article introduces the unit-Weibull geometric model as a geometric series-system compound and advertises increasing, decreasing, unimodal, and bathtub-shaped hazards. Its Figure 2 shows the hazard curves used to support the shape discussion.

Barreto-Souza, de Morais, and Cordeiro's Weibull-geometric model uses the same positive-geometric minimum construction on an unbounded Weibull baseline. Their full preprint derives
\[
h(x)=\alpha\beta^\alpha x^{\alpha-1}
\{1-\rho e^{-(\beta x)^\alpha}\}^{-1}
\]
and proves that genuinely decreasing hazards can occur there. That result does not transfer to the bounded unit-Weibull baseline, whose right endpoint imposes a different singular geometry.

Mazucheli and coauthors give the unit-Weibull baseline as the exponential transform of a Weibull variable. The present result combines that bounded endpoint geometry with the geometric minimum transform and isolates the exact terminal hazard constant \(\beta\).

Focused searches for the UWG model together with endpoint hazard asymptotics, decreasing-hazard impossibility, upside-down-bathtub impossibility, geometric compounding, and correction notices found no published statement covering the endpoint obstruction or correcting the advertised hazard list.

## Limitations
The result excludes only global decreasing and global upside-down-bathtub hazard shapes. It does not classify all possible numbers of interior extrema, and it does not rule out curves that decrease over a substantial initial interval before eventually turning upward.

The target article's full body was not exposed by the publisher's indexed HTML endpoint during this check. The scientific premises used here were independently reconstructed from the article's stated series-system construction, its published hazard figure, the full primary Weibull-geometric precursor, and the established unit-Weibull baseline formulas.

No claim is made about whether any particular finite plotting range could visually resemble a decreasing or single-hump curve before the terminal upturn becomes visible.

## References
1. M. Namsaw, B. Das, M. S. Eliwa, and M. F. Abouelenein, “The unit-Weibull geometric distribution: Mathematical properties, identifiability, and asymptotic analysis with applications to data modeling,” AIMS Mathematics 11 (2026), 29488–29528. DOI: 10.3934/math.20261171.
2. W. Barreto-Souza, A. L. de Morais, and G. M. Cordeiro, “The Weibull-geometric distribution,” Journal of Statistical Computation and Simulation 81 (2011), 645–657. DOI: 10.1080/00949650903436554. Preprint: arXiv:0809.2703.
3. J. Mazucheli, A. F. B. Menezes, L. B. Fernandes, R. P. de Oliveira, and M. E. Ghitany, “The unit-Weibull distribution as an alternative to the Kumaraswamy distribution for the modeling of quantiles conditional on covariates,” Journal of Applied Statistics 47 (2020), 954–974. DOI: 10.1080/02664763.2019.1657813.
