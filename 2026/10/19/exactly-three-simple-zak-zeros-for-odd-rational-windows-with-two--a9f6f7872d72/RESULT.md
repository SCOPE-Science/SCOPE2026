# Exactly three simple Zak zeros for odd rational windows with two imaginary pole pairs

## Finding

For **every** pair of real parameters \(a,b>0\), including \(a=b\), define
\[
g_{a,b}(x)=\frac{x}{(x^2+a^2)(x^2+b^2)}
\]
and the unit-period Zak transform
\[
Zg_{a,b}(t,\xi)=\sum_{k\in\mathbb Z}g_{a,b}(t-k)e^{2\pi i k\xi}.
\]
Its complete zero set in the fundamental cell \([0,1)\times[0,1)\) is **exactly**
\[
\boxed{\{(0,0),(0,\tfrac12),(\tfrac12,0)\}.}
\]
All three zeros are nondegenerate as zeros of the real map \((t,\xi)\mapsto(\operatorname{Re}Zg,\operatorname{Im}Zg)\): its real Jacobian determinant is nonzero at each point. In particular, no additional Zak zero appears as either pole varies or as the two pole pairs coalesce.

## Assumptions and scope

The parameters \(a,b\) are arbitrary **positive real numbers**. The rational function is defined even when \(a=b\), where the denominator has repeated factors. The series defining \(Zg\) is absolutely and locally uniformly convergent, since \(g_{a,b}(x)=O(|x|^{-3})\). The Zak transform is periodic in \(\xi\) and quasiperiodic in \(t\), so its zero set is determined by one half-open unit square. The Fourier transform convention is \(\widehat f(\nu)=\int_{\mathbb R}f(x)e^{-2\pi i x\nu}\,dx\). The theorem concerns this unit-period Zak transform, not all dilated lattice Zak transforms or a complete Gabor frame-set determination.

## Proof

**1. Exact Fourier and Zak formulas.** By symmetry we may suppose \(0<a\le b\). First assume \(a<b\), and put \(\alpha=2\pi a\), \(\beta=2\pi b\), \(\theta=2\pi t\). Partial fractions and the Fourier transforms of Cauchy kernels give
\[
\widehat g_{a,b}(\nu)=-\frac{i\pi\operatorname{sgn}(\nu)}{b^2-a^2}\bigl(e^{-\alpha|\nu|}-e^{-\beta|\nu|}\bigr).
\]
Poisson summation (valid through the exponentially decaying transform, with continuity at integer frequencies) consequently yields, for \(0<\xi<1\),
\[
Zg_{a,b}(t,\xi)=-\frac{i\pi e^{i\theta\xi}}{b^2-a^2}\bigl(K_\alpha(\theta,\xi)-K_\beta(\theta,\xi)\bigr),
\]
where the two geometric series of positive and negative Fourier frequencies sum to
\[
K_\lambda(\theta,\xi)=
\frac{\cosh(\lambda(1-\xi))-e^{-i\theta}\cosh(\lambda\xi)}{\cosh\lambda-\cos\theta},\qquad \lambda>0.
\tag{1}
\]
The denominator is strictly positive. For \(a=b\), the continuous divided-difference limit is
\[
Zg_{a,a}(t,\xi)=\frac{i\pi^2}{a}e^{i\theta\xi}
\left.\partial_\lambda K_\lambda(\theta,\xi)\right|_{\lambda=2\pi a}.
\tag{2}
\]
Thus, in the distinct-pole case it suffices to classify zeros of \(K_\alpha-K_\beta\); in the repeated-pole case, zeros of \(\partial_\lambda K_\lambda\). The same cancellation or differentiation makes their boundary limits at \(\xi=0\) valid, although an individual signed geometric series has a convention-dependent zero-frequency term there.

**2. No zeros off the two real-phase fibers.** Suppose \(0<\xi<1\) and \(\sin\theta\ne0\). Write
\[
K_\lambda=R_\lambda-e^{-i\theta}S_\lambda,\quad
R_\lambda=\frac{\cosh(\lambda(1-\xi))}{\cosh\lambda-\cos\theta},\quad
S_\lambda=\frac{\cosh(\lambda\xi)}{\cosh\lambda-\cos\theta}.
\]
A zero of \(K_\alpha-K_\beta\) forces **both** \(R_\alpha=R_\beta\) and \(S_\alpha=S_\beta\), since its imaginary part equals \(\sin\theta(S_\alpha-S_\beta)\). If \(\xi\ne\tfrac12\), this is impossible: the ratio
\[
\frac{R_\lambda}{S_\lambda}=
\frac{\cosh(\lambda(1-\xi))}{\cosh(\lambda\xi)}
\]
is strictly monotone in \(\lambda>0\), with derivative of its logarithm having the sign of \(1-2\xi\). Indeed \(s\mapsto s\tanh(\lambda s)\) is strictly increasing for \(s>0\). If \(\xi=\tfrac12\), the two functions coincide and equal
\[
F_\lambda(\theta)=\frac{\cosh(\lambda/2)}{\cosh\lambda-\cos\theta};
\]
this is strictly decreasing in \(\lambda\), because
\[
\partial_\lambda\log F_\lambda
=\tfrac12\tanh(\lambda/2)-\frac{\sinh\lambda}{\cosh\lambda-\cos\theta}
\le-\tfrac12\tanh(\lambda/2)<0.
\]
The same argument covers a repeated pole: simultaneous vanishing of \(\partial_\lambda R_\lambda\) and \(\partial_\lambda S_\lambda\) would force the derivative of their ratio to vanish when \(\xi\ne\tfrac12\), and \(\partial_\lambda F_\lambda\ne0\) otherwise. Hence no such zero exists.

**3. The fibers \(\theta=0\) and \(\theta=\pi\).** Put \(u=\tfrac12-\xi\), so \(|u|<\tfrac12\) for \(0<\xi<1\). Formula (1) becomes
\[
K_\lambda(0,\xi)=\frac{\sinh(\lambda u)}{\sinh(\lambda/2)},\qquad
K_\lambda(\pi,\xi)=\frac{\cosh(\lambda u)}{\cosh(\lambda/2)}.
\tag{3}
\]
For \(0<|u|<\tfrac12\), the absolute value of the first expression is strictly decreasing in \(\lambda>0\), since \(s\mapsto s\coth(\lambda s)\) is strictly increasing on positive \(s\). The second expression is strictly decreasing for every \(|u|<\tfrac12\), since \(s\mapsto s\tanh(\lambda s)\) is strictly increasing. Thus \(K_\alpha-K_\beta\), and also \(\partial_\lambda K_\lambda\), vanish on these fibers precisely when \(\theta=0\) and \(u=0\). This is the zero \((t,\xi)=(0,\tfrac12)\).

**4. The frequency boundary.** For \(\xi\downarrow0\), formula (1) gives
\[
K_\lambda(\theta,0^+)=1+\frac{i\sin\theta}{\cosh\lambda-\cos\theta}.
\]
The constant term cancels in \(K_\alpha-K_\beta\), and its derivative vanishes in the repeated-pole case. Since \(\lambda\mapsto(\cosh\lambda-\cos\theta)^{-1}\) is strictly decreasing, the Zak transform has boundary zeros precisely when \(\sin\theta=0\). These give \((0,0)\) and \((\tfrac12,0)\). Quasiperiodicity and the half-open convention complete the zero-set classification.

**5. Nondegeneracy of all zeros.** Remove the everywhere nonzero prefactor from the Zak representation. At each of the three zeros, the \(\theta\)-derivative of the remaining function is purely imaginary and nonzero, while the \(\xi\)-derivative is real and nonzero. For \((0,0)\) and \((\pi,0)\), the former follow from the strictly varying reciprocals \((\cosh\lambda-1)^{-1}\) and \((\cosh\lambda+1)^{-1}\); the latter follow from strict increase of \(\lambda\coth(\lambda/2)\) and \(\lambda\tanh(\lambda/2)\). At \((0,\tfrac12)\), the imaginary derivative uses strict decrease of \(F_\lambda(0)\), and the real derivative uses strict decrease of \(\lambda/\sinh(\lambda/2)\). Strict nonvanishing continues to the coincident-pole case by differentiation with respect to \(\lambda\). The real Jacobian is therefore nonsingular at every zero. \(\square\)

## Verification

The standalone script `check_zak.py` needs only Python 3's standard library. Running `python3 check_zak.py` performs direct truncated-Zak versus closed-form comparisons for distinct and repeated poles, checks that the three prescribed points vanish and have nonzero numerical real Jacobians, and tests additional off-zero grid points. The supplied execution returned `VERIFY_OK 3185 formula, nondegenerate-zero, and grid checks; standard library only`. These numerical checks validate formulas and signs; the exhaustive all-parameter zero classification is analytic, **not** inferred from a finite grid.

## Relationship to prior work

Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568 (first public August 11, 2026), derives a Zak-polynomial representation and rational-density frame results for the fixed-pole window \(a=1\), \(b=2\) in the accessible full text. The revised public abstract also describes a larger **discrete integer-pole** family. Neither the inspected full-text theorems nor the broader abstract supplies this continuous two-parameter three-zero classification or its repeated-pole transversality. Faulhuber (2025) gives the three parity-forced points for odd first-Hermite windows and studies high-density non-frame configurations; the different Gaussian-weighted window does not imply this rational-window classification. Kloos (arXiv:1411.1539) establishes a one-Zak-zero theorem for *totally positive* windows, which are nonnegative rather than the sign-changing odd windows studied here. General parity-based non-frame obstructions do not in themselves rule out additional zeros. The contribution is the parameter-uniform **absence of additional zeros** and their simplicity, not the parity-forced zeros alone.

## Limitations

Only the unit-period Zak transform is classified: dilated periods and complete multi-window or rational-density Gabor frame sets are not addressed. Nondegenerate zeros alone do not yield a global stability bound or decide every Gabor frame property. The literature comparison is bounded; historical priority has not been independently certified, including against hard-to-access older discussions of Zak transforms of rational windows. No independent mathematical audit has been performed.

## References

- R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568 (first public August 11, 2026), https://arxiv.org/abs/2608.10568.
- M. Faulhuber, *Gabor systems with Hermite functions of order N and oversampling greater than N+1 which are not frames*, Sampling Theory, Signal Processing, and Data Analysis **23**, 22 (2025), https://doi.org/10.1007/s43670-025-00112-5.
- T. Kloos, *Zeros of the Zak transform of totally positive functions*, arXiv:1411.1539 (2014), https://arxiv.org/html/1411.1539v1.
- A. Ulanovskii and I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450 (2026), https://arxiv.org/abs/2606.31450.
