# Optimal shifted cyclic certificates for robust Chebyshev interpolation

## Statement

Let \(C>0\), \(0\le \rho<1\), and
\[
H=\frac{C}{1-\rho}.
\]
Let \(\epsilon_{\mathrm{Ch}}(C,\rho)\) denote the optimal robust-obstruction parameter on the full Chebyshev--Lobatto grids in the sense of Yang, arXiv:2609.14769.

For an even integer \(k\ge2\) and a phase \(a\in(0,1)\), define
\[
w_j^{(a)}
=
\frac{(-1)^j\sin(\pi a)}
{2k\sin(\pi(a-j)/k)},
\qquad 0\le j<2k,
\]
and put
\[
W_k(a)=\sum_{j=0}^{2k-1}|w_j^{(a)}|,
\qquad
M_k(a)=\max_{0\le j<2k}|w_j^{(a)}|.
\]
If
\[
E_{k,a}(H)
=
\min\left\{
\frac1k,\,
\frac{(W_k(a)-H)_+}{2k(H+1)M_k(a)}
\right\},
\]
then
\[
\boxed{\epsilon_{\mathrm{Ch}}(C,\rho)\ge
\sup_{\substack{k\ge2\\ k\ {\rm even}}}E_{k,a}(H)}
\]
for every fixed \(a\in(0,1)\).

The shifted weights have the exact identities
\[
W_k(a)
=
\frac{\sin(\pi a)}{k}
\left[
\csc\frac{\pi a}{k}
+
\sum_{r=1}^{k-1}
\csc\frac{\pi(r-a)}{k}
\right],
\]
and, with \(\delta_a=\min(a,1-a)\),
\[
M_k(a)=
\frac{\sin(\pi a)}
{2k\sin(\pi\delta_a/k)}.
\]
As \(k\to\infty\),
\[
W_k(a)=A(a)\log k+B(a)+o(1),
\]
where
\[
A(a)=\frac{2\sin(\pi a)}{\pi},
\]
\[
B(a)=
\frac{\sin(\pi a)}{\pi}
\left[
-\psi(a)-\psi(1-a)+2\log\frac2\pi
\right],
\]
and \(\psi\) is the digamma function. Also
\[
M_k(a)\longrightarrow
M(a)=\frac{\sin(\pi a)}{2\pi\delta_a}.
\]

Consequently, for every fixed \(a\in(0,1)\),
\[
\boxed{
\sup_{\substack{k\ge2\\k\ {\rm even}}}E_{k,a}(H)
=
\bigl(C(a)+o(1)\bigr)
H^{-1}e^{-\lambda(a)H}
}
\qquad(H\to\infty),
\]
with
\[
\lambda(a)=\frac{\pi}{2\sin(\pi a)}
\]
and
\[
C(a)=
\frac{4\delta_a}{\pi e}
\exp\left(
-\frac{\psi(a)+\psi(1-a)}2
\right).
\]

The exponent \(\lambda(a)\) is uniquely minimized at
\[
a=\frac12.
\]
Thus the half-period evaluation used by Yang is the unique fixed phase in this shifted two-point cyclic family that attains the optimal Chebyshev exponential coefficient \(\pi/2\).

At \(a=1/2\),
\[
W_k\!\left(\frac12\right)
=
\frac1k\sum_{j=0}^{k-1}
\csc\frac{\pi(j+1/2)}k
=
\frac2\pi
\left(
\log k+\gamma+\log\frac8\pi
\right)
+o(1),
\]
so
\[
\boxed{
\epsilon_{\mathrm{Ch}}(C,\rho)
\ge
\left(
\frac{8e^{\gamma-1}}{\pi}+o(1)
\right)
\frac{e^{-\pi H/2}}{H}.
}
\]
Numerically,
\[
\frac{8e^{\gamma-1}}{\pi}=1.668503840095\ldots.
\]
An asymptotically optimizing even period satisfies
\[
\boxed{
k\sim
\frac{\pi e^{1-\gamma}}8\,e^{\pi H/2}.
}
\]

This improves the explicit leading coefficient in Yang's published cyclic lower bound
\[
\epsilon_{\mathrm{Ch}}(C,\rho)
\ge
\frac{e^{-\pi/2}}{4(H+1)}e^{-\pi H/2}
\]
by an asymptotic factor
\[
\frac{8e^{\gamma-1}/\pi}{e^{-\pi/2}/4}
=
\frac{32}{\pi}e^{\gamma-1+\pi/2}
=
32.105\ldots.
\]

## Proof

Let \(\mathcal T_k\) be the real trigonometric polynomials of period \(2k\) with frequencies \(\ell\pi/k\), \(|\ell|\le k\). Yang's cardinal kernel is
\[
L_k(t)
=
\frac{\sin(\pi t)}{2k}
\cot\frac{\pi t}{2k},
\]
and every \(F\in\mathcal T_k\) has a representation
\[
F(t)=\sum_{j=0}^{2k-1}F(j)L_k(t-j)+b\sin(\pi t).
\]

For even \(k\), the functional
\[
D_aF=\frac{F(a)-F(k+a)}2
\]
annihilates the last term. Applying \(D_a\) to the cardinal representation gives
\[
D_aF
=
\sum_{j=0}^{2k-1}w_j^{(a)}F(j),
\]
with the displayed \(w_j^{(a)}\). Trivially
\[
|D_aF|\le \|F\|_\infty.
\]
Pairing \(j\) with \(j+k\) gives the formula for \(W_k(a)\). The largest coefficient occurs at the integer sample nearest to \(a\) modulo the period, giving the exact formula for \(M_k(a)\).

Yang's period-averaging proof may now be repeated without replacing the exact coefficient maximum by the coarse estimate \(M_k\le1/2\). If a polynomial has at most \(\epsilon n\) exceptional samples, the limiting periodic function \(g\in\mathcal T_k\) satisfies
\[
H
\ge
W_k(a)-2k\epsilon(H+1)M_k(a).
\]
The spectral reduction to \(\mathcal T_k\) requires \(\epsilon k<1\). Hence every
\[
0<\epsilon<E_{k,a}(H)
\]
is admissible on the Chebyshev--Lobatto grids, proving the exact certificate.

For the weight asymptotic, subtract the two endpoint singularities of \(\csc(\pi x)\):
\[
g(x)=
\csc(\pi x)-\frac1{\pi x}-\frac1{\pi(1-x)}.
\]
The function \(g\) extends continuously to \([0,1]\), and
\[
\int_0^1g(x)\,dx=\frac2\pi\log\frac2\pi.
\]
The endpoint terms are evaluated by
\[
\sum_{r=0}^{k-1}\frac1{r+a}
=
\psi(k+a)-\psi(a),
\]
and the analogous identity with \(1-a\). The Riemann-sum remainder then yields
\[
W_k(a)=A(a)\log k+B(a)+o(1).
\]

Fix \(a\), and write \(A=A(a)\), \(B=B(a)\), \(M=M(a)\). If
\[
u=W_k(a)-H
\]
stays bounded away from both zero and infinity, then
\[
\log k=\frac{H+u-B}{A}+o(1).
\]
At such scales the constraint \(1/k\) is larger than the second term in \(E_{k,a}\) by a factor of order \(H\), so the active term is
\[
E_{k,a}(H)
=
\frac{u}{2M(H+1)}
\exp\left(-\frac{H+u-B}{A}\right)
(1+o(1)).
\]
The factor \(u e^{-u/A}\) is uniquely maximized at \(u=A\), with maximum \(A/e\). Even-integer rounding changes \(k\) only by relative \(o(1)\). Therefore
\[
\sup_{k\ {\rm even}}E_{k,a}(H)
\sim
\frac{A}{2Me}e^{B/A}
H^{-1}e^{-H/A}.
\]
Substituting \(A,B,M\) gives the displayed \(C(a)\) and
\(\lambda(a)=1/A(a)\).

Since \(\sin(\pi a)\le1\), with equality only at \(a=1/2\), the half shift is the unique fixed phase with exponent \(\pi/2\). At \(a=1/2\), the identities
\[
\psi(1/2)=-\gamma-2\log2,
\qquad
\delta_{1/2}=1/2
\]
give
\[
C(1/2)=\frac{8e^{\gamma-1}}{\pi}.
\]
The condition \(u=A=2/\pi\) also gives the stated asymptotic period.

## Context and relation to prior work

Yang (2026) proves
\[
\log\frac1{\epsilon_{\mathrm{Ch}}(C,\rho)}
=
\frac{\pi}{2}H+O(\log(H+1))
\]
and obtains the explicit cyclic lower bound quoted above. The proof already contains the exact inequality
\[
H\ge W_k-2k\epsilon(H+1)\|w\|_\infty
\]
before replacing \(\|w\|_\infty\) by \(1/2\). The present result retains that exact coefficient maximum, evaluates the relevant cosecant sum asymptotically, optimizes the period, and extends the functional from the half shift to every fixed phase \(a\in(0,1)\).

Finite cosecant sums and their asymptotic analysis are classical; Blagouchine (2025) gives a modern treatment of Watson-type cosecant sums. No novelty is claimed for the standalone cosecant-sum asymptotic. The new claim is the optimized robust-interpolation certificate and its phase dependence.

## Limitations

This result does **not** determine an asymptotic equivalent for
\(\epsilon_{\mathrm{Ch}}(C,\rho)\). Yang's upper and lower bounds still leave a factor of order \(H\) between the true parameter bounds. The theorem determines the asymptotic performance of the explicit shifted two-point cyclic obstruction family and improves the published explicit lower coefficient within that mechanism.

The phase classification is for fixed \(a\) as \(H\to\infty\). No claim is made that this family exhausts all periodic sign obstructions or all bounded functionals on \(\mathcal T_k\). No quantitative threshold in the grid size \(n\) is obtained.

## References

1. Jia-Qi Yang, *Erdős's Robust Polynomial Interpolation Problem: the Optimal Exponential Scale*, arXiv:2609.14769 (2026).  
   https://arxiv.org/abs/2609.14769

2. I. V. Blagouchine, *On a generalization of Watson's trigonometric sum (on Dowker's sum of order one half)*, Integers 25 (2025), A30; arXiv:2407.19223.  
   https://arxiv.org/abs/2407.19223
