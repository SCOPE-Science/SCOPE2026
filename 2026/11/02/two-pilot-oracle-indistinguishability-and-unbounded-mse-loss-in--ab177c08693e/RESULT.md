# Two-pilot oracle indistinguishability and unbounded MSE loss in log-determinant budgeting

## Finding

For every integer \(k\ge1\), two explicitly specified strictly positive diagonal matrices have **identical exact best-rank Frobenius residuals at the two pilot ranks** used in a proposed log-determinant budget-allocation test. Nonetheless, their optimal choices between a one-probe rank-\(\ell\) estimator and an equal-budget, multi-probe rank-\(\beta\ell\) estimator are opposite. No deterministic decision rule using only those two residual values, the matrix dimension, and the budget can have a finite, dimension-uniform mean-square-error (MSE) competitive ratio against the better of these two idealized estimators. This happens with \(\beta=3/4\), three Lanczos steps per probe, and \(\kappa(I+A)<5/4\).

In the ideal best-rank oracle version of the specific Frobenius switching inequality of Cortinovis and Toni, Section 4.3, the rule always selects one probe for this family. On its diffuse-tail member the exact one-probe/mixed MSE ratio is
\[
(4k+1)\left(1-\frac{1}{192k}\right),
\]
which diverges. The theorem concerns the **ideal spectral-truncation and exact-pilot model**, not the distribution of the implemented randomized Nyström/leave-one-out algorithm.

## Assumptions and scope

All matrices and vectors are real. The target is \(\operatorname{tr}\log(I+A)=\log\det(I+A)\) for symmetric positive-definite \(A\). A rank-\(r\) spectral truncation \(A_r\) retains the largest \(r\) eigenvalues; \(P_r=I+A_r\) and \(M_r=P_r^{-1/2}(I+A)P_r^{-1/2}\). An ideal probe estimator with \(s\ge1\) independent standard Gaussian vectors is
\[
T_{r,s}=\operatorname{tr}\log P_r+\frac1s\sum_{t=1}^s w_t^T\log(M_r)w_t.
\]
It is unbiased and its MSE is
\[
V_{r,s}(A)=\frac{2}{s}\sum_{i>r}\log^2(1+\lambda_i(A)). \tag{1}
\]
The two alternatives share a nominal cost of \(\ell+3\) matrix-vector products under the ideal cost accounting of the motivating work: \(T_{\ell,1}\) and \(T_{L,N}\) with \(L=3\ell/4\) and \(N=(\ell+3-L)/3\). On the matrices below, the logarithmic quadratic forms are actually exact under at most three steps of symmetric Lanczos, because the preconditioned matrices have at most three distinct eigenvalues. The ranks themselves are supplied by an exact spectral oracle, **not** inferred from three Lanczos steps.

Fix \(k\in\{1,2,\ldots\}\) and put
\[
\ell=48k,\quad J=27k,\quad L=36k,\quad h=12k,\quad p=\ell^2,\quad n=L+p,\quad N=4k+1,\quad\delta=\frac14.
\]
Write \(B_k\) for the diagonal matrix with \(L\) eigenvalues \(\delta\) followed by \(p\) eigenvalues \(\delta/\sqrt p\). For \(0<\varepsilon<p^{-1/2}\), write \(C_{k,\varepsilon}\) for the diagonal matrix with \(L\) eigenvalues \(\delta\), followed by \(h\) eigenvalues
\[
a_{k,\varepsilon}=\delta\sqrt{\frac{1-(p-h)\varepsilon^2}{h}},
\]
and then \(p-h\) eigenvalues \(b_{k,\varepsilon}=\delta\varepsilon\). All multiplicities are positive, both spectra are sorted in nonincreasing order, and \(0<\lambda_i\le\delta\). Thus \(\kappa(I+B_k),\kappa(I+C_{k,\varepsilon})<5/4\).

A **two-pilot rule** in this theorem sees only \((n,\ell,3,\|A-A_J\|_F^2,\|A-A_L\|_F^2)\) before selecting one of these two ideal estimators. The rules covered are deterministic; a randomized selector independent of the subsequent probes has the analogous obstruction as detailed in the proof.

## Proof

**Step 1: identical pilot information.** By construction, the squared Frobenius energy beyond rank \(L\) is \(\delta^2\) for both matrices, since
\[
h a_{k,\varepsilon}^2+(p-h)b_{k,\varepsilon}^2=\delta^2=p(\delta/\sqrt p)^2.
\]
The preceding \(L-J=9k\) eigenvalues all equal \(\delta\). Hence, simultaneously for \(A=B_k\) and \(A=C_{k,\varepsilon}\),
\[
\|A-A_L\|_F^2=\delta^2,\qquad
\|A-A_J\|_F^2=(9k+1)\delta^2. \tag{2}
\]
Because \(\varepsilon^2<1/p\), one has \(b_{k,\varepsilon}<a_{k,\varepsilon}<\delta\); thus these are indeed the tail errors of the **best** rank truncations, not a misordered labeling.

**Step 2: explicit diffuse-tail loss.** Since \(B_k\) has \(p\) equal tail eigenvalues, formula (1) gives
\[
V_{\ell,1}(B_k)=2(p-h)\log^2\left(1+\frac\delta{\sqrt p}\right),\qquad
V_{L,N}(B_k)=\frac{2p}{N}\log^2\left(1+\frac\delta{\sqrt p}\right).
\]
Their ratio is **exactly**
\[
\frac{V_{\ell,1}(B_k)}{V_{L,N}(B_k)}
=N\left(1-\frac hp\right)
=(4k+1)\left(1-\frac{1}{192k}\right)>1. \tag{3}
\]
It tends to infinity, so the mixed estimator is better on every diffuse member.

**Step 3: opposite concentrated-tail decision.** For \(C_{k,\varepsilon}\), truncating to rank \(\ell=L+h\) removes every larger tail eigenvalue. Formula (1) becomes
\[
V_{\ell,1}(C_{k,\varepsilon})
=2(p-h)\log^2(1+\delta\varepsilon),
\]
\[
V_{L,N}(C_{k,\varepsilon})
=\frac2N\left[h\log^2(1+a_{k,\varepsilon})+(p-h)\log^2(1+\delta\varepsilon)\right].
\]
For each fixed \(k\), the first quantity tends to zero as \(\varepsilon\downarrow0\), while the second tends to the strictly positive number \(2h\log^2(1+\delta/\sqrt h)/N\). Therefore the one-probe estimator is better for all sufficiently small \(\varepsilon\), and \(V_{L,N}/V_{\ell,1}\to\infty\).

**Step 4: indistinguishability and the switching rule.** A deterministic two-pilot rule sees exactly the same data (2) for \(B_k\) and every \(C_{k,\varepsilon}\). If it chooses the mixed estimator for some \(k\), then choosing \(\varepsilon\) arbitrarily small makes its competitive ratio arbitrarily large at that fixed \(k\). If it chooses one probe for every \(k\), its ratios (3) on \(B_k\) diverge. In either case no finite dimension-uniform competitive bound is possible. For a randomized choice based only on the same pilots and independent of trace probes, a positive probability of the mixed choice at any fixed \(k\) leads to unbounded expected risk on \(C_{k,\varepsilon}\); otherwise it chooses one with probability one for every \(k\), and (3) applies.

The ideal substitution into the motivating Section 4.3 Frobenius test (its equation (37)) selects one probe when
\[
\frac{3}{(1-3/4)(3/4)\ell+3}\|A-A_J\|_F^2
\ge\|A-A_L\|_F^2.
\]
Using (2), the left/right ratio is \((9k+1)/(3k+1)>1\), regardless of which spectrum is given. Therefore this idealized exact-pilot surrogate selects one on every \(B_k\), suffering precisely (3).

**Step 5: exact three-step quadratic forms.** On these diagonal matrices, \(M_L\) has at most three distinct eigenvalues: \(1\) and at most two values \(1+a\), \(1+b\). Likewise \(M_{\ell}\) has at most two distinct eigenvalues. The minimal-polynomial degree is thus at most three. Exact-arithmetic Lanczos tridiagonalization from any probe terminates in at most three iterations (or at an earlier invariant subspace) and evaluates \(w^T\log(M_r)w\) exactly. Consequently the variance formulas do not hide a finite-step Lanczos error on the constructed family. This observation does not certify the cost of *obtaining oracle best-rank projections* by matvecs.

## Verification

The included standalone `verification.py` checks the pilot equalities, dimension/budget arithmetic, the exact rational switching inequality, the diffuse MSE ratio, concentration reversal, eigenvalue ordering, and scale separation for 103 sample dimensions and three positive concentration parameters per sample. It also checks 1000 further exact rational parameter instances. In total **5,575 finite assertions passed**. The proof above supplies the all-\(k\) quantifiers and limiting argument; finite checks are supporting evidence only.

Reproduce with `python3 verification.py`, using the Python standard library. The verification code evaluates repeated eigenvalues by grouped multiplicity and does not allocate large dense matrices.

## Relationship to prior work

Cortinovis and Toni introduce the one-probe and mixed estimators, prove their ideal MSE identities in Section 2 (equations (11), (14), (15)), and propose a **heuristic** Frobenius pilot switching condition in Section 4.3 (equation (37)); Sections 4-5 compare it experimentally. Those identities and the definition of their heuristic are used here, not claimed as new. The new claim is the *opposite-optimum spectral pair with identical exact pilot data, its unbounded competitive-ratio implication, and the fixed-\(\beta\) explicit misallocation sequence*. Their full paper was inspected through its Sections 1-6, including the earlier ideal analysis and later experiments; no such universal impossibility statement or pair was found.

Persson, Cortinovis, and Kressner's improved Hutch++ work treats randomized trace-estimation error control and adaptation, but its general algorithms can use more information than two fixed pilot residual numbers; it does not imply this two-pilot information lower bound. General Gaussian trace-variance identities alone also do not supply the explicit indistinguishable family or the rank-allocation obstruction.

## Limitations

The matrices are diagonal, their sizes increase quadratically with the nominal rank, and their sorted tails have specially constructed degeneracies. The negative statement is only about an **information-restricted exact-pilot oracle rule** competing with two specified ideal estimators. It does not establish that a randomized Nyström approximation produces either pilot value, nor that the actual leave-one-out diagnostic, adaptive algorithm, or other information-rich selector fails with high probability. It does not assert an optimal universal allocation rule, a relative-error distribution, an end-to-end runtime lower bound, or a result for all possible preconditioners. No independent mathematical audit is asserted.

## References

1. A. Cortinovis and D. Toni, *Detecting when one probe vector is enough for preconditioned log-determinant approximation*, first public preprint 2026-01-09, arXiv:2601.05778, https://arxiv.org/abs/2601.05778; published in *Numerical Linear Algebra with Applications* (2026), https://doi.org/10.1002/nla.70106. Sections 2, 4.3 and 5 were inspected.
2. D. Persson, A. Cortinovis, and D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, *SIAM Journal on Matrix Analysis and Applications* 43 (2022), 1162–1185. https://doi.org/10.1137/21M1447623.
3. M. F. Hutchinson, *A stochastic estimator of the trace of the influence matrix for Laplacian smoothing splines*, *Communications in Statistics: Simulation and Computation* 19 (1990), 433–450. (Background variance identity.)
