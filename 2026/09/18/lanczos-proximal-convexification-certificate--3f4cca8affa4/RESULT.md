# Sharp certification boundary for Lanczos-based proximal convexification

## Result

Consider a real symmetric matrix \(Q\), let
\[
\beta=\max\{1,\|Q\|_\infty\},
\]
and consider the proximal shift used in Eq. (11) of Chen--Lu (2026),
\[
s:=\gamma^{-1}=-\widehat\lambda+\delta\beta,
\qquad \delta>0,
\]
where \(\widehat\lambda\) is an estimate of the smallest eigenvalue produced by Lanczos iterations. Their base convergence hypothesis requires
\[
Q+sI\succ0.
\]

If \(Q\) is indefinite and \(\widehat\lambda=\theta\) is the usual smallest Rayleigh--Ritz value from a Lanczos Krylov subspace, then
\[
\boxed{\lambda_{\min}(Q+sI)
=\delta\beta-\bigl(\theta-\lambda_{\min}(Q)\bigr).}
\]
Consequently the shift strongly convexifies the inner quadratic **if and only if**
\[
\boxed{\theta-\lambda_{\min}(Q)<\delta\beta.}
\]
Thus the safety term \(\delta\beta\) is exactly an allowed additive Ritz overestimate; it is not, by itself, a certificate of strong convexity.

For the paper's \(\delta=10^{-2}\), finite-step Lanczos does not provide this certificate in general. More strongly, for every prescribed finite Krylov dimension \(m\ge1\), there is a diagonal indefinite matrix and an open set of starting vectors for which the returned smallest Ritz value gives \(\gamma>0\) but leaves \(Q+\gamma^{-1}I\) indefinite.

Finally, if no accuracy information about the Ritz value is used beyond the Rayleigh--Ritz enclosure, then the rule above has the sharp uniform safety threshold
\[
\boxed{\delta>2.}
\]
That threshold is intentionally conservative; a certified lower spectral bound gives a much tighter repair.

## Source interface

PDNQP treats linearly constrained QPs with possibly indefinite \(Q\). Its proximal ALM derivation explicitly assumes
\[
Q+\gamma^{-1}I\succ0
\]
so that the inner subproblem is strongly convex. The convergence discussion imports the QPALM guarantees under the same hypothesis.

The practical initialization then states that \(\gamma\) is chosen to convexify the inner QPs and sets
\[
\gamma=
\frac{1}{
-\widehat\lambda_Q+\delta_\gamma\max\{1,\|Q\|_\infty\}},
\qquad \delta_\gamma=10^{-2},
\]
where \(\widehat\lambda_Q\) is described as an estimate of the smallest eigenvalue obtained by Lanczos iterations. No certified lower-bound condition or a posteriori inequality implying
\(Q+\gamma^{-1}I\succ0\) is stated there.

This record concerns the mathematical rule as stated. If an implementation uses an additional certified spectral lower bound or a safeguard not described in the paper, that implementation is outside the counterexample.

## Exact criterion

Let \(\lambda_*=\lambda_{\min}(Q)<0\), and let \(\theta\) be a smallest Ritz value. Rayleigh--Ritz gives
\[
\theta\ge\lambda_*.
\]
With \(s=-\theta+\delta\beta\),
\[
\lambda_{\min}(Q+sI)
=\lambda_*-\theta+\delta\beta
=\delta\beta-(\theta-\lambda_*).
\]
Hence \(Q+sI\succ0\) exactly when
\[
\theta-\lambda_*<\delta\beta.
\]
When this inequality holds, \(s>-\lambda_*>0\), so \(\gamma=1/s\) is also positive.

The quantity \(\theta-\lambda_*\) is therefore the only spectral error that matters for this convexification step. A finite Ritz computation supplies an upper approximation \(\theta\ge\lambda_*\), whereas safe proximal regularization needs control in the opposite direction.

## A finite-step counterexample for every Krylov budget

Fix
\[
0<\delta<1,\qquad m\ge1,
\]
and define the \((m+1)\times(m+1)\) diagonal matrix
\[
Q_m=
\operatorname{diag}\!\left(
-1,\frac{\delta}{m+1},\frac{2\delta}{m+1},
\dots,\frac{m\delta}{m+1}
\right).
\]
Then
\[
\|Q_m\|_\infty=1,\qquad \beta=1,\qquad
\lambda_{\min}(Q_m)=-1.
\]

Choose the normalized starting vector
\[
v_0=
\left(0,\frac1{\sqrt m},\dots,\frac1{\sqrt m}\right)^\top.
\]
Its first coordinate is zero, so the Krylov space remains inside the positive invariant block. Since the positive eigenvalues are distinct and every corresponding coordinate of \(v_0\) is nonzero, the \(m\times m\) Krylov matrix on that block is a diagonally scaled Vandermonde matrix and has full rank. Therefore after \(m\) Lanczos steps the Krylov space is exactly the whole positive block, and its smallest Ritz value is
\[
\theta_m=\frac{\delta}{m+1}.
\]
The practical shift is positive:
\[
s_m
=-\theta_m+\delta
=\frac{m\delta}{m+1}>0,
\]
but the true smallest eigenvalue after shifting is
\[
\lambda_{\min}(Q_m+s_mI)
=
-1+\frac{m\delta}{m+1}
< -1+\delta<0.
\]
Thus the purportedly convexified inner Hessian is still indefinite.

### The failure is not confined to exact orthogonality

Let
\[
K_m(v)=[v,Q_mv,\dots,Q_m^{m-1}v].
\]
At \(v=v_0\), \(K_m(v_0)\) has full column rank. Full rank persists in a neighborhood of \(v_0\), and the orthogonal projector onto
\(\operatorname{range}K_m(v)\) therefore depends continuously on \(v\) there. The smallest Ritz value of the compressed symmetric operator is continuous as well.

At \(v_0\), both inequalities
\[
s_m>0,\qquad
\lambda_{\min}(Q_m+s_mI)<0
\]
are strict. Hence they remain true on some open neighborhood of \(v_0\) on the unit sphere. That neighborhood contains vectors with nonzero component in the \(-1\) eigendirection and has positive surface measure. Thus, for any fixed finite Lanczos budget, random continuous starts do not turn the stated rule into a deterministic or probability-one convexification certificate.

For the paper's \(\delta=10^{-2}\) and \(m=4\), one exact instance is
\[
Q=\operatorname{diag}
\left(-1,\frac1{500},\frac1{250},\frac3{500},\frac1{125}\right),
\quad
v_0=(0,\tfrac12,\tfrac12,\tfrac12,\tfrac12)^\top.
\]
The four-step smallest Ritz value is \(1/500\), so
\[
\gamma^{-1}
=\frac1{100}-\frac1{500}
=\frac1{125}>0,
\]
but
\[
\boxed{\lambda_{\min}(Q+\gamma^{-1}I)=-\frac{124}{125}.}
\]

## Sharp uniform safety factor when only a Ritz value is known

Suppose \(\theta\) is an arbitrary Ritz value of a real symmetric \(Q\), and retain
\[
\beta=\max\{1,\|Q\|_\infty\}.
\]
Because \(Q\) is symmetric,
\[
\|Q\|_2\le\|Q\|_\infty\le\beta,
\]
and every Ritz value satisfies
\[
-\beta\le\lambda_{\min}(Q)\le\theta\le\lambda_{\max}(Q)\le\beta.
\]
Therefore
\[
\lambda_{\min}(Q-\theta I+\delta\beta I)
\ge(\delta-2)\beta.
\]
Also
\[
-\theta+\delta\beta\ge(\delta-1)\beta.
\]
Hence every such Ritz estimate yields a positive proximal parameter and a positive-definite shifted Hessian whenever
\[
\boxed{\delta>2.}
\]

This threshold is sharp for a guarantee that uses no information beyond “\(\theta\) is a Ritz value” and the norm bound:

- For \(0<\delta\le1\), take \(Q=\operatorname{diag}(-1,0)\) and the Ritz subspace \(\operatorname{span}\{e_2\}\). Then \(\theta=0\), the denominator is positive, but the shifted minimum is \(-1+\delta\le0\).
- For \(1<\delta\le2\), take \(Q=\operatorname{diag}(-1,1)\) and the Ritz subspace \(\operatorname{span}\{e_2\}\). Then \(\theta=1\), the denominator is positive, but the shifted minimum is \(\delta-2\le0\).

Thus \(\delta>2\) is necessary and sufficient for an unconditional strict-positivity guarantee of this formula class. This is not a recommendation to replace \(10^{-2}\) by a number above \(2\); such a shift can be needlessly large.

## A certified factorization-free repair

A tighter repair is to use any genuine lower bound
\[
\ell\le\lambda_{\min}(Q)
\]
and set, for an arbitrary margin \(\eta>0\),
\[
s_{\rm cert}
=
\max\{0,-\ell\}+\eta\beta,
\qquad
\gamma_{\rm cert}=s_{\rm cert}^{-1}.
\]
Then
\[
\lambda_{\min}(Q+s_{\rm cert}I)\ge\eta\beta>0.
\]

One inexpensive choice is the Gershgorin lower bound
\[
\ell_G
=
\min_i\left(
q_{ii}-\sum_{j\ne i}|q_{ij}|
\right).
\]
It is standard that \(\ell_G\le\lambda_{\min}(Q)\). Computing it requires rowwise absolute sums and diagonal entries; the same type of row reduction is already needed for \(\|Q\|_\infty\). Moreover
\[
\ell_G\ge-\|Q\|_\infty,
\]
so this certificate is never more conservative than the norm-only shift
\((1+\eta)\beta\).

A practical hybrid is
\[
s=\max\{
-\theta+\delta\beta,\;
\max(0,-\ell_G)+\eta\beta
\},
\]
which preserves the heuristic shift when it is already large enough while making strong convexity explicit.

## Relation to prior work

The underlying warning that an extreme Ritz value need not yet approximate the corresponding extreme eigenvalue is classical. Van Dorsselaer, Hochstenbach, and van der Vorst explicitly studied Lanczos “misconvergence” and probabilistic extreme-eigenvalue bounds, noting that even small Ritz residuals do not by themselves ensure closeness to the extreme eigenvalue. That classical phenomenon is not claimed as new here.

QPALM, on which PDNQP bases its outer convergence argument, separately devotes an eigenvalue routine to producing what it calls a lower bound on the minimum eigenvalue before choosing the proximal penalty. This makes spectral certification part of the pre-existing solver design, although the details and guarantees of that eigenvalue routine are separate from the present claim.

The contribution here is the PDNQP-specific interface analysis: the exact error budget hidden in Eq. (11), a counterexample for every finite Lanczos budget together with an open-set robustness statement, the sharp norm-only safety threshold \(\delta>2\), and an explicit factorization-free certified repair. Searches over the PDNQP title, arXiv identifier, Lanczos convexification, Ritz-value proximal regularization, and related formulations found no public correction or prior statement of this result as of the publication date.

## Limitations

1. The counterexample assumes that “estimate by Lanczos iterations” means the standard smallest Rayleigh--Ritz value of the finite Krylov subspace. If the actual implementation returns a certified lower bound on \(\lambda_{\min}(Q)\), the counterexample does not apply to that implementation.
2. No public PDNQP implementation repository was identified from the paper or the literature search, so undocumented safeguards were not inspected.
3. This result does not show that the reported PDNQP experiments fail, nor that the outer method diverges whenever the shift is insufficient. It shows that the stated practical initialization does not, by itself, establish the strong-convexity hypothesis used by the base theory.
4. The \(\delta>2\) threshold is sharp only for the deliberately information-poor rule class that knows an arbitrary Ritz value and \(\beta\); much smaller certified shifts are possible with additional spectral information.
5. The Gershgorin repair is a correctness certificate, not a claim of optimal conditioning. Tighter certified spectral lower bounds may materially improve performance.

## Reproducibility

`artifacts/verify_pdnqp_shift.py` uses exact rational arithmetic from the Python standard library to verify the explicit \(m=4\) counterexample, the sharp-threshold witnesses, and the Gershgorin repair. `artifacts/verified_output.txt` records its executed output.

## References

- Z. Chen and H. Lu, *PDNQP: A GPU-based Factorization-free Method for Large-scale Nonconvex Quadratic Programming*, arXiv:2609.19557v1, 2026. https://arxiv.org/abs/2609.19557v1
- B. Hermans, A. Themelis, and P. Patrinos, *QPALM: A Proximal Augmented Lagrangian Method for Nonconvex Quadratic Programs*, Mathematical Programming Computation 14 (2022), 497--541; arXiv:2010.02653v2. https://arxiv.org/abs/2010.02653v2
- J. L. M. van Dorsselaer, M. E. Hochstenbach, and H. A. van der Vorst, *Computing Probabilistic Bounds for Extreme Eigenvalues of Symmetric Matrices with the Lanczos Method*, SIAM J. Matrix Anal. Appl. 22(3), 837--852. https://doi.org/10.1137/S0895479800366859
