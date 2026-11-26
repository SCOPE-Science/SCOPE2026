# Uniform inversion of the reduced imperfect Bose-gas saddle near three dimensions

## Finding

Set \(\delta=(3-d)/2>0\). For the reduced saddle equation
\[
X=\operatorname{Li}_{1-\delta}(e^{-x}),\qquad x>0,
\]
let \(A_\delta=\Gamma(\delta)\), \(B_\delta=-\zeta(1-\delta)\), and \(z=[A_\delta/(X+B_\delta)]^{1/\delta}\). In the joint limit \(\delta\downarrow0\), \(X\to\infty\), the unique solution satisfies
\[
x=z\left(1+O\!\left(\frac{z}{1+\delta X}\right)\right).
\]
In particular, writing \(g=[1+\delta X/(1-\gamma_E\delta)]^{-1/\delta}\), where \(\gamma_E\) is Euler's constant, gives the simpler uniform form
\[
x=g\left(1+O\!\left(\delta+\frac{g}{1+\delta X}\right)\right).
\]
The variable \(\delta X\) describes crossover on the logarithmic scale: \(-\log x\sim X\) for \(\delta X\to0\), and more generally \(-\log x\sim\delta^{-1}\log(1+\delta X)\) in the joint limit. **Relative** recovery of the fixed-dimension power law \([A_\delta/X]^{1/\delta}\) instead holds if and only if \(\delta^2 X\to\infty\). At the finer boundary \(\delta^2 X\to c\in(0,\infty)\), the ratio to that power law tends to \(e^{-1/c}\); if \(\delta^2 X\to0\), it tends to zero.

## Model and scope

In the periodic slab model of Jakubczyk, Napiórkowski and Sęk [1], take the lateral thermodynamic limit first, with the quantum-critical hierarchy \(L\gg\lambda\gg D\gg l_{\mathrm{mic}}\). Here \(D\) is the slab width, \(\lambda\) is the thermal de Broglie wavelength, and \(l_{\mathrm{mic}}\) is the microscopic length. For coupling \(a>0\) and chemical potential \(\mu>0\), let \(L_\mu=(a/\mu)^{1/d}\), \(X=\lambda^{d-1}D/L_\mu^d\), and let the stationary point be \(\bar s=-x\). The equation above is the reduced, leading low-temperature equation, with the term proportional to \(-\bar s/(a\beta)\) discarded. The estimates compare solutions of the reduced equation only; they do not bound the error due to that reduction, control finite-volume corrections, or give a uniform asymptotic for the force itself. Continuous \(d\) refers to analytic continuation of the equation.

## Proof

For small positive \(\delta\), the defining series is strictly decreasing in \(x>0\), from infinity to zero. Hence the solution exists and is unique for \(X>0\). In the range \(0<\delta\le\delta_0<1/2\), the series for \(x\ge\eta>0\) is bounded above by \(\sum_{m\ge1}m^{-1+\delta_0}e^{-m\eta}\). Thus the solution tends to zero uniformly as \(X\to\infty\).

The polylogarithm expansion [2] gives
\[
X=A_\delta x^{-\delta}-B_\delta+R_\delta(x),\qquad
R_\delta(x)=\sum_{j\ge1}\zeta(1-\delta-j)\frac{(-x)^j}{j!}
=-\zeta(-\delta)x+O(x^2).
\]
The remainder is uniform for \(0<\delta\le\delta_0\) and sufficiently small \(x>0\): the \(j=1\) coefficient is bounded, and the zeta functional equation and Stirling's formula bound \(|\zeta(1-\delta-j)|/j!\) for \(j\ge2\) by a fixed polynomial in \(j\) times \((2\pi)^{-j}\), uniformly on this interval of \(\delta\). In particular \(R_\delta=O(x)\).

Put \(a_0=\delta^{-1}-\gamma_E\). Both \(A_\delta\) and \(B_\delta\) equal \(a_0+O(\delta)\). Since \(\delta(X+B_\delta)\) is comparable to \(1+\delta X\), inversion yields
\[
\log(x/z)=-\delta^{-1}\log\left(1-\frac{R_\delta(x)}{X+B_\delta}\right)
=O\left(\frac{x}{1+\delta X}\right).
\]
This first gives \(x/z\to1\) and then allows \(z\) in place of \(x\) in the bound. Also
\[
\frac{(X+B_\delta)/A_\delta}{1+X/a_0}
=\frac{X+B_\delta}{X+a_0}\frac{a_0}{A_\delta}=1+O(\delta^2),
\]
so \(\log(z/g)=O(\delta)\). Exponentiation proves both uniform estimates.

To see the logarithmic scale, set \(u=\delta X\). Uniformly for \(u>0\), the difference between \(\log(1+u/(1-\gamma_E\delta))\) and \(\log(1+u)\) is \(O(\delta u/(1+u))\), an \(O(\delta)\) fraction of \(\log(1+u)\). Also \(\delta^{-1}\log(1+\delta X)\to\infty\): when \(u\le1\) it is at least \(X/2\), and otherwise at least \(\log(2)/\delta\). Thus \(-\log x\sim\delta^{-1}\log(1+\delta X)\), which gives the small-\(u\) endpoint. At \(\delta=0\) the reduced equation has exact solution \(-\log(1-e^{-X})\sim e^{-X}\); the joint logarithmic endpoint does not itself assert relative equivalence to this exponential.

For the power law,
\[
\log\frac{x}{[A_\delta/X]^{1/\delta}}
=-\delta^{-1}\log(1+B_\delta/X)+O\left(\frac{z}{1+\delta X}\right).
\]
Set \(b_\delta=\delta B_\delta\to1\) and \(v=\delta^2X\). The positive term \(\delta^{-1}\log(1+b_\delta\delta/v)\) is between \(b_\delta/(v+b_\delta\delta)\) and \(b_\delta/v\) by \(t/(1+t)\le\log(1+t)\le t\). These bounds give the three stated limits. For convergence of the ratio to one, the lower bound must tend to zero, which requires \(v\to\infty\), and the upper bound then also tends to zero. This proves the if and only if statement.

## Verification and sharpness checks

The proof is analytic. For \(\delta=e^{-2X}\), \(g\sim e^{-X}\), and \(R_\delta(x)\sim x/2\) because \(-\zeta(0)=1/2\). Here \(\delta(X+B_\delta)\to1\), and \(\log(x/g)=\log(x/z)+O(\delta)\sim e^{-X}/2\). Thus the error of the simple form cannot in general be bounded by \(O(\delta)\) alone. For \(\delta=j^{-2}\), \(X=j^3\), the quantity \(\delta X=j\) diverges, but \(\delta^2X=1/j\to0\) and the relative power-law ratio tends to zero rather than one.

## Relationship to prior work

The source model, saddle reduction, and separate dimensional endpoints are from [1], Eq. (12) for the saddle before reduction, Eq. (13) at \(d=3\), and Eqs. (16)–(18) for separate \(2<d<3\) asymptotics. In particular Eq. (16) already displays the gamma and zeta terms in the forward expansion. Reference [2] provides the full special-function series used to control its remainder. The result here distinguishes the logarithmic crossover from relative recovery of the power law, with a uniform error for the reduced saddle only. It makes no claim of a new model, new endpoint at fixed dimension, or exhaustive historical priority.

## References

1. P. Jakubczyk, M. Napiórkowski and T. Sęk, “Repulsive Casimir forces at quantum criticality,” *Europhysics Letters* **113** (2016), 30006, DOI 10.1209/0295-5075/113/30006, arXiv:1601.05435.
2. NIST Digital Library of Mathematical Functions, §25.12 Eq. 25.12.12, https://dlmf.nist.gov/25.12.E12.
