# Mathematical assessment

## Correctness
PASS. For exactly equal feedback coefficients \(k_0=m=s>0\), direct differentiation of
\[
V=\frac12\left(x^2+y^2+\frac{s}{k}u^2\right)
\]
yields \(\dot V=-(a x^2-2hxy+b y^2)\). When \(h^2<ab\), the right-hand quadratic form is positive definite, so \(x,y,u\) stay bounded. The stable forced scalar equation for \(z\) prevents blow-up and gives a precompact positive orbit. LaSalle's principle puts every omega-limit set on \(x=y=0\), which forces \(u=0\); then \(\dot z=-dz\), so every trajectory converges to the origin. A separate small-data estimate for the stable \(z\) equation establishes Lyapunov stability.

For a compactly supported invariant probability measure, integrating the generator identity gives the exact moment law \(a\langle x^2\rangle+b\langle y^2\rangle=2h\langle xy\rangle\); positive definiteness forces \(x=y=0\) almost surely. Invariance forces \(u=0\), and stationarity of \(z^2\) forces \(z=0\). Thus the origin's Dirac measure is the only compact invariant probability law in the claimed strict region. Algebraic checking corroborates the derivative identity but does not replace LaSalle's argument.

## Originality
PASS, best of current knowledge, not an assertion of guaranteed historical priority. The full published introducing paper by Li and Cui, *A hyperchaos generated from Rabinovich system* (DOI 10.3934/math.2023071), uses exactly this vector field. Its Theorem 2.1 requires \(k_0>m\) and bounds a region; its Theorem 2.2 is a local spectral result; and its numerical cases use \(k_0=m=0.8\) outside the present strict stability region. Its stated Hopf hypothesis is incompatible with \(k_0=m\) and \(h^2<ab\), but that observation alone does not imply global attraction.

The complete Wei–Yu–Zhang–Yao preprint (DOI 10.1007/s11071-015-2144-8) and the accessible author version of Liu's synchronization paper (DOI 10.1007/s11071-011-9960-2) describe an auxiliary term in the second state equation, not equal feedback in both first two equations. Their bounds and synchronization results do not imply the claimed all-data theorem. The published Cui–Li Qi-derived equilibrium correction also concerns a different four-dimensional field. An exact public mirror of this very claim is not independent earlier coverage.

Residual risk: the complete Liu–Yang–Pang et al. 2010 paper (DOI 10.1016/j.cam.2009.12.008) could not be examined; its indexed abstract and the 2022 paper's explicit lineage discussion were checked. Equivalent short Lyapunov arguments may exist in less searchable dynamical-systems or control literature.

## Mathematical value
PASS. The equality \(k_0=m\) is a natural feedback regime explicitly used in the introducing article's simulations, but excluded from its boundedness theorem. The analytic global-attraction conclusion and universal compact-recurrence exclusion are sharper than local eigenvalue stability or trajectory sampling for this model. The result is a parameter-specific nonlinear certificate; it does not classify the critical surface \(h^2=ab\), unequal feedback, or dynamics above the necessary recurrence barrier.
