# A sign mismatch flips the transverse Lyapunov spectrum of a 5D Sprott-C extension

## Finding
Al-Azzawi and Sheet print the five-dimensional flow
\[
\dot x=yz,\qquad \dot y=x-y,\qquad \dot z=1-x^2,\qquad
\dot w=-3s-x,\qquad \dot s=w-ds,
\]
with \(d>0\). For this printed vector field, the added two-dimensional fiber is uniformly exponentially stable and contributes no positive Lyapunov exponent. More precisely, on every compact ergodic invariant measure the full Lyapunov spectrum is the spectrum of the three-dimensional Sprott-C base together with the two fiber exponents
\[
\rho_\pm=\frac{-d\pm\sqrt{d^2-12}}{2}
\]
when \(d\ge\sqrt{12}\), while for \(0<d<\sqrt{12}\) both fiber exponents have real part \(-d/2\). Hence the printed 5D flow has at most one positive Lyapunov exponent on compact recurrent dynamics and cannot be hyperchaotic in the usual sense of having at least two positive Lyapunov exponents.

The printed sign also gives divergence \(-1-d\), equilibria
\[
E_\pm=(\pm1,\pm1,0,\mp d/3,\mp1/3),
\]
and equilibrium characteristic polynomial
\[
(\lambda+1)(\lambda^2+2)(\lambda^2+d\lambda+3).
\]
The source instead reports the opposite \(w\)-coordinates at equilibrium, a Jacobian with \(+d\) in the last diagonal entry, divergence \(-1+d\), and the polynomial obtained by replacing \(d\) with \(-d\) in the fiber factor. Those formulas are exactly the formulas for the different equation \(\dot s=w+ds\), which the same article later writes explicitly in its projective-synchronization systems. At \(d=0.998\), that plus-sign fiber has two exponents with real part \(+0.499\), which explains the two largest reported finite-time values \(0.4976\) and \(0.4942\); the printed minus-sign fiber instead has two exponents with real part \(-0.499\).

## Assumptions and scope
The claim concerns Eq. (2) exactly as printed, with \(d>0\), and compact invariant dynamics for which Lyapunov exponents are defined. Hyperchaos is used in the standard sense of at least two positive Lyapunov exponents. The conclusion is about the autonomous continuous-time flow, not a discretization.

The three-dimensional base is
\[
\dot x=yz,\qquad \dot y=x-y,\qquad \dot z=1-x^2.
\]
The added variables form the affine stable fiber
\[
\frac{d}{dt}\binom{w}{s}=
\begin{pmatrix}0&-3\\1&-d\end{pmatrix}\binom{w}{s}+\binom{-x}{0}.
\]
No assumption is made that the base is uniformly hyperbolic.

## Proof
Let \(B_-\) denote the displayed \(2\times2\) fiber matrix. Its characteristic polynomial is \(\lambda^2+d\lambda+3\). If \(0<d<\sqrt{12}\), its eigenvalues are a complex conjugate pair with real part \(-d/2\). If \(d\ge\sqrt{12}\), they are
\[
\frac{-d\pm\sqrt{d^2-12}}2,
\]
and both are negative because \(\sqrt{d^2-12}<d\). At the repeated-root value \(d=\sqrt{12}\), the possible polynomial prefactor in \(e^{B_-t}\) does not change the Lyapunov exponent. Thus both fiber exponents are strictly negative for every \(d>0\).

Along any trajectory, the full variational equation has block lower-triangular form
\[
\frac{d}{dt}\binom{\delta q}{\delta v}=
\begin{pmatrix}A(t)&0\\C(t)&B_-\end{pmatrix}
\binom{\delta q}{\delta v},
\]
where \(q=(x,y,z)\) and \(v=(w,s)\). The vertical subbundle \(\delta q=0\) is invariant and carries the constant cocycle \(e^{B_-t}\); the quotient by that subbundle is exactly the Sprott-C variational cocycle. Therefore the Oseledets spectrum of the full finite-dimensional triangular cocycle is the multiset union of the two fiber exponents and the three quotient exponents.

The base divergence is exactly \(-1\), so the sum of its three Lyapunov exponents is \(-1\) on every compact ergodic measure for which the exponents are defined. For a non-equilibrium ergodic measure, the autonomous flow direction contributes the exponent \(0\). The other two base exponents therefore sum to \(-1\), so at most one of them is positive. If the projected measure is an equilibrium, the base characteristic polynomial is \((\lambda+1)(\lambda^2+2)\), giving no positive real part. Adding two strictly negative fiber exponents proves the no-hyperchaos statement.

For the printed vector field, direct differentiation gives divergence \(-1-d\). Solving the five equilibrium equations yields \(s=-x/3\) and \(w=ds=-dx/3\), hence the stated \(E_\pm\). The block triangular equilibrium Jacobian factors as
\[
(\lambda+1)(\lambda^2+2)(\lambda^2+d\lambda+3),
\]
which expands to
\[
\lambda^5+(1+d)\lambda^4+(5+d)\lambda^3+(5+2d)\lambda^2+(6+2d)\lambda+6.
\]
Replacing the last equation by \(\dot s=w+ds\) changes the fiber factor to \(\lambda^2-d\lambda+3\), the divergence to \(-1+d\), and the expansion to the polynomial printed in the source. It also changes the equilibrium \(w\)-coordinate to the sign reported there.

At \(d=499/500\), the plus-sign fiber has complex eigenvalues with real part \(499/1000\), whereas the minus-sign fiber has real part \(-499/1000\). The source reports \(0.4976\) and \(0.4942\) as its two largest finite-time exponents, and its reported five-exponent sum is \(-0.002\), exactly the plus-sign divergence \(-1+0.998\), rather than the printed minus-sign divergence \(-1.998\).

## Verification
The accompanying standard-library script `verify.py` checks the equilibrium residuals, both characteristic-polynomial expansions, both divergences, the fiber roots over representative positive values of \(d\), and the exact \(d=499/500\) transverse real parts. Its recorded output is in `verification_output.txt` and ends with `VERIFY_OK`.

The scientific proof does not depend on finite-time numerical integration. The numerical comparison to the source's reported Lyapunov values is diagnostic evidence for which sign was analyzed, not a proof of the no-hyperchaos theorem.

## Relationship to prior work
The introducing article prints the minus-sign Eq. (2), but its equilibrium coordinates, Jacobian, characteristic polynomial, divergence, and Lyapunov-sum check all use the plus-sign fiber. Its later projective-synchronization master and slave equations explicitly contain \(\dot s=w+ds\). The present result makes this internal sign split mathematically explicit and derives its dynamical consequence: the printed system cannot have two positive asymptotic Lyapunov exponents on compact recurrent dynamics.

A 2023 paper by Yu et al. studies a different Sprott-C-based hyperchaotic construction and discusses parameter choices that can cause divergence. A separate 2023 paper by Al-Azzawi and Hasan introduces another, algebraically different five-dimensional Sprott-C extension. Neither states this sign correction or the stable-fiber Lyapunov decomposition for the 2024 equations.

## Limitations
This result does not rule out ordinary chaos in the printed minus-sign system: the Sprott-C base can still contribute one positive exponent, and the stable fiber can lift that chaotic dynamics. It does not classify all global attractors, prove existence of a particular chaotic invariant measure, or independently validate the asymptotic Lyapunov spectrum of the plus-sign variant. The comparison \(0.4976,0.4942\approx0.499,0.499\) concerns finite-time values reported by the source and is used only as consistency evidence for the sign mismatch.

## References
1. S. F. Al-Azzawi and A. T. Sheet, “A novel simple 5D hyperchaotic system derived from the 3D Sprott C system,” TWMS Journal of Applied and Engineering Mathematics 14(2), 495–507 (2024). Journal page: https://jaem.isikun.edu.tr/web/index.php/current/124-vol14no2/1191 . Author-uploaded public full text: ResearchGate record 379642036.
2. F. Yu, W. Zhang, X. Xiao, W. Yao, S. Cai, J. Zhang, C. Wang, and Y. Li, “Dynamic Analysis and FPGA Implementation of a New, Simple 5D Memristive Hyperchaotic Sprott-C System,” Mathematics 11(3), 701 (2023), DOI 10.3390/math11030701.
3. S. F. Al-Azzawi and H. N. Hasan, “New 5D Hyperchaotic System Derived from the Sprott C System: Properties and Anti Synchronization,” Journal of Intelligent Systems and Control 2(2) (2023), DOI 10.56578/jisc020205.
