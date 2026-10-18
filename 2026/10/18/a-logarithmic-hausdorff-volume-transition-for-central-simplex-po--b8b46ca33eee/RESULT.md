# A logarithmic Hausdorff–volume transition for central simplex polytopes

## Finding
Let \(m\ge2\) be the number of vertices and let \(\Delta_{m-1}=\{x\in\mathbb R^m:x_i\ge0,\sum_{i=1}^m x_i=1\}\), equipped with the Euclidean metric induced by \(\mathbb R^m\). For every real \(c>1\), truncate all vertex directions symmetrically by the coordinate-ratio rule
\[
K_m(c)=\bigl\{x\in\Delta_{m-1}:x_i\le c x_j\text{ for all }i,j\bigr\}.
\]
Write \(V_m(c)\) for the ratio of intrinsic \((m-1)\)-volumes and \(d_m(c)=d_H(K_m(c),\Delta_{m-1})\) for Euclidean Hausdorff distance. Setting \(a=m/(c-1)\), one has the **exact joint identities**
\[
V_m(c)=\frac{\Gamma(m)\Gamma(1+a)}{\Gamma(m+a)},\qquad
 d_m(c)=\frac{\sqrt{m(m-1)}}{m+c-1}
 =\sqrt{\frac{m-1}{m}}\frac{a}{1+a}.
\tag{1}
\]
The general-ratio volume identity is included as a known-source-compatible input, **not separately claimed as a novel formula**. The geometric/dimensional conclusions below are the finding.

**Sharp logarithmic transition.** For every sequence of real parameters \(c_m>1\), \(m\to\infty\), and every extended real \(s\in[0,\infty]\),
\[
 (\log m)\,d_m(c_m)\longrightarrow s
 \quad\Longrightarrow\quad
 V_m(c_m)\longrightarrow e^{-s},
 \qquad e^{-\infty}:=0.
\tag{2}
\]
In particular, at prescribed \(p\in(0,1)\), the unique volume-preserving truncation fraction \(p\) has distance asymptotic to \((-\log p)/\log m\). Thus a sequence of *strictly smaller* inscribed polytopes can become Hausdorff-close to the simplex while continuing to omit a fixed positive fraction of its volume.

**Refined quantile and Euler correction.** Let \(q=-\log p\), \(L_m=\log m+\gamma\), and define the unique \(c_{m,p}\) by \(V_m(c_{m,p})=p\). Then
\[
 d_m(c_{m,p})=\sqrt{\frac{m-1}{m}}
 \left[\frac{q}{L_m}-\frac{q^2}{L_m^2}
 +\frac{q^3+\frac{\pi^2}{12}q^2}{L_m^3}
 +O_p(L_m^{-4})\right].
\tag{3}
\]
For every fixed \(t>0\), the scaling \(c_m=t mL_m\) obeys
\[
 V_m(t m L_m)=e^{-1/t}
 \left[1+\frac{\pi^2}{12t^2L_m^2}+O_t(L_m^{-3})\right].
\tag{4}
\]
The formula is understood for sufficiently large \(m\), when \(t mL_m>1\).

## Assumptions and scope
All volumes are intrinsic \((m-1)\)-dimensional Euclidean volume **ratios**, so their arbitrary common scale cancels. The simplex has side length \(\sqrt2\); consequently the Hausdorff constants depend on this fixed normalization. The parameter \(c\) is real and strictly larger than one. Statements (2)–(4) concern \(m\to\infty\), allowing \(c\) to vary with dimension; the constants hidden in \(O_p\) and \(O_t\) depend only on the displayed fixed parameter. The superscript \(\infty\) in (2) denotes an extended-real limit, not a fixed finite number.

## Proof
**1. Exact volume identity.** Let \(Y_1,\ldots,Y_m\) be independent unit-rate exponential random variables. Their normalization \(X_i=Y_i/\sum_jY_j\) is uniform on the simplex. The event \(X\in K_m(c)\) is exactly \(\max_iY_i\le c\min_iY_i\). Choosing the almost surely unique minimum, integrating it at \(y>0\), and using the independent exponential residual lifetimes gives
\[
V_m(c)=m\int_0^\infty e^{-m y}\bigl(1-e^{-(c-1)y}\bigr)^{m-1}\,dy.
\]
The substitution \(z=e^{-(c-1)y}\) gives \(V_m(c)=aB(a,m)=\Gamma(m)\Gamma(1+a)/\Gamma(m+a)\). For \(c=2\), this is \(\binom{2m-1}{m-1}^{-1}\), matching the established edge-trisection result. More generally the beta-integral is equivalent to the finite inclusion–exclusion sum for arbitrary edge-division ratios already recorded in the motivating literature.

**2. Exact Hausdorff identity.** Since \(K_m(c)\) is convex and contained in \(\Delta_{m-1}\), the function \(x\mapsto \operatorname{dist}(x,K_m(c))\) is convex on \(\Delta_{m-1}\). Its maximum over that simplex therefore occurs at a vertex \(e_i\). Permutation symmetry makes all vertices equivalent. Every \(x\in K_m(c)\) satisfies
\[
x_i\le\frac{c}{m+c-1},
\]
because each of the other \(m-1\) coordinates is at least \(x_i/c\). Given \(x_i=u\), Cauchy–Schwarz gives
\[
\|e_i-x\|_2^2=(1-u)^2+\sum_{j\ne i}x_j^2
\ge\frac{m}{m-1}(1-u)^2.
\]
This decreases with \(u\le1\), and equality holds at the feasible point having \(x_i=c/(m+c-1)\) and every other coordinate \(1/(m+c-1)\). Hence \(d_m(c)=\sqrt{m(m-1)}/(m+c-1)\). Substitution of \(a=m/(c-1)\) gives (1).

**3. Small-parameter expansion.** Put \(L_m=\log m+\gamma\). Taylor expansion of \(\log\Gamma(1+a)\) at zero, and the elementary estimate \(\log\Gamma(m+a)-\log\Gamma(m)=a\log m+O(a/m+a^2/m)\) uniformly for \(0\le a\le1/2\), yield
\[
\log V_m(c)=-L_m a+\frac{\pi^2}{12}a^2
 +O(a^3+a/m).
\tag{5}
\]
All error terms here are uniform for the stated range; derivatives of \(\log\Gamma\) are bounded on the compact interval and \(\psi(m)=\log m+O(1/m)\), \(\psi'(m)=O(1/m)\).

**4. Every logarithmic regime.** Write \(s_m=\sqrt{(m-1)/m}\), so \(a=d/(s_m-d)\). If \((\log m)d\to s<\infty\), then \(d\to0\), \(a\to0\), and \(L_m a\to s\). Equation (5) implies \(\log V_m(c_m)\to-s\). For the infinite case, fix \(T>0\) and compare with \(a_T=T/L_m\), whose Hausdorff distance \(s_m a_T/(1+a_T)\) is asymptotic to \(T/\log m\) and whose volume tends to \(e^{-T}\). Eventually the actual distance is at least this one. Volume is decreasing in \(a\) (equivalently increasing in \(c\)); therefore the actual volume is at most the comparison volume. Sending \(T\to\infty\) gives limit zero.

**5. Fixed-volume calibration.** From (1), \(V_m(c)\) increases strictly from zero to one as \(c\) runs from \(1+\) to infinity: for the ratio event strict increase follows because exponential samples have a continuous positive density, and endpoint limits follow by dominated convergence. Thus \(c_{m,p}\) exists uniquely. Write \(a_{m,p}=m/(c_{m,p}-1)\). Equation (2) (or monotone comparison with \(a=T/L_m\)) first yields \(a_{m,p}=O_p(1/L_m)\). Solving the logarithm of the exact volume through (5), with \(q=-\log p\), gives
\[
a_{m,p}=\frac q{L_m}+\frac{\pi^2q^2}{12L_m^3}+O_p(L_m^{-4}).
\]
Expanding \(d=s_m a/(1+a)\) then proves (3). Finally, when \(c=t mL_m\), \(a=m/(t mL_m-1)=1/(tL_m)+O_t(1/(mL_m^2))\). In (5) this gives
\[
\log V_m(t mL_m)=-\frac1t+\frac{\pi^2}{12t^2L_m^2}+O_t(L_m^{-3}),
\]
and exponentiation proves (4).

## Verification
The self-contained `CHECKER.py` uses exact rational arithmetic for integer coordinate-ratio constraints and verifies the trisection normalization for dimensions \(m=2,\ldots,18\). It separately compares the beta/gamma identity with finite inclusion–exclusion, checks explicit nearest-vertex witnesses, solves several fixed-volume quantiles numerically, and probes both asymptotic refinements. Execution from the embedded artifact reported 167 passing checks. These finite computations check formulas and normalization only: the uniform infinite-dimensional transition, uniqueness and error orders are proved in the analytic steps above.

## Relationship to prior work
Kazakov's June 2026 generalization of Marion's theorem establishes the trisection simplex volume, gives the exponential-order-statistics method and presents parameterized finite inclusion–exclusion expressions for other edge divisions. Therefore the exact general-ratio volume expression here is a reformulation rather than a priority claim. The additional Euclidean Hausdorff parameterization, its all-regime high-dimensional volume transition and the Euler-corrected inverse quantile law address the **simultaneous geometric approximation and volume-loss** question, which is not answered by the inspected statements of that work. The accessible July 2026 exposition by Aldridge explains the fixed trisection phenomenon and its probabilistic proof, not the dimension-varying Hausdorff profile.

## Limitations
The theorem is specialized to fully symmetric pairwise-coordinate-ratio truncations of the regular simplex; it does not give a universal Hausdorff–volume inequality for arbitrary convex bodies or other nonuniform truncations. Its new content relies on standard gamma expansions and extreme order statistics, and a historically equivalent high-dimensional formulation using different vocabulary could exist. The source's general-ratio volume expression must not be attributed as new. Neither the numerical checker nor this written review constitutes independent mathematical certification.

## References
1. Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087, first publicly posted June 1, 2026, https://arxiv.org/abs/2606.02087.
2. Matthew Aldridge, *A (more) probabilistic proof of a geometric result*, July 1, 2026, https://mpaldridge.github.io/blog/marions-theorem.html.
3. Classical Dirichlet–exponential normalization and beta/gamma identities are used as standard mathematical tools, rather than claimed contributions.
