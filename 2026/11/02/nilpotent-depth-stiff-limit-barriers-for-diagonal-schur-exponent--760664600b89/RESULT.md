# Nilpotent-depth stiff-limit barriers for diagonal-Schur exponential time stepping

## Finding

For a strictly dissipative, nonnormal Jordan-chain test family, diagonal-Schur exponential Euler and the standard two-stage ETD2 corrector remain entrywise nonnegative and strict Euclidean contractions at every positive step, yet retain an exactly quantifiable error when the stiffness tends to infinity at a fixed step. The first method retains one nilpotent edge per step; the second retains two. For each fixed positive integer \(k\), the limiting operator-norm errors are precisely \(\rho^k\) when \(k<d\) for exponential Euler and \(\rho^{2k}\) when \(2k<d\) for ETD2, and zero otherwise. Moreover, when \(\lceil d/2\rceil\le k<d\), putting \(m=2k-d+1\) gives the sharp algebraic ETD2 residual limit \(\lim_{\kappa\to\infty}(\kappa h)^m\|E_2(\kappa h)^k-X(\kappa h)^k\|_2=\binom{k}{m}\rho^{d-1}\). Thus the smallest dimensions with a nonvanishing one-step stiff-limit defect are \(d=2\) and \(d=3\), respectively.

## Assumptions and scope

Fix an integer \(d\ge1\), a coupling fraction \(0<\rho<1\), a time step \(h>0\), and a stiffness \(\kappa>0\). Let \(J_d\in\mathbb R^{d\times d}\) have entries \((J_d)_{i,i+1}=1\) for \(1\le i<d\) and all other entries zero. Thus \(J_d^d=0\) and, for integers \(0\le j<d\), \(\|J_d^j\|_2=1\). Consider

\[
\dot y=-L_\kappa y,\qquad L_\kappa=\kappa(I-\rho J_d).
\]

The family is uniformly strongly dissipative in the scale \(\kappa\): for every real vector \(v\),

\[
\langle v,L_\kappa v\rangle\ge\kappa(1-\rho)\|v\|_2^2.
\]

This matrix is itself in real upper-triangular Schur form. Split its negative into a scalar diagonal linear part and an explicit off-diagonal residual, \(\dot y=-\kappa y+g_\kappa(y)\) with \(g_\kappa(y)=\kappa\rho J_d y\). Write \(z=\kappa h\), \(a=e^{-z}\), \(p=1-e^{-z}\), and the usual entire functions \(\varphi_1(w)=(e^w-1)/w\), \(\varphi_2(w)=(e^w-1-w)/w^2\), continued at zero.

Define the one-stage exponential Euler update \(E_1(z)\) by \(y^+=a y+h\varphi_1(-z)g_\kappa(y)\). Define the two-stage ETD2 predictor and corrector by

\[
Y=a y+h\varphi_1(-z)g_\kappa(y),\qquad
 y^+=a y+h[\varphi_1(-z)-\varphi_2(-z)]g_\kappa(y)+h\varphi_2(-z)g_\kappa(Y).
\]

The exact step is \(X(z)=e^{-hL_\kappa}\). All errors below are induced Euclidean (spectral) matrix norms; the initial vector is arbitrary. In the stiff limit, \(d,\rho,h,k\) are held fixed while \(\kappa\to+\infty\).

## Proof

**Step 1: exact formulas.** The nilpotency of \(J_d\) and its commutation with \(I\) give

\[
X(z)=e^{-z}\sum_{j=0}^{d-1}\frac{(\rho z)^j}{j!}J_d^j.
\]

Set \(u=p^2/z\) and \(v=p(z-p)/z\). Since \(z>0\) and \(0<p<z\), we have \(u>0\), \(v>0\), and \(u+v=p\). Substituting \(\varphi_1(-z)=p/z\) and \(\varphi_2(-z)=(z-p)/z^2\) directly into the two algorithm definitions yields

\[
\boxed{E_1(z)=aI+\rho pJ_d,\qquad E_2(z)=aI+\rho uJ_d+\rho^2vJ_d^2.}
\]

For the second identity, \(g_\kappa(Y)=\kappa\rho J_d(aI+\rho pJ_d)y\). The coefficient of \(J_d\) is \(\rho[p-zp\varphi_2(-z)]=\rho p^2/z\); the coefficient of \(J_d^2\) is \(\rho^2zp\varphi_2(-z)=\rho^2p(z-p)/z\). These are exact identities for every dimension, stiffness and step.

**Step 2: positivity, contraction, and dissipativity.** Both matrices \(E_i(z)\) are entrywise nonnegative. A row or column of \(E_1\) has sum at most \(a+\rho p<1\). A row or column of \(E_2\) has sum at most \(a+\rho u+\rho^2v<a+u+v=a+p=1\). Therefore their induced \(1\)- and \(\infty\)-norms are strictly less than one and \(\|E_i(z)\|_2\le\sqrt{\|E_i(z)\|_1\|E_i(z)\|_\infty}<1\). The symmetric part of the generator satisfies \((L_\kappa+L_\kappa^{\mathsf T})/2=\kappa[I-\rho(J_d+J_d^{\mathsf T})/2]\succeq\kappa(1-\rho)I\), because \(\|J_d\|_2\le1\). Thus the underlying dynamics also have strict Euclidean decay; neither instability nor positivity loss explains the limiting numerical defect.

**Step 3: stiff limits.** As \(z\to+\infty\), \(a\to0\), \(p\to1\), \(u\to0\), and \(v\to1\). Hence

\[
E_1(z)\longrightarrow\rho J_d,\qquad E_2(z)\longrightarrow\rho^2J_d^2,\qquad X(z)\longrightarrow0.
\]

The last assertion holds because each term of the finite exact exponential sum is a polynomial in \(z\) multiplied by \(e^{-z}\). Matrix multiplication is continuous in fixed finite dimension, so for every fixed integer \(k\ge1\),

\[
\lim_{\kappa\to\infty}\|E_1(\kappa h)^k-X(\kappa h)^k\|_2=\rho^k\|J_d^k\|_2,
\]

\[
\lim_{\kappa\to\infty}\|E_2(\kappa h)^k-X(\kappa h)^k\|_2=\rho^{2k}\|J_d^{2k}\|_2.
\]

The nilpotent shift \(J_d^j\) maps \(e_{j+1}\) to \(e_1\) for \(j<d\), is a partial isometry of norm one for \(0\le j<d\), and vanishes for \(j\ge d\). This proves the exact piecewise limits. The first nonzero stiff-limit one-step defect consequently requires \(d\ge2\) for exponential Euler, and \(d\ge3\) for ETD2. The vanishings after \(k\ge d\) or \(2k\ge d\) concern the *fixed-horizon stiff limit*, not exact equality of numerical and true matrices at any finite \(z\).

**Step 4: a sharp algebraic residue after the ETD2 depth cutoff.** Suppose \(\lceil d/2\rceil\le k<d\) and set \(m=2k-d+1\), so \(1\le m\le k\). All three terms of \(E_2(z)\) commute. In the expansion of \(E_2(z)^k\), terms containing the scalar factor \(a=e^{-z}\) are exponentially small after multiplication by any fixed power of \(z\). Terms without \(a\), with precisely \(t\) copies of \(\rho uJ_d\) and \(k-t\) copies of \(\rho^2vJ_d^2\), have matrix degree \(2k-t\). They vanish by nilpotency unless \(t\ge m\). At the least surviving value \(t=m\), the coefficient is

\[
\binom{k}{m}\rho^{2k-m}u^m v^{k-m}J_d^{d-1}.
\]

Since \(zu\to1\), \(v\to1\), \(2k-m=d-1\), and all surviving terms with \(t>m\) have strictly higher inverse powers of \(z\),

\[
\boxed{\lim_{\kappa\to\infty}(\kappa h)^m\|E_2(\kappa h)^k-X(\kappa h)^k\|_2=\binom{k}{m}\rho^{d-1}.}
\]

The exact propagator has exponentially small matrix powers, and \(\|J_d^{d-1}\|_2=1\), so the limiting constant is sharp. Hence a vanishing unscaled ETD2 defect need not be exponentially small in stiffness: it can have precisely algebraic decay at and beyond the nilpotent-depth crossing.

**Step 5: consistency at fixed stiffness.**

Expanding around \(z=0\) gives \(E_1(z)-X(z)=O(z^2)\) and \(E_2(z)-X(z)=O(z^3)\) for each fixed \(d,\rho\), with constants allowed to depend on \(\kappa\) when reexpressed in \(h\). Thus the stiff-limit barrier is compatible with conventional local orders one and two and does not imply a failure of convergence as \(h\to0\) at fixed \(\kappa\).

## Verification

Run `python verify.py` under Python 3.10 or later; only the standard library is needed. The standalone script independently constructs the method stages on basis vectors and compares them with the closed forms, compares the exact propagator with its finite exponential-polynomial series, checks nonnegative row and column sums, tests matrix powers, limiting shifts and algebraic post-threshold residues across dimensions and parameters, and checks fixed-stiffness small-step local orders. It reports `PASS: 2838 deterministic arithmetic and structural checks`. These are finite arithmetic tests, not a substitute for the exact argument in the Proof section.

## Relationship to prior work

Zoto and Bowman introduce the computational motivation for diagonal Schur exponential stepping, including the separation of diagonal exponentiation and explicit upper-triangular coupling; their 2023 paper discusses possible additional errors from such a decomposition. The present result isolates a concrete all-dimensions nonnormal, strongly dissipative test class and gives *exact* dimension- and step-count-dependent stiff-limit defects for two specified steppers, a statement not supplied by its examined Schur-splitting discussion.

Hochbruck and Ostermann give general stiff-order conditions and convergence theory for exponential Runge–Kutta integrators in a semilinear setting. Their results assume appropriate regularity and controls for the residual forcing; here the explicit residual derivative is \(\kappa\rho J_d\), so its Lipschitz constant scales with stiffness. Those general estimates neither imply nor contradict the exact singular-family limits proved here. Jordan–Schur full-matrix exponential algorithms treat all triangular couplings within the matrix function and are a different computational operation from diagonal-only exponentiation.

## Limitations

The theorem concerns a diagonal-Schur split of a finite-dimensional nilpotent chain and specifically the two steppers defined above. It does not classify all exponential Runge–Kutta methods, establish computational cost advantages, or prove that a particular adaptive-error controller chooses any fixed step. Its sharpness is in the fixed-step, finite-iterate, large-stiffness limit with \(0<\rho<1\) and fixed dimension; the vanishing limit for some small dimensions is not a uniform-in-stiffness error estimate. Other Schur splittings and matrix-exponential methods can behave differently. No claim of independent validation or exhaustive publication priority is made.

## References

1. T. Zoto and J. C. Bowman, *Schur Decomposition for Stiff Differential Equations*, arXiv:2305.12488v1, first public 2023-05-21. https://arxiv.org/abs/2305.12488
2. M. Hochbruck and A. Ostermann, *Explicit Exponential Runge–Kutta Methods for Semilinear Parabolic Problems*, SIAM Journal on Numerical Analysis 43 (2005), 1069–1090, DOI:10.1137/040611434. Authorized author full text: https://na.math.kit.edu/download/papers/rkexp.pdf
3. A. Petkov, *Jordan–Schur Algorithms for Computing the Matrix Exponential*, 2023, DOI:10.1155/2023/4908185. https://onlinelibrary.wiley.com/doi/10.1155/2023/4908185
