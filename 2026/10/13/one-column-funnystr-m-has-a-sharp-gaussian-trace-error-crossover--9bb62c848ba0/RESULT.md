# One-column funNyström has a sharp Gaussian trace-error crossover under power iteration

## Finding

**Theorem.** Let \(\kappa>1\), integer \(q\ge 1\), and fixed \(0<\theta\le1\). Let \(A_\kappa=\operatorname{diag}(\kappa,1)\), choose a single standard real Gaussian column \(\omega=(G_1,G_2)^\top\), and form the (untruncated) one-column, \(q\)-pass Nyström approximation
\[
N_{\kappa,q}=A_\kappa^q\omega\left(\omega^\top A_\kappa^{2q-1}\omega\right)^{-1}\omega^\top A_\kappa^q.
\]
The matrix-function estimate is \(N_{\kappa,q}^{\theta}\). Its expected trace/nuclear-norm error, relative to the optimal rank-one trace error \(1\), obeys the sharp equivalent
\[
\boxed{\mathbb E\|A_\kappa^\theta-N_{\kappa,q}^\theta\|_*-1
\sim C_\theta\,\kappa^{\theta-q+1/2},\qquad
C_\theta=\frac{2\theta\,\Gamma(\theta+1/2)}{\sqrt\pi\,\Gamma(\theta+1)}.}
\]
The limit is as \(\kappa\to\infty\) with \(q,\theta\) fixed. The ratio of the two positive quantities in this equivalent tends to one, even when the excess tends to zero.

Consequently, for **one pass** (\(q=1\)), the expected error converges to the optimum \(1\) when \(0<\theta<1/2\), converges to \(1+2/\pi\) at \(\theta=1/2\), and diverges at the sharp rate \(C_\theta\kappa^{\theta-1/2}\) when \(1/2<\theta\le1\). For **at least two passes** (every fixed integer \(q\ge2\)), the expected error tends to \(1\) for the entire matrix-power range \(0<\theta\le1\), with the displayed sharp rate. At \(\theta=1\), every finite \(\kappa>1\) admits the exact identity
\[
\mathbb E\|A_\kappa-N_{\kappa,q}\|_*=1+\frac{\kappa-1}{1+\kappa^{q-1/2}}.
\]

There is a sharp nonuniform-integrability distinction: at \(q=1\), for each fixed \(0<\theta<1\), the **realized** trace error tends to \(1\) almost surely under the coupling that reuses the same Gaussian column across \(\kappa\); nevertheless its expectation has a nonoptimal limit at \(\theta=1/2\) and diverges when \(\theta>1/2\). The limiting mean defect is therefore caused by increasingly rare poorly aligned sketches, not typical sketches.

## Assumptions and scope

All calculations are in real exact arithmetic. The Gaussian coordinates are independent standard normals; the denominator is strictly positive almost surely. The underlying matrix has precisely two positive eigenvalues, one of which is normalized to \(1\). The function \(f(t)=t^\theta\) satisfies \(f(0)=0\) and is operator monotone for \(0<\theta\le1\). There is exactly one sketch column and no oversampling, column truncation, or subsequent unbiased residual correction. The integer \(q\) is the number of matrix-vector passes in the Nyström construction quoted above, not an asymptotic parameter.

## Proof

The rank-one matrix \(N_{\kappa,q}\) has unique nonzero eigenvalue
\[
\tau=\frac{\kappa^{2q}G_1^2+G_2^2}{\kappa^{2q-1}G_1^2+G_2^2}
=\kappa-\frac{\kappa-1}{1+\kappa^{2q-1}T},\qquad T=G_1^2/G_2^2.
\]
The residual \(A_\kappa-N_{\kappa,q}\) is positive semidefinite by the projector factorization \(A_\kappa^{1/2}(I-P_{A_\kappa^{q-1/2}\omega})A_\kappa^{1/2}\); operator monotonicity makes \(A_\kappa^\theta-N_{\kappa,q}^\theta\) positive semidefinite. Its nuclear norm is its trace. Since \(\operatorname{tr}(N_{\kappa,q}^\theta)=\tau^\theta\), the error is \(\kappa^\theta+1-\tau^\theta\), with excess \(\Delta=\kappa^\theta-\tau^\theta\ge0\).

The ratio of two squared independent standard Gaussians has density \(p_T(t)=1/(\pi\sqrt t(1+t))\) for \(t>0\). With \(z=\kappa^{2q-1}t\), direct change of variables gives the **exact** integral
\[
\mathbb E\Delta=\frac{\kappa^{\theta-q+1/2}}{\pi}
\int_0^\infty
\frac{1-\left(\frac{z+\kappa^{-1}}{z+1}\right)^\theta}
{\sqrt z\,(1+z/\kappa^{2q-1})}\,dz.
\]
For \(\kappa\ge1\), the integrand is nonnegative and bounded above by
\(z^{-1/2}[1-(z/(z+1))^\theta]\). This majorant is integrable: it is at most \(z^{-1/2}\) at zero and decays as \(\theta z^{-3/2}\) at infinity. Dominated convergence yields the positive asymptotic constant
\[
\frac1\pi\int_0^\infty z^{-1/2}\left[1-\left(\frac z{1+z}\right)^\theta\right]dz
=\frac{2\theta}{\pi}B(\theta+1/2,1/2)
=\frac{2\theta\Gamma(\theta+1/2)}{\sqrt\pi\Gamma(\theta+1)}.
\]
For the first equality, integrate by parts; the boundary terms vanish by the same endpoint estimates. This proves the equivalent and all its mean-error regimes. At \(\theta=1\), the elementary integral \(\mathbb E[(1+aT)^{-1}]=(1+\sqrt a)^{-1}\) (\(a>0\)) gives the finite-\(\kappa\) identity.

For the almost-sure statement, fix a realized \(T>0\) and let \(\kappa\to\infty\). Write \(\Delta=\kappa^\theta[1-(1-\varepsilon)^\theta]\) with \(\varepsilon=(1-\kappa^{-1})/(1+\kappa^{2q-1}T)\). Since \(\varepsilon\to0\), the first-order expansion gives \(\Delta\sim \theta\kappa^{\theta-2q+1}/T\), and this tends to zero whenever \(q\ge2\), \(0<\theta\le1\), or when \(q=1\), \(0<\theta<1\). At \(q=1\), \(\theta=1\), the exact expression tends instead to \(1/T\), which has infinite mean.

## Verification

Run `python verify.py` from the extracted package. It checks 100 rational equalities for the rank-one eigenvalue/residual law, 16 deterministic quadrature evaluations of the exact integral and its elementary \(\theta=1\) specialization, plus both Gamma-function endpoint constants. The observed output is `CHECKS_OK algebra=100 quadrature=16 constants=2`. All-integer \(q\) and all-real \(\theta\) follow from the proof, **not** from finite checks.

## Relationship to prior work

Persson and Kressner introduce funNyström, their formula (3), and prove bounds for operator-monotone matrix functions in Frobenius, nuclear, and spectral norms. Their nuclear-norm expectation theorem (Theorem 3.9) assumes at least two target/sketch columns and oversampling, so it does not settle the one-column, no-oversampling mean-risk regime here. Gittens and Mahoney's Theorem 4 controls the deterministic trace error of power Nyström through an alignment-dependent term; it does not evaluate its Gaussian expectation or the matrix-power transformed trace error. Their formulas and projector interpretation are used and credited here. The unpowered two-eigenvalue Gaussian residual distribution is elementary and is **not** claimed as a new distribution; the claim concerns the explicit function-exponent and power-pass trace asymptotic together with the mean-versus-typical boundary.

## Limitations

The theorem is a sharp **two-eigenvalue** result, not a dimension-free high-dimensional guarantee. It is an asymptotic in growing spectral contrast at fixed \(q,\theta\), with an additional exact identity only for \(\theta=1\). It does not cover multiple Gaussian columns, complex Gaussian probes, rounding error, or independently estimated traces. The probabilistic almost-sure statement uses a common Gaussian coupling across matrices. Although the excess can dwarf the optimal rank-one tail error, its ratio to the full input trace vanishes at growing spectral contrast; this is a failure relative to the low-rank benchmark, not relative total-trace consistency. Literature priority beyond inspected primary sources and searchable records cannot be established conclusively.

## References

1. D. Persson and D. Kressner, *Randomized low-rank approximation of monotone matrix functions*, arXiv:2209.11023, first publicly submitted 2022-09-22; full open-access text: https://arxiv.org/html/2209.11023v3 . Theorem 3.9, Lemma 3.11, and formula (3).
2. A. Gittens and M. W. Mahoney, *Revisiting the Nyström Method for Improved Large-scale Machine Learning*, Journal of Machine Learning Research **17** (2016), article 117, pp. 1–65, https://www.jmlr.org/papers/v17/gittens16a.html . Sections 2.3 and 4.1, especially Theorem 4.
