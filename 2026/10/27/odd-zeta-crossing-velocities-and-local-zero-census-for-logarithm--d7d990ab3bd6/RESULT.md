# Odd-zeta velocities of boundary zeros of logarithmic Bergman kernels

## Finding

For \(s>0\), let the weighted analytic Hilbert space on the unit disk use normalized planar area and weight \(w_s(z)=(-\log|z|^2)^{s-1}/\Gamma(s)\). Its kernel has the form \(K_s(z,w)=P_s(z\overline w)\), with
\[
P_s(t)=\sum_{n\ge0}(n+1)^s t^n=\operatorname{Li}_{-s}(t)/t,\qquad P_s(0)=1.
\]
For each integer \(m\ge1\), the zero at \(t=-1\) for \(s=2m\) has a unique local real-analytic branch \(t_m(s)\). Its velocity in the scalar kernel variable is
\[
\boxed{t_m'(2m)=v_m=\frac{\pi^2}{2m+1}\frac{2^{2m+1}-1}{2^{2m+2}-1}\frac{\zeta(2m+1)}{\zeta(2m+2)}>0.}
\]
Thus \(t_m(s)=-1+v_m(s-2m)+O_m((s-2m)^2)\). In particular \(v_1=14\zeta(3)/\pi^2\) and \(v_m\sim \pi^2/[2(2m+1)]\). The velocity quantifies how rapidly the branch becomes an actual kernel zero: along the branch just inside the disk, choosing equal moduli \(|z|=|w|=\sqrt{-t_m(s)}\) and opposite phases, their moduli drop below one at initial speed \(v_m/2\).

For context, the classical negative-real zero theorem of Jurkat and Peyerimhoff [1] gives simplicity and location in the slit plane for this real-power series. In an \(m\)-dependent neighborhood of \(2m\), the integer Eulerian count together with this location theorem and the direction of the crossing gives \(m-1\) zeros in the open disk for \(s\le2m\) and \(m\) for \(s>2m\). The contribution here is the explicit crossing velocity, not a new general reality, simplicity, or zero-enumeration theorem.

## Proof of the velocity

In polar coordinates \(\|z^n\|_s^2=\Gamma(s)^{-1}\int_0^1u^n(-\log u)^{s-1}du=(n+1)^{-s}\). Angular orthogonality and summation of the Taylor coefficients give the kernel series. Dependence on \((s,t)\) is jointly analytic near \((2m,-1)\): choose an integer \(N>2m\), and apply \((1+t\partial_t)^N\) to
\[
\frac{1}{\Gamma(N-s)}\int_0^\infty \frac{x^{N-s-1}e^{-x}}{1-te^{-x}}\,dx.
\]
For \(\operatorname{Re}s<N\) and \(t\) in compact subsets of \(\mathbb C\setminus[1,\infty)\), the integral is locally normally convergent; its coefficients on the disk are \((n+1)^{s-N}\). Hence this representation continues the kernel series on that slit plane and justifies local analytic differentiation.

Let \(\eta(q)=(1-2^{1-q})\zeta(q)\). The continued value at \(t=-1\) is \(P_s(-1)=\eta(-s)\) (the alternating Dirichlet series identity, continued in the order). Thus \(P_{2m}(-1)=0\) by the trivial zero of \(\zeta\). The identity \(t\partial_tP_s=P_{s+1}-P_s\) gives at \((2m,-1)\)
\[
\partial_tP_s=-\eta(-2m-1)\ne0,\qquad \partial_sP_s=-\eta'(-2m).
\]
The implicit-function theorem gives the unique branch, real for real \(s\) by conjugation, with derivative \(-\eta'(-2m)/\eta(-2m-1)\). The zeta functional equation gives
\[
\zeta'(-2m)=\frac{(-1)^m(2m)!}{2(2\pi)^{2m}}\zeta(2m+1),\qquad
\zeta(-2m-1)=\frac{(-1)^{m+1}(2m+1)!}{2^{2m+1}\pi^{2m+2}}\zeta(2m+2).
\]
Since the derivative of the eta prefactor multiplies a zero at \(-2m\), its contribution vanishes there. The ratio of the remaining eta prefactors is \((2^{2m+1}-1)/(2^{2m+2}-1)\). These identities give the displayed velocity including its sign. Substitution of \(m=1\) and \(\zeta(4)=\pi^4/90\) gives \(v_1\); the zeta ratio tends to one and the power-of-two ratio to one half, giving the asymptotic.

## Local counting consequence and scope

For positive integer \(n\), \(P_n(t)=A_n(t)/(1-t)^{n+1}\), where the degree \(n-1\) Eulerian numerator has simple negative roots and is reciprocal [2]. Thus at \(n=2m\), the simple root at \(-1\) is the unpaired reciprocal root, and exactly \(m-1\) roots lie in \((-1,0)\). For real \(s>0\), [1, Theorem 4 and §4(i)] applies to the series with coefficients \(n^s\) and zero shift. Its zero at the origin is removed by dividing by \(t\); every zero of \(P_s\) in the open disk must be negative real. On the compact interval \([-1,0]\) the family converges uniformly to \(P_{2m}\) as \(s\to2m\). Small disjoint complex disks around its simple zeros each contain a unique continued root, and the rest of \([-1,0]\) is uniformly zero-free. Consequently the \(m-1\) interior branches persist, and the remaining branch crosses inward through \(-1\) as \(s\) increases. There is no assertion of an \(m\)-uniform neighborhood or of an exact disk count for all parameters. A scalar zero with \(|t|<1\) is realized by choosing \(z,w\) with \(z\overline w=t\); it is not a zero of every fixed kernel section.

The accompanying `checker.py` and `requirements.txt` give finite checks of the radial moments, Eulerian counts, and agreement of the two velocity expressions and the local numerical branches. The general statements follow from the analytic derivation and the specified prior location theorem, not from a finite range of sample parameters.

## References

1. W. B. Jurkat and A. Peyerimhoff, *On power series with negative zeros*, Tohoku Math. J. **24** (1972), 207–221, Theorem 4 and §4(i), [doi:10.2748/tmj/1178241531](https://doi.org/10.2748/tmj/1178241531).
2. A. J. Durán, *Asymptotic for the rightmost zeros of Bell and Eulerian polynomials*, [arXiv:2404.03249](https://arxiv.org/abs/2404.03249), Eulerian roots and reciprocity.
3. NIST Digital Library of Mathematical Functions, [Chapter 25](https://dlmf.nist.gov/25), zeta and polylogarithm identities.
