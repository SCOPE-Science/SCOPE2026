# A three-mode perturbation threshold for two-step Euclidean steepest descent
## Finding
Consider exact steepest descent with exact line search on
\[
f(x)=\frac12 x^{\top}Ax,
\]
with
\[
A=\operatorname{diag}(1,s,\kappa),\qquad 1<s<\kappa,
\]
and normalize the initial error so that its squared coordinates are
\[
w_\varepsilon=\left((1-\varepsilon)\frac{\kappa^2}{1+\kappa^2},\ \varepsilon,\ (1-\varepsilon)\frac{1}{1+\kappa^2}\right).
\]
Let
\[
R_\kappa(s,\varepsilon)=\frac{\|x_2\|_2^2}{\|x_0\|_2^2}
\]
be the squared Euclidean error ratio after two exact-line-search steps. At \(\varepsilon=0\), the endpoint two-mode state satisfies
\[
R_\kappa(s,0)=\left(\frac{\kappa-1}{\kappa+1}\right)^4.
\]
Its first-order sensitivity to an added interior spectral mode is
\[
\left.\frac{\partial R_\kappa}{\partial\varepsilon}\right|_{\varepsilon=0}
=-\frac{8(\kappa-s)(s-1)}{\kappa(\kappa+1)^5}P_\kappa(s),
\]
where
\[
\begin{aligned}
P_\kappa(s)={}&2(\kappa-1)^2s^3+(-\kappa^3+3\kappa^2+3\kappa-1)s^2\\
&-2\kappa(\kappa+1)^2s+\kappa(\kappa^3+\kappa^2+\kappa+1).
\end{aligned}
\]
There is a sharp conditioning frontier \(\kappa_0\), the unique real root larger than \(1\) of
\[
F(\kappa)=\kappa^8-16\kappa^7+44\kappa^6-96\kappa^5+118\kappa^4-96\kappa^3+44\kappa^2-16\kappa+1,
\]
namely
\[
\kappa_0\approx 13.162650375738556892.
\]
For every \(1<\kappa\le \kappa_0\) and every \(s\in(1,\kappa)\), the derivative above is nonpositive. For every \(\kappa>\kappa_0\), some \(s\in(1,\kappa)\) makes it positive. Hence, above \(\kappa_0\), an arbitrarily small third spectral mode can make the two-step Euclidean contraction factor strictly worse than the balanced two-mode value
\[
\left(\frac{\kappa-1}{\kappa+1}\right)^2.
\]
For a finite exact witness, \(\kappa=14\), \(s=5\), and \(\varepsilon=1/2000\) give
\[
\frac{\|x_2\|_2}{\|x_0\|_2}\approx 0.7511143120093676
>\frac{169}{225}\approx0.7511111111111111.
\]

## Assumptions and scope
The result is for unconstrained strictly convex quadratic minimization with a symmetric positive-definite diagonal Hessian. Exact line search means that at each iterate \(x\), the step length is
\[
\alpha=\frac{x^{\top}A^2x}{x^{\top}A^3x}.
\]
The initial error is normalized only through its squared coordinates, so signs of the coordinates are irrelevant. The claim is a local perturbation statement around the balanced endpoint two-mode state, together with an exact finite witness; it is not a global maximization of the two-step Euclidean error ratio over all initial states or all spectra.

## Proof
Write the squared spectral weights of the current error as \(w_i\), with eigenvalues \(\lambda_i\), and define moments
\[
m_j=\sum_i w_i\lambda_i^j.
\]
For exact steepest descent,
\[
\alpha=\frac{m_2}{m_3},
\]
and after one step the unnormalized squared weights are \(w_i(1-\alpha\lambda_i)^2\). Thus the post-step moments are
\[
n_j=m_j-2\alpha m_{j+1}+\alpha^2m_{j+2}.
\]
The second exact line-search step has length \(\beta=n_2/n_3\), and the two-step squared Euclidean ratio is
\[
R=n_0-2\beta n_1+\beta^2n_2.
\]

For the stated family,
\[
m_j=(1-\varepsilon)\frac{\kappa^2+\kappa^j}{1+\kappa^2}+\varepsilon s^j.
\]
At \(\varepsilon=0\), direct substitution gives
\[
\alpha=\beta=\frac{2}{\kappa+1}
\]
and
\[
R=\left(\frac{\kappa-1}{\kappa+1}\right)^4.
\]
Differentiating the moment formulas at \(\varepsilon=0\) and simplifying gives exactly
\[
\left.\frac{\partial R}{\partial\varepsilon}\right|_{0}
=-\frac{8(\kappa-s)(s-1)}{\kappa(\kappa+1)^5}P_\kappa(s).
\]
Since \((\kappa-s)(s-1)>0\) for \(s\in(1,\kappa)\), the derivative is positive exactly when \(P_\kappa(s)<0\).

As a cubic in \(s\), \(P_\kappa\) satisfies
\[
P_\kappa(1)=(\kappa-1)^2(\kappa^2+1)>0,
\qquad
P_\kappa(\kappa)=\kappa(\kappa-1)^2(\kappa^2+1)>0.
\]
Its discriminant is
\[
\operatorname{disc}_s P_\kappa
=4\kappa(\kappa-1)^2(\kappa+1)^2F(\kappa).
\]
The polynomial \(F\) is reciprocal. Dividing by \(\kappa^4\), setting \(y=\kappa+\kappa^{-1}\), and then \(z=y-2\), gives
\[
\frac{F(\kappa)}{\kappa^4}
=z^4-8z^3-32z^2-48z-16.
\]
For \(\kappa>1\), one has \(z>0\). The last polynomial has exactly one positive real root by Descartes' rule of signs; therefore \(F\) has exactly one real root \(\kappa_0>1\). Exact evaluations give \(F(13)<0\) and \(F(14)>0\), so \(13<\kappa_0<14\).

When \(1<\kappa<\kappa_0\), the cubic discriminant is negative, so \(P_\kappa\) has only one real root. Since it is positive at both endpoints of \([1,\kappa]\), it cannot be negative inside that interval. At \(\kappa=14\), however,
\[
P_{14}(5)=-755<0.
\]
By continuity, the first appearance of a negative interval as \(\kappa\) increases must occur at an interior double root, hence at a zero of the discriminant. Because \(\kappa_0\) is the only such value above \(1\), this first appearance is exactly \(\kappa_0\). For \(\kappa>\kappa_0\), the two interior simple roots cannot leave through \(s=1\) or \(s=\kappa\), where \(P_\kappa\) remains positive, and cannot collide again because there is no further discriminant zero. Therefore \(P_\kappa(s)<0\) for some \(s\in(1,\kappa)\) for every \(\kappa>\kappa_0\).

Finally, for the finite witness \(\kappa=14\), \(s=5\), \(\varepsilon=1/2000\), exact rational arithmetic gives
\[
R-\left(\frac{13}{15}\right)^4
=\frac{91164433126276821700617499875214708684}{18959132351826932488781898971836487734453125}>0.
\]
Taking square roots yields the displayed strict Euclidean two-step inequality.

## Verification
The accompanying `check_threshold.py` reconstructs the exact-line-search moment formulas symbolically, verifies the derivative identity, verifies the discriminant factorization and endpoint values, isolates the unique threshold above \(1\), and checks the finite witness using exact rational arithmetic. Its recorded output is in `CHECK_OUTPUT.txt`.

## Relationship to prior work
Classical steepest-descent analysis gives the sharp one-step contraction of objective error, equivalently the Hessian norm of the iterate error. Ya-xiang Yuan's study of the Euclidean iterate error gives a sharp one-step Euclidean \(Q\)-linear bound and reduces that one-step extremal problem to two spectral modes. The present statement concerns a different object: the sensitivity of a two-step Euclidean iterate-error ratio to inserting a third spectral mode into the balanced two-mode endpoint state. The one-step result does not imply this sign transition because both exact step lengths change with the perturbed spectral distribution.

Nocedal, Sartenaer, and Zhu studied the behavior of the gradient norm and, according to their abstract and later descriptions, two-step asymptotic behavior of the gradient norm. That is a different observable and an asymptotic statement rather than the finite two-step Euclidean iterate-error perturbation treated here. Cartis, Gould, and Toint studied evaluation complexity of exact-line-search steepest descent for smooth unconstrained problems; their exact-line-search framework is relevant background, but the inspected material concerns gradient-norm complexity rather than this finite-dimensional spectral threshold.

## Limitations
This result does not claim the global worst two-step Euclidean contraction factor for condition number \(\kappa\), nor that the maximizing spectrum always has three points. The frontier is a local stability threshold of one natural two-mode benchmark under the specific mass-preserving perturbation stated above. A full-text copy of the 2002 Nocedal-Sartenaer-Zhu paper was not available through the attempted lawful access paths during verification, so an originality residual risk remains for uninspected details of that paper. No matching statement was found in the inspected sources or in the searched published-finding corpus records.

## References
1. C. Cartis, N. I. M. Gould, and Ph. L. Toint, “On the complexity of the steepest-descent method with exact linesearches,” NAXYS-16-2012, 9 September 2012. https://optimization-online.org/2012/09/3602/
2. Y.-X. Yuan, “A Short Note on the Q-linear Convergence of the Steepest Descent Method,” Mathematical Programming 123 (2010), 339–343. Author manuscript: https://lsec.cc.ac.cn/pub/home/yyx/papers/p0703.pdf
3. J. Nocedal, A. Sartenaer, and C. Zhu, “On the Behavior of the Gradient Norm in the Steepest Descent Method,” Computational Optimization and Applications 22 (2002), 5–35. DOI: 10.1023/A:1014897230089.
