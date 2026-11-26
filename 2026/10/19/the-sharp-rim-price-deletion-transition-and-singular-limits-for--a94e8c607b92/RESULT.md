# Noncommuting cheap-rim and large-wheel limits in resistance-optimal design

## Finding

In a simple wheel with a hub and a cycle of \(n\ge3\) rim vertices, choose each nonnegative edge conductance independently. Spoke conductance has unit price, rim conductance has price \(t>0\), and the budget is \(B>0\). Minimize the sum of effective resistances over unordered vertex pairs, with infinite objective for disconnection. Write \(a_n(t)\) and \(b_n(t)\) for the common spoke and rim conductances of the unique optimum. Put \(x_n=na_n/B\) and \(y_n=nb_n/B\), so the spoke and rim budget fractions are \(x_n\) and \(t y_n=1-x_n\).

At each fixed \(n\ge3\), the sharp cheap-rim law is
\[
 y_n(t)\sim\sqrt{\frac{(n+1)(n^2-1)}{12t}},\qquad
 1-x_n(t)\sim\sqrt{\frac{(n+1)(n^2-1)t}{12}},\qquad t\downarrow0.
\]
Thus the optimized rim conductance diverges even though its budget fraction tends to zero. The spoke-budget limits do not commute:
\[
 \lim_{t\downarrow0}\lim_{n\to\infty}x_n(t)=\tfrac12,
 \qquad
 \lim_{n\to\infty}\lim_{t\downarrow0}x_n(t)=1.
\]
The first of these iterated limits uses the fixed-positive-price law in [1]; the new calculation here is the fixed-order cheap-rim asymptotic and its consequence for the other order of limits. No uniform joint-limit formula is asserted.

## Proof

For connected edge supports the objective is \((n+1)\) times the trace inverse of the Laplacian on the orthogonal complement of the constants. This is strictly convex in the conductance vector: along a nonzero edge perturbation its second derivative is \(2(n+1)\operatorname{tr}(H^{-1}EH^{-1}EH^{-1})>0\), where \(H\) is the positive-definite restricted Laplacian and \(E\ne0\) its symmetric perturbation. Positivity follows by writing the trace as the squared Frobenius norm of \(H^{-1/2}EH^{-1}\). The restriction is injective on edge perturbations because the full Laplacian annihilates constants and its off-diagonal entries recover each edge conductance. The feasible set is compact for fixed \(t>0\), contains a connected star, and at disconnection the objective diverges as an eigenvalue on the orthogonal complement tends to zero. This proves existence and uniqueness. Wheel rotations then force constant conductances within each edge class, with positive spoke conductance because the hub must be connected. These are the symmetry and convexity ingredients of the known priced-wheel reduction [1,2].

Set \(x=1-ty\) for a feasible symmetric allocation, with \(0\le y<1/t\). The nonzero Laplacian eigenvalues, divided by \(B/n\), are \((n+1)x\) and \(x+\delta_k y\), \(1\le k<n\), where \(\delta_k=4\sin^2(\pi k/n)\). Indeed the hub and rim-constant space contributes the first eigenvalue, and the zero-sum rim Fourier modes give the rest. Apart from the constant factor \(n(n+1)/B\), the objective is therefore
\[
 F_{n,t}(y)=\frac{1}{(n+1)(1-ty)}+\sum_{k=1}^{n-1}\frac1{1+ (\delta_k-t)y}.
\]
For fixed \(n\), the trial \(y=t^{-1/4}\) is feasible for small \(t\), makes its first term tend to \(1/(n+1)\), and makes each of the other terms tend to zero. Since \(F_{n,t}(y)\ge 1/[(n+1)(1-ty)]\ge 1/(n+1)\), the optimum tends to \(1/(n+1)\), \(x_n\to1\), and every rim-mode term at the optimum tends to zero. Hence \(y_n\to\infty\); in particular the minimum is interior for small \(t\). The equation \(F'_{n,t}(y_n)=0\) gives
\[
 \frac{t y_n^2}{(n+1)x_n^2}
 =\sum_{k=1}^{n-1}\frac{\delta_k-t}{(\delta_k+x_n/y_n)^2}
 \longrightarrow\sum_{k=1}^{n-1}\frac{1}{\delta_k}.
\]
To evaluate the latter sum, put \(\zeta_k=e^{2\pi i k/n}\) and \(P(z)=\sum_{j=0}^{n-1}z^j=\prod_{k=1}^{n-1}(z-\zeta_k)\). Then \(1/\delta_k=(1-\zeta_k)^{-1}-(1-\zeta_k)^{-2}\). At \(z=1\) the first logarithmic derivative of \(P\) is \((n-1)/2\) and its derivative is \((n-1)(n-2)/3-(n-1)^2/4\). Their sum is \((n^2-1)/12\), as required. Multiplying the limiting equation by \((n+1)x_n^2\) proves the square-root laws for \(y_n\) and \(1-x_n=t y_n\).

For fixed \(0<t<2\), the known large-wheel law [1, Finding and §3] gives \(\lim_{n\to\infty}x_n(t)=2/(4-t)\). It applies at budget \(B\) by homogeneity, since common scaling of conductances by \(B\) scales all resistances by \(1/B\) and leaves the budget fractions unchanged. It follows that taking the large-wheel limit first leaves a limiting spoke fraction of \(1/2\) as the price tends to zero. At each fixed order the stated asymptotic instead gives spoke fraction tending to one. The finite-order proof uses every nonzero rim mode tending to infinite conductance. It is not uniform as the nonzero rim eigenvalues approach zero with increasing order.

## Scope and verification

This concerns linear prices common within each edge class, a continuous conductance budget, and the total electrical resistance. The rim-deletion threshold, finite spectral objective and fixed-price large-wheel allocation are previously described in [1]; that source's boundary derivatives also yield the finite onset slope. They are not asserted as new results here. The bundled `wheel_price_verify.py` includes small exact rational Laplacian-inverse checks, and compares the predicted cheap-rim coefficient in sample sizes using floating-point bisection. The fixed-order asymptotic is proved above rather than inferred from those checks. A related weighted-wheel paper by Li, Yang and Zhang was identified bibliographically, but its full statement was not available for comparison. Historical priority is not asserted.

## References

1. *A sharp rim-price transition and critical window for resistance-optimized wheels*, Finding, Proof §§2–4. https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-a-sharp-rim-price-transition-and-critical-window-for-resistance--c2f59dd7b8a5/RESULT.md
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66, §5.2, Eq. (38), DOI: 10.1137/050645452.
