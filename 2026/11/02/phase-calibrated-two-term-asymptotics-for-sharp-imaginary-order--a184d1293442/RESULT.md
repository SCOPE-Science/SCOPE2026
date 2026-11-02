# Phase-calibrated two-term asymptotics for sharp imaginary-order Macdonald Turán minima

## Finding

Fix a real order \(\nu>0\), let \(f_\nu(x)=K_{i\nu}(x)\), and write its positive zeros in decreasing order \(\kappa_{\nu,1}>\kappa_{\nu,2}>\cdots>0\). On each nodal interval define

\[
T_\nu(x)=\frac{K_{i\nu-1}(x)K_{i\nu+1}(x)}{K_{i\nu}(x)^2}-1
=\frac{\nu^2+\bigl(x f_\nu'(x)/f_\nu(x)\bigr)^2}{x^2}-1.
\]

The unique minimizer of \(T_\nu\) in \((\kappa_{\nu,n+1},\kappa_{\nu,n})\) is denoted \(\alpha_{\nu,n}\), and its sharp minimum is \(\tau_{\nu,n}=T_\nu(\alpha_{\nu,n})\). Existence and uniqueness for all \(n\ge1\) are due to Aktaş–Baricz [1, Theorem 5.4]. Define the *continuous* gamma phase \(\eta_\nu=\operatorname{Im}\log\Gamma(1+i\nu)\), with the logarithm chosen continuously from \(\eta_0=0\), and put

\[
A=1+\nu^2,\quad
\theta_\nu=\arctan\nu,\quad
q_{\nu,n}=2\exp\left(\frac{\eta_\nu-n\pi-\theta_\nu}{\nu}\right).
\]

Then, as \(n\to\infty\) with \(\nu>0\) fixed, the following two **phase-calibrated** expansions hold:

\[
\boxed{\alpha_{\nu,n}=q_{\nu,n}\left[1+\frac{\nu^2+9}{4(1+\nu^2)^2}\,q_{\nu,n}^2+O_\nu(q_{\nu,n}^4)\right],}
\]

\[
\boxed{\tau_{\nu,n}=\frac{1+\nu^2}{q_{\nu,n}^2}-\frac32-\frac{2}{1+\nu^2}+O_\nu(q_{\nu,n}^2).}
\]

In particular, the absolute additive offset of the *optimal nodal constants*, after subtraction of their exponentially increasing calibrated leading term, converges to \(-3/2-2/(1+\nu^2)\). This is stronger than the previously established ratios of consecutive minimizers/minima and the product limit \(\alpha_{\nu,n}^2\tau_{\nu,n}\to1+\nu^2\).

## Assumptions and scope

The order \(\nu\) is fixed and strictly positive, \(x\) is real and positive, \(K\) and \(I\) are the usual modified Bessel functions, and \(n\) counts positive zeros of \(K_{i\nu}\) **from the largest toward zero**. The logarithm of the gamma function must be followed continuously along the positive imaginary-order ray; a principal argument can shift the index by an integer, invalidating the stated calibration. The constants implied by \(O_\nu\) may depend on fixed \(\nu\). No uniformity as \(\nu\downarrow0\) or \(\nu\to\infty\) is claimed.

## Proof

**1. Nodal indexing and the phase.** For \(x>0\), set \(w(x)=I_{i\nu}(x)\). Its conjugate \(\overline{w(x)}=I_{-i\nu}(x)\) satisfies the same real modified Bessel equation; the Wronskian, evaluated using the Frobenius series at the origin, yields

\[
x\,\operatorname{Im}(\overline{w(x)}w'(x))=\frac{\nu}{|\Gamma(1+i\nu)|^2}>0.
\]

Hence \(w(x)\ne0\) for all \(x>0\), and its continuously chosen argument \(\psi(x)\), normalized by \(\psi(x)\to0\) as \(x\to+\infty\), increases strictly with \(x\). The identity

\[
K_{i\nu}(x)=-\frac{\pi}{\sinh(\pi\nu)}\operatorname{Im}I_{i\nu}(x)
\]

implies that its \(n\)-th largest positive zero is exactly the point where \(\psi=-n\pi\). To exclude an unrecorded integer phase shift, note that the small-argument Frobenius series gives \(\psi=\nu\log(x/2)-\eta_\nu+O_\nu(x^2)\) modulo \(2\pi\). The integer offset depends continuously on \(\nu>0\) and vanishes as \(\nu\downarrow0\) at each fixed \(x>0\), because \(I_{i\nu}(x)\to I_0(x)>0\) and \(\eta_\nu\to0\). Thus the displayed phase is valid on the stated continuous branch with no offset. In particular, writing \(s=\nu\log(2/x)+\eta_\nu\), the interval \((\kappa_{\nu,n+1},\kappa_{\nu,n})\) has \(s\) between \(n\pi+O_\nu(x^2)\) and \((n+1)\pi+O_\nu(x^2)\).

**2. Uniform small-argument expansion and its logarithmic derivative.** The exact convergent \(I\)-series and the gamma reflection formula give

\[
K_{i\nu}(x)=\frac{|\Gamma(1+i\nu)|}{\nu}\left[\sin s+\frac{x^2}{4A}(\sin s+\nu\cos s)+O_\nu(x^4)\right],
\]

with the error and its logarithmic \(x\)-derivative uniformly bounded on oscillatory phases when the *undivided* expression is used. More precisely, on any closed subinterval strictly inside \((n\pi,(n+1)\pi)\), and uniformly in integer \(n\), division yields

\[
z(x):=x\frac{K'_{i\nu}(x)}{K_{i\nu}(x)}
=-\nu\cot s+x^2\left[\frac{\nu^2\csc^2s}{4A}+\frac{1+\nu\cot s}{2A}\right]+O_\nu(x^4).
\]

The expansion is termwise differentiable because the underlying series converges absolutely and analytically in \(x^2\), with bounded coefficients for fixed \(\nu>0\).

**3. Critical-point equation.** The modified Bessel differential equation gives the exact Riccati identity \(z'(x)=-xT_\nu(x)\) and, on each nodal interval,

\[
-\frac{x}{2}T_\nu'(x)=1+(1+z(x))T_\nu(x).
\]

At the unique minimum supplied by [1], the first derivative vanishes, so

\[
z(\alpha)=-1-\frac1\tau,\qquad
\alpha^2(\tau+1)=\nu^2+(1+1/\tau)^2.
\]

Since \(\alpha\to0\) and \(z(\alpha)\to-1\) by [1, Remark 5.2], the second equation gives

\[
\tau=\frac A{\alpha^2}+\frac2A-1+O_\nu(\alpha^2),\qquad
z(\alpha)=-1-\frac{\alpha^2}{A}+O_\nu(\alpha^4).
\]

**4. Exact phase offset and the next term.** In the \(n\)-th nodal interval, \(z(\alpha)\to-1\) forces the interior phase to satisfy \(s(\alpha)-n\pi\to\arctan\nu=\theta_\nu\); this is the unique solution of \(-\nu\cot s=-1\) in that interval. Put \(q=q_{\nu,n}\). Then \(s(q)=n\pi+\theta_\nu\), and a first-order implicit expansion yields \(\alpha=q(1+cq^2+O_\nu(q^4))\) with unknown \(c\). At the reference phase \(s(q)\), \(\cot s=1/\nu\), \(\csc^2s=A/\nu^2\), and the entire \(x^2\)-coefficient in Step 2 is exactly \(1/4+1/A\). The phase shift caused by \(\alpha/q=1+cq^2+\cdots\) is \(-\nu cq^2+O_\nu(q^4)\), while the derivative of \(-\nu\cot s\) at \(s(q)\) equals \(A/\nu\). Consequently

\[
z(\alpha)=-1+q^2\left(-Ac+\frac14+\frac1A\right)+O_\nu(q^4).
\]

Comparison with the critical-point equation \(z(\alpha)=-1-q^2/A+O_\nu(q^4)\) shows

\[
c=\frac{A+8}{4A^2}=\frac{\nu^2+9}{4(1+\nu^2)^2}.
\]

The implicit derivative \(A/\nu>0\) is nonzero, so the Taylor expansion and its remainder follow by the analytic implicit-function theorem, uniformly for sufficiently small \(q\) at fixed \(\nu\). Substitution into the exact critical relation finally gives

\[
\begin{aligned}
\tau&=\frac{A}{q^2}-2Ac+\frac2A-1+O_\nu(q^2)\\
&=\frac{A}{q^2}-\frac32-\frac2A+O_\nu(q^2),
\end{aligned}
\]

as claimed. Every limit is an \(n\to\infty\) statement with \(\nu\) held fixed. \(\square\)

## Verification

The accompanying `check.py` directly evaluates \(K_{i\nu}\) and the Riccati critical equation at several fixed orders and indices using high-precision arithmetic. It checks the exact critical equation, that the calibrated-position error is fourth order relative to \(q\), and that the sharp-minimum error is second order in \(q\). The numerical experiments do not prove the expansion for all \(n\) or for all real \(\nu\); Steps 1–4 supply that proof. Reproduce with `python check.py` after installing Python's `mpmath` package. The error thresholds in the script are generously chosen consistency checks, not certified interval error bounds.

## Relationship to prior work

Aktaş and Baricz [1, §5, Theorem 5.4] prove existence, uniqueness, monotonicity, and divergence of the same optimal nodal constants. Their Remark 5.2 proves asymptotic *ratios* of the minimizing arguments and minima, and \(\alpha_{\nu,n}^2\tau_{\nu,n}\to1+\nu^2\). The present claim supplies an index-calibrated gamma-phase prefactor, a nonzero relative location correction, and a finite **additive** correction to the exponentially large sharp constants; none follows by substituting into their ratio limits alone. The original zero-location literature [2–3] addresses positive \(x\)-zeros or \(\nu\)-zeros, not these nodal sharp minima. The small-argument expansion and gamma phase are classical [4]; the new step is their interaction with the exact critical-point equation.

## Limitations

The theorem does not claim new existence/uniqueness of nodal minima, nor a new zero theorem. It requires the precise normalization in the definition of \(T_\nu\) and the continuous gamma logarithm. It is pointwise in each fixed positive order, with no order-uniform error. It does not yield exact closed finite-index minima. An equivalently calibrated expansion in older incompletely indexed work cannot be definitively excluded by literature searching; external mathematical validation has not been performed.

## References

[1] I. Aktaş and Á. Baricz, *Turán type inequalities for oscillatory special functions*, arXiv:2609.39008, initial public submission 2026-09-30, §5, Theorem 5.4 and Remark 5.2. https://arxiv.org/abs/2609.39008

[2] E. M. Ferreira and J. Sesma, *Zeros of the Macdonald function of complex order*, arXiv:math/0607471 (2006). https://arxiv.org/abs/math/0607471

[3] R. B. Paris, *On the \(\nu\)-zeros of the Bessel functions of purely imaginary order*, arXiv:2204.09306 (2022). https://arxiv.org/abs/2204.09306

[4] NIST Digital Library of Mathematical Functions, §§10.24, 10.25, 10.45 (gamma phase, modified Bessel series and small-argument expansions). https://dlmf.nist.gov/10.45
