# Exact angular first-pivot risk and conditioning reversal in Gaussian-sketched QR

## Finding

For a real two-column input whose first column is strictly longer, the probability that a Gaussian sketch makes a norm-maximizing QRCP first pivot choose the *shorter* column has an exact regularized-beta law. This probability is maximal when the original columns are orthogonal and decreases as their absolute correlation grows, whereas their spectral condition number moves in the opposite direction.

For integers \(m\ge d\ge2\), a real matrix \(A=[u\ v]\in\mathbb R^{m\times2}\), and a Gaussian sketch \(S\in\mathbb R^{d\times m}\), let
\[
\kappa=\frac{\|u\|_2}{\|v\|_2}>1,\quad
\rho=\frac{u^\top v}{\|u\|_2\|v\|_2},\quad
\Delta=\sqrt{(\kappa^2+1)^2-4\kappa^2\rho^2},\quad
z=\frac12\left(1-\frac{\kappa^2-1}{\Delta}\right).
\]
The probability that the first norm-maximizing QR column pivot applied to \(SA\) selects \(v\) equals
\[
\boxed{\Pr\{\|Sv\|_2>\|Su\|_2\}= I_z(d/2,d/2)},
\]
where \(I_z(a,a)\) is the regularized incomplete-beta function; by continuity its value is zero at \(|\rho|=1\). For \(0\le|\rho|<1\), the event of a tie has probability zero. The exact maximal risk at a fixed \(\kappa,d\) is
\[
\boxed{I_{1/(1+\kappa^2)}(d/2,d/2)},
\]
achieved precisely at orthogonality. In contrast, the two-column spectral condition number increases strictly with \(|\rho|\) until it diverges as \(|\rho|\to1\). For fixed \(\kappa>1\) and \(|\rho|<1\), the large-sketch sharp asymptotic is
\[
\boxed{\Pr\{\text{shorter column pivoted first}\}\sim
\frac{[4z(1-z)]^{d/2}}{(1-2z)\sqrt{2\pi d}}}
\qquad (d\to\infty).
\]

## Assumptions and scope

All computations are in exact real arithmetic. The columns \(u,v\) are nonzero, with \(\|u\|_2>\|v\|_2\), and \(m\ge d\ge2\). Entries of \(S\) are independent centered Gaussian variables of variance \(1/d\), and the pivot compares squared Euclidean norms of the two columns of \(SA\) before any orthogonalization or updates. This is exactly the first norm-maximizing QRCP decision in the Gaussian sketch stage of the column-pivoted CholeskyQR procedure; no assertion concerns the full factorization or subsequent pivots. The parameter \(\rho\) may be negative, and the formulas depend only on \(|\rho|\). The asymptotic holds with \(\kappa,\rho\) fixed and \(d\to\infty\), along dimensions \(m\ge d\) in which columns with these Gram parameters exist. The parallel case \(|\rho|=1\) is included in the exact formula but not in the stated asymptotic.

## Proof

Normalize \(\|v\|_2=1\) by common scaling. A row of \(\sqrt d\, SA\) is a centered Gaussian pair with covariance
\[
\Sigma=\begin{pmatrix}\kappa^2&\kappa\rho\\\kappa\rho&1\end{pmatrix}.
\]
For each row, the difference of squared coordinates has the law of the quadratic form associated with \(\Sigma^{1/2}\operatorname{diag}(1,-1)\Sigma^{1/2}\). Its positive eigenvalue is \(\lambda_+=(\Delta+\kappa^2-1)/2\); its negative eigenvalue is \(-\gamma\), with \(\gamma=(\Delta-\kappa^2+1)/2\ge0\). By a single orthogonal rotation, summing independently across \(d\) rows yields
\[
\|Su\|_2^2-\|Sv\|_2^2\ \stackrel{\mathrm{law}}{=}
\frac1d\bigl(\lambda_+X-\gamma Y\bigr),
\]
with \(X,Y\) independent chi-square variables of \(d\) degrees of freedom each. If \(|\rho|<1\), both coefficients are positive, so the shorter column wins exactly when
\[
\frac{X}{X+Y}<\frac{\gamma}{\lambda_++\gamma}=z.
\]
The ratio is beta-distributed with equal parameters \(d/2\), giving the asserted exact law. For \(|\rho|=1\), \(\gamma=0\), and since \(\kappa>1\), the longer column wins almost surely.

Since \(\Delta\) decreases strictly with \(|\rho|\) until the parallel endpoint, \(z=[1-(\kappa^2-1)/\Delta]/2\) also decreases strictly. Since the beta density is positive on \((0,1)\), the mispivot probability decreases strictly. At \(\rho=0\), \(\Delta=\kappa^2+1\), hence \(z=1/(1+\kappa^2)\). The nonzero eigenvalues of \(A^\top A\) are
\[
\frac{\kappa^2+1\pm\sqrt{(\kappa^2-1)^2+4\kappa^2\rho^2}}2;
\]
therefore their ratio, and the spectral condition number of \(A\), increase strictly with \(|\rho|\); at the parallel endpoint the matrix has rank one and infinite condition number.

Finally, write \(a=d/2\) and fix \(z\in(0,1/2)\). Endpoint Laplace asymptotics, differentiating \(\log[t(1-t)]\), gives
\[
\int_0^z t^{a-1}(1-t)^{a-1}\,dt
\sim \frac{[z(1-z)]^a}{a(1-2z)}.
\]
Stirling's formula gives \(B(a,a)\sim2\sqrt\pi\,4^{-a}/\sqrt a\). Division yields exactly the stated probability asymptotic. These are analytic identities for all allowed real correlations, not inferences from finite enumeration.

## Verification

For \(\kappa=2\) and \(d=2\), at \(\rho=0\), the formula gives \(z=1/5\) and mispivot probability \(1/5\). At \(\rho=3/4\), it gives \(z=1/8\) and mispivot probability \(1/8\), although the original condition number is larger. At \(d=4\), the corresponding probabilities are \(13/125\) and \(11/256\). The standalone script `verify.py` checks these using exact fractions, checks the strict angle comparison for eight even sketch dimensions, evaluates two asymptotic comparisons, and performs four seeded Monte Carlo checks with sixty thousand trials each. Run with `python3 verify.py`; success prints `VERIFY_OK`. The finite checks are supplemental; the proof is the Gaussian diagonalization and beta-ratio identity above.

## Relationship to prior work

Melnichenko and collaborators' CholeskyQR with Randomization and Pivoting (CQRRPT; arXiv:2311.08316, first public in November 2023) sketches the input and applies column-pivoted QR to that sketch. Its analysis concerns norm and rank-revealing guarantees rather than this exact first-pivot selection probability. Duersch and Gu's earlier randomized QR with column pivoting (arXiv:1509.06820) already used Gaussian sketches, studied marginal sketch-length distributions and sample-column dependence, and supplied qualitative observations about correlations; that shared primitive is not asserted to be new here. Xiao, Gu, and Langou (arXiv:1804.05138) established high-probability pseudo-diagonal-dominance properties of randomized QRCP, not an equality law at fixed column angle. The new comparison distinguishes the exact joint Gaussian selection law from existing bounds and marginal distribution facts. General beta/chi-square identities are standard and are used as proof ingredients, not claimed as new discoveries.

## Limitations

The result covers only the *first* two-way norm-maximizing pivot in an idealized exact-arithmetic Gaussian sketch, not the error of a complete QR or CholeskyQR factorization. It does not imply that highly correlated columns are numerically preferable or that Gaussian sketches improve ill-conditioned least-squares problems. The positive-probability mispivot event does not show numerical instability. A stronger or unindexed exact two-column Gaussian norm-comparison theorem could subsume this special application; publication priority has not been independently established.

## References

1. Melnichenko and collaborators, *CholeskyQR with Randomization and Pivoting for Tall Matrices*, arXiv:2311.08316 (first public version 2023-11-14), Sections 2.1–2.3 and rank-revealing appendix.
2. Duersch and Gu, *Randomized QR with Column Pivoting*, arXiv:1509.06820 (2015), Sections 3–3.3.
3. Xiao, Gu, and Langou, *Fast Parallel Randomized QR with Column Pivoting Algorithms for Reliable Low-Rank Matrix Approximations*, arXiv:1804.05138 (2018), Section III and associated results.
4. Martinsson, *Blocked rank-revealing QR factorizations: How randomized sampling can be used to avoid single-vector pivoting*, arXiv:1505.08115 (2015).
