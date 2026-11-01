# Scientific assessment

## Correctness

For the printed SIRS model's diagonal diffusion coefficients \(g_i(x)=-q_i x\), one has \(g_i g_i'=q_i^2x\). The coefficient of \(((\Delta W_i)^2-h)\) must therefore be positive in the Milstein method specified by Higham (2001), Eq. (6.1), whereas Eq. (4.3) of Huang, Du and Liang (2026) prints a negative coefficient.

On the exactly solvable scalar benchmark \(dX=-qX\,dW\), the negative-sign update has exact mean-square error
\[
X_0^2\big[(1+r+r^2/2)^N+e^{Nr}-2(1+r-r^2/2)^N\big],\quad r=q^2T/N,
\]
which is asymptotic to \(2X_0^2e^{q^2T}q^4Th\), giving root-mean-square order one-half. The correctly signed update has error \(X_0^2[e^{Nr}-(1+r+r^2/2)^N]\), asymptotic to \(X_0^2e^{q^2T}q^6Th^2/6\), giving order one. Both statements follow from exact Gaussian moments and independence, not from fitted slopes.

## Originality and context

Higham's classical formula already determines the proper sign. The bounded contribution is the specific printed-formula discrepancy and its exact finite-step quantitative consequence, rather than a novel SDE solver. Previously published analyses of the same SIRS paper concern stochastic covariance and the disease-free boundary, not numerical Eq. (4.3). A related published Milstein-measles discrepancy concerns a different drift term. No covering publication or erratum was identified in the inspected sources; priority is necessarily a best-of-knowledge statement.

## Significance and limitations

The sign reverses the term responsible for improving strong convergence on the canonical multiplicative-noise equation. The result is relevant to numerical reproducibility, but no unpublished implementation was examined, so it cannot establish which scheme produced any particular figure. The full nonlinear SIRS recurrence was not proved to have global strong order one-half; the exact rate calculation pertains only to the scalar test.

## Primary references

Huang, Du and Liang, *AIMS Mathematics* 11 (2026), 6720–6743, DOI:10.3934/math.2026278, Section 4 and Eq. (4.3). Higham, *SIAM Review* 43 (2001), 525–546, DOI:10.1137/S0036144500378302, Sections 5–6 and Eq. (6.1).
