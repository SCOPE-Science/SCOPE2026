# Tangential cubic coupling gives a sharp active-set capture threshold for SOS-convex cubic Newton steps

## Finding
For real parameters \(c\ne0\), \(B>3c^2/4\), and \(\lambda\ge0\), minimize the strongly convex polynomial
\[
f_\lambda(u,v)=\lambda u+\tfrac12(u^2+v^2)+cv^3+Bv^4
\]
over \(C=\{(u,v):u\ge0\}\). Its unique constrained minimizer is \((0,0)\). Apply the **specific third-order SOS-convex Taylor method** of Ahmadi--Chaudhry--Zhang, as extended to convex polynomial constraints by ter Voert--de Klerk: at each iterate \(z\), take the cubic Taylor polynomial \(T_{z,3}\), find the smallest \(t(z)\ge0\) for which \(T_{z,3}(y)+t(z)\|y-z\|_2^4\) is SOS-convex, and minimize this polynomial over \(C\).

For every starting point \((x,0)\) with \(x>0\), the iterates remain on the horizontal axis. At each such point the SOS-convexification coefficient is **exactly** \(t(x,0)=3c^2/4\). The next iterate is \((x_+,0)\), where \(x_+\) is the unique minimizer on \([0,\infty)\) of
\[
\lambda y+\tfrac12y^2+\tfrac{3c^2}{4}(y-x)^4.
\]
Consequently, the next step identifies the active constraint **if and only if**
\[
\boxed{\lambda\ge3c^2x^3}. \tag{1}
\]
If \(\lambda>0\), the sharp one-step identification radius along this family is \(x_{\rm cap}=(\lambda/(3c^2))^{1/3}\): every start \(0<x\le x_{\rm cap}\) captures the boundary, and every \(x>x_{\rm cap}\) does not. If \(\lambda=0\), then \(0<x_{k+1}<x_k\) for every finite \(k\), although \(x_k\to0\) cubically with the **exact** coefficient
\[
\lim_{k\to\infty}\frac{x_{k+1}}{x_k^3}=3c^2.
\]
Thus strong convexity, an affine constraint satisfying LICQ and Slater's condition, and cubic local convergence do not ensure finite primal active-set identification when its KKT multiplier is zero. The positive-multiplier case exhibits an exact quantitative capture boundary.

## Assumptions and scope
All optimization and iteration statements use exact real arithmetic; minimizers and the minimal SOS-convexification coefficient are selected exactly. The objective is the displayed bivariate quartic; \(B\) may be any number strictly above \(3c^2/4\) and has no effect on the cubic Taylor step along the horizontal axis. The sole inequality is \(-u\le0\); its active multiplier at the minimizer is \(\lambda\). We consider starts \((x,0)\), \(x>0\), not arbitrary starting vectors. Equation (1) includes equality; the asymptotic statement pertains only to \(\lambda=0\).

## Proof
**(1) Objective and constraints.** The Hessian of \(f_\lambda\) is diagonal with entries \(1\) and \(1+6cv+12Bv^2\). Completing the square gives a strictly positive lower bound \(1-3c^2/(4B)\) for the latter, so \(f_\lambda\) is strongly convex. Its gradient at the origin is \((\lambda,0)\), so the origin is the unique constrained minimizer. The half-space has Slater points and the active gradient \((-1,0)\ne0\); the KKT multiplier is \(\lambda\).

**(2) Exact minimal SOS-convexification.** Write the model increment from \((x,0)\) as \((h,v)\). Because the third-order Taylor model is \(\lambda(x+h)+\tfrac12((x+h)^2+v^2)+cv^3\), up to an immaterial constant, its regularization adds \(t(h^2+v^2)^2\). The Hessian is
\[
H_t(h,v)=\begin{pmatrix}1+12th^2+4tv^2&8thv\\8thv&1+6cv+4th^2+12tv^2\end{pmatrix}.
\]
The lower-right diagonal entry at \(h=0\) is nonnegative for all \(v\) only if \(t\ge3c^2/4\), by its quadratic discriminant. Set \(t_0=3c^2/4\). To prove convexity at equality, for a unit direction \(w=(p,q)\), the Hessian quadratic form is
\[
1+6cvq^2+3c^2(h^2+v^2)+6c^2(hp+vq)^2.
\]
As a quadratic function of \((h,v)\), its coefficient matrix is \(3c^2I+6c^2ww^{\mathsf T}\), whose inverse is \((3c^2)^{-1}(I-\tfrac23ww^{\mathsf T})\). Its exact minimum over all \((h,v)\) is
\[
1-3q^4+2q^6=(1-q^2)^2(1+2q^2)\ge0.
\]
Homogeneity in \(w\) proves \(H_{t_0}\succeq0\) at every point. We use the established convexity/SOS-convexity equivalence for bivariate polynomials of degree at most four (Ahmadi--Parrilo, 2013); it applies to this exact bivariate quartic model, so \(t_0\) is SOS-convex feasible. Combining necessity and sufficiency proves \(t(x,0)=t_0\). This reasoning is independent of \(x,\lambda,B\).

**(3) Invariant axis and sharp capture test.** For each fixed \(u\), the convex model has vanishing partial derivative in \(v\) at \(v=0\), hence is minimized there. The Hessian also shows strict convexity in the \(u\) direction. The unique constrained minimum is therefore on \(v=0\), and its normal coordinate minimizes the displayed one-variable function. That function's derivative is \(\lambda+y+3c^2(y-x)^3\) and its second derivative is \(1+9c^2(y-x)^2>0\). It has its unique constrained minimizer at \(y=0\) precisely when the derivative at zero is nonnegative, namely \(\lambda-3c^2x^3\ge0\). Otherwise its unique stationary point lies strictly between \(0\) and \(x\). The same reasoning repeats after every interior step.

**(4) Infinite nonidentification and exact rate.** For \(\lambda=0\), each positive iterate satisfies
\[
x_{k+1}=3c^2(x_k-x_{k+1})^3,\qquad 0<x_{k+1}<x_k.
\]
The positive decreasing sequence has a limit \(L\ge0\); continuity of the recurrence forces \(L=0\). The recurrence also implies \(x_{k+1}/x_k\le3c^2x_k^2\to0\). Dividing it by \(x_k^3\) gives the stated cubic limit \(3c^2\). No finite iterate hits the boundary.

## Verification
The accompanying `verify.py` independently checks the Hessian identity and minimization factorization symbolically, tests the Hessian's exact principal minors using rational numbers, checks the closed-form capture derivative and second derivative symbolically, and compares one-dimensional roots with (1) for several parameter values. It also verifies finite positive iterates and their cubic scaling. Execute `python verify.py` in an environment satisfying `requirements.txt`. These finite tests do not substitute for the argument over all parameters and iterations above.

## Relationship to prior work
Ter Voert--de Klerk (2026, arXiv:2609.01001v1) define the SOS-convexified constrained Taylor step in their Section 3 and prove local \(d\)-th-order convergence and active-set identification under LICQ and strict complementarity in Theorems 5.6 and 5.9. The claimed contribution here is the **specific, exact two-dimensional boundary mechanism and sharp multiplier/starting-distance frontier**, not the source algorithm, convergence theorem, or generic sufficiency of strict complementarity. Ahmadi--Chaudhry--Zhang (2023/2024, arXiv:2311.06374) define the unconstrained higher-order SOS-convex Taylor step; the exact active-set calculation here concerns the later constrained extension. The established bivariate quartic SOS-convexity theorem is used rather than claimed. Burke--Moré (1988) and Díaz et al. (2026) study more general identification and degeneracy in other algorithmic frameworks, but the statements inspected do not yield (1) or this cubic nonidentification trajectory for the specified constrained higher-order method.

## Limitations
The theorem concerns the exact minimal SOS-convexification rule and the invariant set of starts \((x,0)\); it does not classify arbitrary bivariate trajectories, finite-precision semidefinite solvers, other Taylor orders, or alternative regularizers. Lack of finite identification at zero multiplier is not a general impossibility theorem for all algorithms, nor does the theorem claim that strict complementarity is universally necessary. No independent audit has been performed.

## References
1. L. ter Voert and E. de Klerk, *Further analysis and extension of the higher-order Newton method of Ahmadi, Chaudhry, and Zhang*, arXiv:2609.01001v1 (first public 2026-09-01), Sections 3 and 5.1. https://arxiv.org/html/2609.01001v1
2. A. A. Ahmadi, A. Chaudhry, J. Zhang, *Higher-Order Newton Methods with Polynomial Work per Iteration*, arXiv:2311.06374v2 (2024), Sections 3 and 4. https://arxiv.org/html/2311.06374v2
3. A. A. Ahmadi, P. A. Parrilo, *A Complete Characterization of the Gap between Convexity and SOS-Convexity*, SIAM J. Optim. 23 (2013), 811--833, doi:10.1137/110856010.
4. J. V. Burke, J. J. Moré, *On the Identification of Active Constraints*, SIAM J. Numer. Anal., doi:10.1137/0725068.
5. M. Díaz, P. Izquierdo Lehmann, H. Lu, J. Yang, *Active set identification and rapid convergence for degenerate primal-dual problems*, arXiv:2602.10436v1 (2026). https://arxiv.org/html/2602.10436v1
