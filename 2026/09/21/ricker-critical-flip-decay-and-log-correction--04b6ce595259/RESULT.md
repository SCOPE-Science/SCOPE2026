# Critical algebraic decay and logarithmic correction at the Ricker flip threshold

## Result

Consider the normalized one-species Ricker map
\[
x_{n+1}=f_r(x_n):=x_n e^{r(1-x_n)},\qquad x_0>0.
\]
At the first period-doubling threshold \(r=2\), the positive equilibrium \(x=1\) has multiplier \(-1\). The following gives its global critical relaxation law.

**Theorem.** Let \(f=f_2\), and define the exceptional set
\[
\mathcal E:=\bigcup_{k\ge 0}f^{-k}(\{1\}).
\]
Then every positive orbit converges to \(1\). If \(x_0\in\mathcal E\), the orbit reaches \(1\) in finitely many iterates and is constant thereafter. If \(x_0\notin\mathcal E\), then there is a finite constant \(C(x_0)\) such that
\[
\boxed{
\frac{1}{(x_n-1)^2}
=\frac43 n+\frac85\log n+C(x_0)+o(1)
}
\qquad(n\to\infty).
\]
Consequently,
\[
\boxed{\sqrt n\,|x_n-1|\longrightarrow \frac{\sqrt3}{2}},
\]
and more precisely
\[
|x_n-1|
=\frac{\sqrt3}{2\sqrt n}
\left(1-\frac35\frac{\log n}{n}+O\!\left(\frac1n\right)\right).
\]
For every nonexceptional orbit, the sign of \(x_n-1\) alternates at all sufficiently large \(n\).

In the unnormalized form
\[
N_{n+1}=N_n\exp\!\left(2\left(1-\frac{N_n}{K}\right)\right),
\]
the leading law is
\[
\sqrt n\,|N_n-K|\longrightarrow \frac{\sqrt3}{2}K.
\]

The exceptional set is countable: at each finite backward depth there are only finitely many preimages because the Ricker map is unimodal. Thus the algebraic law holds for every positive initial condition except the countable set of histories that land exactly on the equilibrium in finite time.

## Proof

### 1. Global convergence at the threshold

For \(r=2\),
\[
f(x)=xe^{2(1-x)}.
\]
The map is positive on \((0,\infty)\) and has global maximum \(e/2\), attained at \(x=1/2\). Hence after one iterate every orbit lies in \((0,e/2]\).

For a fixed orbit, set
\[
\alpha=\min\{x_1,f(e/2),1/2\}>0.
\]
Since \(f\) is increasing on \((0,1/2)\), decreasing on \((1/2,\infty)\), and \(f(x)>x\) for \(0<x<1\), the compact interval \([\alpha,e/2]\) is forward invariant.

For \(x>0\), the equation \(f^2(x)=x\) is equivalent, after taking logarithms, to
\[
x+f(x)=2.
\]
Let
\[
q(x)=x+f(x)-2.
\]
Then \(q(1)=0\), \(q'(1)=0\), and
\[
q''(x)=4e^{2(1-x)}(x-1).
\]
Thus \(q'\) decreases to \(0\) on \((0,1)\) and increases from \(0\) on \((1,\infty)\), so \(q'(x)>0\) for \(x\ne1\). Therefore \(q\) has the unique zero \(x=1\): there is no nontrivial two-cycle at the threshold. Coppel's iteration theorem then implies convergence of every orbit in the invariant interval to a fixed point. The only positive fixed point is \(1\), hence \(x_n\to1\).

This endpoint global convergence is known in the Ricker literature; it is included here to connect the local critical expansion to every positive initial condition.

### 2. The second iterate removes the sign flip

Put \(u_n=x_n-1\). At \(r=2\), one step is
\[
F(u):=(1+u)e^{-2u}-1
=-u+\frac23u^3-\frac23u^4+\frac25u^5+O(u^6).
\]
The second iterate \(G=F\circ F\) satisfies
\[
G(u)=u-\frac43u^3+\frac{8}{15}u^5+\frac49u^6+O(u^7).
\]
Because every orbit tends to zero in the \(u\)-coordinate, and a nonexceptional orbit never has \(u_n=0\), the even and odd subsequences eventually lie in a punctured neighborhood where \(G\) preserves sign and decreases absolute value.

### 3. Reciprocal-square dynamics

For \(u\to0\), direct expansion gives
\[
\frac1{G(u)^2}-\frac1{u^2}
=\frac83+\frac{64}{15}u^2-\frac89u^3+O(u^4).
\]
Fix either parity and write \(v_m=u_{2m+j}\), \(j\in\{0,1\}\), and
\[
W_m=\frac1{v_m^2}.
\]
Then \(W_m\to\infty\) and
\[
W_{m+1}-W_m
=\frac83+\frac{64}{15}\frac1{W_m}+O(W_m^{-3/2}).
\]
First, \(W_m/m\to8/3\). It follows that \(W_m=(8/3)m+O(\log m)\). Hence
\[
\frac1{W_m}-\frac{3}{8m}=O\!\left(\frac{\log m}{m^2}\right),
\]
and both this error and \(W_m^{-3/2}\) are summable. Therefore
\[
W_m-\frac83m-\frac85\log m
\]
converges to a finite parity-dependent constant.

Finally, the one-step expansion
\[
\frac1{F(u)^2}-\frac1{u^2}=\frac43-\frac43u+O(u^2)
\]
shows that the constants from the two parities match after converting \(m\) to the original index \(n\). Thus a single \(C(x_0)\) satisfies
\[
\frac1{u_n^2}=\frac43n+\frac85\log n+C(x_0)+o(1).
\]
Taking reciprocal square roots gives the stated leading constant and logarithmic correction. Since \(F(u)/u\to-1\), the sign flips on every sufficiently late iterate.

## Context and prior literature

Ricker introduced the stock-recruitment relation in 1954. May's 1975 analysis of the scalar Ricker difference equation identified the globally stable fixed-point regime \(0<r<2\), the period-two branch for \(r>2\), and the ensuing period-doubling cascade. The endpoint \(r=2\) is nonhyperbolic and is excluded from May's displayed strict Lyapunov inequality.

Later difference-equation literature explicitly records global convergence of the positive equilibrium for \(0<r\le2\), using Coppel's theorem, and standard nonhyperbolic-map criteria establish local asymptotic stability when the multiplier is \(-1\) and the relevant Schwarzian sign is negative. Recent planar Ricker papers continue to use \(r=2\) as the one-dimensional period-doubling threshold.

The contribution here is not the location of the flip threshold, global attraction for \(r\le2\), or generic parabolic-iteration theory. It is the explicit Ricker-specific critical asymptotic valid throughout the positive basin: the universal coefficient \(\sqrt3/2\), the next-order \((8/5)\log n\) correction in reciprocal square, and the exact separation of the countable finite-hit exceptional set.

## Scientific limitations

The theorem concerns the deterministic one-dimensional Ricker map exactly at \(r=2\). It does not provide a uniform near-critical crossover theorem as \(r\to2\), nor does it address delay, harvesting, noise, spatial coupling, or higher-dimensional Ricker competition models. The algebraic rate follows from a local neutral second iterate once global convergence is known, so no novelty is claimed for the general method of parabolic iteration. Originality is asserted only to the best of our knowledge. Older model-specific stability sources by Goh (1977), Fisher--Goh--Vincent (1979), and Greenwell--Ng (1984) were identifiable bibliographically but were not all available for complete theorem-level inspection; they remain the most plausible residual priority risk.

## Reproducibility

`artifacts/verify_critical_expansion.py` symbolically verifies the one-step and two-step Taylor expansions, reciprocal-square increments, and the coefficient \(8/5\) of the logarithmic term. `artifacts/VERIFIED_OUTPUT.txt` records the resulting exact expressions.

## References

1. W. E. Ricker, “Stock and Recruitment,” *Journal of the Fisheries Research Board of Canada* 11 (1954), 559–623. https://doi.org/10.1139/f54-039
2. R. M. May, “Biological Populations Obeying Difference Equations: Stable Points, Stable Cycles, and Chaos,” *Journal of Theoretical Biology* 51 (1975), 511–524. https://doi.org/10.1016/0022-5193(75)90078-8
3. W. A. Coppel, “The Solution of Equations by Iteration,” *Mathematical Proceedings of the Cambridge Philosophical Society* 51 (1955), 41–43. https://doi.org/10.1017/S030500410002990X
4. R. Luís and E. Rodrigues, “Local Stability in 3D Discrete Dynamical Systems: Application to a Ricker Competition Model,” *Discrete Dynamics in Nature and Society* (2017), Article 6186354. https://doi.org/10.1155/2017/6186354
5. S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira, and R. Luís, “A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds,” *Journal of Difference Equations and Applications* 29 (2023), 575–591. https://doi.org/10.1080/10236198.2023.2222855
6. H. Naderi Yeganeh and S. Baigent, “New global stability results for the planar Ricker model,” *Journal of Difference Equations and Applications* (2026). https://doi.org/10.1080/10236198.2026.2636481
7. B. S. Goh, “Stability in a Stock-Recruitment Model of an Exploited Fishery,” *Mathematical Biosciences* 33 (1977), 359–372. https://doi.org/10.1016/0025-5564(77)90149-3
8. M. E. Fisher, B. S. Goh, and T. L. Vincent, “Some stability conditions for discrete-time single species models,” *Bulletin of Mathematical Biology* 41 (1979), 861–875. https://doi.org/10.1007/BF02462383
