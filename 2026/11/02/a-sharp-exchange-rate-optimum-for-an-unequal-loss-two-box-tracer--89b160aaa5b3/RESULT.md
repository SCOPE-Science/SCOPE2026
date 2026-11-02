# A sharp exchange-rate optimum for an unequal-loss two-box tracer

## Finding

**Theorem (finite-horizon transfer optimum).** In two equally sized, well-mixed compartments exchanging a passive tracer at the common bidirectional first-order rate \(k>0\), let \(\ell_1,\ell_2\geq0\) be the respective first-order tracer losses. A unit tracer pulse begins entirely in compartment 1, and the receiver concentration \(x_2(T;k)\) is measured at a prescribed \(T>0\). If \(\ell_1=\ell_2\), the receiver concentration increases strictly with \(k\) and has no finite maximizer. If \(\ell_1\ne\ell_2\), it has exactly one finite strict global maximizer \(k_*>0\), and
\[
T k_*>1.
\]
Write \(r=T^2(\ell_1-\ell_2)^2/4\). The dimensionless optimum \(y_*(r)=T k_*\) is strictly decreasing in \(r>0\) and satisfies
\[
\lim_{r\downarrow0}y_*(r)=+\infty,\qquad \lim_{r\to\infty}y_*(r)=1.
\]
Its unique scalar characterization is
\[
\frac{r}{y(y^2+r)}+\frac{y}{\sqrt{y^2+r}}\coth\!\sqrt{y^2+r}=1.
\]
For unequal losses the optimal receiver concentration is strictly larger than the infinite-exchange limit \(\tfrac12\exp[-(\ell_1+\ell_2)T/2]\). The entire receiver response, including the optimal rate, depends on the losses only through their sum and absolute difference; swapping the two losses cannot be distinguished from this receiver-only impulse response.

## Assumptions and scope

Let \(x_1(t),x_2(t)\) be tracer concentrations measured relative to a unit initial pulse, with two equal-volume perfectly mixed compartments, time-independent exchange rate \(k>0\), constant independent local first-order losses \(\ell_j\ge0\), and no additional inputs, feedback, or transport delay. Precisely,
\[
\begin{pmatrix}\dot x_1\\\dot x_2\end{pmatrix}
=\begin{pmatrix}-k-\ell_1&k\\k&-k-\ell_2\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix},\qquad
(x_1(0),x_2(0))=(1,0).
\]
The optimization criterion is the *single-time receiver concentration* \(x_2(T;k)\), not its time integral, total remaining tracer, or a population-level objective. Rate units are inverse time; for equal compartment volumes the shared physical permeability-area exchange divided by volume is \(k\). Conclusions include zero losses in either compartment, but no negative (production) losses or unequal volumes.

## Proof

Set \(m=(\ell_1+\ell_2)/2\), \(\delta=(\ell_1-\ell_2)/2\), and \(s=\sqrt{k^2+\delta^2}\). Write the evolution matrix as \(-(k+m)I+B\) with \(B^2=s^2I\). Taking its \((2,1)\) matrix-exponential entry yields the **exact impulse response**
\[
x_2(T;k)=\frac{k}{s}e^{-(k+m)T}\sinh(sT).
\]
With \(y=kT\), \(r=\delta^2T^2\), and \(z=\sqrt{y^2+r}\), maximization is equivalent to maximization of the positive function
\[
F(y,r)=\frac{y}{z}e^{-y}\sinh z,\qquad y>0,
\]
since \(x_2(T;k)=e^{-mT}F(kT,r)\).

For \(r=0\), \(F(y,0)=(1-e^{-2y})/2\), hence the assertion for equal losses. Assume \(r>0\). The logarithmic derivative equals
\[
D(y,r)=\partial_y\log F(y,r)=\frac{r}{y(y^2+r)}+\frac{y}{z}\coth z-1.
\]
At the left endpoint \(D(y,r)\to+\infty\) as \(y\downarrow0\). At infinity, \(D(y,r)=-r/(2y^2)+O(y^{-3})<0\) for sufficiently large \(y\). The intermediate value theorem gives a zero. To prove uniqueness, differentiate directly in \(y\); at **any** zero of \(D\), substitute
\[
\coth z=\frac{z}{y}\left(1-\frac{r}{yz^2}\right),\qquad
\operatorname{csch}^2z=\coth^2z-1.
\]
Exact algebra then yields
\[
\left.\partial_yD\right|_{D=0}
=-\frac{r(y^2-3y+3)}{y^2(y^2+r)}<0,
\]
because \(y^2-3y+3=(y-3/2)^2+3/4>0\). Every zero is therefore a strict downward crossing. Two different zeros would require an intervening upward or non-downward crossing, so the zero is unique and the derivative \(D\) changes from positive to negative exactly there. This proves the strict global maximum.

Next,
\[
D(1,r)=\frac{z\coth z-1}{z^2}\bigg|_{z=\sqrt{1+r}}>0,
\]
since \(z\coth z>1\) for \(z>0\). Thus \(y_*>1\). For fixed \(y>0\), differentiation in \(r\) gives
\[
\partial_rD(y,r)=\frac{y}{2z^4}\left(2-z\coth z-z^2\operatorname{csch}^2z\right)<0.
\]
To verify the sign without numerical approximations, multiply the negative of the bracket by \(\sinh^2z\). The result is
\[
H(z)=z\sinh z\cosh z+z^2-2\sinh^2z
=\sum_{n=3}^{\infty}\frac{(n-2)2^{2n-1}}{(2n)!}z^{2n}>0.
\]
At the unique zero, both \(D_y<0\) and \(D_r<0\), so implicit differentiation proves \(dy_*/dr=-D_r/D_y<0\). As \(r\downarrow0\), for every fixed \(y>0\) the logarithmic derivative approaches \(\coth y-1>0\); therefore the unique root escapes to infinity. As \(r\to\infty\), for every fixed \(y>1\) it approaches \(1/y-1<0\), while the root always exceeds 1. Consequently \(y_*\downarrow1\).

Finally, for each fixed \(r>0\), \(F(y,r)\to1/2\) as \(y\to\infty\). Since \(F\) is strictly decreasing after its finite maximum, \(F(y_*,r)>1/2\). The displayed exact solution is even in \(\delta\), establishing invariance under \(\ell_1\leftrightarrow\ell_2\). This completes the proof.

## Verification

The independent standalone script `checker.py` uses symbolic polynomial elimination for the critical-point curvature identity and the positive-coefficient hyperbolic series, together with high-precision checks across 81 contrast values and 100 independent matrix exponentials. Run `python checker.py` in an environment with `sympy` and `mpmath`. The saved script produced `PASS 1444 checks`. These finite tests corroborate, but do not replace, the proof for all positive real parameters.

For example, choose \(T=1\), \(\ell_1=0\), \(\ell_2=2\). The unique optimal exchange is
\[
k_*=2.26161115689613192\ldots,
\]
with receiver concentration \(0.206314379849812177\ldots\), versus \(0.183939720585721161\ldots\) in the perfect-mixing limit. With \(T=1\) and losses \(0,10\), the optimum is \(1.24089897162070236\ldots\), confirming the contrast-dependent decrease.

## Relationship to prior work

Two-box exchange and its exact no-loss solution are represented in the University of Washington's publicly archived `Comp2Exchange` model. Its `Comp2ExchangeReaction` model contains exchange and separate irreversible conversion rates in both boxes, with exact governing differential equations visible in the complete published model source and four-page instructional guide. The entire guide considers time courses and changes in reaction location, not a global receiver-concentration maximum over exchange rate. The two-page no-loss exchange guide was also inspected in full. The present result does **not** claim novelty of the governing linear dynamics or their matrix exponential. It addresses the different global question of optimizing *one transient receiving-box concentration* over a shared bidirectional exchange rate, including exact uniqueness, parameter monotonicity, the lower-bound exchange timescale, and the loss-symmetry obstruction.

Shanahan and Harleman (1984) examine multiple-box transport modeling in lakes and the need for calibrated exchange/dispersion parameters. Haggerty, McKenna, and Meigs (2000) study late-time groundwater tracer breakthrough behavior under rate-limited mass exchange. Neither accessible source description establishes this finite-horizon, equal-volume, unequal-loss exchange-rate optimization. This is a comparison with the material available, **not** a claim that inaccessible sections or all preceding mathematical literature have been exhaustively excluded.

## Limitations

The characterization assumes an exact two-state linear model, equal compartment volumes, bidirectional exchange proportional to concentration difference, independent constant nonnegative loss rates, and a single-time objective. The optimum may not remain unique for unequal volumes, external forcing, nonlinear sorption, heterogeneous water bodies, space-resolved advection, or a time-integrated exposure objective. No field measurements or empirical environmental-performance claims are asserted. Historical priority remains subject to inaccessible full journal texts and possible general prior matrix-semigroup optimization results. There has been no independent scientific audit.

## References

- P. Shanahan and D. R. F. Harleman, *Transport in Lake Water Quality Modeling*, Journal of Environmental Engineering **110** (1984), 42–57, published February 1, 1984. https://doi.org/10.1061/(ASCE)0733-9372(1984)110:1(42)
- R. Haggerty, S. A. McKenna, and L. C. Meigs, *On the late-time behavior of tracer test breakthrough curves*, Sandia technical report SAND99-3120J, June 12, 2000. https://digital.library.unt.edu/ark:/67531/metadc703765/
- National Simulation Resource, *Comp2Exchange*, model no. 0245, full MML source and complete two-page model guide. https://www.imagwiki.nibib.nih.gov/sites/default/files/Comp2Exchange_0.mod ; https://www.imagwiki.nibib.nih.gov/sites/default/files/Comp2Exchange_0.pdf
- National Simulation Resource, *Comp2ExchangeReaction*, model no. 0246, full MML source and complete four-page model guide. https://www.imagwiki.nibib.nih.gov/sites/default/files/Comp2ExchangeReaction_0.mod ; https://www.imagwiki.nibib.nih.gov/sites/default/files/Comp2ExchangeReaction_0.pdf
