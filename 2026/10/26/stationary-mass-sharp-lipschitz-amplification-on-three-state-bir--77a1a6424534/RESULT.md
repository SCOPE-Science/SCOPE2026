# Stationary-mass sharp Lipschitz amplification on three-state birth–death chains

## Finding

Let \(X=\{0,1,2\}\) carry graph distance \(d(i,j)=|i-j|\). Consider every continuous-time birth–death chain with strictly positive rates \(u=q_{01}\), \(v=q_{10}\), \(w=q_{12}\), and \(z=q_{21}\), with backward Markov generator
\[
Q=\begin{pmatrix}-u&u&0\\v&-(v+w)&w\\0&z&-z\end{pmatrix},\qquad H_t=e^{tQ}.
\]
For a function \(f:X\to\mathbb R\), set \(\operatorname{Lip}(f)=\max\{|f(1)-f(0)|,|f(2)-f(1)|\}\), and define the induced operator seminorm on the quotient by constants.

**Exact profile.** Put
\[
x=u+v,\quad y=w+z,\quad s=\frac{x+y}{2},\quad d_0=\frac{x-y}{2},\quad
\delta=\sqrt{d_0^2+vw},\quad k=\frac{\max\{w-d_0,v+d_0\}}{\delta}.
\]
Then \(s>\delta>0\), and for every \(t\ge0\),
\[
\boxed{\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
=e^{-st}\left[\cosh(\delta t)+k\sinh(\delta t)\right].}
\]
In fact, \(f(i)=i\) and its negatives realize the norm for every \(t\ge0\). For positive time, the maximizing edge is independent of time. The norm is at most one at every time exactly when \(w\le u+v\) and \(v\le w+z\). Otherwise it has a unique maximum at
\[
t_*={1\over2\delta}\log\!\left(\frac{(s+\delta)(k-1)}{(s-\delta)(k+1)}\right)>0.
\]
This profile and its elementary contractivity criterion are included to specify the optimization problem precisely; novelty is not claimed for the latter criterion apart from the theorem below.

**Stationary-mass sharp envelope.** Fix any strictly positive invariant probability vector \(\pi=(\pi_0,\pi_1,\pi_2)\). Among all irreducible birth–death generators with this invariant distribution (equivalently, all edge conductances \(c_1=\pi_0u=\pi_1v>0\) and \(c_2=\pi_1w=\pi_2z>0\)), the exact sharp all-time Lipschitz amplification envelope is
\[
\boxed{\sup_{c_1,c_2>0}\sup_{t\ge0}\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
=1+\max\left\{\frac{\pi_0}{\pi_0+\pi_1},\frac{\pi_2}{\pi_1+\pi_2}\right\}.}
\]
The strict inequality \(\|H_t\|<1+\max\{\pi_0/(\pi_0+\pi_1),\pi_2/(\pi_1+\pi_2)\}\) holds for every positive conductance pair and finite \(t\ge0\). The envelope is approached, but never attained, by letting one conductance tend to zero while the other equilibrates on its two-vertex component. For the uniform invariant vector, its value is exactly \(3/2\). Across all strictly positive stationary laws the overall supremum is \(2\), never attained.

**Strict conductance monotonicity.** With \(\pi\) and \(c_1\) fixed, the second gradient-row sum \(r_2(t)\) decreases strictly as \(c_2\) increases, at every \(t>0\); the symmetric assertion holds for \(r_1(t)\) as \(c_1\) increases. More precisely,
\[
\begin{aligned}
r_2(t)&<1+\frac{\pi_0}{\pi_0+\pi_1}\left(1-e^{-(u+v)t}\right),\\
r_1(t)&<1+\frac{\pi_2}{\pi_1+\pi_2}\left(1-e^{-(w+z)t}\right),\qquad t>0.
\end{aligned}
\]
The right-hand side of each inequality is the exact weak-other-edge limit and is therefore sharp at every fixed positive time.

## Assumptions and scope

All four rates and all three invariant masses are strictly positive. The metric assigns length one to each of the two path edges; it is not rescaled by jump rates. The generator is the *backward* generator acting on functions; it is neither row-normalized nor a discrete-time transition matrix. All the operators act on real Lipschitz functions modulo constants. Complex scalars give the same norm because the induced gradient matrices have nonnegative entries. All optimizations over rates preserve the given \(\pi\) through the parametrization \(u=c_1/\pi_0\), \(v=c_1/\pi_1\), \(w=c_2/\pi_1\), \(z=c_2/\pi_2\).

## Proof

**1. Gradient similarity and exact row norms.** For \(g=(f(1)-f(0),f(2)-f(1))^\top\), direct subtraction of the components of \(Qf\) gives the gradient generator
\[
B=\begin{pmatrix}-(u+v)&w\\v&-(w+z)\end{pmatrix}.
\]
Every \(g\in\mathbb R^2\) occurs as a gradient, and \(\operatorname{Lip}(f)=\|g\|_\infty\); therefore the desired induced norm is exactly \(\|e^{tB}\|_{\ell_\infty^2\to\ell_\infty^2}\). Since \(B\) is irreducible Metzler, \(e^{tB}\) is entrywise positive for \(t>0\); its norm is its maximum row sum, achieved by \(g=(1,1)^\top\). The identity
\[
B=-sI+\begin{pmatrix}-d_0&w\\v&d_0\end{pmatrix},\qquad
\begin{pmatrix}-d_0&w\\v&d_0\end{pmatrix}^{\!2}=\delta^2 I
\]
gives the stated two row sums
\[
\begin{aligned}
r_1(t)&=e^{-st}\left[\cosh(\delta t)+\frac{w-d_0}{\delta}\sinh(\delta t)\right],\\
r_2(t)&=e^{-st}\left[\cosh(\delta t)+\frac{v+d_0}{\delta}\sinh(\delta t)\right].
\end{aligned}
\]
Because \(\sinh(\delta t)>0\) for \(t>0\), their ordering cannot change with time. Also \(s^2-\delta^2=(u+v)(w+z)-vw=uw+uz+vz>0\).

**2. Contractivity and peak time.** The row-sum derivatives at zero are \(r_1'(0)=w-u-v\), \(r_2'(0)=v-w-z\). If both are nonpositive, \(B\mathbf1\le0\), and positivity of \(e^{tB}\) gives \(e^{tB}\mathbf1\le\mathbf1\) for every time. If either derivative is positive, the norm exceeds one immediately. Write the maximizing row as
\[
r(t)=\frac{1+k}{2}e^{-(s-\delta)t}+\frac{1-k}{2}e^{-(s+\delta)t}.
\]
For an initially increasing norm \(k>s/\delta>1\), the equation \(r'(t)=0\) has exactly one positive root, displayed above. The derivative changes from positive to negative. The strict spectral inequality \(s>\delta\) gives \(r(t)\to0\) as \(t\to\infty\).

**3. Nontrivial conductance monotonicity.** Fix \(\pi\), write
\[
\alpha=\frac1{\pi_0}+\frac1{\pi_1},\quad
\beta=\frac1{\pi_1}+\frac1{\pi_2},\quad
B=\begin{pmatrix}-\alpha c_1&c_2/\pi_1\\c_1/\pi_1&-\beta c_2\end{pmatrix},
\]
and put \(E(\tau)=e^{\tau B}\), \(r(t)=E(t)\mathbf1\). Since \(\partial_{c_2}B=\begin{pmatrix}0&1/\pi_1\\0&-\beta\end{pmatrix}\), Duhamel's differentiation formula gives
\[
\frac{\partial r_2(t)}{\partial c_2}
=\int_0^t r_2(s)\left[\frac{E_{21}(t-s)}{\pi_1}-\beta E_{22}(t-s)\right]ds.
\]
Here \(r_2(s)>0\). We prove the bracket strictly negative for every nonnegative argument. From the exact exponential,
\[
\frac{E_{21}(\tau)}{E_{22}(\tau)}
=\frac{v\tanh(\delta\tau)}{\delta+d_0\tanh(\delta\tau)}
<\frac{v}{\delta+d_0},\qquad\tau>0,
\]
while at \(\tau=0\) the ratio is zero. The fraction is strictly increasing in \(\tanh(\delta\tau)\in[0,1)\), and \(\delta+d_0>0\). To bound its limiting value, define \(h=c_1/(\beta\pi_1^2)\). An exact calculation yields
\[
\delta^2-(h-d_0)^2
=\frac{c_1^2}{\beta\pi_1^2}\left(\alpha-\frac1{\beta\pi_1^2}\right)>0.
\]
The final inequality follows from \(\alpha\beta\pi_1^2>1\). If \(d_0\ge h\), then \(\delta+d_0>h\) immediately; if \(d_0<h\), the displayed identity gives \(\delta>h-d_0\). In either case \(\delta+d_0>h\), hence
\[
\frac{v}{\delta+d_0}<\frac{c_1/\pi_1}{h}=\beta\pi_1.
\]
Thus the integrand in the Duhamel formula is strictly negative for \(t>0\), proving \(\partial_{c_2}r_2(t)<0\). Reflecting the labels \(0\leftrightarrow2\) proves \(\partial_{c_1}r_1(t)<0\).

**4. Endpoint limiting rows and universal optimum.** Send \(c_2\downarrow0\) with \(\pi,c_1,t\) fixed. The limiting triangular gradient generator is \(B_0=\begin{pmatrix}-\alpha c_1&0\\c_1/\pi_1&0\end{pmatrix}\), so direct solution gives
\[
\lim_{c_2\downarrow0}r_2(t)
=1+\frac{\pi_0}{\pi_0+\pi_1}(1-e^{-\alpha c_1t}).
\]
The strict monotonicity established above gives the first stated upper bound. Reflection and \(c_1\downarrow0\) give the second. Both upper bounds are strictly smaller than their corresponding stationary ratios plus one at finite positive time. At time zero the norm equals one, also strictly below the envelope. It follows that the fixed-\(\pi\) supremum is at most the boxed value, without attainment. For sharpness, hold \(c_1=1\), take \(c_2=\varepsilon^2\), and let \(t=\varepsilon^{-1}\) as \(\varepsilon\downarrow0\). Then the fast \(0\!\leftrightarrow\!1\) component equilibrates while escape across the slow edge vanishes, giving \(r_2(t)\to1+\pi_0/(\pi_0+\pi_1)\); reversing the edges gives the other stationary ratio. The overall envelope across \(\pi\) is less than \(2\) for each positive \(\pi\), and tends to \(2\) as an endpoint mass dominates its adjacent middle mass.

## Verification

The accompanying `verify.py` independently constructs the full three-state transition matrix and computes the exact one-dimensional Wasserstein distance between each pair of adjacent starting states by cumulative signed masses, independently of the gradient reduction. It also compares the closed hyperbolic profile to the matrix exponential, checks both strict stationary-envelope bounds and conductance monotonicity over reproducibly randomized parameter samples, and checks the singular optimization regime. Run `python verify.py` with NumPy and SciPy installed. This is finite computational corroboration; the universal claims are proved by the algebra and inequalities above.

## Relationship to prior work

Ollivier's 2007 coarse Ricci curvature framework makes graph-distance Wasserstein contraction and Lipschitz duality natural. Veysseire's 2012 continuous-time contraction theorem connects local curvature estimates to global Markov semigroup bounds. Münch and Wojciechowski's 2017 general graph-Laplacian curvature formula and heat-flow equivalence cover the simple local contractivity criterion for birth–death chains; it is not asserted as new here. The distinct claim proved here is a complete four-rate time profile together with the strict **fixed invariant distribution** optimization and its sharp endpoint-mass envelope, including a conductance derivative inequality and nonattainment. Such an exact stationary-mass envelope is not implied by a local curvature lower bound, because the latter fixes the generator and supplies an exponential estimate rather than optimizing over conductances and times.

## Limitations

The theorem covers only positive-rate three-state nearest-neighbor birth–death chains with unit-edge graph metric. General longer paths, arbitrary non-path finite chains, metric distances derived from inverse conductances, discrete-time chains and normalized Laplacians are not included. The stationary-mass envelope is a supremum realized only through degenerating conductance sequences, not an actual irreducible optimizer. Prior equivalent formulations in literature not discovered by the cited searches remain possible.

## References

1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first submitted 2007-01-30. https://arxiv.org/abs/math/0701886
2. Laurent Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420, first submitted 2012-02-02. https://arxiv.org/abs/1202.0420
3. Florentin Münch and Radoslaw K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first submitted 2017-12-04. https://arxiv.org/abs/1712.00875
