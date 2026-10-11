# Sharp residence-radius threshold and stationary rigidity in the Sprott-N flow

## Finding
Consider the real-parameter quadratic flow
\[
\dot x=-ay,\qquad \dot y=x+z^2,\qquad \dot z=1+y-bz,
\qquad a\ne0.
\]
For \(R>0\), let \(\tau_{a,b}(R)\) be the supremum of the lengths of all (finite) solution segments whose images are contained in the Euclidean ball \(x^2+y^2+z^2\le R^2\), taking the supremum over all initial conditions. The exact threshold is
\[
\tau_{a,b}(R)=\infty\quad\Longleftrightarrow\quad b\ne0\ \text{and}\ R\ge \sqrt{b^{-4}+b^{-2}}.
\]
If \(b=0\), all such segments have duration at most \(2R\sqrt{1+a^{-2}}\), so no forward-bounded trajectory or nonempty compact invariant set exists.

For \(b\ne0\), the unique equilibrium is \(E_b=(-b^{-2},0,b^{-1})\). Every compactly supported invariant probability measure \(\mu\) obeys the exact heightwise law
\[
\mathbb E_\mu[z\mid H]=b^{-1},\qquad H=z+x/a,
\]
and, putting \(L=b^{-2}\), \(v=\operatorname{Var}_\mu(z)\),
\[
\int(x^2+y^2+z^2)\,d\mu
=L^2+L+(2L+1)v+v^2+\operatorname{Var}_\mu(x)+\int y^2\,d\mu,
\]
\[
\operatorname{Cov}_\mu(x,z)=-a\operatorname{Var}_\mu(z),\qquad
\int x\,d\mu=-L-v.
\]
The radial-moment lower bound \(L^2+L\) is attained only by the equilibrium measure \(\delta_{E_b}\); every other compact stationary state has \(v>0\) and charges both \(z<b^{-1}\) and \(z>b^{-1}\).

## Assumptions and scope
The system is the two-parameter normalization of Sprott's case N described in the cited source. Here \(a\) and \(b\) are real, with \(a\ne0\), and the time variable is continuous. A solution segment means a classical solution on some interval of length \(T\ge0\). The ball is centered at the origin and uses the standard Euclidean metric. Compact invariance means invariance under the full flow on the compact set. Polynomial vector fields are locally well posed; an orbit confined to a compact set on a finite interval extends across its endpoints. A compactly supported invariant probability is invariant under the full flow.

## Proof
Define \(H=z+x/a\). Direct differentiation gives the polynomial coboundary
\[
\dot H=\dot z+\dot x/a=(1+y-bz)-y=1-bz.
\]
If \(b=0\), then \(H(t)=H(0)+t\). In the ball of radius \(R\), Cauchy–Schwarz gives \(|H|\le R\sqrt{1+a^{-2}}\); consequently \(T\le2R\sqrt{1+a^{-2}}\), with no assumption about the solution outside the segment. Forward-bounded or complete compact trajectories would have arbitrarily long such segments, a contradiction.

Suppose now \(b\ne0\), and write \(L=b^{-2}\), \(\mathcal R_b=\sqrt{L^2+L}\). The equilibrium equations force \(y=0\), \(z=b^{-1}\), \(x=-L\), so \(E_b\) is the unique equilibrium, at distance \(\mathcal R_b\) from the origin. Thus \(R\ge\mathcal R_b\) gives an arbitrarily long stationary solution segment.

Conversely, let \(R<\mathcal R_b\) and consider an arbitrary solution segment of duration \(T\ge1\) entirely within the radius-\(R\) ball. Set
\[
K=R\sqrt{1+a^{-2}},\qquad C=\frac{4K(1+K)}{b^2},\qquad D=C+2R,\qquad \Delta=L^2+L-R^2>0.
\]
An overbar denotes a time average over this segment. Integrating \(\dot H=1-bz\) yields
\[
|\bar z-b^{-1}|\le\frac{2K}{|b|T},\qquad
|\bar z^2-L|\le \frac{C}{T},
\]
where the second inequality follows from \(T\ge1\) and the product of the difference and sum of the two means. Integrating \(\dot y=x+z^2\), using \(|y(T)-y(0)|\le2R\), and applying Jensen's inequality gives
\[
\bar x\le -\overline{z^2}+\frac{2R}{T}
\le-L+\frac{D}{T}.
\]
If \(T\ge2D/L\), then \(\bar x\le -L/2\), and hence
\[
\bar x^2\ge(L-D/T)^2\ge L^2-\frac{2LD}{T}.
\]
Jensen's inequality applied to the whole position vector therefore gives
\[
R^2\ge\bar x^2+\bar z^2\ge L^2+L-\frac{2LD+C}{T}.
\]
Thus every such segment satisfies the explicit bound
\[
T\le\max\!\left\{1,\ \frac{2D}{L},\ \frac{2LD+C}{\Delta}\right\}.
\]
This handles all \(T>0\): for \(T<1\) or \(T<2D/L\), the stated maximum already exceeds the duration. The threshold equivalence is proved, including both signs of \(b\) and both signs of nonzero \(a\).

Now let \(\mu\) be a compactly supported invariant probability measure and \(b\ne0\). For every smooth function \(\phi\), compact support and invariance imply
\[
0=\int \mathcal L_F\phi(H)\,d\mu
=\int\phi'(H)(1-bz)\,d\mu.
\]
Smooth derivatives approximate all continuous functions on the compact range of \(H\), so \(\mathbb E_\mu[z\mid H]=b^{-1}\). In particular \(\bar z=b^{-1}\) and stationarity of the coordinate \(y\) yields
\[
\bar x=-\int z^2\,d\mu=-L-v.
\]
Stationarity of \(H^2/2\) gives \(\operatorname{Cov}_\mu(H,z)=0\), whence \(\operatorname{Cov}_\mu(x,z)=-av\). Expanding the second moments around the means gives the asserted exact radial identity, with every correction term nonnegative.

Finally, if \(v=0\), the invariant measure is concentrated on \(z=b^{-1}\). Invariance and the identity \(\dot z=1+y-bz\) show \(y=0\) on its support, while invariance and \(\dot y=x+z^2\) show \(x=-L\) there. Thus \(\mu=\delta_{E_b}\). If \(\mu\ne\delta_{E_b}\), then \(v>0\) and a nonconstant real random variable with mean \(b^{-1}\) necessarily takes values both above and below that mean with positive probability.

## Verification
The supplied Python script `CHECK.py` verifies the polynomial coboundary, exact equilibrium substitution, the algebraic radial-moment expansion, and the finite-residence comparison constants symbolically. Its arithmetic checks use SymPy. The infinite-time conclusions are mathematical deductions from the identities, compactness, invariance, and Jensen's inequality; finite computation is not substituted for any quantifier over all trajectories or measures.

## Relationship to prior work
Sprott's 1994 introduction specifies the original case-N system among a catalogue of low-degree chaotic flows, reports equilibrium and numerical dynamical information, and does not state a sharp origin-centered residence-radius theorem. The 2013 case-N parameter atlas presents numerical dynamical regions for the same two-parameter normalization; its illustrations do not imply either a uniform residence-time bound valid for all initial conditions or the conditional stationary identity. Related stationary-moment or recurrence-barrier results for different flows are not a direct implication for this vector field. The proof uses the special cancellation \(\dot H=1-bz\) and the positive square \(z^2\) in \(\dot y\), rather than a numerical assumption about an attractor.

## Limitations
The theorem excludes \(a=0\); that limit changes the equilibrium and balance structure. The radius threshold does not imply that non-equilibrium recurrence exists for any specific parameters, and it does not classify all compact invariant sets at or above the threshold. The explicit finite bound is an upper bound, not a proved optimal residence-time constant. The stationary results concern compactly supported invariant measures only. Novelty remains subject to the possibility of unindexed equivalent earlier statements.

## References
1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E 50, R647–R650 (1994), DOI: 10.1103/PhysRevE.50.R647. First public date used: 1994-08-01.
2. J. C. Sprott, *Dynamic Regions in Simple Chaotic Flows*, technical note dated April 27, 2013, https://sprott.physics.wisc.edu/technote/regions.htm, especially case N and the methodology for parameter-region plots.
