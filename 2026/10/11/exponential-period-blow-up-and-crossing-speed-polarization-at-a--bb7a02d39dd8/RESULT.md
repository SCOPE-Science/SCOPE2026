# Exponential period blow-up and crossing-speed polarization at a nilpotent-center boundary

## Finding
For the cubic nilpotent-center family
\[
\dot x=u,\qquad \dot u=-x^3+b x u,\qquad |b|<2\sqrt2,
\]
fix \(A>0\) and the periodic trajectory through \((A,0)\). Write \(\Delta=8-b^2\). Its minimal period \(T_b(A)\) is measured in the original time, and \(u_+>0>u_-\) denote its distinct upward and downward velocities at the section \(x=0\). Then
\[
T_b(A)\sim \frac{2}{A}\sqrt{\frac\pi e}\exp\left(\frac{\pi |b|}{2\sqrt\Delta}\right)
\quad (|b|\uparrow2\sqrt2),
\qquad \frac{|u_-|}{u_+}=\exp\left(\frac{\pi b}{\sqrt\Delta}\right).
\]
The boundary asymptotic has its complete leading constant. For \(b\uparrow2\sqrt2\), the downward crossing tends to \(-eA^2/\sqrt2\), while the upward crossing is exponentially suppressed with \(e^{\pi b/\sqrt\Delta}u_+\to eA^2/\sqrt2\). For \(b\downarrow-2\sqrt2\), exchange the roles of upward and downward crossings: \(u_+\to eA^2/\sqrt2\), and \(e^{\pi|b|/\sqrt\Delta}|u_-|\to eA^2/\sqrt2\).

## Assumptions and scope
All statements hold for every real \(b\) in the strict global-center interval \(|b|<2\sqrt2\) and every amplitude \(A>0\), using the unique classical solution through \((A,0)\). The two crossings of \(x=0\) are distinguished by the sign of \(u\); the orientation of time does not change. The limit fixes \(A\) and varies the coefficient \(b\) from inside the center interval. No assertion is made at or beyond the boundary \(|b|=2\sqrt2\). The family is equivalent under \(u=-y\) to the cubic case of the García–Llibre nilpotent global-center system \(\dot x=-y,\ \dot y=x^3+bxy\).

## Proof
Set \(w=u/x^2\) for \(x\ne0\). Direct differentiation yields \(\dot w=-xQ_b(w)\), where \(Q_b(w)=2w^2-bw+1\). Since its discriminant is negative throughout \(\Delta>0\), \(Q_b(w)>0\) for every real \(w\). Put
\[
I_b(w)=\int_0^w\frac{s\,ds}{Q_b(s)}
=\frac14\log Q_b(w)+\frac{b}{2\sqrt\Delta}\left(\arctan\frac{4w-b}{\sqrt\Delta}+\arctan\frac b{\sqrt\Delta}\right).
\]
The identity \(d\log|x|/dw=-w/Q_b(w)\) gives the two halves of the same orbit as \(x=\pm A e^{-I_b(w)}\) and \(u=A^2we^{-2I_b(w)}\). On the positive \(x\)-half, \(w\) decreases continuously from \(+\infty\) through zero to \(-\infty\); on the negative half it increases from \(-\infty\) through zero to \(+\infty\). The limits \(u\to A^2we^{-2I_b(w)}\) at both ends are finite and nonzero. Both halves match smoothly at the axis by uniqueness of solutions to the smooth polynomial vector field. The trajectory closes without meeting another zero of \(u\) in either half-plane, hence its indicated period is minimal.

As \(w\to\pm\infty\), direct use of the last expression for \(I_b\) gives the exact velocities
\[
u_+=\frac{A^2}{\sqrt2}\exp\left[-\frac b{\sqrt\Delta}\left(\frac\pi2+\arctan\frac b{\sqrt\Delta}\right)\right],
\quad
u_-=-\frac{A^2}{\sqrt2}\exp\left[\frac b{\sqrt\Delta}\left(\frac\pi2-\arctan\frac b{\sqrt\Delta}\right)\right].
\]
Dividing their magnitudes gives the claimed exact polarization. The expansion \(\arctan(b/\sqrt\Delta)=\operatorname{sgn}(b)\pi/2-\sqrt\Delta/b+o(\sqrt\Delta)\) along either boundary proves the four crossing limits and their sharp constants.

The traversal time of either half-plane is \(A^{-1}\int_{-\infty}^{\infty}e^{I_b(w)}Q_b(w)^{-1}dw\), so
\[
T_b(A)=\frac2A\int_{-\infty}^{\infty}\frac{e^{I_b(w)}}{Q_b(w)}\,dw.
\]
Use \(\theta=\arctan((4w-b)/\sqrt\Delta)\) and \(B=b/(2\sqrt\Delta)\) to obtain
\[
T_b(A)=\frac{2^{5/4}}{A\Delta^{1/4}}\exp\left[B\arctan\frac b{\sqrt\Delta}\right]
\int_{-\pi/2}^{\pi/2}\frac{e^{B\theta}}{\sqrt{\cos\theta}}\,d\theta.
\]
For completeness the standard beta-integral Fourier continuation yields an exact gamma representation
\[
T_b(A)=\frac{2^{7/4}\pi^{3/2}}{A\Delta^{1/4}}
\frac{\exp\bigl[B\arctan(b/\sqrt\Delta)\bigr]}
{\left|\Gamma\left(\tfrac34+\tfrac{iB}{2}\right)\right|^2}.
\]
The integral is positive and finite for all \(\Delta>0\), providing an independent existence and finiteness check. For the critical limit let \(L=|B|\to\infty\). Symmetry of the angular integral, followed by its substitution \(s=L(\pi/2-|\theta|)\) near the dominant endpoint, gives the endpoint Laplace asymptotic
\[
\int_{-\pi/2}^{\pi/2}\frac{e^{B\theta}}{\sqrt{\cos\theta}}d\theta
\sim \sqrt{\frac\pi L}e^{\pi L/2}.
\]
Furthermore \(B\arctan(b/\sqrt\Delta)=\pi L/2-1/2+o(1)\), and \(2^{5/4}\Delta^{-1/4}L^{-1/2}=2^{7/4}/\sqrt{|b|}\to2\). Combining these identities proves the sharp period asymptotic.

## Verification
Run `python checker.py` after `python -m pip install -r requirements.txt`. The independent integral/quadrature and gamma representations are compared for several interior parameter values; the limiting period coefficient and axis-speed polarization are checked at parameters approaching the boundary. The script verifies sample values numerically; the theorem for every interior parameter and the infinite boundary limit are established by the preceding analytic argument, not by those samples.

## Relationship to prior work
García and Llibre classified this polynomial Liénard subfamily as a global nilpotent center for \(|b|<2\sqrt2\) (their quasihomogeneous case). Álvarez, Gasull and Prohens had earlier analyzed period functions of general quasihomogeneous centers and explicitly noted that the member \(\dot x=-y,\dot y=x^3+axy\) already had an explicit period function. Accordingly, neither qualitative center existence, amplitude homogeneity of the period, nor the existence of a period quadrature is claimed as new. The focused result here is the *sharp approach to the loss-of-center parameter boundary*, with its universal essential exponential rate and prefactor and the simultaneously polarized crossing velocities; that is a parameter-family comparison rather than a period-monotonicity statement for a fixed vector field. The 2017 paper was partially accessible through its abstract and an indexed page-11 passage, leaving a material priority risk described below.

## Limitations
The theorem is confined to the explicitly stated cubic family, strict center interval and fixed positive amplitude; it does not extend to non-quasihomogeneous perturbations or classify dynamics at the boundary. The 2017 source already covers qualitative period properties and reports an exact period expression for the same subfamily. Its full text was not obtained, so the possibility that its unpublished-to-this-comparison formulas also state or immediately evaluate the present boundary constants remains a real priority uncertainty. The special-function representation is a derivation aid, not treated as independently novel, and numerical tests are not an infinite proof. No independent audit has been performed.

## References
1. Isaac A. García and Jaume Llibre, *Polynomial Liénard systems with a nilpotent global center*, Rendiconti del Circolo Matematico di Palermo, published online 19 December 2022. DOI: 10.1007/s12215-022-00850-8. Full open-access article inspected.
2. M. J. Álvarez, A. Gasull and R. Prohens, *Global behaviour of the period function of the sum of two quasi-homogeneous vector fields*, Journal of Mathematical Analysis and Applications 449 (2017), 1553–1569. DOI: 10.1016/j.jmaa.2016.12.077. Abstract and an indexed manuscript excerpt inspected; full text inaccessible during comparison.
3. W. Aziz, J. Llibre and C. Pantazi, *Centers of quasi-homogeneous polynomial differential equations of degree three*, Advances in Mathematics 254 (2014). DOI: 10.1016/j.aim.2013.12.006. Background center classification.
