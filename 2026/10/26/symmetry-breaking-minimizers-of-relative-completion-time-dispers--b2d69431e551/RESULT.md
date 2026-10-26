# Symmetry-breaking minimizers of relative completion-time dispersion in a two-type clumsy collector

## Finding
Consider a coupon collector with two types, drawn independently with probabilities \(a\) and \(1-a\). Each draw refreshes the chosen type to present with probability \(q=1-p\), and to absent with probability \(p\), independently of previous refresh outcomes. Other types retain their status. Begin with both types absent, and denote the first time both are present by \(T\). For every \(0<a<1\) and \(0\le p<1\), define the squared coefficient of variation \(R=\operatorname{Var}(T)/(\mathbb ET)^2\). The exact minimizers over \(a\) undergo the following transition at
\[
p_\star=\frac{19-\sqrt{97}}{12}=0.7625951831\ldots.
\]
For \(0\le p\le p_\star\), the unique optimizer is \(a=1/2\). For \(p_\star<p<1\), there are precisely two minimizing, nonuniform probabilities
\[
a_\pm=\frac{1\pm\sqrt{1-4w_\star}}2,\qquad
w_\star=\frac{1-p^2}{19p-10p^2-7}\in(0,1/4).
\]
Thus sufficiently strong loss makes deliberate type imbalance *reduce relative uncertainty*, even though balancing always minimizes absolute waiting-time variance and mean. In fact, with \(w=a(1-a)\),
\[
\mathbb ET=\frac{(1-p)+(2p-1)w}{w(1-p)^2}
\]
and
\[
\operatorname{Var}(T)=\frac{(2p-1)(3p^2-4p+2)w^2-(p-1)(p^2+4p-3)w+(1-p)^2}{w^2(1-p)^4}.
\]

## Assumptions and scope
Discrete times are nonnegative; a step samples one of the two types independently, and refreshes that type to present with probability \(1-p\) and absent otherwise. Counts of previously held coupons beyond the indicator of presence are irrelevant because a clumsy refresh empties the entire selected type. Completion is checked after the refresh. The initial state is both absent. The theorem covers \(0<a<1\), \(0\le p<1\), and minimizes over the open probability simplex; both stated minima are attained in its interior. The degenerate limits \(a=0,1\) or \(p=1\) are excluded because completion is impossible.

## Proof
Write \(b=1-a\), \(q=1-p\), and consider transient states \(00\), \(10\), \(01\), with \(11\) absorbing for the first-passage calculation. Their substochastic transition matrix is
\[
Q=\begin{pmatrix}
p&aq&bq\\
ap&1-ap-bq&0\\
bp&0&1-bp-aq
\end{pmatrix}.
\]
Every transient state reaches \(11\) with positive probability in at most two steps. Therefore \(I-Q\) is invertible, all first-passage moments are finite, and the vectors \(m\) of means and \(u\) of second moments satisfy
\[
(I-Q)m={\bf1},\qquad (I-Q)u=2m-{\bf1}.
\]
Solving these three linear equations and simplifying by \(w=ab\) gives the displayed expressions for \(\mathbb ET=m_{00}\) and \(\operatorname{Var}(T)=u_{00}-m_{00}^2\).

Set \(R(w)=\operatorname{Var}(T)/(\mathbb ET)^2\) for \(0<w\le1/4\). Direct differentiation and cancellation give the key identity
\[
R'(w)=-\frac{(1-p)^2\left[(1-p^2)+(10p^2-19p+7)w\right]}{\left[(1-p)+(2p-1)w\right]^3}.
\]
The denominator is positive because it equals \([w(1-p)^2\mathbb ET]^3\). The numerator's affine bracket is positive at \(w=0\), since \(1-p^2>0\). At the other endpoint its value is
\[
(1-p^2)+\frac{10p^2-19p+7}{4}=\frac{6p^2-19p+11}{4}.
\]
This is nonnegative for \(0\le p\le p_\star\) and negative for \(p_\star<p<1\), because its quadratic roots are \((19\pm\sqrt{97})/12\), the larger of which exceeds \(1\). For \(p\le p_\star\), the affine bracket stays nonnegative throughout the interval and is strictly positive except possibly at its right endpoint. Hence \(R(w)\) strictly decreases and has its unique minimum at \(w=1/4\), corresponding to \(a=1/2\). For \(p>p_\star\), the bracket has exactly one zero in \((0,1/4)\), equal to \(w_\star\) above, and changes sign from positive to negative. Accordingly \(R(w)\) strictly decreases then strictly increases: \(w_\star\) is the unique global minimizing product, attained at the two claimed values of \(a\). Since \(R(w)\to1\) as \(w\downarrow0\), the boundary introduces no missing minimizer.

Finally, explicit subtraction from the balanced values \(w=1/4\) gives
\[
\mathbb ET(w)-\mathbb ET(1/4)=\frac{1-4w}{w(1-p)},\qquad
\operatorname{Var}(T;w)-\operatorname{Var}(T;1/4)=\frac{(1-4w)[w(1+p^2)+(1-p)]}{w^2(1-p)^3}.
\]
Both are strictly positive when \(w<1/4\); hence balancing uniquely minimizes the unnormalized mean and variance even in the symmetry-broken relative-dispersion regime.

## Verification
The accompanying standalone exact-rational program constructs the transient Markov matrix, solves both moment equations directly, and compares the result with both closed forms on a grid of \(361\) rational parameter pairs, including \(p=0\). It passed \(1083\) exact assertions. Numerical values of the critical parameter are diagnostic only: the proof of the optimizer classification uses exact polynomial identities and interval signs, not finite enumeration.

## Relationship to prior work
Attrill and Garoni (2026, arXiv:2605.14206) give generating functions, mean and variance for the *uniform* \(m\)-type clumsy collector and limit regimes as the number of types grows. Long (2026, arXiv:2605.14511, especially Section 4) obtains stationary-entry flux, exponential hitting-time limits, and moment convergence for the *uniform* fixed-loss model. These results do not state the two-type *nonuniform* relative-dispersion optimizer or the transition between equal and unequal optimal weights. The derivation here uses elementary finite-state Markov hitting-time equations, whose general availability is prior methodology, not a novelty claim. Unlocated equivalent finite-state optimizations remain a historical-priority risk.

## Limitations
Only two types, independent refreshes, and a common loss probability are considered. The result does not prove a similar bifurcation for three or more types, nor for type-dependent losses. The exact two-state reduction and optimization are analytic; no independent mathematical audit has been performed.

## References
1. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206 (first public submission 2026-05-14), https://arxiv.org/abs/2605.14206.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (first public submission 2026-05-14), https://arxiv.org/abs/2605.14511.
