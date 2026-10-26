# An exponentially thin endpoint extremizer for mean-centered fractional Volterra integration

## Finding
Let \(I_\alpha\) denote the left Riemann–Liouville integral on \([0,1]\), and let \(Q\) subtract the output's uniform spatial mean. For every \(\frac12\le\alpha<1\), the sharp complex or real \(L^\infty(0,1)\)-operator norm of \(T_\alpha=QI_\alpha\) is
\[
\boxed{\|T_\alpha\|_{\infty\to\infty}=
\frac{x_\alpha^\alpha/\alpha-1/[\alpha(\alpha+1)]+2(1-x_\alpha)^{\alpha+1}/[\alpha(\alpha+1)]}{\Gamma(\alpha)},}
\]
where \(x_\alpha\) is the **unique** solution in \((0,\alpha^{1/(1-\alpha)})\) of
\[
x_\alpha^{1-\alpha}(1-x_\alpha)^\alpha=\alpha/2.
\]
The unique norm-maximizing evaluation point is \(x_\alpha\). Every norm-one extremizing input, modulo null sets, is of the form \(e^{i\theta}\) on \((0,x_\alpha)\) and \(-e^{i\theta}\) on \((x_\alpha,1)\), with \(|e^{i\theta}|=1\); over the reals the global phase is a sign. In particular, for the Abel half-integral,
\[
x_{1/2}=\frac{2-\sqrt3}{4},\qquad
\boxed{\|T_{1/2}\|_{\infty\to\infty}=\frac{3\sqrt6+\sqrt2-4}{3\sqrt\pi}.}
\]
As \(\varepsilon=1-\alpha\downarrow0\), the maximizing point and the sharp improvement over evaluation at the initial endpoint obey
\[
x_\alpha\sim e^{-1}2^{-1/\varepsilon},\qquad
\boxed{\|T_\alpha\|_{\infty\to\infty}-\frac1{\Gamma(\alpha+1)(\alpha+1)}
\sim\frac{2}{e}\,\varepsilon\,2^{-1/\varepsilon}.}
\]
At \(\alpha=1\), the ordinary mean-centered Volterra integral has norm \(1/2\), with maximizing evaluations at the two endpoints. Thus the interior peak at every strictly fractional order persists but becomes exponentially narrow as the integer order is approached.

## Assumptions and scope
For any \(0<\alpha\le1\), define the bounded map \(I_\alpha:L^\infty(0,1;\mathbb C)\to C([0,1];\mathbb C)\) by
\[
(I_\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}f(t)\,dt.
\]
Set \((Qg)(x)=g(x)-\int_0^1g(s)\,ds\). The operator norm is for the standard essential-supremum input norm and supremum output norm (equivalently essential supremum). Uniform continuity of the integral output follows by \(L^1\)-translation continuity of the integrable fractional kernel. The sharp classification and boundary-layer asymptotic concern \(\frac12\le\alpha<1\); no optimality claim is made below one-half or above one. The factorial normalization is \(\Gamma(\alpha)\), not \(\Gamma(\alpha+1)\).

## Proof
**1. Exact kernel and reduction to row variations.** Fubini is justified by bounded input and the integrability of \((s-t)^{\alpha-1}\). One obtains
\[
(T_\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^1K_\alpha(x,t)f(t)\,dt,
\qquad K_\alpha(x,t)=\mathbf1_{t<x}(x-t)^{\alpha-1}-\frac{(1-t)^\alpha}{\alpha}.
\]
Consequently, for \(S_\alpha(x)=\int_0^1|K_\alpha(x,t)|\,dt\),
\(\|T_\alpha\|=\max_{0\le x\le1}S_\alpha(x)/\Gamma(\alpha)\). The upper bound is the integral triangle inequality; the reverse bound at a maximizing row is attained by the measurable sign of its real kernel. The kernel's \(L^1\)-continuity in \(x\) makes the maximum exist.

**2. First sign pattern and its unique peak.** Suppose \(0<\alpha<1\) and set \(b_\alpha=\alpha^{1/(1-\alpha)}\). For \(0\le x\le b_\alpha\), the kernel is positive on \(0\le t<x\) and negative on \(x<t\le1\), because the ratio
\(\alpha(x-t)^{\alpha-1}/(1-t)^\alpha\) increases with \(t\) and its value at \(t=0\) is at least one. Direct integration gives
\[
S_\alpha(x)=\frac{x^\alpha}{\alpha}-\frac1{\alpha(\alpha+1)}+
\frac{2(1-x)^{\alpha+1}}{\alpha(\alpha+1)},\qquad
S_\alpha'(x)=x^{\alpha-1}-\frac2\alpha(1-x)^\alpha.
\]
Write \(h_\alpha(x)=x^{1-\alpha}(1-x)^\alpha\). Its derivative has the sign of \(1-\alpha-x\), so it rises and then falls, with a single interior maximum. Furthermore \(b_\alpha\le e^{-1}<1/2\), by \(\log\alpha\le\alpha-1\), and hence
\(h_\alpha(b_\alpha)=\alpha(1-b_\alpha)^\alpha>\alpha/2\).
There is therefore precisely one \(x_\alpha\in(0,b_\alpha)\) with \(h_\alpha(x_\alpha)=\alpha/2\). The derivative \(S_\alpha'\) changes from positive to negative there. In particular
\(S_\alpha(x_\alpha)>\max\{S_\alpha(0),S_\alpha(b_\alpha)\}\).

**3. The remaining rows cannot dominate.** For \(b_\alpha<x<1\), the kernel has exactly one extra crossing \(t_*(x)\in(0,x)\), negative before \(t_*\) and positive on \((t_*,x)\). Set \(z=1-x\) and \(y=1-t_*\). The crossing identity is
\[
\alpha=(y-z)^{1-\alpha}y^\alpha,
\quad z=y-\alpha^{1/(1-\alpha)}y^{-\alpha/(1-\alpha)},
\quad \frac{dy}{dz}=\frac{1-\alpha}{1-\alpha z/y}\in(0,1).
\]
Integrating the negative region \(t<t_*\) and differentiating at the moving zero (whose boundary term vanishes) yields
\[
S_\alpha'(x)=-(1-z)^{\alpha-1}+\frac2\alpha(y^\alpha-z^\alpha).
\]
The derivative of the right side with respect to \(z\) is strictly negative: its first contribution is \((\alpha-1)(1-z)^{\alpha-2}<0\), and the remainder is \(2(y^{\alpha-1}dy/dz-z^{\alpha-1})<0\), since \(y>z>0\), \(\alpha-1<0\), and \(dy/dz<1\). Thus \(S_\alpha'(x)\) is strictly increasing as \(x\) increases; in particular \(S_\alpha\) is convex on \([b_\alpha,1]\). Therefore its maximum on this interval occurs at one of its endpoints.

The endpoint masses, obtained by direct integration, are
\[
S_\alpha(0)=\frac1{\alpha(\alpha+1)},\qquad
S_\alpha(1)=\frac{2\alpha^{\alpha-1}-1}{\alpha+1}.
\]
For \(\frac12\le\alpha<1\), weighted arithmetic-geometric mean gives
\(\alpha^\alpha\le (1-\alpha)\cdot1+\alpha\cdot\alpha=1-\alpha+\alpha^2\le(1+\alpha)/2\).
Hence \(S_\alpha(1)\le S_\alpha(0)\). Combined with Step 2, the *unique* global maximum occurs at \(x_\alpha\), and the displayed formula for the sharp norm follows. Because \(K_\alpha(x_\alpha,t)\) has one strict sign change (at \(t=x_\alpha\)), equality in the integral triangle inequality forces exactly the asserted unimodular step inputs.

**4. Abel value.** At \(\alpha=1/2\), the stationary equation becomes \(x(1-x)=1/16\). Its unique small root is \((2-\sqrt3)/4\). Substitution in Step 2 and radical simplification give \(S_{1/2}(x_{1/2})=\sqrt6+\sqrt2/3-4/3\), and \(\Gamma(1/2)=\sqrt\pi\).

**5. Exponentially thin transition.** Put \(\alpha=1-\varepsilon\). Since \(h_\alpha\) increases up to \(x=\varepsilon\), its first crossing satisfies \(x_\alpha<\varepsilon\). The stationarity identity gives
\[
x_\alpha^\varepsilon=\frac\alpha2(1-x_\alpha)^{-\alpha}\le
\frac{\alpha^\varepsilon}{2},\qquad
\text{so}\quad x_\alpha\le\alpha2^{-1/\varepsilon}.
\]
Taking logarithms in the same identity, using \(x_\alpha/\varepsilon\to0\), yields
\(\log x_\alpha=(\log\alpha-\log2)/\varepsilon+o(1)\), and hence
\(x_\alpha\sim e^{-1}2^{-1/\varepsilon}\).
To determine the sharp gain, subtract the value at zero from the exact row formula and substitute
\(x_\alpha^\alpha=(2/\alpha)x_\alpha(1-x_\alpha)^\alpha\). Taylor's theorem gives
\[
S_\alpha(x_\alpha)-S_\alpha(0)
=\frac{2(1-\alpha)}{\alpha^2}x_\alpha+O(x_\alpha^2),
\]
uniformly as \(\alpha\uparrow1\). Since \(x_\alpha^2=o((1-\alpha)x_\alpha)\) and \(\Gamma(\alpha)\to1\), the stated asymptotic follows. For \(\alpha=1\), \(K_1(x,t)=t\) if \(t<x\), and \(K_1(x,t)=-(1-t)\) otherwise; thus \(S_1(x)=[x^2+(1-x)^2]/2\), with norm \(1/2\).

## Verification
The included `check.py` (requires Python and `mpmath`) independently evaluates absolute-kernel integrals by a singularity-removing substitution, compares them against the sign-integrated formula at different parameters and evaluation locations, verifies the Abel radical and optimizers, and tests the predicted beyond-all-orders scaling. A replay of the packaged script completed 125 numerical and algebraic assertions. The proof above, not finite numerical sampling, establishes the continuum quantifiers.

## Relationship to prior work
The fractional kernel and its semigroup/space mapping properties belong to classical Riemann–Liouville analysis. Katugampola (arXiv:1010.0742, first posted 2010-10-05), Sections 1–4, studies a generalization and boundedness in weighted Lebesgue spaces; it does not formulate the spatial-mean-centered operator or the sharp endpoint row-sign optimization. Gorenflo–Luchko–Yamamoto (arXiv:1411.7289, first posted 2014-11-26), Sections 1–4, analyze fractional Sobolev \(L^2\) norm equivalences and the Caputo derivative, not the present uniform-norm constant. Set (arXiv:1107.5732, first posted 2011-07-28) develops Ostrowski inequalities for differentiable functions with derivative convexity hypotheses; those conditions do not yield an unrestricted \(L^\infty\)-input norm of \(QI_\alpha\). A published mathematical research note on rank-one-corrected Volterra singular values concerns Hilbert/Schatten spectral majorization, a different operator family and norm objective; it does not imply the sharp fractional \(L^\infty\) result. These are explicit scientific comparisons, not a claim that searching proves historical uniqueness.

## Limitations
The sharp optimization theorem is proved for the natural Abel-to-integer range \(\frac12\le\alpha<1\); the proof does not classify \(0<\alpha<\frac12\) or \(\alpha>1\). The beyond-all-orders asymptotic concerns only \(\alpha\uparrow1\). The available literature review may miss unindexed or inaccessible historical treatments of mean-centering, and independent verification and bibliographic review have not been performed. The numerical script checks finite samples and therefore provides neither exhaustive parameter verification nor a formal proof.

## References
1. U. N. Katugampola, *New Approach To A Generalized Fractional Integral*, arXiv:1010.0742v1 (2010-10-05), https://arxiv.org/abs/1010.0742.
2. R. Gorenflo, Y. Luchko, and M. Yamamoto, *Operator theoretic approach to the Caputo derivative and the fractional diffusion equations*, arXiv:1411.7289v1 (2014-11-26), https://arxiv.org/abs/1411.7289.
3. E. Set, *New inequalities of Ostrowski type for mappings whose derivatives are s-convex in the second sense via fractional integrals*, arXiv:1107.5732v1 (2011-07-28), https://arxiv.org/abs/1107.5732.
4. G. P. Curbera, *Volterra Convolution Operators with Values in Rearrangement Invariant Spaces*, Journal of the London Mathematical Society 60 (1999), 258–268, DOI 10.1112/S0024610799007759 (abstract consulted; full text not inspected).
