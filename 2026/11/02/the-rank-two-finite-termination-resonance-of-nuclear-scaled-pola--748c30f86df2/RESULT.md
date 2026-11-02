# The rank-two finite-termination resonance of nuclear-scaled polar descent

## Finding

Consider the nuclear-scaled polar-gradient update on the isotropic matrix quadratic
\[
f(X)=\frac{\lambda}{2}\|X-X_*\|_{\mathrm F}^2,\qquad \lambda>0,
\]
with the exact thin-SVD polar factor. **Theorem (complete rank classification).** Let \(m,n\geq1\), \(1\leq r\leq\min(m,n)\), and take every nonzero initial error \(E_0=X_0-X_*\in\mathbb R^{m\times n}\) of rank exactly \(r\). At each nonstationary step, choose the *exact line-search* step size along the nuclear-scaled polar direction.

1. If \(r=1\), every such error is eliminated in one step.
2. If \(r=2\), every such error is eliminated in at most two steps. Equal initial singular values give one-step termination; unequal positive singular values give **exactly two** steps.
3. For every \(r\geq3\), there are rank-\(r\) errors that never vanish at any finite step. Indeed, initial positive singular values proportional to \((1,\ldots,1,r-1)\) remain in those same proportions and decrease by the exact factor \((r-2)/r\) at each step.

This is a sharp classification: if instead the normalized step size \(t=\alpha\lambda>0\) is held constant, a fixed \(t\) achieves finite termination **from every rank-\(r\) initialization** if and only if \(r=1,t=1\) or \(r=2,t=1/2\); no such \(t\) exists for \(r\geq3\).

Moreover, the two-step rank-two resonance is discontinuous under rank-raising perturbations. For the exact-line-search map \(T\) in dimension three, put \(E_0=\operatorname{diag}(3,1,0)\) and \(E_\varepsilon=\operatorname{diag}(3,1,\varepsilon)\), \(\varepsilon>0\). Then
\[
\lim_{\varepsilon\downarrow0}\|T(E_\varepsilon)-T(E_0)\|_{\mathrm F}=\sqrt{\frac83}>0.
\]
The theorem concerns the **exact finite-iteration dynamics**, not just asymptotic convergence.

## Assumptions and scope

Work over real matrices, with arbitrary rectangular dimensions \(m,n\) and deterministic data. Let \(E=X-X_*\), \(G=\nabla f(X)=\lambda E\), and for a thin singular-value decomposition \(G=U\operatorname{diag}(\gamma_1,\ldots,\gamma_s)V^\top\), \(\gamma_i>0\), define
\[
\operatorname{polar}(G)=UV^\top,\qquad
\Phi(G)=\|G\|_*\operatorname{polar}(G),\qquad
\Phi(0)=0.
\]
The iteration is \(E_{k+1}=E_k-\alpha_k\Phi(\lambda E_k)\). Exact line search minimizes \(f(X_k-\alpha\Phi(G_k))\) over \(\alpha\geq0\) at each nonzero iterate. For the constant-step statement, \(\alpha_k=t/\lambda\) for all \(k\). A trajectory terminates if and only if \(E_k=0\) for some finite \(k\). No SVD truncation, momentum, stochastic noise, finite-precision rounding or approximate polar oracle is included.

## Proof

**Singular-value recursion.** For a nonzero error \(E=U\operatorname{diag}(s_1,\ldots,s_q)V^\top\) with all \(s_i>0\) and \(S=\sum_{i=1}^q s_i\), the gradient has nuclear norm \(\lambda S\) and polar factor \(UV^\top\). Therefore
\[
E_+=U\operatorname{diag}(s_1-tS,\ldots,s_q-tS)V^\top,
\qquad t=\alpha\lambda.
\tag{1}
\]
Its nonzero singular values are the nonzero entries of \((|s_i-tS|)_{i=1}^q\). Directions in the null singular subspaces remain zero, and ranks may decrease but never increase. Formula (1) is an identity for arbitrary rectangular matrices, not a diagonal-matrix approximation.

**Exact line-search normalization.** The search direction \(D=\Phi(\lambda E)=\lambda S UV^\top\) has
\[
\langle E,D\rangle_{\mathrm F}=\lambda S^2,
\qquad \|D\|_{\mathrm F}^2=\lambda^2S^2q.
\]
The minimizer of \(\|E-\alpha D\|_{\mathrm F}^2\) is consequently
\[
\alpha_*(E)=\frac{\langle E,D\rangle_{\mathrm F}}{\|D\|_{\mathrm F}^2}
=\frac{1}{\lambda q},\qquad t_* =\frac1q.
\tag{2}
\]
Thus line search subtracts the mean \(S/q\) from every active signed singular value.

**Ranks one and two.** At rank one, (1) with \(t_*=1\) gives \(E_+=0\). At rank two, write \(s_1,s_2>0\). Inserting \(t_*=1/2\) into (1) gives the signed coefficients
\[
\frac{s_1-s_2}{2},\qquad\frac{s_2-s_1}{2}.
\]
If \(s_1=s_2\), both vanish immediately. Otherwise the updated error has rank two and its two singular values both equal \(|s_1-s_2|/2\). Applying (2) a second time uses the same normalized step \(1/2\), which subtracts precisely that common singular value and gives \(E_2=0\). Since the first error is nonzero when \(s_1\ne s_2\), two steps are then necessary.

**All higher ranks admit a nonterminating ray.** Fix \(r\geq3\), put \(c=(r-2)/r\in(0,1)\), and start with any matrix of rank \(r\) whose singular values are \(a(1,\ldots,1,r-1)\), for \(a>0\). Their sum is \(2a(r-1)\), so subtracting \(S/r\) produces \(r-1\) signed coefficients \(-ac\) and one \(a(r-1)c\). Hence all updated singular values equal the originals multiplied by \(c\), and all remain strictly positive. This computation iterates inductively; after \(k\) steps every singular value is its starting value times \(c^k>0\). Thus the trajectory converges geometrically but never terminates at a finite index.

**Necessity of the constant step.** Suppose some \(t>0\) terminates every error of rank exactly \(r\). Choose a rank-\(r\) matrix with all \(r\) singular values equal to \(a>0\). Formula (1) shows that each update is exactly \((1-rt)E\), hence this trajectory reaches zero at a finite step only if \(t=1/r\). At this only possible value, the rank-one and rank-two proofs establish universal finite termination, whereas the preceding nonterminating ray excludes every \(r\geq3\). This proves both necessity and sufficiency.

**Discontinuity at a rank change.** In three dimensions, exact line search uses \(t=1/2\) at \(E_0=\operatorname{diag}(3,1,0)\), giving \(T(E_0)=\operatorname{diag}(1,-1,0)\). At \(E_\varepsilon=\operatorname{diag}(3,1,\varepsilon)\), use \(t=1/3\), and hence
\[
T(E_\varepsilon)=\operatorname{diag}\left(3-\frac{4+\varepsilon}{3},\ 1-\frac{4+\varepsilon}{3},\ \varepsilon-\frac{4+\varepsilon}{3}\right).
\]
Subtracting \(T(E_0)\) and taking \(\varepsilon\downarrow0\) gives diagonal entries \((2/3,2/3,-4/3)\), whose squared Frobenius norm is \(8/3\). All claims follow. \(\square\)

## Verification

The standalone script `verify.py` (Python 3, NumPy) runs exact rational-arithmetic checks of the rank-two identity for 1,600 pairs of positive integer singular values, tests higher-rank invariant rays and equal-singular-value obstructions using rational arithmetic, and checks 3,000 randomly oriented rectangular rank-two matrices through direct SVD updates. It separately tests both perturbation formulations. Executing `python verify.py` yields `PASS: 7401 independent finite arithmetic/matrix checks`. The proof above supplies the universal quantifiers; finite computations do not certify those infinitely many cases.

## Relationship to prior work

Jawanpuria, Garai, and Mishra (2026), Theorem 3 and Appendix C, give a general constant-step linear convergence bound for nuclear-scaled polar updates, an exact one-step objective identity, and invariant directions with equal active singular values. Their Proposition 8 yields **one-step** termination of certain equal-spectrum inputs at a resonant step. It does not give the arbitrary-rank-two **two-step** theorem, the across-rank impossibility classification, or the line-search rank-discontinuity formula above. The present proof uses their exact update model, not a different optimizer.

Lau, Long, and Su (2025, initially public May 27), §3.3 and Theorem 3.2, introduce PolarGrad and analyze rank-dependent convergence under a rank-calibrated step. That expected descent mechanism is compatible with, but does not state, the finite-termination dichotomy. Gonon, Muşat, and Boumal (2026) study grid confinement of the **unscaled** polar direction and approximation error; nuclear-norm scaling changes the homogeneous dynamics. Related results about finite termination of singular-value thresholding concern a different, additive soft-thresholding map rather than the coupled mean shift in (1).

## Limitations

The complete classification holds for an isotropic quadratic and an *exact* polar factor and line search. It does not claim the same behavior for anisotropic Hessians, rank-truncated or approximate polar factors, finite-precision singular values, arbitrary nonquadratic objectives, or matrices that change shape. The rank discontinuity explicitly warns that the two-step behavior is not uniformly robust under small rank-increasing perturbations. Historical priority beyond the inspected literature and semantic research-record comparisons has not been independently established.

## References

1. P. Jawanpuria, B. Garai, B. Mishra, *Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics*, arXiv:2610.27747v1 (first public October 20, 2026), especially Theorem 3, Appendix C Proposition 8 and Remark 2. https://arxiv.org/html/2610.27747v1
2. T. T.-K. Lau, Q. Long, W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, arXiv:2505.21799v4 (first public May 27, 2025), especially §3.3 and Theorem 3.2. https://arxiv.org/html/2505.21799v4
3. A. Gonon, A.-A. Muşat, N. Boumal, *Insights on Muon from Simple Quadratics*, arXiv:2602.11948v1 (first public February 12, 2026), especially §§3–4. https://arxiv.org/html/2602.11948v1
