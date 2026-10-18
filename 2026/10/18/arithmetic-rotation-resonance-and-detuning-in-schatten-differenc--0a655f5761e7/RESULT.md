# Arithmetic rotation resonance and detuning in Schatten differences of Dirichlet composition–differentiation operators

## Finding

Let \(\alpha>-1\), let \(m\ge1\) be an integer, and let \(p>0\). On the coefficient-normalized weighted Dirichlet Hilbert space \(\mathcal D_\alpha\), define
\[
D_{t,\theta}^{(m)}f(z)=f^{(m)}(e^{-t+i\theta}z),\qquad
A_{t,\theta}^{(m)}=D_{t,0}^{(m)}-D_{t,\theta}^{(m)},\qquad t>0.
\]
Each difference belongs to every Schatten class, including the quasi-normed classes with \(0<p<1\). Its singular values, as an unordered multiset with zero values allowed, are exactly
\[
\sigma_j(t,\theta)=\frac{(j+m)!}{j!}\,e^{-tj}
\left(\frac{j+1}{j+m+1}\right)^{(1-\alpha)/2}
|1-e^{ij\theta}|,\qquad j=0,1,2,\ldots.
\tag{1}
\]

Fix coprime integers \(a,q\), with \(q\ge1\) and \(0\le a<q\), and fix a real \(\omega\). If
\[
\theta_t=\frac{2\pi a}{q}+\omega t+o(t),\qquad t\downarrow0,
\]
then the **exact resonance profile** is
\[
\boxed{\lim_{t\downarrow0}t^{mp+1}
\|A_{t,\theta_t}^{(m)}\|_{\mathcal S_p}^{p}
=\frac1q\sum_{s=0}^{q-1}\int_0^\infty
x^{mp}e^{-px}\left|1-e^{i(2\pi as/q+\omega x)}\right|^p\,dx.}
\tag{2}
\]
If instead \(\theta_t\to\theta_0\) with \(\theta_0/(2\pi)\) irrational, then
\[
\boxed{\lim_{t\downarrow0}t^{mp+1}
\|A_{t,\theta_t}^{(m)}\|_{\mathcal S_p}^{p}
=\frac{\Gamma(mp+1)}{p^{mp+1}}
\frac{2^p\Gamma((p+1)/2)}{\sqrt\pi\Gamma(1+p/2)}.}
\tag{3}
\]
The same limit (3) holds for \(\theta_t=2\pi a/q+\delta_t\), provided \(\delta_t\to0\) and \(|\delta_t|/t\to\infty\). Thus the rational-resonance boundary layer has angular width of order \(t\), and the leading profiles are independent of \(\alpha\).

As one explicit nonmonotone transition, when \(m=1\), \(p=4\), and the resonant angle is \(\pi\), the right-hand side of (2) equals
\[
F(\omega)=\Gamma(5)\left(\frac6{4^5}+2\operatorname{Re}(4-2i\omega)^{-5}\right).
\tag{4}
\]
Its resonant value is \(F(0)=3/16\), its large-detuning value is \(\lim_{|\omega|\to\infty}F(\omega)=9/64\), and \(F(3/2)<9/64\). This provides a strict dip below both endpoint constants in the normalized Schatten-fourth difference.

## Assumptions and scope

The space is defined for all \(\alpha>-1\) by
\[
\mathcal D_\alpha=\left\{f(z)=\sum_{k\ge0}c_kz^k:
\|f\|_\alpha^2=\sum_{k\ge0}(k+1)^{1-\alpha}|c_k|^2<\infty\right\}.
\]
The analytic variable ranges over the open unit disc. Differentiation is with respect to \(z\) before composition; in particular, \(D_{t,\theta}^{(m)}\) means \(f^{(m)}\) evaluated at the contracted argument, not the derivative of \(f(e^{-t+i\theta}z)\). The Schatten quasi-norm convention for every \(p>0\) is \(\|A\|_{\mathcal S_p}^p=\sum_j s_j(A)^p\). The limits keep \(\alpha,m,p\) fixed, and allow the angle to depend on \(t\).

## Proof

**Step 1: an exact weighted-shift singular spectrum.** The vectors \(e_k(z)=(k+1)^{(\alpha-1)/2}z^k\) form an orthonormal basis. For every \(j\ge0\), differentiation and the phase shift give
\[
A_{t,\theta}^{(m)}e_{j+m}=
\frac{(j+m)!}{j!}\,e^{-tj}
\left(\frac{j+1}{j+m+1}\right)^{(1-\alpha)/2}
(1-e^{ij\theta})e_j.
\]
Vectors of degree below \(m\) lie in the kernel, and the displayed outputs have mutually orthogonal target directions. Therefore (1) is the complete singular spectrum. The coefficients grow at most polynomially before the factor \(e^{-tj}\), so the operator is compact and belongs to \(\mathcal S_p\) for every \(p>0\).

**Step 2: a uniform scaling reduction.** Write
\[
h(x)=x^{mp}e^{-px},\qquad g(u)=|1-e^{iu}|^p.
\]
For \(j\to\infty\), the non-exponential scalar coefficient in (1) equals \(j^m(1+O((j+1)^{-1}))\), with a constant depending only on the fixed parameters. The phase factor is bounded by \(2^p\). Split the sum in (1) into \(tj<\varepsilon\), \(\varepsilon\le tj\le R\), and \(tj>R\). On the middle portion the rescaled coefficient converges uniformly to \((tj)^m\); near zero, the rescaled sum is bounded by a constant times \(\varepsilon^{mp+1}+o(1)\), and the tail is controlled by the integrable exponential envelope. Taking \(t\downarrow0\), then \(\varepsilon\downarrow0\) and \(R\uparrow\infty\), proves the **uniform-in-angle** statement
\[
\sup_{\theta\in\mathbb R}\left|
 t^{mp+1}\|A_{t,\theta}^{(m)}\|_{\mathcal S_p}^p
-t\sum_{j\ge0}h(tj)g(j\theta)\right|\longrightarrow0.
\tag{5}
\]
This argument does not use convexity of the Schatten quasi-norm, and hence includes \(0<p<1\).

**Step 3: rational resonance and finite detuning.** For \(\theta_t=2\pi a/q+\omega t+o(t)\), write \(j=q\ell+s\) with \(0\le s<q\). On compact ranges of \(x=tj\), one has \(j\theta_t=2\pi as/q+\omega x+o(1)\) modulo \(2\pi\), uniformly along the relevant indices. The mesh in \(x\) on each residue class is \(qt\). Each of the \(q\) sums in (5), multiplied by \(t\), converges to \(q^{-1}\) times the corresponding integral. The bound \(g\le2^p\) and the integrability of \(h\) permit removal of the compact-range restriction. This yields (2).

**Step 4: irrational and fast-detuning profiles.** The continuous periodic function \(g\) can be approximated uniformly by trigonometric polynomials, for any \(p>0\). The function \(h\) is integrable and has finite total variation on \([0,\infty)\), since \(mp>0\). Abel summation and the bound for geometric partial sums give, for each integer \(k\ne0\) and \(e^{ik\theta}\ne1\),
\[
\left|t\sum_{j\ge0}h(tj)e^{ikj\theta}\right|
\le\frac{C_{m,p}t}{|1-e^{ik\theta}|}.
\tag{6}
\]
If \(\theta_t\to\theta_0\) with irrational \(\theta_0/(2\pi)\), the denominator in (6) stays bounded away from zero for every fixed nonzero Fourier mode. All those modes vanish in the limit, while the constant mode contributes \(\int_0^\infty h(x)dx=\Gamma(mp+1)/p^{mp+1}\). If \(\theta_t=2\pi a/q+\delta_t\) with \(\delta_t\to0\) and \(|\delta_t|/t\to\infty\), then the modes with \(q\nmid k\) again have nonzero limiting denominators; for each fixed \(k\) divisible by \(q\), the denominator has order \(|\delta_t|\), and (6) is \(O(t/|\delta_t|)=o(1)\). Uniform trigonometric approximation completes both cases. Finally, beta integration gives
\[
\frac1{2\pi}\int_0^{2\pi}|1-e^{iu}|^pdu
=\frac{2^p\Gamma((p+1)/2)}{\sqrt\pi\Gamma(1+p/2)},
\]
proving (3).

**Step 5: strict crossover dip.** For \(p=4\),
\(g(u)=6-8\cos u+2\cos(2u)\). Averaging \(g(\pi s+\omega x)\) over the two residue classes gives \(6+2\cos(2\omega x)\). The Laplace-gamma identity \(\int_0^\infty x^4e^{-zx}dx=\Gamma(5)z^{-5}\), valid for \(\operatorname{Re}z>0\), gives (4). At \(\omega=3/2\),
\[
F(3/2)=\frac9{64}-\frac{149568}{9765625}<\frac9{64}<\frac3{16},
\]
so the dip is rigorous rather than an artifact of numerical sampling.

## Verification

The exact matrix coefficients in Step 1, the scaling exponent, and the finite-residue Riemann sums can be reproduced from the formulas above. The included standalone script `checks/resonance_check.py` (Python standard library only) compares direct normalized sums with midpoint quadrature profiles for five independent parameter sets, including a quasi-norm exponent below one, and checks the quartic rational/irrational constants and the explicit crossover formula. Its numerical bounds are diagnostic; the infinite-dimensional assertions follow from Steps 1–5.

## Relationship to prior work

Barik, Sen, and Paul [1] introduced the weighted Dirichlet composition–differentiation setting, proved boundedness, compactness and Hilbert–Schmidt criteria, and studied the norm of an individual contracted derivative in their Section 7. Those theorems do not determine the Schatten quasi-norm of a **difference** of rotated contractions, its rational/irrational boundary law, or an angular detuning profile. Hu and Yang [2] give Schatten-membership tests for differences of weighted **composition** operators on weighted Bergman spaces over a ball. They do not include differentiation, the present coefficient Hilbert spaces, or the quantitative limit constants. The present proof uses a direct weighted-shift diagonalization and residue/Fourier analysis rather than relying on an asserted implication from either paper.

## Limitations

The theorem addresses the linear inducing maps \(z\mapsto e^{-t+i\theta}z\), identical derivative order on both sides, and the exact coefficient normalization displayed above; it does not cover nonlinear symbols or general multiplier weights. It gives leading asymptotics of Schatten-power sums, not an asymptotic formula for individual ordered singular values or uniformity in a changing exponent. The comparisons with available primary literature and indexed research summaries support a bounded originality assessment, not a claim that all possible unindexed or inaccessible results have been excluded.

## References

[1] S. Barik, A. Sen, and K. Paul, *Weighted Composition-differentiation operators on weighted Dirichlet spaces*, arXiv:2605.00213, first public version April 30, 2026, revised October 7, 2026, particularly Sections 2, 5, 7, and 8. https://arxiv.org/abs/2605.00213

[2] X. Hu and Z. Yang, *Essential norm and Schatten class difference of weighted composition operators over the ball*, arXiv:2507.19745, first public version July 26, 2025, particularly Theorem 1.2 and Section 4. https://arxiv.org/abs/2507.19745
