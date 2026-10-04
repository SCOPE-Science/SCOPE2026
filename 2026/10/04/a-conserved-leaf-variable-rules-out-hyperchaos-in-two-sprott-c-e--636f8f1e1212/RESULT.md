# A conserved leaf variable rules out hyperchaos in two Sprott-C extensions

## Finding
Yu et al. introduce two autonomous extensions of the Sprott-C flow and classify both as hyperchaotic. For the equations printed in the article, that classification is structurally impossible on compact recurrent dynamics.

Their four-dimensional system is
\[
\dot x=yz,\qquad \dot y=x-y,\qquad \dot z=1-x^2,\qquad \dot u=ax+bu,
\]
with the article taking \(a>0\) and \(b<0\). The \((x,y,z)\) subsystem is autonomous and the added scalar is a stable driven fiber. On every compact ergodic invariant measure, its Lyapunov spectrum is therefore the three-dimensional base spectrum together with the exact fiber exponent \(b<0\). A non-equilibrium ergodic measure of the three-dimensional autonomous base has the flow exponent \(0\), while the base divergence is exactly \(-1\); hence the base has at most one positive exponent, and so does the four-dimensional extension.

Their five-dimensional memristive system is
\[
\dot x=cyz,\qquad \dot y=x-y,\qquad \dot z=1-x^2,
\]
\[
\dot u=ax-bu+k\bigl(m+3n\phi^2\bigr)z,\qquad \dot\phi=y-x,
\]
with \(a,b,c,k,m,n>0\). It has the exact first integral
\[
H=y+\phi,
\qquad \dot H=(x-y)+(y-x)=0.
\]
Writing \(h=H\) gives the triangular form
\[
\dot x=cyz,\qquad \dot y=x-y,\qquad \dot z=1-x^2,\qquad \dot h=0,
\]
\[
\dot u=ax-bu+k\bigl(m+3n(h-y)^2\bigr)z.
\]
Thus, on every compact ergodic invariant measure, the full five-dimensional Lyapunov spectrum is exactly the spectrum of the three-dimensional \((x,y,z)\) base together with \(0\) and \(-b\). Since the base divergence is again \(-1\) and a non-equilibrium base measure has the autonomous flow exponent \(0\), the five-dimensional system also has at most one positive Lyapunov exponent. In particular, it cannot be hyperchaotic in the standard sense of having at least two positive asymptotic Lyapunov exponents.

At every equilibrium of the five-dimensional system, with \(s\in\{-1,1\}\),
\[
(x,y,z,u,\phi)=\left(s,s,0,\frac{as}{b},\phi\right),
\]
and the characteristic polynomial is
\[
\lambda(\lambda+b)(\lambda+1)(\lambda^2+2c).
\]
Hence the linear spectrum is independent of \(\phi\), despite the article stating that equilibrium stability depends on \(\phi\).

## Assumptions and scope
The four-dimensional statement uses the parameter regime actually adopted in the article for its claimed bounded hyperchaotic example: \(b<0\). The five-dimensional statement assumes the article's stated positive parameters, in particular \(b>0\) and \(c>0\).

The Lyapunov-spectrum conclusions concern compact ergodic invariant measures for which the usual Oseledets exponents are defined. For non-equilibrium invariant measures of a smooth autonomous flow, the flow direction supplies the standard zero exponent. Measures supported on equilibria are handled separately by the displayed equilibrium spectra.

Hyperchaos means at least two positive asymptotic Lyapunov exponents. The result does not exclude ordinary chaos with one positive exponent, periodic dynamics, multistability, or long finite-time intervals with two numerically positive finite-time growth rates.

## Proof
For the four-dimensional system, order the tangent variables as \((\delta x,\delta y,\delta z,\delta u)\). The variational equation is block lower triangular:
\[
\frac{d}{dt}
\begin{pmatrix}\delta q\\ \delta u\end{pmatrix}
=
\begin{pmatrix}A(t)&0\\ (a,0,0)&b\end{pmatrix}
\begin{pmatrix}\delta q\\ \delta u\end{pmatrix},
\qquad q=(x,y,z).
\]
The one-dimensional vertical bundle is invariant and carries exactly \(e^{bt}\), while the quotient cocycle is the three-dimensional Sprott-C variational cocycle. The Lyapunov spectrum of this triangular cocycle is therefore the multiset union of the base spectrum and \(\{b\}\). The base divergence is \(-1\). For any non-equilibrium ergodic base measure, one exponent is \(0\), so the remaining two sum to \(-1\) and at most one can be positive. At either base equilibrium \((s,s,0)\), \(s=\pm1\), the base characteristic polynomial is \((\lambda+1)(\lambda^2+2)\), so there is no positive real part there either.

For the five-dimensional system, direct differentiation gives
\[
\frac{d}{dt}(y+\phi)=x-y+y-x=0.
\]
Using \(h=y+\phi\) is a global invertible linear change in the \((y,\phi)\) variables. In coordinates \((q,h,u)\), with \(q=(x,y,z)\), the variational equation has the block lower-triangular form
\[
\frac{d}{dt}
\begin{pmatrix}\delta q\\ \delta h\\ \delta u\end{pmatrix}
=
\begin{pmatrix}
A_c(t)&0&0\\
0&0&0\\
B(t)&C(t)&-b
\end{pmatrix}
\begin{pmatrix}\delta q\\ \delta h\\ \delta u\end{pmatrix}.
\]
On compact support, the off-diagonal coefficients are bounded. The invariant \(u\)-fiber has exponent \(-b\), and the quotient by that fiber is the direct sum of the base cocycle and the constant scalar cocycle \(\dot{\delta h}=0\). Hence the full Lyapunov spectrum is the base spectrum together with \(0\) and \(-b\).

The three-dimensional base has divergence \(-1\). Therefore, on every non-equilibrium ergodic base measure, its exponents have the form \(\lambda_+\), \(0\), and \(-1-\lambda_+\) after ordering, with at most one positive member. If the projected base measure is supported at an equilibrium, compact invariance of the driven scalar equation forces \(u\) to its equilibrium value, so the full measure is itself an equilibrium measure.

Finally, at \((s,s,0,as/b,\phi)\), the three-dimensional base factor is \((\lambda+1)(\lambda^2+2c)\), the conserved-leaf direction contributes \(\lambda\), and the stable scalar fiber contributes \(\lambda+b\). This yields the stated equilibrium polynomial and shows explicitly that the eigenvalues do not depend on \(\phi\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the first-integral cancellation, both equilibrium families, the four-dimensional and five-dimensional characteristic-polynomial factorizations, and the source parameter signs. It also checks that the two Lyapunov lists reported by the article have the advertised divergence sums, while emphasizing that matching a divergence sum is necessary but does not overcome the exact triangular-spectrum obstruction.

The verifier was executed from the packaged path and returned `VERIFY_OK`.

## Relationship to prior work
The introducing article gives exactly the two systems above, reports two positive numerical Lyapunov exponents for each, and uses those lists to classify the systems as hyperchaotic. It also states for the memristive model that the equilibrium stability depends on \(\phi\). The first integral \(y+\phi\), the resulting global triangular reduction, and the consequent one-positive-exponent ceiling are not stated there.

A related 2022 memristive Sprott-B paper studies a different four-dimensional vector field and describes it as chaotic rather than establishing the present reduction. A later 2024 five-dimensional Sprott-C construction couples a different two-dimensional linear subsystem and likewise does not contain the conserved quantity \(y+\phi\) or imply the present source-specific decomposition.

Targeted searches for the exact title, the equation-level conserved quantity, the aliases "stable skew product" and "first integral", and the two-positive-exponent implication did not locate a published correction or a stronger result covering these two printed systems.

## Limitations
This result is structural rather than a numerical reconstruction of the article's finite-time Lyapunov algorithm. It does not identify which implementation detail produced the reported second positive exponent. It does not rule out ordinary chaos, hidden chaotic attractors, periodic windows, or coexistence of attractors on different invariant leaves. It also does not assess the FPGA discretization as a discrete-time dynamical system; discretization can have a different Lyapunov spectrum from the continuous-time ODE.

## References
1. F. Yu, W. Zhang, X. Xiao, W. Yao, S. Cai, J. Zhang, C. Wang, and Y. Li, “Dynamic Analysis and FPGA Implementation of a New, Simple 5D Memristive Hyperchaotic Sprott-C System,” Mathematics 11 (2023), 701. DOI: 10.3390/math11030701.
2. R. Ramamoorthy, K. Rajagopal, G. D. Leutcho, O. Krejcar, H. Namazi, and I. Hussain, “Multistable dynamics and control of a new 4D memristive chaotic Sprott B system,” Chaos, Solitons & Fractals 156 (2022), 111834. DOI: 10.1016/j.chaos.2022.111834.
3. S. F. Al-Azzawi and A. T. Sheet, “A novel simple 5D hyperchaotic system derived from the 3D Sprott C system,” TWMS Journal of Applied and Engineering Mathematics 14 (2024), 495–507.
