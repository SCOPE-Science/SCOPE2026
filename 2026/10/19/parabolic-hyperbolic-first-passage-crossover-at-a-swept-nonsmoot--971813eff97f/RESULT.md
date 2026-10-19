# Parabolic–hyperbolic first-passage crossover at a swept nonsmooth fold

## Finding

For a scalar discrete nonsmooth fold under a linearly swept control parameter, a simultaneously weakening repelling multiplier produces a sharp, continuous transition between algebraic and logarithmic first-passage times. For fixed \(0<a<1\), a fixed observation level \(L>0\), and the affine evolution defined below, let \(N_{\varepsilon,\delta}(L)\) be the first iteration at which the distinguished tracking orbit reaches \(L\). If \(\varepsilon\downarrow0\) and \(\delta/\sqrt{\varepsilon}\to\kappa\in[0,\infty)\), then

\[
\sqrt{\varepsilon}\,N_{\varepsilon,\delta}(L)\longrightarrow T_\kappa(L),
\qquad
H_\kappa(T_\kappa(L))=L,
\]

where \(T_\kappa(L)>0\) is the unique solution and

\[
H_\kappa(t)=\int_0^t s\,e^{\kappa(t-s)}\,ds
=\begin{cases}
\dfrac{e^{\kappa t}-1-\kappa t}{\kappa^2},&\kappa>0,\\[4pt]
\dfrac{t^2}{2},&\kappa=0.
\end{cases}
\]

In the exact scaling \(\delta=\kappa\sqrt{\varepsilon}\) with fixed \(\kappa\ge0\), this improves to

\[
N_{\varepsilon,\delta}(L)=\frac{T_\kappa(L)}{\sqrt{\varepsilon}}+O_{a,L,\kappa}(1).
\]

In the distinct near-neutral hyperbolic regime \(\delta\to0\) and \(\delta/\sqrt{\varepsilon}\to\infty\), the same first-passage time satisfies the sharper logarithmic identity

\[
\boxed{
N_{\varepsilon,\delta}(L)\log(1+\delta)
-\log\!\left(\frac{L\delta^2}{\varepsilon}\right)\longrightarrow0.
}
\]

In particular, at the neutral boundary \(\delta=0\), \(N_{\varepsilon,0}(L)\sim\sqrt{2L/\varepsilon}\). The crossover function \(\kappa\mapsto T_\kappa(L)\) is strictly decreasing, so the hyperbolic strengthening always advances the threshold crossing.

## Assumptions and scope

Let \(a\in(0,1)\), \(L>0\), \(\varepsilon>0\), \(\delta\ge0\), and let \(n\in\mathbb Z\) denote the iteration index. Consider the continuous piecewise-affine nonautonomous map

\[
x_{n+1}=\begin{cases}
 a x_n+\varepsilon n,&x_n\le0,\\
 (1+\delta)x_n+\varepsilon n,&x_n\ge0.
\end{cases}
\]

At \(x_n=0\) the two formulae coincide, so the map is unambiguous. For frozen control \(\mu=\varepsilon n<0\) and \(\delta>0\), the left attracting and right repelling fixed points are \(\mu/(1-a)<0\) and \(-\mu/\delta>0\), respectively. They meet at the switching boundary and disappear for positive frozen control. The neutral boundary \(\delta=0\) corresponds to loss of invertibility of the right fixed-point equation \((1-(1+\delta))x=\mu\).

Set \(q=1-a\) and \(n_0=\lceil q^{-1}\rceil\). Select the distinguished orbit by its exact negative-time affine tracking history

\[
x_n=\varepsilon\left(\frac{n}{q}-\frac1{q^2}\right),
\qquad n\le n_0.
\]

This is compatible with the recurrence on the left; it is the unique negative-time affine solution whose difference from the instantaneous left fixed-point path \(\varepsilon n/q\) stays bounded as \(n\to-\infty\). The right branch determines its continuation for \(n\ge n_0\). Define

\[
N_{\varepsilon,\delta}(L)=\min\{n\in\mathbb Z:n\ge n_0,\ x_n\ge L\}.
\]

The minimum exists and is finite. All asymptotic statements hold for fixed \(a,L\); the hyperbolic formula additionally requires \(\delta\to0\), not merely an arbitrary fixed repelling slope.

## Proof

**1. Exact branch transition.** For \(n<n_0\), the affine tracking solution is negative, while at \(n=n_0\) it is nonnegative. The affine identity

\[
a\left(\frac n q-\frac1{q^2}\right)+n
=\frac{n+1}{q}-\frac1{q^2}
\]

proves compatibility through the switch. For \(n\ge n_0\) put \(b=1+\delta\) and \(v_n=x_n/\varepsilon\). Then \(v_{n_0}\ge0\), and \(v_{n+1}=b v_n+n\) is positive and strictly increasing after the switch. In particular \(N_{\varepsilon,\delta}(L)\) exists, and the branch cannot be re-entered. Iteration gives the exact formula

\[
v_n=b^{n-n_0}v_{n_0}+\sum_{j=n_0}^{n-1}j b^{n-1-j}
=S_n+c_{a}(b)b^n,
\]

where

\[
S_n=\sum_{j=0}^{n-1}j b^{n-1-j},\qquad
c_a(b)=b^{-n_0}v_{n_0}-\sum_{j=0}^{n_0-1}j b^{-j-1}.
\]

The finite quantity \(c_a(b)\) is bounded as \(b\downarrow1\). Differentiating the finite geometric sum, or multiplying the recurrence by \(\delta^2\), gives

\[
S_n=\begin{cases}
\dfrac{b^n-1-n\delta}{\delta^2},&\delta>0,\\[5pt]
\dfrac{n(n-1)}2,&\delta=0.
\end{cases}
\tag{1}
\]

All later limits are obtained from this identity; no replacement of the dynamics by a heuristic differential equation is needed.

**2. Finite crossover parameter.** Set \(h=\sqrt{\varepsilon}\), and assume \(\delta/h\to\kappa<\infty\). For \(n=\lfloor t/h\rfloor\), the sum from step 1 is a Riemann sum:

\[
\varepsilon S_n
=h\sum_{j=0}^{n-1}(jh)(1+\delta)^{n-1-j}
\longrightarrow\int_0^t s e^{\kappa(t-s)}\,ds
=H_\kappa(t).
\]

The convergence is uniform for \(t\) in any fixed compact interval, including when \(\kappa=0\). Meanwhile \(\varepsilon c_a(b)b^n\to0\) uniformly on such intervals, because \(c_a(b)=O_a(1)\) and \(b^n\) stays bounded. Hence \(x_{\lfloor t/h\rfloor}\to H_\kappa(t)\). For \(t>0\),

\[
H_\kappa'(t)=\int_0^t s\kappa e^{\kappa(t-s)}\,ds+t>0,
\]

so \(H_\kappa\) rises continuously from zero to infinity. Monotonicity of the discrete orbit and bracketing at \(T_\kappa(L)\pm\eta\) imply \(hN_{\varepsilon,\delta}(L)\to T_\kappa(L)\).

If \(\delta=\kappa h\) exactly, the exponential approximation and the Riemann sum each have error \(O_{a,\kappa,T}(h)\), uniformly on compact \(t\)-intervals, and the initial-history term is \(O_a(h^2)\). Because \(H_\kappa'(T_\kappa(L))>0\), inversion gives \(|hN-T_\kappa(L)|=O(h)\), equivalently the asserted \(O(1)\) iteration error. For fixed \(t>0\), the integral defining \(H_\kappa(t)\) is strictly increasing with \(\kappa\) (its integrand is strictly increasing on a positive-measure subset), so its inverse \(T_\kappa(L)\) is strictly decreasing in \(\kappa\).

**3. Hyperbolic near-neutral regime.** Now assume \(\delta\downarrow0\), \(\delta/h\to\infty\), and write \(R=L\delta^2/\varepsilon\to\infty\). Fix \(\eta>0\), and choose integers \(n_\pm\) satisfying

\[
n_\pm\log(1+\delta)=\log R\pm\eta+O(\log(1+\delta)).
\]

Then \(n_\pm\delta=O(\log R)\), \(b^{n_\pm}/R\to e^{\pm\eta}\), and the exact identity (1) yields

\[
\frac{x_{n_\pm}}L
=\frac{b^{n_\pm}}R
-\frac{1+n_\pm\delta}{R}
+\delta^2 c_a(b)\frac{b^{n_\pm}}R
\longrightarrow e^{\pm\eta}.
\]

For sufficiently small \(\varepsilon\), the lower test point is below \(L\) and the upper point above \(L\). Therefore \(n_-<N_{\varepsilon,\delta}(L)\le n_+\); taking \(\varepsilon\to0\) and then \(\eta\downarrow0\) proves

\[
N_{\varepsilon,\delta}(L)\log(1+\delta)-\log R\to0.
\]

This closes the proof of both regimes and their matching boundary.

## Verification

The accompanying standalone `verify_crossover.py` uses only Python's standard library. It checks the finite-sum formula, the sign-switching trajectory, and its exact-rational version for four contracting slopes and three repelling-slope offsets through at least forty steps. A separately implemented direct numerical recurrence compares five finite-crossover parameters against the unique root of \(H_\kappa(T)=L\) for five sweep rates; two families of near-neutral hyperbolic offsets are checked over three rates each. These are finite consistency tests. Infinite-time and uniform-limit claims follow from the proof above, not from those tests.

Run `python verify_crossover.py` from the directory containing this document and the code file.

## Relationship to prior work

Simpson, *Nonsmooth folds as tipping points* (first public 2024), proves divergence for frozen piecewise-linear maps beyond a nonsmooth fold under nondegeneracy conditions. The claim here concerns a time-dependent swept map and its threshold-crossing rate as the repelling multiplier approaches the parabolic boundary, which Simpson's frozen-map statement does not determine.

Budd and Kuske, *Dynamic tipping and cyclic folds, in a one-dimensional non-smooth dynamical system linked to climate models* (first public 2023), calculate logarithmic sweep-delay asymptotics for an analogous continuous-time absolute-value differential equation with fixed hyperbolicity. The present theorem establishes a *discrete* exact recurrence and the singular joint multiplier–sweep crossover with explicit function \(H_\kappa\). The logarithmic behavior for fixed hyperbolicity is background, not claimed as novel.

Chu, Lin and Tsai, *Slow Passage through a Saddle-Node Bifurcation in Discrete Dynamical Systems* (first public 2023), treat the Euler discretization of a *smooth quadratic* saddle-node, with a two-thirds-power time-scale in the swept parameter. Their equation and estimates do not specialize to a two-branch affine nonsmooth fold or its parabolic–hyperbolic crossover.

## Limitations

The theorem applies only to the specified scalar affine family and its distinguished tracking orbit, with fixed \(a\in(0,1)\) and threshold \(L>0\). It does not prove persistence under nonlinear perturbations, robustness under noise, or the same laws for multidimensional maps. The neutral endpoint \(\delta=0\) is a degenerate border-collision limit: the frozen right fixed point ceases to be isolated, so generic nondegenerate-fold claims do not automatically apply there. The threshold \(L\) is an observation convention, not a universal physical tipping criterion. Earlier equivalent forms of the crossover in broader discrete nonautonomous theory cannot be excluded by finite literature searches; independent priority review remains necessary.

## References

1. D. J. W. Simpson, *Nonsmooth folds as tipping points*, arXiv:2406.04587v1 (7 June 2024), sections 1 and 3, especially Theorem 1. https://arxiv.org/abs/2406.04587
2. C. Budd and R. Kuske, *Dynamic tipping and cyclic folds, in a one-dimensional non-smooth dynamical system linked to climate models*, arXiv:2305.09902v1 (17 May 2023), sections 1–2; later in Physica D **457** (2024), article 133949. https://arxiv.org/abs/2305.09902
3. J. Chu, J.-J. Lin, and J.-C. Tsai, *Slow Passage through a Saddle-Node Bifurcation in Discrete Dynamical Systems*, arXiv:2311.07242v1 (13 November 2023), sections 1–3. https://arxiv.org/abs/2311.07242
4. C. Kiers, *Rate-induced Tipping in Discrete-time Dynamical Systems*, arXiv:1907.11601 (2019), for general qualitative discrete nonautonomous tipping context. https://arxiv.org/abs/1907.11601
