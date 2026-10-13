# A unique reproduction threshold for endemic infection-induced hydra effects

## Finding

In the discrete-time Ricker–Poisson susceptible–infectious system of Strube, Elgart and Childs [1], with fixed non-reproduction parameters, increasing the reproductive capacity \(r\) can change the **infection-induced hydra comparison at a positive endemic equilibrium** at most once, and any change is from a smaller to a larger total population than the corresponding positive disease-free equilibrium. The transition is characterized exactly, including its absence, for the full biologically admissible parameter domain. This strengthens a published sufficient hydra condition into a sharp, global-in-\(r\) classification.

Put \(p=1-d\), \(\delta=d+p\mu\), \(c=\delta/d\), \(a=p/\delta\), and
\[
\kappa=\frac{\beta p}{\delta}(c-w),\qquad
r_c=d\exp\!\left(\frac{b\delta}{p\beta}\right).
\]
For every fixed \(0<d<1\), \(\beta,b>0\), \(0\le w,\mu\le1\), the model has a strictly positive endemic equilibrium if and only if \(r>r_c\). It is unique. Its total size is compared with the positive disease-free equilibrium \(\bar S(r)=\log(r/d)/b\) as follows.

If \(0\le w<1\) and \(b(1-w)\ge\kappa\), the endemic total is **strictly larger** than \(\bar S(r)\) for *every* \(r>r_c\), including equality in the parameter inequality. If \(0\le w<1\) and \(b(1-w)<\kappa\), there is exactly one \(r_H>r_c\) such that the endemic total is smaller than \(\bar S(r)\) on \((r_c,r_H)\), equal at \(r_H\), and larger on \((r_H,\infty)\). If \(w=1\) and \(\mu>0\), the endemic total is strictly smaller for all \(r>r_c\); if \(w=1\) and \(\mu=0\), the totals coincide identically.

The unique threshold is constructive: \(r_H=r(I_H)\), where \(I_H\) is the single positive zero of the explicit strictly convex scalar function in the proof. For the rational biological parameters \(d=1/4\), \(\mu=w=0\), and \(\beta=b=1\),
\[
I_H=\log 3,\quad S_H=\frac{\log3}{2},\quad
r_H=\frac{3\sqrt3}{4},\quad r_c=\frac{e^{1/3}}4.
\]
At this transition the endemic equilibrium is a hyperbolic local sink, so the crossing also occurs on a locally attracting endemic branch. This example lies outside the published sufficient hydra condition.

## Assumptions and scope

All populations are nonnegative real numbers; the time index \(t\) runs over nonnegative integers. The map is precisely [1, Eq. (2)]:
\[
\begin{aligned}
S_{t+1}&=r(S_t+wI_t)e^{-b(S_t+wI_t)}+pS_t e^{-\beta I_t},\\
I_{t+1}&=pS_t(1-e^{-\beta I_t})+p(1-\mu)I_t,
\end{aligned}
\]
where \(p=1-d\), \(0<d<1\), \(r,b,\beta>0\), and \(w,\mu\in[0,1]\). We vary only \(r\). The comparison is between **positive equilibrium populations**, not between arbitrary trajectories, periodic-orbit averages or attractors. The positive disease-free equilibrium exists here because \(r>r_c>d\). The hydra definition is the infection-induced equilibrium comparison in [1, Eq. (7)]; it is distinct from the classical derivative-with-respect-to-mortality hydra effect.

## Proof

**1. Explicit parameterization and uniqueness.** Let \(I>0\). The second fixed-point equation is equivalent to
\[
pS(1-e^{-\beta I})=\delta I,\qquad
S(I)=\frac{\delta I}{p(1-e^{-\beta I})},\qquad
z(I)=\frac{I}{S(I)}=a(1-e^{-\beta I}).
\]
These formulae imply \(S>0\). Substituting the infectious equilibrium equation into the susceptible equilibrium equation gives
\[
r(S+wI)e^{-b(S+wI)}=dS+\delta I.
\]
Thus every positive fixed point corresponds bijectively to some \(I>0\) satisfying
\[
r=r(I):=d\frac{1+cz(I)}{1+wz(I)}\exp\!\left(b[S(I)+wI]\right).
\]
Conversely, these formulae solve both fixed-point equations exactly. The map \(S(I)\) is strictly increasing: with \(u=\beta I>0\), its derivative has the positive sign of \(1-e^{-u}-ue^{-u}>0\). Also \(z'(I)=a\beta e^{-\beta I}>0\). Because \(c=\delta/d\ge1\ge w\), the ratio \((1+cz)/(1+wz)\) is nondecreasing in \(z\). The factor \(e^{b(S+wI)}\) is strictly increasing. Hence \(r(I)\) is continuous and strictly increasing. Its limits at zero and infinity are \(r_c=d e^{b\delta/(p\beta)}\) and infinity, respectively. This establishes the claimed exact existence and uniqueness condition, with no restriction such as \(d\ge1/2\).

**2. Exact hydra sign.** The positive disease-free equilibrium is \(\bar S(r)=b^{-1}\log(r/d)\). The reproduction parameterization gives, with \(L(I):=\log[(1+cz(I))/(1+wz(I))]\),
\[
S(I)+I-\bar S(r(I))
=(1-w)I-\frac{L(I)}b=\frac{h(I)}b,
\qquad h(I):=b(1-w)I-L(I).
\]
In particular \(h(0)=0\), with the value at zero interpreted continuously. Since \(c\ge w\), \(L(I)\ge0\). Direct differentiation yields
\[
L'(I)=\frac{(c-w)a\beta e^{-\beta I}}
{(1+cz(I))(1+wz(I))},\qquad
L'(0)=\kappa.
\]
For \(c>w\), the numerator strictly decreases and both nonnegative denominator factors increase with \(I\), so \(L'\) is strictly decreasing to zero and \(h\) is strictly convex. The nonnegative function \(L\) is bounded by \(\log[(1+ca)/(1+wa)]\).

When \(w<1\), \(c>w\). If \(h'(0)=b(1-w)-\kappa\ge0\), then \(h'(I)>0\) for every \(I>0\), whence \(h(I)>0\). If \(h'(0)<0\), strict convexity, \(h(0)=0\), and \(\lim_{I\to\infty}h(I)=+\infty\) imply exactly one positive zero \(I_H\). The sign is negative below that zero and positive above it. Strict monotonicity of \(r(I)\) translates these signs into the complete \(r\)-classification. If \(w=1\) and \(\mu>0\), then \(c>1=w\), so \(h(I)=-L(I)<0\) for all positive \(I\). If \(w=1\) and \(\mu=0\), then \(c=w=1\), so \(h\equiv0\). All boundary cases are covered.

**3. Exact locally stable crossing outside the earlier sufficient condition.** Take \(d=1/4\), \(\mu=w=0\), and \(\beta=b=1\). Then \(p=3/4\), \(\delta=d\), and
\[
z(I)=3(1-e^{-I}),\qquad
h(I)=I-\log(4-3e^{-I}).
\]
Writing \(t=e^{-I}\in(0,1)\), the sign of \(h(I)\) is the sign of
\[
(1-t)-t(4-3t)=(1-t)(1-3t).
\]
Its unique interior zero is \(t=1/3\), so \(I_H=\log3\), \(S_H=\log3/2\). The explicit formula for \(r(I)\) gives \(r_H=3\sqrt3/4\); the infected equilibrium is smaller than the disease-free equilibrium for \(0<I<\log3\) and larger for \(I>\log3\). The source's sufficient restrictions \(w<1-\beta/b\) and \(d\ge1/2\) both fail in this example.

Put \(L=\log3\). Differentiating the two-dimensional map at this crossing gives
\[
J_H=\begin{pmatrix}1-3L/8&-L/8\\1/2&3/4+L/8\end{pmatrix},\quad
\operatorname{tr}J_H=(7-L)/4,\quad
\det J_H=3/4-3L/32-3L^2/64.
\]
Its three strict Schur inequalities are
\[
\begin{aligned}
1-\det J_H&=(16+6L+3L^2)/64>0,\\
1-\operatorname{tr}J_H+\det J_H&=L(10-3L)/64>0,\\
1+\operatorname{tr}J_H+\det J_H&=(224-22L-3L^2)/64>0.
\end{aligned}
\]
Indeed \(1<L<2\) establishes all three strict inequalities. Both eigenvalues therefore lie strictly in the unit disk; the equilibrium is a hyperbolic sink. By continuity of its Jacobian and the smooth parametrization, nearby endemic fixed points on either side of \(r_H\) are also local sinks. No global stability is inferred.

## Verification

Run `python3 verify.py` in the same directory as this document; the script uses only the Python standard library. Its output begins `VERIFY_OK`. It recomputes the special-case endemic equations at \(I=\log 3\), the exact factorization and Schur expressions, and finite-precision residuals for five additional parameter combinations and five positive infectious levels each. The general \(I>0\) theorem is proved by the analytical monotonicity and strict convexity arguments above, **not** by finite numerical testing. The limiting and equality cases \(w=1\), \(\mu=0\), and \(b(1-w)=\kappa\) are treated analytically.

## Relationship to prior work

[1] gives the same Ricker–Poisson epidemic equations and defines infection-induced equilibrium hydra effects by comparing the positive fixed-point totals. Its Lemma 4 addresses endemic uniqueness, and its Theorem 5 states sufficient inequalities \(w<1-\beta/b\) and \(d\ge1/2\) but not an exhaustive partition of all reproductive rates into no-hydra / hydra regimes. The present theorem concerns the logically stronger, sharp classification as \(r\) varies; the explicit stable crossing violates both sufficient assumptions.

Jaramillo and collaborators [2] study disease-induced hydra effects in related population systems and analyze more general biological mechanisms. Earlier discrete-time statements on existence and nonexistence are not presumed absent; the precise novelty asserted here is the all-parameter, once-only threshold in this specified Ricker–Poisson epidemic map. Subsequent hydra studies [3] use different continuous-time dynamics and therefore do not imply this fixed-point sign classification.

## Limitations

The word 'hydra' refers only to an *equilibrium population comparison*; no conclusion is asserted for periodic orbits, chaotic trajectories, global attraction, selection among multiple attractors or intervention efficacy. Outside the exhibited parameter case the proof classifies equilibrium sizes without generally establishing dynamic stability of the endemic fixed point. The threshold \(r_H\) usually has an implicit but unique scalar definition, not a closed elementary formula. An older closely related article [2] was available in abstract but not in full and creates a residual originality risk. No independent audit has been undertaken.

## References

[1] L. F. Strube, S. Elgart and L. M. Childs, 'Infection-induced increases to population size during cycles in a discrete-time epidemic model', *Journal of Mathematical Biology* 88 (2024), article 60. DOI: 10.1007/s00285-024-02074-z. Published online 2024-04-10. Open full text: https://link.springer.com/article/10.1007/s00285-024-02074-z.

[2] J. M. Jaramillo, J. Ma, P. van den Driessche and A.-A. Yakubu, 'Disease-Induced Hydra Effect with Overcompensatory Recruitment', *Bulletin of Mathematical Biology* 84 (2022), article 17. DOI: 10.1007/s11538-021-00975-4. Abstract inspected; full text unavailable for this comparison.

[3] 'Hormesis and hydra effects revealed by intraspecific overcompensation models and dose–response curves' (2025). DOI: 10.1098/rsif.2025.0169. Related continuous-time model; full text inspected.
