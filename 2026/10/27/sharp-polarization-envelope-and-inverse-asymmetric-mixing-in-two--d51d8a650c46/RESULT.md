# Sharp polarization envelope and inverse asymmetric mixing in two-community logistic threshold networks

## Finding

Consider a directed two-community logistic threshold network with cross-community influence weights \(0<a,b<1\), feedback \(\beta>0\), common external stimulus \(h\in\mathbb R\), and \(\lambda=1-a-b\). There is an exact sharp boundary for heterogeneous stationary activity and a stimulus-optimized polarization envelope:

1. If \(\beta\lambda\le4\), every trajectory synchronizes in the sense that its community difference tends to zero, and **no heterogeneous stationary state exists for any stimulus**. For \(\lambda\le0\) the difference decays at least at rate \(e^{-t}\); if \(0<\beta\lambda<4\), it decays at least at rate \(e^{-(1-\beta\lambda/4)t}\). At \(\beta\lambda=4\), the sharp universal bound is \(\limsup_{t\to\infty}\sqrt t\,|x_2(t)-x_1(t)|\le\sqrt{3/2}\).
2. If \(K:=\beta\lambda>4\), there is one \(d\in(0,1)\) satisfying \(4\operatorname{artanh}(d)/d=K\). Over **all** stimuli and stationary states, the sharp maximum absolute community difference is \(d\). It is attained exactly at \((x_1,x_2)=((1-\sigma d)/2,(1+\sigma d)/2)\) for \(\sigma\in\{-1,+1\}\), at stimulus \(h_\sigma=-\beta[1+\sigma(a-b)d]/2\).
3. Let \(H(d)=(1-d^2)\operatorname{artanh}(d)/d\). Every maximizing stationary state has linearization eigenvalues \(-1+H(d)/\lambda\) and \(-1+H(d)\). For each fixed \(0<\lambda<1\), there is a unique \(d_c\in(0,1)\) with \(H(d_c)=\lambda\). The maximizer is a hyperbolic saddle for \(d<d_c\), a hyperbolic sink for \(d>d_c\), and nonhyperbolic at equality.
4. When \(\beta\) is known and both maximizing stimulus positions \(h_+,h_-\) and the maximum contrast \(d\) are available, the *directed* cross-weights are exactly identifiable: \(\lambda=4\operatorname{artanh}(d)/(\beta d)\), \(a-b=(h_- -h_+)/(\beta d)\), and \(a=[1-\lambda+(a-b)]/2\), \(b=[1-\lambda-(a-b)]/2\). These formulas identify parameters of the specified deterministic quotient, not arbitrary stochastic agents or unequitable networks.

## Assumptions and scope

Write \(L(s)=(1+e^{-s})^{-1}\) and let
\[
B=\begin{pmatrix}1-a&a\\b&1-b\end{pmatrix},\qquad
\dot x_i=-x_i+L\!\left(h+\beta(Bx)_i\right),\quad i=1,2.
\]
Here \(0<a,b<1\), \(\beta>0\), \(h\in\mathbb R\) is held fixed along a trajectory, and \(x(0)\in[0,1]^2\). The square is forward invariant; every equilibrium lies in \((0,1)^2\). This system is an exact equitable two-block quotient of the row-stochastic threshold-response dynamics studied in the motivating preprint, with logistic threshold distribution. The stimulus is allowed to vary *only* when optimizing across equilibria. The theorem makes no claim that a saddle is reached from generic initial states or that observed trajectories automatically reveal the maximizing stimulus.

## Proof

**1. Exact difference inequality and sharp synchronization.** Put \(\Delta=x_2-x_1\). Subtracting the equations and using \((Bx)_2-(Bx)_1=\lambda\Delta\) gives
\[
\dot\Delta=-\Delta+L(z+\beta\lambda\Delta)-L(z)
\]
for a state-dependent \(z\). For any real \(s\), the maximal absolute difference of two logistic values at arguments separated by \(s\) is \(\tanh(|s|/4)\): write \(L(v)=[1+\tanh(v/2)]/2\), differentiate the difference in its midpoint, and see that the unique positive maximum is attained when the midpoint is zero. For \(\lambda\le0\), monotonicity of \(L\) implies \(\operatorname{sgn}(\Delta)[L(z+\beta\lambda\Delta)-L(z)]\le0\), yielding \(D^+|\Delta|\le-|\Delta|\). For \(\lambda>0\),
\[
D^+|\Delta|\le-|\Delta|+\tanh\big(\beta\lambda|\Delta|/4\big).
\]
When \(K=\beta\lambda<4\), \(\tanh(s)\le s\) yields the exponential estimate. When \(K=4\), comparison with \(y'=-y+\tanh y\), \(y(0)=|\Delta(0)|\), implies \(\Delta(t)\to0\). For \(y(0)>0\), \(y'=-y^3/3+O(y^5)\); hence \((y^{-2})'=2/3+O(y^2)\), so \(\sqrt t\,y(t)\to\sqrt{3/2}\). The bound is sharp: take \(a=b\) with \(0<\lambda<1\), \(\beta=4/\lambda\), \(h=-\beta/2\), and initial data satisfying \(x_1+x_2=1\), \(x_1\ne x_2\). This line is invariant, and the difference obeys exactly \(\dot\Delta=-\Delta+\tanh\Delta\). A heterogeneous equilibrium in either subcritical case would contradict the strict decay of its constant nonzero difference.

**2. Exact optimum over all equilibria.** At an equilibrium, \(\operatorname{logit}(x_i)=h+\beta(Bx)_i\), where \(g(x)=\log(x/(1-x))\). Thus
\[
g(x_2)-g(x_1)=K(x_2-x_1).
\]
Suppose \(q=x_2-x_1>0\); the negative case follows by interchanging orientations. Since \(g'(x)=1/[x(1-x)]\) is strictly increasing as \(|x-1/2|\) increases, the integral \(g(x+q)-g(x)=\int_x^{x+q}g'(v)\,dv\) is uniquely minimized among \(0<x<1-q\) when the interval is centered at \(1/2\). (Equivalently differentiate: its derivative is \(g'(x+q)-g'(x)\), with a unique sign change at \(x=(1-q)/2\).) Its minimum is \(4\operatorname{artanh}(q)\). Consequently \(K\ge4\operatorname{artanh}(q)/q\). This right side is strictly increasing from \(4\) to infinity: its derivative has numerator \(q/(1-q^2)-\operatorname{artanh}(q)>0\), as is seen by differentiating once. This proves absence of heterogeneous equilibria at \(K\le4\), existence of a unique cap \(q\le d\) at \(K>4\), and uniqueness of the centered maximizers. Substituting the two centered configurations into the logit equations gives \(h_\sigma=-\beta[1+\sigma(a-b)d]/2\). Both are valid equilibria, so the cap is attained.

**3. Local stability of the maximizers.** At a centered maximizer both logistic derivatives equal \((1-d^2)/4\), so the Jacobian is \(J=-I+\beta(1-d^2)B/4\). The two eigenvalues of \(B\) are \(1\) and \(\lambda\), giving the asserted eigenvalues after using \(K=4\operatorname{artanh}(d)/d\). Here \(0<\lambda<1\), since \(a,b>0\) and \(K>4\). The function \(H\) is strictly decreasing from one to zero because \(\operatorname{artanh}(d)>d/(1+d^2)\) implies \(H'(d)<0\). Thus the contrast eigenvalue is always negative and the common-mode eigenvalue changes sign exactly once at \(H(d)=\lambda\). The descriptions saddle, sink, and nonhyperbolic follow without claiming nonlinear stability at equality.

**4. Inverse weights.** The contrast relation recovers \(\lambda\) from \((d,\beta)\), while the difference between the two maximizing stimulus positions is \(h_--h_+=\beta(a-b)d\). Sum-and-difference inversion of \(a+b=1-\lambda\) proves the formulas. There is no sign ambiguity if the two contrast orientations are labeled consistently.

## Verification

The standalone file `verify.py` uses only the Python standard library. Running `python verify.py` reproduces high-precision constructed stationary contrasts, both maximizing stimulus orientations, inversion of directed mixing weights, saddle/sink eigenvalue signs, midpoint-optimized logit secants, monotonicity of the contrast and stability threshold functions, disassortative contractivity, and a numerical cross-check of the sharp critical scalar asymptotic. Finite parameter checks do not replace any infinite-parameter proof; all quantifiers above are justified analytically. Computations do not assess historical priority.

## Relationship to prior work

Boudourides (2026, arXiv:2609.10580v1) studies the same general row-stochastic threshold ODE and its exact equitable reductions. That article proves weak-feedback global contraction, independent-block multistability under small coupling, and cusp bifurcations for **symmetrically** coupled two blocks. The present result instead optimizes the *activity difference* over all stimuli for the directed asymmetric logistic quotient, gives an exact threshold and critical synchronization rate for the community difference, and reconstructs the asymmetry from the two optimizing stimuli. Earlier symmetric two-community tanh fixed-point calculations cover the symmetric fixed-field reduction by affine change of variables; they do not yield directed stimulus offsets or the two-orientation parameter inverse. Kaye's scalar threshold model and related binary-choice mean-field analyses motivate collective switching but do not provide this asymmetric contrast-envelope/inverse problem. The scalar cubic critical decay and logistic maximum-slope facts are standard tools, not presented as new mathematical phenomena. Historical-priority risk persists because broad two-population sigmoid fixed-point theory could subsume some parts of this classification.

## Limitations

Results concern the exact deterministic, two-block, logistic, constant-stimulus quotient with positive cross-weights. They do not imply whole-network synchronization within blocks away from the equitable invariant subspace, global convergence of both coordinates to a unique equilibrium, generic observability of saddle-type envelope maximizers, robustness under heterogeneous thresholds, or statistical identifiability from finite noisy observations. At the critical spectral stability boundary only nonhyperbolicity is asserted. Independent scientific audit has not been performed.

## References

1. M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580v1 (first public 2026-09-05), https://arxiv.org/html/2609.10580v1.
2. Kaye, *From individual thresholds to collective hysteresis: a mechanistic model of the dawn chorus*, Journal of the Royal Society Interface, DOI:10.1098/rsif.2026.0267 (2026).
3. Holehouse and Pollitt, *Non-equilibrium time-dependent solution to discrete choice with social interactions*, PLOS ONE, DOI:10.1371/journal.pone.0267083 (2022).
