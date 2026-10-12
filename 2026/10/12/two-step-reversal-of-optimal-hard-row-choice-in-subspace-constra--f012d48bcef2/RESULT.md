# Two-step reversal of optimal hard-row choice in subspace-constrained randomized Kaczmarz

## Finding

For a nonsingular real square linear system, fix one equation exactly and apply the subspace-constrained randomized Kaczmarz (SCRK) update with independent projected-row-norm sampling among the remaining equations. Define the finite-horizon minimax expected squared error after \(t\) updates by
\[
L_i(t)=\sup_{\substack{e_0\perp a_i\\\|e_0\|_2=1}}\mathbb E\|e_t\|_2^2,
\]
where \(a_i\) is the fixed row (viewed as a column). In the nonsingular integer system
\[
A=\begin{pmatrix}-2&-1&3\\-1&0&-3\\0&-2&1\end{pmatrix},\qquad\det A=17,
\]
the unique best fixed row is **row 1 at one update** but **row 3 at two updates**:
\[
L_1(1)<L_3(1)<L_2(1),\qquad L_3(2)<L_1(2)<L_2(2).
\]
Moreover, row 3 has the uniquely smallest asymptotic worst-case expected-error rate \(\lim_{t\to\infty}L_i(t)^{1/t}\). This strict reversal persists on an open neighborhood of \(A\) among real nonsingular \(3\times3\) matrices. Dimension three is the smallest square-system dimension in which a strict one-versus-two-update reversal can occur when exactly one row is fixed and all remaining rows are sampled.

## Assumptions and scope

Take any invertible real \(3\times3\) matrix with rows \(a_1^\top,a_2^\top,a_3^\top\). For a chosen hard row \(i\), put \(P_i=I-a_ia_i^\top/\|a_i\|_2^2\). Initially the solution error \(e_0=x^0-x_*\) satisfies \(P_ie_0=e_0\). If \(j,k\) are the other row indices, independently select \(h\in\{j,k\}\) at each step with probability proportional to \(\|P_ia_h\|_2^2\), and update
\[
e_{t+1}=e_t-\frac{\langle P_ia_h,e_t\rangle}{\|P_ia_h\|_2^2}P_ia_h.
\]
This is the exact, unrelaxed SCRK update with one perpetually enforced equation, not the accelerated Krylov variant. The minimax supremum ranges over all unit initial errors in the hard-row nullspace, equivalently over compatible normalized right-hand sides with suitable consistent initialization. It is **not** a comparison for a single common right-hand side and fixed starting vector. Expectations are with respect to the fresh independent row choices, and \(L_i(t)\) measures squared Euclidean solution error, not residual norm.

## Proof

**Exact two-row reduction.** Write \(u=P_ia_j\), \(v=P_ia_k\), \(a=\|u\|_2^2>0\), \(b=\|v\|_2^2>0\), \(d=\langle u,v\rangle\), and define
\[
p=\frac{a}{a+b},\qquad q=1-p,\qquad z=\frac{d^2}{ab}\in[0,1).
\]
The residual plane \(\operatorname{ran}P_i\) has dimension two. Its orthogonal projectors \(T\) and \(U\) onto the lines perpendicular to \(u\) and \(v\) satisfy
\[
T^2=T,\quad U^2=U,\quad TUT=zT,\quad UTU=zU.
\]
Let \(M_t\) be the self-adjoint mean-square propagator defined by \(\mathbb E\|e_t\|_2^2=\langle e_0,M_te_0\rangle\) for \(e_0\) in the residual plane. Independence yields \(M_0=I\), \(M_{t+1}=pTM_tT+qUM_tU\), and \(L_i(t)=\lambda_{\max}(M_t|_{\operatorname{ran}P_i})\).

For \(t=1\), \(M_1=pT+qU\), whose trace and determinant on that plane are \(1\) and \(pq(1-z)\). Hence
\[
L_i(1)=\frac{1+\sqrt{1-4pq(1-z)}}2.
\]
For \(t=2\), the projection identities give
\[
M_2=\alpha T+\beta U,\qquad
\alpha=p^2+pqz,\quad\beta=q^2+pqz,
\]
with trace \(\alpha+\beta\) and determinant \(\alpha\beta(1-z)\). Thus
\[
L_i(2)=\frac{\alpha+\beta+\sqrt{(\alpha-\beta)^2+4\alpha\beta z}}2.
\]
For \(t\ge1\), writing \(M_t=c_tT+d_tU\) gives the exact coefficient recursion
\[
\begin{pmatrix}c_{t+1}\\d_{t+1}\end{pmatrix}=
\begin{pmatrix}p&pz\\qz&q\end{pmatrix}
\begin{pmatrix}c_t\\d_t\end{pmatrix}.
\]
For \(0<z<1\), its matrix is strictly positive and its Perron root is
\[
\rho(p,z)=\frac{1+\sqrt{(p-q)^2+4pqz^2}}2.
\]
The coefficient vector starts strictly positive and the rank-one line projectors are nonzero, so the Perron theorem implies \(\lim_{t\to\infty}L_i(t)^{1/t}=\rho(p,z)\).

**Exact integer witness.** The Gram matrix is
\[
AA^\top=\begin{pmatrix}14&-7&5\\-7&10&-3\\5&-3&5\end{pmatrix}.
\]
Applying the formulas to each fixed row yields the following exact parameters and minimax values:

| Fixed row \(i\) | \(p\) | \(z\) | \(L_i(1)\) | \(L_i(2)\) | \(\rho_i\) |
| --- | --- | --- | --- | --- | --- |
| 1 | \(91/136\) | \(7/585\) | \(1/2+\sqrt2/8\) | \(9/32+\sqrt{45487}/1248\) | \(1/2+\sqrt{4355}/390\) |
| 2 | \(91/132\) | \(841/3731\) | \(1/2+\sqrt{1466}/132\) | \(2911/8712+\sqrt{331034466539}/2500344\) | \(1/2+\sqrt{314974751}/82082\) |
| 3 | \(45/86\) | \(80/369\) | \(1/2+\sqrt{101}/43\) | \(2253/7396+\sqrt{1062490646}/227427\) | \(1/2+\sqrt{343129}/5289\) |

The following strict *rational* bounds certify the orderings without relying on rounded decimals. Multiply every entry by \(10^{-4}\):

| Fixed row | Interval for \(L_i(1)\) | Interval for \(L_i(2)\) | Interval for \(\rho_i\) |
| --- | --- | --- | --- |
| 1 | \((6767,6768)\) | \((4521,4522)\) | \((6692,6693)\) |
| 2 | \((7900,7901)\) | \((5642,5643)\) | \((7162,7163)\) |
| 3 | \((7337,7338)\) | \((4479,4480)\) | \((6107,6108)\) |

Every bound follows by isolating the positive radical and squaring the two rational sides, as reproduced by the exact checker. Consequently all asserted inequalities are strict. Since projected lengths, correlations, and these eigenvalues are continuous near invertible matrices, the strict inequalities survive sufficiently small matrix perturbations.

**Minimal square-system dimension.** In an invertible \(2\times2\) system, imposing one nonzero hard row leaves a one-dimensional feasible error space. The sole remaining independent projected row annihilates that error after its first update. Thus each possible hard-row choice has zero minimax error at every positive horizon, ruling out strict reversal in dimension two; dimension one is also trivial. The displayed dimension-three witness is therefore minimal within square systems with one fixed row.

## Verification

Run `python verify.py` with `sympy` installed (`requirements.txt`). The script independently computes the exact projected row Gram parameters from the integer matrix, constructs both residual-space projectors as \(3\times3\) rational matrices, checks idempotence and the alternating-projection identities, forms both full one- and two-step expectation operators, and verifies their characteristic invariants and the Perron-root equations. It proves the stated rational enclosures as exact inequalities of quadratic radicals and prints `VERIFY_OK`. The analytic argument establishes the general formulas and minimality; the executable checks establish the witness with exact arithmetic.

## Relationship to prior work

Lok and Rebrova (arXiv:2309.04889, 2023) introduced SCRK and its projected-norm row distribution and proved a convergence-rate bound. Sun, Qi, Han, and Xie (arXiv:2605.29304v1, May 28, 2026), notably Remark 3.1 and Section 3.2, extend subspace-constrained preconditioning and propose fixed-subsystem selection guided by spectral rate criteria and practical surrogates. Neither inspected primary treatment supplies the strict *one-step versus two-step best-hard-row reversal* above.

Agaskar, Wang, and Lu (2014) give a general exact moment-operator formula for randomized Kaczmarz and a spectral long-time optimization over *sampling probabilities*. That general formula can compute the present individual finite-time quantities after specialization: the operator formalism and the projection reduction are not claimed as novel. What is newly established here is an explicit invertible integer witness that optimizers over **which equation is held exact** reverse as the iteration horizon changes, and the dimension-minimal, open-set character of that reversal. This claim is distinct from optimizing probabilities on a fixed row collection; no uniqueness of the fact in all literature is asserted.

## Limitations

This is a worst-initial-error result for the one-hard-row, projected-row-norm SCRK specialization on nonsingular square systems. It is not a theorem about a common fixed right-hand side across all hard-row choices, and does not compare typical errors, finite-precision implementations, total computational costs of enforcing a hard row, or the source paper's accelerated methods. The exact formulas derive from classical linear-algebra and randomized-projection machinery; broader previously published operator formulas can reproduce them. An equivalent earlier row-choice reversal may exist in unindexed literature. There is no independent audit.

## References

1. Y. Sun, H.-D. Qi, D. Han, J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1 (2026-05-28), https://arxiv.org/html/2605.29304.
2. J. Lok, E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889v2 (2024 revision of a 2023 preprint), https://arxiv.org/pdf/2309.04889.
3. A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities* (2014), https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content.
