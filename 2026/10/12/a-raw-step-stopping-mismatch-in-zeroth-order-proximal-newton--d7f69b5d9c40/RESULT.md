# A raw-step stopping mismatch in zeroth-order proximal Newton
## Finding
For every tolerance \(\varepsilon>0\), the stopping rule printed in Algorithms 1--2 of Liu and Fan's zeroth-order proximal Newton framework can terminate at the first outer iteration and return a point that is not \(\varepsilon\)-stationary, even when the objective is a scalar strongly convex quadratic and the central-difference gradient is exact.

The witness is
\[
f(x)=\frac12x^2,\qquad h(x)=0,\qquad x_0=2\varepsilon,
\]
with \(H_0=4\), \(\gamma=1\), \(c_1=1/4\), \(c_2=1\), \(\beta=1/2\), \(\bar t=1\), \(\kappa_{\rm eg}=1\), \(\underline\kappa=1\), \(\bar\kappa=4\), and \(\Delta=\varepsilon/100\). The first FISTA step is the exact subproblem minimizer,
\[
d_0=-\frac{\varepsilon}{2},
\]
so the printed test \(\|d_0\|\leq\varepsilon\) stops immediately. Algorithm 1 then returns \(x_0+d_0=3\varepsilon/2\), where
\[
\operatorname{dist}(0,\partial F(x_0+d_0))=\frac{3\varepsilon}{2}>\varepsilon.
\]
Thus the raw step-length threshold does not, with the same tolerance, certify the stationarity target asserted in Theorem 3.3.

## Assumptions and scope
The source problem is \(F=f+h\). Here \(f(x)=x^2/2\) has Lipschitz gradient constant \(L_f=1\), is bounded below, and is strongly convex; \(h\equiv0\) is proper, closed, and convex. The scalar matrix \(H_0=4\) is positive definite and satisfies \(1\leq H_0\leq4\); arbitrary positive-definite BFGS initialization is also explicitly allowed by the source's BFGS discussion. The claim needs only the first outer iteration and the assumptions used by Theorem 3.3.

For any \(\Delta>0\), the central difference is exact on this quadratic:
\[
g_0=\frac{f(x_0+\Delta)-f(x_0-\Delta)}{2\Delta}=x_0=2\varepsilon.
\]
Hence the gradient-error assumption holds with zero error and therefore with \(\kappa_{\rm eg}=1\). No stochastic or finite-precision effect is used.

## Proof
With the displayed parameters, Lemma 2.4 gives
\[
\underline t
=\frac12\min\left\{1,\frac12,2\right\}
=\frac14.
\]
The radius bound in Theorem 3.3(i) therefore specializes to
\[
\Delta\leq
\frac{(1/4)\varepsilon}{2(5+1/4)}
=\frac{\varepsilon}{42}.
\]
Our choice \(\Delta=\varepsilon/100\) satisfies this condition.

At the first inner FISTA iteration, the source uses \(\alpha=1/\|H_0\|=1/4\). Since \(h=0\) and the initial extrapolated point equals \(x_0\), its proximal update is
\[
y_{0,1}=x_0-\frac14g_0
=2\varepsilon-\frac{\varepsilon}{2}
=\frac{3\varepsilon}{2}.
\]
Thus
\[
d_0=y_{0,1}-x_0=-\frac{\varepsilon}{2}.
\]
The subproblem residual is exactly
\[
r_0=g_0+H_0d_0=2\varepsilon-2\varepsilon=0,
\]
so the source inexactness condition is satisfied exactly. Algorithm 2 returns this step, and Algorithm 1 stops because \(\|d_0\|=\varepsilon/2\leq\varepsilon\). The printed output is \(x_0+d_0=3\varepsilon/2\). Since \(h=0\), the stationarity residual there is
\[
\operatorname{dist}(0,\partial F(3\varepsilon/2))
=|f'(3\varepsilon/2)|
=\frac{3\varepsilon}{2},
\]
which is strictly larger than \(\varepsilon\).

The source's Lemma 2.5 itself gives the sufficient certificate
\[
\operatorname{dist}(0,\partial F(x_k+d_k))
\leq
(L_f+(2-\gamma)\bar\kappa)\|d_k\|+\kappa_{\rm eg}\Delta_k.
\]
Consequently, a direct repair is to stop only when the right-hand side is at most the desired stationarity tolerance.

## Verification
The standalone script `verify_zopn_stop.py` uses exact rational arithmetic after normalizing \(\varepsilon=1\). It checks the Lemma 2.4 lower step bound, the Theorem 3.3(i) sampling-radius ceiling, the exact central-difference gradient, the first FISTA step, the zero subproblem residual, the triggered stopping test, and the returned stationarity residual. The argument for all \(\varepsilon>0\) is analytic: every quantity in the witness scales linearly with \(\varepsilon\), while the relevant ratios are constant.

## Relationship to prior work
The primary source prints the raw stopping test \(\|d_k\|\leq\varepsilon\), returns \(x_k+d_k\) when it fires, and separately bounds stationarity by a scaled step term plus gradient-estimation error. Its Theorem 3.3 states an \(\varepsilon\)-stationarity guarantee under a sampling-radius condition, but its proof establishes the existence of an iterate with a substantially smaller step before invoking the stationarity bound; the proof does not address an earlier stop at the raw threshold.

A broader warning was already known for inexact proximal Newton methods: Pötzl et al. explain that unscaled small update norms can be caused by large damping and can trigger termination far from optimality, motivating a scaled stopping criterion. That prior result is conceptually related but does not state this source-specific first-iteration counterexample, does not analyze the 2026 zeroth-order framework, and does not imply the exact \(\varepsilon/42\) compatibility with Theorem 3.3(i).

## Limitations
The result concerns the literal stopping and output rules printed in the cited version and the use of the same \(\varepsilon\) as the target stationarity tolerance. It does not claim that the iteration fails if the stopping test is disabled or tightened, nor that every small-step stopping rule in proximal Newton methods is unsound. The witness uses an allowed nonidentity Hessian approximation at the first iteration; it does not address the source's particular numerical experiments, which initialize the experimental BFGS matrix at the identity.

## References
- Z. Liu and J. Fan, *A Unified Zeroth-Order Proximal Newton-Type Framework for Composite Optimization*, arXiv:2605.06016v1, 2026.
- C. Pötzl et al., *Inexact proximal Newton methods in Hilbert spaces*, Computational Optimization and Applications, DOI:10.1007/s10589-023-00515-x.
