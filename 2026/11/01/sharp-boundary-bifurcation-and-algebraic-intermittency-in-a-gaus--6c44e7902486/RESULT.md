# Sharp boundary bifurcation and algebraic intermittency in a Gaussian full-branch family

## Finding

For all \(a>0\), consider the Gaussian S-unimodal interval family
\[
 f_a(x)=e^{-(x-1/2)^2/a}-e^{-1/(4a)},\qquad
 G_{a,s}(x)=\frac{1-e^{-s f_a(x)}}{1-e^{-s f_a(1/2)}},\quad 0\le x\le1,
\]
where \(s\in\mathbb R\setminus\{0\}\); the continuous extension at \(s=0\) is \(G_{a,0}=f_a/f_a(1/2)\). These are the two exponential branches of Patidar's Gaussian family under the change of parameter \(s=\mp\log v\).

Write
\[
 h=e^{-1/(4a)},\quad d=1-h,\quad k=\frac{h}{ad},\quad \Psi(u)=\frac{u}{1-e^{-u}},\quad \Psi(0)=1.
\]
There is exactly one \(s_c(a)\in\mathbb R\) with \(G'_{a,s_c}(0)=1\). Let \(z=1/k\). Its explicit expression is
\[
 s_c(a)=\frac{z+W_b(-ze^{-z})}{d},\quad
 b=\begin{cases}0&k<1,\\-1&k>1,\end{cases}
\]
with \(s_c=0\) at the unique \(a\) satisfying \(k=1\). Here \(W_0\) and \(W_{-1}\) are real Lambert branches. For \(s<s_c(a)\), the fixed point zero is attracting and \(G_{a,s}\) has exactly **three** fixed points in \([0,1]\): zero, one repelling fixed point in \((0,1/2)\), and one in \((1/2,1)\). For \(s\ge s_c(a)\), the map has exactly **two** fixed points: zero and the right-hand fixed point. For \(s>s_c(a)\), zero is repelling.

At \(s=s_c(a)\), zero is nondegenerately parabolic from the right, with
\[
 B(a):=G''_{a,s_c}(0)=\frac1a-3+e^{-d s_c(a)}>0.
\]
For every sufficiently small fixed \(\delta>0\), define \(N_\delta(x)=\min\{n\ge0:G_{a,s_c}^n(x)\ge\delta\}\) for \(0<x<\delta\). Then, as \(x\downarrow0\),
\[
 \boxed{N_\delta(x)=\frac{2}{B(a)x}+O_{a,\delta}\!\bigl(\log(1/x)\bigr).}
\]
Thus the critical surface supports a sharp inverse-distance residence-time law. At all parameters, including where zero has an open attracting basin, the map has **topological entropy** \(\log2\). The coexistence of a sink and full topological entropy therefore holds on the entire open region \(s<s_c(a)\). At the excluded original-source parameter \(s=0\), all assertions involving \(G_{a,0}\) concern only the explicitly stated continuous extension.

## Assumptions and scope

The interval is the closed real interval \([0,1]\); \(a\) is any strictly positive real number. Both signs in the source's exponential parameterization are included by allowing positive and negative \(s\). No assumption about a physical invariant density, metric entropy, mixing, Lyapunov exponent of typical trajectories, or conjugacy with the logistic map is made. On the source's unextended domain the special slice \(s=0\) is omitted; its neutral point occurs at exactly one \(a\) and is explicitly identified as a removable extension.

## Proof

**Endpoint multiplier and exact threshold.** Put \(u=sd\). Direct differentiation at zero gives
\[
 \lambda(a,s):=G'_{a,s}(0)=k\Psi(sd).
\]
For \(u\ne0\),
\[
 \Psi'(u)=\frac{1-(1+u)e^{-u}}{(1-e^{-u})^2}>0
\]
because \(e^u>1+u\) for \(u\ne0\), and \(\Psi'(0)=1/2\). Moreover, \(\Psi(u)\to0\) as \(u\to-\infty\) and \(\Psi(u)\to\infty\) as \(u\to+\infty\), so the threshold is unique. The Lambert identity follows by solving \(1-e^{-u}=ku\), discarding its spurious zero solution except where \(k=1\). The nontrivial real branch is \(W_0\) when \(k<1\), and \(W_{-1}\) when \(k>1\). Writing \(z_0=1/(4a)\), one has \(k=4z_0/(e^{z_0}-1)\), which increases strictly with \(a\) from zero to four, proving uniqueness of the \(k=1\) slice.

**Nondegenerate critical direction.** At zero,
\[
 f'_a(0)=h/a,\quad f''_a(0)=h(a^{-2}-2a^{-1}),\quad
 G''_{a,s}(0)=G'_{a,s}(0)\bigl(f''_a(0)/f'_a(0)-s f'_a(0)\bigr).
\]
At neutrality \(s h/a=1-e^{-u}\), giving \(B(a)=a^{-1}-3+e^{-u}\). If \(a\le1/3\), positivity is immediate. If \(a>1/3\), then \(k=4z_0/(e^{z_0}-1)>3/(e^{3/4}-1)>2\). Since \(k\Psi(-\log3)=k(\log3)/2>1\) and \(\Psi\) is increasing, the neutral \(u<-\log3\). Hence \(e^{-u}>3\), again \(B(a)>0\).

**Exact fixed-point census.** Each \(G_{a,s}\) is increasing on \([0,1/2]\) from zero to one and decreasing on \([1/2,1]\) from one to zero. The right branch intersects the diagonal exactly once. To control the left, write \(y=x-1/2\). For \(x\ne1/2\), the Schwarzian chain rule and the exponential Schwarzian give
\[
 S(G_{a,s})(x)=-\frac{3}{2y^2}-\frac{2y^2}{a^2}-\frac{s^2}{2}\bigl(f'_a(x)\bigr)^2<0.
\]
The final term is zero for the continuous \(s=0\) extension. Therefore \(U(x)=1/\sqrt{G'_{a,s}(x)}\) is strictly convex on \((0,1/2)\), because \(U''=-\tfrac12 S(G_{a,s})U>0\). Hence the set where \(G'>1\) is an interval; it is nonempty since \(G(1/2)-G(0)=1\) on a length-\(1/2\) interval. Also \(G'(1/2)=0\). If \(\lambda<1\), then \(G(x)-x<0\) for small \(x>0\), while \(G(1/2)-1/2=1/2>0\); the single interval of positive derivative of \(G(x)-x\) yields exactly one interior left fixed point, crossed with slope above one. If \(\lambda>1\), \(G(x)-x>0\) near zero and cannot vanish before \(1/2\), by the same one-hump derivative structure and its positive endpoint value. At \(\lambda=1\), the positive quadratic coefficient \(B(a)/2\) gives the same strict positivity near zero. Thus the claimed counts and repelling type hold.

**Sharp residence time.** At neutrality, real analyticity at zero yields \(G(x)=x+c x^2+O(x^3)\), where \(c=B(a)/2>0\). Choose \(\delta\) small enough that \(G(x)>x\) and \(\log(G(x)/x)\ge(c/2)x\) for \(0<x\le\delta\). Until the first exit the trajectory is increasing, and its one-step reciprocal increment is \(1/G(x)-1/x=-c+O(x)\). Summation of logarithmic increments gives \(\sum_{j<N_\delta(x)}x_j=O_{a,\delta}(\log(1/x))\); the first-exit value stays between \(\delta\) and \(G(\delta)\). Telescoping reciprocals now gives \(c N_\delta(x)=1/x+O_{a,\delta}(\log(1/x))\), proving the asserted coefficient and error. This is an asymptotic in initial distance for fixed critical parameters, not a uniform claim as parameters approach the critical surface.

**Entropy.** Both monotone branches map onto the whole interval. Every inverse image of a branch interval is again a nonempty full branch, so the \(n\)-th iterate has exactly \(2^n\) monotonic laps. The lap-growth formula for piecewise monotone continuous interval maps gives \(h_{\mathrm{top}}=\lim_n n^{-1}\log 2^n=\log2\). Since \(0<\lambda<1\) on the stable side, that side has an open interval of points converging to zero, without lowering topological entropy.

## Verification

All nonstandard identities are shown algebraically above. `verify_gaussian.py` independently checks the Schwarzian and Taylor identities symbolically, locates neutral surfaces for multiple parameter values at high precision, checks the fixed-point count on both sides, and compares the sharp residence-time coefficient with long finite trajectories. It is diagnostic and not a substitute for the all-parameter proofs. The key all-parameter steps are the monotonicity of \(\Psi\), the strict Schwarzian inequality, and the positive quadratic coefficient.

## Relationship to prior work

Patidar (2024), DOI:10.3389/fphy.2024.1328895, introduces precisely this Gaussian-based exponential S-unimodal family and uses the endpoint derivative test to plot numerical stability regions. The paper does not give the closed Lambert-branch threshold, the complete fixed-point counts on both sides, the nondegenerate parabolic coefficient or its sharp inverse-distance residence-time law. Its negative-Schwarzian observation is acknowledged and independently reconstructed. The full-branch entropy identity is classical and is not claimed as a new general principle; its coexistence with a sink on this family's **exact** stable side is part of the family-specific phase description. The constant in the residence law follows from a standard parabolic normal-form argument, here with an explicit positive coefficient valid for every positive Gaussian width. Standard one-dimensional interval dynamics and Lambert W theory provide techniques, not the assembled family-specific boundary statement.

## Limitations

The result does not establish a unique physical attractor, an absolutely continuous invariant probability, or uniform chaos under all parameters. The stable region has an attracting boundary fixed point, so it is incorrect to interpret global positive topological entropy as chaos for every initial state. The boundary residence estimate is for initial points approaching zero with the map parameters fixed and does not imply a uniform two-parameter crossover. The exceptional source parameter \(s=0\) is not in the article's stated domain; assertions there concern only the continuous extension. Publication priority beyond the inspected literature is not conclusively certified; independent audit has not been performed.

## References

1. V. Patidar, "A family of robust chaotic S-unimodal maps based on the Gaussian function," *Frontiers in Physics* 12 (2024), 1328895; published March 14, 2024. DOI:10.3389/fphy.2024.1328895.
2. M. Misiurewicz and W. Szlenk, "Entropy of piecewise monotone mappings," *Studia Mathematica* 67 (1980), 45–63 (the classical lap-number entropy formula).
3. M. Andrecut and M. K. Ali, "Robust chaos in smooth unimodal maps," *Physical Review E* 64 (2001), 025203 (general S-unimodal construction; cited in [1]).
