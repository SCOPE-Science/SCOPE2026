# Two sharp coupling transitions in randomized implicit Runge–Kutta decay

## Finding
Consider two consecutive uniform-randomized implicit Runge–Kutta steps on scalar decay, with an arbitrary **joint** distribution of the two stage parameters but uniform individual marginals. For each fixed nondimensional decay rate \(r>0\), the smallest attainable expected squared two-step multiplier is exactly
\[
K_r=\int_0^1 Q_r(p)Q_r(1-p)\,dp,
\]
where the explicit quantile \(Q_r\) is specified below. Its minimizing couplings are precisely those for which the *squared one-step amplifications*, rather than necessarily the stages, have oppositely ordered quantile ranks. Ordinary stage antithetic pairing \(V=1-U\) is the unique minimizing coupling when \(0<r\le1\), but is strictly suboptimal for **every** \(r>1\). In the latter regime, the endpoint carrying the upper tail of squared amplification switches sharply at \(r=\sqrt2\). At \(r=2\), the optimal two-step expected squared multiplier is approximately \(0.00187992027519949\), versus \(0.0187482336645021\) under ordinary stage antithetic pairing, a factor of about \(9.9728876\). This is a fixed-\(r\) mean-square optimum, not a claim about nonlinear accuracy or a single coupling optimized simultaneously for all \(r\).

## Assumptions and scope
Take the autonomous scalar test equation \(y'(t)=-a y(t)\) with \(a>0\), step length \(h>0\), and \(r=ah\). For either of the two implicit randomized schemes (S1) or (S2) of Bochacik and Przybyłowicz, one step has multiplier
\[
R_r(u)=1-\frac{r}{1+ru},\quad 0\le u\le1.
\]
Within a pair, choose \((U,V)\) by any Borel probability law on \([0,1]^2\) with each marginal uniform; distinct pairs are independent. Write \(g_r(u)=R_r(u)^2\). The squared two-step multiplier is \(g_r(U)g_r(V)\). No assertion about the original authors' within-time independent stage schedule is made: its coupling is changed here. All statements concern exact arithmetic and fixed \(r\).

Define \(F_r(x)=\mathbb P\{g_r(U)\le x\}\) for a uniform \(U\), and \(Q_r(p)=\inf\{x:F_r(x)\ge p\}\). For \(0<r\le1\),
\[
Q_r(p)=\left(1-\frac r{1+rp}\right)^2,\quad 0\le p\le1.
\]
For \(r>1\) put
\[
m_r=\min\left\{r-1,\frac1{1+r}\right\},\qquad
\theta_r=\frac{2m_r}{1-m_r^2},
\]
and let \(Q_r(p)=T_r(p)^2\), where
\[
T_r(p)=\begin{cases}
\dfrac{p}{1+\sqrt{1+p^2}},&0\le p\le\theta_r,\\[3pt]
1-\dfrac1{p+1/r},&\theta_r<p\le1,\quad 1<r<\sqrt2,\\[3pt]
\dfrac1{1+1/r-p}-1,&\theta_r<p\le1,\quad r>\sqrt2.
\end{cases}
\]
At \(r=\sqrt2\), \(\theta_r=1\) and the first branch supplies the entire quantile. Thus the formula is valid for every finite \(r>0\), with branch endpoints interpreted continuously.

## Proof
**Step 1: amplification and distribution.** Substituting the scalar field into either scheme (S1) or (S2) gives \(y_+=R_r(u)y\). Thus, for arbitrary stage coupling, the required objective is \(\mathbb E[g_r(U)g_r(V)]\). Let \(q=R_r(u)\). Inverting this strictly increasing map gives \(u=1/(1-q)-1/r\), so \(q\) has density \((1-q)^{-2}\) on \([1-r,(1+r)^{-1}]\). When \(r\le1\), the multiplier is nonnegative throughout the interval and \(g_r\) is strictly increasing, giving the stated first quantile formula.

For \(r>1\), the multiplier interval straddles zero. Write \(t=\sqrt{x}\). For \(0\le t\le m_r\), both \(-t\) and \(t\) lie in its range, and direct integration gives
\[
F_r(t^2)=\int_{-t}^{t}\frac{dq}{(1-q)^2}=\frac{2t}{1-t^2}.
\]
Solving for \(t\) yields \(t=p/(1+\sqrt{1+p^2})\). Above \(m_r\), only one sign branch remains. When \(1<r<\sqrt2\), the negative branch exhausts first and \(F_r(t^2)=1/(1-t)-1/r\). When \(r>\sqrt2\), the positive branch exhausts first and \(F_r(t^2)=1+1/r-1/(1+t)\). Their inverses are exactly the other two branches of \(T_r\). Equality of the endpoint magnitudes \(r-1=(1+r)^{-1}\) occurs precisely at \(r=\sqrt2\), establishing the second sharp transition.

**Step 2: globally optimal joint law.** For nonnegative random variables \(X,Y\) with the common continuous distribution \(F_r\), the layer-cake representation gives \(\mathbb E[XY]=\int_0^\infty\int_0^\infty\mathbb P(X>s,Y>t)\,ds\,dt\). The elementary Fréchet bound on the intersection probability gives the lower bound obtained when the two scalar ranks are countermonotone. It is attained by \(X=Q_r(W)\), \(Y=Q_r(1-W)\) for a uniform \(W\), yielding \(K_r\). Every such joint law of the responses lifts to a coupling of uniform stage parameters by disintegrating the uniform law over the finite inverse fibers of \(g_r\). The response law has no atoms and is strictly increasing on its support, so equality in the layer-cake bound characterizes the countermonotone joint response law. This is the established bivariate rearrangement principle; its use here does not claim that principle as new.

**Step 3: sharp stage-coupling frontier.** If \(0<r\le1\), \(g_r\) is strictly increasing, so the equality condition translates uniquely to \(V=1-U\) almost surely. For \(r>1\), \(g_r\) decreases on \((0,1-1/r)\) and increases on \((1-1/r,1)\). On a sufficiently small interval \(0<u<\min\{1-1/r,1/r\}\), both \(g_r(u)\) and \(g_r(1-u)\) strictly decrease with \(u\). Hence ordinary stage antithetic pairing matches the larger squared amplification to the larger squared amplification on that interval. Exchanging the partner values between two disjoint equal-length subintervals strictly lowers the integral, because the resulting cost reduction is the integral of a product of two strictly positive differences. This preserves both uniform marginals. The antithetic stage coupling is therefore strictly suboptimal for every \(r>1\). Existence of the sharp rank-optimal coupling was established in Step 2.

**Step 4: exact benchmark.** At \(r=2\), \(\theta_2=3/4\) and
\[
Q_2(p)=\begin{cases}
\left(\dfrac{p}{1+\sqrt{1+p^2}}\right)^2,&0\le p\le3/4,\\[3pt]
\left(\dfrac1{3/2-p}-1\right)^2,&3/4<p\le1.
\end{cases}
\]
The exact sharp squared contraction is the displayed one-dimensional integral of these explicit functions. Numerical quadrature yields \(K_2\approx0.00187992027519949\). Direct integration of the ordinary stage antithetic product gives \(\mathbb E[g_2(U)g_2(1-U)]=5/3-(3/2)\log3\approx0.0187482336645021\). Strictness is already proved analytically, independently of these decimals. Independent copies of an optimizing pair give the exact mean-square law \(\mathbb E|y_{2k}|^2=|y_0|^2K_r^k\) for each integer \(k\ge0\).

## Verification
Run `python verify.py` from this directory. It uses only the Python standard library, independently checks the explicit quantile inversion on 9,990 input pairs, exhaustively checks five six-cell rational coupling problems using exact fractions, and compares the \(r=2\) integral with high-resolution midpoint quadrature. Expected output begins with `VERIFY_OK` and prints the two numerical factors. The symbolic distribution calculation, layer-cake inequality, and strict-exchange argument above are the actual infinite-domain proof; finite enumeration or numerical quadrature alone would not establish them.

## Relationship to prior work
Bochacik and Przybyłowicz (arXiv:2404.19059, first public version 2024-04-29) derive the uniform randomized implicit-stage method and investigate independent-step mean-square stability on the Dahlquist equation; the original process is not unconditionally mean-square stable. No theorem on optimal uniform-marginal pair couplings, their squared-response ranks, or the two transition parameters appears in the inspected full text. Puccetti and Wang (2015) discuss the general bivariate countermonotone minimum for supermodular costs. That general principle is credited, and no new rearrangement inequality is asserted: the new claim concerns its nontrivial specialization to this particular nonmonotone stability multiplier, including the explicit piecewise quantile, sharp stage-antithetic transition at \(r=1\), upper-tail switch at \(r=\sqrt2\), and exact method-specific optimum. Earlier calculations of stage-antithetic pathwise stability address a different objective (all-step pathwise stability) and do not establish the fixed-step global mean-square optimum here. The extension from scalar multiplier optimization to arbitrary nonlinear ODEs is not claimed.

## Limitations
The minimized quantity is expected squared numerical amplitude after two steps for one fixed real negative Dahlquist mode, not error against the exact trajectory. Optimal couplings can depend on the chosen \(r\), and they need not be pathwise contractive at all step sizes. The original method's independent temporal randomization and its accuracy theorem do not automatically extend to coupled samples. General bivariate rearrangement optimality is previously known. Published mathematical databases and literature can be incomplete; novelty relative to unobserved source-specific coupling analyses remains a risk. The verification is analytical plus finite corroboration, without independent scientific validation.

## References
- T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059, first version 2024-04-29, Section 1.2 and Section 3, https://arxiv.org/abs/2404.19059.
- G. Puccetti and R. Wang, *Extremal dependence concepts*, *Statistical Science* 30 (2015), 485–517, doi:10.1214/15-STS525, Sections 1 and 3, https://arxiv.org/abs/1512.03232.
- W. J. Barclay, D. F. Griffiths, and D. J. Higham, *Theta method dynamics*, *LMS Journal of Computation and Mathematics* 3 (2000), 27–43; background on deterministic theta amplifications.
