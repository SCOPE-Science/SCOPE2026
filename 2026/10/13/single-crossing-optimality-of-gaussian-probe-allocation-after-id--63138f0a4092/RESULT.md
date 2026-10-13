# Single-crossing optimality of Gaussian probe allocation after ideal spectral deflation

## Finding

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive semidefinite, with ordered eigenvalues \(\lambda_1\ge\cdots\ge\lambda_n\ge0\). Fix an integer matrix-vector-product budget \(B\) and an integer modeled per-probe cost \(m\), with \(n\ge B\ge2m\ge2\), and let \(K=\lfloor B/m\rfloor\). In the idealized spectral-preconditioner model of Cortinovis and Toni, allocating \(N\in\{1,\ldots,K\}\) independent Gaussian trace probes leaves exactly \(k_N=B-mN\) leading eigenpairs in the preconditioner. Write

\[
 a_i=\log^2(1+\lambda_i),\qquad
 F_N=\frac2N\sum_{i=k_N+1}^{n}a_i.
\]

Then \(F_N\) is the exact mean-square error of the idealized regularized log-determinant estimator. **The entire allocation profile is single-crossing:** its consecutive differences can change sign only from negative to nonnegative, never back. Thus the minimizers constitute a consecutive interval. In particular, **one probe is globally MSE-optimal among every feasible allocation if and only if it beats the two-probe allocation**. Equivalently,

\[
 \boxed{F_1\le F_2\quad\Longleftrightarrow\quad
 \sum_{i=B-2m+1}^{B-m}\log^2(1+\lambda_i)
 \ \ge\ \sum_{i=B-m+1}^{n}\log^2(1+\lambda_i).}
\]

The inequalities are strict precisely when one probe is the unique minimizer. If the inequality fails, one probe is not optimal; the exact globally optimal allocation is the first \(N\in\{1,\ldots,K-1\}\) for which

\[
 N\sum_{i=B-m(N+1)+1}^{B-mN}a_i\ \ge\
 \sum_{i=B-mN+1}^{n}a_i,
\]

or \(N=K\) if no such index exists. At equality, neighboring counts tie; all equalities are included rather than discarded.

For the motivated geometric *logarithmic* spectrum

\[
 \lambda_i=\exp\!\bigl(Cq^{(i-1)/2}\bigr)-1,
 \qquad C>0,\quad 0<q<1,
\]

one probe is globally optimal **exactly when**

\[
 \boxed{q^{-m}+q^{\,n-B+m}\ge2.}
\]

At fixed \(B,m,q\), the limiting infinite-tail boundary is the sharp transition \(q^m\le\tfrac12\). More generally, for this limit the minimizing count is \(\min\{K,\lceil (q^{-m}-1)^{-1}\rceil\}\); when \((q^{-m}-1)^{-1}\) is an integer strictly below \(K\), it ties with the next count.

## Assumptions and scope

The method is **idealized**, not a claim about an implementable Nyström or truncated-Lanczos routine: for any \(0\le k\le B-m\), the \(k\) leading eigenpairs are known exactly at nominal cost \(k\), the residual logarithmic quadratic form is computed without quadrature error at nominal cost \(m\) per Gaussian vector, and its probe vectors are independent standard real Gaussians. For \(N\) probes, the estimator is

\[
 \widehat L_N=\sum_{i=1}^{k_N}\log(1+\lambda_i)
 +\frac1N\sum_{r=1}^N\sum_{i=k_N+1}^{n}
 \log(1+\lambda_i)g_{ri}^{2},
 \qquad g_{ri}\stackrel{\mathrm{iid}}{\sim}\mathcal N(0,1).
\]

Its target is \(L=\log\det(I+A)\). All \(B,m,n,N\) are integers with the preceding bounds. Zero eigenvalues, equal eigenvalues, vanishing variance, a nondivisible budget, and ties between allocations are allowed. The discrete theorem also applies to any nonincreasing nonnegative squared spectral weights \(a_i\), independently of how those weights were obtained.

## Proof

**Gaussian error identity.** After subtracting \(L\), only terms \((g_{ri}^{2}-1)\log(1+\lambda_i)\) remain. Independence, centering and \(\operatorname{Var}(g_{ri}^{2})=2\) give exactly

\[
 \mathbb E(\widehat L_N-L)^2
 =\frac2N\sum_{i=k_N+1}^{n}\log^2(1+\lambda_i)=F_N.
\]

No inequality is used in this step.

**One crossing.** Put \(T_0=\sum_{i=B+1}^{n}a_i\) and partition the indices \(1,\ldots,B\) into consecutive blocks exposed by sacrificing \(m\) eigenpairs for each additional probe:

\[
 c_j=\sum_{i=B-mj+1}^{B-m(j-1)}a_i,
 \qquad 1\le j\le K.
\]

Every block has \(m\) terms. Because \(a_1\ge\cdots\ge a_n\ge0\), the block masses obey \(c_{j+1}\ge c_j\). For \(T_N=T_0+\sum_{j=1}^N c_j\), the Gaussian error identity reads \(F_N=2T_N/N\). Define, for \(1\le N<K\),

\[
 H_N=Nc_{N+1}-T_N.
\]

A direct subtraction gives both exact identities

\[
 F_{N+1}-F_N=\frac{2H_N}{N(N+1)},
 \qquad H_{N+1}-H_N=(N+1)(c_{N+2}-c_{N+1})\ge0
\]

(the second identity applies to \(1\le N<K-1\)). Hence the sequence of difference signs cannot change from positive to negative. The optimum therefore occurs at the first nonnegative \(H_N\), or at \(K\) if all are negative. Since \(H_1=c_2-T_1\) and \(T_1=\sum_{i=B-m+1}^n a_i\), one-probe optimality is equivalent to \(H_1\ge0\). If \(H_1>0\), every later difference is strictly positive, proving uniqueness. If \(H_1=0\), the first two allocations tie, so uniqueness fails. All other equality cases follow from the same monotone sequence.

**Exact geometric frontier.** For the stated spectrum, \(a_i=C^2q^{i-1}\). With \(k_1=B-m\), finite geometric summation gives

\[
 c_2=\frac{C^2 q^{B-2m}(1-q^m)}{1-q},
 \qquad T_1=\frac{C^2 q^{B-m}(1-q^{n-B+m})}{1-q}.
\]

The inequality \(c_2\ge T_1\) is exactly \(q^{-m}+q^{n-B+m}\ge2\). Sending \(n\) to infinity at fixed \(B,m,q\) gives the first-probe threshold \(q^m\le1/2\). Moreover,

\[
 \lim_{n\to\infty}F_N=\frac{2C^2q^{B-mN}}{N(1-q)}
\]

for every fixed feasible \(N\). The sign of its \(N\)-to-\(N+1\) difference is the sign of \(N(q^{-m}-1)-1\), yielding the claimed exact minimizing count and its tie convention. The transition is sharp: both sides occur for admissible \(q\), while taking a constant positive spectral weight with \(n>B\) instead gives \(F_N=2a(m+(n-B)/N)\), strictly improved by every additional probe and minimized at \(K\).

## Verification

Run `python3 verify.py` with the Python standard library. The program checks 3,261 exact-rational finite-spectrum allocations (including zero, flat and nondivisible-budget cases), 15,198 exact-rational objective values, and 108 exact geometric specializations. It tests both difference identities, monotonicity, all minimizing rules, the one-probe criterion, and the finite geometric sign formula. The expected output is `VERIFY_OK exact_rational_allocation_cases=3261 checked_probe_values=15198 geometric_cases=108`. These finite checks do **not** establish the universal or infinite-tail results; the preceding algebra does.

## Relationship to prior work

Cortinovis and Toni (2026), Section 2, equations (14)–(15), derive the mean-square error for an **individual** idealized allocation and compare it with the one-probe allocation for an arbitrary fixed split. Those exact pointwise formulas are credited here. The present contribution is a complete **global** optimizer classification for all integer probe counts: spectral ordering forces a single crossing, so checking only the adjacent two-probe allocation suffices to decide whether *all* other allocations are worse. The formula for the sharp geometric-log-spectrum boundary and the exact limiting number of probes are consequences of this structural result, not numerical fits. Classical Hutch++ provides randomized trace-deflation complexity results under different sampling and matrix-oracle models; its general guarantees do not supply the stated exact ordered-tail allocation law.

## Limitations

The sharp classification applies to the known-spectrum, **ideal** rank-\(k\) preconditioner and exact Gaussian quadratic forms with fixed modeled costs. It does not automatically hold for random Nyström subspaces, adaptive estimated spectra, Rademacher probes, numerical Lanczos errors, roundoff, or wall-clock optimality. The one-probe condition involves unknown true eigenvalues and is a mathematical benchmark, not a free implementable test. A broad inequality of Cortinovis and Toni covers fixed pairwise comparisons; the present theorem gives a simplified global reduction under ordered tails, not a new variance formula. An undiscovered identical single-crossing criterion is a remaining originality risk.

## References

1. A. Cortinovis and D. Toni, *Preconditioned log-determinant approximation: one Gaussian probe vector is almost always enough*, arXiv:2601.05778, first posted 2026-01-09. https://arxiv.org/abs/2601.05778
2. A. Cortinovis and D. Toni, *Detecting When One Probe Vector is Enough for Preconditioned Log-Determinant Approximation*, Numerical Linear Algebra with Applications 33 (2026), e70106. https://doi.org/10.1002/nla.70106
3. R. A. Meyer, C. Musco, C. Musco, and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, SOSA (2021), pp. 142–155. https://doi.org/10.1137/1.9781611976496.16
