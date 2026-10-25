# Unique event-time reversal for angular escape versus absorption at a sticky active wall

## Finding

In the angular wall-binding subproblem of a confined active Brownian particle with constant wall-killing rate, there is **exactly one** initial-angle threshold separating which terminal event is faster on average, conditional on that event happening. Fix rotational diffusivity \(D>0\), killing rate \(\kappa>0\), and angular half-width \(L=\pi/2\). Put
\[
z=L\sqrt{\kappa/D},\qquad u=|\theta_0|/L\in[0,1).
\]
Let \(\tau_{\rm abs}(u,z)\) and \(\tau_{\rm esc}(u,z)\) be the mean time to killing and to angular escape, respectively, conditioned on the indicated event occurring before its competitor. There is a unique \(u_c(z)\in(0,1)\) such that
\[
\begin{array}{ll}
\tau_{\rm esc}>\tau_{\rm abs},&0\le u<u_c(z),\\
\tau_{\rm esc}=\tau_{\rm abs},&u=u_c(z),\\
\tau_{\rm esc}<\tau_{\rm abs},&u_c(z)<u<1.
\end{array}
\]
The threshold is the unique interior root of
\[
H(z,u)=\frac z2\big[\tanh z-u\tanh(uz)\big]-1+\frac{\cosh(uz)}{\cosh z}=0.
\]
It has the two parameter-free endpoint laws
\[
u_c(z)=\frac{1}{\sqrt5}+\frac{8\sqrt5}{1875}z^2+O(z^4)\quad(z\downarrow0),
\]
and
\[
z[1-u_c(z)]\longrightarrow w_*\quad(z\to\infty),
\qquad w_*=1.59362426004004009\ldots,
\]
where \(w_*\) is the unique positive solution of \(w=2(1-e^{-w})\). Thus the high-reactivity angular boundary layer has physical thickness \(L-|\theta_{0,c}|\sim w_*\sqrt{D/\kappa}\). The statements concern the **single bound episode at the absorbing wall**, not the total lifetime over excursions through the channel.

## Assumptions and scope

While an active particle sticks at the wall, its shifted orientation \(\Theta_t\) is one-dimensional Brownian motion with generator \(D\partial_\theta^2\) on \((-L,L)\), with absorption at the angular endpoints \(\pm L\) interpreted as escape into the channel. Independently, a constant-hazard exponential clock \(E\sim\operatorname{Exp}(\kappa)\) triggers irreversible killing at the wall. Let \(T=\inf\{t\ge0:|\Theta_t|=L\}\), with deterministic starting point \(\Theta_0=\theta_0\in(-L,L)\). The two disjoint events are \(\{E<T\}\) and \(\{T<E\}\); ties have probability zero. Conditional means refer to the elapsed time \(E\) on the first event and \(T\) on the second event. Both events have strictly positive probability for interior starts and \(D,\kappa>0\). Symmetry reduces the start to \(u=|\theta_0|/L\). No assumption on, or result for, the distribution of orientations on later wall returns is used.

## Proof

**1. Transform and conditional means.** The backward Dirichlet problem \(Df''=\kappa f\), \(f(-L)=f(L)=1\), gives the exit-time Laplace transform
\[
F(\kappa;\theta_0)=\mathbb E_{\theta_0}[e^{-\kappa T}]
=\frac{\cosh(uz)}{\cosh z}\in(0,1).
\]
Therefore \(\Pr(T<E)=F\), \(\Pr(E<T)=1-F\), and differentiation under expectation (permitted by bounded-domain exponential tails) gives
\[
\tau_{\rm esc}=-\frac{F'(\kappa)}{F},\qquad
\tau_{\rm abs}=\frac1\kappa+\frac{F'(\kappa)}{1-F}.
\]
For killing, the numerator identity is \(\mathbb E[E\mathbf1_{E<T}]=(1-F)/\kappa+F'\). Differentiating \(z=L\sqrt{\kappa/D}\) yields the **exact signed comparison**
\[
\tau_{\rm esc}-\tau_{\rm abs}
=\frac{H(z,u)}{\kappa[1-F(\kappa;\theta_0)]}.
\]
The denominator is strictly positive, so the sign is precisely that of \(H\).

**2. A single interior zero.** For every \(z>0\),
\[
H(z,0)=\frac z2\tanh z-1+\operatorname{sech}z>0,
\quad H(z,1)=0,
\quad \partial_uH(z,1)=\frac z2(\tanh z-z\operatorname{sech}^2z)>0.
\]
The first inequality is equivalent to \(z>2\tanh(z/2)\); the last follows since \(\tanh z-z\operatorname{sech}^2z\) starts at zero and has positive derivative \(2z\operatorname{sech}^2z\tanh z\). Thus \(H(z,u)<0\) just to the left of \(u=1\).

For \(0<u<1\), put \(w=uz\). Direct differentiation and positive-factor extraction show
\[
\operatorname{sgn}(\partial_uH)
=\operatorname{sgn}\!\left(\frac{2}{\cosh z}-Q(w)\right),\qquad
Q(w)=\operatorname{sech}w+\frac{w}{\sinh w}\operatorname{sech}^2w.
\]
Both terms in \(Q\) are strictly decreasing on \(w>0\): in particular \(w/\sinh w\) decreases because \(w\cosh w-\sinh w>0\), whose derivative is \(w\sinh w>0\); \(Q(0+)=2>2/\cosh z\), while
\[
Q(z)=\frac1{\cosh z}+\frac{z}{\sinh z\cosh^2 z}<\frac2{\cosh z},
\]
because \(\sinh z\cosh z>z\). Therefore \(\partial_uH\) changes sign exactly once, from negative to positive. The function \(H(z,\cdot)\) has one strict minimum, starts positive, is negative before ending at zero at \(u=1\), and hence has exactly one zero in \((0,1)\), with the stated sign pattern.

**3. Weak-killing boundary.** Uniform Taylor expansion for \(u\) in compact subsets of \([0,1)\) gives
\[
H(z,u)=\frac{(1-u^2)(1-5u^2)}{24}z^4
+\frac{(1-u^2)(47u^4+62u^2-13)}{720}z^6+O(z^8).
\]
Comparing signs either side of \(1/\sqrt5\) and invoking uniqueness shows \(u_c(z)\to1/\sqrt5\). Since the derivative in \(u\) of the coefficient of \(z^4\) at this point is nonzero, the analytic implicit-function theorem applied after dividing by \(z^4\) gives
\(u_c(z)=1/\sqrt5+(8\sqrt5/1875)z^2+O(z^4)\).
The leading threshold also has the independent moment interpretation \(\operatorname{Var}(T)=\mathbb E[T]^2\): from the exit-time boundary problems,
\[
\mathbb E[T]=\frac{L^2(1-u^2)}{2D},\quad
\mathbb E[T^2]=\frac{L^4(5-6u^2+u^4)}{12D^2},\quad
\frac{\operatorname{Var}(T)}{\mathbb E[T]^2}=\frac{2(1+u^2)}{3(1-u^2)},
\]
which equals one exactly at \(u=1/\sqrt5\).

**4. Strong-killing boundary layer.** Write \(u=1-w/z\) with fixed \(w>0\) and \(z>w\). Hyperbolic-function limits give
\[
H(z,1-w/z)\longrightarrow G(w):=\frac w2-1+e^{-w}.
\]
Here \(G(0)=0\), \(G'(0)=-1/2\), \(G''(w)=e^{-w}>0\), and \(G(w)\to\infty\). Thus exactly one strictly positive root \(w_*\) exists, with \(G<0\) on \((0,w_*)\) and \(G>0\) above it. For any fixed \(0<a<w_*<b\), the signs at \(u=1-a/z\) and \(u=1-b/z\), together with the unique interior crossing, squeeze \(z[1-u_c(z)]\) between \(a\) and \(b\) for sufficiently large \(z\). Letting \(a,b\to w_*\) proves the stated limit.

## Verification

A standalone `checker.py` uses only Python's standard library to bisect the exact comparison function and check the sign reversal, the center/boundary inequalities, the conditional-mean identity, and the two endpoint limits at representative dimensionless rates. Run with `python3 checker.py`. This numerical check supports but does not replace the analytic argument, which covers every \(D,\kappa>0\) and every interior orientation.

## Relationship to prior work

Bressloff, *Trapping of an active Brownian particle at a partially absorbing wall* (first public arXiv version 2023-02-17), derives the angular diffusion-with-killing boundary problem in section 3.2, its splitting probabilities and two conditional mean times in equations (3.18)–(3.25), and plots their orientation dependence in figure 4. The new result compares those two conditional times, proves a **unique crossover angle for every rate**, and computes its two sharp endpoint regimes. The source formulas imply our expressions for the individual means, but the one-crossing theorem and its constants require the separate sign and shape analysis above. Bressloff's *Close encounters of the sticky kind* (arXiv:2302.13986) studies an occupation-time formulation of sticky Brownian motion, not this angular-event time ordering. Related competing-trap literature addresses different geometries or absorption probabilities. The result is not a new formula for the source's full-channel mean absorption time.

## Limitations

The theorem applies only to a bound episode with constant exponential killing and unbiased rotational diffusion. It does not apply as stated to non-exponential reaction thresholds, angular drift, position-dependent rotational diffusion, or a full channel trajectory with repeated wall encounters. Literature searching cannot exclude an unindexed equivalent theorem phrased entirely as a result about exponentially killed Brownian exit times; that is the main residual originality risk.

## References

1. P. C. Bressloff, *Trapping of an active Brownian particle at a partially absorbing wall*, arXiv:2302.09105 (first version 2023-02-17), particularly sections 3.2–3.3 and equations (3.18)–(3.25); https://arxiv.org/pdf/2302.09105 .
2. P. C. Bressloff, *Close encounters of the sticky kind: Brownian motion at absorbing boundaries*, arXiv:2302.13986 (2023-02-27), particularly introduction and section III; https://arxiv.org/pdf/2302.13986 .
3. P. C. Bressloff and H. Kim, *Search-and-capture model of cytoneme-mediated morphogen gradient formation*, Phys. Rev. E 99 (2019), 052401; https://www.math.utah.edu/~bresslof/publications/19-b.pdf .
