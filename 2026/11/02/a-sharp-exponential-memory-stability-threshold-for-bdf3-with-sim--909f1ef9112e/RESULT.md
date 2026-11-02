# A sharp exponential-memory stability threshold for BDF3 with Simpson–Adams–Bashforth quadrature

## Finding
Consider the BDF3–Simpson–Adams–Bashforth memory discretization of Qiu (2026) on the scalar Volterra test equation
\[y'(t)=-\lambda y(t)+\lambda\kappa\int_0^t e^{-a(t-s)}y(s)\,ds,\qquad a,\lambda,\kappa>0.\]
Set \(\theta=ah>0\), \(\mu=\lambda h>0\), \(q=e^{-\theta}\), and \(\beta=\kappa/a>0\). The exact characteristic polynomial of its constant-coefficient tail is
\[
\begin{aligned}
P(z)={}&(11+6\mu)z^4-\left[18+(11+6\mu)q+\tfrac{23}{2}\mu\beta\theta q\right]z^3\\
&+\left[9+18q+8\mu\beta\theta q^2\right]z^2
-\left[2+9q+\tfrac52\mu\beta\theta q^3\right]z+2q.
\end{aligned}
\]
All four roots of \(P\) have modulus strictly below one **if and only if**
\[
0<\beta<\beta_{\mathrm{crit}}(\theta)
:=\frac{12(1-e^{-\theta})}{\theta e^{-\theta}(23-16e^{-\theta}+5e^{-2\theta})}.
\]
At equality the polynomial has a **simple** root \(z=1\) and its three remaining roots lie strictly inside the unit disk; above the threshold it has a real root larger than one. Moreover \(\beta_{\mathrm{crit}}(\theta)>1\) for every \(\theta>0\), with
\[\beta_{\mathrm{crit}}(\theta)=1+\tfrac38\theta^3+O(\theta^4)\quad(\theta\downarrow0),\qquad
\beta_{\mathrm{crit}}(\theta)\sim\frac{12e^\theta}{23\theta}\quad(\theta\to\infty).\]
Hence for every positive timestep the discretization admits a nonempty range \(1<\beta<\beta_{\mathrm{crit}}(\theta)\) on which the **continuous** Volterra equation has an exponentially growing mode but **every** discrete trajectory with finite starting values decays to zero. One explicit case is \(\theta=\log4\), \(\beta=6/5\), and any \(\mu>0\).

## Assumptions and scope
The statements concern exact arithmetic, scalar real coefficients \(a,\lambda,\kappa,h>0\), and the specific BDF3 derivative coefficients \((11,-18,9,-2)/(6h)\) and memory convolution formed by Simpson's rule over the earliest panels and three-point Adams–Bashforth extrapolation over the newest panel. Initial steps may follow the prescribed lower-order startup; only the eventual constant-coefficient recurrence is analyzed. Thus the result is a discrete asymptotic **spectral** stability classification, not a finite-time error bound, an assertion about every startup, or a stability result for spatially varying operators.

For indices \(n\ge5\), the convolution coefficients at lags \(j=1,2,3,\ldots,n-3,n-2,n-1,n\) are respectively \(23/12,7/12,1,\ldots,1,4/3,5/12,3/4\). For a short sum interpret the interior range as empty. The derivation below uses the actual tail for \(n\ge6\). Define
\[B(q)=23-16q+5q^2>0,\qquad W(q)=\frac{q B(q)}{12(1-q)}.\]

## Proof
**1. Eliminate the exponential-memory recurrence.** For sufficiently large \(n\), the scalar discretization is
\[
(11+6\mu)y_n-18y_{n-1}+9y_{n-2}-2y_{n-3}
=6\mu\beta\theta\left(\sum_{j=1}^{n}w_j q^j y_{n-j}\right).
\]
The exact quadrature weights satisfy \(w_1=23/12\), \(w_2=7/12\), \(w_j=1\) for interior lags, with the three left-end corrections given in the preceding section. Thus the entire convolution equals
\[
\sum_{j=1}^{n}\bar w_jq^jy_{n-j}+q^n C,\quad
\bar w_1=23/12,\ \bar w_2=7/12,\ \bar w_j=1\ (j\ge3),\quad
C=-\tfrac14y_0-\tfrac7{12q}y_1+\tfrac1{3q^2}y_2.
\]
Subtract \(q\) times the equation at index \(n-1\) from that at index \(n\); the starting-value term \(q^nC\) cancels. The remaining convolution difference is exactly
\[\tfrac{23}{12}q y_{n-1}-\tfrac43 q^2y_{n-2}+\tfrac5{12}q^3y_{n-3}.\]
This gives \(P(E)y_n=0\) for \(n\ge6\), with \(P\) displayed in the finding. Its spectral radius therefore governs all tail solutions, regardless of the finite starting values.

**2. Show the sufficient stability half-line sharply.** Put \(v=\beta\theta W(q)\). Since \(0<q<1\) and \(B(q)>0\), the condition \(v<1\) is equivalent to the displayed bound on \(\beta\). Write \(k=\mu\beta\theta=12\mu(1-q)v/[qB(q)]\), and define the Cayley transform
\[H(w)=(1-w)^4P\!\left(\frac{1+w}{1-w}\right)=\sum_{j=0}^4H_j w^j,\qquad C_j=B(q)H_j.\]
The mapping \(z=(1+w)/(1-w)\) takes \(\Re w<0\) exactly to \(|z|<1\). The quartic Routh–Hurwitz conditions (listed here in coefficients ordered high to low) are
\[
C_4,C_3,C_2,C_1,C_0>0,\quad
C_3C_2-C_4C_1>0,\quad
C_3C_2C_1-C_4C_1^2-C_3^2C_0>0.
\]
All seven are established **symbolically** for every \(0<q<1\), \(\mu>0\), and \(0\le v<1\), not by sampling. Namely, each listed left-hand side is transformed by \(q=X/(1+X)\) and \(v=Y/(1+Y)\), with \(X>0\), \(Y\ge0\), into a polynomial numerator over a product of positive powers of \(1+X\) and \(1+Y\). All coefficients of each numerator in \(X,Y,\mu\) are exact nonnegative rationals, with a strictly positive coefficient on a monomial that is positive throughout the domain. The included `verify_schur.py` reconstructs \(P\), the transform, all seven polynomials, every denominator factor, and every numerator coefficient over the rational field. The seven nonzero coefficient counts are \(3,14,16,16,16,63,117\), respectively. This is a finite, exact polynomial-positivity certificate for **every** parameter in the declared range.

**3. Prove necessity and classify the boundary.** Direct calculation gives
\[P(1)=6\mu(1-q)(1-v).\]
When \(v>1\), this is negative whereas \(P(z)\to+\infty\) as \(z\to+\infty\). Hence there is a real root strictly above one. When \(v=1\), the exact certificate still makes \(C_1,C_2,C_3,C_4\) and \(C_3C_2-C_4C_1\) strictly positive, while \(C_0=0\). Thus \(H(w)=wG(w)\), where the cubic \(G\) is strictly Hurwitz by its positive coefficients and positive cubic Hurwitz determinant. The root \(w=0\), equivalently \(z=1\), is simple, and the other three roots are strictly inside the unit disk.

**4. The discrete threshold exceeds the continuous one.** Put \(t=1-q\in(0,1)\). Exactly,
\[\theta W(e^{-\theta})
=\frac{-\log(1-t)}{t}\left(1-\tfrac12t-\tfrac1{12}t^2-\tfrac5{12}t^3\right).\]
The coefficient of \(t^j\) is zero for \(j=1,2\), while for \(j\ge3\) it is strictly negative because
\[\frac{1}{j+1}<\frac{1}{2j}+\frac{1}{12(j-1)}+\frac{5}{12(j-2)},\]
where the right-side weights total one and each denominator is strictly less than \(j+1\). Hence \(0<\theta W(e^{-\theta})<1\), and \(\beta_{\rm crit}>1\). Taylor expansion gives \(\theta W=1-3\theta^3/8+O(\theta^4)\). As \(\theta\to\infty\), \(q\to0\) and \(B(q)\to23\), yielding the stated large-step asymptotic.

**5. Exhibit false stability.** Introduce the continuous memory state \(m(t)=\kappa\int_0^t e^{-a(t-s)}y(s)\,ds\). The continuous system \(y'=-\lambda y+\lambda m\), \(m'=\kappa y-am\) has characteristic equation
\[r^2+(\lambda+a)r+\lambda a(1-\beta)=0.\]
For \(\beta>1\) it has one strictly positive root and one negative root; with \(y(0)>0\), \(m(0)=0\), the coefficient of the positive mode is nonzero. But the tail recurrence is strictly Schur for \(\beta<\beta_{\rm crit}\), forcing \(y_n\to0\) for all finite starters. At \(q=1/4\), \(W(q)=103/192\); the choice \(\beta=6/5\) gives \(v=(103/160)\log4<309/320<1\), since \(e^{3/2}>4\). This is an explicit family for every \(\mu>0\).

## Verification
Run `python verify_schur.py` with SymPy installed. It checks the exact polynomial identity, Cayley transform, full seven-part rational-coefficient Routh–Hurwitz certificate and rational witness. In the reproduced run its seven numerator polynomials had respectively \(3,14,16,16,16,63,117\) nonzero terms, all with positive rational coefficients. Optional NumPy checks test four sample spectra but **are not** used to prove the theorem. The appendix-free proof above and script together specify every critical computation.

## Relationship to prior work
Qiu (2026) provides the BDF3 method and its Simpson/Adams–Bashforth memory rule, proving sufficient long-time stability under a norm-based memory strength bound \(\beta<500/579\). That general sufficient estimate does not provide a sharp **scalar exponential-kernel** threshold. The present result uses the original quadrature weights, rather than a generic convolution or the standard BDF3 stability region, and identifies an entire continuous-unstable/discrete-decaying interval. General stability theory for convolution recurrences motivates the spectral test but does not by itself imply the exact threshold derived for these five coefficient groups.

## Limitations
Only the scalar exponential-memory mode and the constant-coefficient scheme tail are classified. The continuous and discrete asymptotic classifications need not describe finite-time errors, and instability of the numerical recurrence at \(\beta>\beta_{\mathrm{crit}}\) does not imply every special starting vector excites the unstable mode. The result does not claim A-stability, nonlinear stability, convergence on a fixed time interval for an inconsistent timestep family, or a PDE analogue. The symbolic positivity certificate depends on the explicit polynomial defined above; it is included for independent replay. Historical priority beyond inspected primary literature and available search records remains a research risk; no independent mathematical audit has been performed.

## References
1. W. Qiu, *Long-time stability and convergence of a BDF3 method for a parabolic equation with fading memory*, arXiv:2610.32364v1 (first public submission 2026-10-23), https://arxiv.org/abs/2610.32364 . Specifically the BDF3 scheme, Simpson/Adams–Bashforth memory quadrature, and long-time stability bound.
2. V. Thomée and L. Wahlbin, *Long-time numerical solution of a parabolic equation with memory*, Mathematics of Computation 62 (1994), 477–496, DOI: 10.2307/2153519. Background on numerical equations with memory; full paper was not checked for historical priority.
3. Classical Routh–Hurwitz criterion and Cayley transform for discrete polynomial stability, used as standard algebraic tools.
