# Exact cover-time variance and a mean–risk conflict in Brownian resetting

## Finding

A reflected Brownian searcher on a finite interval, reset at Poisson times to its initial site, retains the set of sites it has already visited. For every reset site we derive its exact cover-time second moment by combining three distinct killed-boundary renewal problems. The exact formulas establish an observable design conflict: when the dimensionless reset rate is \(rL^2/D=1\), resetting at either boundary is the **unique mean-cover-time minimizing choice**, whereas resetting at the midpoint has **strictly smaller cover-time variance** than either mean minimizer. This is a strict, reproducible mean–variance reversal, not an assertion that the midpoint globally minimizes variance.

Let \(x\in[0,L]\), \(L,D,r>0\), \(k=\sqrt{r/D}\), and
\[
F_+(s)=\frac{\cosh(\sqrt{s/D}\,x)}{\cosh(\sqrt{s/D}\,L)},\quad
F_-(s)=\frac{\cosh(\sqrt{s/D}\,(L-x))}{\cosh(\sqrt{s/D}\,L)},\quad
F_{\pm}(s)=\frac{\cosh(\sqrt{s/D}\,(x-L/2))}{\cosh(\sqrt{s/D}\,L/2)}.
\]
Write \(\epsilon_+=\epsilon_-=1\) and \(\epsilon_{\pm}=-1\). Define \(T_r(x)\) to be the first time *both* endpoints have been visited, including the initial point at time zero. Then
\[
\mathbb E T_r(x)=\frac1r\sum_{j\in\{+,-,\pm\}}\epsilon_j\left(F_j(r)^{-1}-1\right),
\]
\[
\boxed{\mathbb E[T_r(x)^2]=\frac{2}{r^2}\sum_{j\in\{+,-,\pm\}}\epsilon_j\frac{1-F_j(r)+rF_j'(r)}{F_j(r)^2}.}
\]
These statements hold for every \(x\in[0,L]\) and every positive \(L,D,r\); a prime means differentiation in the argument \(s\), not in the spatial coordinate. The variance is the second moment minus the squared first moment.

At \(r=D/L^2\), set \(\kappa=1\). At either edge \(x\in\{0,L\}\), and at \(x=L/2\), respectively,
\[
\frac D{L^2}\mathbb ET_r(0)=\cosh1-1\approx0.543080635,
\quad\frac D{L^2}\mathbb ET_r(L/2)=3\cosh(1/2)-2/\cosh(1/2)-1\approx0.609240128,
\]
\[
\frac{D^2}{L^4}\operatorname{Var}(T_r(0))=\sinh1\,(\sinh1-1)\approx0.205896652,
\]
\[
\boxed{\frac{D^2}{L^4}\operatorname{Var}(T_r(L/2))=
\frac{10\sinh^2 1-11\sinh(1/2)-3\sinh(3/2)}{4(\cosh1+1)}\approx0.166244407.}
\]
Thus the edge minimizes the mean globally, although its variance exceeds that at the center by about \(0.039652245L^4/D^2\). Continuity also gives a nonempty open interval of dimensionless rates containing one for which these strict location comparisons persist.

## Assumptions and scope

The searcher is one-dimensional reflected Brownian motion on \([0,L]\), with generator \(D\partial_{xx}\) and Neumann boundaries, started at \(x\). Independent exponential Poisson events of constant rate \(r\) instantaneously return the position to the same fixed \(x\). A reset **does not erase previously visited points**. Since paths are continuous between resets, covering the entire interval is equivalent to visiting both endpoints at least once, allowing visits on different reset cycles. Endpoints are counted as visited at time zero if the initial point is an endpoint. The Brownian and reset clocks are independent. No other targets, spatially distributed reset law, or reset-induced delay is considered.

## Proof

**1. Three first-passage transforms.** Let \(\tau_+\) be the first free-diffusion hit of \(L\), with reflection at zero, \(\tau_-\) the first hit of zero with reflection at \(L\), and \(\tau_{\pm}\) the first hit of either endpoint with absorbing endpoints. The solutions of \(Df''=sf\) with the respective Dirichlet/Neumann boundary conditions are exactly the three functions \(F_j(s)=\mathbb E_x[e^{-s\tau_j}]\) displayed above. For \(s>0\) each is positive and differentiable; all formulas extend to boundary initial sites by continuity.

**2. Renewal and inclusion–exclusion.** For a single target event with free hitting transform \(F(s)\), repeated independent Poisson resets to the same \(x\) give the reset-survival Laplace transform
\[
\widetilde S_r(s)=\frac{1-F(s+r)}{s+rF(s+r)},\qquad s\ge0.
\]
This follows by renewal at the first reset and uses no assumption of finite free mean hitting time. For every sample path, regardless of how many resets occur, the event that both endpoints are *not yet* visited is the union of the events that the left endpoint has not been visited and that the right endpoint has not been visited. Therefore the cover survival function satisfies
\[
\Pr(T_r(x)>t)=S_{+,r}(t)+S_{-,r}(t)-S_{\pm,r}(t).
\]
The two single-target survival functions retain reflection at the non-target endpoint. Their intersection is exactly the event that neither endpoint has been visited, justifying the absorbing–absorbing term. This identity respects persistent visit history, unlike restarting an already completed portion of the cover task.

**3. Moments and normalization.** Differentiating the displayed survival transform at \(s=0\) gives
\[
\widetilde S_r(0)=\frac{1-F(r)}{rF(r)},\qquad
-\widetilde S_r'(0)=\frac{1-F(r)+rF'(r)}{r^2F(r)^2}.
\]
Each hit occurs with positive probability in a reset-free interval of fixed length, so the number of cycles until success has a geometric upper bound and all cover moments in this compact-domain model are finite. Consequently \(\mathbb ET=\int_0^\infty\Pr(T>t)dt\) and \(\mathbb ET^2=2\int_0^\infty t\Pr(T>t)dt\) may be applied to the inclusion–exclusion expression. This proves the exact first- and second-moment formulas.

**4. Global mean-optimal sites at the specified rate.** By scaling, set \(D=L=r=1\). Write \(b=\cosh(1/2)>1\) and \(z=\cosh(x-1/2)\in[1,b]\). Hyperbolic addition and the three first-passage transforms simplify the mean to
\[
\mathbb E T_1(x)+1=\frac{b}{z}\frac{(4b^2-3)z^2-(b^2-1)}{b^2+z^2-1}.
\]
For fixed \(B=b^2>1\), the derivative of the rational factor on the right (with the positive constant \(b\) removed) has the sign of
\[
P_B(Z)=(3-4B)Z^2+4B(B-1)Z+(B-1)^2,\qquad Z=z^2.
\]
Its quadratic leading coefficient is negative, its constant is positive, and therefore it has exactly one positive root. Moreover \(P_B(1)=5B^2-10B+4<0\) because \(1<B=(1+\cosh1)/2<7/5\), as certified by the rational Taylor enclosure, and \(P_B(1)=5(B-1)^2-1<0\). Hence \(P_B(Z)<0\) for every \(Z\ge1\). The mean is strictly decreasing in \(z\), and \(z\) takes its maximum \(b\) exactly at \(x=0,L\). These two sites, and no other sites, globally minimize the mean.

**5. Independent variance comparison.** Substitution of the respective hyperbolic transforms and their \(s\)-derivatives into Step 3, followed by \(\cosh(2a)=2\cosh^2(a)-1\), gives the two closed variance formulas under Finding. Their strict comparison can be certified using rational interval arithmetic. For \(t\in\{1/2,1,3/2\}\), bound \(e^t\) from below by its degree-20 Taylor partial sum and above by that sum plus the first omitted term divided by \(1-t/22\). Evaluate \(\cosh t=(e^t+e^{-t})/2\) and \(\sinh t=(e^t-e^{-t})/2\) using interval arithmetic, including reciprocal bounds. The included standalone verifier computes rational enclosures for the mean and variance differences and confirms positive lower endpoints: the certified dimensionless mean difference is within \((0.06615949286,0.06615949287)\) and the certified variance difference is within \((0.03965224476,0.03965224477)\). Because these are strict, the inequalities persist on an open neighborhood of the chosen dimensionless rate by analyticity.

## Verification

Run `python3 verify.py` with a standard Python 3 installation. The script prints certified rational Taylor intervals and conducts independent discrete reflected-walk checks using tridiagonal killed-generator equations. Its CTMC mesh uses nearest-neighbor rates \(D/h^2\) in the interior and \(2D/h^2\) at reflecting endpoints. The script checks reflection symmetry, mean-transform equivalence, positive moments, representative spatial mean ordering, and convergence of the independently computed first and second moments to the continuous formula. Its finite checks support the exact proof but do not substitute for the global derivative argument or the rational interval certificate.

## Relationship to prior work

Ghosh and Sabhapandit (arXiv:2605.31207v1, first public 2026-05-29) study this confined Brownian cover problem at the midpoint and obtain its mean and distribution under Poisson resetting. In particular their midpoint mean is exactly the specialization of the first-moment expression above; it is not new here. Linn and Lawley (arXiv:2406.12154, first public 2024-06-17; later Chaos 2025) previously derive an exact mean cover time for arbitrary asymmetric intervals and provide general high-reset moment asymptotics. Their asymmetric exact mean formula also subsumes our *general first-moment expression*, and is acknowledged as such. Pal and Prasad (arXiv:1812.03009) give earlier interval first-passage/resetting formulas underlying these methods.

The claim evaluated here is limited to the arbitrary-location **exact finite-rate second moment and variance** and the certified **opposition between globally mean-optimal endpoint resets and lower midpoint variance at the specified rate**. Neither of the first two inspected primary manuscripts states that exact joint moment comparison. Renewal-transform differentiation and the known arbitrary-location mean formula remain relevant routes by which some components might have been implicit in earlier literature; the result is not claimed to be independent of standard renewal machinery.

## Limitations

The midpoint is proved to have lower variance than the mean-optimal endpoints at the specified rate, **not** to minimize variance over all reset positions. The optimal spatial design for variance at every rate and the Pareto frontier are not classified. Results are exact only for one-dimensional standard reflected Brownian motion, single Poisson rate, fixed-site full position reset, and persistent cover history. No finite-sample observational uncertainty or experiment is analyzed. Novelty is assessed relative to inspected sources and available research records, not certified across all literature. No external independent audit has been performed.

## References

1. A. Ghosh and S. Sabhapandit, *Cover time statistics of one-dimensional Brownian motion under stochastic resetting*, arXiv:2605.31207v1, posted 2026-05-29, https://arxiv.org/abs/2605.31207.
2. S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154, posted 2024-06-17; Chaos 35, 043124 (2025), https://arxiv.org/abs/2406.12154.
3. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018), https://arxiv.org/abs/1812.03009.
